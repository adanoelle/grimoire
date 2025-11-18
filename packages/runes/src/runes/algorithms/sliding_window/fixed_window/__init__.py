"""
Sliding Window: Fixed Size - Reference Implementations

Core Intuition:
    Maintain a window of exactly k elements. Slide it across the array,
    updating the result as you go. Each element enters once and exits once.

When to Use:
    - Finding max/min/average of k consecutive elements
    - Problem explicitly mentions "subarray of size k"
    - Need to process all windows of fixed size
    - Pattern matching within fixed-length windows

Time Complexity: O(n) - each element processed at most twice
Space Complexity: O(1) or O(k) depending on what we track

Key: Avoid recalculating the entire window each time!
"""


def find_max_average(nums: list[int], k: int) -> float:
    """
    REFERENCE: Maximum Average Subarray I (LeetCode #643)

    Find the maximum average of any contiguous subarray of length k.

    Args:
        nums: Array of integers
        k: Window size

    Returns:
        Maximum average value

    Time: O(n), Space: O(1)
    """
    if not nums or k > len(nums):
        return 0.0

    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(nums)):
        # Remove leftmost, add rightmost
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


def num_of_subarrays(arr: list[int], k: int, threshold: int) -> int:
    """
    REFERENCE: Number of Sub-arrays of Size K and Average >= Threshold (LeetCode #1343)

    Count subarrays of size k where average >= threshold.

    Args:
        arr: Array of integers
        k: Window size
        threshold: Minimum average threshold

    Returns:
        Count of qualifying subarrays

    Time: O(n), Space: O(1)
    """
    if not arr or k > len(arr):
        return 0

    # Optimization: compare sum to threshold * k instead of calculating average each time
    target_sum = threshold * k
    count = 0

    # Calculate first window
    window_sum = sum(arr[:k])
    if window_sum >= target_sum:
        count += 1

    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum >= target_sum:
            count += 1

    return count


def count_good_substrings(s: str) -> int:
    """
    REFERENCE: Substrings of Size Three with Distinct Characters (LeetCode #1876)

    Count substrings of length 3 where all characters are distinct.

    Args:
        s: Input string

    Returns:
        Count of good substrings

    Time: O(n), Space: O(1)
    """
    if len(s) < 3:
        return 0

    count = 0

    # Slide fixed window of size 3
    for i in range(len(s) - 2):
        # Check if all 3 characters are distinct
        window = s[i:i+3]
        if len(set(window)) == 3:
            count += 1

    return count


def check_inclusion(s1: str, s2: str) -> bool:
    """
    REFERENCE: Permutation in String (LeetCode #567)

    Check if s2 contains any permutation of s1.

    Args:
        s1: Pattern string
        s2: Search string

    Returns:
        True if permutation found, False otherwise

    Time: O(n), Space: O(1) - fixed alphabet size
    """
    if len(s1) > len(s2):
        return False

    from collections import Counter

    # Create frequency map for s1
    s1_count = Counter(s1)
    window_count = Counter()

    # Initialize first window
    for i in range(len(s1)):
        window_count[s2[i]] += 1

    # Check first window
    if window_count == s1_count:
        return True

    # Slide the window
    for i in range(len(s1), len(s2)):
        # Add new character
        window_count[s2[i]] += 1

        # Remove old character
        left_char = s2[i - len(s1)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]

        # Check if current window matches
        if window_count == s1_count:
            return True

    return False


def find_anagrams(s: str, p: str) -> list[int]:
    """
    REFERENCE: Find All Anagrams in a String (LeetCode #438)

    Find all start indices where p's anagrams appear in s.

    Args:
        s: Search string
        p: Pattern string

    Returns:
        List of start indices

    Time: O(n), Space: O(1) - fixed alphabet size
    """
    if len(p) > len(s):
        return []

    from collections import Counter

    result = []
    p_count = Counter(p)
    window_count = Counter()

    # Initialize first window
    for i in range(len(p)):
        window_count[s[i]] += 1

    # Check first window
    if window_count == p_count:
        result.append(0)

    # Slide the window
    for i in range(len(p), len(s)):
        # Add new character
        window_count[s[i]] += 1

        # Remove old character
        left_char = s[i - len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]

        # Check if current window is an anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)

    return result


if __name__ == "__main__":
    print("=" * 60)
    print("SLIDING WINDOW (FIXED SIZE) - REFERENCE IMPLEMENTATIONS")
    print("=" * 60)
    print()
    print("✓ All reference implementations loaded")
    print()
    print("Available functions:")
    print("  - find_max_average()")
    print("  - num_of_subarrays()")
    print("  - count_good_substrings()")
    print("  - check_inclusion()")
    print("  - find_anagrams()")
    print()
    print("Master the expand-contract rhythm!")
    print("=" * 60)
