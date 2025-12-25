"""
CANTRIP 5: Longest Valid Parentheses (LeetCode #32)

Target: < 9:00 | Difficulty: Hard

Given a string containing just '(' and ')', find the length
of the longest valid (well-formed) parentheses substring.

Pattern: Stack matching with indices
- Stack stores INDICES, not characters
- Initialize stack with -1 (base for length calculation)
- When '(': push index
- When ')': pop, then calculate length
- If stack empty after pop: push current index (new base)
- Track max length seen

Examples:
    >>> s = "(()"
    >>> longest_valid_parentheses(s)
    2

    >>> s = ")()())"
    >>> longest_valid_parentheses(s)
    4

    >>> s = ""
    >>> longest_valid_parentheses(s)
    0

    >>> s = "()(()"
    >>> longest_valid_parentheses(s)
    2

Edge cases:
    - Empty string -> 0
    - All valid: "()" -> 2, "(())" -> 4
    - Partial valid: "(()" -> 2
    - Multiple segments: "()(()" -> 2
"""


def longest_valid_parentheses(s: str) -> int:
    """Find length of longest valid parentheses substring.

    Args:
        s: String containing only '(' and ')'.

    Returns:
        Length of longest valid substring.

    Time: O(n) - single pass
    Space: O(n) - stack size
    """
    pass
