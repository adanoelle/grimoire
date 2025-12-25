"""
CANTRIP 1: Valid Parentheses (LeetCode #20)

Target: < 3:00 | Difficulty: Easy

Given a string containing just '(', ')', '{', '}', '[', ']',
determine if the input string is valid.

Valid means:
- Open brackets closed by same type
- Open brackets closed in correct order
- Every closing bracket has matching opening bracket

Pattern: Stack matching
- Use stack to track opening brackets
- Hash map: closing -> opening for quick lookup
- Check stack non-empty before pop
- End: stack should be empty for valid expression

Examples:
    >>> s = "()"
    >>> is_valid(s)
    True

    >>> s = "()[]{}"
    >>> is_valid(s)
    True

    >>> s = "(]"
    >>> is_valid(s)
    False

    >>> s = "([)]"
    >>> is_valid(s)
    False

Edge cases:
    - Empty string (valid)
    - Single character (invalid)
    - All opening or all closing (invalid)
    - Interleaved but not nested properly: "([)]" (invalid)
"""


def is_valid(s: str) -> bool:
    """Check if string has valid parentheses.

    Args:
        s: String containing only '(){}[]' characters.

    Returns:
        True if parentheses are valid, False otherwise.

    Time: O(n) - single pass
    Space: O(n) - stack size
    """
    pass
