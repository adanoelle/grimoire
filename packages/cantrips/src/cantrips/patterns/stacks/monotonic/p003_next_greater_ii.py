"""
CANTRIP 3: Next Greater Element II (LeetCode #503)

Target: < 7:00 | Difficulty: Medium

Given a circular array, return next greater element for each element.
The next greater of nums[i] might be before i (wrapping around).
Return -1 if no greater element exists.

Circular: nums = [1, 2, 1] -> [2, -1, 2] (last 1 wraps to find 2)

Pattern: Monotonic decreasing stack with 2x iteration
- Circular = iterate TWICE (2*n iterations)
- Use index % n to access actual element
- Only fill answer array once per index
- Second pass finds next greater by wrapping

Examples:
    >>> nums = [1, 2, 1]
    >>> next_greater_elements(nums)
    [2, -1, 2]

    >>> nums = [1, 2, 3, 4, 3]
    >>> next_greater_elements(nums)
    [2, 3, 4, -1, 4]

Edge cases:
    - All elements same -> all -1
    - Max element -> -1
    - Strictly increasing -> wrap around
"""


def next_greater_elements(nums: list[int]) -> list[int]:
    """Find next greater element in circular array.

    Args:
        nums: Circular array of integers.

    Returns:
        List of next greater elements, -1 if none exists.

    Time: O(n) - 2n iterations, each element processed at most twice
    Space: O(n) - stack size
    """
    pass
