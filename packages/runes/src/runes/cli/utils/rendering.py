"""
Rich rendering utilities for beautiful terminal output.

Helper functions for creating tables, panels, and styled console output.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Global console instance
console = Console()


def create_patterns_table(patterns_data: list[dict]) -> Table:
    """
    Create a table showing kata patterns and their status.

    Args:
        patterns_data: List of dicts with pattern information

    Returns:
        Rich Table object

    Expected dict structure:
        {
            "name": "two_pointers/opposite_ends",
            "status": "Practicing",
            "last_practice": "2025-11-18",
            "best_time": "2:10",
            "test_mode": "pytest",
        }
    """
    table = Table(title="Kata Patterns", show_header=True, header_style="bold magenta")

    table.add_column("Pattern", style="cyan", no_wrap=True)
    table.add_column("Status", style="green")
    table.add_column("Last Practice", style="yellow")
    table.add_column("Best Time", justify="right")
    table.add_column("Test Mode", justify="center")

    for pattern in patterns_data:
        # Color code status
        status = pattern.get("status", "Unknown")
        if status == "Mastered":
            status_styled = Text(status, style="bold green")
        elif status == "Practicing":
            status_styled = Text(status, style="yellow")
        else:
            status_styled = Text(status, style="white")

        # Format test mode
        test_mode = pattern.get("test_mode", "doctest")
        if test_mode == "pytest":
            test_mode_styled = Text("✓ pytest", style="green")
        else:
            test_mode_styled = Text("✗ doctest", style="red")

        table.add_row(
            pattern.get("name", ""),
            status_styled,
            pattern.get("last_practice", "Never"),
            pattern.get("best_time", "-"),
            test_mode_styled,
        )

    return table


def create_progress_table(kata_data: list[dict]) -> Table:
    """
    Create a table showing progress for individual katas.

    Args:
        kata_data: List of dicts with kata information

    Returns:
        Rich Table object

    Expected dict structure:
        {
            "kata_num": 1,
            "target": "< 2:00",
            "best": "1:45",
            "latest": "2:10",
            "status": "Mastered" | "Practice" | "Not Started",
        }
    """
    table = Table(show_header=True, header_style="bold cyan")

    table.add_column("Kata", justify="center")
    table.add_column("Target", style="dim")
    table.add_column("Best", style="green")
    table.add_column("Latest", style="yellow")
    table.add_column("Status")

    for kata in kata_data:
        status = kata.get("status", "Not Started")

        # Style status
        if status == "Mastered":
            status_text = Text("✓ Mastered", style="bold green")
        elif status == "Practice":
            status_text = Text("⚡ Practice", style="yellow")
        else:
            status_text = Text("○ Not Started", style="dim")

        table.add_row(
            str(kata.get("kata_num", "")),
            kata.get("target", ""),
            kata.get("best", "-"),
            kata.get("latest", "-"),
            status_text,
        )

    return table


def create_summary_panel(title: str, content: str, style: str = "cyan") -> Panel:
    """
    Create a styled panel for displaying summary information.

    Args:
        title: Panel title
        content: Panel content (can be multiline)
        style: Border style color

    Returns:
        Rich Panel object
    """
    return Panel(content, title=title, border_style=style, padding=(1, 2))


def print_success(message: str) -> None:
    """Print a success message."""
    console.print(f"✅ {message}", style="bold green")


def print_error(message: str) -> None:
    """Print an error message."""
    console.print(f"❌ {message}", style="bold red")


def print_warning(message: str) -> None:
    """Print a warning message."""
    console.print(f"⚠️  {message}", style="bold yellow")


def print_info(message: str) -> None:
    """Print an informational message."""
    console.print(f"ℹ️  {message}", style="cyan")


def print_header(text: str) -> None:
    """Print a section header."""
    console.print(f"\n{text}", style="bold magenta underline")


def format_test_status(passed: int, failed: int, skipped: int, total: int) -> Text:
    """
    Format test status with colors.

    Args:
        passed: Number of passed tests
        failed: Number of failed tests
        skipped: Number of skipped tests
        total: Total number of tests

    Returns:
        Rich Text object with styled test summary
    """
    text = Text()

    if passed > 0:
        text.append(f"✓ {passed} passed", style="green")

    if failed > 0:
        if len(text) > 0:
            text.append(" | ")
        text.append(f"✗ {failed} failed", style="red")

    if skipped > 0:
        if len(text) > 0:
            text.append(" | ")
        text.append(f"⊙ {skipped} skipped", style="yellow")

    if len(text) > 0:
        text.append(f" ({total} total)")

    return text
