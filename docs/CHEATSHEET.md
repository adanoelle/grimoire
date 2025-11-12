# Grimoire Daily Workflow Cheat Sheet

Quick reference for your daily study routine during the 8-week sprint.

---

## ⏰ Daily Schedule at a Glance

```
08:00 - 08:05   🎯 Start Session (invoke session-starter)
08:05 - 11:00   💻 DSA Block (2-3 LeetCode problems)
11:00 - 14:00   🍽️  Lunch Break (NO STUDYING - rest required!)
14:00 - 17:00   🏗️  Systems Block (concept or design)
17:00 - 20:00   🎮 Free Time (rest, exercise, life)
20:00 - 20:30   📝 Evening Review (set tomorrow's goals)
```

**Total Study Time:** 5-6 hours/day (sustainable pace)

---

## 🤖 Agent Quick Reference

### When to Invoke Each Agent

| Agent | When | Command |
|-------|------|---------|
| **session-starter** | Start of day (once) | `"Start my study session"` |
| **grimoire-keeper** | Check-ins (any time!) | `"Check in"` or `"What have I done today?"` |
| **study-partner** | Stuck on DSA >20 min | `"Invoke study-partner - stuck on [problem]"` |
| **systems-sage** | Starting systems work | `"Invoke systems-sage - design [system]"` |
| **testing-sage** | Adding property tests | `"Invoke testing-sage for [problem]"` |

### Agent Conversation Examples

**grimoire-keeper (check-ins):**
```
"Check in" → Shows today's progress, commit count, assessment
"I finished two-sum" → Structures commit message for you
"Am I on track?" → Shows pace vs targets, sprint progress
"Weekly review" → Runs report, provides analysis
"What should I do now?" → Suggests based on schedule and progress
```

**study-partner:**
```
"I'm stuck on reverse-linked-list. I tried iterative but my pointers are confused."
"I solved container-water O(n²). Is there better? Don't tell me, guide me."
"Help me debug - my BFS is returning wrong level order."
```

**systems-sage:**
```
"Design Instagram. Act as my interviewer."
"Stuck on fanout-on-write vs read for Twitter. Help me reason through it."
"Review my URL shortener design for bottlenecks."
"Help me understand when to use consistent hashing."
```

---

## 🌅 Morning Block: DSA (3 hours)

### Start (5 min)
```
cd ~/grimoire
"Start my study session"
```

### For Each Problem (45-60 min)

**1. Understand (5 min)**
- [ ] Read problem 2x
- [ ] Clarify constraints
- [ ] Work through 2 examples by hand

**2. Plan (5 min)**
- [ ] What pattern is this? (two pointers, sliding window, BFS, etc.)
- [ ] Sketch approach in comments
- [ ] Consider edge cases

**3. Implement (20-30 min)**
```bash
cp docs/templates/cantrip.py packages/cantrips/src/cantrips/[topic]/[name].py
```
- [ ] Write clean code
- [ ] Good variable names
- [ ] Handle edge cases

**4. Test (10 min)**
- [ ] Run test cases
- [ ] Test edge cases manually
- [ ] Fix bugs

**5. Document (10 min)**
- [ ] Fill in "What I Learned"
- [ ] Note pattern used
- [ ] Analyze time/space complexity

### If Stuck >20 Minutes

```
"Invoke study-partner - I'm stuck on [problem]. I've tried [approach] but [issue]."
```

Study-partner will ask questions, not give answers.

### End of Morning

```
# Check in with grimoire-keeper
"I finished my problems, ready to commit"

# Grimoire-keeper will:
# 1. Check git status
# 2. Structure commit message for you
# 3. Give exact command to run
# 4. Show updated progress after commit
```

Or manually:
```bash
git add packages/cantrips/
git commit -m "cantrips(arrays): two-sum, container-water, remove-duplicates"
git today
```

---

## 🍽️ Lunch Break (3 hours)

**CRITICAL: Actually rest!**

- ✅ Eat food
- ✅ Walk outside (20+ min)
- ✅ Rest eyes (no screens)
- ✅ Passive learning OK (one video)
- ❌ NO active problem-solving

Your brain consolidates learning during rest.

---

## 🏗️ Afternoon Block: Systems (2-3 hours)

### Choose Your Focus

**Fundamental Day (Tue/Thu/Sat)** → Study concept + implement
**Design Day (Mon/Wed/Fri)** → Full system design practice

---

### Option A: Fundamental Day

**1. Invoke systems-sage (start)**
```
"I'm studying [caching strategies]. Help me understand write-through vs write-back."
```

**2. Study (30-45 min)**
- Read `docs/SYSTEMS_DESIGN_GUIDE.md` section
- Read engineering blog
- Watch ByteByteGo video

**3. Implement (60-90 min)**
```bash
cp docs/templates/fundamental.py packages/incantations/src/incantations/fundamentals/[name].py
```

Implement key algorithm:
- LRU cache
- Consistent hashing
- Token bucket rate limiter
- Load balancer round-robin

**4. Document (20-30 min)**
- Fill in variations, trade-offs
- Real-world examples
- Interview tips

**5. Commit**
```bash
git add packages/incantations/
git commit -m "incantations(fundamentals): lru-cache with OrderedDict"
```

---

### Option B: Design Day

**1. Invoke systems-sage as interviewer**
```
"I want to design [URL shortener]. Act as my interviewer."
```

**2. RADIO Framework (90-120 min)**

**R - Requirements (10 min)**
- [ ] Functional requirements
- [ ] Non-functional (scale, latency, consistency)
- [ ] Scope (what's in/out)

**A - Architecture (15 min)**
- [ ] Draw high-level components
- [ ] Data flow diagram
- [ ] Technology choices

**D - Data Model (10 min)**
- [ ] Database schema
- [ ] SQL vs NoSQL choice
- [ ] Access patterns

**I - Interface (10 min)**
- [ ] API endpoints
- [ ] Request/response examples
- [ ] Authentication

**O - Optimization (15 min)**
- [ ] Bottleneck analysis
- [ ] Scaling strategy
- [ ] Trade-offs
- [ ] Failure scenarios

**3. Implement core algorithm (30-45 min)**
```bash
cp docs/templates/design.py packages/incantations/src/incantations/designs/[name].py
```

**4. Practice explaining (15 min)**
- Record yourself on phone
- Walk through design out loud
- Listen back - clear?

**5. Commit**
```bash
git add packages/incantations/
git commit -m "incantations(designs): url-shortener with base62 and caching"
```

---

## 🌙 Evening Review (30 min)

### Reflect (10 min)

```bash
# What did I do today?
git today

# What did I do this week?
git week
```

**Ask yourself:**
- What patterns did I practice?
- What concepts clicked?
- What am I still fuzzy on?

### Set Tomorrow's Goals (5 min)

**Be specific:**
```markdown
## Tomorrow
- **DSA**: 2 linked list problems (fast/slow pointer)
- **Systems**: Complete Twitter feed design
- **Focus**: Understanding fanout trade-offs
```

### Final Commit (if needed)

```bash
git add .
git commit -m "docs: updated progress notes"
```

**Done!** Close laptop without guilt.

---

## 📋 Commit Message Patterns

### Format
```
<type>(<scope>): <subject>
```

### Examples

**DSA:**
```
cantrips(arrays): two-sum, container-water, remove-duplicates
cantrips(strings): valid-palindrome, longest-substring [sliding-window]
cantrips(trees): revisited serialize-tree, now understand BFS approach
```

**Systems:**
```
incantations(fundamentals): lru-cache with OrderedDict
incantations(designs): url-shortener with estimation and caching
incantations(patterns): consistent-hashing with virtual nodes
```

**Other:**
```
docs: updated weekly progress
runes(structures): implemented doubly-linked-list
chore: updated templates
```

---

## 🚀 Quick Commands Reference

### Claude Code Slash Commands (New!)

Type these in Claude Code for instant workflows:

```
/start-session      # Morning kickoff with session-starter
/check-in          # Quick progress check
/commit-dsa        # Commit DSA work with proper formatting
/commit-systems    # Commit systems work with proper formatting
/weekly-review     # Sunday review with comprehensive stats
/design            # Start system design with systems-sage
```

### Justfile Recipes (New!)

Quick workflows using `just`:

```bash
# Session management
just start         # Start study session
just check-in      # Quick progress check
just review        # End of day review
just weekly        # Sunday weekly review

# Progress tracking
just today         # Today's commits with stats
just week          # This week's progress
just sprint 2024-12-20  # Sprint progress (set your start date)
just status        # Current git status + recent work

# DSA workflow
just cantrip-array two_sum     # Create new cantrip
just test-array two_sum        # Test specific problem
just work-array two_sum        # Create + remind to test
just test-topic arrays_strings # Test all in topic

# Systems workflow
just fundamental lru-cache     # Create fundamental concept
just design url-shortener      # Create system design
just fundamentals              # List all fundamentals
just designs                   # List all designs
just run-fundamental lru_cache # Run fundamental (if has main)

# Git helpers
just commit        # Interactive commit helper
just commit-dsa    # Quick commit DSA work
just commit-systems # Quick commit systems work
just log           # Nice git log (last 20)
just diff-today    # What changed today

# Utilities
just topics        # List all cantrip topics
just clean         # Clean Python cache files
```

### Git Workflow

```bash
# Daily
git today                    # Today's commits
git last                     # Last commit details

# Weekly
git week                     # This week's commits
git study                    # Study commits only
git dsa                      # DSA commits only
git sys                      # Systems commits only

# Reports
./scripts/weekly-report.sh   # Weekly summary
./scripts/sprint-report.sh   # Sprint progress
```

### Template Shortcuts (Old Way - Use Justfile Instead!)

```bash
# DSA problem
./scripts/new-cantrip.sh arrays_strings two_sum

# Systems concept
./scripts/new-fundamental.sh lru-cache

# System design
./scripts/new-design.sh url-shortener
```

---

## 🎯 Problem-Solving Checklist

Quick reference while solving:

```
[ ] Understand: Read 2x, clarify constraints
[ ] Examples: Work through 2-3 by hand
[ ] Pattern: What pattern does this use?
[ ] Plan: Pseudocode in comments
[ ] Edge cases: Empty? Single? Duplicates?
[ ] Implement: Clean code, good names
[ ] Test: Run all test cases
[ ] Complexity: Analyze time & space
[ ] Optimize: Can we do better?
[ ] Document: Fill in "What I Learned"
[ ] Commit: Good message
```

---

## 🏗️ System Design Checklist (RADIO)

Quick reference for designs:

```
[ ] Requirements (10 min)
    [ ] Functional requirements
    [ ] Non-functional (scale, latency, consistency)
    [ ] Scope agreement

[ ] Architecture (15 min)
    [ ] High-level components
    [ ] Data flow
    [ ] Tech choices with justification

[ ] Data Model (10 min)
    [ ] Database schema
    [ ] SQL vs NoSQL explained
    [ ] Access patterns

[ ] Interface (10 min)
    [ ] API endpoints
    [ ] Request/response
    [ ] Authentication

[ ] Optimization (15 min)
    [ ] Bottleneck analysis
    [ ] Scaling strategy
    [ ] Trade-offs documented
    [ ] Failure scenarios
```

---

## 📊 Weekly Rhythm

| Day | Morning (DSA) | Afternoon (Systems) |
|-----|---------------|---------------------|
| Mon | 2-3 problems | Design Day (full design) |
| Tue | 2-3 problems | Fundamental Day (concept + implement) |
| Wed | 2-3 problems | Design Day (full design) |
| Thu | 2-3 problems | Fundamental Day (concept + implement) |
| Fri | 2-3 problems | Design Day (full design) |
| Sat | 2-3 problems | Fundamental Day (concept + implement) |
| Sun | Review (redo problems) | Mock interview (timed design) |

---

## 🚩 Red Flags & Good Signs

### 🚩 Red Flags (Take Action)

- **>90 min on single Easy problem** → Move on, come back later
- **No commits 2+ days** → You're stuck, invoke agents
- **Studying >6 hrs/day consistently** → Burnout incoming
- **Skipping lunch breaks** → Diminishing returns
- **Not practicing out loud** → Won't be ready for interviews
- **Agents giving answers** → Reset conversation, ask to guide only

### ✅ Good Signs (Keep Going)

- **2-4 commits per day** → Steady progress
- **Problems getting faster** → Pattern recognition working
- **Can explain trade-offs** → Understanding deepening
- **Specific agent questions** → Engaged learning
- **Taking breaks guilt-free** → Sustainable pace
- **Redo problems easily** → Patterns internalized

---

## 🎨 Common Patterns Quick Reference

### DSA Patterns

| Pattern | When to Use | Example Problems |
|---------|-------------|------------------|
| **Two Pointers** | Sorted array, opposite ends | Two Sum II, Container With Water |
| **Sliding Window** | Contiguous subarray | Longest Substring, Max Sum Subarray |
| **Fast & Slow Pointers** | Linked list cycle | Detect Cycle, Middle Node |
| **BFS** | Level-order, shortest path | Binary Tree Level Order, Word Ladder |
| **DFS** | Explore all paths | Tree Paths, Permutations |
| **Binary Search** | Sorted array search | Search in Rotated, Find Peak |
| **Dynamic Programming** | Optimal substructure | Fibonacci, Coin Change, Knapsack |

### Systems Patterns

| Pattern | When to Use | Example Systems |
|---------|-------------|-----------------|
| **Caching** | Read-heavy (90%+ reads) | Twitter feed, User profiles |
| **Sharding** | Write scaling, data too large | Twitter tweets, User data |
| **Replication** | Read scaling, availability | Read replicas for DB |
| **Load Balancing** | Distribute traffic | Any high-traffic service |
| **Message Queue** | Async processing | Analytics, Email sending |
| **CDN** | Static content, global users | Netflix video, Image hosting |
| **Rate Limiting** | Prevent abuse | API endpoints |

---

## 💡 Pro Tips

### Efficiency Hacks

1. **Template aliases** (add to `~/.bashrc` or `~/.zshrc`):
```bash
alias cantrip='cp ~/grimoire/docs/templates/cantrip.py'
alias fundamental='cp ~/grimoire/docs/templates/fundamental.py'
alias design='cp ~/grimoire/docs/templates/design.py'
```

2. **Quick commit** (only after finishing work):
```bash
alias gcp='git add -A && git commit'
# Usage: gcp -m "cantrips(arrays): two-sum"
```

3. **Agent shortcuts** (mental model):
- Stuck on code? → study-partner
- Stuck on design? → systems-sage
- Start of day? → session-starter
- Adding tests? → testing-sage

### Interview Day Prep

**Night before:**
- [ ] Review 3-5 recent problems (don't solve new)
- [ ] Review 2-3 system designs (focus on trade-offs)
- [ ] Get 8 hours sleep
- [ ] Set out clothes, snacks, water

**Day of:**
- [ ] Warm up with 1 easy problem (not new!)
- [ ] Review pattern cheat sheet
- [ ] Remember: Think out loud, ask clarifying questions
- [ ] Start with brute force, then optimize

---

## 🔮 Daily Mantras

When you feel overwhelmed:

- **"I'm building my grimoire, one spell at a time"**
- **"Every problem teaches me a pattern"**
- **"Struggle means growth, not failure"**
- **"I explain clearly because I understand deeply"**
- **"Consistency over intensity"**

Focus on TODAY's work. Trust the process.

---

## 📚 Quick Documentation Reference

| Doc | Purpose |
|-----|---------|
| **CHEATSHEET.md** | This file - daily quick reference |
| **DAILY_WORKFLOW.md** | Detailed daily guide with examples |
| **INTERVIEW_SPRINT.md** | 8-week overview and targets |
| **SYSTEMS_DESIGN_GUIDE.md** | Full systems design reference |
| **GIT_WORKFLOW.md** | Git tracking and commit conventions |
| **HYPOTHESIS_GUIDE.md** | Property-based testing (optional) |

---

## 🚀 Start Your Day Right Now

```bash
cd ~/grimoire
```

Then:
```
"Start my study session"
```

Session-starter will handle the rest. 🔮

**You've got this. The grimoire grows with every commit.**
