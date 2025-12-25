"""
CANTRIP 2: Next Greater Element I (LeetCode #496)

Target: < 6:00 | Difficulty: Easy

nums1 is a subset of nums2. For each element in nums1,
find the next greater element in nums2.
Return -1 if no greater element exists.

nums2 has no duplicates.

Pattern: Monotonic decreasing stack + hash map
- Process nums2 with monotonic stack to build {num -> next_greater}
- When nums2[i] > stack top: found next greater, store in map
- Then lookup nums1 elements in map

Examples:
    >>> nums1, nums2 = [4, 1, 2], [1, 3, 4, 2]
    >>> next_greater_element(nums1, nums2)
    [-1, 3, -1]

    >>> nums1, nums2 = [2, 4], [1, 2, 3, 4]
    >>> next_greater_element(nums1, nums2)
    [3, -1]

Edge cases:
    - Element is last in nums2 -> -1
    - Element is largest in nums2 -> -1
    - All elements decreasing -> all -1
"""


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """Find next greater element in nums2 for each element in nums1.

    Args:
        nums1: Subset of nums2 to query.
        nums2: Array to search for next greater elements.

    Returns:
        List of next greater elements, -1 if none exists.

    Time: O(m + n) - process nums2 once, query nums1 once
    Space: O(n) - stack and hash map
    """
    pass
