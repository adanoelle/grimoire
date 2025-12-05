"""
CANTRIP 4: 3Sum (LeetCode #15)

Target: < 4:00 | Difficulty: Medium

Find all unique triplets that sum to zero.

Pattern: Sort + nested two pointers
- Sort array first
- Fix first element, use two pointers for remaining pair
- Skip duplicates at all levels

Examples:
    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> three_sum([0, 1, 1])
    []
    >>> three_sum([0, 0, 0])
    [[0, 0, 0]]

Edge cases:
    - All zeros: [[0, 0, 0]]
    - No valid triplets: []
    - Duplicates in input
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    """Find all unique triplets that sum to zero.

    Args:
        nums: List of integers.

    Returns:
        List of unique triplets.

    Time: O(n^2) - nested loop with two pointers
    Space: O(1) or O(n) depending on sort implementation
    """
    pass  # Your solution here
