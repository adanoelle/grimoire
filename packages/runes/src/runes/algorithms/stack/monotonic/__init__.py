"""
Stack Pattern: Monotonic Stack

Core Intuition:
    Maintain stack in strictly increasing or decreasing order.
    When element breaks monotonicity, you've found the
    "next greater/smaller" for elements being popped.

When to Use:
    - "Next greater element"
    - "Next smaller element"
    - "Previous greater/smaller"
    - Stock span problems
    - Temperature/histogram problems
    - Any "next/previous X that is greater/smaller"

Time Complexity: O(n) - each element pushed/popped at most once
Space Complexity: O(n)

Key: Stack stores INDICES not values (to calculate distance/position)
"""

def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    REFERENCE: Daily Temperatures (LeetCode #739)

    For each day, find how many days until a warmer temperature.

    Args:
        temperatures: List of daily temperatures

    Returns:
        List where answer[i] is days to wait for warmer temperature,
        or 0 if no warmer day exists

    Time: O(n), Space: O(n)

    Examples:
        >>> daily_temperatures([73,74,75,71,69,72,76,73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> daily_temperatures([30,40,50,60])
        [1, 1, 1, 0]
        >>> daily_temperatures([30,60,90])
        [1, 1, 0]
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Monotonic decreasing stack of indices

    for i in range(n):
        # While current temp breaks monotonicity (warmer than stack top)
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            answer[prev_idx] = i - prev_idx  # Days until warmer

        stack.append(i)  # Always push current index

    # Remaining indices in stack have no warmer day (already 0)
    return answer


if __name__ == "__main__":
    print("=" * 60)
    print("STACK PATTERN: Monotonic Stack")
    print("=" * 60)
    print()
    print("✓ Daily Temperatures reference implementation loaded")
    print()
    print("Monotonic stack finds next greater element efficiently:")
    print("  - Stack maintains decreasing order of temperatures")
    print("  - Store INDICES not values (to calculate distance)")
    print("  - When warmer temp found: pop all colder, record distances")
    print("  - Each element pushed/popped exactly once → O(n)")
    print()
    print("This pattern unlocks 10+ advanced problems!")
    print("=" * 60)
