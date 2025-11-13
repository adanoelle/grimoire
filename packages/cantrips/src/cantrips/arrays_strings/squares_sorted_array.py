"""Squares of a Sorted Array - LeetCode #977

Difficulty: Easy
Topic: Arrays
Link: https://leetcode.com/problems/squares-of-a-sorted-array/description/

# Problem

Given an integer array nums sorted in non-decreasing order, return an
array of the squares of each number sorted in non-decreasing order.

Constraints:

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.

# Approach

The key here is that we would like to do this in O(N) time.

Complexity:

- Time: O(N)
- Space: O(N)

Key Insights:

- Two pointers + for loop indices gives you the ability to compare two
  indices while maintaining an iterative index
"""

import pytest
from dataclasses import dataclass
from typing import *

# Property-based testing with Hypothesis
from hypothesis import given
from hypothesis import strategies as st


def sorted_squares(nums: List[int]) -> List[int]:
    """Square and sort an array of integers

    Note:
        - numbers could be negative and repeating

    Example:
         [-3, -2, 1, 1, 2, 3]
           *               *
    Args:
        input_data: non-decreasing integers

    Returns:
        the input_data squared and sorted
    """
    num_elems = len(nums)
    # pre-allocate an array since we need indices of that array
    result = [0] * num_elems

    left = 0
    right = num_elems - 1
    # Iterate in reverse
    for idx in range(num_elems - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            elem = nums[right]
            right -= 1
        else:
            elem = nums[left]
            left += 1

        result[idx] = elem**2

    return result


@dataclass
class Case:
    input: List[int]
    expected: List[int]
    description: str = "non-decreasing integers"


TEST_CASES = [
    Case(
        input=[-7, -3, 2, 3, 11],
        expected=[4, 9, 9, 49, 121],
        description="basic case from leetcode",
    ),
    # Add more test cases:
    # - LeetCode examples
    # - Edge cases (empty, single element, large input)
    # - Corner cases specific to the problem
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_sorted_squares(case):
    """Test problem with all cases from TEST_CASES."""
    assert sorted_squares(case.input) == case.expected, case.description


# Property-based tests - Hypothesis generates random test cases automatically
@given(st.lists(st.integers(-100, 100), min_size=1, max_size=10).map(sorted))
def test_sorted_squares_properties(nums):
    """Test invariants that should always hold for sorted_squares.

    Property-based testing focuses on testing PROPERTIES (invariants) rather
    than specific input/output examples. Hypothesis generates hundreds of
    random test cases to try to break your code.

    Strategy breakdown:
        st.lists(...)           - Generate a list
        st.integers(-10000, 10000)  - With integers in problem's constraint range
        min_size=1              - Non-empty (matches problem constraint)
        max_size=100            - Limit size for fast testing
        .map(sorted)            - CRITICAL: Sort the list (input must be sorted!)

    The .map(sorted) transforms any generated list into a sorted one, ensuring
    we meet the problem's precondition that input is sorted.
    """
    result = sorted_squares(nums)

    # Property 1: Output must be sorted (non-decreasing)
    # This checks that result[i] <= result[i+1] for all valid i
    assert result == sorted(result), "Output should be sorted in non-decreasing order"

    # Property 2: Output length equals input length
    # We square each element once - nothing added or removed
    assert len(result) == len(nums), "Output should have same length as input"

    # Property 3: All output values must be non-negative
    # Squares are always >= 0, regardless of input sign
    assert all(x >= 0 for x in result), "All squared values should be non-negative"

    # Property 4: Output contains exactly the squares of input (STRONGEST PROPERTY)
    # This is the "oracle" - a naive reference implementation to check correctness
    # If we square all inputs and sort them, we should get the same result
    expected = sorted([x**2 for x in nums])
    assert result == expected, f"Result should be sorted squares of input"

    # Note: Property 4 actually implies Properties 1-3, so technically you could
    # test just Property 4. But testing all of them provides clearer error messages
    # if something breaks - you'll know WHICH property failed.


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


# Reflections
# -----------
"""
## What I Learned
 
- Two pointers + a for loop index gives you three indices to rely on
- Considering subsections of the array, negative and positive, was the tricky part
- Iterating in reverse is a must

Since we have the potential for a section of negative numbers, and, when squaring those
numbers we need to consider that we may need to move that newly squared negative number
to the end of the solution array, we need to first compare the absolute value of the
left and right pointers. If the absolute value of the left pointer is less than the
absolute value of the right pointer, then we want the square of the right pointer. Since
we are iteratively building up the solution, where would be put it in the solution array?
In the latest most index of the solution at that time of iterating, of course! Since the
input data in non-decreasing, we know that comparing the current left and right pointers
will always allow us to square the appropriate value, again based on absolute value, and then
place that at the index of the solution array as we decrement it. The trick is to iterate in
reverse!

## Patterns Used
- Two Pointers

## Similar Problems
- LeetCode #[num]: [Problem Name]
- LeetCode #[num]: [Problem Name]

## Alternative Approaches
1. **[Approach Name]**: [Brief description] - O(?) time, O(?) space
2. **[Approach Name]**: [Brief description] - O(?) time, O(?) space

## Mistakes I Made
 
I recognized that two pointers would be a good fit here, but was thinking in terms
of while loops. I briefly considered the idea of having a third index, but I was
overcomplicating things by trying to think if I should increment or decrement the
third pointer. I needed to realize that the index in a for loop would have given
me a reliable way to know that I am incrementing through the array once.
"""
