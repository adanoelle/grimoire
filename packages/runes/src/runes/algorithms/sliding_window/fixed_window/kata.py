"""
Sliding Window (Fixed Size) - Daily Kata Practice

🥋 Master the expand-contract rhythm

Key pattern: Remove left element, add right element, update result.
"""


def max_sum_subarray_size_k(nums: list[int], k: int) -> int:
    """
    KATA 1: Maximum sum of k consecutive elements

    ⏱️  Target time: < 2 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Common mistakes:
    - Recalculating entire window sum each time (O(n²))
    - Off-by-one in window boundaries
    - Not handling k > len(nums)

    Edge cases:
    - k > len(nums)
    - k == len(nums)
    - All negative numbers
    - Single element

    Examples:
        >>> max_sum_subarray_size_k([2, 1, 5, 1, 3, 2], 3)
        9
        >>> max_sum_subarray_size_k([2, 3, 4, 1, 5], 2)
        7
        >>> max_sum_subarray_size_k([-1, -2, -3], 2)
        -3

    START CODING BELOW:
    """
    pass

def average_of_subarrays_size_k(nums: list[int], k: int) -> list[float]:
    """
    KATA 2: Average of each subarray of size k (LC #643)

    ⏱️  Target time: < 3 minutes
    🎯 Goal: Zero bugs, return all averages

    Examples:
        >>> average_of_subarrays_size_k([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
        [2.2, 2.8, 2.4, 3.6, 2.8]

    START CODING BELOW:
    """
    pass

def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    KATA 3: Contains duplicate within k distance (LC #219)

    ⏱️  Target time: < 3 minutes
    🎯 Goal: Zero bugs, O(n) time, O(k) space

    Return True if there are duplicates within distance k.

    Strategy: Use a set as sliding window to track last k elements.

    Examples:
        >>> contains_nearby_duplicate([1, 2, 3, 1], 3)
        True
        >>> contains_nearby_duplicate([1, 0, 1, 1], 1)
        True
        >>> contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)
        False

    START CODING BELOW:
    """
    pass

# ============================================================================
# MASTERY TRACKING
# ============================================================================

"""
MASTERY CHECKLIST:
[ ] Kata 1: Can code in < 2 min, zero bugs
[ ] Kata 2: Can code in < 3 min, zero bugs
[ ] Kata 3: Can code in < 3 min, zero bugs
[ ] Understand the slide rhythm (remove left, add right)
[ ] Never recalculate entire window
[ ] Recognize fixed window pattern (< 30 sec)

PRACTICE LOG:
Date       | Kata | Time  | Bugs | Notes
-----------|------|-------|------|---------------------------------------


BREATHING KNOWLEDGE:
[ ] All 3 katas in under 7 minutes total
[ ] Zero bugs
[ ] Can explain the pattern while coding
"""


if __name__ == "__main__":
    import doctest

    print("=" * 60)
    print("SLIDING WINDOW (FIXED SIZE) - KATA PRACTICE")
    print("=" * 60)
    print()

    results = doctest.testmod()

    if results.failed == 0:
        print("✅ All tests passed!")
        print(f"   {results.attempted} tests run")
        print()
        print("🎯 Master the slide rhythm: remove left, add right!")
    else:
        print(f"❌ {results.failed} test(s) failed")
        print("Debug and retry!")

    print()
    print("=" * 60)
