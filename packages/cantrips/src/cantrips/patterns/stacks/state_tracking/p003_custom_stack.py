"""
CANTRIP 3: Design a Stack With Increment Operation (LeetCode #1381)

Target: < 6:00 | Difficulty: Medium

Design a stack with a fixed capacity that supports:
- CustomStack(maxSize): Initialize with max capacity
- push(x): Push x if stack not full
- pop(): Pop and return top, or -1 if empty
- increment(k, val): Add val to bottom k elements

The trick: increment must be O(1), not O(k)!

Pattern: Lazy increment with auxiliary array
- Use array/list + top pointer
- Lazy evaluation: Don't apply increment immediately!
- Auxiliary array to track pending increments at each index
- When pop: apply increment to that position, propagate down
- increment(k, val): Only update inc[k-1] += val

Examples:
    >>> stack = CustomStack(3)
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.pop()
    2
    >>> stack.push(2)
    >>> stack.push(3)
    >>> stack.push(4)  # Full, ignored
    >>> stack.increment(5, 100)  # Only 3 elements
    >>> stack.increment(2, 100)  # Bottom 2
    >>> stack.pop()
    103
    >>> stack.pop()
    202
    >>> stack.pop()
    201

Edge cases:
    - Push when full (ignore)
    - Pop when empty (return -1)
    - Increment more than size (only increment actual elements)
    - Increment 0 elements
"""


class CustomStack:
    """Stack with O(1) increment operation.

    Time: O(1) for all operations
    Space: O(maxSize) - fixed array
    """

    def __init__(self, maxSize: int):
        """Initialize stack with max capacity.

        Args:
            maxSize: Maximum stack capacity.
        """
        pass

    def push(self, x: int) -> None:
        """Push element if not full.

        Args:
            x: Value to push.
        """
        pass

    def pop(self) -> int:
        """Pop and return top element.

        Returns:
            Top element, or -1 if empty.
        """
        pass

    def increment(self, k: int, val: int) -> None:
        """Add val to bottom k elements.

        Args:
            k: Number of bottom elements to increment.
            val: Value to add.
        """
        pass
