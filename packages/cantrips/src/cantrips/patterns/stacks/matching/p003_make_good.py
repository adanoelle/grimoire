"""
CANTRIP 3: Make The String Great (LeetCode #1544)

Target: < 5:00 | Difficulty: Easy

Remove adjacent characters where one is uppercase and one is
lowercase of the SAME letter. Keep removing until no such
pairs remain.

"Good" string = no adjacent chars that are same letter but different case

Pattern: Stack matching
- Use stack to track characters
- When new char forms bad pair with stack top: they cancel (pop)
- Bad pair = same letter, different case
- Check: stack[-1].lower() == char.lower() and stack[-1] != char

Examples:
    >>> s = "leEeetcode"
    >>> make_good(s)
    'leetcode'

    >>> s = "abBAcC"
    >>> make_good(s)
    ''

    >>> s = "s"
    >>> make_good(s)
    's'

Edge cases:
    - No bad pairs: "abc" -> "abc"
    - All cancel: "aA" -> ""
    - Chain reaction: "leEeetcode" -> "leetcode" (remove "Ee")
    - Mixed: "abBAcC" -> "" (all cancel)
"""


def make_good(s: str) -> str:
    """Make string 'great' by removing bad adjacent pairs.

    Args:
        s: Input string with letters.

    Returns:
        String with no adjacent same-letter different-case pairs.

    Time: O(n) - single pass
    Space: O(n) - stack size
    """
    pass
