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


# ============================================================================
# RELATED CANTRIPS - Apply this pattern in real LeetCode problems
# ============================================================================

"""
After mastering these katas, practice the pattern in these problems:

EASY (Learn pattern application):
- LC #643: Maximum Average Subarray (similar mechanics, fixed size)
- LC #1004: Max Consecutive Ones III
- LC #485: Max Consecutive Ones

MEDIUM (Pattern core):
- LC #3: Longest Substring Without Repeating Characters
- LC #209: Minimum Size Subarray Sum → cantrips/arrays_strings/longest-subarray-under-sum.py
- LC #904: Fruit Into Baskets
- LC #340: Longest Substring with At Most K Distinct Characters
- LC #713: Subarray Product Less Than K
- LC #424: Longest Repeating Character Replacement
- LC #1438: Longest Continuous Subarray With Absolute Diff <= Limit

HARD (Advanced variations):
- LC #76: Minimum Window Substring (combines with hash map)
- LC #992: Subarrays with K Different Integers
- LC #1074: Number of Subarrays That Match Target Sum

PROGRESSION PATH:
1. Master katas 1-2 (length_of_longest_substring, min_subarray_len)
2. Solve Easy cantrips for confidence
3. Master katas 3-5 (total_fruit, k_distinct, subarray_product)
4. Tackle Medium cantrips (core variable window patterns)
5. Challenge yourself with Hard cantrips (complex constraint combinations)
"""


# ============================================================================
# MASTERY PROGRESSION - When to move to cantrips
# ============================================================================

"""
LEVEL 1 (Learning) - Week 1-2:
[ ] Can code katas 1-2 with reference template open
[ ] Understand expand-contract rhythm
[ ] Time doesn't matter yet

LEVEL 2 (Practicing) - Week 2-3:
[ ] Can code katas 1-2 from memory
[ ] < 5 bugs per week across all katas
[ ] Average time under 2× target time
→ READY FOR: Easy cantrips and simple Medium problems

LEVEL 3 (Proficient) - Week 3-4:
[ ] Zero bugs on katas 1-2 for a week
[ ] Consistently under target time
[ ] Can explain while coding
→ READY FOR: Medium cantrips (LC #3, #209, #904)

LEVEL 4 (Mastered) - Week 4-6:
[ ] 10+ perfect reps on each kata
[ ] Under 80% of target time
[ ] Can code katas 3-5 from memory
[ ] Used successfully in 5+ cantrips
→ READY FOR: Hard cantrips and teaching others

LEVEL 5 (Breathing Knowledge) - Week 6+:
[ ] Pattern recognition is automatic (< 10 sec in new problems)
[ ] Can code all 5 katas in under 18 minutes
[ ] Can teach this pattern to someone else
[ ] Expand-contract rhythm is muscle memory
→ INTERVIEW READY: This pattern is now a superpower

WHEN TO MOVE TO CANTRIPS:
- Reach Level 2 (Practicing) on katas 1-2 → Start Easy cantrips
- Reach Level 3 (Proficient) → Start Medium cantrips
- If you struggle on a cantrip → Return to katas for more reps
"""
from collections import Counter # when checking frequency maps


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
    seen = set()
    longest = 0
    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        longest = max(longest, right - left + 1)

    return longest

    
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
    window_sum = 0
    shortest = float('inf')
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            shortest = min(shortest, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return shortest if shortest != float('inf') else 0

        
        

            
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
    basket = Counter()
    max_fruit = 0
    left = 0
    for right in range(len(fruits)):
        basket[fruits[right]] += 1

        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]

            left += 1

        max_fruit = max(max_fruit, right - left + 1)

    return max_fruit


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


def min_window(s: str, t: str) -> str:
    """
    KATA 6: Minimum Window Substring (LeetCode #76)

    ⏱️  Target time: < 5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(t) space

    Find the minimum window in s that contains all characters of t.
    Return empty string if no such window exists.

    Pattern: Two frequency maps (have vs need), track "satisfied" count

    Edge cases:
    - t longer than s → return ""
    - t has duplicate chars → need that many in window
    - Multiple valid windows → return any minimum

    Hint if stuck: Track how many unique chars are "satisfied" (have >= need).
                   When all satisfied, try shrinking from left.

    Examples:
        >>> min_window("ADOBECODEBANC", "ABC")
        'BANC'
        >>> min_window("a", "a")
        'a'
        >>> min_window("a", "aa")
        ''

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    """
    KATA 7: Subarrays with K Different Integers (LeetCode #992)

    ⏱️  Target time: < 5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(k) space

    Count subarrays with exactly k distinct integers.

    Pattern: exactlyK(k) = atMostK(k) - atMostK(k-1)

    Reuse your kata 4/5 logic as a helper!

    Edge cases:
    - k = 0 → return 0
    - k > unique elements → return 0
    - All same element, k=1 → n*(n+1)/2

    Hint if stuck: Write a helper function count_at_most_k(nums, k) that counts
                   subarrays with AT MOST k distinct elements (like kata 5 counting).
                   Then: exactly_k = at_most_k(k) - at_most_k(k-1)

    Examples:
        >>> subarrays_with_k_distinct([1,2,1,2,3], 2)
        7
        >>> subarrays_with_k_distinct([1,2,1,3,4], 3)
        3

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
2025-12-04 | 2    | 6:51  | 0    | 
2025-12-04 | 1    | 4:40  | 0    | 
2025-12-02 | 1    | 1:44  | 0    | 
2025-12-01 | 4    | 5:52  | 0    | 
2025-11-30 | 3    | 6:28  | 0    | 
2025-11-30 | 1    | 1:50  | 0    | 
2025-11-25 | 5    | 2:07  | 1    | 
2025-11-25 | 3    | 0:11  | 0    | 
2025-11-25 | 1    | 2:15  | 0    | 
2025-11-25 | 2    | 0:11  | 0    | 
2025-11-25 | 2    | 7:08  | 1    | 
2025-11-20 | 1    | 3:51  | 0    | Careful with comments: we want to contract while the condition is met!
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
