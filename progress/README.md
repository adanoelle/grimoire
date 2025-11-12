# Progress Reports

This directory contains automatically generated and manual progress reports for the grimoire interview preparation sprint.

## Directory Structure

```
progress/
├── weekly/          # Weekly progress reports (auto-generated)
│   ├── 2024-W46.md
│   ├── 2024-W47.md
│   └── ...
└── daily/           # Optional daily check-ins (manual)
    ├── 2024-11-12.md
    └── ...
```

## Weekly Reports (Auto-Generated)

Every **Sunday at 8:00 PM**, a GitHub Action automatically:
1. Runs `./scripts/weekly-report.sh`
2. Saves the report to `weekly/YYYY-WWW.md`
3. Creates a GitHub issue with the report
4. Commits the report file to the repo

### Report Contents

Each weekly report includes:
- Total commits this week (DSA vs Systems breakdown)
- All problems/concepts completed
- Topics covered
- Assessment vs weekly targets:
  - DSA: 10-15 commits (20-30 problems)
  - Systems: 4-6 commits
  - Total: 14-21 commits
  - Days active: 6-7 days
- Motivational message

### Viewing Reports

**In the repo:**
```bash
# Latest week
cat progress/weekly/$(ls -t progress/weekly/ | head -1)

# Specific week
cat progress/weekly/2024-W46.md

# All weeks
ls -lh progress/weekly/
```

**On GitHub:**
- Check the [Issues tab](../../issues) for reports labeled `progress-tracker`
- Browse this directory: [`progress/weekly/`](./weekly/)

## Daily Check-Ins (Optional/Manual)

The `daily/` directory is available for manual progress notes. Not auto-generated.

**How to use:**
```bash
# Quick check-in
just check-in > progress/daily/$(date +%Y-%m-%d).md

# Or manually create
echo "# $(date +%Y-%m-%d) Progress" > progress/daily/$(date +%Y-%m-%d).md
echo "" >> progress/daily/$(date +%Y-%m-%d).md
git today >> progress/daily/$(date +%Y-%m-%d).md
```

## Why Track Progress?

### Accountability
- Weekly GitHub issues create a public commitment
- Historical record shows consistency

### Motivation
- See how far you've come
- Celebrate wins (hitting targets, streaks)
- Identify patterns (which topics are you crushing?)

### Interview Prep
- When you interview: "I solved 120 problems over 8 weeks"
- Show the GitHub issues as proof of consistent work
- Demonstrates discipline and organization

### Reflection
- Weekly reviews help internalize patterns
- Identify what's working vs what's not
- Adjust pace if needed

## Manual Triggering

You can manually trigger a weekly report anytime:

**Via GitHub UI:**
1. Go to [Actions tab](../../actions)
2. Select "Weekly Progress Report"
3. Click "Run workflow"

**Via CLI (requires GitHub CLI):**
```bash
gh workflow run weekly-progress.yml
```

## Sprint Targets Reminder

**8-week goals (from INTERVIEW_SPRINT.md):**
- DSA: 100-120 problems (~120 commits)
- Systems: 15-20 designs/concepts (~20 commits)
- Total: ~140 study commits over 56 days

**Weekly pace:**
- Week 1-2: ~15 commits/week (foundations)
- Week 3-4: ~18 commits/week (pattern recognition)
- Week 5-6: ~20 commits/week (advanced topics)
- Week 7-8: ~15 commits/week (mock interviews, review)

**Daily pace:**
- 2-4 commits per day (3-6 hours study time)
- Consistency > intensity

---

🔮 **The grimoire grows with every commit. Trust the process.**
