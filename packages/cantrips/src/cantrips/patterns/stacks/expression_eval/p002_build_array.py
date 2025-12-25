"""
CANTRIP 2: Build an Array With Stack Operations (LeetCode #1441)

Target: < 4:00 | Difficulty: Easy

Given target array and integer n, return list of "Push" and "Pop"
operations to build target from [1, 2, 3, ..., n].

You have an empty stack and a stream of integers [1, 2, ..., n].
Operations:
- "Push": Take next integer from stream, push to stack
- "Pop": Remove top element

Target contains distinct integers in ascending order from 1 to n.

Pattern: Simulate stack operations
- Iterate stream 1 to target[-1]
- If current number in target: "Push"
- If not in target: "Push" then "Pop" (skip it)
- Use target as a set for O(1) lookup
- Stop at target[-1] (max value)

Examples:
    >>> target, n = [1, 3], 3
    >>> build_array(target, n)
    ['Push', 'Push', 'Pop', 'Push']

    >>> target, n = [1, 2, 3], 3
    >>> build_array(target, n)
    ['Push', 'Push', 'Push']

    >>> target, n = [1, 2], 4
    >>> build_array(target, n)
    ['Push', 'Push']

Edge cases:
    - Target = [1, 2, 3] -> just push push push
    - Target = [1, 3] -> push, push, pop, push (skip 2)
    - Target = [2, 3, 4] -> push, pop, push, push, push (skip 1)
"""


def build_array(target: list[int], n: int) -> list[str]:
    """Build target array using Push and Pop operations.

    Args:
        target: Target array to build (distinct, ascending).
        n: Maximum value in stream [1..n].

    Returns:
        List of "Push" and "Pop" operations.

    Time: O(target[-1]) - iterate up to max target value
    Space: O(target[-1]) - output list
    """
    pass
