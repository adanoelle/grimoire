"""
Contribution calendar widget.

GitHub-style activity heatmap showing practice history.
"""

from datetime import date, timedelta

from rich.text import Text
from textual.widget import Widget
from textual.reactive import reactive

from cantrips.data import Database


class ContributionCalendar(Widget):
    """GitHub-style contribution calendar showing practice activity.

    Displays a full year of activity as colored squares,
    matching GitHub's contribution graph design.
    """

    BORDER_TITLE = "Activity"

    DEFAULT_CSS = """
    ContributionCalendar {
        height: auto;
        min-height: 11;
        padding: 1;
    }
    """

    # Activity data: date string -> session count
    data: reactive[dict[str, int]] = reactive({}, always_update=True)

    # Christmas-style color levels for intensity (0-4)
    COLORS = [
        "#161b22",  # 0: no activity (dark background)
        "#5c1a1a",  # 1: dark red
        "#8b2323",  # 2: medium red
        "#c41e3a",  # 3: christmas red (primary)
        "#ffd700",  # 4: gold (accent) for high activity
    ]

    def __init__(
        self,
        db: Database | None = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.db = db

    def on_mount(self) -> None:
        """Load data when mounted."""
        self.load_data()

    def load_data(self) -> None:
        """Load calendar data from database."""
        if self.db:
            self.data = self.db.get_calendar_data(days=370)

    def get_intensity(self, count: int) -> int:
        """Map session count to intensity level 0-4."""
        if count == 0:
            return 0
        if count <= 1:
            return 1
        if count <= 2:
            return 2
        if count <= 4:
            return 3
        return 4

    def render(self) -> Text:
        """Render the contribution calendar with GitHub-style squares."""
        text = Text()
        today = date.today()

        # Calculate start: ~1 year ago, aligned to Sunday
        start = today - timedelta(days=364)
        # Adjust to previous Sunday (Python: Mon=0, Sun=6)
        days_back = (start.weekday() + 1) % 7
        start = start - timedelta(days=days_back)

        # Calculate number of weeks from start to today
        days_total = (today - start).days + 1
        num_weeks = (days_total + 6) // 7  # Ceiling division

        # Month labels row - positioned by character offset
        # Each week = 2 chars, month names = 3 chars
        text.append("    ")  # Padding for day labels (4 chars)

        # First, collect which weeks need month labels
        month_at_week: dict[int, str] = {}
        prev_month = ""
        for w in range(num_weeks):
            week_month = None
            for d in range(7):
                day = start + timedelta(days=w * 7 + d)
                if day > today:
                    break
                if day.day == 1:
                    week_month = day.strftime("%b")
                    break
            if week_month is None and w == 0:
                week_month = start.strftime("%b")
            if week_month and week_month != prev_month:
                month_at_week[w] = week_month
                prev_month = week_month

        # Render with proper spacing
        char_pos = 0
        for w in range(num_weeks):
            target_pos = w * 2
            if w in month_at_week:
                # Add spacing to reach this position
                if target_pos > char_pos:
                    text.append(" " * (target_pos - char_pos))
                text.append(month_at_week[w])
                char_pos = target_pos + 3  # Month name is 3 chars
            # No else - we just skip and let next label catch up

        text.append("\n")

        # Day rows
        day_names = ["", "Mon", "", "Wed", "", "Fri", ""]
        for day in range(7):
            # Day label (4 chars)
            label = day_names[day]
            text.append(f"{label:<4}", style="dim" if label else None)

            # Each week column
            for w in range(num_weeks):
                d = start + timedelta(days=w * 7 + day)
                if d > today:
                    break  # Don't render future
                date_str = d.isoformat()
                count = self.data.get(date_str, 0)
                intensity = self.get_intensity(count)
                text.append("■ ", style=self.COLORS[intensity])
            text.append("\n")

        # Legend
        text.append("    Less ")
        for i in range(5):
            text.append("■ ", style=self.COLORS[i])
        text.append("More")

        return text
