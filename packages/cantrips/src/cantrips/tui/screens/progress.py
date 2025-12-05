"""Progress screen showing detailed statistics.

Displays:
- Overall stats (total sessions, time, patterns)
- Per-pattern progress with mastery levels
- Recent session history
"""

from datetime import date, timedelta

from rich.table import Table
from rich.text import Text
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Vertical, Horizontal, ScrollableContainer
from textual.screen import Screen
from textual.widgets import Footer, Header, Static

from cantrips.data import Database, MasteryStatus
from cantrips.utils.discovery import discover_patterns


class OverallStats(Static):
    """Widget showing overall statistics."""

    DEFAULT_CSS = """
    OverallStats {
        height: auto;
        padding: 1;
        border: solid $primary;
        margin-bottom: 1;
    }
    """

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db

    def render(self) -> str:
        """Render overall stats."""
        if not self.db:
            return "[dim]No database connection[/dim]"

        stats = self.db.get_total_stats()
        streak = self.db.get_streak()

        total_minutes = stats["total_time_seconds"] // 60
        hours = total_minutes // 60
        minutes = total_minutes % 60

        lines = [
            "[bold cyan]Overall Progress[/bold cyan]",
            "",
            f"  Total Sessions:     [green]{stats['total_sessions']}[/green]",
            f"  Patterns Practiced: [green]{stats['patterns_practiced']}[/green]",
            f"  Total Time:         [green]{hours}h {minutes}m[/green]",
            "",
            f"  Current Streak:     [{'green' if streak.current > 0 else 'dim'}]{streak.current} days[/{'green' if streak.current > 0 else 'dim'}]",
            f"  Longest Streak:     [cyan]{streak.longest} days[/cyan]",
        ]

        return "\n".join(lines)


class PatternProgressList(Static):
    """Widget showing progress for each pattern."""

    DEFAULT_CSS = """
    PatternProgressList {
        height: auto;
        padding: 1;
        border: solid $secondary;
        margin-bottom: 1;
    }
    """

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db

    def render(self) -> str:
        """Render pattern progress list."""
        if not self.db:
            return "[dim]No database connection[/dim]"

        patterns = discover_patterns()
        lines = ["[bold cyan]Pattern Mastery[/bold cyan]", ""]

        for pattern in patterns:
            pattern_name = f"{pattern.category}/{pattern.name}"
            progress = self.db.get_pattern_progress(pattern_name)

            if progress:
                status = progress.mastery_status
                symbol = status.symbol
                color = status.color
                sessions = progress.total_sessions
            else:
                symbol = "○"
                color = "dim"
                sessions = 0

            # Format pattern name
            display = f"{pattern.category}/{pattern.name}"
            lines.append(
                f"  [{color}]{symbol}[/{color}] {display:<35} "
                f"[dim]{sessions:>3} sessions[/dim]"
            )

        return "\n".join(lines)


class RecentSessions(Static):
    """Widget showing recent practice sessions."""

    DEFAULT_CSS = """
    RecentSessions {
        height: auto;
        max-height: 15;
        padding: 1;
        border: solid $primary;
    }
    """

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db

    def render(self) -> str:
        """Render recent sessions."""
        if not self.db:
            return "[dim]No database connection[/dim]"

        sessions = self.db.get_recent_sessions(limit=10)
        lines = ["[bold cyan]Recent Sessions[/bold cyan]", ""]

        if not sessions:
            lines.append("  [dim]No sessions yet[/dim]")
        else:
            for session in sessions:
                time_str = f"{session.time_seconds // 60}:{session.time_seconds % 60:02d}"
                bug_str = f"[red]{session.bugs}[/red]" if session.bugs > 0 else "[green]0[/green]"
                date_str = session.date.strftime("%m/%d")

                lines.append(
                    f"  {date_str}  {session.pattern_name:<30} "
                    f"#{session.cantrip_number}  {time_str}  bugs: {bug_str}"
                )

        return "\n".join(lines)


class ProgressScreen(Screen):
    """Screen showing detailed progress statistics."""

    BINDINGS = [
        Binding("escape", "back", "Back"),
        Binding("r", "refresh", "Refresh"),
    ]

    CSS = """
    ProgressScreen {
        background: $surface;
    }

    #progress-container {
        padding: 1 2;
    }

    #stats-row {
        height: auto;
        margin-bottom: 1;
    }

    #overall-stats {
        width: 1fr;
    }

    #pattern-progress {
        width: 1fr;
        margin-left: 1;
    }
    """

    def __init__(self, db: Database | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.db = db

    def compose(self) -> ComposeResult:
        """Compose the progress screen."""
        yield Header()
        with ScrollableContainer(id="progress-container"):
            yield Static(
                "[bold magenta]Progress Dashboard[/bold magenta]\n",
                id="title",
            )

            with Horizontal(id="stats-row"):
                yield OverallStats(db=self.db, id="overall-stats")
                yield PatternProgressList(db=self.db, id="pattern-progress")

            yield RecentSessions(db=self.db, id="recent-sessions")

        yield Footer()

    def action_back(self) -> None:
        """Return to dashboard."""
        self.app.pop_screen()

    def action_refresh(self) -> None:
        """Refresh stats."""
        self.query_one("#overall-stats", OverallStats).refresh()
        self.query_one("#pattern-progress", PatternProgressList).refresh()
        self.query_one("#recent-sessions", RecentSessions).refresh()
        self.notify("Stats refreshed")
