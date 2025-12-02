"""
Stack Pattern: Matching/Pairing

Core Intuition:
    Use stack LIFO behavior to match pairs. Most recent opening
    bracket must match the next closing bracket.

When to Use:
    - Matching pairs (parentheses, brackets, tags)
    - Balanced expressions
    - Nested structures with open/close markers

Time Complexity: O(n)
Space Complexity: O(n)

Key: Stack tracks "most recent unmatched opening"
"""

def is_valid(s: str) -> bool:
    """
    REFERENCE: Valid Parentheses (LeetCode #20)

    Check if string of parentheses/brackets is valid.

    Args:
        s: String containing only '(', ')', '{', '}', '[', ']'

    Returns:
        True if all brackets are properly opened and closed in correct order,
        False otherwise

    Time: O(n), Space: O(n)

    Examples:
        >>> is_valid("()")
        True
        >>> is_valid("()[]{}")
        True
        >>> is_valid("(]")
        False
        >>> is_valid("([)]")
        False
        >>> is_valid("{[]}")
        True
    """
    stack = []
    close_to_open = {"}": "{", "]": "[", ")": "("}

    for char in s:
        if char in close_to_open:
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack


if __name__ == "__main__":
    print("=" * 60)
    print("STACK PATTERN: Matching/Pairing")
    print("=" * 60)
    print()
    print("✓ Valid Parentheses reference implementation loaded")
    print()
    print("Use stack LIFO to match pairs:")
    print("  - Most recent opening must match next closing")
    print("  - Hash map for O(1) closing → opening lookup")
    print("  - Check stack non-empty before accessing top")
    print()
    print("=" * 60)
