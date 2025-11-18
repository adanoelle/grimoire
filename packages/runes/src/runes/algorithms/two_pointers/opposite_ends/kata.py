"""
Two Pointers (Opposite Ends) - Daily Kata Practice

🥋 RULES:
1. Code from memory - NO looking at templates!
2. Set timer for each kata
3. Run tests after coding
4. If bugs: understand why, redo tomorrow
5. If perfect: move to next kata

PROGRESSION:
- Week 1: Code with reference, understand
- Week 2: Code from memory, small bugs OK
- Week 3: Code perfectly in under target time
- Week 4+: Breathing knowledge - teach someone else

Track your progress in the mastery log below.
"""

# ============================================================================
# RELATED CANTRIPS - Apply this pattern in real LeetCode problems
# ============================================================================

"""
After mastering these katas, practice the pattern in these problems:

EASY (Learn pattern application):
- LC #344: Reverse String → cantrips/arrays_strings/reverse_string.py
- LC #125: Valid Palindrome
- LC #167: Two Sum II (Sorted Array)
- LC #977: Squares of a Sorted Array → cantrips/arrays_strings/squares_sorted_array.py
- LC #283: Move Zeroes

MEDIUM (Pattern combinations):
- LC #15: 3Sum
- LC #11: Container With Most Water
- LC #16: 3Sum Closest
- LC #18: 4Sum
- LC #42: Trapping Rain Water

HARD (Advanced variations):
- LC #42: Trapping Rain Water (can also be Hard)
- LC #76: Minimum Window Substring (combines with sliding window)

PROGRESSION PATH:
1. Master katas 1-3 (two_sum_sorted, is_palindrome, reverse_string)
2. Solve Easy cantrips (build pattern recognition)
3. Master katas 4-5 (three_sum_closest, container_with_most_water)
4. Tackle Medium cantrips (apply advanced variations)
"""


# ============================================================================
# MASTERY PROGRESSION - When to move to cantrips
# ============================================================================

"""
LEVEL 1 (Learning) - Week 1-2:
[ ] Can code katas 1-3 with reference template open
[ ] Understand each line of code
[ ] Time doesn't matter yet

LEVEL 2 (Practicing) - Week 2-3:
[ ] Can code katas 1-3 from memory
[ ] < 5 bugs per week across all katas
[ ] Average time under 2× target time
→ READY FOR: Easy cantrips (LC #344, #125, #167)

LEVEL 3 (Proficient) - Week 3-4:
[ ] Zero bugs on katas 1-3 for a week
[ ] Consistently under target time
[ ] Can explain while coding
→ READY FOR: Medium cantrips (LC #15, #11)

LEVEL 4 (Mastered) - Week 4-6:
[ ] 10+ perfect reps on each kata
[ ] Under 80% of target time
[ ] Can code katas 4-5 from memory
[ ] Used successfully in 5+ cantrips
→ READY FOR: Hard cantrips and teaching others

LEVEL 5 (Breathing Knowledge) - Week 6+:
[ ] Pattern recognition is automatic (< 10 sec in new problems)
[ ] Can code all 5 katas in under 12 minutes
[ ] Can teach this pattern to someone else
[ ] Fingers start typing before conscious thought
→ INTERVIEW READY: This pattern is now a superpower

WHEN TO MOVE TO CANTRIPS:
- Reach Level 2 (Practicing) on katas 1-3 → Start Easy cantrips
- Reach Level 3 (Proficient) → Start Medium cantrips
- If you struggle on a cantrip → Return to katas for more reps
"""


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """
    KATA 1: Find pair that sums to target in sorted array

    ⏱️  Target time: < 2 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Edge cases to consider:
    - Empty array
    - No solution exists
    - Multiple valid pairs (return any)
    - Negative numbers
    - Duplicates

    Hint if stuck: Two pointers start at ends, move based on sum comparison

    Args:
        nums: Sorted array of integers
        target: Target sum

    Returns:
        List [i, j] where nums[i] + nums[j] == target, or [] if no solution

    Examples:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum_sorted([2, 3, 4], 6)
        [0, 2]
        >>> two_sum_sorted([1, 2, 3], 10)
        []

    START CODING BELOW (delete 'pass' and write your solution):
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []


def is_palindrome(s: str) -> bool:
    """
    KATA 2: Check if string is palindrome (alphanumeric, ignore case)

    ⏱️  Target time: < 2 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space (excluding preprocessing)

    Edge cases:
    - Empty string → True
    - Single character → True
    - All non-alphanumeric → True
    - Mixed case
    - Spaces and punctuation

    Hint if stuck: Clean string first, then two pointers from ends

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True
        >>> is_palindrome(".,")
        True

    START CODING BELOW:
    """
    s = str(s)
    left = 0
    right =  len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def reverse_string(s: list[str]) -> None:
    """
    KATA 3: Reverse string in-place (modify input array)

    ⏱️  Target time: < 1.5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Edge cases:
    - Empty array
    - Single character
    - Even vs odd length

    Note: Modifies s in-place, returns None

    Examples:
        >>> s = ["h", "e", "l", "l", "o"]
        >>> reverse_string(s)
        >>> s
        ['o', 'l', 'l', 'e', 'h']
        >>> s = ["H", "a", "n", "n", "a", "h"]
        >>> reverse_string(s)
        >>> s
        ['h', 'a', 'n', 'n', 'a', 'H']

    START CODING BELOW:
    """
    left = 0
    right = len(s) -1
    while left < right:
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1


def three_sum_closest(nums: list[int], target: int) -> int:
    """
    KATA 4: Find three numbers whose sum is closest to target (LC #16)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(n²) time, O(1) space

    This is ADVANCED - master kata 1-3 first!

    Strategy:
    - Sort the array first
    - Fix one number, use two pointers for other two
    - Track closest sum seen so far

    Edge cases:
    - Exactly 3 elements → return their sum
    - Multiple sums with same distance → return any

    Examples:
        >>> three_sum_closest([-1, 2, 1, -4], 1)
        2
        >>> three_sum_closest([0, 0, 0], 1)
        0

    START CODING BELOW:
    """
    pass


def container_with_most_water(heights: list[int]) -> int:
    """
    KATA 5: Maximum water container area (LC #11)

    ⏱️  Target time: < 3 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Key insight: Start with widest container, move pointer with smaller height
    (moving taller pointer can't increase area)

    Edge cases:
    - Two elements → return min(heights) * 1
    - All same height → depends on width

    Examples:
        >>> container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        >>> container_with_most_water([1, 1])
        1
        >>> container_with_most_water([4, 3, 2, 1, 4])
        16

    START CODING BELOW:
    """
    pass


# ============================================================================
# MASTERY TRACKING
# ============================================================================

"""
Log your practice sessions here. Track time and bugs.

Date       | Kata | Time  | Bugs | Notes
-----------|------|-------|------|---------------------------------------
2025-11-16 | 1    | 3:45  | 1    | Off-by-one error in while condition
2025-11-17 | 1    | 2:10  | 0    | Clean! Moving to kata 2
2025-11-17 | 2    | 4:00  | 2    | Forgot to handle non-alphanumeric
2025-11-18 | 1-2  | 3:30  | 0    | Both perfect! Starting kata 3


MASTERY CHECKLIST:
[ ] Kata 1: Can code in < 2 min with zero bugs
[ ] Kata 2: Can code in < 2 min with zero bugs
[ ] Kata 3: Can code in < 1.5 min with zero bugs
[ ] Kata 4: Can code in < 4 min with zero bugs
[ ] Kata 5: Can code in < 3 min with zero bugs
[ ] Can explain the pattern while coding
[ ] Can identify when to use in new problems (< 30 sec)
[ ] Used successfully in 5+ LeetCode problems

BREATHING KNOWLEDGE (Ultimate Goal):
[ ] Can code all 5 katas in under 12 minutes total
[ ] Zero bugs across all katas
[ ] Can teach this pattern to someone else
[ ] Pattern recognition is automatic
"""


# ============================================================================
# TEST RUNNER
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TWO POINTERS (OPPOSITE ENDS) - KATA PRACTICE")
    print("=" * 60)
    print()
    print("🥋 Run tests with pytest:")
    print()
    print("   pytest test_kata.py                  # Run all tests")
    print("   pytest test_kata.py -m kata1         # Run kata 1 only")
    print("   pytest test_kata.py -m kata2         # Run kata 2 only")
    print("   pytest test_kata.py -v               # Verbose output")
    print()
    print("Or use justfile commands:")
    print()
    print("   just kata::test two_pointers/opposite_ends")
    print("   just opposite-ends::test")
    print("   just opposite-ends::test-kata1")
    print()
    print("🎯 KATA MASTERY TIPS:")
    print("   - Code from memory, no peeking!")
    print("   - Time yourself")
    print("   - Aim for zero bugs")
    print("   - Practice daily until automatic")
    print()
    print("=" * 60)
