"""
CANTRIP 5: Largest Rectangle in Histogram (LeetCode #84)

Target: < 14:00 | Difficulty: Hard

Given histogram heights, find the area of the largest rectangle.

For each bar, find left and right boundaries where all bars
are >= current bar height. Use monotonic INCREASING stack.

When a shorter bar arrives:
- Shorter bar is right boundary
- Stack top (after pop) is left boundary
- Width = right - left - 1
- Area = height * width

Pattern: Monotonic increasing stack
- When heights[i] < heights[stack[-1]]: time to process
- Pop idx, height = heights[idx]
- Right boundary = i (current shorter bar)
- Left boundary = stack[-1] after pop (or -1 if empty)
- After main loop: process remaining stack (right boundary = len)

Examples:
    >>> heights = [2, 1, 5, 6, 2, 3]
    >>> largest_rectangle_area(heights)
    10

    >>> heights = [2, 4]
    >>> largest_rectangle_area(heights)
    4

    >>> heights = [2, 1, 2]
    >>> largest_rectangle_area(heights)
    3

Edge cases:
    - Single bar: area = heights[0] * 1
    - Strictly increasing: process all at end
    - Strictly decreasing: each bar pops previous
    - All same height: max_area = height * len(heights)
"""


def largest_rectangle_area(heights: list[int]) -> int:
    """Find largest rectangle area in histogram.

    Args:
        heights: List of bar heights.

    Returns:
        Maximum rectangle area.

    Time: O(n) - each element pushed/popped once
    Space: O(n) - stack size
    """
    pass
