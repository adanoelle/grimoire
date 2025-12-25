"""
CANTRIP 4: Maximum Frequency Stack (LeetCode #895)

Target: < 8:00 | Difficulty: Hard

Design a stack where pop() removes the most frequent element.
If tie: remove the one closest to top.

Operations:
- push(val): Push val onto stack
- pop(): Remove and return most frequent element
          (ties broken by most recent)

Both operations must be O(1)!

Pattern: Triple tracking
- Track THREE things:
  1. freq: {val -> frequency}
  2. group: {frequency -> stack of vals with that frequency}
  3. max_freq: current maximum frequency
- push(val): freq[val]++, group[freq[val]].push(val), update max_freq
- pop(): val = group[max_freq].pop(), freq[val]--, adjust max_freq if needed
- This is NOT a traditional stack - it's frequency-based!

Examples:
    >>> fs = FreqStack()
    >>> fs.push(5)
    >>> fs.push(7)
    >>> fs.push(5)
    >>> fs.push(7)
    >>> fs.push(4)
    >>> fs.push(5)
    >>> fs.pop()  # 5 (freq 3)
    5
    >>> fs.pop()  # 7 (freq 2, most recent)
    7
    >>> fs.pop()  # 5 (freq 2, most recent)
    5
    >>> fs.pop()  # 4 (freq 1)
    4

Edge cases:
    - Single element
    - All same frequency
    - Frequency changes after pops
"""


class FreqStack:
    """Stack that pops most frequent element.

    Time: O(1) for push and pop
    Space: O(n) - frequency tracking
    """

    def __init__(self):
        """Initialize the FreqStack."""
        pass

    def push(self, val: int) -> None:
        """Push element onto stack.

        Args:
            val: Value to push.
        """
        pass

    def pop(self) -> int:
        """Pop and return most frequent element.

        Returns:
            Most frequent element (ties broken by recency).
        """
        pass
