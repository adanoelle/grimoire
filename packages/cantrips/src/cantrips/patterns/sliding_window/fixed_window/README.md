# Fixed Window Sliding Window

Master the fixed-size sliding window pattern through deliberate practice.

## Pattern Recognition

Use fixed window when:
- Need to process subarrays of exact size K
- Sliding one element at a time
- Can maintain window state incrementally
- O(n) time is required (can't recalculate each window)

## Technique

```python
# Fixed Window Pattern:
# 1. Initialize tracking structure for first window
# 2. Check the first window for result
# 3. Slide left & right:
#    a. add nums[right] or s[right] to tracking structure
#    b. remove nums[left] or s[left] from tracking structure
#    c. check if current window matches solution condition
#    d. move left += 1
# 4. return result

# Iteration bounds:
for idx in range(window_size, len(data)):
    # idx is the RIGHT edge of window
    # idx - window_size is the element leaving
```

## Cantrips

| # | Problem | LeetCode | Target | Difficulty |
|---|---------|----------|--------|------------|
| 1 | Maximum Average Subarray I | #643 | < 2:00 | Easy |
| 2 | Number of Sub-arrays of Size K | #1343 | < 2:30 | Medium |
| 3 | Substrings of Size Three | #1876 | < 2:00 | Easy |
| 4 | Permutation in String | #567 | < 4:00 | Medium |
| 5 | Find All Anagrams | #438 | < 4:30 | Medium |

## Progression

1. **Cantrips 1-2**: Basic sum tracking (numeric windows)
2. **Cantrip 3**: Set-based tracking (character windows)
3. **Cantrips 4-5**: Frequency map tracking (anagram detection)

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
