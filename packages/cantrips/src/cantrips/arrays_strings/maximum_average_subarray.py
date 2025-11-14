"""Maximum Average Subarray I - LeetCode #643

Difficulty: Easy
Topic: Arrays - sliding window
Link: https://leetcode.com/problems/maximum-average-subarray-i/description/

# Problem

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. Any answer with a calculation error less than
10-5 will be accepted.

Constraints:

- n == nums.length
- 1 <= k <= n <= 105
- -104 <= nums[i] <= 104

# Approach

We know that we have a fixed window size in this case of size k. We want to slide that
window over the array, compute the average of the values in that array, and store the
largest average as the answer. Once we finish iterating (upperbound is at index len(input)),
we break and return the answer.


Complexity:
- Time: O(N)
- Space: O(1)

Key Insights:

- Fixed window sizes can be iterated with for loops, index with the right pointer
"""

import pytest
from dataclasses import dataclass
from typing import List

# Uncomment for property-based testing:
# from hypothesis import given, assume
# from hypothesis import strategies as st


def my_first_attempt(input: List[int], k: int) -> float:
    """Find the largest average subarray of input

    Example:
        [0, 1, 2, 3, 4], k=3
         *     *
        [ ,  ,  ]

    Args:
        input: array of integers

    Returns:
        the largest average of the subarrays
    """
    left = right = curr_sum = max_sum = 0
    while right < k:
        curr_sum += input[right]
        right += 1

    max_sum = curr_sum
    while right < len(input):
        curr_sum -= input[left]
        left += 1
        curr_sum += input[right]
        right += 1
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum / k


def max_avg_subarray(input: List[int], k: int) -> float:
    """Find the largest average subarray of input

    Example:
        [0, 1, 2, 3, 4], k=3
         *     *
        [ ,  ,  ]

    Args:
        input: array of integers

    Returns:
        the largest average of the subarrays
    """
    curr_sum = max_sum = 0
    for idx in range(k):
        curr_sum += input[idx]

    max_sum = curr_sum
    for idx in range(k, len(input)):
        curr_sum += input[idx] - input[idx - k]
        max_sum = max(max_sum, curr_sum)

    return max_sum / k


@dataclass
class Case:
    input: List[int]
    k: int
    expected: float
    description: str = "find the maximum average subarray"


TEST_CASES = [
    Case(
        input=[1, 12, -5, -6, 50, 3],
        k=4,
        expected=12.75000,
        description="example 1: basic case",
    ),
    Case(
        input=[5],
        k=1,
        expected=5.00000,
        description="edge: single element",
    ),
    Case(
        input=[-1, -2, -3, -4],
        k=2,
        expected=-1.5,
        description="all negatives",
    ),
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_problem_name(case):
    """Test problem with all cases from TEST_CASES."""
    assert max_avg_subarray(case.input, case.k) == case.expected, case.description


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

- fixed sized windows mean that we can iterate with for loops
- Use idx as the right bound. Left bound is [idx - window_size]

## Patterns Used

Sliding Windows

## Similar Problems
- LeetCode #[num]: [Problem Name]
- LeetCode #[num]: [Problem Name]

## Alternative Approaches
1. **[Approach Name]**: [Brief description] - O(?) time, O(?) space
2. **[Approach Name]**: [Brief description] - O(?) time, O(?) space

## Mistakes I Made

Initially, I was thinking of while loops and moving both the left and
the right bounds, similar to when the window size needs to be dynamic.
Since the window size here is fixed, we can iterate with for loops,
tracking the right pointer. The left pointer will always be
`input[idx - window_size]`
"""
