"""
Kata pattern discovery utilities.

Functions to find and analyze kata patterns in the algorithms directory.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from ..domain import Result, Success, Failure, FileSystemError


@dataclass
class KataPattern:
    """Information about a kata pattern."""

    name: str  # e.g., "two_pointers/opposite_ends"
    path: Path  # Path to pattern directory
    kata_file: Path  # Path to kata.py
    test_file: Optional[Path]  # Path to test_kata.py (if exists)
    has_pytest: bool  # Whether pattern has pytest tests
    has_justfile: bool  # Whether pattern has local justfile
    category: str  # e.g., "two_pointers"
    pattern: str  # e.g., "opposite_ends"

    @property
    def display_name(self) -> str:
        """Return formatted display name."""
        return f"{self.category}/{self.pattern}"

    @property
    def is_migrated(self) -> bool:
        """Return True if pattern has been migrated to pytest."""
        return self.has_pytest


def get_algorithms_dir() -> Path:
    """
    Get the algorithms directory path.

    Returns:
        Path to packages/runes/src/runes/algorithms/

    Raises:
        FileNotFoundError: If algorithms directory not found
    """
    # Find from current file location
    current = Path(__file__)
    runes_dir = current.parent.parent.parent  # Up to src/runes/
    algorithms_dir = runes_dir / "algorithms"

    if not algorithms_dir.exists():
        raise FileNotFoundError(f"Algorithms directory not found: {algorithms_dir}")

    return algorithms_dir


def find_all_kata_patterns() -> list[KataPattern]:
    """
    Find all kata patterns in the algorithms directory.

    Returns:
        List of KataPattern objects, sorted by name

    Examples:
        >>> patterns = find_all_kata_patterns()
        >>> len(patterns) >= 1
        True
        >>> any(p.name == "two_pointers/opposite_ends" for p in patterns)
        True
    """
    algorithms_dir = get_algorithms_dir()
    patterns = []

    # Find all kata.py files
    for kata_file in sorted(algorithms_dir.glob("**/kata.py")):
        pattern_dir = kata_file.parent
        category_dir = pattern_dir.parent

        # Extract names
        category = category_dir.name
        pattern = pattern_dir.name
        name = f"{category}/{pattern}"

        # Check for companion files
        test_file = pattern_dir / "test_kata.py"
        justfile = pattern_dir / "justfile"

        patterns.append(
            KataPattern(
                name=name,
                path=pattern_dir,
                kata_file=kata_file,
                test_file=test_file if test_file.exists() else None,
                has_pytest=test_file.exists(),
                has_justfile=justfile.exists(),
                category=category,
                pattern=pattern,
            )
        )

    return sorted(patterns, key=lambda p: p.name)


def find_kata_pattern(pattern_name: str) -> Result[KataPattern, FileSystemError]:
    """
    Find a specific kata pattern by name.

    Args:
        pattern_name: Pattern name (e.g., "opposite_ends" or "two_pointers/opposite_ends")

    Returns:
        Result containing KataPattern if found, or FileSystemError if not found

    Examples:
        >>> result = find_kata_pattern("opposite_ends")
        >>> result.is_success()
        True
        >>> result = find_kata_pattern("two_pointers/opposite_ends")
        >>> result.is_success()
        True
        >>> result = find_kata_pattern("nonexistent")
        >>> result.is_failure()
        True
    """
    patterns = find_all_kata_patterns()

    # Try exact match first
    for pattern in patterns:
        if pattern.name == pattern_name:
            return Success(pattern)

    # Try matching just the pattern name (without category)
    for pattern in patterns:
        if pattern.pattern == pattern_name:
            return Success(pattern)

    # Try case-insensitive match
    pattern_lower = pattern_name.lower()
    for pattern in patterns:
        if pattern.name.lower() == pattern_lower or pattern.pattern.lower() == pattern_lower:
            return Success(pattern)

    # Not found - create descriptive error
    return Failure(
        FileSystemError(
            f"Pattern '{pattern_name}' not found",
            details={"pattern": pattern_name, "reason": "not_found"}
        )
    )


def get_pattern_display_info(pattern: KataPattern) -> dict[str, str]:
    """
    Get display information for a kata pattern.

    Args:
        pattern: KataPattern object

    Returns:
        Dictionary with display fields:
        - status: "Migrated" or "Legacy"
        - test_mode: "pytest" or "doctest"
        - justfile: "✓" or "✗"

    Examples:
        >>> pattern = find_kata_pattern("opposite_ends")
        >>> info = get_pattern_display_info(pattern)
        >>> "status" in info
        True
    """
    return {
        "status": "Migrated" if pattern.is_migrated else "Legacy",
        "test_mode": "pytest" if pattern.has_pytest else "doctest",
        "justfile": "✓" if pattern.has_justfile else "✗",
    }
