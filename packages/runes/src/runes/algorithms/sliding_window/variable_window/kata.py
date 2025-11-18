"""
🥋 SLIDING WINDOW (VARIABLE SIZE) - KATA PRACTICE

Master the variable-size sliding window pattern through deliberate practice.

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
Use variable window when:
- ✓ Need longest/shortest subarray meeting condition
- ✓ Window size changes based on condition
- ✓ Expand until condition violated, then contract
- ✓ "At most K" or "at least X" constraints

TECHNIQUE:
1. Expand: Add right element, update state
2. Contract: While condition violated, remove left element
3. Update result: Track best window seen so far
4. Repeat until right reaches end
"""


def length_of_longest_substring(s: str) -> int:
    """
    KATA 1: Longest Substring Without Repeating Characters (LeetCode #3)

    ⏱️  Target time: < 3 minutes
    🎯 Goal: Zero bugs, O(n) time, O(min(n, alphabet)) space

    Find the length of the longest substring without repeating characters.

    Edge cases:
    - Empty string → return 0
    - All unique characters → return len(s)
    - All same character → return 1
    - Two characters alternating

    Hint if stuck: Use set/dict to track characters in current window.
                   When duplicate found, shrink from left until no duplicate.

    Examples:
        >>> length_of_longest_substring("abcabcbb")
        3
        >>> length_of_longest_substring("bbbbb")
        1
        >>> length_of_longest_substring("pwwkew")
        3

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    KATA 2: Minimum Size Subarray Sum (LeetCode #209)

    ⏱️  Target time: < 3.5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Find the minimal length of a subarray whose sum is >= target.
    Return 0 if no such subarray exists.

    Edge cases:
    - No subarray meets target → return 0
    - Single element >= target → return 1
    - Entire array needed → return len(nums)
    - All elements positive (guaranteed in LC #209)

    Hint if stuck: Expand to meet target, then contract to minimize length.
                   Track minimum length seen.

    Examples:
        >>> min_subarray_len(7, [2,3,1,2,4,3])
        2
        >>> min_subarray_len(4, [1,4,4])
        1
        >>> min_subarray_len(11, [1,1,1,1,1,1,1,1])
        0

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def total_fruit(fruits: list[int]) -> int:
    """
    KATA 3: Fruit Into Baskets (LeetCode #904)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space (at most 2 types)

    Pick maximum fruits from trees where you have 2 baskets.
    Each basket holds one fruit type. Find max fruits with at most 2 types.

    This is: "longest subarray with at most K=2 distinct elements"

    Edge cases:
    - All same type → return len(fruits)
    - Alternating two types → return len(fruits)
    - More than 2 types → need to find best window

    Hint if stuck: Track frequency of each fruit type in window.
                   When types > 2, shrink from left.

    Examples:
        >>> total_fruit([1,2,1])
        3
        >>> total_fruit([0,1,2,2])
        3
        >>> total_fruit([1,2,3,2,2])
        4

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    KATA 4: Longest Substring with At Most K Distinct Characters (LeetCode #340)

    ⏱️  Target time: < 4 minutes
    🎯 Goal: Zero bugs, O(n) time, O(k) space

    Find length of longest substring with at most k distinct characters.

    Edge cases:
    - k == 0 → return 0
    - k >= unique chars in s → return len(s)
    - Empty string → return 0

    Hint if stuck: Same as Kata 3, but with variable k instead of k=2.
                   Use frequency map, shrink when distinct > k.

    Examples:
        >>> length_of_longest_substring_k_distinct("eceba", 2)
        3
        >>> length_of_longest_substring_k_distinct("aa", 1)
        2

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    """
    KATA 5: Subarray Product Less Than K (LeetCode #713)

    ⏱️  Target time: < 4.5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(1) space

    Count number of contiguous subarrays where product < k.

    Edge cases:
    - k <= 1 → return 0 (all products >= 1)
    - Single element < k → counts as 1
    - Product becomes >= k → shrink window

    Hint if stuck: For each right position, count ALL valid subarrays ending at right.
                   Number of subarrays = (right - left + 1)

    Examples:
        >>> num_subarray_product_less_than_k([10,5,2,6], 100)
        8
        >>> num_subarray_product_less_than_k([1,2,3], 0)
        0

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
    print("SLIDING WINDOW (VARIABLE SIZE) - KATA PRACTICE")
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
    print("   just kata::test sliding_window/variable_window")
    print("   just variable-window::test")
    print("   just variable-window::test-kata1")
    print()
    print("🎯 KATA MASTERY TIPS:")
    print("   - Code from memory, no peeking!")
    print("   - Time yourself")
    print("   - Aim for zero bugs")
    print("   - Practice daily until automatic")
    print()
    print("   Key insight: Expand until invalid, contract until valid")
    print()
    print("=" * 60)
