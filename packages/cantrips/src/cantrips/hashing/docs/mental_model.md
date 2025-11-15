# 🔍 How to Recognize a Hashing Problem

## Key Signal Words

- "Find pairs" or "two elements" → Complement pattern (Two Sum)
- "Count frequency" or "occurrences" → Frequency map
- "Check for duplicates" → HashSet
- "Find unique" or "first non-repeating" → Frequency counting
- "Group by" or "categorize" → HashMap with categorical keys
- "Subarray sum" → Prefix sum + HashMap
- "Anagram" → Sorted string or char count as key

## Performance Clues

- Brute force is O(n²) but you need O(n) → Usually needs hashing
- Need to "remember" previously seen values → HashMap/HashSet
- Need O(1) lookup → HashMap/HashSet is the answer

---

## 🎯 The Three Core Hashing Patterns

Pattern 1: HashSet for Existence/Duplicates

Mental Model: "Have I seen this before?"

Structure: seen = set() for item in items: if item in seen: # Found duplicate/match
seen.add(item)

## When to use:

- Checking for duplicates
- Checking membership
- Finding complements/pairs

## Examples:

- Contains Duplicate (you did this!)
- Two Sum (checking for complement)
- Happy Number

Time/Space: O(n) / O(n)

---

## Pattern 2: HashMap for Counting/Frequency

### Mental Model: "How many times have I seen this?"

Structure: from collections import Counter counts = Counter(items)

**Or manually**:

counts = {} for item in items: counts[item] = counts.get(item, 0) + 1

### When to use:

- Count occurrences
- Find most/least frequent
- Find first unique character
- Compare frequencies (anagrams)

### Examples:

- First Unique Character
- Valid Anagram
- Ransom Note

**Time/Space**: O(n) / O(k) where k = unique elements

---

## Pattern 3: HashMap for Association/Mapping

### Mental Model: "What value is associated with this key?"

Structure: mapping = {} for item in items: key = compute_key(item) if key not in
mapping: mapping[key] = [] mapping[key].append(item)

### When to use:

- Group items by property (Group Anagrams)
- Map value to index (Two Sum)
- Track relationships
- Prefix sum problems

### Examples:

- Two Sum (value → index)
- Group Anagrams (sorted string → list of words)
- Subarray Sum (prefix_sum → count/index)

**Time/Space**: O(n) / O(n)

---

# 🧩 Advanced Patterns (You'll See These Soon)

## Pattern 4: HashMap + Prefix Sum

### Mental Model: "What running sum/count have I seen before?"

Technique: prefix_sum = 0 sums = {0: 1} # Base case for num in nums: prefix_sum +=
num # Check if (prefix_sum - target) exists if (prefix_sum - target) in sums: # Found
subarray

### When to use:

- Subarray sum problems
- Contiguous subarray with condition
- "Find number of subarrays..."

### Examples:

- Subarray Sum Equals K (LC #560)
- Continuous Subarray Sum

---

## Pattern 5: HashMap + Sliding Window

### Mental Model: "Track frequency in current window"

#### Technique:

```python
window = {} left = 0 for right, char in enumerate(s): window[char] =
window.get(char, 0) + 1
while violates_condition(window):
    window[s[left]] -= 1
    left += 1
```

### When to use:

- Longest/shortest substring with constraint
- Variable window size problems
- Character/element frequency in window

### Examples:

- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Permutation in String

---

## 🎓 Your Problem-Solving Framework

### Step 1: Recognition (30 seconds)

Ask yourself:

1. Do I need to remember previous values? → Likely hashing
2. Is brute force O(n²) with nested loops? → Can hashing make it O(n)?
3. Do I need to count, group, or check existence? → Hashing!

### Step 2: Choose Data Structure (1 minute)

- Need existence only? → set()
- Need counts? → Counter() or dict
- Need association? → dict with custom keys
- Need ordering + counts? → Consider dict (maintains insertion order in Python 3.7+)

### Step 3: Pick Pattern (2-3 minutes)

Match problem to one of the 5 patterns above:

1. Existence/Duplicates → HashSet
2. Counting → Counter/HashMap
3. Association → HashMap with custom keys
4. Prefix Sum → HashMap tracking running sums
5. Sliding Window → HashMap tracking window state

### Step 4: Implement (10-20 minutes)

- Start with the basic structure
- Handle edge cases
- Write tests

---

## Quick Reference Table

| Problem Type              | Data Structure | Pattern        | Example            |
| ------------------------- | -------------- | -------------- | ------------------ |
| Find duplicates           | set()          | Existence      | Contains Duplicate |
| Find pairs (two elements) | dict or set    | Complement     | Two Sum            |
| Count occurrences         | Counter        | Frequency      | Valid Anagram      |
| Group by property         | dict           | Association    | Group Anagrams     |
| Subarray sum              | dict           | Prefix Sum     | Subarray Sum = K   |
| Substring with constraint | dict           | Sliding Window | Longest Substring  |
| First unique element      | Counter        | Frequency      | First Unique Char  |
| Check membership          | set()          | Existence      | Jewels and Stones  |

---

## 🔥 Pro Tips for Interviews

1. State your approach first: "This looks like a hashing problem because we need O(1)
   lookups..."
2. Mention the trade-off: "Using a HashMap gives us O(n) time but requires O(n)
   space"
3. Consider alternatives: "We could also solve this with sorting in O(n log n) time
   but O(1) space"
4. Optimize incrementally: Start with HashSet, then realize you need counts → upgrade
   to HashMap

---

### Your Current Mastery

From your completed problems:

- ✅ Pattern 1 (Existence): Contains Duplicate, Jewels and Stones
- ✅ Pattern 3 (Association): Two Sum (value→index), Missing Number (range→set)
- ⏳ Pattern 2 (Counting): Not yet practiced
- ⏳ Pattern 4 (Prefix Sum): Not yet practiced
- ⏳ Pattern 5 (Sliding Window): Not yet practiced

---

### Recommended Next Steps

Based on this framework, here's the optimal learning path:

1. Group Anagrams → Practice Pattern 2 (Counting) + Pattern 3 (Association with
   custom keys)
2. Subarray Sum Equals K → Learn Pattern 4 (Prefix Sum + HashMap)
3. Longest Substring Without Repeating → Combine Pattern 1 + Pattern 5 (Sliding
   Window)

Does this mental model help? Which pattern would you like to practice next? I'd
recommend Group Anagrams since it combines counting (Pattern 2) with grouping
(Pattern 3) - it's a natural next step! 🔮
