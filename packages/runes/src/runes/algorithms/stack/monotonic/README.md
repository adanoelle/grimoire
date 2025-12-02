# Stack Pattern: Monotonic Stack

## Pattern Overview

```
Monotonic Decreasing Stack Example: [73, 74, 75, 71, 69, 72, 76, 73]

i=0, temp=73: stack=[] → push 0 → stack=[0]
i=1, temp=74: 74>73, pop 0, answer[0]=1-0=1 → push 1 → stack=[1]
i=2, temp=75: 75>74, pop 1, answer[1]=2-1=1 → push 2 → stack=[2]
i=3, temp=71: 71<75 → push 3 → stack=[2,3]
i=4, temp=69: 69<71 → push 4 → stack=[2,3,4]
i=5, temp=72: 72>69, pop 4, answer[4]=5-4=1
              72>71, pop 3, answer[3]=5-3=2
              72<75 → push 5 → stack=[2,5]
i=6, temp=76: 76>72, pop 5, answer[5]=6-5=1
              76>75, pop 2, answer[2]=6-2=4
              stack=[] → push 6 → stack=[6]
i=7, temp=73: 73<76 → push 7 → stack=[6,7]

Final: answer=[1,1,4,2,1,1,0,0]  (indices 6,7 remain = no warmer day)
```

## When to Use

✅ Use when:
- "Next greater element"
- "Next smaller element"
- "Previous greater/smaller"
- "How many days/elements until..."
- Stock span, temperature, histogram problems
- Need O(n) time for element-wise comparisons

❌ Don't use when:
- Don't need "next/previous" relationships
- Order doesn't matter
- Need all elements comparison (just iterate)

## Complexity

- **Time**: O(n) - each element pushed/popped exactly once
- **Space**: O(n) - worst case stack holds all elements

## The Template

```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Monotonic decreasing stack of INDICES

    for i in range(n):
        # While current breaks monotonicity (warmer than stack top)
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            answer[prev_idx] = i - prev_idx  # Calculate distance

        stack.append(i)  # Always push current index

    return answer  # Remaining stack indices stay 0
```

## Key Decisions

### Why store indices instead of values?
- Need to calculate distance/position
- Index gives both position AND value access
- `answer[prev_idx] = i - prev_idx` needs indices

### Why monotonic decreasing for "next warmer"?
- Decreasing stack = smallest/coolest on top
- When warmer arrives, all cooler days get resolved
- Increasing stack would be for "next cooler"

### Why `while` not `if` for popping?
- Current element might resolve multiple stack elements
- Example: 69,71,73,100 → 100 resolves all three
- Must pop ALL elements that break monotonicity

### Why always append after popping?
- Current element becomes candidate for future elements
- Even if it resolved others, it needs resolution too
- Stack maintains candidates awaiting resolution

## Common Mistakes

1. **Storing values instead of indices**: Need positions for distance
2. **Using `if` instead of `while`**: Miss multiple resolutions
3. **Forgetting to push after popping**: Breaks future resolutions
4. **Wrong inequality**: Use `>` for next greater, `<` for next smaller
5. **Not initializing answer to 0**: Remaining elements need default

## Interview Tips

- Draw the stack evolution (show indices and temps)
- State "monotonic decreasing" or "monotonic increasing" explicitly
- Emphasize O(n) time: "each element pushed/popped once"
- Explain why indices not values
- Mention this pattern solves 10+ LeetCode problems

## LeetCode Problems

### Easy
- LC #496: Next Greater Element I

### Medium
- ✓ LC #739: Daily Temperatures
- LC #503: Next Greater Element II
- LC #556: Next Greater Element III
- LC #901: Online Stock Span
- LC #1019: Next Greater Node in Linked List

### Hard
- LC #84: Largest Rectangle in Histogram (uses monotonic stack)
- LC #85: Maximal Rectangle
- LC #402: Remove K Digits

## Variations

### Next Smaller Element
Use monotonic **increasing** stack, change `>` to `<`

### Previous Greater Element
Iterate right-to-left instead of left-to-right

### Circular Array
Use modulo arithmetic: `for i in range(2 * n)` with `i % n`

### Largest Rectangle in Histogram
Monotonic increasing stack, calculate area when popping

## The Breakthrough Insight

> Monotonic stack transforms O(n²) nested loops into O(n) single pass!

**Naive approach** (O(n²)):
```python
for i in range(n):
    for j in range(i+1, n):
        if temperatures[j] > temperatures[i]:
            answer[i] = j - i
            break
```

**Monotonic stack** (O(n)):
- Each element touched twice (push + pop)
- Stack maintains "unresolved" elements
- Current element resolves all smaller stack elements

## Mastery Checklist

- [ ] Can code in under 12 minutes
- [ ] Zero bugs on practice runs
- [ ] Understand why indices not values
- [ ] Know when to use while vs if
- [ ] Can draw stack evolution diagram
- [ ] Recognize pattern in problem descriptions
- [ ] This pattern unlocks 10+ other problems!

## Next Steps After Mastery

Once you've mastered Daily Temperatures, try:
1. Next Greater Element I (LC #496) - simpler variant
2. Next Greater Element II (LC #503) - circular array
3. Largest Rectangle in Histogram (LC #84) - ultimate challenge
