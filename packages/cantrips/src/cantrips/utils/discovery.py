"""Pattern discovery utilities.

This module provides functions for discovering cantrip patterns in the
filesystem and loading their metadata for display in the TUI.

Example:
    >>> from cantrips.utils.discovery import discover_patterns
    >>> patterns = discover_patterns()
    >>> for p in patterns:
    ...     print(f"{p.category}/{p.name}: {len(p.cantrips)} cantrips")
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator
import importlib.util
import ast


# Default patterns directory (relative to package)
PATTERNS_DIR = Path(__file__).parent.parent / "patterns"


@dataclass
class CantripsInfo:
    """Information about a single cantrip problem.

    Attributes:
        number: The cantrip number (1-5).
        name: Function name (e.g., "find_max_average").
        title: Human-readable title (e.g., "Maximum Average Subarray I").
        target_time: Target completion time in seconds.
        difficulty: Problem difficulty (Easy, Medium, Hard).
        leetcode_id: LeetCode problem number if applicable.
        file_path: Path to the cantrip file.
    """

    number: int
    name: str
    title: str
    target_time: int = 120  # 2 minutes default
    difficulty: str = "Medium"
    leetcode_id: int | None = None
    file_path: Path | None = None


@dataclass
class PatternInfo:
    """Information about a cantrip pattern.

    Attributes:
        name: Pattern name (e.g., "fixed_window").
        category: Pattern category (e.g., "sliding_window").
        display_name: Human-readable name.
        path: Path to the pattern directory.
        cantrips: List of cantrips in this pattern.
        has_tests: Whether test file exists.
        description: Brief description of the pattern.
    """

    name: str
    category: str
    display_name: str
    path: Path
    cantrips: list[CantripsInfo] = field(default_factory=list)
    has_tests: bool = False
    description: str = ""

    @property
    def full_name(self) -> str:
        """Get the full pattern name (category/name)."""
        return f"{self.category}/{self.name}"

    @property
    def cantrip_count(self) -> int:
        """Get the number of cantrips in this pattern."""
        return len(self.cantrips)


def discover_patterns(patterns_dir: Path | None = None) -> list[PatternInfo]:
    """Discover all cantrip patterns in the patterns directory.

    Scans the patterns directory for pattern folders and extracts
    metadata about each pattern and its cantrips.

    Args:
        patterns_dir: Optional path to patterns directory. Defaults to
            the package's patterns directory.

    Returns:
        List of PatternInfo objects sorted by category and name.

    Example:
        >>> patterns = discover_patterns()
        >>> len(patterns) > 0
        True
    """
    if patterns_dir is None:
        patterns_dir = PATTERNS_DIR

    if not patterns_dir.exists():
        return []

    patterns: list[PatternInfo] = []

    # Scan for category directories
    for category_dir in sorted(patterns_dir.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith("_"):
            continue

        category = category_dir.name

        # Scan for pattern directories within category
        for pattern_dir in sorted(category_dir.iterdir()):
            if not pattern_dir.is_dir() or pattern_dir.name.startswith("_"):
                continue

            pattern = _load_pattern(pattern_dir, category)
            if pattern:
                patterns.append(pattern)

    return patterns


def _load_pattern(pattern_dir: Path, category: str) -> PatternInfo | None:
    """Load pattern information from a directory.

    Args:
        pattern_dir: Path to the pattern directory.
        category: The category this pattern belongs to.

    Returns:
        PatternInfo object or None if invalid pattern.
    """
    name = pattern_dir.name
    display_name = name.replace("_", " ").title()

    pattern = PatternInfo(
        name=name,
        category=category,
        display_name=display_name,
        path=pattern_dir,
    )

    # Check for test file
    test_file = pattern_dir / "test_cantrips.py"
    pattern.has_tests = test_file.exists()

    # Load cantrips (look for p[0-9][0-9][0-9]_*.py files)
    for cantrip_file in sorted(pattern_dir.glob("p[0-9][0-9][0-9]_*.py")):
        cantrip = _load_cantrip(cantrip_file)
        if cantrip:
            pattern.cantrips.append(cantrip)

    # Load description from README if present
    readme = pattern_dir / "README.md"
    if readme.exists():
        try:
            content = readme.read_text()
            # Extract first paragraph as description
            lines = content.split("\n\n")[0].split("\n")
            # Skip header line if starts with #
            desc_lines = [l for l in lines if not l.startswith("#")]
            pattern.description = " ".join(desc_lines).strip()
        except Exception:
            pass

    return pattern


def _load_cantrip(file_path: Path) -> CantripsInfo | None:
    """Load cantrip information from a file.

    Extracts metadata from the cantrip file's docstring and function.

    Args:
        file_path: Path to the cantrip file.

    Returns:
        CantripsInfo object or None if invalid.
    """
    try:
        # Parse the filename: p001_function_name.py
        stem = file_path.stem  # e.g., "p001_find_max_average"

        if not stem.startswith("p") or len(stem) < 5:
            return None

        num_part = stem[1:4]  # "001"
        if not num_part.isdigit():
            return None

        number = int(num_part)
        func_name = stem[5:]  # everything after "p001_"

        # Parse the file to extract docstring info
        content = file_path.read_text()
        tree = ast.parse(content)

        # Get module docstring
        title = func_name.replace("_", " ").title()
        target_time = 120
        difficulty = "Medium"
        leetcode_id = None

        # Try to extract from module docstring
        if tree.body and isinstance(tree.body[0], ast.Expr):
            if isinstance(tree.body[0].value, ast.Constant):
                docstring = tree.body[0].value.value
                title, target_time, difficulty, leetcode_id = _parse_docstring(
                    docstring, title, target_time, difficulty, leetcode_id
                )

        return CantripsInfo(
            number=number,
            name=func_name,
            title=title,
            target_time=target_time,
            difficulty=difficulty,
            leetcode_id=leetcode_id,
            file_path=file_path,
        )
    except Exception:
        return None


def _parse_docstring(
    docstring: str,
    default_title: str,
    default_time: int,
    default_difficulty: str,
    default_leetcode: int | None,
) -> tuple[str, int, str, int | None]:
    """Parse cantrip metadata from docstring.

    Args:
        docstring: The docstring to parse.
        default_title: Default title if not found.
        default_time: Default target time if not found.
        default_difficulty: Default difficulty if not found.
        default_leetcode: Default LeetCode ID if not found.

    Returns:
        Tuple of (title, target_time, difficulty, leetcode_id).
    """
    title = default_title
    target_time = default_time
    difficulty = default_difficulty
    leetcode_id = default_leetcode

    lines = docstring.strip().split("\n")

    for line in lines:
        line = line.strip()

        # Look for title line (first non-empty, non-marker line)
        if line and not line.startswith(("CANTRIP", "Target", "⏱", "🎯", "Difficulty")):
            if "LeetCode" in line or "LC #" in line:
                # Extract title from "Title (LeetCode #123)" format
                if "(" in line:
                    title = line.split("(")[0].strip()
                # Extract LeetCode ID
                import re
                match = re.search(r"#(\d+)", line)
                if match:
                    leetcode_id = int(match.group(1))
            elif not title or title == default_title:
                title = line

        # Look for target time
        if "Target" in line or "⏱" in line:
            import re
            match = re.search(r"(\d+)\s*(?:min|minute)", line)
            if match:
                target_time = int(match.group(1)) * 60
            else:
                match = re.search(r"<\s*(\d+):(\d+)", line)
                if match:
                    target_time = int(match.group(1)) * 60 + int(match.group(2))

        # Look for difficulty
        if "Easy" in line:
            difficulty = "Easy"
        elif "Hard" in line:
            difficulty = "Hard"
        elif "Medium" in line:
            difficulty = "Medium"

    return title, target_time, difficulty, leetcode_id


def get_pattern(pattern_name: str, patterns_dir: Path | None = None) -> PatternInfo | None:
    """Get a specific pattern by name.

    Args:
        pattern_name: Pattern name in "category/name" format.
        patterns_dir: Optional path to patterns directory.

    Returns:
        PatternInfo or None if not found.

    Example:
        >>> pattern = get_pattern("sliding_window/fixed_window")
        >>> pattern.display_name if pattern else "Not found"
        'Fixed Window'
    """
    if "/" not in pattern_name:
        return None

    category, name = pattern_name.split("/", 1)

    if patterns_dir is None:
        patterns_dir = PATTERNS_DIR

    pattern_dir = patterns_dir / category / name
    if pattern_dir.exists():
        return _load_pattern(pattern_dir, category)

    return None


def get_cantrip_file(
    pattern_name: str,
    cantrip_number: int,
    patterns_dir: Path | None = None,
) -> Path | None:
    """Get the file path for a specific cantrip.

    Args:
        pattern_name: Pattern name in "category/name" format.
        cantrip_number: Cantrip number (1-5).
        patterns_dir: Optional path to patterns directory.

    Returns:
        Path to the cantrip file or None if not found.
    """
    pattern = get_pattern(pattern_name, patterns_dir)
    if not pattern:
        return None

    for cantrip in pattern.cantrips:
        if cantrip.number == cantrip_number:
            return cantrip.file_path

    return None
