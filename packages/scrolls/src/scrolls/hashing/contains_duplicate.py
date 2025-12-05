"""Contains Duplicates - LeetCode #217

Difficulty: Easy
Topic: Hashing
Link: https://leetcode.com/problems/contains-duplicate/

# Problem

Given an integer array nums, return true if any value appears at
least twice in the array, and return false if every element is distinct.

Constraints:

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

# Approach

We can use a set to create a copy of the elements, removing duplicates.
If the `len(set) < len(input)`, we know that there are duplicates.

Complexity:

- Time: O(N)
- Space: O(N)

Key Insights:

Hash sets are the key here
"""

import pytest
from dataclasses import dataclass
from typing import *

# Uncomment for property-based testing:
# from hypothesis import given, assume
# from hypothesis import strategies as st


def contains_duplicates(nums: List[int]) -> bool:
    """Check whether a list of ints contains duplicates

    Args:
        nums: list of nums, possibly containing duplicates

    Returns:
        whether nums has duplicates
    """
    return len(set(nums)) < len(nums)


@dataclass
class Case:
    """Test Case

    Note:
        Update fields to match those found in
        leetcode problems. Make sure to updating
        typing information
    """
    input: List[int]
    expected: bool
    description: str = "Whether an array has duplicates"


TEST_CASES = [
    Case(
        input=[1, 2, 3, 1],
        expected=True,
        description="example 1: basic case",
    ),
    Case(
        input=[0, 1],
        expected=False,
        description="no duplicates",
    ),
    Case(
        input=[],
        expected=False,
        description="edge: empty array",
    ),
    # Add more test cases:
    # - LeetCode examples
    # - Edge cases (empty, single element, large input)
    # - Corner cases specific to the problem
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_problem_name(case):
    """Test problem with all cases from TEST_CASES."""
    assert contains_duplicates(case.input) == case.expected, case.description


# Property-based tests (uncomment when useful for discovering edge cases)
# @given(st.lists(st.integers(-1000, 1000), min_size=0, max_size=100))
# def test_problem_name_properties(input_data):
#     """Test invariants that should always hold.
#
#     Common strategies:
#     - Sorted arrays: st.lists(st.integers()).map(sorted)
#     - Non-empty: min_size=1
#     - Positive only: st.integers(min_value=1)
#     - Fixed length: st.lists(st.integers(), min_size=N, max_size=N)
#     """
#     result = problem_name(input_data)
#
#     # Example properties to test:
#     # assert result >= 0  # Output is always non-negative
#     # assert len(result) <= len(input_data)  # Output can't be longer
#     # assert isinstance(result, int)  # Type checking
#     pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


"""
## What I Learned

- hashsets are key for removing duplicates
- O(N) space and time since we need to create a new set of numbers,
  which iterates under the hood

## Patterns Used

- Hashing

## Similar Problems

- LeetCode #[num]: [Problem Name]
- LeetCode #[num]: [Problem Name]

## Alternative Approaches

1. **[Approach Name]**: [Brief description] - O(?) time, O(?) space
2. **[Approach Name]**: [Brief description] - O(?) time, O(?) space

## Mistakes I Made
"""
