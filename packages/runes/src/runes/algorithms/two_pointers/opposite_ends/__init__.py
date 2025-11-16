"""
Two Pointers: Opposite Ends Pattern

Core Intuition:
    Start with pointers at both ends of array/string, move them toward each other.
    Avoids nested loops by processing from both directions simultaneously.

When to Use:
    - Sorted or sortable array
    - Finding pairs with a property
    - Palindrome checking
    - Container/area problems

Time Complexity: O(n) - single pass
Space Complexity: O(1) - only pointer variables

Common Pitfalls:
    - Forgetting to handle even/odd length differently for palindromes
    - Not checking if left < right before accessing
    - Moving both pointers when you should only move one
"""


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """
    TEMPLATE: Find pair that sums to target in sorted array.

    This is the canonical two-pointer opposite-ends template.
    Study this until you can code it with eyes closed.

    Args:
        nums: Sorted array of integers
        target: Target sum

    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
        Empty list if no solution

    Examples:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum_sorted([2, 3, 4], 6)
        [0, 2]
        >>> two_sum_sorted([1, 2, 3], 10)
        []

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            # Need larger sum, move left pointer right
            left += 1
        else:
            # Need smaller sum, move right pointer left
            right -= 1

    return []


def is_palindrome(s: str) -> bool:
    """
    TEMPLATE: Check if string is palindrome (alphanumeric only, case-insensitive).

    Args:
        s: Input string

    Returns:
        True if palindrome, False otherwise

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True

    Time: O(n), Space: O(1)
    """
    # Preprocess: keep only alphanumeric, lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())

    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def container_with_most_water(heights: list[int]) -> int:
    """
    TEMPLATE: Find maximum area container (LC #11).

    Key insight: Start with widest container, move pointer with smaller height
    (moving the taller one can't increase area).

    Args:
        heights: List of heights

    Returns:
        Maximum area of water container

    Examples:
        >>> container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        >>> container_with_most_water([1, 1])
        1

    Time: O(n), Space: O(1)
    """
    max_area = 0
    left, right = 0, len(heights) - 1

    while left < right:
        # Calculate current area
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        max_area = max(max_area, area)

        # Move pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("✓ Two Pointers (Opposite Ends) templates loaded")
    print("Study these until you can code them from memory!")
