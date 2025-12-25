"""
CANTRIP 2: Remove All Adjacent Duplicates In String (LeetCode #1047)

Target: < 4:00 | Difficulty: Easy

Remove all adjacent duplicate characters repeatedly.
When you remove adjacent duplicates, new duplicates may form.
Keep removing until no more duplicates remain.

Pattern: Stack matching
- Use stack to track characters
- When new char matches stack top: they cancel (pop)
- Otherwise: push new char
- Same LIFO matching pattern as bracket matching

Examples:
    >>> s = "abbaca"
    >>> remove_duplicates(s)
    'ca'

    >>> s = "azxxzy"
    >>> remove_duplicates(s)
    'ay'

    >>> s = "abcd"
    >>> remove_duplicates(s)
    'abcd'

Edge cases:
    - No duplicates: "abc" -> "abc"
    - All cancel: "aa" -> ""
    - Chain reaction: "abbaca" -> "ca" (bb removed, then aa)
    - Single char: "a" -> "a"
"""


def remove_duplicates(s: str) -> str:
    """Remove all adjacent duplicates from string.

    Args:
        s: Input string with lowercase letters.

    Returns:
        String with no adjacent duplicates.

    Time: O(n) - single pass
    Space: O(n) - stack size
    """
    pass
