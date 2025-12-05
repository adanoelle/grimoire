"""Review screen for spaced repetition queue.

Displays patterns due for review and allows starting practice sessions.
"""

from datetime import date

from rich.text import Text
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Vertical, ScrollableContainer
from textual.screen import Screen
from textual.widgets import Footer, Header, Static, ListView, ListItem, Label

from cantrips.data import Database, ReviewItem
from cantrips.utils.discovery import discover_patterns, get_pattern


class ReviewQueueList(Static):
    """Widget showing the full review queue."""

    BORDER_TITLE = "Review Queue"

    DEFAULT_CSS = """
    ReviewQueueList {
        height: auto;
        padding: 1;
        border: round $primary;
    }
    """

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db
        self._queue: list[ReviewItem] = []
        self._selected_index = 0

    def on_mount(self) -> None:
        """Load queue when mounted."""
        self.load_queue()

    def load_queue(self) -> None:
        """Load review queue from database."""
        if self.db:
            self._queue = self.db.get_review_queue()
            self.refresh()

    def get_selected_pattern(self) -> str | None:
        """Get the currently selected pattern name."""
        if self._queue and 0 <= self._selected_index < len(self._queue):
            return self._queue[self._selected_index].pattern_name
        return None

    def move_selection(self, delta: int) -> None:
        """Move selection up or down."""
        if self._queue:
            self._selected_index = max(
                0, min(len(self._queue) - 1, self._selected_index + delta)
            )
            self.refresh()

    def render(self) -> str:
        """Render the review queue."""
        lines = []

        if not self._queue:
            lines.append("  [green]No patterns due for review![/green]")
            lines.append("")
            lines.append("  [dim]Practice some cantrips to build your queue.[/dim]")
        else:
            lines.append(
                f"  [dim]{len(self._queue)} patterns due for review[/dim]"
            )
            lines.append("")

            for i, item in enumerate(self._queue):
                days = item.days_overdue

                if days > 7:
                    status = f"[red]{days}d overdue[/red]"
                elif days > 0:
                    status = f"[yellow]{days}d overdue[/yellow]"
                else:
                    status = "[green]Due today[/green]"

                # Selection indicator
                if i == self._selected_index:
                    prefix = "[reverse] > [/reverse]"
                else:
                    prefix = "   "

                lines.append(f"{prefix}{item.pattern_name:<35} {status}")

        lines.append("")
        lines.append("[dim]↑/↓ to select, Enter to practice, Esc to go back[/dim]")

        return "\n".join(lines)


class ReviewStats(Static):
    """Widget showing review statistics."""

    BORDER_TITLE = "Spaced Repetition Stats"

    DEFAULT_CSS = """
    ReviewStats {
        height: auto;
        padding: 1;
        border: round $secondary;
        margin-top: 1;
    }
    """

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db

    def _get_accent_color(self) -> str:
        """Get the theme's secondary color for accents."""
        try:
            theme = self.app.current_theme
            return theme.secondary or "cyan"
        except Exception:
            return "cyan"

    def render(self) -> str:
        """Render review stats."""
        if not self.db:
            return "[dim]No database connection[/dim]"

        queue = self.db.get_review_queue()
        patterns = discover_patterns()
        color = self._get_accent_color()

        total_patterns = len(patterns)
        due_count = len(queue)
        overdue_count = sum(1 for item in queue if item.days_overdue > 0)

        lines = [
            f"Total Patterns:    [{color}]{total_patterns}[/{color}]",
            f"Due for Review:    [{'yellow' if due_count > 0 else 'green'}]{due_count}[/{'yellow' if due_count > 0 else 'green'}]",
            f"Overdue:           [{'red' if overdue_count > 0 else 'green'}]{overdue_count}[/{'red' if overdue_count > 0 else 'green'}]",
            "",
            "[dim]SM-2 Algorithm:[/dim]",
            "  • Pass with 0 bugs → interval increases",
            "  • Pass with 1-2 bugs → interval stays",
            "  • Fail (3+ bugs) → reset to 1 day",
        ]

        return "\n".join(lines)


class ReviewScreen(Screen):
    """Screen for managing spaced repetition review queue."""

    BINDINGS = [
        Binding("escape", "back", "Back"),
        Binding("enter", "practice", "Practice Selected"),
        Binding("up", "move_up", "Up", show=False),
        Binding("down", "move_down", "Down", show=False),
        Binding("k", "move_up", "Up", show=False),
        Binding("j", "move_down", "Down", show=False),
    ]

    CSS = """
    ReviewScreen {
        background: $surface;
    }

    #review-container {
        padding: 1 2;
    }
    """

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db

    def compose(self) -> ComposeResult:
        """Compose the review screen."""
        yield Header()
        with ScrollableContainer(id="review-container"):
            yield Static(
                "[bold magenta]Spaced Repetition Review[/bold magenta]\n",
                id="title",
            )
            yield ReviewQueueList(db=self.db, id="queue-list")
            yield ReviewStats(db=self.db, id="review-stats")

        yield Footer()

    def action_back(self) -> None:
        """Return to dashboard."""
        self.app.pop_screen()

    def action_move_up(self) -> None:
        """Move selection up."""
        self.query_one("#queue-list", ReviewQueueList).move_selection(-1)

    def action_move_down(self) -> None:
        """Move selection down."""
        self.query_one("#queue-list", ReviewQueueList).move_selection(1)

    def action_practice(self) -> None:
        """Start practice for selected pattern."""
        queue_list = self.query_one("#queue-list", ReviewQueueList)
        pattern_name = queue_list.get_selected_pattern()

        if not pattern_name:
            self.notify("No pattern selected", severity="warning")
            return

        # Find pattern and first cantrip
        pattern = get_pattern(pattern_name)
        if pattern and pattern.cantrips:
            from .practice import PracticeScreen

            self.app.push_screen(
                PracticeScreen(pattern, pattern.cantrips[0], db=self.db)
            )
        else:
            self.notify(f"Pattern not found: {pattern_name}", severity="error")
