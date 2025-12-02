"""
🥋 STACK STATE TRACKING - KATA PRACTICE

Master maintaining O(1) invariants with auxiliary data structures.

RULES:
1. Code from memory - NO looking at reference!
2. Set timer for each kata
3. Run tests after coding
4. If bugs: understand why, redo tomorrow
5. If perfect: celebrate, repeat until automatic

TARGET: < 8 minutes, zero bugs, all operations O(1)
"""

class MinStack:
    """
    KATA 2: Min Stack (LeetCode #155)

    ⏱️  Target time: < 8 minutes
    🎯 Goal: All operations O(1), clean design

    Design a stack that supports push, pop, top, and retrieving
    the minimum element in constant time.

    Operations:
    - push(val): Push element onto stack
    - pop(): Remove top element
    - top(): Get top element
    - getMin(): Retrieve minimum element

    All operations must be O(1)!

    Edge cases:
    - Stack with one element (min = that element)
    - Push smaller value (new min)
    - Pop current min (revert to previous min)
    - All same values

    Hint if stuck:
    - Use TWO stacks: main + min tracker
    - Min stack mirrors main stack, stores min at each depth
    - When pushing: min = min(val, current_min)
    - When popping: both stacks pop together

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

    START CODING BELOW:
    """

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
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
