"""
CANTRIP 5: Subarray Product Less Than K (LeetCode #713)

Target: < 4:30 | Difficulty: Medium

Count number of contiguous subarrays where product < k.

Pattern: Variable window with product tracking
- For each right position, count ALL valid subarrays ending at right
- Number of subarrays = (right - left + 1)

Examples:
    >>> num_subarray_product_less_than_k([10, 5, 2, 6], 100)
    8
    >>> num_subarray_product_less_than_k([1, 2, 3], 0)
    0

Edge cases:
    - k <= 1: return 0 (all products >= 1 for positive nums)
    - Single element < k: counts as 1
    - Product becomes >= k: shrink window
"""


def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    """Count subarrays with product less than k.

    Args:
        nums: List of positive integers.
        k: Product threshold.

    Returns:
        Count of valid subarrays.

    Time: O(n) - single pass
    Space: O(1) - only tracking product and pointers
    """
    pass  # Your solution here
