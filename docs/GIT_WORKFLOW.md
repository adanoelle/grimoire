# Git Workflow for Grimoire Study Tracking

Using git commits as your primary progress tracking system - simple, effective, no extra tools.

## Philosophy

**Git as study journal:**
- Each commit = session or milestone
- Commit messages = what you learned
- Git log = progress tracker
- Branches (optional) = focus areas
- No separate tracking tool needed

**Keep it simple:**
- Commit often (2-4x per day)
- Good messages > perfect messages
- Hooks are optional helpers, not requirements

---

## Commit Message Convention

### Format

```
<type>(<scope>): <subject>

[optional body]
```

### Types for Grimoire

**cantrips**: LeetCode problem solutions
**incantations**: Systems design work
**runes**: Data structure implementations
**docs**: Documentation updates
**chore**: Maintenance (templates, config)

### Scopes (Topic Areas)

**For cantrips:**
- `arrays`, `strings`, `hashing`, `linked-lists`, `stacks`, `queues`, `trees`, `graphs`, `heaps`, `dp`, `greedy`

**For incantations:**
- `fundamentals`, `designs`, `patterns`

### Subject Line

**Be specific and informative:**

✅ Good:
```
cantrips(arrays): two-sum, container-water, remove-duplicates [two-pointers]
incantations(designs): url-shortener with base62 encoding and caching
incantations(fundamentals): lru-cache with OrderedDict and doubly-linked list
cantrips(trees): revisited serialize-tree, now understand BFS approach
runes(structures): implemented doubly-linked-list with insert/delete
```

❌ Bad:
```
solved problems
updated files
did some work
finished coding
```

### Optional Body (for significant work)

```
cantrips(arrays): three-sum, four-sum

Struggled with three-sum for 45 min, finally understood the pattern:
- Sort first
- Fix one element, use two pointers for rest
- Skip duplicates carefully

Four-sum was easier after understanding three-sum pattern.
Time complexity: O(n²) for three-sum, O(n³) for four-sum.

Pattern: Reducing K-sum to (K-1)-sum problem.
```

---

## Git Aliases for Speed

Add these to `~/.gitconfig` or run commands to set them up:

```bash
# Add aliases
git config --global alias.today "log --oneline --since='1 day ago'"
git config --global alias.week "log --oneline --since='1 week ago' --no-merges"
git config --global alias.study "log --oneline --grep='cantrips\\|incantations' --since='1 week ago'"
git config --global alias.dsa "log --oneline --grep='cantrips' --since='1 week ago'"
git config --global alias.sys "log --oneline --grep='incantations' --since='1 week ago'"
git config --global alias.last "log -1 --stat"
```

### Usage

```bash
# What did I do today?
git today

# What did I do this week?
git week

# Show only study commits (not docs/chore)
git study

# DSA problems only
git dsa

# Systems design only
git sys

# Last commit details
git last

# Count this week's commits
git week | wc -l
```

---

## Git Hooks for Progress Tracking

**Optional but helpful** - hooks run automatically at certain git events.

### Setup Hooks

Create `.git/hooks/` scripts (already exists in repo):

```bash
# Make hooks executable
chmod +x .git/hooks/post-commit
chmod +x .git/hooks/pre-push
```

### Hook 1: Post-Commit Progress (Optional)

Automatically shows your progress after each commit.

**Create `.git/hooks/post-commit`:**

```bash
#!/bin/bash
# Post-commit hook: Show progress after each commit

# Get commit message
COMMIT_MSG=$(git log -1 --pretty=%B)

# If it's a study commit (cantrips or incantations), show stats
if echo "$COMMIT_MSG" | grep -qE "cantrips|incantations"; then
    echo ""
    echo "📊 Study Progress Update:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    # Count this week's study commits
    DSA_COUNT=$(git log --oneline --since="1 week ago" --grep="cantrips" --no-merges | wc -l | tr -d ' ')
    SYS_COUNT=$(git log --oneline --since="1 week ago" --grep="incantations" --no-merges | wc -l | tr -d ' ')
    TOTAL_COUNT=$((DSA_COUNT + SYS_COUNT))

    echo "This week: $TOTAL_COUNT study commits ($DSA_COUNT DSA, $SYS_COUNT Systems)"

    # Show today's commits
    echo ""
    echo "Today's work:"
    git log --oneline --since="1 day ago" --no-merges | head -5
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
fi
```

**What it does:**
- Runs after every `git commit`
- Shows weekly DSA/Systems commit counts
- Shows today's commits
- Only triggers for study commits (not docs/chore)

### Hook 2: Weekly Reminder (Optional)

Reminds you to review progress on Sundays.

**Create `.git/hooks/pre-commit`:**

```bash
#!/bin/bash
# Pre-commit hook: Weekly review reminder

# Check if it's Sunday
if [ "$(date +%u)" -eq 7 ]; then
    # Check if this is first commit today
    TODAY_COMMITS=$(git log --oneline --since="1 day ago" --no-merges | wc -l | tr -d ' ')

    if [ "$TODAY_COMMITS" -eq 0 ]; then
        echo ""
        echo "🔮 Sunday Review Reminder:"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "Before you start, consider reviewing the week:"
        echo "  - git week           # See all commits"
        echo "  - git dsa            # DSA work"
        echo "  - git sys            # Systems work"
        echo ""
        echo "Update PROGRESS.md with weekly summary!"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
    fi
fi

# Continue with commit
exit 0
```

**What it does:**
- Runs before first Sunday commit
- Reminds you to review the week
- Doesn't block the commit

### Hook 3: Commit Message Validation (Optional)

Ensures your commit messages follow convention.

**Create `.git/hooks/commit-msg`:**

```bash
#!/bin/bash
# Commit message validation

COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

# Allow merge commits
if echo "$COMMIT_MSG" | grep -q "^Merge"; then
    exit 0
fi

# Check format: type(scope): subject
if ! echo "$COMMIT_MSG" | grep -qE "^(cantrips|incantations|runes|docs|chore)(\([a-z-]+\))?: .+"; then
    echo "❌ Invalid commit message format!"
    echo ""
    echo "Expected: <type>(<scope>): <subject>"
    echo ""
    echo "Examples:"
    echo "  cantrips(arrays): two-sum, container-water"
    echo "  incantations(designs): url-shortener"
    echo "  docs: updated daily workflow"
    echo ""
    echo "Types: cantrips, incantations, runes, docs, chore"
    echo ""
    exit 1
fi

exit 0
```

**What it does:**
- Validates commit message format
- Rejects commits with bad messages
- Helps maintain consistent history

**To disable temporarily:**
```bash
git commit --no-verify -m "your message"
```

---

## Progress Tracking Commands

### Daily Check-in

```bash
# Morning: What did I do yesterday?
git today

# Last commit details
git last
```

### Weekly Review

```bash
# All work this week
git week

# Study commits only
git study

# DSA vs Systems breakdown
echo "DSA: $(git dsa | wc -l) commits"
echo "Systems: $(git sys | wc -l) commits"

# Visual weekly summary
git log --oneline --since="1 week ago" --no-merges --pretty=format:"%s" | sort
```

### Sprint Progress (8 weeks)

```bash
# Total commits since sprint start (adjust date)
git log --oneline --since="2024-12-20" --no-merges | wc -l

# Study commits breakdown
git log --oneline --since="2024-12-20" --grep="cantrips" --no-merges | wc -l
git log --oneline --since="2024-12-20" --grep="incantations" --no-merges | wc -l

# Commits per week (visual)
git log --oneline --since="8 weeks ago" --format="%ad" --date=format:"%Y-W%U" | sort | uniq -c
```

### Topic-Specific Progress

```bash
# All array problems
git log --oneline --grep="cantrips(arrays)" --no-merges

# All system designs
git log --oneline --grep="incantations(designs)" --no-merges

# Specific pattern (two-pointers)
git log --oneline --grep="two-pointers" --no-merges
```

---

## Branching Strategy (Optional)

**For sprint: Stay on `main`**
- Simple, fast, no overhead
- Commit directly to main
- Good enough for solo work

**After sprint: Consider branches for focus areas**

```bash
# Create branch for specific topic
git checkout -b trees-and-graphs
# Work on tree problems for a few days
# Merge back when done
git checkout main
git merge trees-and-graphs
```

**When to branch:**
- Experimenting with alternative approach
- Working on complex system design over multiple days
- Want to keep main "clean" for some reason

**For now: Don't branch.** Stay simple.

---

## Progress Visualization

### Simple Weekly Report

Create this bash script: `scripts/weekly-report.sh`

```bash
#!/bin/bash
# Weekly progress report

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 GRIMOIRE WEEKLY REPORT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Date range
START_DATE=$(date -v-7d +"%Y-%m-%d")
END_DATE=$(date +"%Y-%m-%d")
echo "📅 Week: $START_DATE to $END_DATE"
echo ""

# Commit counts
TOTAL=$(git log --oneline --since="1 week ago" --no-merges | wc -l | tr -d ' ')
DSA=$(git log --oneline --since="1 week ago" --grep="cantrips" --no-merges | wc -l | tr -d ' ')
SYSTEMS=$(git log --oneline --since="1 week ago" --grep="incantations" --no-merges | wc -l | tr -d ' ')
RUNES=$(git log --oneline --since="1 week ago" --grep="runes" --no-merges | wc -l | tr -d ' ')

echo "📈 Commits:"
echo "   Total: $TOTAL"
echo "   DSA (cantrips): $DSA"
echo "   Systems (incantations): $SYSTEMS"
echo "   Foundations (runes): $RUNES"
echo ""

# Work log
echo "📝 This week's work:"
git log --oneline --since="1 week ago" --no-merges --grep="cantrips\|incantations" | head -15
echo ""

# Topics covered
echo "🎯 Topics:"
git log --oneline --since="1 week ago" --no-merges | grep -oE "\([a-z-]+\)" | sort | uniq -c | sort -rn
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔮 Keep building your grimoire!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
```

Make it executable:
```bash
chmod +x scripts/weekly-report.sh
```

Run it:
```bash
./scripts/weekly-report.sh
```

### Sprint Progress Report

Create: `scripts/sprint-report.sh`

```bash
#!/bin/bash
# Full sprint progress report

SPRINT_START="2024-12-20"  # Adjust to your start date

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 GRIMOIRE 8-WEEK SPRINT REPORT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Calculate weeks elapsed
START_EPOCH=$(date -j -f "%Y-%m-%d" "$SPRINT_START" +%s)
NOW_EPOCH=$(date +%s)
DAYS_ELAPSED=$(( (NOW_EPOCH - START_EPOCH) / 86400 ))
WEEKS_ELAPSED=$(( DAYS_ELAPSED / 7 ))
echo "📅 Sprint Day: $DAYS_ELAPSED/56 (Week $WEEKS_ELAPSED/8)"
echo ""

# Total counts
TOTAL=$(git log --oneline --since="$SPRINT_START" --no-merges | wc -l | tr -d ' ')
DSA=$(git log --oneline --since="$SPRINT_START" --grep="cantrips" --no-merges | wc -l | tr -d ' ')
SYSTEMS=$(git log --oneline --since="$SPRINT_START" --grep="incantations" --no-merges | wc -l | tr -d ' ')

echo "📈 Total Progress:"
echo "   Commits: $TOTAL"
echo "   DSA Problems: ~$DSA sessions"
echo "   Systems Work: ~$SYSTEMS sessions"
echo ""

# Target tracking
DSA_TARGET=120
SYSTEMS_TARGET=20
DSA_PROGRESS=$(( DSA * 100 / DSA_TARGET ))
SYS_PROGRESS=$(( SYSTEMS * 100 / SYSTEMS_TARGET ))

echo "🎯 Target Progress:"
echo "   DSA: $DSA_PROGRESS% ($DSA / $DSA_TARGET estimated problems)"
echo "   Systems: $SYS_PROGRESS% ($SYSTEMS / $SYSTEMS_TARGET estimated designs)"
echo ""

# Weekly breakdown
echo "📊 Weekly Breakdown:"
for week in {1..8}; do
    WEEK_START=$(date -v-"$((56 - week*7))d" -v+1d +"%Y-%m-%d")
    WEEK_END=$(date -v-"$((56 - week*7 - 6))d" +"%Y-%m-%d")
    WEEK_COMMITS=$(git log --oneline --since="$WEEK_START" --until="$WEEK_END" --no-merges --grep="cantrips\|incantations" | wc -l | tr -d ' ')

    if [ $week -le $WEEKS_ELAPSED ]; then
        echo "   Week $week: $WEEK_COMMITS commits"
    else
        echo "   Week $week: (upcoming)"
    fi
done
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔮 The grimoire grows stronger every day!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
```

---

## Commit Workflow Examples

### Morning DSA Session

```bash
# After solving 2-3 problems
git add packages/cantrips/src/cantrips/arrays/
git status  # Review what's being committed

git commit -m "cantrips(arrays): two-sum-ii, container-water, remove-duplicates

Practiced two-pointers pattern:
- two-sum-ii: Opposite ends, move based on sum
- container-water: Greedy - always move shorter side
- remove-duplicates: In-place modification

Pattern clicking: Two pointers great for sorted arrays."

# Hook shows progress automatically
```

### Afternoon Systems Session

```bash
# After implementing concept
git add packages/incantations/src/incantations/fundamentals/
git status

git commit -m "incantations(fundamentals): lru-cache with OrderedDict

Implemented LRU cache using Python's OrderedDict:
- get(): O(1) - move_to_end for LRU ordering
- put(): O(1) - automatic eviction via popitem

Also sketched doubly-linked list + hashmap approach.
Understanding how Redis uses this internally."

# Hook shows progress
```

### Design Session

```bash
git add packages/incantations/src/incantations/designs/
git commit -m "incantations(designs): url-shortener with estimation and caching

Completed full design:
- Estimation: 10B requests/month = ~4K QPS
- Base62 encoding for short codes
- Redis cache for hot URLs (80/20 rule)
- PostgreSQL for persistence
- Sharding strategy: hash(short_code)

Practiced with systems-sage - understood trade-offs between
random generation vs sequential counter approaches."
```

### End of Day

```bash
# Review your work
git today

# Update progress notes (optional)
git add PROGRESS.md
git commit -m "docs: updated week 1 progress notes"
```

---

## .gitignore for Grimoire

Ensure these are ignored:

```bash
# Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/
.coverage
htmlcov/

# Virtual environments
venv/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Personal notes (if you want privacy)
# PROGRESS.md
# notes/
```

---

## Best Practices

### DO ✅

- **Commit after each problem** or **each concept studied**
- **Write informative subjects** - future you will thank you
- **Include patterns/lessons** in commit body when relevant
- **Use aliases** for quick progress checks
- **Review `git today`** every evening
- **Review `git week`** every Sunday

### DON'T ❌

- **Don't batch commits** - commit granularly for better tracking
- **Don't use vague messages** - "updated files" tells you nothing
- **Don't commit broken code** - finish the problem/concept first
- **Don't obsess over perfect messages** - good enough is fine
- **Don't commit sensitive info** - no API keys, passwords, etc.
- **Don't forget to push** occasionally (if using remote for backup)

---

## Troubleshooting

### Hook not running?

```bash
# Check if executable
ls -la .git/hooks/post-commit

# Make executable
chmod +x .git/hooks/post-commit
```

### Want to skip hooks temporarily?

```bash
git commit --no-verify -m "your message"
```

### Want to disable a hook?

```bash
# Rename it
mv .git/hooks/post-commit .git/hooks/post-commit.disabled
```

### Aliases not working?

```bash
# Check if they're set
git config --global --get-regexp alias

# Re-add them
git config --global alias.today "log --oneline --since='1 day ago'"
```

---

## Quick Setup Script

Run this to set up everything at once:

```bash
#!/bin/bash
# setup-git-workflow.sh

echo "Setting up grimoire git workflow..."

# Add aliases
git config --global alias.today "log --oneline --since='1 day ago'"
git config --global alias.week "log --oneline --since='1 week ago' --no-merges"
git config --global alias.study "log --oneline --grep='cantrips\\|incantations' --since='1 week ago'"
git config --global alias.dsa "log --oneline --grep='cantrips' --since='1 week ago'"
git config --global alias.sys "log --oneline --grep='incantations' --since='1 week ago'"
git config --global alias.last "log -1 --stat"

echo "✓ Git aliases configured"

# Create scripts directory
mkdir -p scripts

echo "✓ Scripts directory created"

echo ""
echo "Git workflow configured!"
echo ""
echo "Try these commands:"
echo "  git today    # See today's work"
echo "  git week     # See this week"
echo "  git study    # Study commits only"
echo ""
echo "Optional: Add git hooks (see GIT_WORKFLOW.md)"
```

Save and run:
```bash
chmod +x scripts/setup-git-workflow.sh
./scripts/setup-git-workflow.sh
```

---

## Summary

**Git as your study tracker:**
- ✅ Already using it
- ✅ No extra tools
- ✅ Powerful queries
- ✅ Visual history
- ✅ Automatic timestamping
- ✅ Works offline

**Keep it simple:**
- Good commit messages
- Useful aliases
- Optional hooks for automation
- Weekly reviews

**Your commits tell the story of your grimoire's growth.** 🔮

---

## Related Documentation

- `DAILY_WORKFLOW.md` - Daily study structure
- `INTERVIEW_SPRINT.md` - 8-week overview
- `SYSTEMS_DESIGN_GUIDE.md` - Systems reference

---

**Setup now:**
```bash
./scripts/setup-git-workflow.sh
```

**Then check:**
```bash
git today
```
