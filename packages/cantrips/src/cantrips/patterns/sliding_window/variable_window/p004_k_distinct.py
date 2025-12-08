"""
CANTRIP 4: Longest Substring with At Most K Distinct Characters (LeetCode #340)

Target: < 4:00 | Difficulty: Medium

Find length of longest substring with at most k distinct characters.

Pattern: Same as Cantrip 3, but with variable k
- Use frequency map
- Shrink when distinct > k

Examples:
    >>> length_of_longest_substring_k_distinct("eceba", 2)
    3
    >>> length_of_longest_substring_k_distinct("aa", 1)
    2

Edge cases:
    - k == 0: return 0
    - k >= unique chars in s: return len(s)
    - Empty string: return 0
"""

from collections import Counter


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """Find longest substring with at most k distinct characters.

    Args:
        s: Input string.
        k: Maximum number of distinct characters allowed.

    Returns:
        Length of longest valid substring.

    Time: O(n) - single pass
    Space: O(k) - frequency map size
    """
    chars = Counter()
    longest = 0
    left = 0
    for right in range(len(s)):
        chars[s[right]] += 1

        while len(chars) > k:
            chars[s[left]] -= 1
            if chars[s[left]] == 0:
                del chars[s[left]]

        longest = max(longest, right - left + 1)

    return longest
