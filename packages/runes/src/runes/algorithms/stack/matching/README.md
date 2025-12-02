# Stack Pattern: Matching/Pairing

## Pattern Overview

```
Stack tracks most recent unmatched opening:

Input: "({[]})"
Step 1: '(' → stack: ['(']
Step 2: '{' → stack: ['(', '{']
Step 3: '[' → stack: ['(', '{', '[']
Step 4: ']' → matches '[', pop → stack: ['(', '{']
Step 5: '}' → matches '{', pop → stack: ['(']
Step 6: ')' → matches '(', pop → stack: []
Result: Valid (stack empty)
```

## When to Use

✅ Use when:
- Matching pairs (parentheses, brackets, braces, tags)
- Balanced expressions
- Nested structures with open/close markers
- "Valid" or "balanced" in problem description

❌ Don't use when:
- Need to find all occurrences (use hash map)
- Order doesn't matter (use counter)
- Need middle elements (use deque or array)

## Complexity

- **Time**: O(n) - single pass through string
- **Space**: O(n) - worst case all opening brackets

## The Template

```python
def is_valid(s: str) -> bool:
    stack = []
    close_to_open = {"}": "{", "]": "[", ")": "("}  # Map closing → opening

    for char in s:
        if char in close_to_open:  # Closing bracket
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()  # Match found
            else:
                return False  # No match or empty stack
        else:  # Opening bracket
            stack.append(char)

    return not stack  # Valid only if all matched
```

## Key Decisions

### Why hash map for closing → opening?
- Fast O(1) lookup to identify closing brackets
- Clean way to verify match

### Why check `stack` before `stack[-1]`?
- Prevents IndexError on empty stack
- Closing bracket without opening is invalid

### Why `not stack` at end?
- Leftover opening brackets = invalid
- Empty stack = all brackets matched

## Common Mistakes

1. **Forgetting to check stack non-empty**: `if stack[-1] == ...` crashes
2. **Checking wrong condition**: Need `stack AND stack[-1]`, not `OR`
3. **Returning True early**: Must check entire string
4. **Wrong empty check**: `not stack` not `len(stack) == 0`

## Interview Tips

- Mention hash map for O(1) lookup upfront
- Draw stack evolution for interviewer
- State edge cases: empty string, all opening, all closing
- Time/space: Both O(n)

## LeetCode Problems

### Easy
- ✓ LC #20: Valid Parentheses
- LC #1021: Remove Outermost Parentheses

### Medium
- LC #921: Minimum Add to Make Parentheses Valid
- LC #1249: Minimum Remove to Make Valid Parentheses

### Hard
- LC #32: Longest Valid Parentheses
- LC #301: Remove Invalid Parentheses

## Mastery Checklist

- [ ] Can code in under 5 minutes
- [ ] Zero bugs on practice runs
- [ ] Can explain LIFO matching while coding
- [ ] Recognize pattern in problem descriptions
- [ ] Know all edge cases by heart
