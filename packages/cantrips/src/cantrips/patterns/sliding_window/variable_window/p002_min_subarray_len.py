"""
CANTRIP 2: Minimum Size Subarray Sum (LeetCode #209)

Target: < 3:30 | Difficulty: Medium

Find the minimal length of a subarray whose sum is >= target.
Return 0 if no such subarray exists.

Pattern: Variable window - expand to meet target, contract to minimize
- Expand by adding right element
- Contract while sum >= target (recording min length)

Examples:
    >>> min_subarray_len(7, [2, 3, 1, 2, 4, 3])
    2
    >>> min_subarray_len(4, [1, 4, 4])
    1
    >>> min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1])
    0

Edge cases:
    - No subarray meets target: return 0
    - Single element >= target: return 1
    - Entire array needed: return len(nums)
    - All elements positive (guaranteed)
"""


def min_subarray_len(target: int, nums: list[int]) -> int:
    """Find minimal length subarray with sum >= target.

    Args:
        target: Minimum sum threshold.
        nums: List of positive integers.

    Returns:
        Minimal subarray length, or 0 if impossible.

    Time: O(n) - each element processed at most twice
    Space: O(1) - only tracking sum and pointers
    """
    pass  # Your solution here
