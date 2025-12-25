"""
CANTRIP 1: Min Stack (LeetCode #155)

Target: < 5:00 | Difficulty: Medium

Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.

Operations:
- push(val): Push element onto stack
- pop(): Remove top element
- top(): Get top element
- getMin(): Retrieve minimum element

All operations must be O(1)!

Pattern: Auxiliary min-tracking stack
- Use TWO stacks: main + min tracker
- Min stack mirrors main stack, stores min at each depth
- When pushing: min = min(val, current_min if min_stack else val)
- When popping: both stacks pop together
- getMin() just returns min_stack[-1]

Examples:
    >>> ms = MinStack()
    >>> ms.push(-2)
    >>> ms.push(0)
    >>> ms.push(-3)
    >>> ms.getMin()
    -3
    >>> ms.pop()
    >>> ms.top()
    0
    >>> ms.getMin()
    -2

Edge cases:
    - Stack with one element (min = that element)
    - Push smaller value (new min)
    - Pop current min (revert to previous min)
    - All same values
    - Duplicate minimums
"""


class MinStack:
    """Stack with O(1) minimum retrieval.

    Time: O(1) for all operations
    Space: O(n) - two stacks
    """

    def __init__(self):
        """Initialize the MinStack."""
        pass

    def push(self, val: int) -> None:
        """Push element onto stack.

        Args:
            val: Value to push.
        """
        pass

    def pop(self) -> None:
        """Remove top element from stack."""
        pass

    def top(self) -> int:
        """Get top element.

        Returns:
            Top element value.
        """
        pass

    def getMin(self) -> int:
        """Get minimum element in stack.

        Returns:
            Minimum element value.
        """
        pass
