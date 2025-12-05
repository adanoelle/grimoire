"""
CANTRIP 4: Permutation in String (LeetCode #567)

Target: < 4:00 | Difficulty: Medium

Return true if s2 contains a permutation of s1.

Pattern: Fixed window with frequency map
- Window size = len(s1)
- Compare character frequencies
- Use Counter or frequency array

Examples:
    >>> check_inclusion("ab", "eidbaooo")
    True
    >>> check_inclusion("ab", "eidboaoo")
    False

Edge cases:
    - len(s1) > len(s2): return False
    - s1 is empty: return True
    - s1 and s2 identical: return True
"""

from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    """Check if s2 contains a permutation of s1.

    Args:
        s1: Pattern string to find permutation of.
        s2: String to search in.

    Returns:
        True if any permutation of s1 exists in s2.

    Time: O(n) - single pass through s2
    Space: O(1) - 26-letter alphabet is constant
    """
    target = Counter(s1)
    window = Counter(s2[:len(s1)])
    if target == window:
        return True

    left = 0
    for right in range(len(s1), len(s2)):
        # add the value coming in from the right
        window[s2[right]] += 1
        window[s2[left]] -= 1

        if window == target:
            return True

        left += 1

    return False
