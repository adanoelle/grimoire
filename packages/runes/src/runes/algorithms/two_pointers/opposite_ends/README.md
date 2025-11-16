# Two Pointers: Opposite Ends

## Pattern Overview

**Core Idea:** Start with pointers at both ends of array/string, move them toward each other based on problem conditions.

**Visual:**
```
[a, b, c, d, e, f, g]
 ↑                 ↑
left            right

↓ Move pointers based on condition ↓

[a, b, c, d, e, f, g]
    ↑           ↑
  left        right
```

## When to Use

✅ **Use this pattern when:**
- Array/string is sorted (or can be sorted)
- Looking for pairs with a property
- Checking palindromes
- Optimizing from O(n²) nested loops

❌ **Don't use when:**
- Need to maintain original order and can't sort
- Looking for subarrays (use sliding window instead)
- Need more than two pointers

## Complexity

- **Time:** O(n) - single pass through array
- **Space:** O(1) - only pointer variables

## The Template

```python
def two_pointer_opposite_ends(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Check condition with arr[left] and arr[right]

        if condition_met:
            return result
        elif need_larger_value:
            left += 1  # Move left pointer right
        else:
            right -= 1  # Move right pointer left

    return default_result
```

## Key Decisions

### Which pointer to move?

**For sum problems:**
- Current sum < target → move `left` (increase sum)
- Current sum > target → move `right` (decrease sum)

**For comparison problems:**
- Move pointer with "worse" value
- Example: Container problem - move pointer with smaller height

**For palindromes:**
- If mismatch → not palindrome
- If match → move both pointers

## Common Variations

### 1. Finding Pairs (Two Sum)
- **Problem:** Find two numbers that sum to target
- **Key:** Array must be sorted
- **Move:** Based on sum comparison

### 2. Palindrome Check
- **Problem:** Check if string reads same forwards/backwards
- **Key:** Compare characters at both ends
- **Move:** Both pointers if match, break if mismatch

### 3. Container Problems
- **Problem:** Maximize area between two lines
- **Key:** Move pointer with smaller value
- **Move:** Greedy - can't improve by moving taller line

### 4. Three Sum
- **Problem:** Find three numbers that sum to target
- **Key:** Fix one number, two pointers for other two
- **Complexity:** O(n²) - outer loop + two pointers

## Interview Tips

### What interviewers want to hear:

**Pattern Recognition:**
> "This is sorted and we're looking for pairs - I'll use two pointers from opposite ends."

**Complexity Explanation:**
> "Two pointers avoid the O(n²) brute force. We make one pass, O(n) time with O(1) space."

**Edge Cases:**
> "I should check: empty array, no solution, and duplicates."

### Common Mistakes to Avoid:

1. **Off-by-one errors**
   - Wrong: `while left <= right` (for pairs)
   - Right: `while left < right`

2. **Moving wrong pointer**
   - Think about what movement improves your situation
   - Example: In two sum, if sum too small, move left (increases sum)

3. **Forgetting to handle no solution**
   - Always return default value ([], -1, etc.)

4. **Not considering duplicates**
   - Some problems need to skip duplicate values
   - Advance pointer while `arr[left] == arr[left+1]`

## LeetCode Problems to Practice

### Easy:
- LC #167: Two Sum II - Input Array Is Sorted ⭐ START HERE
- LC #125: Valid Palindrome
- LC #344: Reverse String

### Medium:
- LC #15: 3Sum
- LC #11: Container With Most Water
- LC #16: 3Sum Closest
- LC #259: 3Sum Smaller
- LC #75: Sort Colors (Dutch National Flag)

### Hard:
- LC #42: Trapping Rain Water
- LC #4: Median of Two Sorted Arrays

## Mastery Goals

- [ ] Can code two sum sorted in < 2 min from memory
- [ ] Can code palindrome check in < 2 min from memory
- [ ] Can explain when to use this pattern in < 30 sec
- [ ] Can identify pattern in new problems instantly
- [ ] Understand why we move each pointer
- [ ] Handle edge cases automatically
- [ ] Used successfully in 5+ LeetCode problems

## Study Notes

*Add your insights here as you practice:*

**What I learned:**
-

**Gotchas I discovered:**
-

**Problems where this pattern appeared:**
-

**When I tend to use this:**
-
