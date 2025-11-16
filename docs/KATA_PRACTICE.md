## Algorithm Kata Practice - Daily Ritual

> "Musicians practice scales. Athletes practice drills. Engineers practice katas."

This guide explains how to use `runes/algorithms/` kata exercises to build muscle
memory for core algorithmic patterns. This is the **missing piece** between knowing
patterns intellectually and implementing them reflexively in interviews.

## Philosophy: Scales vs. Songs

**LeetCode problems are "songs"** - complete performances where you apply patterns in
context.

**Algorithm katas are "scales"** - fundamental techniques practiced until they're
muscle memory.

A concert pianist doesn't just play songs. They practice scales, arpeggios, and
technical exercises **every single day**. The scales make the songs effortless.

**You should do the same with algorithms.**

## The Kata System

### Directory Structure

```
runes/algorithms/
├── two_pointers/
│   ├── opposite_ends/
│   │   ├── __init__.py        # Reference templates
│   │   ├── kata.py            # Practice from memory
│   │   └── README.md          # Pattern guide
│   ├── fast_slow/             # Cycle detection
│   └── same_direction/        # Remove duplicates, etc.
│
├── searching/
│   └── binary_search/
│       ├── __init__.py        # Classic, first/last occurrence
│       ├── kata.py            # Code 100 times until perfect
│       └── README.md
│
└── sliding_window/
    ├── fixed_window/          # Max sum of k elements
    └── variable_window/       # Longest substring, etc.
```

### The Two Files

Each pattern has two files:

**`__init__.py` - Reference Templates**

- Clean, documented implementations
- Study these to understand the pattern
- **You CAN look at these when learning**

**`kata.py` - Practice Problems**

- Exercises to code from memory
- Timed challenges
- **DON'T look at solutions until after you try**

## Daily Kata Ritual

### Morning Warmup (5-10 minutes)

**BEFORE your LeetCode ritual, practice core patterns:**

```
Daily Flow:
├─ 5-10 min: Kata warmup (muscle memory)
│   └─ Code 2-3 templates from memory
│
└─ 45-60 min: LeetCode ritual with /ritual
    └─ Apply patterns you just practiced
```

**Why this works:**

1. **Kata first** → Fresh muscle memory of the pattern
2. **LeetCode second** → Apply it immediately in real problems
3. **Spaced repetition** → Same kata every few days until automatic

### The 5-Minute Kata Session

**Quick Commands:**

```bash
just kata-list                    # View all available patterns
just kata-practice binary_search  # Start practice (opens in Helix)
just kata-reset-pattern binary_search  # Reset after practice (Y/n confirmation)
just kata-reset                   # Reset ALL katas (Y/n confirmation)
just kata-dry-run                 # Preview what would be reset
```

**Step 1: Pick a Pattern (30 seconds)**

```bash
just kata-list
```

Choose based on:

- What you're working on this week
- What pattern you'll practice in LeetCode today
- What felt shaky yesterday

**Step 2: Start Practice**

```bash
just kata-practice binary_search
```

This opens the kata file in Helix and shows the workflow steps.

**Step 3: Code from Memory (2-3 minutes)**

- Find KATA 1, delete 'pass', code from memory
- NO peeking at templates!
- Set timer and START

**Step 4: Run Tests (10 seconds)**

```bash
python kata.py
# OR use justfile (from workspace root)
just kata-test binary_search
```

**Step 5: Assess (30 seconds)**

- ✅ **All tests passed?** → Record time, move to next kata tomorrow
- ❌ **Tests failed?** → Debug, understand WHY, redo tomorrow
- ⏱️ **Too slow?** → Practice again tomorrow, aim for faster

**Step 6: Log Progress (20 seconds)**

- Update the mastery log in kata.py
- Track time and bugs
- Note insights

**Step 7: Reset for Next Time**

```bash
just kata-reset-pattern binary_search
# Press Enter to confirm (or 'n' to cancel)
```

This resets all implementations back to `pass` while preserving your practice log.

### Twice-Daily Practice

**Morning (5-10 min):**

- Code 2-3 katas from current focus pattern
- Builds muscle memory
- Primes brain for LeetCode

**Evening (5 min):**

- Code 1-2 katas from patterns used today
- Reinforcement
- Spaced repetition

**Total: 10-15 min/day → 8 weeks → Absolute mastery**

## The Mastery Progression

### Week 1-2: Learning

**Goal:** Understand the pattern

- Read template (`__init__.py`)
- Code kata WITH reference open
- Focus on understanding each line
- Time doesn't matter yet

**Success:** Can code kata correctly with reference

### Week 2-3: Practicing

**Goal:** Build memory

- Code kata from memory
- Small bugs are okay
- Check template AFTER attempt
- Redo next day

**Success:** Can code kata from memory with 1-2 small bugs

### Week 3-4: Refining

**Goal:** Achieve perfection

- Code kata perfectly from memory
- Under target time
- Zero bugs
- Explain while coding

**Success:** Consistent zero-bug implementations under target time

### Week 4+: Breathing Knowledge

**Goal:** Make it reflexive

- Code with eyes closed (literally!)
- Instant pattern recognition in new problems
- Can teach someone else
- Used successfully in 5+ LeetCode problems

**Success:** Pattern is muscle memory, implementation automatic

## Weekly Pattern Focus

**Weeks 1-2: Tier 1 Basics**

- Two pointers (opposite ends)
- Binary search (classic)
- Sliding window (fixed)

**Weeks 3-4: Tier 1 Complete + Tier 2 Start**

- Two pointers (fast-slow)
- Sliding window (variable)
- BFS/DFS basics

**Weeks 5-6: Tier 2 + Tier 3**

- Tree traversals
- Monotonic stack
- Prefix sums

**Weeks 7-8: Advanced + Combinations**

- DP patterns
- Pattern combinations
- Hardest variants

## Tracking Mastery

### The 100-Repetition Rule

**For binary search specifically:**

Code classic binary search **100 times** until you can do it perfectly, with zero
bugs, in under 2 minutes, **with your eyes closed**.

This is not hyperbole. True mastery = muscle memory.

**Track every attempt in kata.py:**

```
Date       | Kata | Attempt # | Time  | Bugs | Notes
-----------|------|-----------|-------|------|------------------------
2025-11-16 | 1    | 1         | 4:30  | 2    | Used left<right, off-by-one
2025-11-16 | 1    | 2         | 3:15  | 1    | Forgot mid calculation
2025-11-17 | 1    | 3         | 2:45  | 0    | Clean!
2025-11-17 | 1    | 4         | 2:10  | 0    | Getting faster
2025-11-18 | 1    | 5         | 1:50  | 0    | Under 2 min! ✓
...
2025-12-01 | 1    | 100       | 1:15  | 0    | MASTERED - can do in sleep!
```

### Mastery Checklist (Per Pattern)

Each kata file has a checklist:

```markdown
MASTERY CHECKLIST: [ ] Kata 1: Can code in < 2 min, zero bugs [ ] Kata 2: Can code in
< 3 min, zero bugs [ ] Kata 3: Can code in < 4 min, zero bugs [ ] Can explain the
pattern while coding [ ] Can identify when to use (< 30 sec recognition) [ ] Used
successfully in 5+ LeetCode problems

BREATHING KNOWLEDGE (Ultimate Goal): [ ] All katas in under 15 minutes total [ ] Zero
bugs across all katas [ ] Can teach this pattern to someone else [ ] Pattern
recognition is automatic
```

## Integration with LeetCode Ritual

### Daily Flow

**6:00 AM - Morning Practice**

```
1. Kata warmup (5-10 min)
   - Two pointers opposite ends: kata 1-2
   - Binary search: kata 1

2. LeetCode ritual (45-60 min)
   - Use /ritual for guided practice
   - Apply patterns from kata warmup

3. Commit progress
```

**6:00 PM - Evening Reinforcement**

```
1. Kata review (5 min)
   - Repeat patterns used today
   - Focus on any that felt shaky

2. Update mastery logs
3. Plan tomorrow's focus
```

### The Synergy

**Kata practice makes LeetCode easier:**

- Pattern recognition faster (< 30 sec)
- Implementation automatic
- Fewer bugs
- More time for edge cases and testing

**LeetCode practice reinforces katas:**

- See patterns in real contexts
- Learn when to apply each pattern
- Discover edge cases for kata practice

## Pattern-Specific Goals

### Two Pointers (Opposite Ends)

- **Daily:** Code 2-3 katas in < 6 minutes total
- **Weekly:** Use in 3+ LeetCode problems
- **Mastery:** Instant recognition when you see "sorted array + pairs"

### Binary Search

- **Daily:** Code classic BS in < 2 min, zero bugs
- **Goal:** 100 perfect repetitions
- **Mastery:** Can code with eyes literally closed

### Sliding Window (Fixed)

- **Daily:** Code max sum kata in < 2 min
- **Weekly:** Use in 2+ LeetCode problems
- **Mastery:** Never recalculate entire window sum

### Sliding Window (Variable)

- **Daily:** Code longest substring kata in < 3 min
- **Weekly:** Use in 2+ LeetCode problems
- **Mastery:** Expand-contract rhythm is automatic

## Red Flags & Troubleshooting

### "I keep making the same bugs"

**Solution:**

- Add that bug to your kata notes
- Create a specific drill for that edge case
- Code that kata 10 times in a row until bug-free
- Review why the bug happens conceptually

### "I'm too slow"

**Solution:**

- You're probably thinking too much
- Code the kata 5 times in a row (no breaks)
- Focus on rhythm and flow, not optimization
- Muscle memory comes from repetition

### "I can't remember the pattern"

**Solution:**

- Read the template (`__init__.py`) again
- Understand the WHY, not just the HOW
- Explain it out loud to yourself
- Draw the pattern visually
- Sleep on it and try again tomorrow

### "Katas are boring"

**Reminder:**

- Scales are boring. Concerts are exciting.
- Katas are boring. Google interviews are exciting.
- 10 minutes/day of "boring" → lifetime of "exciting" job offers

## The Commitment

**Every day for 8 weeks:**

- ✅ 5-10 min kata warmup before LeetCode
- ✅ 5 min kata reinforcement in evening
- ✅ Track progress in mastery logs
- ✅ Update checklists weekly

**No exceptions. No shortcuts.**

## Success Metrics

### Week 2:

- Can code 3+ Tier 1 patterns from memory
- Small bugs acceptable
- Building confidence

### Week 4:

- Zero bugs on Tier 1 patterns
- Under target times
- Pattern recognition < 1 minute

### Week 6:

- Tier 1 patterns are breathing knowledge
- Tier 2 patterns coded from memory
- Used patterns in 20+ LeetCode problems

### Week 8:

- All Tier 1-2 patterns automatic
- Pattern recognition < 30 seconds
- Can teach patterns to others
- **Interview ready**

## The Transformation

**Week 1:**

> "I know the pattern exists but I have to think through the implementation..."

**Week 4:**

> "I can code this pattern without really thinking about it..."

**Week 8:**

> "I see the problem and my fingers start typing the pattern automatically..."

**This is breathing knowledge.**

## Quick Start

**Today, right now:**

1. **Pick one pattern** to master this week (recommend: two pointers opposite ends)

2. **Do your first kata:**

   ```bash
   cd packages/runes/src/runes/algorithms/two_pointers/opposite_ends
   python kata.py
   ```

3. **Set a daily reminder:**
   - Morning: 7:00 AM - "Kata warmup"
   - Evening: 7:00 PM - "Kata reinforcement"

4. **Track your first attempt** in the kata file

5. **Tomorrow:** Do it again, aim to be faster

6. **Repeat for 8 weeks**

7. **Walk into Google interview** with muscle memory that makes interviewers say:
   "This person really knows their stuff."

---

## The Math

- 10 min/day × 56 days = **560 minutes** of deliberate pattern practice
- 4-6 patterns × 3-5 katas each = **20-30 unique exercises**
- Each kata practiced 10-20 times = **200-400 total repetitions**

**That's how you build world-class pattern mastery.**

Not by solving 500 LeetCode problems.

By practicing 20 fundamental patterns until they're breathing knowledge.

Then applying them to those 100-120 problems in your 8-week sprint.

---

**Ready to start?** Pick your first pattern and do your first kata right now. Set a
timer. Code from memory. This is how you become exceptional.

🥋
