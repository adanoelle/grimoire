"""Valid Parentheses - LeetCode #20

Difficulty: Easy
Topic: Stacks
Link: https://leetcode.com/problems/valid-parentheses/

# Problem

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. An input string is valid if: (1) open
brackets are closed by the same type of brackets, and (2) open brackets are
closed in the correct order. Every closing bracket must have a corresponding
opening bracket of the same type.

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only: '()[]{}'

# Approach

Use a stack to track opening brackets. When we encounter an opening bracket,
push it onto the stack. When we encounter a closing bracket, check if the stack
is non-empty and the top matches the corresponding opening bracket. If so, pop
the stack. If not, the string is invalid. At the end, the stack must be empty
for the string to be valid.

Complexity:

- Time: O(n) - single pass through the string
- Space: O(n) - worst case all opening brackets (e.g., "((((")

Key Insights:

- Use a hash map to map closing brackets to their opening counterparts
- Must check stack is non-empty before accessing the top element
- Stack must be empty at the end (all opened brackets properly closed)
"""

import pytest
from dataclasses import dataclass
from typing import *

# Property-based testing
from hypothesis import given
from hypothesis import strategies as st


def is_valid(s: str) -> bool:
    """Check if a string of parentheses is valid.

    Args:
        s: String containing only '(', ')', '{', '}', '[', ']'

    Returns:
        True if all brackets are properly opened and closed in correct order,
        False otherwise
    """
    stack = []
    close_to_open = {"}": "{", "]": "[", ")": "("}

    for char in s:
        if char in close_to_open:
            # Closing bracket: check if it matches top of stack
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            # Opening bracket: push to stack
            stack.append(char)

    # Valid only if all brackets were closed
    return not stack


@dataclass
class Case:
    """Test Case for Valid Parentheses."""
    input: str
    expected: bool
    description: str = ""


TEST_CASES = [
    # LeetCode Examples
    Case(
        input="()",
        expected=True,
        description="example 1: simple valid pair",
    ),
    Case(
        input="()[]{}",
        expected=True,
        description="example 2: multiple types, all valid",
    ),
    Case(
        input="(]",
        expected=False,
        description="example 3: wrong closing bracket",
    ),
    Case(
        input="([)]",
        expected=False,
        description="example 4: interleaved, not properly nested",
    ),
    Case(
        input="{[]}",
        expected=True,
        description="example 5: properly nested",
    ),

    # Edge Cases
    Case(
        input="(",
        expected=False,
        description="edge: unclosed opening bracket",
    ),
    Case(
        input=")",
        expected=False,
        description="edge: closing without opening",
    ),
    Case(
        input="(())",
        expected=True,
        description="edge: nested same type",
    ),
    Case(
        input="(((",
        expected=False,
        description="edge: all opening brackets",
    ),
    Case(
        input=")))",
        expected=False,
        description="edge: all closing brackets",
    ),

    # Corner Cases
    Case(
        input="[",
        expected=False,
        description="corner: single opening bracket",
    ),
    Case(
        input="]",
        expected=False,
        description="corner: single closing bracket",
    ),
    Case(
        input="(((())))",
        expected=True,
        description="corner: long valid nested",
    ),
    Case(
        input="(((()))",
        expected=False,
        description="corner: long invalid (one unclosed)",
    ),
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_is_valid(case):
    """Test is_valid with all cases from TEST_CASES."""
    assert is_valid(case.input) == case.expected, case.description


@given(st.text(alphabet='()[]{}', min_size=0, max_size=100))
def test_is_valid_properties(s):
    """Test invariants that must hold for all inputs.

    Strategy breakdown:
        st.text(...)           - Generate a string
        alphabet='()[]{}'      - Only use valid bracket characters
        min_size=0             - Allow empty strings (which are valid)
        max_size=100           - Limit size for fast testing
    """
    result = is_valid(s)

    # Property 1: Result must be boolean
    assert isinstance(result, bool), "is_valid must return a boolean"

    # Property 2: Odd length strings are always invalid
    # (Can't have balanced brackets with odd number of chars)
    if len(s) % 2 == 1:
        assert result == False, "Odd length strings cannot be valid"

    # Property 3: Empty string is valid
    if len(s) == 0:
        assert result == True, "Empty string is valid"

    # Property 4: Single character is always invalid
    if len(s) == 1:
        assert result == False, "Single character cannot be valid"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


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
