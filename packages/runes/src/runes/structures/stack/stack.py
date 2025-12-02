"""
Stack - LIFO (last in, first out) Data Structure

When to Use:

- Need to track the MOST RECENT thing
- Matching pairs (parentheses, brackets)
- Nested structures (function calls, DFS)
- Undo/redo operations
- Expression evaluation (calculators)
- Backtracking algorithms

Time Complexity: All operations O(1)
Space Complexity: O(n) where n = number of items

key: LIFO = "What did I see MOST RECENTLY"
"""

from typing import Any, Optional


class Stack:
    """
    LIFO Stack

    A stack maintains Last-In-First-Out ordering where the
    most recent element is the first removed.
    """

    def __init__(self):
        """Initialize an empty stack"""
        self._items = []

    def push(self, item: Any) -> None:
        """Add an element to the stack

        Args:
            item: the element to add

        Notes:
            Time: O(1), Space: O(1)
        """
        self._items.append(item)

    def pop(self) -> Optional[Any]:
        """Pop the most recent item"""
        if not self.is_empty():
            return self._items.pop()
        else:
            return None

    def peek(self) -> Optional[Any]:
        """Peek at the element at the top without removing it"""
        if not self.is_empty():
            return self._items[-1]
        else:
            return None

    def is_empty(self) -> bool:
        """Check if the stack is empty"""
        return len(self._items) == 0

    def size(self) -> int:
        """Check the size of the stack"""
        return len(self._items)

    def __str__(self) -> str:
        if self.is_empty():
            return "Stack([])"
        else:
            return f"Stack({self._items})"
           

if __name__ == "__main__":
    print("=" * 60)
    print("STACK - LIFO Data Structure")
    print("=" * 60)
    print()
    print("Demonstration:")
    print()

    stack = Stack()
    print(f"Created empty stack: {stack}")
    print(f"Is empty? {stack.is_empty()}")
    print()

    print("Pushing 1, 2, 3...")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    print(f"Peek: {stack.peek()}")
    print(f"Peek: {stack.peek()}")
    print()

    print("Popping...")
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    print()

    print("✓ Stack implementation complete!")
    print()
    print("REMEMBER: Stack = 'What did I see MOST RECENTLY?'")
    print("=" * 60)
