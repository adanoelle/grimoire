"""
Interactive CLI menu for kata practice.

Provides a user-friendly interface for selecting katas, running tests,
and managing practice sessions without memorizing justfile commands.
"""

import os
import subprocess
from datetime import date
from pathlib import Path
from typing import Optional

import questionary
from questionary import Style
from rich.console import Console
from rich.table import Table

from ..utils.discovery import find_all_kata_patterns, find_kata_pattern
from ..utils.mastery import parse_mastery_log, get_practice_summary, append_practice_session
from ..utils.timer import PracticeTimer
from ..utils.rendering import console, print_error, print_info, print_success, print_warning
from . import test_cmd, list_cmd, reset_cmd


# Custom questionary style matching grimoire theme
grimoire_style = Style([
    ('qmark', 'fg:#ff00ff bold'),           # Question mark (magenta)
    ('question', 'bold'),                    # Question text
    ('answer', 'fg:#00ff00 bold'),          # Selected answer (green)
    ('pointer', 'fg:#ff00ff bold'),         # Selection pointer (magenta)
    ('highlighted', 'fg:#ff00ff bold'),     # Highlighted choice
    ('selected', 'fg:#00ff00'),             # Multi-select checked (green)
    ('separator', 'fg:#555555'),            # Separator lines
    ('instruction', 'fg:#888888'),          # Instructions
    ('text', ''),                           # Default text
])


def run_interactive_menu():
    """Main entry point for interactive kata menu."""
    console.print("\n[bold magenta]🥋 Kata Practice Menu[/bold magenta]\n")

    while True:
        choice = show_main_menu()

        if choice == "Practice Kata":
            handle_practice_flow()
        elif choice == "Run Tests":
            handle_test_flow()
        elif choice == "View Progress":
            handle_progress_flow()
        elif choice == "Reset Kata":
            handle_reset_flow()
        elif choice == "Quit":
            console.print("\n[dim]Happy practicing! 🎯[/dim]\n")
            break


def show_main_menu() -> str:
    """Display main menu and get user choice."""
    choices = [
        "Practice Kata",
        "Run Tests",
        "View Progress",
        "Reset Kata",
        "Quit",
    ]

    return questionary.select(
        "What would you like to do?",
        choices=choices,
        style=grimoire_style,
        instruction="(Use arrow keys)"
    ).ask()


# ============================================================================
# PRACTICE FLOW
# ============================================================================

def handle_practice_flow():
    """Handle pattern selection -> open in editor with timer -> log session."""
    # Get all patterns with mastery data
    patterns = find_all_kata_patterns()
    if not patterns:
        print_error("No kata patterns found!")
        return

    # Build pattern choices with status display
    pattern_choices = []
    pattern_map = {}

    for pattern in patterns:
        display_text = format_pattern_for_menu(pattern)
        pattern_choices.append(display_text)
        pattern_map[display_text] = pattern

    # Add back option
    pattern_choices.append("← Back to main menu")

    # Show selection
    selected = questionary.select(
        "\nSelect a pattern to practice:",
        choices=pattern_choices,
        style=grimoire_style,
        instruction="(Arrow keys to navigate, Enter to select)"
    ).ask()

    if selected == "← Back to main menu" or not selected:
        return

    pattern = pattern_map[selected]

    # Open in editor with automatic timer
    console.print(f"\n[bold]🥋 Opening {pattern.display_name}[/bold]")
    console.print(f"[dim]File: {pattern.kata_file}[/dim]")
    console.print(f"[dim]⏱️  Timer will start when editor opens...[/dim]\n")

    # Determine editor (prefer $EDITOR, fallback to common editors)
    editor = os.environ.get('EDITOR', 'vim')

    # Start timer and open editor
    timer = PracticeTimer()
    timer.start()

    editor_success = False
    try:
        subprocess.run([editor, str(pattern.kata_file)])
        editor_success = True
    except FileNotFoundError:
        # Try fallback editors
        for fallback in ['vim', 'vi', 'nano']:
            try:
                subprocess.run([fallback, str(pattern.kata_file)])
                editor_success = True
                break
            except FileNotFoundError:
                continue

        if not editor_success:
            timer.stop()  # Stop timer since editor failed
            print_error(f"Could not find editor. Please set $EDITOR or install vim/nano")
            console.print(f"\n[dim]File location: {pattern.kata_file}[/dim]\n")
            return

    # Stop timer after editor closes
    timer.stop()

    # Show elapsed time
    console.print(f"\n[bold green]✓ Finished practicing![/bold green]")
    console.print(f"[bold]⏱️  Time: {timer.elapsed_formatted}[/bold]\n")

    # Ask if user wants to run tests first (to see bugs before logging)
    try:
        run_tests_now = questionary.confirm(
            "Would you like to run tests?",
            default=True,
            style=grimoire_style,
        ).ask()

        if run_tests_now and pattern.has_pytest:
            # Ask which kata to test
            kata_to_test = questionary.select(
                "Which kata would you like to test?",
                choices=["All katas", "Kata 1", "Kata 2", "Kata 3", "Kata 4", "Kata 5"],
                style=grimoire_style,
            ).ask()

            if kata_to_test:
                kata_num = None if kata_to_test == "All katas" else int(kata_to_test.split()[-1])

                # Run tests (delegates to test_cmd)
                try:
                    test_cmd.run_tests(pattern.name, kata_number=kata_num, verbose=False)
                except Exception as e:
                    print_warning(f"Could not run tests: {e}")

                console.print()  # Add spacing after test output
        elif run_tests_now and not pattern.has_pytest:
            print_warning(f"{pattern.display_name} uses legacy doctest. Run manually: python {pattern.kata_file.name}")
            console.print()

    except KeyboardInterrupt:
        console.print("\n[dim]Cancelled.[/dim]\n")
        return

    # Now ask if user wants to log this session
    try:
        log_session = questionary.confirm(
            "Would you like to log this practice session?",
            default=True,
            style=grimoire_style,
        ).ask()

        if not log_session:
            console.print("[dim]Session not logged.[/dim]\n")
            return

        # Prompt for kata number
        kata_number = questionary.select(
            "Which kata did you practice?",
            choices=["Kata 1", "Kata 2", "Kata 3", "Kata 4", "Kata 5"],
            style=grimoire_style,
        ).ask()

        if not kata_number:
            console.print("[dim]Logging cancelled.[/dim]\n")
            return

        # Extract number from "Kata X"
        kata_num = int(kata_number.split()[-1])

        # Prompt for bugs
        bugs_input = questionary.text(
            "How many bugs did you encounter?",
            default="0",
            style=grimoire_style,
        ).ask()

        if bugs_input is None:
            console.print("[dim]Logging cancelled.[/dim]\n")
            return

        try:
            bugs = int(bugs_input)
        except ValueError:
            bugs = 0

        # Prompt for notes (optional)
        notes = questionary.text(
            "Notes (optional, press Enter to skip):",
            default="",
            style=grimoire_style,
        ).ask()

        if notes is None:
            notes = ""

        # Log the session
        result = append_practice_session(
            pattern.kata_file,
            kata_number=kata_num,
            time_str=timer.elapsed_formatted,
            bugs=bugs,
            notes=notes,
        )

        if result.is_failure():
            error = result.error
            print_error(f"Could not log practice session: {error.message}")
            console.print(f"[dim]You can log manually: runes kata log {pattern.name} {kata_num} {timer.elapsed_formatted} -b {bugs}[/dim]\n")
            return

        # Success!
        print_success(f"✓ Session logged!")
        console.print(f"[dim]{pattern.display_name} - Kata {kata_num} - {timer.elapsed_formatted} - {bugs} bugs[/dim]")
        console.print(f"\n[dim]Next steps:[/dim]")
        console.print(f"[dim]  • Run tests: runes kata test {pattern.name}[/dim]")
        console.print(f"[dim]  • View progress: runes kata progress {pattern.name}[/dim]")
        console.print(f"[dim]  • Reset pattern: runes kata reset {pattern.name}[/dim]\n")

    except KeyboardInterrupt:
        console.print("\n[dim]Logging cancelled.[/dim]\n")
        return


def format_pattern_for_menu(pattern) -> str:
    """Format pattern with mastery status for menu display."""
    # Try to parse mastery log
    log_result = parse_mastery_log(pattern.kata_file)

    if log_result.is_success():
        log = log_result.unwrap()
        summary = get_practice_summary(log)

        # Format status with color
        status = log.status.value
        if status == "Mastered":
            status_display = f"[green]{status}[/green]"
        elif status == "Practicing":
            status_display = f"[yellow]{status}[/yellow]"
        else:
            status_display = f"[dim]{status}[/dim]"

        # Format last practice
        last_practice = summary.get("last_practice")
        if last_practice:
            days_ago = (date.today() - last_practice).days
            if days_ago == 0:
                last_str = "today"
            elif days_ago == 1:
                last_str = "yesterday"
            else:
                last_str = f"{days_ago}d ago"
        else:
            last_str = "never"

        # Format best time for kata 1
        best_times = summary.get("best_times", {})
        best_time_str = format_time_seconds(best_times.get(1)) if best_times else "-"

        return f"{pattern.display_name:40} [{status:12}]  Last: {last_str:10}  Best: {best_time_str}"
    else:
        # Fallback if can't parse log
        return f"{pattern.display_name:40} [Unknown]"


def format_time_seconds(seconds: Optional[int]) -> str:
    """Format seconds as M:SS."""
    if seconds is None:
        return "-"
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins}:{secs:02d}"


# ============================================================================
# TEST FLOW
# ============================================================================

def handle_test_flow():
    """Handle pattern selection -> test filter selection -> run tests."""
    # Get all patterns
    patterns = find_all_kata_patterns()
    if not patterns:
        print_error("No kata patterns found!")
        return

    # Build choices
    pattern_choices = [p.display_name for p in patterns]
    pattern_choices.append("← Back to main menu")
    pattern_map = {p.display_name: p for p in patterns}

    # Select pattern
    selected = questionary.select(
        "\nSelect a pattern to test:",
        choices=pattern_choices,
        style=grimoire_style,
    ).ask()

    if selected == "← Back to main menu" or not selected:
        return

    pattern = pattern_map[selected]

    # Check if pattern has pytest tests
    if not pattern.has_pytest:
        print_error(f"{pattern.display_name} hasn't been migrated to pytest yet")
        console.print("[dim]Run tests manually or migrate to pytest first.[/dim]\n")
        return

    # Select test filter
    test_filter = select_test_filter(pattern)
    if not test_filter:
        return

    # Run tests
    run_pattern_tests(pattern, test_filter)


def select_test_filter(pattern) -> Optional[dict]:
    """Select which tests to run."""
    choices = [
        "Run All Tests",
        "Kata 1 Tests Only",
        "Kata 2 Tests Only",
        "Kata 3 Tests Only",
        "Kata 4 Tests Only",
        "Kata 5 Tests Only",
        "LeetCode Examples Only",
        "Edge Cases Only",
        "Property Tests Only",
        "← Back",
    ]

    selected = questionary.select(
        f"\nWhich tests for {pattern.display_name}?",
        choices=choices,
        style=grimoire_style,
    ).ask()

    if selected == "← Back" or not selected:
        return None

    # Map selection to pytest args
    filter_map = {
        "Run All Tests": {"args": [], "description": "all tests"},
        "Kata 1 Tests Only": {"args": ["-m", "kata1"], "description": "kata 1 tests"},
        "Kata 2 Tests Only": {"args": ["-m", "kata2"], "description": "kata 2 tests"},
        "Kata 3 Tests Only": {"args": ["-m", "kata3"], "description": "kata 3 tests"},
        "Kata 4 Tests Only": {"args": ["-m", "kata4"], "description": "kata 4 tests"},
        "Kata 5 Tests Only": {"args": ["-m", "kata5"], "description": "kata 5 tests"},
        "LeetCode Examples Only": {"args": ["-k", "examples"], "description": "LeetCode examples"},
        "Edge Cases Only": {"args": ["-k", "edge"], "description": "edge cases"},
        "Property Tests Only": {"args": ["-k", "Properties"], "description": "property tests"},
    }

    return filter_map[selected]


def run_pattern_tests(pattern, test_filter: dict):
    """Run pytest with selected filters."""
    console.print(f"\n[bold]Running {test_filter['description']} for {pattern.display_name}...[/bold]\n")

    test_file = pattern.test_file
    cmd = ["pytest", str(test_file), "-v"] + test_filter["args"]

    try:
        subprocess.run(cmd, check=False)
    except Exception as e:
        print_error(f"Failed to run tests: {e}")


# ============================================================================
# PROGRESS FLOW
# ============================================================================

def handle_progress_flow():
    """Show progress overview or detailed pattern view."""
    choices = [
        "View All Patterns (Table)",
        "View Specific Pattern (Detailed)",
        "← Back to main menu",
    ]

    selected = questionary.select(
        "\nProgress view:",
        choices=choices,
        style=grimoire_style,
    ).ask()

    if selected == "View All Patterns (Table)":
        # Use existing list command
        console.print()
        list_cmd.list_patterns()
        console.print()
    elif selected == "View Specific Pattern (Detailed)":
        show_pattern_details()


def show_pattern_details():
    """Show detailed progress for a specific pattern."""
    patterns = find_all_kata_patterns()
    if not patterns:
        print_error("No kata patterns found!")
        return

    pattern_choices = [p.display_name for p in patterns]
    pattern_choices.append("← Back")
    pattern_map = {p.display_name: p for p in patterns}

    selected = questionary.select(
        "\nSelect pattern for detailed view:",
        choices=pattern_choices,
        style=grimoire_style,
    ).ask()

    if selected == "← Back" or not selected:
        return

    pattern = pattern_map[selected]
    display_pattern_details(pattern)


def display_pattern_details(pattern):
    """Display detailed mastery information for a pattern."""
    console.print(f"\n[bold magenta]{pattern.display_name}[/bold magenta]\n")

    log_result = parse_mastery_log(pattern.kata_file)

    if not log_result.is_success():
        console.print("[yellow]No practice log found for this pattern.[/yellow]\n")
        return

    log = log_result.unwrap()
    summary = get_practice_summary(log)

    # Create table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Total Sessions", str(summary.get("total_sessions", 0)))
    table.add_row("Mastery Status", log.status.value)

    last_practice = summary.get("last_practice")
    if last_practice:
        days_ago = (date.today() - last_practice).days
        table.add_row("Last Practice", f"{last_practice} ({days_ago} days ago)")
    else:
        table.add_row("Last Practice", "Never")

    # Best times per kata
    best_times = summary.get("best_times", {})
    for kata_num in sorted(best_times.keys()):
        time_str = format_time_seconds(best_times[kata_num])
        table.add_row(f"Best Time (Kata {kata_num})", time_str)

    # Total bugs
    total_bugs = summary.get("total_bugs", {})
    for kata_num in sorted(total_bugs.keys()):
        bug_count = total_bugs[kata_num]
        table.add_row(f"Total Bugs (Kata {kata_num})", str(bug_count))

    console.print(table)
    console.print()


# ============================================================================
# RESET FLOW
# ============================================================================

def handle_reset_flow():
    """Handle pattern selection -> reset with confirmation."""
    patterns = find_all_kata_patterns()
    if not patterns:
        print_error("No kata patterns found!")
        return

    pattern_choices = [p.display_name for p in patterns]
    pattern_choices.append("Reset ALL patterns (⚠️  use with caution!)")
    pattern_choices.append("← Back to main menu")
    pattern_map = {p.display_name: p for p in patterns}

    selected = questionary.select(
        "\nSelect pattern to reset:",
        choices=pattern_choices,
        style=grimoire_style,
        instruction="(This will reset functions to 'pass')"
    ).ask()

    if selected == "← Back to main menu" or not selected:
        return

    if selected == "Reset ALL patterns (⚠️  use with caution!)":
        # Confirm
        confirm = questionary.confirm(
            "Are you SURE you want to reset ALL patterns?",
            default=False,
            style=grimoire_style,
        ).ask()

        if confirm:
            reset_cmd.reset_all_patterns(force=False, dry_run=False)
    else:
        pattern = pattern_map[selected]

        # Show dry-run first
        console.print(f"\n[bold yellow]Preview: Resetting {pattern.display_name}[/bold yellow]")
        console.print("[dim]All kata functions will be reset to 'pass'[/dim]")
        console.print("[dim]Docstrings and mastery logs will be preserved[/dim]\n")

        # Confirm
        confirm = questionary.confirm(
            "Continue with reset?",
            default=False,
            style=grimoire_style,
        ).ask()

        if confirm:
            reset_cmd.reset_pattern(pattern.name, force=True, dry_run=False)


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def safe_ask(question_func):
    """Safely ask questionary question, handling KeyboardInterrupt."""
    try:
        return question_func.ask()
    except KeyboardInterrupt:
        console.print("\n[dim]Operation cancelled.[/dim]\n")
        return None
