# Sliding Window: Fixed Size

## Pattern Overview

**Core Idea:** Maintain a window of exactly K elements. Slide it one position at a time, updating result incrementally without recalculating from scratch.

**Visual:**
```
Array: [2, 1, 5, 1, 3, 2]  k=3

Window 1: [2, 1, 5]  sum=8
           -------

Window 2:    [1, 5, 1]  sum=7  (remove 2, add 1)
              -------

Window 3:       [5, 1, 3]  sum=9  (remove 1, add 3)
                 -------
```

## When to Use

✅ **Use this pattern when:**
- Problem mentions "subarray of size k" or "k consecutive elements"
- Need to process ALL windows of fixed size
- Can maintain window state incrementally (sum, count, frequency)
- Looking for max/min/average of fixed-length subarrays
- Pattern matching within fixed-length windows

❌ **Don't use when:**
- Window size varies (use variable-size sliding window)
- Need non-contiguous elements
- Window doesn't slide smoothly (gaps or jumps)
- Looking for pairs/triplets (use two pointers instead)

## Complexity

- **Time:** O(n) - each element enters window once and exits once
- **Space:** O(1) for numeric windows, O(k) for tracking unique elements
- **Key insight:** Never recalculate entire window! Update incrementally.

## The Template

```python
def sliding_window_fixed(arr, k):
    if k > len(arr):
        return None  # Invalid input

    # 1. Calculate first window
    window_state = calculate_initial_window(arr[:k])
    result = window_state  # or initialize result list

    # 2. Slide the window
    for i in range(k, len(arr)):
        # Remove element leaving window
        update_state_remove(arr[i - k])

        # Add element entering window
        update_state_add(arr[i])

        # Update result
        result = update_result(window_state)

    return result
```

## Key Decisions

### What state to maintain?

**For sum/average problems:**
- Track running sum
- Update: `sum = sum - arr[left] + arr[right]`

**For frequency problems:**
- Use Counter/dict to track character/element counts
- Update: decrement count for leaving element, increment for entering element

**For uniqueness problems:**
- Use set to track distinct elements
- Update: remove from set if count reaches 0, add new element

## Common Variations

### 1. Maximum/Minimum Sum (Most Basic)
- **Problem:** Find max sum of k consecutive elements
- **State:** Running sum
- **Update:** `sum = sum - nums[i-k] + nums[i]`
- **Example:** LC 643 - Max Average Subarray

### 2. Count Windows Meeting Condition
- **Problem:** Count windows where average >= threshold
- **State:** Running sum
- **Check:** `sum >= threshold * k` (avoid division)
- **Example:** LC 1343 - Number of Sub-arrays

### 3. Distinct Elements in Window
- **Problem:** Count windows with all distinct characters
- **State:** Set or frequency map
- **Check:** `len(set) == k` or all counts == 1
- **Example:** LC 1876 - Good Substrings

### 4. Pattern Matching (Advanced)
- **Problem:** Find if pattern permutation exists in window
- **State:** Two frequency maps (pattern + current window)
- **Check:** Maps are equal
- **Example:** LC 567 - Permutation in String

### 5. Multiple Matches
- **Problem:** Find ALL windows matching condition
- **State:** Same as pattern matching
- **Result:** List of start indices
- **Example:** LC 438 - Find All Anagrams

## Interview Tips

### What interviewers want to hear:

1. **"I recognize this is a fixed-size sliding window"**
   - Shows pattern recognition (huge interview skill)

2. **"I'll maintain the window state incrementally"**
   - Shows you understand O(n) vs O(n*k) difference

3. **"First, I'll handle the initial window, then slide"**
   - Shows systematic thinking

4. **"The key insight is we only need to update, not recalculate"**
   - Shows optimization mindset

### Common pitfalls:

❌ Recalculating entire window each iteration (O(n*k) instead of O(n))
❌ Off-by-one errors in loop bounds
❌ Forgetting to handle k > len(arr)
❌ Not initializing first window before sliding

## Progression Path

**Level 1: Basic Sum** (Kata 1-2)
- Maximum average subarray
- Count subarrays meeting threshold
- Focus: Master the slide mechanic

**Level 2: Strings & Uniqueness** (Kata 3)
- Distinct characters in window
- Focus: State management beyond simple sum

**Level 3: Frequency Maps** (Kata 4-5)
- Pattern matching with character frequencies
- Finding multiple matches
- Focus: Counter/dict updates, comparison logic

## Practice Strategy

1. **Master Kata 1 first** - This is THE template
   - Code it 10 times from memory
   - Should be automatic

2. **Kata 2 builds on Kata 1** - Same pattern, add condition
   - Practice transitioning from max to count

3. **Kata 3 introduces state beyond sum** - Set manipulation
   - Understand when to use set vs counter

4. **Kata 4-5 are frequency map masters** - Core interview pattern
   - These appear constantly in real interviews
   - Practice until the Counter pattern is muscle memory

## Related LeetCode Problems

**Easy:**
- [x] 643 - Maximum Average Subarray I (Kata 1)
- [x] 1876 - Substrings of Size Three (Kata 3)
- [ ] 1984 - Minimum Difference in Test Scores
- [ ] 2269 - Find K-Beauty Numbers

**Medium:**
- [x] 1343 - Number of Sub-arrays (Kata 2)
- [x] 567 - Permutation in String (Kata 4)
- [x] 438 - Find All Anagrams (Kata 5)
- [ ] 1456 - Maximum Vowels in Substring
- [ ] 1004 - Max Consecutive Ones III
- [ ] 2841 - Maximum Sum of Subsequence

**Hard:**
- [ ] 239 - Sliding Window Maximum (requires deque)
- [ ] 76 - Minimum Window Substring (variable window)
- [ ] 480 - Sliding Window Median

## Mastery Checklist

**Pattern Recognition (30 seconds)**
- [ ] Can identify fixed window problems immediately
- [ ] Know when NOT to use this pattern

**Implementation (under 15 minutes total)**
- [ ] Kata 1 in < 2 min (core template)
- [ ] Kata 2 in < 2.5 min (add condition)
- [ ] Kata 3 in < 2 min (set operations)
- [ ] Kata 4 in < 4 min (frequency maps)
- [ ] Kata 5 in < 4.5 min (collect all matches)

**Explanation**
- [ ] Can explain why O(n) not O(n*k)
- [ ] Can draw window sliding on whiteboard
- [ ] Can articulate state management choices

**Variants**
- [ ] Know when to use Counter vs set vs int
- [ ] Can adapt template to new problems
- [ ] Can optimize (e.g., compare sums not averages)

## Study Notes

(Add your insights, common mistakes, aha moments here as you practice)

---

**Next:** After mastering fixed-size windows, move to [Variable-Size Sliding Window](../variable_window/README.md)
