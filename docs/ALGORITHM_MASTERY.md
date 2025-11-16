# Algorithm Mastery Guide

> "The goal is not to know algorithms. The goal is for explaining them to feel like
> breathing."

This guide contains the core algorithms and mental frameworks that will make LeetCode
problem-solving feel natural and interviews feel like a breeze. These are the
patterns expert interviewers expect you to reach for instinctively.

## Philosophy: Breathing Knowledge

**Breathing knowledge** means:

- You recognize the pattern in under 30 seconds
- You can code the solution from memory in under 3 minutes
- You can explain the intuition in one sentence
- The optimization feels obvious, not clever

**How to use this guide:**

1. Work through patterns in order (Tier 1 → Tier 4)
2. For each pattern, solve the canonical problems
3. Practice the daily drills until muscle memory kicks in
4. Track your mastery level with the checkboxes
5. Review weekly using the quick reference tables

---

## Self-Assessment Tracker

Track your mastery level for each core pattern:

- `[ ]` Learning: Understanding the concept
- `[~]` Practicing: Can solve with hints/reference
- `[x]` Mastered: Instinctive recognition and implementation

### Tier 1: Absolute Fundamentals

- [ ] Two Pointers
- [ ] Hash Maps for O(1) Lookup
- [ ] Binary Search
- [ ] Sliding Window

### Tier 2: Graph & Tree Traversal

- [ ] DFS (Depth-First Search)
- [ ] BFS (Breadth-First Search)
- [ ] Tree Traversals (Inorder, Preorder, Postorder)

### Tier 3: Power Patterns

- [ ] Monotonic Stack/Queue
- [ ] Prefix Sums
- [ ] Union-Find (Disjoint Set)

### Tier 4: Advanced High-Leverage

- [ ] Dynamic Programming Patterns
- [ ] Greedy + Sorting
- [ ] Heap (Priority Queue)

---

## Tier 1: The Absolute Fundamentals

Master these first. They appear in 60-70% of Easy/Medium problems.

### 1. Two Pointers

**Core Intuition:** Process array/string from multiple positions to avoid nested
loops

**When to Apply:**

- You're considering nested loops on sorted/ordered data
- Need to find pairs with a property
- Need to partition or rearrange elements

**Complexity:**

- Time: O(n) - single pass with two pointers
- Space: O(1) - only pointer variables

**Core Variants:**

1. **Opposite ends** (palindrome, pair sum in sorted array)
2. **Same direction, different speeds** (remove duplicates, partition)
3. **Fast & slow** (cycle detection in linked lists)

**Canonical Problems:**

- LC #167: Two Sum II - Input Array Is Sorted (Easy)
- LC #15: 3Sum (Medium)
- LC #11: Container With Most Water (Medium)

**Daily Practice Drill (5 min):**

```python
# Drill 1: Code opposite-ends two pointer from memory
def two_sum_sorted(nums, target):
    """Find pair that sums to target in sorted array"""
    # Code this without looking - 2 minutes max
    pass

# Drill 2: Code fast-slow pointer from memory
def has_cycle(head):
    """Detect cycle in linked list"""
    # Code this without looking - 2 minutes max
    pass
```

**Breathing Knowledge Test:**

- See "sorted array" + "find pair" → instant two-pointer reflex
- See "linked list" + "cycle" → instant fast-slow pointer reflex

---

### 2. Hash Maps for O(1) Lookup

**Core Intuition:** Trade space for time by storing what you've seen

**When to Apply:**

- Looking for complements (two sum)
- Counting frequency/occurrences
- Checking if element exists
- Grouping/categorizing elements

**Complexity:**

- Time: O(n) - single pass with O(1) lookups
- Space: O(n) - storing elements in hash map

**Core Patterns:**

1. **Complement lookup** (two sum, pair finding)
2. **Frequency counting** (anagrams, character maps)
3. **Seen set** (duplicates, unique elements)

**Canonical Problems:**

- LC #1: Two Sum (Easy)
- LC #49: Group Anagrams (Medium)
- LC #383: Ransom Note (Easy)

**Daily Practice Drill (5 min):**

```python
# Drill 1: Two Sum from memory
def two_sum(nums, target):
    """Find indices of two numbers that sum to target"""
    # Code in under 2 minutes without looking
    pass

# Drill 2: First unique character from memory
def first_uniq_char(s):
    """Find first non-repeating character"""
    # Code in under 2 minutes without looking
    pass
```

**Breathing Knowledge Test:**

- Hear "find pair/complement" → immediate hashmap thought
- Hear "frequency/count" → immediate hashmap thought
- Think "I need to check if X exists" → reach for hashmap

---

### 3. Binary Search

**Core Intuition:** Not just for finding elements - search the answer space on
monotonic functions

**When to Apply:**

- Data is sorted
- You can verify if answer X works in O(n) or less
- Looking for minimum/maximum value that satisfies condition
- Rotated/shifted sorted arrays

**Complexity:**

- Time: O(log n) - halving search space each iteration
- Space: O(1) - iterative, or O(log n) for recursive

**Core Patterns:**

1. **Find exact element** (classic binary search)
2. **Find boundary** (first/last occurrence)
3. **Search answer space** (minimize max, maximize min)

**Canonical Problems:**

- LC #704: Binary Search (Easy)
- LC #33: Search in Rotated Sorted Array (Medium)
- LC #875: Koko Eating Bananas (Medium)

**Daily Practice Drill (5 min):**

```python
# Drill 1: Classic binary search from memory
def binary_search(nums, target):
    """Find target in sorted array, return index or -1"""
    # Must code without bugs in under 2 minutes
    pass

# Drill 2: Find first occurrence from memory
def first_occurrence(nums, target):
    """Find leftmost index of target"""
    # Code in under 3 minutes
    pass
```

**Breathing Knowledge Test:**

- See "sorted" → think binary search
- See "minimize the maximum" or "maximize the minimum" → think binary search on
  answer
- Can code bug-free binary search with eyes closed

---

### 4. Sliding Window

**Core Intuition:** Maintain a window of elements and expand/contract to satisfy
constraints

**When to Apply:**

- Finding subarray/substring with property X
- Hear words: "contiguous," "substring," "subarray"
- Optimization from O(n²) checking all subarrays

**Complexity:**

- Time: O(n) - each element enters and exits window once
- Space: O(1) or O(k) - for tracking window state

**Core Patterns:**

1. **Fixed window** (max sum of k elements)
2. **Variable window** (longest substring with condition)
3. **Window + hashmap** (character frequency constraints)

**Canonical Problems:**

- LC #643: Maximum Average Subarray I (Easy)
- LC #3: Longest Substring Without Repeating Characters (Medium)
- LC #76: Minimum Window Substring (Hard)

**Daily Practice Drill (5 min):**

```python
# Drill 1: Fixed window from memory
def max_sum_k(nums, k):
    """Maximum sum of subarray of size k"""
    # Code in under 2 minutes
    pass

# Drill 2: Variable window from memory
def longest_substring_no_repeat(s):
    """Longest substring without repeating characters"""
    # Code in under 3 minutes
    pass
```

**Breathing Knowledge Test:**

- Hear "substring" or "subarray" → instant sliding window thought
- Hear "contiguous" → instant sliding window thought
- Can explain expand-right, contract-left pattern without thinking

---

## Tier 2: Graph & Tree Traversal

Essential for interviews. Master these until they're muscle memory.

### 5. DFS (Depth-First Search)

**Core Intuition:** Explore as deep as possible before backtracking

**When to Apply:**

- Need to explore all paths/possibilities
- Check if path exists
- Generate all combinations/permutations
- Tree/graph traversal

**Complexity:**

- Time: O(V + E) for graphs, O(n) for trees
- Space: O(h) recursive stack height, O(n) worst case

**Core Variants:**

1. **Recursive** (most intuitive, uses call stack)
2. **Iterative** (explicit stack, better for deep structures)
3. **Backtracking** (explore, mark, recurse, unmark)

**Canonical Problems:**

- LC #200: Number of Islands (Medium)
- LC #78: Subsets (Medium)
- LC #46: Permutations (Medium)

**Daily Practice Drill (5 min):**

```python
# Drill 1: Tree DFS from memory
def dfs_tree(root):
    """Print all nodes using DFS (recursive)"""
    # Code in under 1 minute
    pass

# Drill 2: Graph DFS from memory
def dfs_graph(graph, start, visited):
    """Explore graph from start node"""
    # Code in under 2 minutes
    pass
```

**Breathing Knowledge Test:**

- Should code DFS in your sleep
- Instantly know: base case, recursive case, backtrack if needed
- See "explore all paths" → DFS reflex

---

### 6. BFS (Breadth-First Search)

**Core Intuition:** Explore level by level, guarantees shortest path in unweighted
graphs

**When to Apply:**

- Need shortest path (unweighted)
- Level-order processing
- Minimum steps/moves problems
- State space exploration

**Complexity:**

- Time: O(V + E) for graphs, O(n) for trees
- Space: O(w) where w is max width, O(n) worst case

**Core Pattern:**

1. Queue for frontier
2. Visited set to avoid cycles
3. Process level by level (track level if needed)

**Canonical Problems:**

- LC #102: Binary Tree Level Order Traversal (Medium)
- LC #133: Clone Graph (Medium)
- LC #127: Word Ladder (Hard)

**Daily Practice Drill (5 min):**

```python
# Drill 1: Tree level order from memory
def level_order(root):
    """Return level-order traversal of tree"""
    # Code in under 2 minutes
    pass

# Drill 2: Shortest path in grid from memory
def shortest_path_grid(grid, start, end):
    """Find shortest path in binary grid"""
    # Code in under 3 minutes
    pass
```

**Breathing Knowledge Test:**

- Hear "shortest path" (unweighted) → BFS, not DFS
- Hear "level by level" → BFS
- Hear "minimum steps" → BFS

---

### 7. Tree Traversals (Inorder, Preorder, Postorder)

**Core Intuition:** Order of processing matters for different tree problems

**When to Apply:**

- **Inorder** (left, root, right): BST problems, gives sorted order
- **Preorder** (root, left, right): Creating copy, serialization
- **Postorder** (left, right, root): Deletion, bottom-up processing

**Complexity:**

- Time: O(n) - visit each node once
- Space: O(h) - recursive stack height

**Key Insight:**

- Inorder of BST is sorted - use this property!
- Postorder for "process children before parent"
- Preorder for "process parent before children"

**Canonical Problems:**

- LC #94: Binary Tree Inorder Traversal (Easy)
- LC #230: Kth Smallest Element in a BST (Medium)
- LC #297: Serialize and Deserialize Binary Tree (Hard)

**Daily Practice Drill (5 min):**

```python
# Drill: Code all three traversals from memory
def inorder(root):
    """Left, root, right"""
    pass

def preorder(root):
    """Root, left, right"""
    pass

def postorder(root):
    """Left, right, root"""
    pass
```

**Breathing Knowledge Test:**

- BST problem → think inorder for sorted access
- "Delete tree" → think postorder
- "Copy tree" → think preorder
- Can code all three in under 3 minutes total

---

## Tier 3: The Power Patterns

These unlock O(n) solutions to problems that seem O(n²). High impact for Medium/Hard.

### 8. Monotonic Stack/Queue

**Core Intuition:** Maintain useful ordering by removing "useless" elements

**When to Apply:**

- "Next greater/smaller element" problems
- Maintain min/max in sliding window
- Rectangle/histogram area problems

**Complexity:**

- Time: O(n) - each element pushed/popped once
- Space: O(n) - stack/queue storage

**Core Pattern:**

1. Iterate through elements
2. Pop elements that are "useless" (won't be the answer)
3. Current element is the answer for popped elements
4. Push current element

**Canonical Problems:**

- LC #496: Next Greater Element I (Easy)
- LC #739: Daily Temperatures (Medium)
- LC #84: Largest Rectangle in Histogram (Hard)

**Daily Practice Drill (5 min):**

```python
# Drill: Next greater element from memory
def next_greater_element(nums):
    """For each element, find next greater element"""
    # Code in under 3 minutes
    pass
```

**Breathing Knowledge Test:**

- Hear "next greater" → monotonic stack
- Hear "next smaller" → monotonic stack
- Understanding: we pop because those elements won't be useful anymore

---

### 9. Prefix Sums / Cumulative Arrays

**Core Intuition:** Precompute cumulative values for O(1) range queries

**When to Apply:**

- Subarray sum queries (multiple times)
- Range sum problems
- Converting O(n) per query to O(1) per query

**Complexity:**

- Time: O(n) preprocessing, O(1) per query
- Space: O(n) for prefix array

**Core Pattern:**

1. Build prefix sum: `prefix[i] = nums[0] + ... + nums[i]`
2. Range sum [i, j] = `prefix[j] - prefix[i-1]`
3. Handle edge cases (i = 0)

**Canonical Problems:**

- LC #303: Range Sum Query - Immutable (Easy)
- LC #560: Subarray Sum Equals K (Medium)
- LC #974: Subarray Sums Divisible by K (Medium)

**Daily Practice Drill (5 min):**

```python
# Drill: Build and query prefix sum from memory
def range_sum_query(nums, queries):
    """Preprocess nums, answer multiple range sum queries"""
    # Code in under 3 minutes
    pass
```

**Breathing Knowledge Test:**

- Hear "subarray sum" asked multiple times → prefix sums
- Hear "range query" → prefix sums or segment tree
- Instant recognition: sum(i to j) = prefix[j] - prefix[i-1]

---

### 10. Union-Find (Disjoint Set)

**Core Intuition:** Track connected components with near-O(1) operations

**When to Apply:**

- Dynamic connectivity queries
- Group elements by connectivity
- Cycle detection in undirected graphs
- Kruskal's MST algorithm

**Complexity:**

- Time: O(α(n)) ≈ O(1) per operation with path compression + union by rank
- Space: O(n) for parent and rank arrays

**Core Operations:**

1. **Find**: Get root of element (with path compression)
2. **Union**: Connect two components (by rank)
3. **Connected**: Check if same component

**Canonical Problems:**

- LC #547: Number of Provinces (Medium)
- LC #200: Number of Islands (Medium) - alternative to DFS
- LC #684: Redundant Connection (Medium)

**Daily Practice Drill (5 min):**

```python
# Drill: Implement Union-Find from memory
class UnionFind:
    def __init__(self, n):
        """Initialize parent and rank"""
        pass

    def find(self, x):
        """Find with path compression"""
        pass

    def union(self, x, y):
        """Union by rank"""
        pass
```

**Breathing Knowledge Test:**

- Hear "are these connected?" → Union-Find
- Hear "number of components" → Union-Find
- Can code from scratch in under 5 minutes

---

## Tier 4: Advanced High-Leverage

These are harder but appear frequently in Medium/Hard interviews.

### 11. Dynamic Programming Patterns

**Core Intuition:** Break problem into subproblems, memoize results to avoid
recomputation

**When to Apply:**

- Optimal substructure: optimal solution contains optimal solutions to subproblems
- Overlapping subproblems: same subproblems computed multiple times
- Asks for "maximum," "minimum," "count ways"

**Complexity:**

- Time: O(states × transitions)
- Space: O(states) - can often optimize to O(1) or O(k)

**Core Patterns:**

1. **1D DP** (house robber, climbing stairs)
   - `dp[i]` = answer for first i elements
2. **2D DP** (grid paths, LCS)
   - `dp[i][j]` = answer for first i elements of A, first j of B
3. **Knapsack variants**
   - 0/1 knapsack, unbounded, subset sum

**Canonical Problems:**

- LC #70: Climbing Stairs (Easy)
- LC #198: House Robber (Medium)
- LC #322: Coin Change (Medium)
- LC #300: Longest Increasing Subsequence (Medium)

**Daily Practice Drill (5 min):**

```python
# Drill 1: Recognize DP recurrence
# Given problem, identify:
# 1. What are the states?
# 2. What's the recurrence relation?
# 3. What are base cases?

# Drill 2: 1D DP from memory
def climb_stairs(n):
    """Number of ways to climb n stairs (1 or 2 steps at a time)"""
    # Code in under 2 minutes
    pass
```

**Breathing Knowledge Test:**

- Can identify optimal substructure in 30 seconds
- Can write recurrence before coding
- Know when to use top-down (memoization) vs bottom-up (tabulation)

---

### 12. Greedy + Sorting

**Core Intuition:** Local optimal choice leads to global optimal (must prove!)

**When to Apply:**

- Optimization problems (max/min)
- Interval/scheduling problems
- After proving greedy choice property holds

**Complexity:**

- Time: O(n log n) for sorting, O(n) for greedy pass
- Space: O(1) to O(n)

**Core Pattern:**

1. Sort by appropriate criterion (start time, end time, value)
2. Iterate and make greedy choice
3. Prove: greedy choice doesn't exclude optimal solution

**Canonical Problems:**

- LC #455: Assign Cookies (Easy)
- LC #435: Non-overlapping Intervals (Medium)
- LC #45: Jump Game II (Medium)

**Daily Practice Drill (5 min):**

```python
# Drill: Interval scheduling from memory
def max_non_overlapping_intervals(intervals):
    """Select maximum number of non-overlapping intervals"""
    # Code in under 2 minutes
    # Key: sort by end time!
    pass
```

**Breathing Knowledge Test:**

- See "intervals" → think sort by end time
- See "maximize/minimize" → consider greedy, then try to prove or find counterexample
- Can explain why greedy works for specific problem

---

### 13. Heap (Priority Queue)

**Core Intuition:** Maintain best element dynamically with O(log n) operations

**When to Apply:**

- "Kth largest/smallest" with streaming data
- Merge K sorted lists
- "Keep top K elements"
- Dijkstra's shortest path (weighted graphs)

**Complexity:**

- Time: O(log n) insert/extract, O(1) peek
- Space: O(k) for top-K heap, O(n) for general use

**Core Operations:**

1. **Min heap**: Parent ≤ children (get minimum quickly)
2. **Max heap**: Parent ≥ children (get maximum quickly)
3. **Heapify**: O(n) to build heap from array

**Canonical Problems:**

- LC #215: Kth Largest Element in an Array (Medium)
- LC #347: Top K Frequent Elements (Medium)
- LC #23: Merge k Sorted Lists (Hard)

**Daily Practice Drill (5 min):**

```python
import heapq

# Drill: Kth largest from memory
def find_kth_largest(nums, k):
    """Find kth largest element using min heap of size k"""
    # Code in under 2 minutes
    pass
```

**Breathing Knowledge Test:**

- Hear "Kth largest/smallest" → heap
- Hear "streaming/online" + "best element" → heap
- Know: min heap for Kth largest, max heap for Kth smallest

---

## Mental Frameworks

These are the instincts that make you seem like an expert.

### 1. The Constraint Analysis Reflex

Constraints tell you what complexity is expected:

| Constraint | Expected Complexity | Possible Approaches                     |
| ---------- | ------------------- | --------------------------------------- |
| n ≤ 10     | O(2^n), O(n!)       | Recursion, backtracking, brute force    |
| n ≤ 20     | O(2^n)              | Recursion with memoization, bitmask DP  |
| n ≤ 100    | O(n³)               | Triple nested loops (rare)              |
| n ≤ 1,000  | O(n²)               | Double nested loops, DP                 |
| n ≤ 10⁵    | O(n log n)          | Sorting, heap, divide & conquer         |
| n ≤ 10⁶    | O(n)                | Hash maps, sliding window, two pointers |
| n ≤ 10⁹    | O(log n), O(1)      | Binary search, math formula             |

**Breathing knowledge**: Glance at constraints → know immediately what won't work

---

### 2. Pattern Recognition Flowchart

**Input Analysis:**

```
Is the array/string sorted?
  → YES: Binary search, two pointers
  → NO: Can sorting help? Or hash map?

Looking for pairs/complements?
  → Hash map (O(n)) or two pointers if sorted

Subarray/substring problem?
  → Sliding window or prefix sums

Tree problem?
  → What order do I need? (Inorder/preorder/postorder)
  → Need shortest path? BFS : DFS

Graph connectivity?
  → Shortest path: BFS
  → Path exists: DFS or Union-Find
  → Components: Union-Find or DFS

Optimization with choices at each step?
  → Can greedy work (prove it)?
  → Recursive structure (DP)?
```

**Breathing knowledge**: This flowchart runs automatically in your head

---

### 3. Complexity Intuition

You should _feel_ these in your gut:

**Red flags:**

- Nested loops on same array → probably can optimize
- Looking at all pairs → O(n²), can I use hash map?
- Sorted data not using binary search → missing something
- Recursion without memoization → probably recomputing

**Green flags:**

- Single pass with hash map → optimal O(n)
- Binary search → can't beat O(log n) for searching
- BFS for shortest path → optimal for unweighted
- Sliding window for substring → optimal O(n)

**Breathing knowledge**: Code smell detection happens instantly

---

### 4. The Interview Communication Pattern

Expert interviewers notice this structure:

**Step 1: Clarify (30 seconds)**

- Can array be empty? Negative numbers?
- Is it sorted? Can I modify it?
- What's the expected complexity?

**Step 2: Brute Force (30 seconds)**

- "The naive solution is nested loops, O(n²)..."
- Don't code it, just acknowledge it

**Step 3: Optimize (2-3 minutes)**

- "We're rechecking elements we've seen..."
- "If we store seen elements in a hash map..."
- Explain the pattern you're using

**Step 4: Complexity Analysis (30 seconds)**

- "This is O(n) time, O(n) space..."
- Acknowledge trade-offs

**Step 5: Code (5-10 minutes)**

- Think out loud
- Test with small example
- Handle edge cases

**Breathing knowledge**: This structure is autopilot

---

## Quick Reference Tables

### Pattern → Complexity

| Pattern         | Time                        | Space        | Key Insight                     |
| --------------- | --------------------------- | ------------ | ------------------------------- |
| Two Pointers    | O(n)                        | O(1)         | Avoid nested loops              |
| Hash Map        | O(n)                        | O(n)         | Trade space for time            |
| Binary Search   | O(log n)                    | O(1)         | Sorted or monotonic             |
| Sliding Window  | O(n)                        | O(1) or O(k) | Each element in/out once        |
| DFS/BFS         | O(V+E)                      | O(V)         | Visit each node/edge once       |
| Monotonic Stack | O(n)                        | O(n)         | Each element pushed/popped once |
| Prefix Sum      | O(n) preprocess, O(1) query | O(n)         | Precompute for queries          |
| Union-Find      | O(α(n)) ≈ O(1)              | O(n)         | Path compression + rank         |
| DP              | O(states × transitions)     | O(states)    | Memoize subproblems             |
| Heap            | O(log n) insert/extract     | O(k) or O(n) | Maintain best dynamically       |

### Problem Type → Pattern

| Problem Type               | First Try       | Alternative          |
| -------------------------- | --------------- | -------------------- |
| Pair sum in sorted array   | Two pointers    | Hash map             |
| Pair sum in unsorted array | Hash map        | Sort + two pointers  |
| Longest substring with...  | Sliding window  | -                    |
| Subarray sum queries       | Prefix sum      | -                    |
| Next greater element       | Monotonic stack | -                    |
| Shortest path (unweighted) | BFS             | -                    |
| Shortest path (weighted)   | Dijkstra (heap) | Bellman-Ford         |
| Connected components       | Union-Find      | DFS/BFS              |
| Kth largest/smallest       | Heap            | Quickselect          |
| Top K elements             | Heap            | -                    |
| Interval scheduling        | Sort + greedy   | -                    |
| Optimize with choices      | DP              | Greedy (if provable) |

---

## Daily Practice Ritual

### Morning Warmup: Kata Practice (5-10 minutes) 🥋

**BEFORE solving LeetCode problems, practice algorithm katas:**

This builds muscle memory. See `docs/KATA_PRACTICE.md` for full guide.

1. **Pick today's pattern focus** (e.g., two pointers, binary search)
2. **Navigate to kata file:**
   ```bash
   cd packages/runes/src/runes/algorithms/two_pointers/opposite_ends
   python kata.py
   ```
3. **Set timer** (2-3 min per kata)
4. **Code from memory** - NO peeking at templates!
5. **Run tests** - Zero bugs is the goal
6. **Log progress** - Track time and bugs

**Why this works:**
- Fresh muscle memory before LeetCode
- Pattern becomes automatic
- Implementation is instant, not thought-through

**Recommended katas:**
- **Week 1-2:** Two pointers (opposite ends), binary search (classic)
- **Week 3-4:** Sliding window (fixed), binary search (variants)
- **Week 5-6:** Two pointers (fast-slow), sliding window (variable)
- **Week 7-8:** All Tier 1 patterns in sequence

---

### LeetCode Problem Solving

**After kata warmup, solve today's problem:**

1. Read the problem statement
2. Identify pattern category in 30 seconds (faster after katas!)
3. State expected complexity based on constraints
4. Choose your approach before coding

### During Solving

**Narrate your thought process:**

1. "This looks like [pattern] because..."
2. "I'm using [data structure] to..."
3. "The complexity will be..."
4. Talk out loud even when alone

### After Solving (5 minutes)

**Reflection checklist:**

- [ ] Did I recognize the pattern quickly?
- [ ] Did I code without bugs?
- [ ] Did I explain complexity correctly?
- [ ] What was the key insight?
- [ ] Write pattern + insight in topic README

### Evening Reinforcement: Kata Review (5 min)

**Optional but powerful:**

1. Repeat katas for patterns used in today's LeetCode
2. Focus on any that felt shaky
3. Build spaced repetition

### Spaced Repetition

- **Daily:** Same kata until under target time, zero bugs
- **3 days later**: Re-solve kata to verify retention
- **1 week later**: Solve LeetCode problem using that pattern
- **1 month later**: Harder variant of pattern

---

## The "Explain to a 5-Year-Old" Test

For each core pattern, can you:

1. **Explain the intuition in one sentence?**
   - "Two pointers avoids nested loops by tracking from both ends"
   - "Hash map trades memory to remember what we've seen"

2. **Code it from memory in under 3 minutes?**
   - Set a timer, code without reference
   - If you can't, you don't know it yet

3. **Recognize the pattern in under 30 seconds?**
   - Read new problem
   - Identify pattern before reading constraints
   - If it takes longer, keep practicing

If you can't pass all three, the pattern isn't "breathing knowledge" yet.

---

## 8-Week Sprint Integration

### Weeks 1-2: Master Tier 1

**Focus:** Two pointers, hash maps, binary search, sliding window

- Solve 5-7 problems per pattern
- Do daily drills until muscle memory
- Goal: All Tier 1 patterns at "Mastered" level

### Weeks 3-4: Master Tier 2 + Practice Tier 1

**Focus:** DFS, BFS, tree traversals

- Solve 5-7 problems per pattern
- Mix in Tier 1 problems to maintain fluency
- Goal: All Tier 2 at "Mastered," Tier 1 still sharp

### Weeks 5-6: Add Tier 3 + Harder Problems

**Focus:** Monotonic stack, prefix sums, Union-Find, intro to DP

- Solve Medium/Hard problems combining patterns
- Start recognizing pattern combinations
- Goal: Tier 3 at "Practicing," Tiers 1-2 instinctive

### Weeks 7-8: Polish + Mock Interviews

**Focus:** DP, heaps, hardest problems, full mocks

- Explain solutions out loud
- Time yourself (45 min per problem max)
- Simulate interview pressure
- Goal: All patterns accessible under pressure

### Weekly Check-In Questions

- Which patterns did I use this week?
- Which patterns felt natural vs. struggled?
- Did I recognize patterns quickly?
- Can I code them without reference?

---

## Progress Tracking

### Weekly Review (Sundays)

Use `/weekly-review` to assess:

- How many problems solved?
- Which patterns practiced?
- Which patterns need more work?
- Are you on pace for sprint goals?

### Pattern Mastery Checklist

For each pattern, track:

- [ ] Read about it / watched explanation
- [ ] Solved canonical problems (Easy)
- [ ] Can code template from memory
- [ ] Solved 5+ problems using this pattern
- [ ] Can explain when to use it
- [ ] Recognize it instantly in new problems
- [ ] Solved Medium/Hard variants

### Red Flags to Watch

- Taking > 5 minutes to recognize pattern
- Can't code template without reference
- Keep making same bugs
- Need to re-learn pattern every week

If you see red flags, slow down and drill that pattern more.

---

## Conclusion

Algorithmic mastery isn't about memorizing solutions. It's about building instincts:

- Pattern recognition becomes instant
- Implementation becomes automatic
- Complexity analysis becomes intuitive
- Communication becomes natural

**The goal**: When you see a new LeetCode problem, your brain automatically:

1. Identifies the pattern (30 seconds)
2. Recalls the template (immediate)
3. Adapts to specific problem (2-3 minutes)
4. Codes bug-free solution (5-10 minutes)

This only happens through deliberate practice. Use this guide as your roadmap.

**Your daily commitment:**

- 1-2 problems with full focus
- Document the pattern you practiced
- Do 5-minute drill on weak patterns
- Update your mastery checklist weekly

**Remember:** You're not trying to solve every problem. You're trying to master every
pattern. Once patterns are breathing knowledge, any problem becomes solvable.

Now go forth and make these patterns second nature!

---

## Appendix: Pattern Recognition Practice

### Diagnostic Test (Try before reading hints)

For each problem description, identify the pattern in 30 seconds:

1. "Find two numbers in sorted array that sum to target"
2. "Longest substring without repeating characters"
3. "Find if path exists between two nodes in graph"
4. "Kth largest element in unsorted array"
5. "Count number of islands in grid"
6. "Next greater element for each element in array"
7. "Minimum window substring containing all characters"
8. "Number of connected components in undirected graph"

**Answers:**

1. Two pointers (sorted → two pointers)
2. Sliding window (substring → sliding window)
3. DFS or BFS (path exists → DFS)
4. Heap (Kth largest → min heap of size k)
5. DFS or Union-Find (islands/components → DFS)
6. Monotonic stack (next greater → monotonic stack)
7. Sliding window + hash map (window + character count)
8. Union-Find or DFS (components → Union-Find)

**Scoring:**

- 8/8: Breathing knowledge achieved
- 6-7/8: Very good, keep practicing
- 4-5/8: Practicing level, more repetitions needed
- 0-3/8: Learning level, focus on pattern study

Retake this test weekly to track improvement.
