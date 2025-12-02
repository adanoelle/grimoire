"""
🥋 STACK EXPRESSION EVALUATION - KATA PRACTICE

Master evaluating expressions with stack-based operand tracking.

RULES:
1. Code from memory - NO looking at reference!
2. Set timer for each kata
3. Run tests after coding
4. If bugs: understand why, redo tomorrow
5. If perfect: celebrate, repeat until automatic

TARGET: < 7 minutes, zero bugs, O(n) time
"""

def eval_rpn(tokens: list[str]) -> int:
    """
    KATA 3: Evaluate Reverse Polish Notation (LeetCode #150)

    ⏱️  Target time: < 7 minutes
    🎯 Goal: Zero bugs, O(n) time, O(n) space

    Evaluate an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /.
    Each operand may be an integer or another expression.

    Edge cases:
    - Single number (no operators)
    - Division truncates toward zero
    - Negative numbers in tokens
    - Order matters for - and /

    Hint if stuck:
    - Stack holds numbers (partial results)
    - When you see operator: pop 2, compute, push result
    - Watch order: b = pop(), a = pop(), then a OP b
    - int(a / b) truncates toward zero

    Examples:
        >>> eval_rpn(["2","1","+","3","*"])
        9  # ((2 + 1) * 3) = 9
        >>> eval_rpn(["4","13","5","/","+"])
        6  # (4 + (13 / 5)) = (4 + 2) = 6
        >>> eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        22

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
