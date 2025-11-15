"""Jewels and Stones - LeetCode #771

Difficulty: Easy
Topic: Hashing
Link: https://leetcode.com/problems/jewels-and-stones/description/

# Problem

You're given strings jewels representing the types of stones that are jewels, and stones
representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Constraints:

- 1 <= jewels.length, stones.length <= 50
- jewels and stones consist of only English letters.
- All the characters of jewels are unique.

# Approach

We can create a set of jewels, then iterate over the stones and increment
a counter for every stone that is in the jewels set.

Complexity:

- Time: O(N)
- Space: O(N)

Key Insights:

- Hashset O(1) lookup means we only need to iterate over stones once
"""

import pytest
from dataclasses import dataclass
from typing import *

# Uncomment for property-based testing:
# from hypothesis import given, assume
# from hypothesis import strategies as st


def jewels_and_stones(jewels: str, stones: str) -> int:
    """Count how many stones are jewels.

    Args:
        jewels: a string of jewels
        stones: a string of stones

    Returns:
        the total number of stones that are jewels
    """
    count = 0
    jewels = set(jewels)
    for stone in stones:
        if stone in jewels:
            count += 1

    return count
                   


@dataclass
class Case:
    """Test Case

    Note:
        Update fields to match those found in
        leetcode problems. Make sure to updating
        typing information
    """
    jewels: str
    stones: str
    expected: int
    description: str = "some jewels and stones"


TEST_CASES = [
    Case(
        jewels = "aaAbB",
        stones = "abcd",
        expected=2,
        description="example 1: basic case",
    ),
    Case(
        jewels = "abBd",
        stones = "aabcd",
        expected=4,
        description="example 2: quite a few",
    ),
    Case(
        jewels = "abBd",
        stones = "ugggghhhhhh",
        expected=0,
        description="no jewels",
    ),
    Case(
        jewels = "aA",
        stones = "aAAbbbb",
        expected=3,
        description="LeetCode example",
    ),
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_jewels_and_stones(case):
    """Test problem with all cases from TEST_CASES."""
    assert jewels_and_stones(case.jewels, case.stones) == case.expected, case.description


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

- Rely on sets O(1) lookup for set inclusion

## Patterns Used

- Hashset

## Similar Problems

- LeetCode #[num]: [Problem Name]
- LeetCode #[num]: [Problem Name]

## Alternative Approaches

## Mistakes I Made

Got this one first try! 
"""
