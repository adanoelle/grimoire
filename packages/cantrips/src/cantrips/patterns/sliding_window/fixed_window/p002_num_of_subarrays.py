"""
CANTRIP 2: Number of Sub-arrays of Size K and Average >= Threshold (LeetCode #1343)

Target: < 2:30 | Difficulty: Medium

Count subarrays of size k where average >= threshold.

Pattern: Fixed-size sliding window with counting
- Same sliding technique as Cantrip 1
- Count windows where sum >= threshold * k (avoid division)

Examples:
    >>> num_of_subarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
    3
    >>> num_of_subarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5)
    6

Edge cases:
    - No subarrays meet threshold: return 0
    - All subarrays meet threshold: return len(arr) - k + 1
    - threshold == 0: all subarrays qualify
    - Negative numbers in array
"""


def num_of_subarrays(nums: list[int], k: int, threshold: int) -> int:
    """Count subarrays of size k with average >= threshold.

    Args:
        nums: List of integers.
        k: Size of the sliding window.
        threshold: Minimum average threshold.

    Returns:
        Count of qualifying subarrays.

    Time: O(n) - single pass
    Space: O(1) - only tracking sum and count
    """
    window_sum = sum(nums[:k])
    counts = 0
    if window_sum / k >= threshold:
        counts += 1

    left = 0
    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[left]
        left += 1

        if window_sum / k >= threshold:
            counts += 1

    return counts
