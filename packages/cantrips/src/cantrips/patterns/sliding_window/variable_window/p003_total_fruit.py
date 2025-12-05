"""
CANTRIP 3: Fruit Into Baskets (LeetCode #904)

Target: < 4:00 | Difficulty: Medium

Pick maximum fruits where you have 2 baskets.
Each basket holds one fruit type. Find max fruits with at most 2 types.

This is: "longest subarray with at most K=2 distinct elements"

Pattern: Variable window with frequency map
- Track frequency of each fruit type in window
- Contract when types > 2

Examples:
    >>> total_fruit([1, 2, 1])
    3
    >>> total_fruit([0, 1, 2, 2])
    3
    >>> total_fruit([1, 2, 3, 2, 2])
    4

Edge cases:
    - All same type: return len(fruits)
    - Alternating two types: return len(fruits)
    - More than 2 types: need to find best window
"""

from collections import Counter


def total_fruit(fruits: list[int]) -> int:
    """Find maximum fruits collectable with 2 baskets.

    Args:
        fruits: List of fruit types (integers).

    Returns:
        Maximum number of fruits that can be collected.

    Time: O(n) - single pass
    Space: O(1) - at most 3 types in counter
    """
    pass  # Your solution here
