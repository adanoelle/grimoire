"""
CANTRIP 5: Time Based Key-Value Store (LeetCode #981)

Target: < 9:00 | Difficulty: Medium

Design a time-based key-value store that stores multiple
values for the same key at different timestamps.

Operations:
- set(key, value, timestamp): Store value at timestamp
- get(key, timestamp): Get value at timestamp_prev <= timestamp
                      Return "" if no such value

Timestamps are strictly increasing for each key.

Pattern: Hash map + binary search
- Use hash map: {key -> list of (timestamp, value) pairs}
- set() is O(1): just append (sorted by construction)
- get() requires binary search for largest timestamp <= given
- Python bisect_right - 1 can help

Examples:
    >>> tm = TimeMap()
    >>> tm.set("foo", "bar", 1)
    >>> tm.get("foo", 1)
    'bar'
    >>> tm.get("foo", 3)
    'bar'
    >>> tm.set("foo", "bar2", 4)
    >>> tm.get("foo", 4)
    'bar2'
    >>> tm.get("foo", 5)
    'bar2'

Edge cases:
    - get() before any set() for that key
    - get() with exact timestamp match
    - get() with timestamp before all values
    - get() with timestamp after all values
"""


class TimeMap:
    """Time-based key-value store.

    Time: O(1) for set, O(log n) for get
    Space: O(n) - all key-value-timestamp tuples
    """

    def __init__(self):
        """Initialize the TimeMap."""
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Store value for key at timestamp.

        Args:
            key: Key to store.
            value: Value to store.
            timestamp: Timestamp (strictly increasing per key).
        """
        pass

    def get(self, key: str, timestamp: int) -> str:
        """Get value for key at or before timestamp.

        Args:
            key: Key to retrieve.
            timestamp: Target timestamp.

        Returns:
            Value at largest timestamp <= given, or "" if none.
        """
        pass
