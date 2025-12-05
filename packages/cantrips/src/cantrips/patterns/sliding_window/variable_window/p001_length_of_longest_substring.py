"""
CANTRIP 1: Longest Substring Without Repeating Characters (LeetCode #3)

Target: < 3:00 | Difficulty: Medium

Find the length of the longest substring without repeating characters.

Pattern: Variable-size sliding window with set
- Expand right to add characters
- Contract left when duplicate found
- Track max window size seen

Examples:
    >>> length_of_longest_substring("abcabcbb")
    3
    >>> length_of_longest_substring("bbbbb")
    1
    >>> length_of_longest_substring("pwwkew")
    3

Edge cases:
    - Empty string: return 0
    - All unique characters: return len(s)
    - All same character: return 1
    - Two characters alternating: return 2
"""


def length_of_longest_substring(s: str) -> int:
    """Find length of longest substring without repeating characters.

    Args:
        s: Input string.

    Returns:
        Length of longest substring with all unique characters.

    Time: O(n) - each character visited at most twice
    Space: O(min(n, alphabet)) - set size bounded by alphabet
    """
    pass  # Your solution here
