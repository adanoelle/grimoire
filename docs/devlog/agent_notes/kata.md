What I Built

A complete daily practice system for building muscle memory with core algorithmic
patterns - the missing piece between knowing patterns and mastering them.

1. Pattern Kata Libraries (runes/algorithms/)

Created 6 fundamental pattern directories with templates + practice katas:

runes/algorithms/ ├── two_pointers/ │ ├── opposite_ends/ # Pair sum, palindrome,
container │ ├── fast_slow/ # Cycle detection, find middle │ └── same_direction/ #
(ready for you to add) │ ├── searching/ │ └── binary_search/ # Classic, first/last,
rotated array │ └── sliding_window/ ├── fixed_window/ # Max sum k, averages └──
variable_window/ # Longest substring, min subarray

Each pattern has:

- **init**.py - Clean reference templates (you CAN look at these)
- kata.py - Practice from memory (DON'T peek!)
- README.md - When to use, complexity, interview tips

2. KATA_PRACTICE.md - Your Daily Ritual Guide

Comprehensive guide explaining:

- Philosophy: Scales vs. songs metaphor
- 5-minute kata session workflow
- Twice-daily practice (morning + evening)
- Mastery progression (Learning → Practicing → Breathing Knowledge)
- Weekly pattern focus
- The 100-repetition rule for binary search
- Integration with LeetCode ritual

3. Updated ALGORITHM_MASTERY.md

Integrated kata practice into the daily ritual section:

- Morning kata warmup (5-10 min) BEFORE LeetCode
- Week-by-week kata focus
- Evening reinforcement (optional)

How to Use This System

Your New Daily Flow

Morning (60-70 min total):

6:00-6:10 AM: Kata Warmup (10 min) ├─ Pick today's pattern (e.g., two pointers) ├─ cd
packages/runes/src/runes/algorithms/two_pointers/opposite_ends ├─ python kata.py ├─
Code kata 1-2 from memory (2-3 min each) ├─ Run tests, log progress └─ Build fresh
muscle memory

6:10-7:00 AM: LeetCode Ritual (50 min) └─ Use /ritual for guided practice └─ Apply
the patterns you just warmed up!

Evening (5 min, optional but powerful):

7:00-7:05 PM: Kata Reinforcement └─ Repeat patterns used in today's LeetCode └─ Focus
on any that felt shaky └─ Spaced repetition

Start TODAY

Right now, do your first kata:

# Navigate to two pointers

cd packages/runes/src/runes/algorithms/two_pointers/opposite_ends

# Read the template first (understand it)

cat **init**.py

# Now practice from memory

code kata.py # Open and code KATA 1: two_sum_sorted

# Set timer for 2 minutes

# Delete 'pass', code from memory

# NO peeking!

# Run tests

python kata.py

Tomorrow morning:

- Do the same kata again
- Aim to be faster
- Track in the practice log

By week 2:

- Under 2 minutes, zero bugs
- Move to kata 2

The Weekly Plan

Week 1-2: (Starting TODAY!)

- Morning kata: Two pointers (opposite ends) - kata 1-2
- Morning kata: Binary search (classic) - kata 1
- LeetCode: Use these patterns in Medium problems
- Goal: Can code from memory with small bugs

Week 3-4:

- Morning kata: Sliding window (fixed) - kata 1-2
- Morning kata: Binary search (variants) - kata 2-3
- LeetCode: More complex applications
- Goal: Zero bugs, under target time

Week 5-6:

- Morning kata: Two pointers (fast-slow) - kata 1-2
- Morning kata: Sliding window (variable) - kata 1-2
- LeetCode: Combine patterns
- Goal: Breathing knowledge for Tier 1

Week 7-8:

- Morning kata: All Tier 1 patterns in sequence
- LeetCode: Hardest problems, mocks
- Goal: Muscle memory so deep you can code with eyes closed

The Key Exercises

CRITICAL: Binary Search (100 Reps)

The most important kata:

Code classic binary search 100 times until you can do it perfectly, zero bugs, under
2 minutes, with your eyes closed.

Track every attempt in runes/algorithms/searching/binary_search/kata.py:

| Date       | Kata | Attempt # | Time | Bugs | Notes                       |
| ---------- | ---- | --------- | ---- | ---- | --------------------------- |
| 2025-11-16 | 1    | 1         | 4:30 | 2    | Used left<right, off-by-one |
| 2025-11-16 | 1    | 2         | 3:15 | 1    | Forgot mid calculation      |

... 2025-12-01 | 1 | 100 | 1:15 | 0 | MASTERED!

Foundational: Two Pointers

Master these three katas:

1. Two sum sorted (< 2 min, zero bugs)
2. Is palindrome (< 2 min, zero bugs)
3. Container with most water (< 3 min, zero bugs)

Essential: Sliding Window

Fixed window:

- Max sum subarray (< 2 min, zero bugs)

Variable window:

- Longest substring no repeat (< 3 min, zero bugs)

Why This Works

The Science:

- Spaced repetition: Same kata every few days → long-term memory
- Deliberate practice: Timed, focused, immediate feedback
- Muscle memory: 100+ reps → automatic implementation
- Transfer: Kata warmup → immediate LeetCode application

The Results:

Week 1: "I have to think through how to implement two pointers..."

Week 4: "My fingers just type the two-pointer template..."

Week 8: "I see 'sorted array + find pair' and the implementation flows out
automatically. The interviewer is impressed by how clean and bug-free my code is."

Files Created

packages/runes/src/runes/algorithms/ ├── two_pointers/ │ ├── opposite_ends/ │ │ ├──
**init**.py ✅ Templates │ │ ├── kata.py ✅ 5 practice katas │ │ └── README.md ✅
Pattern guide │ └── fast_slow/ │ ├── **init**.py ✅ Templates │ └── kata.py ✅ 4
practice katas │ ├── searching/ │ └── binary_search/ │ ├── **init**.py ✅ Templates │
└── kata.py ✅ 6 practice katas │ └── sliding_window/ ├── fixed_window/ │ ├──
**init**.py ✅ Templates │ └── kata.py ✅ 3 practice katas └── variable_window/ ├──
**init**.py ✅ Templates └── kata.py ✅ 4 practice katas

docs/ └── KATA_PRACTICE.md ✅ Complete guide └── ALGORITHM_MASTERY.md ✅ Updated with
kata integration

The Commitment

10-15 minutes per day × 56 days = 560 minutes of focused pattern practice

That's how you build muscle memory that makes Google interviewers think: "This person
has mastered the fundamentals at a deep level."

---

Start Right Now

1. Read the guide: cat docs/KATA_PRACTICE.md
2. Do your first kata: cd
   packages/runes/src/runes/algorithms/two_pointers/opposite_ends python kata.py
3. Set daily reminders:
   - 7:00 AM: "Kata warmup before LeetCode"
   - 7:00 PM: "Kata reinforcement"

4. Tomorrow: Same kata, aim to be faster
5. Track progress in the kata files
6. 8 weeks from now: Walk into interviews with patterns that feel like breathing

---

You now have the complete system musicians use to master their instrument. Scales
(katas) + songs (LeetCode) = mastery.

Ready to practice your first kata? 🥋🔥
