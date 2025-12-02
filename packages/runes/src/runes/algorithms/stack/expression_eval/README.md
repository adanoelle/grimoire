# Stack Pattern: Expression Evaluation

## Pattern Overview

```
RPN evaluation example: ["2", "1", "+", "3", "*"]

Step 1: "2" → stack: [2]           (push number)
Step 2: "1" → stack: [2, 1]        (push number)
Step 3: "+" → pop 1,2 → 2+1=3 → stack: [3]  (operator: compute and push)
Step 4: "3" → stack: [3, 3]        (push number)
Step 5: "*" → pop 3,3 → 3*3=9 → stack: [9]  (operator: compute and push)
Result: 9
```

## When to Use

✅ Use when:
- Reverse Polish Notation (postfix expressions)
- Calculator problems without parentheses
- Expression evaluation without operator precedence issues
- Compiler/interpreter design (intermediate representation)

❌ Don't use when:
- Infix notation with parentheses (use different algorithm)
- Need to preserve expression structure (use AST)
- Human-readable output required (RPN is not intuitive)

## Complexity

- **Time**: O(n) - single pass through tokens
- **Space**: O(n) - worst case all numbers before operators

## The Template

```python
def eval_rpn(tokens: list[str]) -> int:
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            # Pop two operands (ORDER MATTERS!)
            b = stack.pop()  # Second operand
            a = stack.pop()  # First operand

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)  # a - b, not b - a
            elif token == '*':
                stack.append(a * b)
            else:  # '/'
                stack.append(int(a / b))  # Truncate toward zero
        else:
            stack.append(int(token))  # It's a number

    return stack[0]  # Final result
```

## Key Decisions

### Why pop in reverse order?
- Stack: [a, b] (a pushed first)
- Pop: b first, then a
- For a - b, need to pop b=pop(), a=pop()

### Why `int(a / b)` instead of `a // b`?
- `//` is floor division (rounds toward -∞)
- `int(/)` truncates toward zero
- Different for negative numbers!
  - `int(-3 / 2)` = -1 ✓
  - `-3 // 2` = -2 ✗

### Why check operators with set?
- O(1) lookup
- Clear separation: operators vs operands
- Easy to extend with more operators

## Common Mistakes

1. **Wrong operand order**: `a = pop(), b = pop()` then `a - b` is wrong!
2. **Using `//` instead of `int(/)`**: Wrong for negative division
3. **Forgetting to convert tokens**: `int(token)` needed
4. **Not handling single number**: Edge case, should return that number
5. **Returning wrong stack element**: Return `stack[0]` not `stack[-1]`

## Interview Tips

- Mention "operand stack" upfront
- Emphasize order matters for - and /
- Explain truncate vs floor division
- State "each element processed once" (O(n))
- RPN avoids parentheses and precedence issues

## LeetCode Problems

### Easy
- ✓ LC #150: Evaluate Reverse Polish Notation

### Medium
- LC #224: Basic Calculator
- LC #227: Basic Calculator II
- LC #772: Basic Calculator III

### Hard
- LC #770: Basic Calculator IV
- LC #282: Expression Add Operators

## Variations

### Infix to Postfix Conversion
Use two stacks: operators and output (Shunting Yard algorithm)

### Calculator with Parentheses
Handle operator precedence and parentheses

### Multiple Data Types
Extend to handle floats, strings, etc.

## Mastery Checklist

- [ ] Can code in under 7 minutes
- [ ] Zero bugs on practice runs
- [ ] Remember operand order for - and /
- [ ] Know int(/) vs // difference
- [ ] Recognize RPN in problem descriptions
