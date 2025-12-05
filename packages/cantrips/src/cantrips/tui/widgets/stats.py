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

    DEFAULT_CSS = """
    StatsPanel {
        height: 5;
        padding: 1;
        border: solid $primary;
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

        # Streak
        streak_icon = "🔥" if self._streak.current > 0 else "  "
        text.append(f"{streak_icon} Streak: ", style="bold")
        text.append(f"{self._streak.current} days", style="green" if self._streak.current > 0 else "dim")

        text.append("  │  ")

        # Today's sessions
        text.append("Today: ", style="bold")
        text.append(f"{self._today.sessions_count} sessions", style="cyan")

        text.append("  │  ")

        # Today's time
        minutes = self._today.total_time_seconds // 60
        text.append("Time: ", style="bold")
        text.append(f"{minutes} min", style="cyan")

        return text
