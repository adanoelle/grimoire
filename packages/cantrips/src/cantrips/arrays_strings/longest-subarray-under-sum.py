"""[Problem Name] - LeetCode #[Number]

Difficulty: Easy
Topic: Arrays
Problem Link: [Sliding Window Article](https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4502/)

# Problem

Find the longest subarray with a sum less than or equal to k (constraint metric = sum)

Constraints:

- k: the upperbound sum of the subarray size

# Approach

Iteratively build a sliding window that tracks its current size subject to the
sum of the elements within the window being less than the constraint `k`.

## Algorithm:

1. initialize left, curr, ans to 0
2. iterate over the input array, using the index as the right bound of the window
3. add the value of nums[idx] to the curr sum
4. while the curr > constraint -> subtract the value of num[left] and left++
5. at each index as we iterate over the array, the answer is max(ans, right - left + 1)
6. after finising iterating (moving right to the end of the array), return ans

Complexity:
- Time: O(2N) [this is amortized due to partial sums]
- Space: O(1)

Key Insights:
- [What makes this approach work?]
- [Any important observations?]
"""

import pytest
from dataclasses import dataclass
from typing import *

# Uncomment for property-based testing:
# from hypothesis import given, assume
# from hypothesis import strategies as st


def longest_subarray_under_sum(nums: List[int], constraint: int) -> int:
    """Find the length of the longest subarray whose sum is less than constraint

    Notes:
        This is a sliding window problem

    Algorithm:
        1. initialize left, curr, ans to zero
        2. increment the right bound of the window
        3. compute the current sum by adding the value of input[right]
        3. while curr > constraint => move left bound to the right
        4. once we finish iterating, the solution is max(curr, right - left + 1)

    Args:
        nums: array of ints to iterate over
        constraint: the upperbound of the sum of the longest valid subarray

    Returns:
        the length of the longest subarray
    """
    ans = left = curr = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > constraint:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans


@dataclass
class Case:
    input_array: List[int]
    constraint: int
    expected: int
    description: str = ""


TEST_CASES = [
    Case(
        input_array=[1, 2, 1, 4, 3],
        constraint=6,
        expected=3,
        description="example 1: basic case",
    ),
    Case(
        input_array=[],
        constraint=10,
        expected=0,
        description="empty array should return 0",
    ),
    Case(
        input_array=[5],
        constraint=10,
        expected=1,
        description="single element within constraint",
    ),
    Case(
        input_array=[10],
        constraint=5,
        expected=0,
        description="single element exceeds constraint",
    ),
    Case(
        input_array=[1, 1, 1, 1],
        constraint=1000,
        expected=4,
        description="all elements valid - whole array is answer",
    ),
    Case(
        input_array=[100, 200, 300],
        constraint=5,
        expected=0,
        description="no valid subarrays - all elements too large",
    ),
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_longest_subarray_under_sum(case):
    """Test problem with all cases from TEST_CASES."""
    assert (
        longest_subarray_under_sum(case.input_array, case.constraint) == case.expected
    ), case.description


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


# Reflections
# -----------
"""
## What I Learned

We can slide a window over the input array, iteratively building our solution
by keeping track of the current window size and the longest window size we
have seen thus far.
 
## Patterns Used
 
- Sliding Window

## Similar Problems

- LeetCode #[num]: [Problem Name]
- LeetCode #[num]: [Problem Name]

## Alternative Approaches
 
1. **[Approach Name]**: [Brief description] - O(?) time, O(?) space
2. **[Approach Name]**: [Brief description] - O(?) time, O(?) space

## Mistakes I Made

Initially, I made the mistake of incorrectly updating the answer:

```python
# Wrong -> comparing with curr where it should have been `ans`
ans = max(curr, right - left + 1)
```

```python
# Correct -> comparing with `ans`
ans = max(ans, right - left + 1)
```

We are iteratively discovering the answer, which is always the current max, or the
length of the current sliding window that didn't break the constraint.
"""
