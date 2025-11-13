# Arrays & Strings

## Overview

Arrays and strings are fundamental data structures. Most interview problems start here
because they test your ability to manipulate data efficiently using indices, iteration,
and clever algorithms.

## Core Concepts

### Concept 1: Two Pointers

**What it is**: Using two indices to traverse an array/string, either from opposite ends
or at different speeds **When to use**: Sorted arrays, palindromes, pairs with target
sum **Time complexity**: O(n)

### Concept 2: Sliding Window

**What it is**: Maintain a window of elements and slide it across the array **When to
use**: Subarray/substring problems, "contiguous" or "consecutive" **Time complexity**:
O(n)

### Concept 3: Prefix Sum

**What it is**: Precompute cumulative sums for fast range queries **When to use**:
Multiple range sum queries, subarray sum problems **Time complexity**: O(n)
preprocessing, O(1) queries

## Common Patterns

### Pattern 1: Two Pointers (Opposite Ends)

**Recognition**: "Reverse", "palindrome", "pair that sums to target" **Approach**: Start
pointers at both ends, move them toward center **Example problems**: Reverse string, Two
Sum II (sorted)

### Pattern 2: Sliding Window (Fixed Size)

**Recognition**: "Window of size k", "every subarray of length k" **Approach**:
Initialize window, slide one element at a time **Example problems**: Maximum average
subarray

### Pattern 3: Sliding Window (Variable Size)

**Recognition**: "Longest/shortest subarray with condition" **Approach**: Expand window
until invalid, then shrink **Example problems**: Longest substring without repeating
characters

## Problems

### Easy Problems

- [ ] **[Two Pointers](link)** - Article
  - Pattern: Introduction to two pointers
  - Key insight: Learn the basic technique
  - Related to: Arrays

- [x] **[Reverse String](link)** - LC #344
  - Pattern: Two pointers (opposite ends)
  - Key insight: Swap elements from both ends
  - Related to: Arrays

- [x] **[Squares of a Sorted Array](link)** - LC #977
  - Pattern: Two pointers
  - Key insight: Compare absolute values, build solution iteratively in reverse
  - Related to: Arrays

- [ ] **[Sliding Window](link)** - Article
  - Pattern: Introduction to sliding window
  - Key insight: Learn the basic technique
  - Related to: Arrays

- [ ] **[More Common Patterns](link)** - Article
  - Pattern: Various
  - Key insight: Pattern recognition
  - Related to: Arrays

### Medium Problems

- [ ] **[Maximum Average Subarray I](link)** - LC #643
  - Pattern: Sliding window (fixed)
  - Key insight: Maintain sum of window
  - Related to: Arrays

- [ ] **[Max Consecutive Ones III](link)** - LC #1004
  - Pattern: Sliding window (variable)
  - Key insight: Track number of zeros
  - Related to: Arrays

- [ ] **[Prefix Sum](link)** - Article
  - Pattern: Prefix sum introduction
  - Key insight: Precomputation for efficiency
  - Related to: Arrays

- [ ] **[Running Sum of 1d Array](link)** - LC #1480
  - Pattern: Prefix sum
  - Key insight: Build cumulative array
  - Related to: Arrays

- [ ] **[Minimum Value to Get Positive Step by Step Sum](link)** - LC #1413
  - Pattern: Prefix sum
  - Key insight: Track minimum prefix
  - Related to: Arrays

### Hard Problems

- [ ] **[K Radius Subarray Averages](link)** - LC #2090
  - Pattern: Sliding window + prefix sum
  - Key insight: Combine techniques
  - Related to: Arrays

- [ ] **[Bonus Problems](link)** - Various
  - Pattern: Mixed
  - Key insight: Practice all patterns
  - Related to: Arrays

## Progress Tracker

**Completed**: 1 / 12

- Easy: 1 / 5
- Medium: 0 / 5
- Hard: 0 / 2

**Time spent**: **Start date**: **Completion date**:

## Key Insights

### What I learned

- Two pointers technique moving from opposite ends is perfect for reversing/palindrome
  problems
- In-place array modifications can achieve O(1) space complexity
- Python's tuple unpacking allows swapping without temporary variables

### Common mistakes I made

- Forgetting proper spacing around operators (PEP 8)
- File naming inconsistencies (plural vs singular)

### Interview tips for this topic

- Always consider if the array is sorted
- Ask about duplicates and edge cases (empty, single element)
- Two pointers is your friend for O(n) solutions
- Think about whether you need to preserve the original array
- Think about whether you should iterate over the input in reverse

## Related Runes

Data structures from `runes` that are useful here:

- This topic uses built-in Python lists/strings

## Problem Connections

-

## Resources

- [Two Pointers Visualizer](https://visualgo.net)
- [Sliding Window Tutorial](https://leetcode.com/explore/)
