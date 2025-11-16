# /kata - Algorithm Kata Practice

Invoke the kata-master agent to guide your daily algorithm kata practice, track mastery progression, and correlate practice with LeetCode performance.

## Usage

```bash
/kata                  # Start kata session or check progress
/kata session          # Start guided kata practice
/kata progress         # View mastery levels
/kata report           # Weekly correlation report
/kata milestones       # Check 100-rep goal and achievements
```

## What This Does

The kata-master agent guides you through deliberate practice of core algorithmic patterns:

### 1. **Guided Kata Session**
- Helps pick which pattern to practice today
- Shows your recent attempts and current mastery level
- Times your practice (you report results)
- Records progress in mastery logs
- Tracks improvements (time, bugs, consistency)

### 2. **Mastery Progress Tracking**
- Shows mastery level for each pattern (Learning → Practicing → Mastered)
- Tracks best times and bug counts
- Identifies patterns needing more work
- Celebrates achievements (zero bugs, target times reached)

### 3. **Weekly Correlation Report**
- Reads your kata practice logs
- Reads your LeetCode (cantrips) git commits
- Shows correlation: kata practice → LeetCode success
- Provides data-driven insights

### 4. **Milestone Tracking**
- Binary Search 100 reps goal (most critical!)
- Pattern mastery checkboxes
- Streaks and consistency
- Achievement unlocks

## The Kata Practice Flow

**Morning warmup (5-10 min):**
```
1. /kata session
2. Pick pattern (e.g., two pointers)
3. Code kata from memory (agent guides you)
4. Report time and results
5. Agent logs progress and shows improvement
```

**Evening reinforcement (5 min):**
```
1. /kata session
2. Practice patterns used in today's LeetCode
3. Build muscle memory through repetition
```

## Integration with LeetCode Ritual

**Perfect daily flow:**
```
Morning:
├─ /kata session (5-10 min)
│  └─ Warm up core patterns
│
└─ /ritual (45-60 min)
   └─ Apply patterns in LeetCode problems
```

**Why this works:**
- Fresh muscle memory from kata → easier LeetCode
- Pattern is automatic → more time for edge cases
- Correlation tracking shows what works

## What the Agent Does

- ✅ Guides pattern selection based on your sprint week
- ✅ Shows current mastery levels
- ✅ Records practice attempts with time and bugs
- ✅ Tracks improvements over time
- ✅ Correlates kata practice with LeetCode success
- ✅ **Automatically updates correlation guide** when you solve problems (ZERO friction!)
- ✅ Celebrates milestones (50 reps, zero bugs, etc.)
- ✅ Provides honest feedback on progress
- ✅ Identifies patterns needing more work

### Automatic Correlation Tracking

**Zero-friction accountability:**

When you say "I just solved Binary Search #704" or complete any LeetCode problem:

1. Agent automatically updates `docs/KATA_CANTRIP_CORRELATION.md`
2. Marks problem as complete [x]
3. Updates pattern progress count (e.g., Binary Search: 1/5 → 2/5)
4. Recommends next problem in the pattern
5. Shows correlation with your kata practice

**No manual tracking required!** Just tell kata-master when you solve a problem, and it handles the rest.

## What the Agent Won't Do

- ❌ Code katas for you
- ❌ Give hints during practice
- ❌ Let you skip tracking results
- ❌ Accept inconsistency without pointing it out

## Example Session

```
You: /kata session

Agent: 🥋 KATA PRACTICE SESSION

Recommended today (Week 2):
- Two Pointers (Opposite Ends) - 🟡 Practicing
- Binary Search (Classic) - 🟡 47/100 reps!
- Sliding Window (Fixed) - 🔴 Needs work

Which pattern?

You: binary search

Agent: Binary Search - Kata 1: Classic

Your progress:
- 47 attempts (3 away from milestone 50!)
- Last 10: ALL CLEAN 🔥
- Best time: 1:50 (under target!)

Ready? Type START when you begin coding.

You: START

[Agent waits]

You: Done! 1:48, all tests passed

Agent: LOGGED ✓

New best: 1:48 (2s faster!)
Attempt 48/100
11 clean in a row! 🔥

🎉 Only 2 away from milestone 50!

Practice again or different pattern?
```

## Weekly Report Example

```
You: /kata report

Agent: WEEKLY CORRELATION REPORT

Kata practice:
- 6 sessions this week
- 18 katas attempted
- 15/18 clean (83%)

LeetCode performance:
- 8 problems solved
- Two Pointers: 8 katas → 3 problems ✓
- Binary Search: 6 katas → 2 problems ✓

💡 INSIGHT: Strong correlation! Your kata warmup
is making LeetCode problems smoother.

Sliding Window needs more kata practice.
Add 2 sessions this week.
```

## Philosophy

**Katas are like scales for musicians.**

- Scales (katas) = muscle memory
- Songs (LeetCode) = application
- Practice both = mastery

**10 min/day × 56 days = 560 min of deliberate practice**
= Patterns that feel like breathing

## Quick Commands

- `/kata` - Full menu
- `/kata session` - Start practice
- `/kata progress` - Check mastery
- `/kata report` - Weekly insights
- `/kata milestones` - Track big goals

---

**Build muscle memory. Track progress. Crush interviews.** 🥋
