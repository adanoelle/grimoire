"""
CANTRIP 1: Maximum Average Subarray I (LeetCode #643)

Target: < 2:00 | Difficulty: Easy

Find contiguous subarray of length k with maximum average value.
Return the maximum average.

Pattern: Fixed-size sliding window
- Initialize window with first K elements
- Slide: Remove left, add right
- Track running sum (convert to average at end)

Examples:
    >>> find_max_average([1, 12, -5, -6, 50, 3], 4)
    12.75
    >>> find_max_average([5], 1)
    5.0

Edge cases:
    - k == len(nums): return average of entire array
    - k == 1: return max element
    - All elements equal: return that value
    - Negative numbers: handle correctly
"""


def find_max_average(nums: list[int], k: int) -> float:
    """Find the maximum average of any contiguous subarray of size k.

    Args:
        nums: List of integers.
        k: Size of the sliding window.

    Returns:
        Maximum average as a float.

    Time: O(n) - single pass through array
    Space: O(1) - only tracking sum and max
    """
    pass  # Your solution here
