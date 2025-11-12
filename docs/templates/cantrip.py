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
from typing import List, Optional


class Solution:
    def problem_name(self, input_data: List[int]) -> int:
        """Brief one-line description of what this method does.

        Args:
            input_data: Description of the input parameter

        Returns:
            Description of what is returned
        """
        # Your implementation here
        pass


TEST_CASES = [
    # (input, expected_output, description)
    ([1, 2, 3], 6, "example 1: basic case"),
    ([], 0, "edge: empty input"),
    ([1], 1, "edge: single element"),
    # Add more test cases:
    # - LeetCode examples
    # - Edge cases (empty, single element, large input)
    # - Corner cases specific to the problem
]


@pytest.mark.parametrize("input_data,expected,description", TEST_CASES)
def test_problem_name(input_data, expected, description):
    """Test problem with all cases from TEST_CASES."""
    sol = Solution()
    assert sol.problem_name(input_data) == expected, description


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
