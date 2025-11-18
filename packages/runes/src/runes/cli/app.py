"""
Main Typer app for kata practice CLI.

Entry point for the runes kata command-line interface.
"""

import typer
from rich.console import Console

from .commands import list_cmd, progress_cmd, test_cmd, reset_cmd, practice_cmd, menu_cmd

console = Console()

# Create parent app
app = typer.Typer(
    help="🧙 Runes - Data structures and algorithms from scratch",
    add_completion=True,
)

# Create kata subcommand group
kata_app = typer.Typer(
    help="🥋 Kata practice system for algorithm mastery",
)

# Register kata commands
@kata_app.command("menu")
def menu_command():
    """
    Launch interactive kata practice menu.

    Provides a user-friendly interface for:
    - Selecting katas to practice
    - Running tests with filters
    - Viewing progress
    - Resetting katas

    No need to memorize justfile commands!

    Example:
        runes kata menu    # Launch interactive menu
    """
    menu_cmd.run_interactive_menu()


@kata_app.command("list")
def list_patterns_command():
    """
    List all kata patterns with status.

    Shows practice history, best times, and migration status.
    """
    list_cmd.list_patterns()


@kata_app.command("progress")
def progress_command(
    pattern: str = typer.Argument(..., help="Kata pattern name (e.g., 'opposite_ends', 'binary_search')")
):
    """
    Show detailed progress for a kata pattern.

    Displays practice history, mastery status, and checklist.
    """
    progress_cmd.show_progress(pattern)


@kata_app.command("test")
def test_command(
    pattern: str = typer.Argument(..., help="Kata pattern name"),
    kata: int = typer.Option(None, "--kata", "-k", help="Specific kata number to test (e.g., 1, 2, 3)"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose pytest output"),
):
    """
    Run pytest tests for a kata pattern.

    Examples:
        runes kata test opposite_ends          # Test all katas
        runes kata test opposite_ends -k 1     # Test only kata 1
        runes kata test binary_search -v       # Verbose output
    """
    test_cmd.run_tests(pattern, kata_number=kata, verbose=verbose)


@kata_app.command("test-all")
def test_all_command(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose pytest output")
):
    """
    Run pytest tests for all migrated patterns.

    Runs all test_kata.py files for patterns that have pytest tests.
    """
    test_cmd.run_all_tests(verbose=verbose)


@kata_app.command("reset")
def reset_command(
    pattern: str = typer.Argument(..., help="Kata pattern name"),
    force: bool = typer.Option(False, "--force", "-f", help="Skip confirmation prompt"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show what would be changed without writing"),
):
    """
    Reset kata functions back to 'pass'.

    Preserves function signatures, docstrings, and mastery tracking.
    Use this to practice the kata again from scratch.

    Examples:
        runes kata reset opposite_ends       # Reset with confirmation
        runes kata reset binary_search -f    # Force reset without prompt
        runes kata reset opposite_ends --dry-run  # Preview changes
    """
    reset_cmd.reset_pattern(pattern, force=force, dry_run=dry_run)


@kata_app.command("reset-all")
def reset_all_command(
    force: bool = typer.Option(False, "--force", "-f", help="Skip confirmation prompt"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show what would be changed without writing"),
):
    """
    Reset ALL kata patterns back to 'pass'.

    ⚠️  WARNING: This resets all patterns in the algorithms directory.
    Preserves docstrings and mastery tracking.

    Examples:
        runes kata reset-all --dry-run   # Preview what would be reset
        runes kata reset-all             # Reset with confirmation
        runes kata reset-all -f          # Force reset without prompt
    """
    reset_cmd.reset_all_patterns(force=force, dry_run=dry_run)


@kata_app.command("undo")
def undo_reset_command(
    pattern: str = typer.Argument(..., help="Kata pattern name"),
):
    """
    Undo the last reset by restoring from backup.

    Backups are automatically created when you reset a kata.
    This command restores the kata.py file from the .kata.backup file.

    Examples:
        runes kata undo opposite_ends        # Restore from backup
        runes kata undo sliding_window/fixed_window
    """
    reset_cmd.undo_reset_pattern(pattern)


@kata_app.command("practice")
def practice_command(
    pattern: str = typer.Argument(..., help="Kata pattern name"),
    kata: int = typer.Option(None, "--kata", "-k", help="Specific kata number to practice"),
    skip_timer: bool = typer.Option(False, "--skip-timer", help="Skip interactive timer (manual time entry)"),
):
    """
    Start an interactive practice session.

    Guides you through:
    - Shows kata requirements and hints
    - Starts timer
    - Prompts for results (time, bugs, notes)
    - Logs session to mastery tracking

    Examples:
        runes kata practice opposite_ends           # Choose kata interactively
        runes kata practice opposite_ends -k 1      # Practice kata 1
        runes kata practice binary_search --skip-timer  # Manual time entry
    """
    practice_cmd.start_practice(pattern, kata_number=kata, skip_timer=skip_timer)


@kata_app.command("log")
def log_command(
    pattern: str = typer.Argument(..., help="Kata pattern name"),
    kata: int = typer.Argument(..., help="Kata number practiced"),
    time: str = typer.Argument(..., help="Time taken (e.g., '2:30')"),
    bugs: int = typer.Option(0, "--bugs", "-b", help="Number of bugs encountered"),
    notes: str = typer.Option("", "--notes", "-n", help="Optional notes about the session"),
):
    """
    Quickly log a practice session without interactive prompts.

    For when you practiced outside the CLI and want to log retroactively.

    Examples:
        runes kata log opposite_ends 1 2:30           # Perfect run
        runes kata log binary_search 1 3:45 -b 2      # With bugs
        runes kata log opposite_ends 2 4:00 -b 1 -n "Forgot edge case"
    """
    practice_cmd.quick_log(pattern, kata, time, bugs=bugs, notes=notes)


# Add kata subcommand to parent app
app.add_typer(kata_app, name="kata")


# Main entry point
def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
