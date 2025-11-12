---
name: progress-today
description: Shows today's git commits and study progress. Use when user asks to check in, see today's work, or track daily progress. Provides commit counts, topics covered, and time estimates.
---

# Today's Progress Tracker

This skill shows what work has been completed today by analyzing git commits.

## When to Use

Use this skill when:
- User says "check in" or "what have I done today?"
- Tracking daily progress
- User asks about today's commits or work
- grimoire-keeper agent needs daily metrics

## What It Does

1. Shows all commits from today
2. Counts DSA (cantrips) and Systems (incantations) commits separately
3. Estimates time spent based on commit count
4. Provides assessment vs daily targets

## How to Use

Simply invoke this skill when checking daily progress. The skill will:

```bash
# Get today's commits
git log --oneline --since="1 day ago" --no-merges

# Count DSA commits
git log --oneline --since="1 day ago" --grep="cantrips" --no-merges | wc -l

# Count systems commits
git log --oneline --since="1 day ago" --grep="incantations" --no-merges | wc -l
```

## Output Format

Present the information like:
```
📊 Today's Progress (Dec 23):

DSA: 2 commits
- cantrips(arrays): two-sum, container-water
- cantrips(strings): valid-palindrome

Systems: 1 commit
- incantations(fundamentals): lru-cache

Total: 3 commits ✅ (target: 2-4 per day)
Time estimate: ~5 hours

Status: On track!
```

## Target Assessment

- 0 commits: ⚠️ Just starting or blocked?
- 1-2 commits: ✅ Good progress
- 3-4 commits: ✅ Excellent (target hit)
- 5+ commits: ✅ Outstanding pace

## Notes

- Each commit typically represents 45-90 minutes of work
- 2-4 commits = 3-6 hours (target study time)
- Commits should follow convention: `cantrips(topic):` or `incantations(type):`
