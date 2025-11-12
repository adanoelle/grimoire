---
name: progress-sprint
description: Shows 8-week sprint progress with targets and pace analysis. Use when user asks "am I on track?", "how's my sprint?", or needs overall progress assessment. Provides estimated problems solved and target comparison.
---

# Sprint Progress Tracker

This skill shows overall progress for the 8-week interview sprint.

## When to Use

Use this skill when:
- User asks "am I on track?" or "how's my sprint going?"
- User needs motivation (show progress made!)
- Checking if pace adjustment needed
- Weekly or bi-weekly sprint check-ins

## What It Does

Runs the sprint report script with the sprint start date:

```bash
./scripts/sprint-report.sh 2024-12-20  # Adjust to actual start date
```

Shows:
1. Days/weeks elapsed in sprint
2. Total commits (DSA and Systems)
3. Estimated problems solved
4. Pace vs target (ahead/behind/on-track)
5. Projected final count
6. Recent work summary

## Sprint Targets

**8-week goals:**
- **DSA**: 100-120 problems (120 commits ~= 2-3 problems each)
- **Systems**: 15-20 designs/concepts (20 commits)
- **Total**: ~140 study commits over 56 days

**Weekly pace:**
- Week 1-2: ~15 commits/week (foundations)
- Week 3-4: ~18 commits/week (pattern recognition)
- Week 5-6: ~20 commits/week (advanced topics)
- Week 7-8: ~15 commits/week (mock interviews, review)

## Pace Assessment

The skill calculates:
- Expected progress at current week
- Actual progress
- Percentage of target (ahead/behind)
- Projection to end of sprint

Examples:
- "At this rate: ~140 problems by week 8 (17% ahead of target!)"
- "You're at 70% of target - need to increase pace or adjust goals"

## Notes

- Sprint start date must be accurate (hardcoded in script or passed as arg)
- Uses commit count as proxy for problems (rough estimate)
- Encourages user to update READMEs with actual problem counts
- Provides motivation and course correction
