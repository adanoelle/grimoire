# Automatic Correlation Tracking with kata-master

> Zero-friction accountability for your kata practice and LeetCode progress

## How It Works

The **kata-master** agent automatically tracks the correlation between your kata practice and LeetCode problem-solving, updating your correlation guide without any manual work from you.

## Usage

### Option 1: After Solving a LeetCode Problem

**Just tell kata-master:**
```
You: I just solved Binary Search #704

Agent: ✅ Binary Search #704 marked as complete!

Progress update:
- Binary Search: 1/5 problems (20%) ✅ FIRST ONE!
- You've now used Binary Search in a real cantrip!
- Pattern status updated in correlation guide

Kata practice correlation:
- You've done 0 binary search kata reps
- ⚠️  Recommend: Practice kata 10 times to build muscle memory
- Next kata session: just kata-practice binary_search

Next recommended problem:
- Search Insert Position (#35)
```

**What happens automatically:**
1. Reads `docs/KATA_CANTRIP_CORRELATION.md`
2. Marks Binary Search #704 as [x] complete
3. Updates pattern progress: 0/5 → 1/5 (20%)
4. Updates mastery checklist if it's your first time using the pattern
5. Updates "Last Updated" timestamp
6. Recommends next action

### Option 2: During Kata Session

**When reporting kata results:**
```
You: /kata session
You: binary search
You: Done! 1:48, all tests passed

Agent: LOGGED ✓
New best: 1:48
Attempt 1/100

Correlation update:
- You haven't used Binary Search in LeetCode yet
- ⚠️  Next step: Solve Binary Search #704 to apply this pattern
- Ready to tackle it? The kata warmup will help!
```

**What happens automatically:**
1. Logs your kata attempt in the practice log
2. Checks if you've used this pattern in any cantrips
3. If not used yet: Recommends the first problem to try
4. If already used: Shows how kata practice improves LeetCode performance

### Option 3: Weekly Correlation Report

**Check overall progress:**
```
You: /kata report

Agent: WEEKLY CORRELATION REPORT

Kata practice:
- 6 sessions this week
- Binary Search: 10 kata attempts (all clean!)
- Two Pointers: 8 kata attempts

LeetCode performance:
(Auto-reading your recent commits...)
- Binary Search: 2 problems solved (#704, #35)
- Two Pointers: 3 problems solved

Correlation:
✅ Binary Search: 10 katas → 2 problems (strong correlation!)
✅ Two Pointers: 8 katas → 3 problems (great work!)

Updated correlation guide with latest progress!
```

**What happens automatically:**
1. Reads recent git commits from cantrips
2. Counts kata practice from logs
3. Correlates patterns practiced with patterns used
4. Updates correlation guide with new data
5. Provides insights and recommendations

## What Gets Updated Automatically

**In `docs/KATA_CANTRIP_CORRELATION.md`:**

✅ Problem completion checkboxes: `[ ]` → `[x]`
✅ Pattern progress counts: `0/5` → `1/5`
✅ Percentages: `(0%)` → `(20%)`
✅ Mastery checklist items
✅ "Last Updated" timestamp
✅ Binary search rep count
✅ Pattern usage in "Quick Reference" table

**You never need to edit this file manually!**

## Triggering Updates

### Automatic Triggers
- Saying "I solved [problem]"
- Saying "I completed [problem]"
- Running `/kata report` (updates from git commits)
- Completing a kata session

### Manual Triggers
- Saying "Update my correlation guide"
- Saying "Check my pattern progress"
- Asking "What should I solve next?"

## Example Workflows

### Workflow 1: Morning Practice

```bash
# 1. Kata warmup
/kata session
# Pick binary search, practice 3 times

# Agent automatically:
# - Logs your attempts
# - Checks LeetCode correlation
# - Recommends: "Ready to apply this in Binary Search #704?"

# 2. Solve LeetCode
/ritual
# Work on Binary Search #704

# 3. Report completion
"I just solved Binary Search #704"

# Agent automatically:
# - Updates correlation guide
# - Marks problem complete
# - Updates pattern progress
# - Recommends next problem: Search Insert Position #35
```

### Workflow 2: Evening Reinforcement

```bash
# After solving problems during the day:
"I solved 3 problems today: #704, #35, and #141"

# Agent automatically:
# - Updates all 3 in correlation guide
# - Shows pattern breakdown:
#   - Binary Search: 2 problems (40%)
#   - Fast/Slow Pointers: 1 problem (25%)
# - Updates mastery checklists
# - Recommends evening kata practice for these patterns
```

### Workflow 3: Weekly Review

```bash
# Sunday evening:
/kata report

# Agent automatically:
# - Scans git commits from the past week
# - Updates correlation guide with any missed problems
# - Shows weekly correlation
# - Recommends next week's focus patterns
```

## Benefits

### Zero Friction
- No manual editing of markdown files
- No manual counting of problems
- No manual percentage calculations
- Just focus on learning!

### Accurate Tracking
- Agent reads from single source of truth (git commits)
- Counts kata attempts from practice logs
- Correlates automatically
- No human error

### Actionable Insights
- "You practiced binary search 10 times but haven't solved a problem yet"
- "Sliding window needs more kata practice (only 2 attempts)"
- "Strong correlation: 8 two-pointer katas → 3 LeetCode problems"

### Accountability
- Agent holds you accountable to patterns you haven't practiced
- Celebrates when you close gaps
- Shows data-driven correlation between practice and success

## Quick Reference Commands

```bash
# Start kata session (auto-tracks)
/kata session

# Report problem completion (auto-updates correlation guide)
"I just solved Binary Search #704"

# Weekly report (auto-updates from git commits)
/kata report

# Manual update if needed
"Update my correlation guide"

# Check pattern status
"How am I doing on Binary Search?"

# Get next recommendation
"What should I solve next?"
```

## Tips for Maximum Benefit

1. **Report immediately after solving**: Tell kata-master right away so it can update and recommend the next problem

2. **Use /kata before /ritual**: Kata warmup → LeetCode problem → Report completion = Full correlation tracking

3. **Check weekly reports**: Sunday `/kata report` shows overall correlation and recommends focus areas

4. **Trust the agent**: It's reading from git commits, so it knows your actual progress

5. **Focus on correlation**: If kata practice is high but LeetCode problems are low (or vice versa), the agent will catch it

---

**The result: You practice katas, solve problems, and kata-master handles all the tracking, correlation, and accountability automatically!** 🥋
