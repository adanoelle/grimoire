# Heaps

## Overview

Heaps (priority queues) efficiently maintain min/max elements. Essential for "top K",
scheduling, and median-finding problems.

## Core Concepts

### Concept 1: Min Heap

**What it is**: Tree where parent ≤ children **When to use**: Finding minimum, k
smallest elements **Time complexity**: O(log n) insert/remove, O(1) peek

### Concept 2: Max Heap

**What it is**: Tree where parent ≥ children **When to use**: Finding maximum, k
largest elements **Time complexity**: O(log n) insert/remove, O(1) peek

### Concept 3: Top K Pattern

**What it is**: Maintain heap of size k **When to use**: "K largest", "K closest", "K
frequent" **Time complexity**: O(n log k)

## Common Patterns

### Pattern 1: K Largest/Smallest

**Recognition**: "K largest", "top K" **Approach**: Min heap of size k for largest,
max heap for smallest **Example problems**: Kth Largest Element

### Pattern 2: Two Heaps (Median)

**Recognition**: "Running median", "balance" **Approach**: Max heap for lower half,
min heap for upper half **Example problems**: Find Median from Data Stream

### Pattern 3: K-way Merge

**Recognition**: "Merge K sorted" **Approach**: Heap with one element from each list
**Example problems**: Merge K Sorted Lists

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

- [Heap](../../../runes/structures/heap/)
