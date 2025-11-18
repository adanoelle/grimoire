## Algorithm Kata Practice - Daily Ritual

> "Musicians practice scales. Athletes practice drills. Engineers practice
> katas."

This guide explains how to use `runes/algorithms/` kata exercises to build
muscle memory for core algorithmic patterns. This is the **missing piece**
between knowing patterns intellectually and implementing them reflexively in
interviews.

## Philosophy: Scales vs. Songs

**LeetCode problems are "songs"** - complete performances where you apply
patterns in context.

**Algorithm katas are "scales"** - fundamental techniques practiced until
they're muscle memory.

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

**Interactive Menu (Recommended):**

```bash
runes kata menu
# Or via justfile
just kata::menu
```

The menu handles everything:

1. Shows all patterns with practice history
2. Opens kata in your editor with timer
3. Runs tests when you're ready
4. Prompts to log your session
5. Tracks progress automatically

**Manual CLI (Power Users):**

If you prefer direct commands:

```bash
# Step 1: Pick a pattern (30 seconds)
runes kata list

# Step 2: Start practice
runes kata practice sliding-window/fixed-window
# Opens in $EDITOR, timer starts automatically

# Step 3: Code from memory (2-3 minutes)
# - Find KATA 1, delete 'pass', code from memory
# - NO peeking at templates (__init__.py)!

# Step 4: Run tests (10 seconds)
runes kata test sliding-window/fixed-window -k 1
# Or test all katas:
runes kata test sliding-window/fixed-window

# Step 5: Log your session
runes kata log sliding-window/fixed-window 1 2:30 -b 1
# Format: <pattern> <kata-number> <time> -b <bugs>

# Step 6: Reset for next time
runes kata reset sliding-window/fixed-window
# Creates automatic backup, can undo with: runes kata undo
```

**Legacy Justfile Commands (Backwards Compatible):**

```bash
just kata::practice sliding-window/fixed-window  # Opens in Helix
just kata::test sliding-window/fixed-window       # Run pytest
just kata::reset sliding-window/fixed-window      # Reset (Y/n confirm)
```

### Testing with Pytest (Migrated Patterns)

Patterns migrated to pytest use markers for granular test selection:

**Test specific katas:**

```bash
# Just kata 1
runes kata test sliding-window/fixed-window -k 1

# Katas 1 and 2
runes kata test sliding-window/fixed-window -m "kata1 or kata2"

# All katas
runes kata test sliding-window/fixed-window
```

**Test specific categories:**

```bash
# Just LeetCode examples
runes kata test sliding-window/fixed-window -m examples

# Just edge cases
runes kata test sliding-window/fixed-window -m edge
```

**Verbose output (see all test names):**

```bash
runes kata test sliding-window/fixed-window -v -k 1
```

**Available markers:**

- `kata1`, `kata2`, `kata3`, `kata4`, `kata5` - Individual practice problems
- `examples` - LeetCode example test cases
- `edge` - Edge case tests
- `properties` - Property-based tests (if available)

**Why pytest?**

- Granular test selection (practice one kata at a time)
- Better error messages
- Marker-based organization
- Industry standard testing framework

**Migration status:** Check which patterns use pytest: `runes kata list`

- ✅ Green check = pytest
- ⚠️ Yellow warning = legacy doctest

### Safety and Backups

**Automatic backups on reset:**

Every time you reset a kata, a timestamped backup is created:

```bash
runes kata reset sliding-window/fixed-window
# Creates: .kata_backups/sliding-window_fixed-window_20250118_143052.py
```

**Undo last reset:**

```bash
runes kata undo
# Restores most recent backup
```

**Manual backup management:**

```bash
# List all backups
ls -la .kata_backups/

# Restore specific backup manually
cp .kata_backups/sliding-window_fixed-window_20250118_143052.py \
   packages/runes/src/runes/algorithms/sliding_window/fixed_window/kata.py
```

**What's preserved:**

- ✅ Practice logs and session history
- ✅ Mastery checklists
- ✅ Your personal notes in docstrings
- ✅ All test files (never reset)

**What's reset:**

- ❌ Function implementations (back to `pass`)
- ❌ Only in `kata.py`, never touches `__init__.py` templates

**Dry-run mode:**

Preview what would be reset without making changes:

```bash
runes kata reset sliding-window/fixed-window --dry-run
```

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

Code classic binary search **100 times** until you can do it perfectly, with
zero bugs, in under 2 minutes, **with your eyes closed**.

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
MASTERY CHECKLIST: [ ] Kata 1: Can code in < 2 min, zero bugs [ ] Kata 2: Can
code in < 3 min, zero bugs [ ] Kata 3: Can code in < 4 min, zero bugs [ ] Can
explain the pattern while coding [ ] Can identify when to use (< 30 sec
recognition) [ ] Used successfully in 5+ LeetCode problems

BREATHING KNOWLEDGE (Ultimate Goal): [ ] All katas in under 15 minutes total [ ]
Zero bugs across all katas [ ] Can teach this pattern to someone else [ ]
Pattern recognition is automatic
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

**Interactive Menu (Easiest!):**

```bash
runes kata menu
```

Follow the prompts:

1. Choose "Practice Kata"
2. Select a pattern (try `two-pointers/opposite-ends`)
3. Code in your editor (timer runs automatically)
4. Run tests when prompted
5. Log your session

**Manual CLI:**

```bash
# 1. View available patterns
runes kata list

# 2. Pick one pattern to master this week (recommend: two-pointers/opposite-ends)
runes kata practice two-pointers/opposite-ends

# 3. Code from memory, run tests
runes kata test two-pointers/opposite-ends -k 1

# 4. Log your session
runes kata log two-pointers/opposite-ends 1 2:15 -b 0

# 5. Set daily reminders
#    Morning: 7:00 AM - "Kata warmup"
#    Evening: 7:00 PM - "Kata reinforcement"

# 6. Tomorrow: Reset and repeat
runes kata reset two-pointers/opposite-ends
```

**Integration with LeetCode:**

```bash
# Morning workflow
runes kata menu          # 5-10 min warmup
# ... then use /ritual for LeetCode practice

# Evening reinforcement
runes kata menu          # 5 min drill patterns used today
```

**8-week goal:** Walk into Google interview with muscle memory that makes
interviewers say: "This person really knows their stuff."

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

**Ready to start?** Pick your first pattern and do your first kata right now.
Set a timer. Code from memory. This is how you become exceptional.

🥋
