# Grimoire Scripts

Helper scripts for progress tracking and workflow automation.

## Setup

### Configure Git Workflow

Run once to set up git aliases and progress tracking:

```bash
./scripts/setup-git-workflow.sh
```

This adds global git aliases:
- `git today` - See today's commits
- `git week` - See this week's commits
- `git study` - Study commits only
- `git dsa` - DSA commits only
- `git sys` - Systems commits only
- `git last` - Last commit details

## Progress Reports

### Weekly Report

View your progress for the past week:

```bash
./scripts/weekly-report.sh
```

Shows:
- Commit counts by type (DSA, Systems, etc.)
- This week's work log
- Topics covered

**Run every Sunday for weekly review.**

### Sprint Report

View your 8-week sprint progress:

```bash
# Default: assumes sprint started 2024-12-20
./scripts/sprint-report.sh

# Custom start date:
./scripts/sprint-report.sh 2024-12-15
```

Shows:
- Days/weeks elapsed
- Total DSA and Systems commits
- Estimated progress toward targets
- Pace check
- Recent work

**Run weekly to track sprint progress.**

## Usage Examples

```bash
# Setup (run once)
./scripts/setup-git-workflow.sh

# Daily: check today's work
git today

# Weekly: Sunday review
./scripts/weekly-report.sh

# Sprint check (any time)
./scripts/sprint-report.sh 2024-12-20
```

## Notes

All scripts are designed to:
- Work cross-platform (macOS and Linux)
- Require no additional dependencies
- Run quickly (<1 second)
- Not interfere with your workflow

See `docs/GIT_WORKFLOW.md` for detailed git workflow documentation.
