"""
🥋 STACK MATCHING - KATA PRACTICE

Master stack-based matching through deliberate practice.

RULES:
1. Code from memory - NO looking at reference!
2. Set timer for each kata
3. Run tests after coding
4. If bugs: understand why, redo tomorrow
5. If perfect: celebrate, repeat until automatic

TARGET: < 5 minutes, zero bugs, can explain while coding
"""

def is_valid(s: str) -> bool:
    """
    KATA 1: Valid Parentheses (LeetCode #20)

    ⏱️  Target time: < 5 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Given a string containing just '(', ')', '{', '}', '[', ']',
    determine if the input string is valid.

    Valid means:
    - Open brackets closed by same type
    - Open brackets closed in correct order
    - Every closing bracket has matching opening bracket

    Edge cases:
    - Empty string (valid)
    - Single character (invalid)
    - All opening or all closing (invalid)
    - Interleaved but not nested properly: "([)]" (invalid)

    Hint if stuck:
    - Use stack to track opening brackets
    - Hash map: closing → opening for quick lookup
    - Check stack non-empty before pop!

    Examples:
        >>> is_valid("()")
        True
        >>> is_valid("()[]{}")
        True
        >>> is_valid("(]")
        False
        >>> is_valid("([)]")
        False

    START CODING BELOW:
    """
    pass


# MASTERY TRACKING
"""
Track your practice sessions. Be honest about bugs!

Date       | Time  | Bugs | Notes
-----------|-------|------|-------
YYYY-MM-DD | MM:SS | N    |
"""

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
