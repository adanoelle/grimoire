"""
Practice session timer utilities.

Simple timer for tracking kata practice duration.
"""

import time
from datetime import timedelta


class PracticeTimer:
    """Timer for kata practice sessions."""

    def __init__(self):
        """Initialize timer."""
        self._start_time: float | None = None
        self._elapsed: float = 0.0
        self.elapsed_str: str | None = None  # Manual time entry

    def start(self) -> None:
        """Start the timer."""
        self._start_time = time.time()

    def stop(self) -> None:
        """Stop the timer and record elapsed time."""
        if self._start_time is not None:
            self._elapsed = time.time() - self._start_time
            self._start_time = None

    @property
    def elapsed_seconds(self) -> float:
        """Get elapsed time in seconds."""
        if self._start_time is not None:
            # Timer is running
            return time.time() - self._start_time
        return self._elapsed

    @property
    def elapsed_formatted(self) -> str:
        """
        Get elapsed time formatted as MM:SS.

        Returns:
            Time string like "3:45" or "12:03"

        Examples:
            >>> timer = PracticeTimer()
            >>> timer._elapsed = 225.5  # 3 min 45.5 sec
            >>> timer.elapsed_formatted
            '3:45'
        """
        total_seconds = int(self.elapsed_seconds)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02d}"

    def reset(self) -> None:
        """Reset the timer."""
        self._start_time = None
        self._elapsed = 0.0


def format_time_delta(seconds: int) -> str:
    """
    Format seconds as a human-readable time string.

    Args:
        seconds: Number of seconds

    Returns:
        Formatted string like "2m 30s" or "1h 5m"

    Examples:
        >>> format_time_delta(150)
        '2m 30s'
        >>> format_time_delta(3665)
        '1h 1m 5s'
    """
    td = timedelta(seconds=seconds)
    hours, remainder = divmod(int(td.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)

    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if seconds > 0 or not parts:
        parts.append(f"{seconds}s")

    return " ".join(parts)
