"""
Progress command - Show detailed progress for a kata pattern.

Display practice history, mastery status, and checklist for a specific pattern.
"""

import typer
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from ..utils.discovery import find_kata_pattern
from ..utils.mastery import parse_mastery_log, get_practice_summary
from ..utils.rendering import console, print_error, print_warning


def show_progress(pattern_name: str):
    """
    Show detailed progress for a specific kata pattern.

    Args:
        pattern_name: Name of the pattern (e.g., "opposite_ends", "binary_search")

    Displays:
        - Mastery status
        - Practice history table
        - Per-kata progress with best times
        - Mastery checklist
    """
    # Find the pattern
    pattern_result = find_kata_pattern(pattern_name)

    if pattern_result.is_failure():
        error = pattern_result.error
        print_error(f"Pattern not found: {error.message}")
        raise typer.Exit(1)

    pattern = pattern_result.unwrap()

    # Parse mastery log
    log_result = parse_mastery_log(pattern.kata_file)

    if log_result.is_failure():
        error = log_result.error
        print_error(f"Could not parse mastery log: {error.message}")
        raise typer.Exit(1)

    log = log_result.unwrap()

    # Show warnings if any
    if log.warnings:
        for warning in log.warnings:
            print_warning(warning)
        console.print()  # Blank line

    # Header
    console.print(f"\n[bold magenta]🥋 {pattern.display_name}[/bold magenta]\n")

    # Mastery status
    summary = get_practice_summary(log)
    status = log.status
    status_color = status.display_color

    console.print(
        f"[bold]MASTERY STATUS:[/bold] [{status_color}]{status.value}[/{status_color}] "
        f"({summary['total_sessions']} practice sessions)"
    )

    if summary["last_practice"]:
        console.print(f"[dim]Last practice: {summary['last_practice']}[/dim]")

    console.print()

    # Practice history
    if log.sessions:
        console.print("[bold]PRACTICE HISTORY:[/bold]\n")

        history_table = Table(show_header=True, header_style="bold cyan")
        history_table.add_column("Date", style="dim")
        history_table.add_column("Kata", justify="center")
        history_table.add_column("Time", justify="right")
        history_table.add_column("Bugs", justify="center")
        history_table.add_column("Notes")

        for session in log.sessions:
            bugs_style = "green" if session.bugs == 0 else "yellow" if session.bugs < 3 else "red"
            history_table.add_row(
                str(session.date),
                str(session.kata_number),
                session.time_str,
                f"[{bugs_style}]{session.bugs}[/{bugs_style}]",
                session.notes,
            )

        console.print(history_table)
        console.print()
    else:
        console.print("[yellow]No practice sessions yet. Start practicing![/yellow]\n")

    # Per-kata progress
    if summary["best_times"]:
        console.print("[bold]KATA PROGRESS:[/bold]\n")

        best_times = summary["best_times"]
        total_bugs = summary["total_bugs"]

        for kata_num in sorted(best_times.keys()):
            best_seconds = best_times[kata_num]
            minutes = best_seconds // 60
            seconds = best_seconds % 60
            time_str = f"{minutes}:{seconds:02d}"

            bugs = total_bugs.get(kata_num, 0)

            # Simple progress indicator (can be enhanced with target times later)
            if bugs == 0 and best_seconds < 120:
                indicator = "✓"
                style = "green"
            else:
                indicator = " "
                style = "white"

            console.print(
                f"[{style}]{indicator} Kata {kata_num}: Best time {time_str}, "
                f"{bugs} total bugs[/{style}]"
            )

        console.print()

    # Checklist
    if log.checklist_items:
        console.print("[bold]MASTERY CHECKLIST:[/bold]\n")

        for item in log.checklist_items:
            # Color based on completion
            if item.startswith("[x]") or item.startswith("[X]"):
                console.print(f"[green]{item}[/green]")
            else:
                console.print(f"[dim]{item}[/dim]")

        console.print()

    # Encouragement
    if summary["total_sessions"] == 0:
        console.print("[bold yellow]💪 Start your first practice session![/bold yellow]")
    elif status.value == "Learning":
        remaining = 5 - summary["total_sessions"]
        console.print(
            f"[bold yellow]💪 {remaining} more sessions to reach Practicing level![/bold yellow]"
        )
    elif status.value == "Practicing":
        remaining = 20 - summary["total_sessions"]
        console.print(
            f"[bold yellow]💪 {remaining} more sessions to reach Mastered level![/bold yellow]"
        )
    else:
        console.print("[bold green]🎉 Mastered! Keep practicing to maintain muscle memory.[/bold green]")

    console.print()
