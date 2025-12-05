"""Reverse String - LeetCode #344

Difficulty: Easy | Topic: Arrays & Strings | https://leetcode.com/problems/reverse-string/

# Problem

Write a function that reverses a string. The input string is given as an array
of characters that must be modified in-place with O(1) extra memory.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is a printable ASCII character

# Approach

Use two pointers starting at opposite ends of the array. While the pointers
haven't met, swap the characters at each pointer position and move the pointers
toward the center. This achieves a complete reversal in a single pass.

Complexity:
- Time: O(n) - single pass through half the array
- Space: O(1) - only pointer variables needed

Key Insights:
- Two pointers from opposite ends is perfect for symmetric operations like reversing
- In-place swapping eliminates the need for additional data structures
- Loop terminates when pointers meet in the middle

# Kata Practice Integration

PREREQUISITE KATAS:
- Drill first: two_pointers/opposite_ends (kata 3: reverse_string)
- Target: < 1.5 min, zero bugs
- Location: packages/runes/src/runes/algorithms/two_pointers/opposite_ends/kata.py

THIS PROBLEM TEACHES:
- When to recognize two-pointer pattern (symmetric operations, in-place requirement)
- Edge case handling (empty array, single element, even vs odd length)
- Interview communication (explain pointer movement while coding)
- LeetCode submission format (modify in-place, return value)

MASTERY CHECK:
Before attempting this problem, you should have:
- Reached Level 2 (Practicing) on two_pointers/opposite_ends katas 1-3
- Can code reverse_string kata in < 1.5 min with zero bugs
- Understand why two pointers work for symmetric operations

AFTER SOLVING:
- If struggled with logic → Return to kata 3 for 5 more reps
- If struggled with edge cases → Practice kata 3 with extreme inputs
- If solved easily → Ready for LC #125 (Valid Palindrome), LC #977 (Squares Sorted Array)
- Update kata mastery log: "Used successfully in LC #344"
"""

import pytest
from typing import List


def reverse_string(s: List[str]) -> None:
    """Reverse a string in-place using the two-pointer technique.

    Args:
        s: List of characters to reverse (modified in-place)

    Returns:
        The reversed list (same object as input)
    """
    start = 0
    end = len(s) - 1

    while start < end:
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp
        start += 1
        end -= 1

    return s


TEST_CASES = [
    # (input, expected_output, description)
    (
        ["h", "e", "l", "l", "o"],
        ["o", "l", "l", "e", "h"],
        "example 1: basic odd-length string",
    ),
    (
        ["H", "a", "n", "n", "a", "h"],
        ["h", "a", "n", "n", "a", "H"],
        "example 2: even-length palindrome name",
    ),
    (["a"], ["a"], "edge: single character"),
    (["a", "b"], ["b", "a"], "edge: two characters"),
]


@pytest.mark.parametrize("input_data,expected,description", TEST_CASES)
def test_reverse_string(input_data, expected, description):
    """Test reverse string with all cases from TEST_CASES."""
    assert reverse_string(input_data) == expected, description


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


"""
# Reflections
# ---
 
## What I Learned
 
- Two pointers technique is fundamental for array problems requiring O(1) space
- Moving pointers toward each other from opposite ends is perfect for symmetric operations
- In-place modifications require careful tracking of indices

## Patterns Used
 
- Two pointers (opposite ends)

## Similar Problems
 
- LeetCode #125: Valid Palindrome (also uses two pointers from opposite ends)
- LeetCode #977: Squares of a Sorted Array (two pointers on sorted array)

## Alternative Approaches
 
1. **Python built-in**: `s.reverse()` - O(n) time, O(1) space. Same complexity,
   but less educational for understanding the algorithm.
2. **Pythonic swap**: Use `s[start], s[end] = s[end], s[start]` to swap without
   a temporary variable - O(n) time, O(1) space. Cleaner Python idiom.
"""
