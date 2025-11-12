---
name: progress-week
description: Shows this week's study progress with detailed stats. Use for weekly reviews, checking pace, or when user asks about weekly progress. Runs the weekly-report.sh script.
---

# Weekly Progress Report

This skill generates a comprehensive weekly progress report using git commits.

## When to Use

Use this skill when:
- User asks for "weekly review" or "how was my week?"
- Sunday review sessions
- Checking weekly pace vs targets
- User asks "am I on track this week?"

## What It Does

Runs the weekly report script which shows:
1. Total commits this week
2. DSA vs Systems breakdown
3. All work completed
4. Topics covered
5. Assessment vs weekly targets

## How to Use

Simply invoke the script:

```bash
./scripts/weekly-report.sh
```

The script handles:
- Date range calculation
- Commit counting and categorization
- Topic extraction
- Formatted output

## Target Assessment

Weekly targets (8-week sprint):
- **DSA**: 10-15 commits (~20-30 problems)
- **Systems**: 4-6 commits (concepts or designs)
- **Total**: 14-21 commits
- **Days**: 6-7 days with commits

## Output Includes

- Commit counts by type
- Full work log
- Topics covered (extracted from commit scopes)
- Motivational message

## Notes

- Best used on Sundays for weekly review
- Helps identify patterns (consistent or sporadic)
- Can reveal topic focus areas
- Useful for adjusting next week's plan
