"""Two Sum - LeetCode #1

Difficulty: Easy
Topic: Hashing
Link: https://leetcode.com/problems/two-sum/

# Problem

Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target. You may assume that each
input would have exactly one solution, and you may not use the same element
twice. You can return the answer in any order.

Constraints:

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.
 
# Approach

We want to iterate over the array, keeping track of the indices at which
two numbers sum to a target. For each value in the array, we can use

```
complement = target - nums[idx]    
```

while iteratively building up a dictionary of {values: indices}. If the complement
is in the dictionary, we know that the current index and the dict[complement]
are the indices we are looking for. If it is not, we add the {value: index} into the
dictionary and then move to the next index.

Complexity:

- Time: O(N)
- Space: O(N)

Key Insights:

- Hashing allows us to track indices as we iterate
- Order matters! Check for the values in the index before adding them to the map
"""

import pytest
from dataclasses import dataclass
from typing import List

# Uncomment for property-based testing:
# from hypothesis import given, assume
# from hypothesis import strategies as st


def two_sum(nums: List[int], target: int) -> List:
    """Find the index of two values in `nums` that sum to `target`

    Args:
        nums: list of values 

    Returns:
        list of indices whose values in nums sum to target
    """
    indices = {}
    for idx, val in enumerate(nums):
        complement = target - val

        if complement in indices:
            return [indices[complement], idx]

        indices[val] = idx

    return []
      


@dataclass
class Case:
    """Test Case

    Note:
        Update fields to match those found in
        leetcode problems. Make sure to updating
        typing information
    """
    input: List[int]
    target: int
    expected: List[int]
    description: str = "Finding two sum"


TEST_CASES = [
    Case(
        input=[1, 3, 3],
        target=6,
        expected=[1, 2],
        description="example 1: basic case",
    ),
    Case(
        input=[1, 2, 5, 3],
        target=4,
        expected=[0, 3],
        description="zeroth and last",
    ),
    Case(
        input=[2, 7, 11, 15],
        target=9,
        expected=[0, 1],
        description=" LeetCode example",
    ),
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_problem_name(case):
    """Test problem with all cases from TEST_CASES."""
    assert two_sum(case.input, case.target) == case.expected, case.description


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

- When you need to keep track of indices, a hashmap is the way to go - {val: idx}

## Patterns Used

Hashing

## Similar Problems

- LeetCode #[num]: Two Sum II
- LeetCode #[num]: Three Sum

## Alternative Approaches

1. Two Pointers

## Mistakes I Made

Initially, I made the mistake of adding the {val: index} to the indices map
before checking if the complement was in the map. This meant that for cases
where

```
val * 2 == target
```

I was returning the same index as [idx, idx]. We need to find two separate
values in the array that sum to target and return their indices. The trick was
to check if the complement was in the map first, and then add that {val: idx}
to the map.
"""
