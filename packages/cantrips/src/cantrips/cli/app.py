"""
Cantrip CLI application.

Provides commands for algorithm pattern practice.
"""

import typer
from rich.console import Console

app = typer.Typer(
    name="cantrip",
    help="Algorithm pattern drills for interview preparation",
    add_completion=True,
    no_args_is_help=True,
)

console = Console()


@app.command()
def menu() -> None:
    """Launch the interactive TUI dashboard."""
    from cantrips.tui.app import CantripsApp

    tui = CantripsApp()
    tui.run()


@app.command()
def list() -> None:
    """List all available cantrip patterns."""
    console.print("[dim]Coming soon...[/dim]")


@app.command()
def practice(
    pattern: str = typer.Argument(..., help="Pattern to practice (e.g., 'sliding_window/fixed')"),
    number: int = typer.Option(None, "--number", "-n", help="Specific cantrip number (1-5)"),
) -> None:
    """Start a practice session for a specific pattern."""
    console.print(f"[dim]Practice {pattern} coming soon...[/dim]")


@app.command()
def stats() -> None:
    """Show your practice statistics."""
    console.print("[dim]Stats coming soon...[/dim]")


if __name__ == "__main__":
    app()
