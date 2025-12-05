"""CLI entry point for cantrips."""

import typer

from .app import app

def main() -> None:
    """Main entry point for the cantrip CLI."""
    app()


__all__ = ["main", "app"]
