"""[Problem Name] - LeetCode #[Number]

Difficulty: [Easy/Medium/Hard] | Topic: [Topic Name] | [Problem Link]

# Problem

[Write a concise 1-2 paragraph description of the problem here. Focus on what
needs to be accomplished, not implementation details.]

Constraints:
- [Key constraint 1]
- [Key constraint 2]
- [Add more as needed]

# Approach

[Explain your high-level strategy in 2-4 sentences. What technique or pattern
are you using? Why does it work?]

Complexity:
- Time: O(?)
- Space: O(?)

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


def problem_name(input_data: List[int]) -> int:
    """Brief one-line description of what this function does.

    Args:
        input_data: Description of the input parameter

    Returns:
        Description of what is returned
    """
    # Your implementation here
    pass


@dataclass
class Case:
    input: Any  # Replace with actual input type
    expected: Any  # Replace with actual expected output type
    description: str = ""


TEST_CASES = [
    Case(
        input=[1, 2, 3],
        expected=6,
        description="example 1: basic case",
    ),
    Case(
        input=[],
        expected=0,
        description="edge: empty input",
    ),
    Case(
        input=[1],
        expected=1,
        description="edge: single element",
    ),
    # Add more test cases:
    # - LeetCode examples
    # - Edge cases (empty, single element, large input)
    # - Corner cases specific to the problem
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_problem_name(case):
    """Test problem with all cases from TEST_CASES."""
    assert problem_name(case.input) == case.expected, case.description


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
- [Key insight or technique you learned]
- [Understanding gained about complexity or edge cases]
- [Any algorithmic patterns recognized]

## Patterns Used
- [Pattern name: e.g., Two Pointers, Sliding Window, etc.]

## Similar Problems
- LeetCode #[num]: [Problem Name]
- LeetCode #[num]: [Problem Name]

## Alternative Approaches
1. **[Approach Name]**: [Brief description] - O(?) time, O(?) space
2. **[Approach Name]**: [Brief description] - O(?) time, O(?) space

## Mistakes I Made
- [Common pitfall or error you encountered]
- [What you'd do differently next time]
"""
