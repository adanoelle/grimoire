"""
CANTRIP 5: Find All Anagrams in a String (LeetCode #438)

Target: < 4:30 | Difficulty: Medium

Find all start indices of p's anagrams in s.

Pattern: Fixed window with frequency map (like Cantrip 4)
- Collect ALL matching window start indices
- Not just return True on first match

Examples:
    >>> find_anagrams("cbaebabacd", "abc")
    [0, 6]
    >>> find_anagrams("abab", "ab")
    [0, 1, 2]

Edge cases:
    - len(p) > len(s): return []
    - No matches: return []
    - Multiple overlapping matches: return all start indices
"""

from collections import Counter


def find_anagrams(s: str, p: str) -> list[int]:
    """Find all start indices of p's anagrams in s.

    Args:
        s: String to search in.
        p: Pattern string to find anagrams of.

    Returns:
        List of starting indices where anagrams begin.

    Time: O(n) - single pass through s
    Space: O(1) - 26-letter alphabet is constant
    """
    anagram = Counter(p)
    window = Counter(s[:len(p)])
    indices = []
    left = 0

    if window == anagram:
        indices.append(left)

    for right in range(len(p), len(s)):
        window[s[right]] += 1
        window[s[left]] -= 1

        if window[s[left]] == 0:
            del window[s[left]]

        left += 1

        if window == anagram:
            indices.append(left)

    return indices
