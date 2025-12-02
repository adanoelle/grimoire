"""
🥋 MONOTONIC STACK - KATA PRACTICE

Master the breakthrough pattern that solves "next greater" problems.

RULES:
1. Code from memory - NO looking at reference!
2. Set timer for each kata
3. Run tests after coding
4. If bugs: understand why, redo tomorrow
5. If perfect: celebrate, repeat until automatic

TARGET: < 12 minutes, zero bugs, O(n) time
THIS IS THE PATTERN THAT CHANGES EVERYTHING!
"""

def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    KATA 4: Daily Temperatures (LeetCode #739)

    ⏱️  Target time: < 12 minutes
    🎯 Goal: O(n) time with monotonic stack, zero bugs

    Given daily temperatures, return array where answer[i]
    is the number of days until a warmer temperature.
    If no warmer day exists, answer[i] = 0.

    KEY INSIGHT: Monotonic decreasing stack
    - Stack stores INDICES with decreasing temperatures
    - When warmer temp found: pop all colder indices
    - Calculate days: current_index - popped_index
    - Each element pushed/popped exactly once → O(n)

    Edge cases:
    - Last day always 0 (no future days)
    - Strictly decreasing temps: all 0s
    - Strictly increasing temps: all 1s
    - Equal temperatures: wait for strictly warmer

    Hint if stuck:
    - Initialize answer = [0] * n
    - Stack holds INDICES not temperatures!
    - Check temperatures[stack[-1]] to compare temps
    - Pop when current temp > stack top temp
    - Always append current index to stack

    Examples:
        >>> daily_temperatures([73,74,75,71,69,72,76,73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> daily_temperatures([30,40,50,60])
        [1, 1, 1, 0]
        >>> daily_temperatures([30,60,90])
        [1, 1, 0]

    START CODING BELOW:
    """
    pass


# MASTERY TRACKING
"""
Track your practice sessions. Be honest about bugs!

Date       | Time  | Bugs | Notes
-----------|-------|------|-------
YYYY-MM-DD | MM:SS | N    |

MASTERY GOAL: This pattern unlocks 10+ other problems!
Once mastered: Next Greater Element, Largest Rectangle, Car Fleet, etc.
"""

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
