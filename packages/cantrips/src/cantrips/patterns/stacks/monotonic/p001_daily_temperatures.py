"""
CANTRIP 1: Daily Temperatures (LeetCode #739)

Target: < 8:00 | Difficulty: Medium

Given daily temperatures, return array where answer[i]
is the number of days until a warmer temperature.
If no warmer day exists, answer[i] = 0.

Pattern: Monotonic decreasing stack
- Stack stores INDICES with decreasing temperatures
- When warmer temp found: pop all colder indices, calculate days
- Calculate days: current_index - popped_index
- Each element pushed/popped exactly once -> O(n)

Examples:
    >>> temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    >>> daily_temperatures(temperatures)
    [1, 1, 4, 2, 1, 1, 0, 0]

    >>> temperatures = [30, 40, 50, 60]
    >>> daily_temperatures(temperatures)
    [1, 1, 1, 0]

    >>> temperatures = [30, 60, 90]
    >>> daily_temperatures(temperatures)
    [1, 1, 0]

Edge cases:
    - Last day always 0 (no future days)
    - Strictly decreasing temps: all 0s
    - Strictly increasing temps: all 1s
    - Equal temperatures: wait for strictly warmer
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Find days until warmer temperature for each day.

    Args:
        temperatures: List of daily temperatures.

    Returns:
        List where answer[i] is days until warmer temp.

    Time: O(n) - each element pushed/popped once
    Space: O(n) - stack size
    """
    pass
