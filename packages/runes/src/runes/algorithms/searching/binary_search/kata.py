"""
Binary Search - Daily Kata Practice

🥋 THE MOST CRITICAL ALGORITHM TO MASTER

Binary search is prone to off-by-one errors. Practice until PERFECT.
You should be able to code this in your sleep, zero bugs, every time.

Goal: Code classic binary search 100 times until muscle memory.
"""


# ============================================================================
# RELATED CANTRIPS - Apply this pattern in real LeetCode problems
# ============================================================================

"""
After mastering these katas, practice the pattern in these problems:

EASY (Learn pattern application):
- LC #35: Search Insert Position
- LC #704: Binary Search
- LC #278: First Bad Version
- LC #374: Guess Number Higher or Lower
- LC #69: Sqrt(x)

MEDIUM (Pattern variations):
- LC #33: Search in Rotated Sorted Array
- LC #34: Find First and Last Position of Element in Sorted Array
- LC #162: Find Peak Element
- LC #153: Find Minimum in Rotated Sorted Array
- LC #852: Peak Index in a Mountain Array
- LC #74: Search a 2D Matrix
- LC #240: Search a 2D Matrix II

HARD (Advanced binary search):
- LC #4: Median of Two Sorted Arrays
- LC #1095: Find in Mountain Array
- LC #410: Split Array Largest Sum
- LC #154: Find Minimum in Rotated Sorted Array II (with duplicates)

PROGRESSION PATH:
1. Master kata 1 (classic) - Do 100 reps until muscle memory
2. Solve Easy cantrips (LC #35, #704, #278)
3. Master katas 2-4 (first/last occurrence, insert position)
4. Tackle Medium cantrips (rotated arrays, 2D matrices)
5. Master katas 5-6 (rotated array, peak element)
6. Challenge yourself with Hard cantrips
"""


# ============================================================================
# MASTERY PROGRESSION - When to move to cantrips
# ============================================================================

"""
LEVEL 1 (Learning) - Week 1:
[ ] Can code kata 1 with reference template open
[ ] Understand loop invariants and boundary conditions
[ ] Time doesn't matter yet

LEVEL 2 (Practicing) - Week 1-2:
[ ] Can code kata 1 from memory
[ ] < 5 bugs per week on kata 1
[ ] Average time under 4 minutes
→ READY FOR: Easy cantrips (LC #35, #704)

LEVEL 3 (Proficient) - Week 2-3:
[ ] Zero bugs on kata 1 for a week
[ ] Consistently under 2 minutes on kata 1
[ ] Can code katas 2-4 from memory
→ READY FOR: Medium cantrips (LC #33, #34, #162)

LEVEL 4 (Mastered) - Week 3-5:
[ ] 50+ perfect reps on kata 1
[ ] Under 90 seconds on kata 1
[ ] Can code all 6 katas from memory
[ ] Used successfully in 10+ cantrips
→ READY FOR: Hard cantrips and teaching others

LEVEL 5 (Breathing Knowledge) - Week 5+:
[ ] 100+ perfect reps on kata 1 (THE GOAL!)
[ ] Can code kata 1 with eyes literally closed
[ ] All 6 katas in under 20 minutes
[ ] Pattern recognition is instant (< 5 sec)
[ ] Can explain boundary conditions in your sleep
→ INTERVIEW READY: Binary search is now a superpower

THE 100-REP GOAL:
Binary search is THE most critical algorithm to master.
Off-by-one errors plague even experienced engineers.
100 perfect repetitions builds neural pathways that make bugs impossible.

WHEN TO MOVE TO CANTRIPS:
- Reach Level 2 (Practicing) on kata 1 → Start Easy cantrips
- Reach Level 3 (Proficient) → Start Medium cantrips
- If you struggle on a cantrip → Return to kata 1 for 10 more reps
- THE RULE: Never attempt Hard cantrips before 50+ perfect reps on kata 1
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