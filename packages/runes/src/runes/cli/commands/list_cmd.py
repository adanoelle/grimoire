"""
List command - Show all kata patterns with status.

Display a table of all available kata patterns with their practice status.
"""

import typer
from rich.console import Console

from ..utils.discovery import find_all_kata_patterns
from ..utils.mastery import parse_mastery_log, get_practice_summary
from ..utils.rendering import create_patterns_table, console, print_warning


def list_patterns():
    """
    List all kata patterns with their status.

    Shows a table with:
    - Pattern name
    - Status (Learning/Practicing/Mastered)
    - Last practice date
    - Best time
    - Test mode (pytest/doctest)
    """
    console.print("\n[bold magenta]🥋 Kata Patterns[/bold magenta]\n")

    # Find all patterns
    patterns = find_all_kata_patterns()

    if not patterns:
        console.print("[yellow]No kata patterns found.[/yellow]")
        return

    # Gather data for table
    patterns_data = []
    for pattern in patterns:
        # Parse mastery log (returns Result)
        log_result = parse_mastery_log(pattern.kata_file)

        if log_result.is_failure():
            # Log warning but don't fail entire operation
            error = log_result.error
            print_warning(f"Could not parse {pattern.display_name}: {error.message}")
            # Add pattern with default values
            patterns_data.append(
                {
                    "name": pattern.display_name,
                    "status": "Unknown",
                    "last_practice": "Error",
                    "best_time": "-",
                    "test_mode": "pytest" if pattern.has_pytest else "doctest",
                }
            )
            continue

        log = log_result.unwrap()

        # Display any parse warnings
        if log.warnings:
            for warning in log.warnings:
                print_warning(f"{pattern.display_name}: {warning}")

        summary = get_practice_summary(log)

        # Get status from domain model (no more business logic in UI!)
        status = log.status.value

        # Format last practice date
        last_practice = summary["last_practice"]
        last_practice_str = str(last_practice) if last_practice else "Never"

        # Get best time for first kata (most commonly practiced)
        best_times = summary["best_times"]
        best_time_str = "-"
        if 1 in best_times:
            seconds = best_times[1]
            minutes = seconds // 60
            secs = seconds % 60
            best_time_str = f"{minutes}:{secs:02d}"

        patterns_data.append(
            {
                "name": pattern.display_name,
                "status": status,
                "last_practice": last_practice_str,
                "best_time": best_time_str,
                "test_mode": "pytest" if pattern.has_pytest else "doctest",
            }
        )

    # Create and print table
    table = create_patterns_table(patterns_data)
    console.print(table)

    # Print summary
    total = len(patterns)
    migrated = sum(1 for p in patterns if p.has_pytest)
    console.print(
        f"\n[dim]Total patterns: {total} | Pytest-ready: {migrated} | Legacy: {total - migrated}[/dim]\n"
    )
