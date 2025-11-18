# Sliding Window: Variable Size

## Pattern Overview

**Core Idea:** Window size changes dynamically based on a condition. Expand by adding elements until constraint is violated, then contract by removing elements from the left.

**Visual:**
```
Array: [2, 3, 1, 2, 4, 3]  target_sum=7

Window expands:  [2, 3, 1]  sum=6  (< 7, keep expanding)
                 [2, 3, 1, 2]  sum=8  (>= 7, start contracting)

Window contracts: [3, 1, 2]  sum=6  (< 7, done contracting)
                    [1, 2]  sum=3  (still < 7)

Continue expanding...
                  [1, 2, 4]  sum=7  (>= 7, found valid window!)
```

**Key insight:** Each element enters and exits the window at most once → O(n) time

## When to Use

✅ **Use this pattern when:**
- Problem asks for "longest substring with..."
- Problem asks for "minimum/shortest subarray with..."
- Constraint involves window **contents**, not just size
- "At most K" or "at least X" conditions
- Window size needs to change dynamically

❌ **Don't use when:**
- Window size is fixed (use fixed-size sliding window)
- Need exact subarray length K
- Looking for pairs/triplets (use two pointers)
- Need non-contiguous elements

## Complexity

- **Time:** O(n) - each element enters/exits window once
- **Space:** O(1) to O(k) depending on what we track
- **Critical:** Right pointer moves forward n times, left pointer moves forward at most n times total

## The Template

```python
def variable_window(arr):
    left = 0
    result = 0  # or float('inf') for minimization
    window_state = initialize_state()

    for right in range(len(arr)):
        # EXPAND: Add arr[right] to window
        update_state_add(arr[right])

        # CONTRACT: While constraint violated
        while constraint_violated(window_state):
            update_state_remove(arr[left])
            left += 1

        # UPDATE: Track best window seen
        result = update_result(result, right - left + 1)

    return result
```

## Key Decisions

### When to expand vs contract?

**Always expand:** Right pointer always moves forward
**Contract when:** Constraint is violated
- Too many distinct elements
- Sum/product exceeds limit
- Duplicate character found

### Maximization vs Minimization?

**For longest/maximum:**
```python
result = 0
for right in range(len(arr)):
    # expand
    while invalid:
        # contract
    result = max(result, window_size)  # Update after valid
```

**For shortest/minimum:**
```python
result = float('inf')
for right in range(len(arr)):
    # expand
    while valid:  # ← opposite!
        result = min(result, window_size)  # Update before contract
        # contract
```

### What state to maintain?

**For uniqueness:** Set or frequency dict
**For sum:** Running sum (integer)
**For product:** Running product (integer)
**For distinct count:** Frequency dict, check `len(dict)`

## Common Variations

### 1. Longest Without Duplicates (Foundation)
- **Problem:** Longest substring with no repeating chars
- **State:** Set of characters in window
- **Contract:** When duplicate found, remove from left until unique
- **Example:** LC 3 - Longest Substring No Repeat

### 2. Minimum Meeting Target (Sum)
- **Problem:** Shortest subarray with sum >= target
- **State:** Running sum
- **Contract:** While sum >= target, try to shrink
- **Example:** LC 209 - Minimum Size Subarray Sum

### 3. At Most K Distinct (Frequency Map)
- **Problem:** Longest substring with <= K distinct characters
- **State:** Frequency map
- **Contract:** While distinct > K, remove from left
- **Example:** LC 904 (K=2), LC 340 (variable K)

### 4. Product Constraint (Counting)
- **Problem:** Count subarrays where product < K
- **State:** Running product
- **Insight:** For each right, count = (right - left + 1)
- **Example:** LC 713 - Subarray Product Less Than K

## Interview Tips

### What interviewers want to hear:

1. **"This is a variable-size sliding window"**
   - Distinguishes from fixed-size pattern

2. **"I'll expand until the constraint is violated, then contract"**
   - Shows you understand the two-phase approach

3. **"Both pointers only move forward, so it's O(n)"**
   - Critical complexity insight

4. **"For minimization, I update DURING the contraction"**
   - Shows nuanced understanding

### Common pitfalls:

❌ Confusing with fixed window (wrong pattern entirely)
❌ Updating result at wrong time (before vs after contract)
❌ Not understanding that left pointer also moves O(n) total
❌ Forgetting to handle edge cases (empty, single element)
❌ Using wrong loop condition (while invalid vs while valid)

## Progression Path

**Level 1: Uniqueness with Set** (Kata 1)
- Longest substring without repeating chars
- Focus: Basic expand-contract with set

**Level 2: Sum with Target** (Kata 2)
- Minimum subarray sum >= target
- Focus: Minimization problem, update during contract

**Level 3: K=2 Distinct** (Kata 3)
- Fruit into baskets (at most 2 types)
- Focus: Frequency map, shrink when > 2

**Level 4: Variable K Distinct** (Kata 4)
- Generalize to any K
- Focus: Same pattern, configurable constraint

**Level 5: Product Counting** (Kata 5)
- Count subarrays where product < K
- Focus: Counting all valid windows, not just longest

## Practice Strategy

1. **Master Kata 1 absolutely** - This is the foundation
   - The expand-contract pattern must be muscle memory
   - Practice 20+ times until automatic

2. **Understand the minimization twist** (Kata 2)
   - Notice how update timing changes
   - This trips up many candidates

3. **Frequency maps are everywhere** (Kata 3-4)
   - Most variable window problems use this
   - Practice the "decrement and delete if zero" pattern

4. **Counting problems are tricky** (Kata 5)
   - Understanding `count += right - left + 1` is key
   - This is a common interview twist

## Related LeetCode Problems

**Easy:**
- [x] 3 - Longest Substring Without Repeating (Kata 1)
- [ ] 121 - Best Time to Buy/Sell Stock (one pass)
- [ ] 643 - Maximum Average Subarray (technically fixed, but good practice)

**Medium:**
- [x] 209 - Minimum Size Subarray Sum (Kata 2)
- [x] 904 - Fruit Into Baskets (Kata 3)
- [x] 340 - Longest Substring K Distinct (Kata 4) *Premium*
- [x] 713 - Subarray Product Less Than K (Kata 5)
- [ ] 424 - Longest Repeating Character Replacement
- [ ] 1004 - Max Consecutive Ones III
- [ ] 1208 - Get Equal Substrings Within Budget
- [ ] 1493 - Longest Subarray After Deleting One Element

**Hard:**
- [ ] 76 - Minimum Window Substring (classic!)
- [ ] 239 - Sliding Window Maximum (needs deque)
- [ ] 992 - Subarrays with K Different Integers
- [ ] 1687 - Delivering Boxes

## Pattern Recognition Guide

**See "longest substring with..."** → Variable window (maximize)
**See "minimum/shortest subarray with..."** → Variable window (minimize)
**See "at most K"** → Variable window with frequency map
**See "product/sum < target"** → Variable window with running state

**Contrast with fixed window:**
- Fixed: "subarray of size K"
- Variable: "longest/shortest subarray"

## Mastery Checklist

**Pattern Recognition (30 seconds)**
- [ ] Distinguish variable from fixed window problems
- [ ] Identify maximize vs minimize instantly
- [ ] Know when to use set vs frequency dict

**Implementation (under 18 minutes total)**
- [ ] Kata 1 in < 3 min (foundation)
- [ ] Kata 2 in < 3.5 min (minimization twist)
- [ ] Kata 3 in < 4 min (frequency map K=2)
- [ ] Kata 4 in < 4 min (variable K)
- [ ] Kata 5 in < 4.5 min (counting variant)

**Explanation**
- [ ] Can explain why O(n) not O(n²)
- [ ] Can draw expand-contract on whiteboard
- [ ] Can articulate when to update result
- [ ] Can explain counting formula (Kata 5)

**Variants**
- [ ] Can switch between maximize and minimize
- [ ] Can adapt template to new constraints
- [ ] Can handle "at most" vs "at least" vs "exactly"

## Study Notes

(Add your insights, aha moments, common mistakes here as you practice)

---

**Next:** After mastering variable windows, you have solid sliding window skills! Move on to more advanced patterns or revisit [Fixed-Size Sliding Window](../fixed_window/README.md) for review.
