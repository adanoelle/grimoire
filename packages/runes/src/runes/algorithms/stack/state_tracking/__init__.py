"""
Stack Pattern: State Tracking

Core Intuition:
    Use auxiliary data structure to track state/invariants
    alongside main stack. Both stay synchronized.

When to Use:
    - Need to track min/max/frequency while maintaining stack
    - O(1) constraint for queries
    - State depends on current stack depth

Time Complexity: All operations O(1)
Space Complexity: O(n)

Key: Auxiliary structure mirrors main stack growth
"""

class MinStack:
    """
    REFERENCE: Min Stack (LeetCode #155)

    Stack with O(1) getMin() operation.

    Complexity:
        - push: O(1)
        - pop: O(1)
        - top: O(1)
        - getMin: O(1)

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
    """

    def __init__(self):
        """Initialize empty min stack."""
        self.stack = []
        self.min_stack = []  # Tracks minimum at each depth

    def push(self, val: int) -> None:
        """
        Push element onto stack.

        Args:
            val: Value to push

        Time: O(1), Space: O(1)
        """
        self.stack.append(val)
        # Min at this depth is min(val, previous min)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        """
        Remove top element from stack.

        Time: O(1), Space: O(1)
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """
        Get top element without removing.

        Returns:
            Top element of stack

        Time: O(1), Space: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Get minimum element in constant time.

        Returns:
            Minimum element currently in stack

        Time: O(1), Space: O(1)
        """
        return self.min_stack[-1]


if __name__ == "__main__":
    print("=" * 60)
    print("STACK PATTERN: State Tracking")
    print("=" * 60)
    print()
    print("✓ Min Stack reference implementation loaded")
    print()
    print("Maintain O(1) invariants with auxiliary stack:")
    print("  - Two stacks: main + min tracker")
    print("  - Min stack mirrors main stack growth")
    print("  - Each depth knows its minimum")
    print()
    print("=" * 60)
