"""
Binary Search - The Most Important Algorithm Template

Core Intuition:
    If data is sorted (or answer space is monotonic), we can eliminate
    half the search space with each comparison. O(log n) instead of O(n).

When to Use:
    - Array is sorted
    - Can verify if answer X works in O(n) or less (binary search on answer)
    - Finding boundaries (first/last occurrence)
    - Rotated sorted arrays

Time Complexity: O(log n)
Space Complexity: O(1) iterative, O(log n) recursive

CRITICAL:
    Binary search has many off-by-one error traps. Practice until bug-free!
"""


def binary_search_classic(nums: list[int], target: int) -> int:
    """
    TEMPLATE: Classic binary search - find exact element.

    THIS IS THE MOST IMPORTANT TEMPLATE TO MASTER.
    Code it perfectly 100 times until you can do it with eyes closed.

    Args:
        nums: Sorted array
        target: Element to find

    Returns:
        Index of target, or -1 if not found

    Examples:
        >>> binary_search_classic([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search_classic([1, 2, 3, 4, 5], 6)
        -1
        >>> binary_search_classic([], 1)
        -1

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:  # Note: <= for exact search
        mid = left + (right - left) // 2  # Avoid overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found


def find_first_occurrence(nums: list[int], target: int) -> int:
    """
    TEMPLATE: Find FIRST (leftmost) occurrence of target.

    Key difference from classic: Don't return immediately when found.
    Keep searching left to find the first occurrence.

    Args:
        nums: Sorted array (may have duplicates)
        target: Element to find

    Returns:
        Index of first occurrence, or -1 if not found

    Examples:
        >>> find_first_occurrence([1, 2, 2, 2, 3], 2)
        1
        >>> find_first_occurrence([1, 2, 2, 2, 3], 4)
        -1

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid      # Found it, but keep searching left
            right = mid - 1   # Continue searching in left half
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def find_last_occurrence(nums: list[int], target: int) -> int:
    """
    TEMPLATE: Find LAST (rightmost) occurrence of target.

    Similar to first occurrence, but search right after finding.

    Args:
        nums: Sorted array (may have duplicates)
        target: Element to find

    Returns:
        Index of last occurrence, or -1 if not found

    Examples:
        >>> find_last_occurrence([1, 2, 2, 2, 3], 2)
        3
        >>> find_last_occurrence([1, 2, 2, 2, 3], 4)
        -1

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid      # Found it, but keep searching right
            left = mid + 1    # Continue searching in right half
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def search_insert_position(nums: list[int], target: int) -> int:
    """
    TEMPLATE: Find position where target should be inserted (LC #35).

    This finds the leftmost position where target can be inserted
    to maintain sorted order.

    Args:
        nums: Sorted array
        target: Value to insert

    Returns:
        Index where target should be inserted

    Examples:
        >>> search_insert_position([1, 3, 5, 6], 5)
        2
        >>> search_insert_position([1, 3, 5, 6], 2)
        1
        >>> search_insert_position([1, 3, 5, 6], 7)
        4

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Insert position is where left ended up


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("✓ Binary Search templates loaded")
    print("MASTER THESE - they're the foundation of O(log n) thinking!")
