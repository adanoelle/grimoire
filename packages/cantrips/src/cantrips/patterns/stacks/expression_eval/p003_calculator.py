"""
CANTRIP 3: Basic Calculator (LeetCode #224)

Target: < 10:00 | Difficulty: Hard

Evaluate infix expression with +, -, (, ), and spaces.
NO multiplication or division.

The challenge: Parentheses can nest and reverse sign.
Example: "2 - (3 + (4 - 5))" -> 2 - (3 + (-1)) -> 2 - 2 -> 0

Pattern: Stack for (result, sign) pairs
- Stack stores (running_result, sign_before_paren)
- Track: result (accumulator), sign (1 or -1), num (current number)
- When '(': push (result, sign), reset result=0, sign=1
- When ')': pop, compute: result = prev_result + prev_sign * result
- When digit: build number
- When '+'/'-': apply previous operation, update sign
- No precedence needed (only +, -)

Examples:
    >>> s = "1 + 1"
    >>> calculate(s)
    2

    >>> s = " 2-1 + 2 "
    >>> calculate(s)
    3

    >>> s = "(1+(4+5+2)-3)+(6+8)"
    >>> calculate(s)
    23

Edge cases:
    - No parentheses: "1 + 2"
    - Nested parentheses: "1+(2-(3+4))"
    - Leading negative: "-2+ 1"
    - Spaces everywhere
"""


def calculate(s: str) -> int:
    """Evaluate infix expression with +, -, and parentheses.

    Args:
        s: Expression string with +, -, (, ), digits, spaces.

    Returns:
        Result of the expression.

    Time: O(n) - single pass
    Space: O(n) - stack depth for nested parens
    """
    pass
