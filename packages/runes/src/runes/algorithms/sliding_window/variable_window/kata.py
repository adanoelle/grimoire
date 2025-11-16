"""
Sliding Window (Variable Size) - Daily Kata Practice

🥋 Master the expand-contract dance

Pattern: Expand with right, contract with left when constraint violated.
"""


def longest_substring_no_repeat(s: str) -> int:
    """
    KATA 1: Longest substring without repeating chars (LC #3)

    ⏱️  Target time: < 3 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Strategy:
    - Expand: add char at right to set
    - Contract: if duplicate, remove from left until no duplicate
    - Track max length

    Edge cases:
    - Empty string → 0
    - All same character → 1
    - No repeats → len(s)

    Examples:
        >>> longest_substring_no_repeat("abcabcbb")
        3
        >>> longest_substring_no_repeat("bbbbb")
        1
        >>> longest_substring_no_repeat("pwwkew")
        3
        >>> longest_substring_no_repeat("")
        0

    START CODING BELOW:
    """
    pass

def min_subarray_sum_geq_target(nums: list[int], target: int) -> int:
    """
    KATA 2: Minimum subarray with sum ≥ target (LC #209)

    ⏱️  Target time: < 3 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Strategy:
    - Expand: add nums[right] to sum
    - Contract: while sum ≥ target, shrink from left
    - Track minimum length

    Edge cases:
    - No valid subarray → return 0
    - Single element ≥ target → return 1

    Examples:
        >>> min_subarray_sum_geq_target([2, 3, 1, 2, 4, 3], 7)
        2
        >>> min_subarray_sum_geq_target([1, 4, 4], 4)
        1
        >>> min_subarray_sum_geq_target([1, 1, 1], 11)
        0

    START CODING BELOW:
    """
    pass

def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    KATA 3: Longest substring with ≤ k distinct chars (LC #340)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(n) time, O(k) space

    Strategy:
    - Use dict/defaultdict to count characters
    - Expand: add char to count
    - Contract: while distinct > k, remove from left
    - Track max length

    Examples:
        >>> longest_substring_k_distinct("eceba", 2)
        3
        >>> longest_substring_k_distinct("aa", 1)
        2

    START CODING BELOW:
    """
    pass

def max_consecutive_ones_k_flips(nums: list[int], k: int) -> int:
    """
    KATA 4: Max consecutive 1s with at most k flips (LC #1004)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    You can flip at most k zeros to ones. Find longest subarray of 1s.

    Strategy:
    - Expand: count zeros in window
    - Contract: while zeros > k, shrink from left
    - Track max window size

    Examples:
        >>> max_consecutive_ones_k_flips([1,1,1,0,0,0,1,1,1,1,0], 2)
        6
        >>> max_consecutive_ones_k_flips([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
        10

    START CODING BELOW:
    """
    pass

# ============================================================================
# MASTERY TRACKING
# ============================================================================

"""
MASTERY CHECKLIST:
[ ] Kata 1: Can code in < 3 min, zero bugs
[ ] Kata 2: Can code in < 3 min, zero bugs
[ ] Kata 3: Can code in < 4 min, zero bugs
[ ] Kata 4: Can code in < 4 min, zero bugs
[ ] Understand expand-contract pattern deeply
[ ] Know when to expand vs contract
[ ] Recognize variable window pattern (< 30 sec)

PRACTICE LOG:
Date       | Kata | Time  | Bugs | Notes
-----------|------|-------|------|---------------------------------------


BREATHING KNOWLEDGE:
[ ] All 4 katas in under 13 minutes total
[ ] Zero bugs
[ ] Can explain expand-contract while coding
[ ] Pattern recognition automatic
"""


if __name__ == "__main__":
    import doctest

    print("=" * 60)
    print("SLIDING WINDOW (VARIABLE SIZE) - KATA PRACTICE")
    print("=" * 60)
    print()

    results = doctest.testmod()

    if results.failed == 0:
        print("✅ All tests passed!")
        print(f"   {results.attempted} tests run")
        print()
        print("🎯 Master expand-contract: grow window, shrink when constraint breaks!")
    else:
        print(f"❌ {results.failed} test(s) failed")
        print("Debug and retry!")

    print()
    print("=" * 60)
