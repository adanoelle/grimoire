"""
Sliding Window: Variable Size - Reference Implementations

Core Intuition:
    Expand window by moving right pointer. When constraint violated,
    contract by moving left pointer. Track max/min window seen.

When to Use:
    - "Longest substring with..."
    - "Minimum subarray with..."
    - "At most K" or "at least X" constraints
    - Window size changes based on condition

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


def length_of_longest_substring(s: str) -> int:
    """
    REFERENCE: Longest Substring Without Repeating Characters (LeetCode #3)

    This is THE canonical variable window template. Master this!

    Args:
        s: Input string

    Returns:
        Length of longest substring without repeating characters

    Time: O(n), Space: O(min(n, alphabet))
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


def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    REFERENCE: Minimum Size Subarray Sum (LeetCode #209)

    Find minimal length subarray with sum >= target.

    Args:
        nums: Array of positive integers
        target: Target sum

    Returns:
        Length of minimum subarray, or 0 if impossible

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


def total_fruit(fruits: list[int]) -> int:
    """
    REFERENCE: Fruit Into Baskets (LeetCode #904)

    Pick maximum fruits with at most 2 types (baskets).

    This is: "longest subarray with at most K=2 distinct elements"

    Args:
        fruits: Array where fruits[i] is type of fruit at tree i

    Returns:
        Maximum number of fruits that can be collected

    Time: O(n), Space: O(1) - at most 2 types in dict
    """
    from collections import defaultdict

    fruit_count = defaultdict(int)
    left = 0
    max_fruits = 0

    for right in range(len(fruits)):
        # Expand: add fruit at right
        fruit_count[fruits[right]] += 1

        # Contract: while more than 2 types
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    REFERENCE: Longest Substring with At Most K Distinct Characters (LeetCode #340)

    Args:
        s: Input string
        k: Maximum distinct characters

    Returns:
        Length of longest substring with <= k distinct chars

    Time: O(n), Space: O(k)
    """
    if k == 0:
        return 0

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


def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    """
    REFERENCE: Subarray Product Less Than K (LeetCode #713)

    Count number of contiguous subarrays where product < k.

    Args:
        nums: Array of positive integers
        k: Product threshold

    Returns:
        Count of valid subarrays

    Time: O(n), Space: O(1)
    """
    if k <= 1:
        return 0

    product = 1
    left = 0
    count = 0

    for right in range(len(nums)):
        # Expand: multiply by nums[right]
        product *= nums[right]

        # Contract: while product too large
        while product >= k:
            product //= nums[left]
            left += 1

        # Add count of all subarrays ending at right
        # From [left, right] to [right, right], that's (right - left + 1) subarrays
        count += right - left + 1

    return count


if __name__ == "__main__":
    print("=" * 60)
    print("SLIDING WINDOW (VARIABLE SIZE) - REFERENCE IMPLEMENTATIONS")
    print("=" * 60)
    print()
    print("✓ All reference implementations loaded")
    print()
    print("Available functions:")
    print("  - length_of_longest_substring()")
    print("  - min_subarray_len()")
    print("  - total_fruit()")
    print("  - length_of_longest_substring_k_distinct()")
    print("  - num_subarray_product_less_than_k()")
    print()
    print("Master the expand-contract dance!")
    print("=" * 60)
