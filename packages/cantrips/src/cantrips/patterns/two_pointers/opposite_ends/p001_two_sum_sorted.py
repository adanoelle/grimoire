"""
CANTRIP 1: Two Sum II - Input Array Is Sorted (LeetCode #167)

Target: < 2:00 | Difficulty: Medium

Find two numbers in a sorted array that sum to target.
Return their 1-indexed positions.

Pattern: Opposite ends two pointers
- Left pointer at start, right at end
- Sum too small? Move left forward
- Sum too big? Move right backward

Examples:
    >>> two_sum_sorted([2, 7, 11, 15], 9)
    [1, 2]
    >>> two_sum_sorted([2, 3, 4], 6)
    [1, 3]
    >>> two_sum_sorted([-1, 0], -1)
    [1, 2]

Edge cases:
    - Answer at ends
    - Negative numbers
    - Duplicates in array
"""


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """Find two numbers in sorted array that sum to target.

    Args:
        nums: Sorted list of integers.
        target: Target sum.

    Returns:
        1-indexed positions of the two numbers.

    Time: O(n) - each pointer moves at most n times
    Space: O(1) - only two pointers
    """
    pass  # Your solution here
