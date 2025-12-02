"""
Stack Pattern: Expression Evaluation

Core Intuition:
    Stack stores operands. When operator encountered,
    pop operands, compute, push result. Process left-to-right.

When to Use:
    - Reverse Polish Notation (RPN)
    - Postfix expressions
    - Calculator problems
    - Expression parsing without parentheses

Time Complexity: O(n)
Space Complexity: O(n)

Key: Stack maintains partial results, operators consume top elements
"""

def eval_rpn(tokens: list[str]) -> int:
    """
    REFERENCE: Evaluate Reverse Polish Notation (LeetCode #150)

    Evaluate arithmetic expression in Reverse Polish Notation.

    Args:
        tokens: List of strings representing RPN expression

    Returns:
        Result of evaluating the expression

    Time: O(n), Space: O(n)

    Examples:
        >>> eval_rpn(["2","1","+","3","*"])
        9
        >>> eval_rpn(["4","13","5","/","+"])
        6
        >>> eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        22
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            # Pop two operands (order matters for - and /)
            b = stack.pop()  # Second operand
            a = stack.pop()  # First operand

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # '/'
                # Truncate toward zero (Python3 requirement)
                stack.append(int(a / b))
        else:
            # Token is a number
            stack.append(int(token))

    return stack[0]  # Final result


if __name__ == "__main__":
    print("=" * 60)
    print("STACK PATTERN: Expression Evaluation")
    print("=" * 60)
    print()
    print("✓ Evaluate RPN reference implementation loaded")
    print()
    print("Process RPN expressions left-to-right:")
    print("  - Numbers: push to stack")
    print("  - Operators: pop 2 operands, compute, push result")
    print("  - Order matters for - and /")
    print("  - Final result: single value on stack")
    print()
    print("=" * 60)
