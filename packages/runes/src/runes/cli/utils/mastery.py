"""
Mastery log parsing and manipulation utilities.

Functions to read, parse, and update mastery tracking logs in kata.py files.
"""

import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Optional

from ..domain import Result, Success, Failure, ParseError, FileSystemError, ValidationError
from ..domain.models import MasteryStatus, calculate_mastery_status


@dataclass
class PracticeSession:
    """A single practice session entry."""

    date: date
    kata_number: int
    time_str: str  # e.g., "3:45"
    bugs: int
    notes: str

    @property
    def time_seconds(self) -> int:
        """Convert time string to seconds."""
        parts = self.time_str.split(":")
        if len(parts) == 2:
            minutes, seconds = map(int, parts)
            return minutes * 60 + seconds
        return 0

    def __str__(self) -> str:
        """Format as table row."""
        return f"{self.date} | {self.kata_number}    | {self.time_str:5} | {self.bugs}    | {self.notes}"


@dataclass
class MasteryLog:
    """Parsed mastery tracking information from kata.py."""

    sessions: list[PracticeSession]
    checklist_items: list[str]  # Checklist items with [ ] or [x]
    full_content: str  # Original full content of kata.py
    warnings: list[str] = None  # Parse warnings (e.g., skipped malformed entries)

    def __post_init__(self):
        """Initialize warnings list if not provided."""
        if self.warnings is None:
            object.__setattr__(self, 'warnings', [])

    @property
    def total_sessions(self) -> int:
        """Total number of practice sessions."""
        return len(self.sessions)

    @property
    def last_session(self) -> Optional[PracticeSession]:
        """Most recent practice session."""
        return self.sessions[-1] if self.sessions else None

    @property
    def best_times(self) -> dict[int, int]:
        """Best time in seconds for each kata number."""
        best = {}
        for session in self.sessions:
            kata = session.kata_number
            time = session.time_seconds
            if kata not in best or time < best[kata]:
                best[kata] = time
        return best

    @property
    def total_bugs(self) -> dict[int, int]:
        """Total bugs for each kata number."""
        bugs = {}
        for session in self.sessions:
            kata = session.kata_number
            bugs[kata] = bugs.get(kata, 0) + session.bugs
        return bugs

    @property
    def status(self) -> MasteryStatus:
        """Calculate mastery status from practice history."""
        # TODO: Add logic to check if target times are met
        target_time_met = False  # Placeholder
        return calculate_mastery_status(self.total_sessions, target_time_met)


def parse_mastery_log(kata_file: Path) -> Result[MasteryLog, ParseError | FileSystemError]:
    """
    Parse mastery tracking section from kata.py file.

    Args:
        kata_file: Path to kata.py file

    Returns:
        Result containing MasteryLog or error

    Examples:
        >>> from pathlib import Path
        >>> # kata_file = Path("path/to/kata.py")
        >>> # result = parse_mastery_log(kata_file)
        >>> # if result.is_success():
        >>> #     log = result.unwrap()
    """
    # Handle file reading errors
    try:
        content = kata_file.read_text()
    except FileNotFoundError:
        return Failure(FileSystemError.file_not_found(kata_file))
    except PermissionError:
        return Failure(FileSystemError.permission_denied(kata_file))

    # Extract mastery tracking section
    mastery_match = re.search(
        r'# =+\s*\n# MASTERY TRACKING\s*\n# =+.*?""".*?"""',
        content,
        re.DOTALL,
    )

    if not mastery_match:
        # No mastery log found - could be new file or wrong format
        # Return empty log as Success (not an error, just no history yet)
        return Success(MasteryLog(sessions=[], checklist_items=[], full_content=content))

    mastery_section = mastery_match.group(0)

    # Parse practice log table
    # Support two formats:
    # 1. Date | Kata | Time | Bugs | Notes (5 columns)
    # 2. Date | Kata | Attempt # | Time | Bugs | Notes (6 columns)
    sessions = []
    warnings = []
    # Flexible pattern: optional middle column for attempt number
    log_pattern = r"(\d{4}-\d{2}-\d{2})\s*\|\s*(\d+)\s*\|\s*(?:\d+\s*\|\s*)?([\d:]+)\s*\|\s*(\d+)\s*\|\s*(.*?)$"

    line_num = 0
    for match in re.finditer(log_pattern, mastery_section, re.MULTILINE):
        line_num += 1
        date_str, kata_str, time_str, bugs_str, notes = match.groups()

        try:
            session_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            kata_num = int(kata_str.strip())
            bugs = int(bugs_str.strip())
            sessions.append(
                PracticeSession(
                    date=session_date,
                    kata_number=kata_num,
                    time_str=time_str.strip(),
                    bugs=bugs,
                    notes=notes.strip(),
                )
            )
        except ValueError as e:
            # Collect warning instead of silently skipping
            if "invalid literal" in str(e).lower():
                warnings.append(
                    f"Skipped entry at line {line_num}: invalid kata number '{kata_str.strip()}'"
                )
            elif "does not match format" in str(e):
                warnings.append(
                    f"Skipped entry at line {line_num}: invalid date '{date_str}'"
                )
            else:
                warnings.append(
                    f"Skipped entry at line {line_num}: {str(e)[:50]}"
                )
            continue
        except AttributeError:
            warnings.append(
                f"Skipped entry at line {line_num}: malformed data"
            )
            continue

    # Parse checklist items
    checklist_items = []
    checklist_pattern = r"\[[ x]\] .+$"
    for match in re.finditer(checklist_pattern, mastery_section, re.MULTILINE):
        checklist_items.append(match.group(0))

    return Success(
        MasteryLog(
            sessions=sessions,
            checklist_items=checklist_items,
            full_content=content,
            warnings=warnings,
        )
    )


def append_practice_session(
    kata_file: Path,
    kata_number: int,
    time_str: str,
    bugs: int,
    notes: str = "",
) -> Result[None, ValidationError | FileSystemError]:
    """
    Append a new practice session to the mastery log.

    Args:
        kata_file: Path to kata.py file
        kata_number: Which kata was practiced (1, 2, 3, etc.)
        time_str: Time taken (e.g., "3:45")
        bugs: Number of bugs encountered
        notes: Optional notes about the session

    Returns:
        Result indicating success or validation/filesystem error

    Examples:
        >>> from pathlib import Path
        >>> # kata_file = Path("path/to/kata.py")
        >>> # result = append_practice_session(kata_file, 1, "2:30", 0, "Clean run!")
        >>> # if result.is_success():
        >>> #     print("Session logged!")
    """
    # Validate inputs
    from ..domain.models import validate_time_string, validate_kata_number, validate_bugs_count

    is_valid, error_msg = validate_time_string(time_str)
    if not is_valid:
        return Failure(ValidationError.invalid_time_format(time_str))

    is_valid, error_msg = validate_kata_number(kata_number)
    if not is_valid:
        return Failure(ValidationError.invalid_kata_number(kata_number, 10))

    is_valid, error_msg = validate_bugs_count(bugs)
    if not is_valid:
        return Failure(ValidationError.negative_bugs(bugs))

    # Read file
    try:
        content = kata_file.read_text()
    except FileNotFoundError:
        return Failure(FileSystemError.file_not_found(kata_file))
    except PermissionError:
        return Failure(FileSystemError.permission_denied(kata_file))

    # Find the log table
    log_header_pattern = r"(Date\s+\|\s+Kata\s+\|\s+Time\s+\|\s+Bugs\s+\|\s+Notes\s*\n[^\n]+\n)"

    header_match = re.search(log_header_pattern, content)
    if not header_match:
        # Can't find log table - file might not have mastery section yet
        return Failure(ParseError.no_mastery_section(kata_file))

    # Create new entry
    today = date.today().strftime("%Y-%m-%d")
    new_entry = f"{today} | {kata_number}    | {time_str:5} | {bugs}    | {notes}\n"

    # Find insertion point (after the header divider)
    header_end = header_match.end()

    # Insert new entry
    new_content = content[:header_end] + new_entry + content[header_end:]

    # Write back
    try:
        kata_file.write_text(new_content)
    except PermissionError:
        return Failure(FileSystemError.permission_denied(kata_file))

    return Success(None)


def get_practice_summary(log: MasteryLog) -> dict[str, any]:
    """
    Generate summary statistics from mastery log.

    Args:
        log: MasteryLog object

    Returns:
        Dictionary with summary stats:
        - total_sessions: int
        - last_practice: date or None
        - best_times: dict[kata_num -> seconds]
        - total_bugs: dict[kata_num -> count]
        - recent_streak: int (consecutive days)

    Examples:
        >>> log = MasteryLog(sessions=[], checklist_items=[], full_content="")
        >>> summary = get_practice_summary(log)
        >>> summary["total_sessions"]
        0
    """
    if not log.sessions:
        return {
            "total_sessions": 0,
            "last_practice": None,
            "best_times": {},
            "total_bugs": {},
            "recent_streak": 0,
        }

    # Calculate streak
    dates = sorted(set(s.date for s in log.sessions), reverse=True)
    streak = 0
    if dates:
        current_date = date.today()
        for practice_date in dates:
            delta = (current_date - practice_date).days
            if delta == streak:
                streak += 1
            else:
                break

    return {
        "total_sessions": log.total_sessions,
        "last_practice": log.last_session.date if log.last_session else None,
        "best_times": log.best_times,
        "total_bugs": log.total_bugs,
        "recent_streak": streak,
    }
