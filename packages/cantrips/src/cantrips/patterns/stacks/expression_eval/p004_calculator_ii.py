"""
CANTRIP 4: Basic Calculator II (LeetCode #227)

Target: < 8:00 | Difficulty: Medium

Evaluate infix expression with +, -, *, /, and spaces.
NO parentheses.

The challenge: Handle operator precedence (* and / before + and -)

Pattern: Stack with deferred addition
- Stack holds numbers
- Track: num (current), sign (last operator)
- When +/-: push (+/- num) to stack, defer addition
- When *//: pop last, compute, push result (immediate eval)
- End: sum entire stack
- Initialize sign = '+', num = 0

Examples:
    >>> s = "3+2*2"
    >>> calculate_ii(s)
    7

    >>> s = " 3/2 "
    >>> calculate_ii(s)
    1

    >>> s = " 3+5 / 2 "
    >>> calculate_ii(s)
    5

Edge cases:
    - Only one number: "42"
    - Division: "14/3" -> 4 (truncate toward zero)
    - Negative result: "1-5" -> -4
    - Spaces: " 3+5 / 2 "
"""


def calculate_ii(s: str) -> int:
    """Evaluate infix expression with +, -, *, / (no parentheses).

    Args:
        s: Expression string with operators, digits, spaces.

    Returns:
        Result of the expression.

    Time: O(n) - single pass
    Space: O(n) - stack size
    """
    pass
