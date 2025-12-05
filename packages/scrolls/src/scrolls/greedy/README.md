# Greedy Algorithms

## Overview

Greedy algorithms make locally optimal choices at each step. Often combined with
sorting. Key challenge: proving correctness.

## Core Concepts

### Concept 1: Local Optimality

**What it is**: Choose best option at each step **When to use**: When local choices
lead to global optimum **Time complexity**: Varies, often O(n log n) due to sorting

### Concept 2: Interval Problems

**What it is**: Scheduling, merging, or selecting intervals **When to use**:
"Non-overlapping", "maximum meetings" **Time complexity**: O(n log n) for sorting

### Concept 3: Exchange Argument

**What it is**: Proof technique for greedy correctness **When to use**: Proving
greedy works **Time complexity**: N/A (proof technique)

## Common Patterns

### Pattern 1: Sort + Greedy

**Recognition**: "Maximum", "minimum", with ordering **Approach**: Sort by
appropriate criterion, then greedily select **Example problems**: Assign Cookies

### Pattern 2: Interval Scheduling

**Recognition**: "Non-overlapping intervals", "meetings" **Approach**: Sort by end
time, greedily select **Example problems**: Non-overlapping Intervals

### Pattern 3: Two-choice Greedy

**Recognition**: "At least", "at most", binary choice at each step **Approach**:
Compare two options, pick better one **Example problems**: Jump Game

## Problems

Fill in problems as you work through the section.

### Easy Problems

- [ ] **[Problem Name](link)** - LC #

### Medium Problems

- [ ] **[Problem Name](link)** - LC #

### Hard Problems

- [ ] **[Problem Name](link)** - LC #

## Progress Tracker

**Completed**: 0 / 6

- Easy: 0 / 2
- Medium: 0 / 3
- Hard: 0 / 1

## Related Runes

- Greedy is more about algorithmic technique than specific data structures
