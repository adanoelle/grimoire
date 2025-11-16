# Kata-Cantrip Correlation Guide

> Connecting daily kata practice with LeetCode problem-solving

This document tracks which kata patterns you've practiced in actual LeetCode problems
(cantrips) and recommends specific problems to reinforce each pattern.

## Current Progress

### Patterns Practiced in Cantrips ✅

**Two Pointers - Opposite Ends** (2 problems)

- ✅ Reverse String (#344)
- ✅ Squares of Sorted Array (#977)

**Sliding Window - Fixed** (1 problem)

- ✅ Maximum Average Subarray I (#643)

**Sliding Window - Variable** (1 problem)

- ✅ Longest Subarray with Sum ≤ K

### Patterns NOT Yet Used ❌

**Two Pointers - Fast/Slow** (0 problems)

- ❌ Not yet practiced in any cantrip

**Binary Search** (0 problems)

- ❌ Not yet practiced in any cantrip

---

## Recommended Next Problems

### Priority 1: Fill Pattern Gaps

These problems will let you apply the kata patterns you haven't used yet:

#### Binary Search - CRITICAL (Practice 100 times!)

**Easy - Start Here:**

1. **Binary Search** (#704) - MUST DO
   - Classic binary search on sorted array
   - **Kata correlation**: `searching/binary_search/kata.py` - Kata 1
   - Target: Code in < 2 min, zero bugs
   - This is THE most important algorithm to master

2. **Search Insert Position** (#35)
   - Find target or insertion position
   - **Kata correlation**: `searching/binary_search/kata.py` - Kata 2
   - Pattern: First occurrence variant

3. **First Bad Version** (#278)
   - API-based binary search
   - **Kata correlation**: `searching/binary_search/kata.py` - Kata 3
   - Pattern: Find first occurrence

**Medium - After Mastering Easy:** 4. **Find First and Last Position** (#34)

- Find range of target in sorted array
- **Kata correlation**: `searching/binary_search/kata.py` - Kata 2 & 3
- Pattern: Combine first and last occurrence

5. **Search in Rotated Sorted Array** (#33)
   - Modified binary search
   - **Kata correlation**: `searching/binary_search/kata.py` - Kata 4
   - Pattern: Binary search with condition modification

#### Two Pointers - Fast/Slow (Cycle Detection)

**Easy:**

1. **Linked List Cycle** (#141) - MUST DO
   - Detect cycle in linked list
   - **Kata correlation**: `two_pointers/fast_slow/kata.py` - Kata 1
   - Classic fast/slow pointer application

2. **Happy Number** (#202)
   - Cycle detection in number sequence
   - **Kata correlation**: `two_pointers/fast_slow/kata.py` - Kata 2
   - Pattern: Fast/slow in non-array context

**Medium:** 3. **Linked List Cycle II** (#142)

- Find where cycle begins
- **Kata correlation**: `two_pointers/fast_slow/kata.py` - Kata 3
- Pattern: Advanced fast/slow with calculation

4. **Find the Duplicate Number** (#287)
   - Array as linked list
   - **Kata correlation**: `two_pointers/fast_slow/kata.py` - Kata 4
   - Pattern: Floyd's algorithm application

### Priority 2: Deepen Existing Patterns

These problems reinforce patterns you've already used:

#### Two Pointers - Opposite Ends (More Practice)

**Easy:**

1. **Valid Palindrome** (#125)
   - Check if string is palindrome
   - **Kata correlation**: `two_pointers/opposite_ends/kata.py` - Kata 2
   - Similar to Reverse String but with comparison

2. **Two Sum II - Input Array is Sorted** (#167)
   - Find pair summing to target
   - **Kata correlation**: `two_pointers/opposite_ends/kata.py` - Kata 1
   - Classic two-pointer on sorted array

**Medium:** 3. **Container With Most Water** (#11)

- Find maximum area between two lines
- **Kata correlation**: `two_pointers/opposite_ends/kata.py` - Kata 3
- Greedy two-pointer approach

4. **3Sum** (#15)
   - Find all triplets summing to zero
   - **Kata correlation**: `two_pointers/opposite_ends/kata.py` - Kata 1 + sorting
   - Pattern: Two pointers inside loop

#### Sliding Window - Fixed (More Practice)

**Easy:**

1. **Contains Duplicate II** (#219)
   - Find duplicate within k distance
   - **Kata correlation**: `sliding_window/fixed_window/kata.py` - Kata 3
   - Fixed window with hash set

2. **Maximum Sum of Distinct Subarrays With Length K** (#2461)
   - Fixed window with uniqueness constraint
   - **Kata correlation**: `sliding_window/fixed_window/kata.py` - Kata 1 + set
   - Pattern: Fixed window + additional tracking

#### Sliding Window - Variable (More Practice)

**Medium:**

1. **Longest Substring Without Repeating Characters** (#3)
   - Find longest unique character substring
   - **Kata correlation**: `sliding_window/variable_window/kata.py` - Kata 1
   - Classic variable window problem

2. **Minimum Size Subarray Sum** (#209)
   - Smallest subarray with sum ≥ target
   - **Kata correlation**: `sliding_window/variable_window/kata.py` - Kata 2
   - Pattern: Minimize instead of maximize

3. **Longest Repeating Character Replacement** (#424)
   - Longest substring with k replacements
   - **Kata correlation**: `sliding_window/variable_window/kata.py` - Kata 3
   - Pattern: Variable window with frequency tracking

---

## Recommended Daily Practice Flow

### Week 1-2: Fill Critical Gaps

**Morning Kata (10 min):**

- Binary Search kata 1 (classic) - 3 reps
- Two Pointers fast/slow kata 1 - 2 reps

**LeetCode Problems (45 min):**

- Day 1: Binary Search (#704) - Your first binary search problem!
- Day 2: Search Insert Position (#35)
- Day 3: Linked List Cycle (#141) - Your first fast/slow pointer!
- Day 4: First Bad Version (#278)
- Day 5: Happy Number (#202)
- Day 6: Review + practice weaker problems
- Day 7: Two Sum II (#167) - Reinforce two pointers

### Week 3-4: Deepen All Patterns

**Morning Kata (10 min):**

- Rotate through all 5 patterns
- Focus on speed and zero bugs

**LeetCode Problems (45 min):**

- Mix of Medium problems from all patterns
- Valid Palindrome (#125)
- Container With Most Water (#11)
- Longest Substring Without Repeating (#3)
- Minimum Size Subarray Sum (#209)

---

## Pattern Mastery Checklist

### Two Pointers - Opposite Ends

- [x] Practiced kata 10+ times
- [x] Used in 2+ cantrips (Reverse String, Squares)
- [ ] Used in 5+ cantrips total
- [ ] Can recognize in < 30 seconds
- [ ] Zero bugs on last 5 attempts

### Two Pointers - Fast/Slow

- [ ] Practiced kata 10+ times
- [ ] Used in 1+ cantrips
- [ ] Used in 3+ cantrips total
- [ ] Can recognize in < 30 seconds
- [ ] Zero bugs on last 5 attempts

### Binary Search

- [ ] Practiced kata 100+ times (THE GOAL!)
- [ ] Used in 1+ cantrips
- [ ] Used in 5+ cantrips total
- [ ] Can code classic BS with eyes closed
- [ ] Zero bugs on last 10 attempts

### Sliding Window - Fixed

- [x] Practiced kata 10+ times
- [x] Used in 1+ cantrips (Maximum Average)
- [ ] Used in 3+ cantrips total
- [ ] Can recognize in < 30 seconds
- [ ] Zero bugs on last 5 attempts

### Sliding Window - Variable

- [x] Practiced kata 10+ times
- [x] Used in 1+ cantrips (Longest Subarray)
- [ ] Used in 3+ cantrips total
- [ ] Can recognize in < 30 seconds
- [ ] Zero bugs on last 5 attempts

---

## Quick Reference: Pattern → Problems

| Kata Pattern                  | Easy Problems          | Medium Problems | Your Progress    |
| ----------------------------- | ---------------------- | --------------- | ---------------- |
| **Two Pointers (Opposite)**   | #125, #167, #344, #977 | #11, #15        | 2/6 ✅           |
| **Two Pointers (Fast/Slow)**  | #141, #202             | #142, #287      | 0/4 ❌           |
| **Binary Search**             | #35, #278, #704        | #33, #34        | 0/5 ❌ CRITICAL! |
| **Sliding Window (Fixed)**    | #219, #643             | #2461           | 1/3 ✅           |
| **Sliding Window (Variable)** | -                      | #3, #209, #424  | 1/3 ✅           |

---

## Immediate Action Items

**Today:**

1. Do Binary Search kata 1 (classic) - 5 times
2. Solve Binary Search (#704) - Your first BS problem!
3. Log time and bugs in kata file

**This Week:**

1. Binary Search kata daily (goal: 100 reps over 8 weeks)
2. Solve all 3 easy binary search problems (#704, #35, #278)
3. Linked List Cycle (#141) - Your first fast/slow pointer

**By End of Week 2:**

- 20 binary search kata reps minimum
- 5 binary search cantrips solved
- 2 fast/slow pointer cantrips solved
- All patterns used at least once

---

## Tracking Your Progress

Update this file as you solve problems:

- Mark [x] when you solve a recommended problem
- Note the date and your kata rep count
- Track pattern recognition speed (goal: < 30 sec)
- Log bug count (goal: zero bugs)

**Last Updated**: [Date] **Binary Search Reps**: 0/100 ⚠️ START TODAY! **Patterns
Mastered**: 0/5 (Working on it!)
