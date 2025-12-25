"""
CANTRIP 5: Basic Calculator III (LeetCode #772 - Premium)

Target: < 12:00 | Difficulty: Hard

Evaluate infix expression with +, -, *, /, (, ), and spaces.
Combines Calculator I (parentheses) and Calculator II (precedence).

This is the FULL calculator - all features combined!

Pattern: Recursive or stack-based
- Recursive approach: when '(' found, evaluate sub-expression
- OR: Stack-based like Calculator II, but handle '(' by recursion
- When '(': recursively evaluate inner expression
- When ')': return result of this level
- Otherwise: use Calculator II logic (precedence handling)

Helper function approach:
- helper(s, index) returns (result, next_index)
- Recursive call for each '('
- Return when ')' found

Examples:
    >>> s = "2*(5+5*2)/3+(6/2+8)"
    >>> calculate_iii(s)
    21

    >>> s = "(2+6*3+5-(3*14/7+2)*5)+3"
    >>> calculate_iii(s)
    -12

    >>> s = "1+2*3"
    >>> calculate_iii(s)
    7

Edge cases:
    - Precedence with parens: "2*(3+4)"
    - Nested parens with ops: "2*(5+5*2)/3+(6/2+8)"
    - Negative in parens: "-(2+3)"
"""


def calculate_iii(s: str) -> int:
    """Evaluate full infix expression with all operators and parentheses.

    Args:
        s: Expression string with +, -, *, /, (, ), digits, spaces.

    Returns:
        Result of the expression.

    Time: O(n) - each character processed once
    Space: O(n) - recursion/stack depth
    """
    pass
