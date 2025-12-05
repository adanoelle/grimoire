"""Missing Number - LeetCode #268

Difficulty: Easy
Topic: Hashing
Link: https://leetcode.com/problems/missing-number/description/

# Problem

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Constraints:

None

# Approach

Given an array of numbers, with one missing number, we can use the length
of the array and a hashset to find the missing value.

Let's say we have

```
[0, 3, 1]
```
We can start by creating a hashset of all the values we would expect in the range
[0, n]. Then we can iterate over the array, adding removing elements from the set that
is also in the array. At the end, there will be one element that we have not removed,
the missing number!

Complexity:

- Time: O(N)
- Space: O(N)

Key Insights:

- Retrieval and Deletion from sets are O(1)
"""

import pytest
from dataclasses import dataclass
from typing import List

# Uncomment for property-based testing:
# from hypothesis import given, assume
# from hypothesis import strategies as st


def missing_number(nums: List[int]) -> int:
    """Find the missing number in an array

    Args:
        nums: list of number [0, n] with one
            number missing

    Returns:
        ans: the number that is missing in the sequence
    """
    all_nums = {x for x in range(len(nums) + 1)}
    for val in nums:
        if val in all_nums:
            all_nums.remove(val)

    return all_nums.pop()


@dataclass
class Case:
    """Test Case

    Note:
        Update fields to match those found in
        leetcode problems. Make sure to updating
        typing information
    """
    input: List[int]
    expected: int
    description: str = "List [0, n] with a missing number" 


TEST_CASES = [
    Case(
        input=[0, 2, 3],
        expected=1,
        description="example 1: basic case",
    ),
    Case(
        input=[1, 2, 3],
        expected=0,
        description="missing starting place",
    ),
    Case(
        input=[0, 1, 2],
        expected=3,
        description="missing ending place",
    ),
    Case(
        input=[9,6,4,2,3,5,7,0,1],
        expected=8,
        description="LeetCode example",
    ),
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_missing_number(case):
    """Test problem with all cases from TEST_CASES."""
    assert missing_number(case.input) == case.expected, case.description


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

- Hashsets allow for O(1) lookup and deletion
- After creating a hashset, se only need to iterate over the array once

## Patterns Used

Hashset

## Similar Problems

- LeetCode #[num]: [Problem Name]
- LeetCode #[num]: [Problem Name]

## Alternative Approaches

There is a pure math approach where we can rely on the sum of a series:

```python
num_elems = len(nums)
# Formula for sum of a series
expected_sum = num_elems * (num_elems + 1) // 2
actual_sum = sum(nums)
# The difference in the sum is the missing number in the series
return expected_sum - actual_sum
    
```

## Mistakes I Made

I made the mistake of naively relying on `len(nums)` to construct my
hashset, but we know that we have a missing value in the nums, so the
hashset must be constructed by

```python
expected = {x for x in range(len(nums) + 1)}
    
```
"""
