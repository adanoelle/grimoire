# Hashing

## Overview

Hashing enables O(1) average-case lookups, making it essential for problems
involving counting, frequency analysis, and finding duplicates or complements.

## Core Concepts

### Concept 1: Hash Maps (Dictionaries)

**What it is**: Key-value storage with O(1) average lookup **When to use**:
Counting, caching, two-element lookups **Time complexity**: O(1) average, O(n)
worst

### Concept 2: Hash Sets

**What it is**: Collection of unique elements with O(1) membership testing
**When to use**: Checking existence, finding duplicates **Time complexity**:
O(1) average

### Concept 3: Frequency Counting

**What it is**: Using hash map to track occurrence counts **When to use**: "Most
frequent", "first unique", character counting **Time complexity**: O(n)

## Common Patterns

### Pattern 1: Complement Pattern

**Recognition**: Two Sum, pair problems **Approach**: Store seen elements, check
for complement **Example problems**: Two Sum, Two Sum variations

### Pattern 2: Counting with HashMap

**Recognition**: "Count occurrences", "frequency" **Approach**: Build frequency
map, then process **Example problems**: First unique character

### Pattern 3: HashSet for Duplicates

**Recognition**: "Find duplicate", "contains duplicate" **Approach**: Add to
set, check if already present **Example problems**: Contains Duplicate

## Problems

Fill in problems as you work through the LeetCode hashing section.

### Easy Problems

- [x] **[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)** -
      LC #217
  - Pattern: HashSet for duplicates
  - Key insight: Set comparison - if len(set) < len(list), duplicates exist

### Medium Problems

- [ ] **[Problem Name](link)** - LC #
  - Pattern:
  - Key insight:

### Hard Problems

- [ ] **[Problem Name](link)** - LC #
  - Pattern:
  - Key insight:

## Progress Tracker

**Completed**: 1 / 9

- Easy: 1 / 4
- Medium: 0 / 4
- Hard: 0 / 1

## Key Insights

### What I learned

- First hashing problem! Hash sets provide O(1) lookup for duplicate detection
- Set size comparison technique: comparing set length vs list length
- Converting list to set automatically removes duplicates

### Common mistakes I made

-

## Related Runes

- [Hash Table](../../../runes/structures/hash_table/) - When you implement it

## Resources

- [Hash Table Visualization](https://visualgo.net)
