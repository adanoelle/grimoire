"""
LeetCode Reverse Strings: 344
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-string/description/
Topic: Arrays

================================================================================
PROBLEM DESCRIPTION
================================================================================

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

## Example 1:
 
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Explanation:

## Example 2:
 
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
Explanation:

Constraints:

- 1 <= s.length <= 105
- s[i] is a printable ascii character.

================================================================================
APPROACH
================================================================================

## High-level strategy:

We know that we will always be swapping two positions in the array with one another.
The trick is that while iterating across the array, we can always track these two
positions simultaneously using two pointers, one starting at the beginning of the
array and one starting at the end of the array.

Start with a pointer at index 0 or the array, and another at index len(array) - 1,
then iterate over the array, swapping the value at the left index with the value at
the right. When the indices meet, we know that we have swapped everything and can break.

## Detailed steps:
 
1. Initialize left and right indexes at the start and end of the array
2. Iterate over the array
3. Swap left with right, making use of a temporary variable
4. When the two pointers meet, break and return 

## Key insights:
 
- Two pointers allow us to do this in O(N) time.
- Keeping a temporary variable and swapping the values in place gives us O(1) space

## Why this works:

Tracking multiple indices in the array makes efficient use of time.

================================================================================
COMPLEXITY ANALYSIS
================================================================================

Time Complexity: O(N)

Space Complexity: O(1)
- Data structure 1: Array modified in place: O(1)
- Total: O(1)

================================================================================
IMPLEMENTATION
================================================================================
"""

from typing import List, Optional


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses a string in-place using the two-pointer technique.

        Args:
            s: List of characters to reverse (modified in-place)

        Returns:
            The reversed list (modifies the input list)
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


"""
================================================================================
TEST CASES
================================================================================
"""


def test_solution():
    """Test cases for the solution"""
    sol = Solution()

    # Test case 1: Basic odd-length string
    solution = sol.reverseString(["h","e","l","l","o"])
    assert solution == ["o","l","l","e","h"]

    # Test case 2: Even-length string with palindrome name
    assert sol.reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()


"""
================================================================================
ALTERNATIVE APPROACHES
================================================================================

Approach 2: Python Built-in Reverse
- Description: Use s.reverse() method
- Time: O(n)
- Space: O(1)
- When to use: When code clarity matters more than showing algorithmic knowledge
- Code: s.reverse()

Approach 3: Pythonic Swap (No Temp Variable)
- Description: Use Python's tuple unpacking to swap without a temporary variable
- Time: O(n)
- Space: O(1)
- When to use: Cleaner Python code, same performance
- Code: s[start], s[end] = s[end], s[start]

================================================================================
LESSONS LEARNED
================================================================================

What I learned:
- Two pointers technique is fundamental for array problems requiring O(1) space
- Moving pointers toward each other from opposite ends is perfect for symmetric operations
- In-place modifications require careful tracking of indices

Mistakes I made:

Similar problems:
- LeetCode #125: Valid Palindrome (also uses two pointers from opposite ends)
- LeetCode #344: Reverse String (this problem)
- LeetCode #977: Squares of a Sorted Array (two pointers on sorted array)

Patterns used:
- Two pointers (opposite ends)
"""
