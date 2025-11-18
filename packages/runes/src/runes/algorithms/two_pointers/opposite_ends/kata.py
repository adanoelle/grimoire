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
