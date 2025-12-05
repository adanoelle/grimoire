"""
CANTRIP 5: Container With Most Water (LeetCode #11)

Target: < 3:00 | Difficulty: Medium

Find two lines that form container holding most water.

Pattern: Greedy two pointers
- Start with widest container
- Move pointer with shorter height (can't do worse)

Examples:
    >>> max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    49
    >>> max_area([1, 1])
    1

Edge cases:
    - Two elements: base case
    - All same height: width matters
    - Monotonically increasing/decreasing
"""


def max_area(height: list[int]) -> int:
    """Find maximum water container area.

    Args:
        height: List of line heights.

    Returns:
        Maximum area between two lines.

    Time: O(n) - single pass with two pointers
    Space: O(1) - only two pointers
    """
    pass  # Your solution here
