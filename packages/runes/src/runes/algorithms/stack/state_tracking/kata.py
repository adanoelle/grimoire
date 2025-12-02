"""
🥋 STACK STATE TRACKING - KATA PRACTICE

Master maintaining O(1) invariants with auxiliary data structures.

RULES:
1. Code from memory - NO looking at reference!
2. Set timer for each kata
3. Run tests after coding
4. If bugs: understand why, redo tomorrow
5. If perfect: celebrate, repeat until automatic

PROGRESSION:
- Week 1: Code with reference, understand
- Week 2: Code from memory, small bugs OK
- Week 3: Code perfectly in under target time
- Week 4+: Breathing knowledge - teach someone else

PATTERN RECOGNITION:
Use state tracking when:
- ✓ Need to track min/max/frequency while maintaining stack operations
- ✓ O(1) constraint for queries (can't iterate stack)
- ✓ State depends on current stack depth
- ✓ "Design a stack that supports..." in problem description

TECHNIQUE:
1. Main stack for actual data
2. Auxiliary structure mirrors main stack growth
3. Synchronize both structures on push/pop
4. Query auxiliary structure for O(1) state access
"""

"""
# State Tracking Pattern Core Intuition:

Use auxiliary data structure to track invariants alongside main stack.
Both structures stay synchronized - grow and shrink together.

Example: Min Stack
- Main stack: [5, 2, 3]
- Min stack:  [5, 2, 2]  (min at each depth)
When pop(): both stacks pop
When push(4): main=[5,2,3,4], min=[5,2,2,2]

Key Insight: Auxiliary structure "shadows" main stack to maintain state

Cost: 2x space for O(1) queries (often worth it in interviews!)
"""

# ============================================================================
# RELATED CANTRIPS - Apply this pattern in real LeetCode problems
# ============================================================================

"""
After mastering these katas, practice the pattern in these problems:

EASY (Learn pattern application):
- LC #155: Min Stack → cantrips/stacks_queues/min_stack.py
- LC #232: Implement Queue using Stacks
- LC #225: Implement Stack using Queues

MEDIUM (Pattern combinations):
- LC #716: Max Stack (Premium - practice here!)
- LC #1381: Design a Stack With Increment Operation
- LC #895: Maximum Frequency Stack
- LC #981: Time Based Key-Value Store

HARD (Advanced variations):
- LC #1172: Dinner Plate Stacks
- LC #895 + variations: Multi-constraint tracking

PROGRESSION PATH:
1. Master katas 1-2 (MinStack, MaxStack - mirror problems)
2. Solve Easy cantrips (basic stack implementations)
3. Master katas 3-4 (CustomStack, FreqStack - new constraints)
4. Tackle Medium cantrips (apply multi-state tracking)
5. Challenge yourself with kata 5 (TimeMap) and combining patterns
"""


# ============================================================================
# MASTERY PROGRESSION - When to move to cantrips
# ============================================================================

"""
LEVEL 1 (Learning) - Week 1-2:
[ ] Can code katas 1-2 with reference template open
[ ] Understand auxiliary stack concept
[ ] Time doesn't matter yet

LEVEL 2 (Practicing) - Week 2-3:
[ ] Can code katas 1-2 from memory
[ ] < 5 bugs per week across all katas
[ ] Average time under 2× target time
→ READY FOR: Easy cantrips (LC #155, #232)

LEVEL 3 (Proficient) - Week 3-4:
[ ] Zero bugs on katas 1-2 for a week
[ ] Consistently under target time
[ ] Can explain O(1) invariant maintenance
→ READY FOR: Medium cantrips (LC #1381, #895)

LEVEL 4 (Mastered) - Week 4-6:
[ ] 10+ perfect reps on each kata
[ ] Under 80% of target time
[ ] Can code katas 3-5 from memory
[ ] Used successfully in 5+ cantrips
→ READY FOR: Hard cantrips and complex state tracking

LEVEL 5 (Breathing Knowledge) - Week 6+:
[ ] Pattern recognition is automatic (< 10 sec in new problems)
[ ] Can code all 5 katas in under 30 minutes
[ ] Can teach this pattern to someone else
[ ] Immediately see auxiliary structure opportunities
→ INTERVIEW READY: This pattern is now a superpower

WHEN TO MOVE TO CANTRIPS:
- Reach Level 2 (Practicing) on katas 1-2 → Start Easy cantrips
- Reach Level 3 (Proficient) → Start Medium cantrips
- If you struggle on a cantrip → Return to katas for more reps
"""


class MinStack:
    """
    KATA 1: Min Stack (LeetCode #155)

    ⏱️  Target time: < 5 minutes
    🎯 Goal: All operations O(1), clean design

    Design a stack that supports push, pop, top, and retrieving
    the minimum element in constant time.

    Operations:
    - push(val): Push element onto stack
    - pop(): Remove top element
    - top(): Get top element
    - getMin(): Retrieve minimum element

    All operations must be O(1)!

    Edge cases:
    - Stack with one element (min = that element)
    - Push smaller value (new min)
    - Pop current min (revert to previous min)
    - All same values
    - Duplicate minimums

    Hint if stuck:
    - Use TWO stacks: main + min tracker
    - Min stack mirrors main stack, stores min at each depth
    - When pushing: min = min(val, current_min if min_stack else val)
    - When popping: both stacks pop together
    - getMin() just returns min_stack[-1]

    Examples:
        >>> ms = MinStack()
        >>> ms.push(-2)
        >>> ms.push(0)
        >>> ms.push(-3)
        >>> ms.getMin()
        -3
        >>> ms.pop()
        >>> ms.top()
        0
        >>> ms.getMin()
        -2

    START CODING BELOW (delete 'pass' and write your solution):
    """

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


class MaxStack:
    """
    KATA 2: Max Stack (LeetCode #716 - Premium)

    ⏱️  Target time: < 5 minutes
    🎯 Goal: All operations O(1), parallel to MinStack

    Design a stack that supports push, pop, top, and retrieving
    the maximum element in constant time.

    Operations:
    - push(val): Push element onto stack
    - pop(): Remove top element
    - top(): Get top element
    - getMax(): Retrieve maximum element

    All operations must be O(1)!

    Edge cases:
    - Stack with one element (max = that element)
    - Push larger value (new max)
    - Pop current max (revert to previous max)
    - All same values
    - Duplicate maximums

    Hint if stuck:
    - EXACT same structure as MinStack
    - Use TWO stacks: main + max tracker
    - Max stack stores max at each depth
    - When pushing: max = max(val, current_max if max_stack else val)
    - Direct parallel to kata 1!

    Examples:
        >>> ms = MaxStack()
        >>> ms.push(5)
        >>> ms.push(1)
        >>> ms.push(5)
        >>> ms.top()
        5
        >>> ms.getMax()
        5
        >>> ms.pop()
        >>> ms.getMax()
        5

    START CODING BELOW (delete 'pass' and write your solution):
    """

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMax(self) -> int:
        pass


class CustomStack:
    """
    KATA 3: Design a Stack With Increment Operation (LeetCode #1381)

    ⏱️  Target time: < 6 minutes
    🎯 Goal: O(1) push, pop, increment with lazy evaluation

    Design a stack with a fixed capacity that supports:
    - CustomStack(maxSize): Initialize with max capacity
    - push(x): Push x if stack not full
    - pop(): Pop and return top, or -1 if empty
    - increment(k, val): Add val to bottom k elements

    The trick: increment must be O(1), not O(k)!

    Edge cases:
    - Push when full (ignore)
    - Pop when empty (return -1)
    - Increment more than size (only increment actual elements)
    - Increment 0 elements

    Hint if stuck:
    - Use array/list + top pointer (not Python list operations)
    - Lazy evaluation: Don't apply increment immediately!
    - Auxiliary array to track pending increments at each index
    - When pop: apply increment to that position, propagate down
    - increment(k, val): Only update inc[k-1] += val

    Examples:
        >>> stack = CustomStack(3)
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.push(4)  # Full, ignored
        >>> stack.increment(5, 100)  # Only 3 elements
        >>> stack.increment(2, 100)  # Bottom 2
        >>> stack.pop()
        103
        >>> stack.pop()
        202
        >>> stack.pop()
        201

    START CODING BELOW (delete 'pass' and write your solution):
    """

    def __init__(self, maxSize: int):
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def increment(self, k: int, val: int) -> None:
        pass


class FreqStack:
    """
    KATA 4: Maximum Frequency Stack (LeetCode #895)

    ⏱️  Target time: < 8 minutes
    🎯 Goal: O(1) push and pop with frequency tracking

    Design a stack where pop() removes the most frequent element.
    If tie: remove the one closest to top.

    Operations:
    - push(val): Push val onto stack
    - pop(): Remove and return most frequent element
              (ties broken by most recent)

    Both operations must be O(1)!

    Edge cases:
    - Single element
    - All same frequency
    - Frequency changes after pops

    Hint if stuck:
    - Track THREE things:
      1. freq: {val → frequency}
      2. group: {frequency → stack of vals with that frequency}
      3. max_freq: current maximum frequency
    - push(val): freq[val]++, group[freq[val]].push(val), update max_freq
    - pop(): val = group[max_freq].pop(), freq[val]--, adjust max_freq if needed
    - This is NOT a traditional stack - it's frequency-based!

    Examples:
        >>> fs = FreqStack()
        >>> fs.push(5)
        >>> fs.push(7)
        >>> fs.push(5)
        >>> fs.push(7)
        >>> fs.push(4)
        >>> fs.push(5)
        >>> fs.pop()  # 5 (freq 3)
        5
        >>> fs.pop()  # 7 (freq 2, most recent)
        7
        >>> fs.pop()  # 5 (freq 2, most recent)
        5
        >>> fs.pop()  # 4 (freq 1)
        4

    START CODING BELOW (delete 'pass' and write your solution):
    """

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> int:
        pass


class TimeMap:
    """
    KATA 5: Time Based Key-Value Store (LeetCode #981)

    ⏱️  Target time: < 9 minutes
    🎯 Goal: O(1) set, O(log n) get with binary search

    Design a time-based key-value store that stores multiple
    values for the same key at different timestamps.

    Operations:
    - set(key, value, timestamp): Store value at timestamp
    - get(key, timestamp): Get value at timestamp_prev <= timestamp
                          Return "" if no such value

    Timestamps are strictly increasing for each key.

    Edge cases:
    - get() before any set() for that key
    - get() with exact timestamp match
    - get() with timestamp before all values
    - get() with timestamp after all values

    Hint if stuck:
    - Use hash map: {key → list of (timestamp, value) pairs}
    - set() is O(1): just append (sorted by construction)
    - get() requires binary search for largest timestamp <= given
    - Python bisect_right - 1 can help
    - OR: dict of key → {timestamp → value} if timestamps always exact

    Examples:
        >>> tm = TimeMap()
        >>> tm.set("foo", "bar", 1)
        >>> tm.get("foo", 1)
        "bar"
        >>> tm.get("foo", 3)
        "bar"
        >>> tm.set("foo", "bar2", 4)
        >>> tm.get("foo", 4)
        "bar2"
        >>> tm.get("foo", 5)
        "bar2"

    START CODING BELOW (delete 'pass' and write your solution):
    """

    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


# ============================================================================
# MASTERY TRACKING
# ============================================================================

"""
Track your practice sessions below. Be honest about bugs!

Date       | Kata | Time  | Bugs | Notes
-----------|------|-------|------|---------------------------------------
YYYY-MM-DD | 1    | MM:SS | N    | Description of any issues or insights
YYYY-MM-DD | 2    | MM:SS | N    | ...

MASTERY CHECKLIST:
For each kata, check off when you achieve:
[ ] Code from memory without hints
[ ] Zero bugs on first run
[ ] Under target time
[ ] Can explain O(1) invariant maintenance
[ ] Automatic auxiliary structure recognition
"""


# ============================================================================
# TEST RUNNER
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("STACK STATE TRACKING - KATA PRACTICE")
    print("=" * 60)
    print()
    print("🥋 Run tests with pytest:")
    print()
    print("   pytest test_kata.py                  # Run all tests")
    print("   pytest test_kata.py -m kata1         # Run kata 1 only")
    print("   pytest test_kata.py -m kata2         # Run kata 2 only")
    print("   pytest test_kata.py -v               # Verbose output")
    print()
    print("Or use justfile commands:")
    print()
    print("   just kata::test stack/state_tracking")
    print("   just kata::practice stack/state_tracking")
    print()
    print("🎯 KATA MASTERY TIPS:")
    print("   - Code from memory, no peeking!")
    print("   - Time yourself")
    print("   - Aim for zero bugs")
    print("   - Master auxiliary structure pattern")
    print()
    print("=" * 60)
