"""
Sliding Window: Fixed Size

Core Intuition:
    Maintain a window of exactly k elements. Slide it across the array,
    updating the result as you go. Each element enters once and exits once.

When to Use:
    - Finding max/min/average of k consecutive elements
    - Problem explicitly mentions "subarray of size k"
    - Need to process all windows of fixed size

Time Complexity: O(n) - each element processed at most twice
Space Complexity: O(1) or O(k) depending on what we track

Key: Avoid recalculating the entire window each time!
"""


def max_sum_subarray_size_k(nums: list[int], k: int) -> int:
    """
    TEMPLATE: Maximum sum of subarray of size k.

    This is THE canonical fixed window template. Master this first.

    Args:
        nums: Array of integers
        k: Window size

    Returns:
        Maximum sum of any k consecutive elements

    Examples:
        >>> max_sum_subarray_size_k([2, 1, 5, 1, 3, 2], 3)
        9
        >>> max_sum_subarray_size_k([2, 3, 4, 1, 5], 2)
        7

    Time: O(n), Space: O(1)
    """
    if not nums or k > len(nums):
        return 0

    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(nums)):
        # Remove leftmost element, add new rightmost element
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


def average_of_subarrays_size_k(nums: list[int], k: int) -> list[float]:
    """
    TEMPLATE: Average of each subarray of size k (LC #643).

    Similar to max sum, but return all averages.

    Args:
        nums: Array of numbers
        k: Window size

    Returns:
        List of averages for each window

    Examples:
        >>> average_of_subarrays_size_k([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
        [2.2, 2.8, 2.4, 3.6, 2.8]

    Time: O(n), Space: O(n) for output
    """
    if not nums or k > len(nums):
        return []

    result = []
    window_sum = sum(nums[:k])
    result.append(window_sum / k)

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        result.append(window_sum / k)

    return result


def max_of_all_subarrays_size_k(nums: list[int], k: int) -> list[int]:
    """
    TEMPLATE: Maximum element in each window of size k (LC #239).

    This requires a deque to track potential maximums efficiently.
    More advanced than basic sliding window!

    Args:
        nums: Array of integers
        k: Window size

    Returns:
        List of maximum values for each window

    Examples:
        >>> max_of_all_subarrays_size_k([1, 3, -1, -3, 5, 3, 6, 7], 3)
        [3, 3, 5, 5, 6, 7]

    Time: O(n), Space: O(k)
    """
    from collections import deque

    if not nums or k == 0:
        return []

    if k == 1:
        return nums

    result = []
    # Deque stores indices of potential maximums
    dq = deque()

    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements (they can't be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Start recording results after first window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("✓ Sliding Window (Fixed Size) templates loaded")
    print("Master the expand-contract rhythm!")
