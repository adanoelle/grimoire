"""
CANTRIP 2: Valid Palindrome (LeetCode #125)

Target: < 2:00 | Difficulty: Easy

Check if string is palindrome, considering only alphanumeric characters.

Pattern: Opposite ends two pointers
- Skip non-alphanumeric chars
- Compare characters case-insensitively

Examples:
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    >>> is_palindrome(" ")
    True

Edge cases:
    - Empty string: True
    - Single character: True
    - Only non-alphanumeric: True
    - Mixed case
"""


def is_palindrome(s: str) -> bool:
    """Check if string is a valid palindrome.

    Args:
        s: Input string (may contain non-alphanumeric chars).

    Returns:
        True if alphanumeric content forms a palindrome.

    Time: O(n) - single pass with two pointers
    Space: O(1) - in-place comparison
    """
    pass  # Your solution here
