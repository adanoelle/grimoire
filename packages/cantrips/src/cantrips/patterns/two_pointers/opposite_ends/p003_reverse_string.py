"""
CANTRIP 3: Reverse String (LeetCode #344)

Target: < 1:30 | Difficulty: Easy

Reverse a string in-place.

Pattern: Opposite ends two pointers
- Swap characters at left and right
- Move pointers toward center

Examples:
    >>> s = ["h", "e", "l", "l", "o"]
    >>> reverse_string(s)
    >>> s
    ['o', 'l', 'l', 'e', 'h']

Edge cases:
    - Empty array: no change
    - Single character: no change
    - Even vs odd length
"""


def reverse_string(s: list[str]) -> None:
    """Reverse string in-place.

    Args:
        s: List of characters to reverse (modified in place).

    Returns:
        None (modifies list in place).

    Time: O(n) - n/2 swaps
    Space: O(1) - in-place
    """
    left = 0
    right = len(s) - 1

    while left < right:
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1

        
