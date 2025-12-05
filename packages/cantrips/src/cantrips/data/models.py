"""Data models for cantrips.

This module defines the core data structures used throughout the cantrips
application for tracking practice sessions, progress, and spaced repetition.

All models are implemented as dataclasses for immutability and easy serialization.

Example:
    >>> from cantrips.data.models import PracticeSession, MasteryStatus
    >>> from datetime import date
    >>> session = PracticeSession(
    ...     pattern_name="sliding_window/fixed_window",
    ...     cantrip_number=1,
    ...     date=date.today(),
    ...     time_seconds=145,
    ...     bugs=0,
    ... )
    >>> session.time_display
    '2:25'
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum


class MasteryStatus(str, Enum):
    """Mastery level for a cantrip pattern.

    Mastery is determined by the number of practice sessions completed:
        - LEARNING: Less than 5 sessions
        - PRACTICING: 5-19 sessions
        - MASTERED: 20+ sessions with target times consistently met

    Attributes:
        LEARNING: Initial learning phase, building familiarity.
        PRACTICING: Active practice phase, building speed and accuracy.
        MASTERED: Pattern is automatic, can be performed without thinking.

    Example:
        >>> status = MasteryStatus.PRACTICING
        >>> status.color
        'yellow'
        >>> status.symbol
        '◐'
    """

    LEARNING = "Learning"
    PRACTICING = "Practicing"
    MASTERED = "Mastered"

    @property
    def color(self) -> str:
        """Get the Rich color for this status.

        Returns:
            A color string compatible with Rich markup.
        """
        colors = {
            MasteryStatus.LEARNING: "white",
            MasteryStatus.PRACTICING: "yellow",
            MasteryStatus.MASTERED: "green",
        }
        return colors[self]

    @property
    def symbol(self) -> str:
        """Get the Unicode symbol for this status.

        Returns:
            A single-character symbol representing the status.
        """
        symbols = {
            MasteryStatus.LEARNING: "○",
            MasteryStatus.PRACTICING: "◐",
            MasteryStatus.MASTERED: "✓",
        }
        return symbols[self]


@dataclass
class PracticeSession:
    """A single practice session for a cantrip.

    Represents one attempt at solving a cantrip problem, including
    timing information, bug count, and optional notes.

    Attributes:
        pattern_name: The pattern identifier (e.g., "sliding_window/fixed_window").
        cantrip_number: Which cantrip in the pattern (1-5).
        date: The date of the practice session.
        time_seconds: Time taken to complete, in seconds.
        bugs: Number of bugs/errors encountered (0 for perfect run).
        notes: Optional notes about the session.
        id: Database ID (None if not persisted).
        created_at: Timestamp when the session was logged.

    Example:
        >>> session = PracticeSession(
        ...     pattern_name="two_pointers/opposite_ends",
        ...     cantrip_number=2,
        ...     date=date(2024, 1, 15),
        ...     time_seconds=180,
        ...     bugs=1,
        ...     notes="Off-by-one error on edge case",
        ... )
        >>> session.time_display
        '3:00'
    """

    pattern_name: str
    cantrip_number: int
    date: date
    time_seconds: int
    bugs: int = 0
    notes: str = ""
    id: int | None = None
    created_at: datetime | None = None

    @property
    def time_display(self) -> str:
        """Format the time as M:SS or MM:SS.

        Returns:
            Human-readable time string.
        """
        minutes = self.time_seconds // 60
        seconds = self.time_seconds % 60
        return f"{minutes}:{seconds:02d}"


@dataclass
class DailyActivity:
    """Aggregated activity for a single day.

    Used for the contribution calendar to show practice intensity.

    Attributes:
        date: The date of activity.
        sessions_count: Total practice sessions on this day.
        total_time_seconds: Total time spent practicing.
        patterns_practiced: List of pattern names practiced.

    Example:
        >>> activity = DailyActivity(
        ...     date=date.today(),
        ...     sessions_count=3,
        ...     total_time_seconds=900,
        ...     patterns_practiced=["sliding_window/fixed_window", "binary_search"],
        ... )
        >>> activity.intensity
        2
    """

    date: date = field(default_factory=date.today)
    sessions_count: int = 0
    total_time_seconds: int = 0
    patterns_practiced: list[str] = field(default_factory=list)

    @property
    def intensity(self) -> int:
        """Get intensity level 0-4 for calendar coloring.

        Maps session count to a color intensity level suitable for
        rendering a GitHub-style contribution calendar.

        Returns:
            Integer from 0 (no activity) to 4 (very high activity).
        """
        if self.sessions_count == 0:
            return 0
        if self.sessions_count <= 2:
            return 1
        if self.sessions_count <= 4:
            return 2
        if self.sessions_count <= 6:
            return 3
        return 4


@dataclass
class ReviewItem:
    """A pattern in the spaced repetition queue.

    Tracks when a pattern was last reviewed and when it should be
    reviewed next, using the SM-2 spaced repetition algorithm.

    Attributes:
        pattern_name: The pattern identifier.
        last_reviewed: Date of the most recent review.
        next_review: Scheduled date for next review.
        ease_factor: SM-2 ease factor (default 2.5, min 1.3).
        interval_days: Current interval in days.
        repetitions: Number of successful repetitions.

    Example:
        >>> item = ReviewItem(
        ...     pattern_name="sliding_window/fixed_window",
        ...     next_review=date.today(),
        ... )
        >>> item.is_due
        True
    """

    pattern_name: str
    last_reviewed: date | None = None
    next_review: date | None = None
    ease_factor: float = 2.5
    interval_days: int = 1
    repetitions: int = 0

    @property
    def is_due(self) -> bool:
        """Check if this pattern is due for review.

        Returns:
            True if the pattern should be reviewed today or earlier.
        """
        if self.next_review is None:
            return True
        return date.today() >= self.next_review

    @property
    def days_overdue(self) -> int:
        """Calculate how many days overdue this review is.

        Returns:
            Positive number if overdue, zero if due today,
            negative if not yet due.
        """
        if self.next_review is None:
            return 0
        return (date.today() - self.next_review).days


@dataclass
class PatternProgress:
    """Progress summary for a pattern.

    Aggregates all practice data for a pattern into a summary
    suitable for display in the UI.

    Attributes:
        pattern_name: Full pattern identifier (e.g., "sliding_window/fixed_window").
        display_name: Human-readable name (e.g., "fixed_window").
        category: Pattern category (e.g., "sliding_window").
        total_sessions: Total number of practice sessions.
        mastery_status: Current mastery level.
        last_practice: Date of most recent practice.
        best_times: Best time (seconds) for each cantrip number.
        total_bugs: Total bugs encountered for each cantrip number.

    Example:
        >>> progress = PatternProgress(
        ...     pattern_name="sliding_window/fixed_window",
        ...     display_name="fixed_window",
        ...     category="sliding_window",
        ...     total_sessions=12,
        ... )
        >>> progress.mastery_status
        <MasteryStatus.PRACTICING: 'Practicing'>
    """

    pattern_name: str
    display_name: str
    category: str
    total_sessions: int = 0
    mastery_status: MasteryStatus = MasteryStatus.LEARNING
    last_practice: date | None = None
    best_times: dict[int, int] = field(default_factory=dict)
    total_bugs: dict[int, int] = field(default_factory=dict)

    @classmethod
    def calculate_status(cls, total_sessions: int) -> MasteryStatus:
        """Calculate mastery status from session count.

        Args:
            total_sessions: Number of completed practice sessions.

        Returns:
            The appropriate MasteryStatus based on session count.
        """
        if total_sessions < 5:
            return MasteryStatus.LEARNING
        if total_sessions < 20:
            return MasteryStatus.PRACTICING
        return MasteryStatus.MASTERED


@dataclass
class Streak:
    """Practice streak information.

    Tracks consecutive days of practice for motivation and gamification.

    Attributes:
        current: Current streak in consecutive days.
        longest: Longest streak ever achieved.
        last_practice_date: Date of most recent practice.

    Example:
        >>> streak = Streak(current=7, longest=14, last_practice_date=date.today())
        >>> streak.is_active_today
        True
    """

    current: int = 0
    longest: int = 0
    last_practice_date: date | None = None

    @property
    def is_active_today(self) -> bool:
        """Check if user has practiced today.

        Returns:
            True if there was practice activity today.
        """
        if self.last_practice_date is None:
            return False
        return self.last_practice_date == date.today()
