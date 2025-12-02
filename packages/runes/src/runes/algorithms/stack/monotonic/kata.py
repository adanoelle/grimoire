"""
🥋 MONOTONIC STACK - KATA PRACTICE

Master the breakthrough pattern that solves "next greater/smaller" problems.

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
Use monotonic stack when:
- ✓ "Next greater element" or "next smaller element"
- ✓ "Previous greater/smaller"
- ✓ Need O(n) time for array problems that seem like O(n²)
- ✓ Finding spans, ranges, or distances to next/prev element
- ✓ Problems about histograms, temperatures, stock prices

TECHNIQUE:
1. Stack stores INDICES (not values!) to calculate distances
2. Maintain monotonic property (increasing or decreasing)
3. When element breaks monotonicity: found answer for stack elements!
4. Pop violators, process them, push current index
5. Each element pushed and popped exactly once → O(n)

THIS IS THE PATTERN THAT CHANGES EVERYTHING!
"""

"""
# Monotonic Stack Pattern Core Intuition:

Maintain stack in sorted order (increasing or decreasing).
When new element breaks the order, you've found the "next greater/smaller"!

Example: Daily Temperatures [73, 74, 75, 71, 69, 72, 76, 73]
Want: Days until warmer temp

Use monotonic DECREASING stack (indices with decreasing temps):

i=0, temp=73 → stack:[] → push 0 → stack:[0]
i=1, temp=74 → 74 > temps[0]=73 → FOUND ANSWER for day 0!
             → answer[0] = 1-0 = 1, pop 0
             → push 1 → stack:[1]
i=2, temp=75 → 75 > temps[1]=74 → answer[1] = 2-1 = 1, pop 1
             → push 2 → stack:[2]
i=3, temp=71 → 71 < 75, maintains decreasing → push 3 → stack:[2,3]
i=4, temp=69 → push 4 → stack:[2,3,4]
i=5, temp=72 → 72 > temps[4]=69 → answer[4]=5-4=1, pop 4
             → 72 > temps[3]=71 → answer[3]=5-3=2, pop 3
             → 72 < temps[2]=75 → stop
             → push 5 → stack:[2,5]
i=6, temp=76 → 76 > all remaining → answer them all!
             → push 6 → stack:[6]
i=7, temp=73 → push 7 → stack:[6,7]

Result: [1, 1, 4, 2, 1, 1, 0, 0]

Key Insight: Stack "remembers" indices waiting for next greater element
When found: calculate distance, pop, continue
Amortized O(n): each index pushed once, popped once
"""

# ============================================================================
# RELATED CANTRIPS - Apply this pattern in real LeetCode problems
# ============================================================================

"""
After mastering these katas, practice the pattern in these problems:

EASY/MEDIUM (Learn pattern application):
- LC #496: Next Greater Element I
- LC #503: Next Greater Element II (circular)
- LC #739: Daily Temperatures → cantrips/stacks_queues/daily_temperatures.py
- LC #901: Online Stock Span

HARD (Advanced variations):
- LC #84: Largest Rectangle in Histogram (BREAKTHROUGH!)
- LC #85: Maximal Rectangle (2D histogram)
- LC #42: Trapping Rain Water
- LC #907: Sum of Subarray Minimums

PROGRESSION PATH:
1. Master katas 1-2 (daily_temperatures, next_greater_i - core pattern)
2. Solve Easy/Medium cantrips (build recognition)
3. Master kata 3 (next_greater_ii - circular array variation)
4. Master kata 4 (stock_span - running/streaming data)
5. Challenge yourself with kata 5 (largest_rectangle - HARD capstone)
   Once you master this, 10+ other problems become trivial!
"""


# ============================================================================
# MASTERY PROGRESSION - When to move to cantrips
# ============================================================================

"""
LEVEL 1 (Learning) - Week 1-2:
[ ] Can code katas 1-2 with reference template open
[ ] Understand why indices, not values
[ ] Understand monotonic property
[ ] Time doesn't matter yet

LEVEL 2 (Practicing) - Week 2-3:
[ ] Can code katas 1-2 from memory
[ ] < 5 bugs per week across all katas
[ ] Average time under 2× target time
→ READY FOR: Easy/Medium cantrips (LC #496, #503, #739)

LEVEL 3 (Proficient) - Week 3-4:
[ ] Zero bugs on katas 1-2 for a week
[ ] Consistently under target time
[ ] Can explain O(n) amortized complexity
→ READY FOR: More cantrips, kata 4 (stock_span)

LEVEL 4 (Mastered) - Week 4-8:
[ ] 10+ perfect reps on katas 1-4
[ ] Under 80% of target time
[ ] Can code kata 5 (largest_rectangle) with minimal bugs
[ ] Pattern recognition is automatic
→ READY FOR: Hard cantrips (LC #84, #85, #42, #907)

LEVEL 5 (Breathing Knowledge) - Week 8+:
[ ] Can code all 5 katas in under 40 minutes
[ ] Largest rectangle feels routine
[ ] Can teach monotonic stack to someone else
[ ] See the pattern in seconds when reading problem
[ ] This pattern unlocked 15+ problems for you
→ INTERVIEW READY: This is your secret weapon

WHEN TO MOVE TO CANTRIPS:
- Reach Level 2 (Practicing) on katas 1-2 → Start Easy cantrips
- Reach Level 3 (Proficient) → Tackle Medium cantrips and kata 4
- Reach Level 4 (Mastered) → Challenge kata 5 and Hard cantrips
- If you struggle on kata 5 → That's normal! It's a Hard problem. Practice katas 1-4 more.
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    KATA 1: Daily Temperatures (LeetCode #739)

    ⏱️  Target time: < 8 minutes
    🎯 Goal: O(n) time with monotonic stack, zero bugs

    Given daily temperatures, return array where answer[i]
    is the number of days until a warmer temperature.
    If no warmer day exists, answer[i] = 0.

    KEY INSIGHT: Monotonic decreasing stack (indices with decreasing temps)
    - Stack stores INDICES with decreasing temperatures
    - When warmer temp found: pop all colder indices, calculate days
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
    - While loop: temperatures[i] > temperatures[stack[-1]]
    - Pop, calculate days, store in answer
    - Always append current index to stack after while loop

    Examples:
        >>> daily_temperatures([73,74,75,71,69,72,76,73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> daily_temperatures([30,40,50,60])
        [1, 1, 1, 0]
        >>> daily_temperatures([30,60,90])
        [1, 1, 0]

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    KATA 2: Next Greater Element I (LeetCode #496)

    ⏱️  Target time: < 6 minutes
    🎯 Goal: O(m + n) time, monotonic stack + hash map

    nums1 is a subset of nums2. For each element in nums1,
    find the next greater element in nums2.
    Return -1 if no greater element exists.

    nums2 has no duplicates.

    Edge cases:
    - Element is last in nums2 → -1
    - Element is largest in nums2 → -1
    - All elements decreasing → all -1

    Hint if stuck:
    - Process nums2 with monotonic stack to build {num → next_greater}
    - Monotonic DECREASING stack (looking for next greater)
    - When nums2[i] > stack top: found next greater, store in map
    - Then lookup nums1 elements in map
    - Two-pass: build map from nums2, query for nums1

    Examples:
        >>> next_greater_element([4,1,2], [1,3,4,2])
        [-1, 3, -1]  # 4→-1, 1→3, 2→-1
        >>> next_greater_element([2,4], [1,2,3,4])
        [3, -1]  # 2→3, 4→-1

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


def next_greater_elements(nums: list[int]) -> list[int]:
    """
    KATA 3: Next Greater Element II (LeetCode #503)

    ⏱️  Target time: < 7 minutes
    🎯 Goal: O(n) time, handle circular array

    Given a circular array, return next greater element for each element.
    The next greater of nums[i] might be before i (wrapping around).
    Return -1 if no greater element exists.

    Circular: nums = [1,2,1] → [2,-1,2] (last 1 wraps to find 2)

    Edge cases:
    - All elements same → all -1
    - Max element → -1
    - Strictly increasing → wrap around

    Hint if stuck:
    - Circular = iterate TWICE (2*n iterations)
    - Use index % n to access actual element
    - Monotonic decreasing stack (indices)
    - Only fill answer array once per index
    - Second pass finds next greater by wrapping

    Pattern:
    for i in range(2 * n):
        actual_idx = i % n
        actual_val = nums[actual_idx]
        # Monotonic stack logic
        # Only set answer[idx] if not set yet

    Examples:
        >>> next_greater_elements([1,2,1])
        [2, -1, 2]
        >>> next_greater_elements([1,2,3,4,3])
        [2, 3, 4, -1, 4]

    START CODING BELOW (delete 'pass' and write your solution):
    """
    pass


class StockSpanner:
    """
    KATA 4: Online Stock Span (LeetCode #901)

    ⏱️  Target time: < 8 minutes
    🎯 Goal: O(1) amortized per next(), monotonic stack

    Design an algorithm that calculates the span of stock prices.
    The span on day i is the maximum number of consecutive days
    (including today) with price <= prices[i].

    Operations:
    - StockSpanner(): Initialize
    - next(price): Return span for current day

    Each price comes one at a time (streaming data).

    Edge cases:
    - First price → span = 1
    - Prices always increasing → span always 1
    - Prices always decreasing → span = day_count
    - Price equal to previous → include in span

    Hint if stuck:
    - Monotonic DECREASING stack: stores (price, span) pairs
    - When new price >= stack top price:
      → Pop, accumulate span
    - Stack stores indices OR (price, span) tuples
    - Accumulate spans while popping
    - Push (current_price, accumulated_span)

    Pattern:
    span = 1  # At least today
    while stack and price >= stack[-1][0]:
        span += stack.pop()[1]  # Add span of smaller/equal prices
    stack.append((price, span))
    return span

    Examples:
        >>> ss = StockSpanner()
        >>> ss.next(100)
        1  # [100], span=1
        >>> ss.next(80)
        1  # [100,80], span=1
        >>> ss.next(60)
        1  # [100,80,60], span=1
        >>> ss.next(70)
        2  # [100,80,70], span=2 (70,60)
        >>> ss.next(60)
        1  # span=1
        >>> ss.next(75)
        4  # span=4 (75,60,70,60)
        >>> ss.next(85)
        6  # span=6 (85,75,60,70,60,80)

    START CODING BELOW (delete 'pass' and write your solution):
    """

    def __init__(self):
        pass

    def next(self, price: int) -> int:
        pass


def largest_rectangle_area(heights: list[int]) -> int:
    """
    KATA 5: Largest Rectangle in Histogram (LeetCode #84) [HARD]

    ⏱️  Target time: < 14 minutes
    🎯 Goal: O(n) time, monotonic increasing stack

    Given histogram heights, find the area of the largest rectangle.

    KEY INSIGHT: For each bar, find left and right boundaries
    where all bars are >= current bar height.
    Use monotonic INCREASING stack.

    When do we process a bar? When a shorter bar arrives!
    → Shorter bar is right boundary
    → Stack top (after pop) is left boundary
    → Width = right - left - 1
    → Area = height * width

    Edge cases:
    - Single bar: area = heights[0] * 1
    - Strictly increasing: process all at end
    - Strictly decreasing: each bar pops previous
    - All same height: max_area = height * len(heights)

    Hint if stuck:
    - Monotonic INCREASING stack (indices)
    - When heights[i] < heights[stack[-1]]: time to process!
    - Pop idx, height = heights[idx]
    - Right boundary = i (current shorter bar)
    - Left boundary = stack[-1] after pop (or -1 if stack empty)
    - Width = i - stack[-1] - 1 (or i if stack empty)
    - Area = height * width
    - After main loop: process remaining stack (right boundary = len)
    - Add sentinel: append 0 to heights to force processing all bars

    Tricky parts:
    1. Stack stores indices (need to calculate widths)
    2. Width calculation: depends on what remains in stack
    3. Need to process remaining stack at end
    4. Appending 0 to heights simplifies code

    Examples:
        >>> largest_rectangle_area([2,1,5,6,2,3])
        10  # Rectangle: height=5, width=2 (bars at idx 2,3)
        >>> largest_rectangle_area([2,4])
        4  # Rectangle: height=4, width=1
        >>> largest_rectangle_area([2,1,2])
        3  # Rectangle: height=1, width=3 (all bars)

    START CODING BELOW (delete 'pass' and write your solution):
    """
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
[ ] Can explain why indices, not values
[ ] Can explain O(n) amortized complexity
[ ] Automatic monotonic stack recognition
[ ] Can identify increasing vs decreasing stack needed

MASTERY GOAL: This pattern unlocks 15+ other problems!
Once mastered: Maximal Rectangle, Trapping Rain Water, Sum of Subarray Minimums, etc.
"""


# ============================================================================
# TEST RUNNER
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("MONOTONIC STACK - KATA PRACTICE")
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
    print("   just kata::test stack/monotonic")
    print("   just kata::practice stack/monotonic")
    print()
    print("🎯 KATA MASTERY TIPS:")
    print("   - Code from memory, no peeking!")
    print("   - Time yourself")
    print("   - THIS IS THE BREAKTHROUGH PATTERN!")
    print("   - Master this, unlock 15+ problems")
    print("   - Indices not values - always remember why")
    print()
    print("=" * 60)
