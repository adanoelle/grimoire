# Variable Window Sliding Window

Master the variable-size sliding window pattern through deliberate practice.

## Pattern Recognition

Use variable window when:
- Need longest/shortest subarray meeting condition
- Window size changes based on condition
- Expand until condition violated, then contract
- "At most K" or "at least X" constraints

## Technique

```python
# Variable Window Pattern:
# 1. Expand: Add right element, update state
# 2. Contract: While condition violated, remove left element
# 3. Update result: Track best window seen so far
# 4. Repeat until right reaches end

left = 0
for right in range(len(data)):
    # Add data[right] to window state

    while window_invalid():
        # Remove data[left] from window state
        left += 1

    # Update result (max length, count, etc.)
```

## Cantrips

| # | Problem | LeetCode | Target | Difficulty |
|---|---------|----------|--------|------------|
| 1 | Longest Substring Without Repeating | #3 | < 3:00 | Medium |
| 2 | Minimum Size Subarray Sum | #209 | < 3:30 | Medium |
| 3 | Fruit Into Baskets | #904 | < 4:00 | Medium |
| 4 | K Distinct Characters | #340 | < 4:00 | Medium |
| 5 | Subarray Product Less Than K | #713 | < 4:30 | Medium |

## Progression

1. **Cantrips 1-2**: Core expand-contract mechanics
2. **Cantrip 3**: Frequency map with k=2 constraint
3. **Cantrips 4-5**: Generalized constraints (variable k, products)

## Key Insight

> Expand until invalid, contract until valid

The variable window "breathes" - expanding to explore possibilities, contracting to maintain validity.

## Running Tests

```bash
# All tests
pytest test_cantrips.py

# Specific cantrip
pytest test_cantrips.py -m cantrip1

# Just examples
pytest test_cantrips.py -k examples

# Verbose
pytest test_cantrips.py -v
```
