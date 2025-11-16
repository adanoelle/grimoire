"""
Binary Search - Daily Kata Practice

🥋 THE MOST CRITICAL ALGORITHM TO MASTER

Binary search is prone to off-by-one errors. Practice until PERFECT.
You should be able to code this in your sleep, zero bugs, every time.

Goal: Code classic binary search 100 times until muscle memory.
"""


def binary_search_classic(nums: list[int], target: int) -> int:
    """
    KATA 1: Classic binary search

    ⏱️  Target time: < 2 minutes
    🎯 Goal: ZERO bugs (this is non-negotiable)

    Common mistakes:
    - Using left < right instead of left <= right
    - Using mid instead of mid ± 1 for left/right update
    - Integer overflow in (left + right) / 2 (use left + (right-left)//2)

    Edge cases:
    - Empty array
    - Single element
    - Target not in array
    - Target at start/end

    Examples:
        >>> binary_search_classic([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search_classic([1, 2, 3, 4, 5], 6)
        -1
        >>> binary_search_classic([], 1)
        -1
        >>> binary_search_classic([5], 5)
        0

    START CODING BELOW:
    """
    pass

def find_first_occurrence(nums: list[int], target: int) -> int:
    """
    KATA 2: Find FIRST occurrence of target

    ⏱️  Target time: < 3 minutes
    🎯 Goal: Zero bugs, find leftmost occurrence

    Key difference: Don't return immediately. Keep searching left!

    Edge cases:
    - No duplicates → same as classic search
    - All same elements
    - Target at start/end

    Examples:
        >>> find_first_occurrence([1, 2, 2, 2, 3], 2)
        1
        >>> find_first_occurrence([2, 2, 2, 2, 2], 2)
        0
        >>> find_first_occurrence([1, 2, 3], 4)
        -1

    START CODING BELOW:
    """
    pass

def find_last_occurrence(nums: list[int], target: int) -> int:
    """
    KATA 3: Find LAST occurrence of target

    ⏱️  Target time: < 3 minutes
    🎯 Goal: Zero bugs, find rightmost occurrence

    Opposite of kata 2: Keep searching right after finding.

    Examples:
        >>> find_last_occurrence([1, 2, 2, 2, 3], 2)
        3
        >>> find_last_occurrence([2, 2, 2, 2, 2], 2)
        4
        >>> find_last_occurrence([1, 2, 3], 4)
        -1

    START CODING BELOW:
    """
    pass

def search_insert_position(nums: list[int], target: int) -> int:
    """
    KATA 4: Search insert position (LC #35)

    ⏱️  Target time: < 2 minutes
    🎯 Goal: Zero bugs

    Return index where target should be inserted to maintain order.

    Examples:
        >>> search_insert_position([1, 3, 5, 6], 5)
        2
        >>> search_insert_position([1, 3, 5, 6], 2)
        1
        >>> search_insert_position([1, 3, 5, 6], 7)
        4
        >>> search_insert_position([1, 3, 5, 6], 0)
        0

    START CODING BELOW:
    """
    pass

def search_rotated_array(nums: list[int], target: int) -> int:
    """
    KATA 5: Search in rotated sorted array (LC #33)

    ⏱️  Target time: < 5 minutes
    🎯 Goal: Zero bugs, O(log n) time

    This is ADVANCED! Master kata 1-4 first.

    Array is sorted but rotated: [4,5,6,7,0,1,2]

    Strategy:
    1. Find which half is sorted (left or right)
    2. Check if target is in sorted half
    3. If yes, search that half; if no, search other half

    Examples:
        >>> search_rotated_array([4,5,6,7,0,1,2], 0)
        4
        >>> search_rotated_array([4,5,6,7,0,1,2], 3)
        -1
        >>> search_rotated_array([1], 0)
        -1

    START CODING BELOW:
    """
    pass

def find_peak_element(nums: list[int]) -> int:
    """
    KATA 6: Find peak element (LC #162)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(log n) time

    Peak: nums[i] > nums[i-1] and nums[i] > nums[i+1]

    Key insight: Always move toward higher neighbor (guaranteed peak exists).

    Examples:
        >>> find_peak_element([1, 2, 3, 1])
        2
        >>> find_peak_element([1, 2, 1, 3, 5, 6, 4])
        5

    START CODING BELOW:
    """
    pass

# ============================================================================
# MASTERY TRACKING
# ============================================================================

"""
🎯 BINARY SEARCH MASTERY GOAL:
Code classic binary search 100 times until you can do it perfectly,
with zero bugs, in under 2 minutes, WITH YOUR EYES CLOSED.

This is not hyperbole. True mastery means muscle memory.

PRACTICE LOG (Track every attempt):
Date       | Kata | Attempt # | Time  | Bugs | Notes
-----------|------|-----------|-------|------|------------------------
2025-11-16 | 1    | 1         | 4:30  | 2    | Used left<right, off-by-one
2025-11-16 | 1    | 2         | 3:15  | 1    | Forgot mid calculation
2025-11-17 | 1    | 3         | 2:45  | 0    | Clean!
2025-11-17 | 1    | 4         | 2:10  | 0    | Getting faster
2025-11-18 | 1    | 5         | 1:50  | 0    | Under 2 min! ✓


MASTERY CHECKLIST:
[ ] Kata 1: Coded 100 times, can do with eyes closed
[ ] Kata 1: Under 2 min, zero bugs, last 10 attempts
[ ] Kata 2: Can code in < 3 min, zero bugs
[ ] Kata 3: Can code in < 3 min, zero bugs
[ ] Kata 4: Can code in < 2 min, zero bugs
[ ] Kata 5: Can code in < 5 min, zero bugs
[ ] Kata 6: Can code in < 4 min, zero bugs
[ ] Understand WHY each boundary condition
[ ] Can explain while coding
[ ] Recognize binary search in new problems (< 15 sec)

BREATHING KNOWLEDGE:
[ ] All 6 katas in under 20 minutes total
[ ] Zero bugs across all katas
[ ] Can code classic BS with eyes literally closed
[ ] Immediately recognize when to use binary search
[ ] Used successfully in 10+ LeetCode problems

Common Bugs I've Made (learn from these):
-
-
-
"""


if __name__ == "__main__":
    import doctest

    print("=" * 60)
    print("BINARY SEARCH - KATA PRACTICE")
    print("=" * 60)
    print()
    print("🥋 The most important algorithm to master!")
    print()

    results = doctest.testmod()

    if results.failed == 0:
        print("✅ All tests passed!")
        print(f"   {results.attempted} tests run")
        print()
        print("KEEP PRACTICING until you can code this in your sleep!")
        print("Goal: 100 perfect attempts of classic binary search")
    else:
        print(f"❌ {results.failed} test(s) failed")
        print()
        print("Debug, understand WHY, then retry!")
        print("Binary search must be PERFECT.")

    print()
    print("=" * 60)

    pass
    pass