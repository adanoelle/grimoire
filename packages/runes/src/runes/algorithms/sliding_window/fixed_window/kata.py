"""
🥋 SLIDING WINDOW (FIXED SIZE) - KATA PRACTICE

Master the fixed-size sliding window pattern through deliberate practice.

RULES:
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

PATTERN RECOGNITION:
Use fixed window when:
- ✓ Need to process subarrays of exact size K
- ✓ Sliding one element at a time
- ✓ Can maintain window state incrementally
- ✓ O(n) time is required (can't recalculate each window)

TECHNIQUE:
1. Initialize window with first K elements
2. Slide: Remove left, add right
3. Update state/result as you slide
4. Repeat until window reaches end
"""


def find_max_average(nums: list[int], k: int) -> float:
    """
    KATA 1: Maximum Average Subarray I (LeetCode #643)

    ⏱️  Target time: < 2 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Find contiguous subarray of length k with maximum average value.
    Return the maximum average.

    Edge cases:
    - k == len(nums) → return average of entire array
    - k == 1 → return max element
    - All elements equal → return that value
    - Negative numbers

    Hint if stuck: Calculate first window sum, then slide by removing
                   left element and adding right element

    Examples:
        >>> find_max_average([1,12,-5,-6,50,3], 4)
        12.75
        >>> find_max_average([5], 1)
        5.0

    START CODING BELOW (delete 'pass' and write your solution):
    """
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for idx in range(k, len(nums)):
        curr_sum = curr_sum - nums[idx-k] + nums[idx]
        max_sum = max(curr_sum, max_sum)

    return max_sum / k


def num_of_subarrays(arr: list[int], k: int, threshold: int) -> int:
    """
    KATA 2: Number of Sub-arrays of Size K and Average >= Threshold (LeetCode #1343)

    ⏱️  Target time: < 2.5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Count subarrays of size k where average >= threshold.

    Edge cases:
    - No subarrays meet threshold → return 0
    - All subarrays meet threshold → return len(arr) - k + 1
    - threshold == 0
    - Negative numbers in array

    Hint if stuck: Similar to Kata 1, but count windows where sum/k >= threshold
                   (or equivalently: sum >= threshold * k)

    Examples:
        >>> num_of_subarrays([2,2,2,2,5,5,5,8], 3, 4)
        3
        >>> num_of_subarrays([11,13,17,23,29,31,7,5,2,3], 3, 5)
        6

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def count_good_substrings(s: str) -> int:
    """
    KATA 3: Substrings of Size Three with Distinct Characters (LeetCode #1876)

    ⏱️  Target time: < 2 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space (size-3 set is constant)

    Count substrings of length 3 with all distinct characters.

    Edge cases:
    - len(s) < 3 → return 0
    - All characters the same → return 0
    - All distinct → return len(s) - 2

    Hint if stuck: Fixed window of size 3, check if all 3 chars are different
                   (can use set or manual comparison)

    Examples:
        >>> count_good_substrings("xyzzaz")
        1
        >>> count_good_substrings("aababcabc")
        4

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def check_inclusion(s1: str, s2: str) -> bool:
    """
    KATA 4: Permutation in String (LeetCode #567)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space (26-letter alphabet)

    Return true if s2 contains a permutation of s1.

    Edge cases:
    - len(s1) > len(s2) → return False
    - s1 is empty → return True
    - s1 and s2 identical → return True

    Hint if stuck: Use frequency map for s1. Slide fixed window of len(s1) over s2.
                   Check if window frequency matches s1 frequency.

    Examples:
        >>> check_inclusion("ab", "eidbaooo")
        True
        >>> check_inclusion("ab", "eidboaoo")
        False

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def find_anagrams(s: str, p: str) -> list[int]:
    """
    KATA 5: Find All Anagrams in a String (LeetCode #438)

    ⏱️  Target time: < 4.5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space (26-letter alphabet)

    Find all start indices of p's anagrams in s.

    Edge cases:
    - len(p) > len(s) → return []
    - No matches → return []
    - Multiple overlapping matches → return all start indices

    Hint if stuck: Similar to Kata 4, but collect ALL matching window start indices,
                   not just return True on first match

    Examples:
        >>> find_anagrams("cbaebabacd", "abc")
        [0, 6]
        >>> find_anagrams("abab", "ab")
        [0, 1, 2]

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


# ============================================================================
# MASTERY TRACKING
# ============================================================================

"""
Track your practice sessions below. Be honest about bugs!

Date       | Kata | Time  | Bugs | Notes
-----------|------|-------|------|---------------------------------------
2025-11-18 | 1    | 0:12  | 0    | Keep in mind that indexing with a fixed window is [idx - k] and [idx]
2025-11-18 | 1    | 3:14  | 0    | 
YYYY-MM-DD | 1    | MM:SS | N    | Description of any issues or insights
YYYY-MM-DD | 1    | MM:SS | N    | ...

MASTERY CHECKLIST:
For each kata, check off when you achieve:
[ ] Code from memory without hints
[ ] Zero bugs on first run
[ ] Under target time
[ ] Can explain trade-offs
[ ] Automatic pattern recognition
"""


# ============================================================================
# TEST RUNNER
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("SLIDING WINDOW (FIXED SIZE) - KATA PRACTICE")
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
    print("   just kata::test sliding_window/fixed_window")
    print("   just fixed-window::test")
    print("   just fixed-window::test-kata1")
    print()
    print("🎯 KATA MASTERY TIPS:")
    print("   - Code from memory, no peeking!")
    print("   - Time yourself")
    print("   - Aim for zero bugs")
    print("   - Practice daily until automatic")
    print()
    print("=" * 60)
