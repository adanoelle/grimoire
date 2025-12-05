"""
CANTRIP 3: Substrings of Size Three with Distinct Characters (LeetCode #1876)

Target: < 2:00 | Difficulty: Easy

Count substrings of length 3 with all distinct characters.

Pattern: Fixed window of size 3
- Check if all 3 chars are different
- Can use set or manual comparison (set(window) has len 3)

Examples:
    >>> count_good_substrings("xyzzaz")
    1
    >>> count_good_substrings("aababcabc")
    4

Edge cases:
    - len(s) < 3: return 0
    - All characters the same: return 0
    - All distinct: return len(s) - 2
"""


def count_good_substrings(s: str) -> int:
    """Count substrings of length 3 with all distinct characters.

    Args:
        s: Input string.

    Returns:
        Count of "good" substrings.

    Time: O(n) - single pass
    Space: O(1) - set of max 3 elements is constant
    """
    pass  # Your solution here
