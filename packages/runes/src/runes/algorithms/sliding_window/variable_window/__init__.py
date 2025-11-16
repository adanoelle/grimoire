"""
Sliding Window: Variable Size

Core Intuition:
    Expand window by moving right pointer. When constraint violated,
    contract by moving left pointer. Track max/min window seen.

When to Use:
    - "Longest substring with..."
    - "Minimum subarray with..."
    - Constraint on window contents (not just size)

Time Complexity: O(n) - each element enters and exits at most once
Space Complexity: O(1) or O(k) for tracking window state

Template:
    left = 0
    for right in range(len(arr)):
        # Expand: add arr[right] to window

        while window_violates_constraint:
            # Contract: remove arr[left] from window
            left += 1

        # Update result with current window
"""


def longest_substring_no_repeat(s: str) -> int:
    """
    TEMPLATE: Longest substring without repeating characters (LC #3).

    This is THE canonical variable window template. Master this!

    Args:
        s: Input string

    Returns:
        Length of longest substring without repeating characters

    Examples:
        >>> longest_substring_no_repeat("abcabcbb")
        3
        >>> longest_substring_no_repeat("bbbbb")
        1
        >>> longest_substring_no_repeat("pwwkew")
        3

    Time: O(n), Space: O(min(n, m)) where m is charset size
    """
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Expand: add s[right]
        while s[right] in char_set:
            # Contract: remove s[left] until no duplicate
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def min_subarray_sum_geq_target(nums: list[int], target: int) -> int:
    """
    TEMPLATE: Minimum length subarray with sum ≥ target (LC #209).

    Args:
        nums: Array of positive integers
        target: Target sum

    Returns:
        Length of minimum subarray, or 0 if impossible

    Examples:
        >>> min_subarray_sum_geq_target([2, 3, 1, 2, 4, 3], 7)
        2
        >>> min_subarray_sum_geq_target([1, 4, 4], 4)
        1
        >>> min_subarray_sum_geq_target([1, 1, 1], 11)
        0

    Time: O(n), Space: O(1)
    """
    left = 0
    window_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        # Expand: add nums[right]
        window_sum += nums[right]

        # Contract: while condition met, try to shrink
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    TEMPLATE: Longest substring with at most k distinct characters (LC #340).

    Args:
        s: Input string
        k: Maximum distinct characters

    Returns:
        Length of longest substring with ≤ k distinct chars

    Examples:
        >>> longest_substring_k_distinct("eceba", 2)
        3
        >>> longest_substring_k_distinct("aa", 1)
        2

    Time: O(n), Space: O(k)
    """
    from collections import defaultdict

    char_count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Expand: add s[right]
        char_count[s[right]] += 1

        # Contract: while too many distinct chars
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("✓ Sliding Window (Variable Size) templates loaded")
    print("Master the expand-contract dance!")
