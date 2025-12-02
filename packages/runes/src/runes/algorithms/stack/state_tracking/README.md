# Stack Pattern: State Tracking

## Pattern Overview

```
Two-stack approach to maintain O(1) minimum:

Operation    | Main Stack | Min Stack | Explanation
-------------|------------|-----------|-------------
push(-2)     | [-2]       | [-2]      | First element is min
push(0)      | [-2, 0]    | [-2, -2]  | Min still -2
push(-3)     | [-2,0,-3]  | [-2,-2,-3]| New min: -3
getMin()     | [-2,0,-3]  | [-2,-2,-3]| Return top of min_stack: -3
pop()        | [-2, 0]    | [-2, -2]  | Both stacks pop
getMin()     | [-2, 0]    | [-2, -2]  | Return top of min_stack: -2
```

## When to Use

✅ Use when:
- Need O(1) access to min/max/frequency
- Maintaining invariants alongside stack operations
- "Design a stack that supports..." with constraints
- State depends on current stack depth

❌ Don't use when:
- Don't need the extra invariant (use regular stack)
- Need historical mins (use different data structure)
- O(n) time acceptable (simpler implementation)

## Complexity

- **Time**: O(1) for all operations
- **Space**: O(n) for auxiliary stack

## The Template

```python
class MinStack:
    def __init__(self):
        self.stack = []      # Main stack
        self.min_stack = []  # Tracks min at each depth

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Current min is min(val, previous min)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()      # Remove from main
        self.min_stack.pop()  # Remove from min tracker

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]  # O(1) lookup
```

## Key Decisions

### Why two stacks?
- Auxiliary stack mirrors main stack growth
- Each depth "remembers" its minimum
- Popping automatically reverts to previous min

### Why `min(val, previous_min)`?
- New value might be new minimum
- Or previous minimum still holds
- Store whichever is smaller

### Why pop both stacks together?
- Keeps stacks synchronized
- Min at depth N corresponds to elements at depth N
- Breaking sync breaks getMin()

## Common Mistakes

1. **Forgetting to handle empty min_stack**: Use `if self.min_stack else val`
2. **Only storing mins**: Min stack must mirror ALL pushes, not just new mins
3. **Not popping min_stack**: Both stacks must stay in sync
4. **Wrong comparison**: Need `min(val, prev)` not just `val < prev`

## Interview Tips

- Start with "I'll use two stacks: main and auxiliary"
- Draw the stack evolution diagram
- Emphasize O(1) for all operations
- Mention space trade-off (2x space for O(1) time)
- Variations: MaxStack uses same pattern

## LeetCode Problems

### Easy
- ✓ LC #155: Min Stack

### Medium
- LC #716: Max Stack (similar pattern)
- LC #895: Maximum Frequency Stack

### Hard
- LC #1249: Minimum Remove to Make Valid Parentheses (uses stack tracking)

## Variations

### Max Stack
Replace `min()` with `max()`, same pattern

### Stack with Max Frequency
Track frequency counts in auxiliary structure

### O(1) Space Alternative
Store (value, min) pairs in single stack (trades time for space slightly)

## Mastery Checklist

- [ ] Can code in under 8 minutes
- [ ] Zero bugs on practice runs
- [ ] Understand why both stacks must stay synchronized
- [ ] Can explain O(1) guarantee
- [ ] Know when to use auxiliary data structures
