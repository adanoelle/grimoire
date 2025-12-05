"""
Main Textual application for cantrips.

Provides the TUI dashboard and navigation.
"""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, Static, ListView, ListItem, Label
from textual.containers import Container, Horizontal, Vertical

from cantrips.data import Database, ReviewItem
from cantrips.tui.widgets import ContributionCalendar, StatsPanel
from cantrips.tui.screens import BrowserScreen, PracticeScreen, ProgressScreen, ReviewScreen
from cantrips.tui.themes import CUSTOM_THEMES
from cantrips.utils.discovery import discover_patterns


class ReviewQueue(Static):
    """Widget showing patterns due for review."""

    DEFAULT_CSS = """
    ReviewQueue {
        height: auto;
        max-height: 10;
        padding: 1;
        border: solid $secondary;
    }

    ReviewQueue .title {
        text-style: bold;
        color: $text;
    }

    ReviewQueue .empty {
        color: $text-muted;
        text-style: italic;
    }

    ReviewQueue .due {
        color: $warning;
    }

    ReviewQueue .overdue {
        color: $error;
    }
    """

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db
        self._queue: list[ReviewItem] = []

    def on_mount(self) -> None:
        """Load review queue when mounted."""
        self.load_data()

    def load_data(self) -> None:
        """Load review queue from database."""
        if self.db:
            self._queue = self.db.get_review_queue()
            self.refresh()

    def render(self) -> str:
        """Render the review queue."""
        lines = ["[bold]Review Queue[/bold]"]

        if not self._queue:
            lines.append("[dim italic]No patterns due for review[/dim italic]")
        else:
            for item in self._queue[:5]:  # Show top 5
                days = item.days_overdue
                if days > 0:
                    status = f"[red]{days}d overdue[/red]"
                else:
                    status = "[yellow]Due today[/yellow]"
                lines.append(f"  {item.pattern_name} - {status}")

            if len(self._queue) > 5:
                lines.append(f"  [dim]...and {len(self._queue) - 5} more[/dim]")

        return "\n".join(lines)


class QuickActions(Static):
    """Widget showing available keyboard shortcuts."""

    DEFAULT_CSS = """
    QuickActions {
        height: auto;
        padding: 1;
        border: solid $primary;
    }
    """

    def render(self) -> str:
        return """[bold]Quick Actions[/bold]

  [green]p[/green] Practice    [green]b[/green] Browse
  [green]r[/green] Review      [green]s[/green] Stats
  [green]q[/green] Quit"""


class CantripsApp(App[None]):
    """Main cantrips TUI application."""

    TITLE = "Cantrips"
    SUB_TITLE = "Algorithm Pattern Practice"

    CSS = """
    Screen {
        background: $surface;
    }

    Header {
        background: $primary;
    }

    Footer {
        background: $surface-darken-1;
    }

    #dashboard {
        padding: 1 2;
    }

    #calendar-container {
        height: auto;
        margin-bottom: 1;
    }

    #stats-row {
        height: auto;
        margin-bottom: 1;
    }

    #stats-panel {
        width: 1fr;
    }

    #actions-panel {
        width: 1fr;
        margin-left: 1;
    }

    #review-container {
        height: auto;
    }

    ContributionCalendar {
        border: solid $primary;
    }

    StatsPanel {
        border: solid $secondary;
    }
    """

    BINDINGS = [
        Binding("p", "practice", "Practice"),
        Binding("b", "browse", "Browse"),
        Binding("r", "review", "Review"),
        Binding("s", "stats", "Stats"),
        Binding("q", "quit", "Quit"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.db = Database()

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id="dashboard"):
            # Title
            yield Static(
                "[bold magenta]Cantrips[/bold magenta] - Practice until it's muscle memory\n",
                id="title",
            )

            # Contribution Calendar (full year)
            with Container(id="calendar-container"):
                yield ContributionCalendar(db=self.db)

            # Stats and Quick Actions row
            with Horizontal(id="stats-row"):
                yield StatsPanel(db=self.db, id="stats-panel")
                yield QuickActions(id="actions-panel")

            # Review Queue
            with Container(id="review-container"):
                yield ReviewQueue(db=self.db)

        yield Footer()

    def on_mount(self) -> None:
        """Register custom themes and set default."""
        for theme in CUSTOM_THEMES:
            self.register_theme(theme)
        # Set Christmas theme as default
        self.theme = "christmas"

    def action_practice(self) -> None:
        """Start a practice session with first due item or first cantrip."""
        # Check review queue first
        queue = self.db.get_review_queue()
        if queue:
            # Practice the first due pattern
            pattern_name = queue[0].pattern_name
            patterns = discover_patterns()
            for pattern in patterns:
                if f"{pattern.category}/{pattern.name}" == pattern_name:
                    if pattern.cantrips:
                        self.push_screen(
                            PracticeScreen(pattern, pattern.cantrips[0], db=self.db)
                        )
                        return

        # Otherwise go to browser
        self.push_screen(BrowserScreen(db=self.db))

    def action_browse(self) -> None:
        """Open the pattern browser."""
        self.push_screen(BrowserScreen(db=self.db))

    def action_review(self) -> None:
        """Open the review queue."""
        self.push_screen(ReviewScreen(db=self.db))

    def action_stats(self) -> None:
        """Show statistics."""
        self.push_screen(ProgressScreen(db=self.db))


def main() -> None:
    """Run the cantrips TUI."""
    app = CantripsApp()
    app.run()


if __name__ == "__main__":
    main()
