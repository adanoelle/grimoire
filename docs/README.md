# Grimoire Documentation

Quick guide to all documentation files.

## 🚀 Quick Start

**New to grimoire?** Start here in order:

1. **[CHEATSHEET.md](CHEATSHEET.md)** ⭐ - Print this! Daily quick reference
2. **[INTERVIEW_SPRINT.md](INTERVIEW_SPRINT.md)** - 8-week sprint overview
3. **[DAILY_WORKFLOW.md](DAILY_WORKFLOW.md)** - Detailed daily guide
4. **[GIT_WORKFLOW.md](GIT_WORKFLOW.md)** - Git progress tracking

Then reference as needed:
- **[SYSTEMS_DESIGN_GUIDE.md](SYSTEMS_DESIGN_GUIDE.md)** - Systems concepts
- **[HYPOTHESIS_GUIDE.md](HYPOTHESIS_GUIDE.md)** - Property testing

## 📋 Documentation Index

### Essential (Read First)

| File | Purpose | When to Read |
|------|---------|--------------|
| **[CHEATSHEET.md](CHEATSHEET.md)** | Daily quick reference | Print and keep visible |
| **[INTERVIEW_SPRINT.md](INTERVIEW_SPRINT.md)** | 8-week plan overview | Before starting sprint |
| **[DAILY_WORKFLOW.md](DAILY_WORKFLOW.md)** | Hour-by-hour daily guide | Day 1, then reference |
| **[GIT_WORKFLOW.md](GIT_WORKFLOW.md)** | Git for tracking progress | Setup day, then reference |

### Reference Guides

| File | Purpose | When to Use |
|------|---------|-------------|
| **[SYSTEMS_DESIGN_GUIDE.md](SYSTEMS_DESIGN_GUIDE.md)** | Complete systems design reference | During systems study |
| **[HYPOTHESIS_GUIDE.md](HYPOTHESIS_GUIDE.md)** | Property-based testing guide | When adding tests (optional) |
| **[DAILY_RITUAL.md](DAILY_RITUAL.md)** | Alternative workflows | If you want different structure |

### Templates

| File | Purpose |
|------|---------|
| **[templates/cantrip.py](templates/cantrip.py)** | LeetCode solution template |
| **[templates/fundamental.py](templates/fundamental.py)** | Systems concept template |
| **[templates/design.py](templates/design.py)** | System design template |
| **[templates/structure.md](templates/structure.md)** | Data structure template |
| **[templates/algorithm.md](templates/algorithm.md)** | Algorithm template |
| **[templates/topic.md](templates/topic.md)** | Topic progress template |

## 🎯 What to Read When

### Day 0 (Setup)
1. Read [INTERVIEW_SPRINT.md](INTERVIEW_SPRINT.md) - Understand the plan
2. Run `./scripts/setup-git-workflow.sh` - Configure git
3. Read [CHEATSHEET.md](CHEATSHEET.md) - Know your daily flow
4. Print CHEATSHEET.md and keep visible

### Day 1 (First Study Day)
1. Reference [CHEATSHEET.md](CHEATSHEET.md) for schedule
2. Invoke session-starter
3. Follow morning/afternoon blocks
4. Use [DAILY_WORKFLOW.md](DAILY_WORKFLOW.md) for details

### During Sprint (Ongoing)
- **Daily**: Glance at [CHEATSHEET.md](CHEATSHEET.md)
- **DSA Problems**: Use [templates/cantrip.py](templates/cantrip.py)
- **Systems Work**: Reference [SYSTEMS_DESIGN_GUIDE.md](SYSTEMS_DESIGN_GUIDE.md)
- **Commit Messages**: Follow [GIT_WORKFLOW.md](GIT_WORKFLOW.md)

### Weekly Review (Sundays)
1. Run `./scripts/weekly-report.sh`
2. Review [INTERVIEW_SPRINT.md](INTERVIEW_SPRINT.md) - Am I on track?
3. Adjust next week's focus

## 🔧 Quick Commands

```bash
# Setup (run once)
./scripts/setup-git-workflow.sh

# Daily workflow
cd ~/grimoire
# Then: "Start my study session"

# Check progress
git today                    # Today's work
git week                     # This week
./scripts/weekly-report.sh   # Weekly summary
./scripts/sprint-report.sh   # Sprint progress

# Templates
cp docs/templates/cantrip.py packages/cantrips/src/cantrips/[topic]/[name].py
cp docs/templates/fundamental.py packages/incantations/src/incantations/fundamentals/[name].py
cp docs/templates/design.py packages/incantations/src/incantations/designs/[name].py
```

## 🤖 Agent Reference

| Agent | When | Command |
|-------|------|---------|
| **session-starter** | Start of day | `"Start my study session"` |
| **grimoire-keeper** | Check-ins (any time) | `"Check in"` or `"What have I done today?"` |
| **study-partner** | Stuck on DSA >20 min | `"Invoke study-partner - stuck on [problem]"` |
| **systems-sage** | Systems design work | `"Invoke systems-sage - design [system]"` |
| **testing-sage** | Adding property tests | `"Invoke testing-sage for [problem]"` |

## 📊 Progress Tracking

### Git Aliases (Already Configured)
- `git today` - Today's commits
- `git week` - This week's commits
- `git study` - Study commits only
- `git dsa` - DSA commits only
- `git sys` - Systems commits only

### Reports
- `./scripts/weekly-report.sh` - Weekly summary
- `./scripts/sprint-report.sh [DATE]` - Sprint progress

### Manual Tracking
- `packages/cantrips/README.md` - DSA progress dashboard
- `packages/incantations/README.md` - Systems progress dashboard
- `PROGRESS.md` (optional) - Personal notes

## 🎓 Learning Path

### Week 1-2: Foundations
- **DSA**: Arrays, Strings, Hashing (25-30 problems)
- **Systems**: Scaling, Caching, Databases (3-5 fundamentals)

### Week 3-4: Pattern Recognition
- **DSA**: Linked Lists, Stacks, Queues, Trees (25-30 problems)
- **Systems**: First designs (URL shortener, Pastebin, Rate limiter, KV store)

### Week 5-6: Advanced Topics
- **DSA**: Binary Search, DFS/BFS, Heaps, DP (30-35 problems)
- **Systems**: Complex designs (Twitter, Instagram, Uber, YouTube, Chat, Crawler)

### Week 7-8: Interview Simulation
- **DSA**: Mock interviews, weak areas (20-25 problems)
- **Systems**: Timed designs, practice explaining (8-10 designs)

## 📚 External Resources Referenced

- **Books**: "System Design Interview" by Alex Xu, "DDIA" by Kleppmann
- **Videos**: ByteByteGo (YouTube)
- **Courses**: Educative "Grokking System Design"
- **Practice**: LeetCode, Pramp (mocks)
- **Blogs**: Netflix, Uber, Twitter, Instagram engineering blogs

## 🔮 Remember

**The grimoire grows through consistent practice.**

- Focus on TODAY's work
- Trust the process
- Rest is part of learning
- Commit often, track progress
- Use agents for guidance

**Start now:**
```
"Start my study session"
```

---

*For project overview and context, see [CLAUDE.md](../CLAUDE.md) at repo root.*
