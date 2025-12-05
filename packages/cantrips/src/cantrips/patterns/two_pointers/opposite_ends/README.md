# Opposite Ends Two Pointers

Master the opposite-ends two pointer pattern through deliberate practice.

## Pattern Recognition

Use opposite ends when:
- Working with sorted arrays
- Searching for pairs that meet a condition
- In-place array manipulation
- Comparing from both ends

## Technique

```python
# Opposite Ends Pattern:
left, right = 0, len(arr) - 1

while left < right:
    # Check condition at current pointers
    if condition_met():
        # Found answer or update result
        pass
    elif need_larger_value:
        left += 1
    else:
        right -= 1
```

## Cantrips

| # | Problem | LeetCode | Target | Difficulty |
|---|---------|----------|--------|------------|
| 1 | Two Sum II (Sorted) | #167 | < 2:00 | Medium |
| 2 | Valid Palindrome | #125 | < 2:00 | Easy |
| 3 | Reverse String | #344 | < 1:30 | Easy |
| 4 | 3Sum | #15 | < 4:00 | Medium |
| 5 | Container With Most Water | #11 | < 3:00 | Medium |

## Progression

1. **Cantrips 1-3**: Core opposite-ends mechanics
2. **Cantrip 4**: Nested two pointers with deduplication
3. **Cantrip 5**: Greedy selection with two pointers

## Running Tests

```bash
pytest test_cantrips.py
pytest test_cantrips.py -m cantrip1
pytest test_cantrips.py -k examples
```
