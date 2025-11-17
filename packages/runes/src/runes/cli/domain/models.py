"""
Domain models for kata practice system.

Business logic and status calculations.
"""

from enum import Enum


class MasteryStatus(str, Enum):
    """Mastery level for a kata pattern."""

    LEARNING = "Learning"
    PRACTICING = "Practicing"
    MASTERED = "Mastered"

    @property
    def display_color(self) -> str:
        """Get Rich color for this status."""
        return {
            MasteryStatus.LEARNING: "white",
            MasteryStatus.PRACTICING: "yellow",
            MasteryStatus.MASTERED: "bold green",
        }[self]


def calculate_mastery_status(total_sessions: int, target_time_met: bool = False) -> MasteryStatus:
    """
    Calculate mastery status from practice sessions.

    Args:
        total_sessions: Total number of practice sessions
        target_time_met: Whether target time has been consistently met

    Returns:
        MasteryStatus enum value

    Business Rules:
        - Learning: < 5 sessions
        - Practicing: 5-19 sessions
        - Mastered: 20+ sessions AND target time met
    """
    if total_sessions < 5:
        return MasteryStatus.LEARNING
    elif total_sessions < 20:
        return MasteryStatus.PRACTICING
    else:
        # For mastery, should also check if target times are met
        # For now, just session count (can enhance later)
        return MasteryStatus.MASTERED if target_time_met else MasteryStatus.PRACTICING


def validate_time_string(time_str: str) -> tuple[bool, str]:
    """
    Validate time string format.

    Args:
        time_str: Time string to validate (e.g., "3:45" or "12:03")

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> validate_time_string("3:45")
        (True, '')
        >>> validate_time_string("invalid")
        (False, 'Time must be in M:SS or MM:SS format')
        >>> validate_time_string("3:5")
        (False, 'Seconds must be two digits (00-59)')
    """
    import re

    # Match M:SS or MM:SS format
    match = re.match(r"^(\d{1,2}):(\d{2})$", time_str)

    if not match:
        return False, "Time must be in M:SS or MM:SS format"

    minutes, seconds = match.groups()
    sec_int = int(seconds)

    if sec_int >= 60:
        return False, "Seconds must be 00-59"

    return True, ""


def validate_kata_number(kata_num: int, max_katas: int = 10) -> tuple[bool, str]:
    """
    Validate kata number.

    Args:
        kata_num: Kata number to validate
        max_katas: Maximum number of katas (default 10)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if kata_num < 1:
        return False, f"Kata number must be >= 1"

    if kata_num > max_katas:
        return False, f"Kata number must be <= {max_katas}"

    return True, ""


def validate_bugs_count(bugs: int) -> tuple[bool, str]:
    """
    Validate bug count.

    Args:
        bugs: Number of bugs

    Returns:
        Tuple of (is_valid, error_message)
    """
    if bugs < 0:
        return False, "Bug count cannot be negative"

    if bugs > 100:
        return False, "Bug count seems unrealistic (> 100)"

    return True, ""
