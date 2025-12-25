"""
CANTRIP 4: Minimum Remove to Make Valid Parentheses (LeetCode #1249)

Target: < 6:00 | Difficulty: Medium

Remove the minimum number of parentheses so that the resulting
string is valid. Return any valid result.

Pattern: Stack matching with indices
- Use stack to track indices of unmatched '(' parentheses
- Track set of indices to remove
- First pass: find all invalid ')' and unmatched '('
- Second pass: build result skipping invalid indices

Examples:
    >>> s = "lee(t(c)o)de)"
    >>> min_remove_to_make_valid(s)
    'lee(t(c)o)de'

    >>> s = "a)b(c)d"
    >>> min_remove_to_make_valid(s)
    'ab(c)d'

    >>> s = "))(("
    >>> min_remove_to_make_valid(s)
    ''

Edge cases:
    - Already valid: "a(b)c" -> "a(b)c"
    - Extra closing: "a)b(c" -> "ab(c"
    - Extra opening: "a(b(c" -> "a(bc" or "abc"
    - Multiple solutions possible
"""


def min_remove_to_make_valid(s: str) -> str:
    """Remove minimum parentheses to make string valid.

    Args:
        s: String with letters and parentheses.

    Returns:
        Valid string with minimum removals.

    Time: O(n) - two passes
    Space: O(n) - stack and set size
    """
    pass
