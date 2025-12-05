"""Stats panel widget.

Shows today's stats, streak, and quick summary information
in a compact format suitable for the dashboard.

Example:
    >>> from cantrips.tui.widgets import StatsPanel
    >>> from cantrips.data import Database
    >>> db = Database()
    >>> panel = StatsPanel(db=db)
"""

from datetime import date

from rich.text import Text
from textual.widget import Widget
from textual.reactive import reactive

from cantrips.data import Database, DailyActivity, Streak


class StatsPanel(Widget):
    """Panel showing today's stats and streak."""

    BORDER_TITLE = "Stats"

    DEFAULT_CSS = """
    StatsPanel {
        height: auto;
        min-height: 5;
        padding: 1;
        border: round $primary;
    }
    """

    streak: reactive[Streak] = reactive(Streak)
    today: reactive[DailyActivity] = reactive(DailyActivity)

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db
        self._streak = Streak()
        self._today = DailyActivity(date=date.today())

    def on_mount(self) -> None:
        """Load data when mounted."""
        self.load_data()

    def load_data(self) -> None:
        """Load stats from database."""
        if self.db:
            self._streak = self.db.get_streak()
            self._today = self.db.get_today_stats()
            self.refresh()

    def render(self) -> Text:
        """Render the stats panel."""
        text = Text()

        # Today's stats section
        text.append("Today\n", style="bold")
        text.append(f"  Sessions: ")
        text.append(f"{self._today.sessions_count}", style="cyan")

        minutes = self._today.total_time_seconds // 60
        text.append(f"  │  Time: ")
        text.append(f"{minutes} min", style="cyan")
        text.append("\n")

        # Patterns practiced today
        if self._today.patterns_practiced:
            patterns = [p.split("/")[-1] for p in self._today.patterns_practiced[:3]]
            text.append("  Patterns: ")
            text.append(", ".join(patterns), style="dim")
            if len(self._today.patterns_practiced) > 3:
                text.append(f" +{len(self._today.patterns_practiced) - 3}", style="dim")
            text.append("\n")

        text.append("\n")

        # Streak section
        text.append("Streak\n", style="bold")
        streak_icon = "🔥" if self._streak.current > 0 else "  "
        text.append(f"  Current: {streak_icon}")
        text.append(f"{self._streak.current}", style="green" if self._streak.current > 0 else "dim")
        text.append(" days")

        if self._streak.longest > 0:
            text.append(f"  │  Best: ")
            text.append(f"{self._streak.longest}", style="dim")
            text.append(" days", style="dim")

        return text
