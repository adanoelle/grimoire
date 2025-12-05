# Two Pointers

[LeetCode Article](https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4501/)

## Overview

This is a very common technique used in array problems, allowing us to solve problems
that would otherise be O(N^2) time in O(N) time. Using two index pointers, often called
left and right, we can compare two separate indices in the array at each point as we
iterate of the array. Consider the following example:

```
# Array of chars, which we want to reverse
[l, i, v, e, d]
```

If we wanted to reverse this string in O(N) time and O(N) space, let's see how two
pointers could allow us to do that. Start with left and right pointers at the beginning
and ending of the string respectively:

```
[l, i, v, e, d]
 *           *
```

We want the string on the right to be the in the position at the left pointer, so we can
swap them, then move the left pointer up one and the right pointer down one:

```
[d, i, v, e, l]
    *     *
```

then swap, increment left up and right down:

```
[d, e, v, i, l]
       *
```

Now, when the pointers have met, we know that we have flipped all of the characters we
need to, and we can break from the loop. Here is the solution in Python:

```python
word = [l, i, v, e, d]

left = 0
right = len(word) -1
while left < right:
    tmp = word[left]
    word[left] = word[right]
    word[right] = tmp
```
