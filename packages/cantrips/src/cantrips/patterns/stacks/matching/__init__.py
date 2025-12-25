"""Stack matching pattern cantrips.

Use stack matching when:
- Need to match pairs (parentheses, brackets, braces, tags)
- Balanced expressions or nested structures
- "Valid" or "balanced" in problem description
- Most recent opening must match next closing (LIFO behavior)
"""

from .p001_valid_parentheses import is_valid
from .p002_remove_duplicates import remove_duplicates
from .p003_make_good import make_good
from .p004_min_remove_valid import min_remove_to_make_valid
from .p005_longest_valid_parens import longest_valid_parentheses

__all__ = [
    "is_valid",
    "remove_duplicates",
    "make_good",
    "min_remove_to_make_valid",
    "longest_valid_parentheses",
]
