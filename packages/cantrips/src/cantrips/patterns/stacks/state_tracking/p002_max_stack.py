"""
CANTRIP 2: Max Stack (LeetCode #716 - Premium)

Target: < 5:00 | Difficulty: Medium

Design a stack that supports push, pop, top, and retrieving
the maximum element in constant time.

Operations:
- push(val): Push element onto stack
- pop(): Remove top element
- top(): Get top element
- getMax(): Retrieve maximum element

All operations must be O(1)!

Pattern: Auxiliary max-tracking stack
- EXACT same structure as MinStack
- Use TWO stacks: main + max tracker
- Max stack stores max at each depth
- When pushing: max = max(val, current_max if max_stack else val)
- Direct parallel to MinStack!

Examples:
    >>> ms = MaxStack()
    >>> ms.push(5)
    >>> ms.push(1)
    >>> ms.push(5)
    >>> ms.top()
    5
    >>> ms.getMax()
    5
    >>> ms.pop()
    >>> ms.getMax()
    5

Edge cases:
    - Stack with one element (max = that element)
    - Push larger value (new max)
    - Pop current max (revert to previous max)
    - All same values
    - Duplicate maximums
"""


class MaxStack:
    """Stack with O(1) maximum retrieval.

    Time: O(1) for all operations
    Space: O(n) - two stacks
    """

    def __init__(self):
        """Initialize the MaxStack."""
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

    def getMax(self) -> int:
        """Get maximum element in stack.

        Returns:
            Maximum element value.
        """
        pass
