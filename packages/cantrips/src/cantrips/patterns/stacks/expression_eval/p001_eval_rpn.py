"""
CANTRIP 1: Evaluate Reverse Polish Notation (LeetCode #150)

Target: < 5:00 | Difficulty: Medium

Evaluate an arithmetic expression in Reverse Polish Notation (RPN).
Valid operators are +, -, *, and /.
Each operand may be an integer or another expression.

RPN (Postfix): operators come AFTER operands
"2 1 +" means "2 + 1"

Pattern: Stack for operands
- Stack holds numbers (partial results)
- When you see number: push it
- When you see operator: pop 2, compute, push result
- Watch order: b = pop(), a = pop(), then a OP b
- int(a / b) truncates toward zero

Examples:
    >>> tokens = ["2", "1", "+", "3", "*"]
    >>> eval_rpn(tokens)
    9

    >>> tokens = ["4", "13", "5", "/", "+"]
    >>> eval_rpn(tokens)
    6

    >>> tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    >>> eval_rpn(tokens)
    22

Edge cases:
    - Single number (no operators)
    - Division truncates toward zero: int(a / b)
    - Negative numbers in tokens: "-3"
    - Order matters for - and /: "4 2 -" -> 4-2=2 (not 2-4)
"""


def eval_rpn(tokens: list[str]) -> int:
    """Evaluate expression in Reverse Polish Notation.

    Args:
        tokens: List of operators and operands in RPN order.

    Returns:
        Result of the expression.

    Time: O(n) - single pass
    Space: O(n) - stack size
    """
    pass
