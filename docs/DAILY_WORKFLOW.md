# Daily Study Workflow - Practical Guide

Your executable guide for productive study days during the 8-week interview sprint.

## Time Allocation (5-6 hours/day)

- **Morning (3 hours)**: DSA - Peak cognitive energy for algorithms
- **Lunch (3 hours)**: Break - Essential recovery time
- **Afternoon (2-3 hours)**: Systems - Architecture and design thinking
- **Evening (30 min)**: Review and planning

---

## Morning Block: DSA (8am-11am)

### Start Ritual (5 min)

```bash
cd ~/grimoire
```

Then invoke session-starter:
```
"Start my study session"
```

Session-starter will:
- Review yesterday's commits
- Check progress in READMEs
- Help set today's specific goals
- Get you focused

### Problem Solving (2.5 hours)

**Problem 1 (45-60 min)**
1. Pick problem from current topic
2. Copy template: `cp docs/templates/cantrip.py packages/cantrips/src/cantrips/[topic]/[problem_name].py`
3. Understand requirements (5 min)
4. Plan approach (5 min)
5. Implement (20-30 min)
6. Test with examples (10 min)
7. Document learnings (10 min)

**If stuck >20 minutes:**
```
"Invoke study-partner - I'm stuck on [problem]. I've tried [approach] but [issue]."
```

**Problem 2 (45-60 min)**
- Repeat process
- Try different pattern if possible

**Problem 3 (optional, 30-45 min)**
- If time and energy permit
- Or redo tricky problem from yesterday

### Document & Commit (15 min)

1. Fill in "Reflections" sections
2. Update topic README checkboxes
3. Update main progress dashboard

**Commit your work:**
```bash
git add packages/cantrips/
git commit -m "cantrips(arrays): two-sum, valid-palindrome, container-water"
```

See `GIT_WORKFLOW.md` for commit message conventions.

---

## Lunch Break (11am-2pm)

**Critical for performance:**
- ✅ Eat actual food
- ✅ Walk outside (20+ min)
- ✅ Rest your eyes (no screens)
- ✅ Passive learning OK (one 15-min video)
- ❌ No active problem-solving
- ❌ No guilt about not studying

**Your brain consolidates learnings during rest.**

---

## Afternoon Block: Systems (2pm-5pm)

Choose between Fundamental Day or Design Day:

### Option A: Fundamental Day (3 days/week: Tue/Thu/Sat)

**Study Concept (30-45 min)**
- Read from `docs/SYSTEMS_DESIGN_GUIDE.md`
- Read engineering blog post
- Watch ByteByteGo video
- Read Alex Xu chapter

**Invoke systems-sage:**
```
"I'm studying [caching strategies]. Help me understand when to use write-through vs write-back."
```

**Implement Key Algorithm (60-90 min)**
```bash
cp docs/templates/fundamental.py packages/incantations/src/incantations/fundamentals/[concept].py
```

Implement in Python:
- LRU cache
- Consistent hashing ring
- Token bucket rate limiter
- Simple load balancer
- etc.

**Systems-sage can guide:**
```
"What should I implement to really understand consistent hashing?"
```

**Document (20-30 min)**
- Fill in template: variations, trade-offs, examples
- Include real-world use cases (Netflix, Uber, etc.)

**Commit:**
```bash
git add packages/incantations/
git commit -m "incantations(fundamentals): consistent-hashing with virtual nodes"
```

### Option B: Design Day (2-3 days/week: Mon/Wed/Fri)

**Invoke systems-sage as interviewer:**
```
"I want to design [URL shortener]. Act as my interviewer."
```

**Work through RADIO (90-120 min)**

Systems-sage will guide you:
- "What are the requirements? Be specific about scale."
- "Walk me through your architecture. Why these components?"
- "Show me your database schema. What's your access pattern?"
- "What happens when traffic increases 10x?"

Interactive back-and-forth like real interview.

**Implement Core Algorithm (30-45 min)**
```bash
cp docs/templates/design.py packages/incantations/src/incantations/designs/[system].py
```

Implement the "meaty" part in Python:
- Short code generation
- Feed ranking algorithm
- Matching algorithm
- Whatever is most interesting

**Document (20-30 min)**
- Complete design template
- Trade-offs and follow-ups

**Practice Explaining (15 min)**
- Record yourself on phone
- Walk through design out loud
- Listen back: Are you clear?

**Commit:**
```bash
git add packages/incantations/
git commit -m "incantations(designs): url-shortener with base62 encoding and caching"
```

---

## Evening Wind-down (8pm-8:30pm)

**Don't start new work - just reflect and plan.**

### Review (10 min)

```bash
# What did I do today?
git log --oneline --since="1 day ago"

# What did I do this week?
git log --oneline --since="1 week ago" --no-merges
```

Ask yourself:
- What patterns did I practice?
- What concepts clicked?
- What am I still fuzzy on?

### Set Tomorrow's Goals (5 min)

**Be specific** - write in progress notes or README:

```markdown
## Tomorrow (Dec 24)
- **DSA**: 2 linked list problems (fast/slow pointer pattern)
- **Systems**: Complete Twitter feed design OR study database sharding
- **Focus**: Understanding trade-offs between fanout approaches
```

### Final Commit (if needed)

```bash
git add .
git commit -m "docs: updated progress notes"
```

**Done!** Close laptop, rest without guilt.

---

## Using Agents Throughout Day

### session-starter (Once, at start of day)
**When**: First thing when sitting down
**Invocation**: `"Start my study session"`
**Purpose**: Focus and goal-setting (<10 min)

### grimoire-keeper (Throughout day, any time)
**When**: Check-ins, commits, reviews
**Invocations**:
- `"Check in"` - See today's progress
- `"What have I done today?"` - Detailed stats
- `"I finished [work], ready to commit"` - Structure commit
- `"Am I on track?"` - Pace vs targets
- `"Weekly review"` - Full analysis
**Purpose**: Accountability and progress tracking with minimal overhead

### study-partner (As needed during DSA)
**When**:
- Stuck >20 min
- Bug in implementation
- Want to verify approach

**Invocations**:
- `"I'm stuck on [problem]. I think [approach] but [issue]."`
- `"My linked list reversal returns wrong result. Help me debug."`
- `"I solved this O(n²). Is there better? Don't tell me, guide me."`

### systems-sage (Start of systems + as needed)
**When**:
- Beginning systems work
- Stuck on architecture
- Want feedback
- Learning concept

**Invocations**:
- `"Design Instagram. Act as my interviewer."`
- `"Stuck on fanout-on-write vs read. Help me reason through it."`
- `"Review my URL shortener for bottlenecks."`

### testing-sage (Optional)
**When**: Adding property-based tests
**Invocation**: `"Help me add Hypothesis tests for two-sum on sorted array."`

---

## Weekly Rhythm

**Monday/Wednesday/Friday**: Design days
- Afternoon = full system design practice
- Mock interview style with systems-sage

**Tuesday/Thursday/Saturday**: Fundamental days
- Afternoon = study concept + implement
- Deep understanding through code

**Sunday**: Review & Mock Interview
- Morning: Redo tricky problems from scratch
- Afternoon: Timed mock design (45 min)
- Review weak areas

---

## Tracking Progress (Simple)

### Primary: Git Commits
Your commit history IS your tracker.

```bash
# Today's work
git log --oneline --since="1 day ago"

# This week's work
git log --online --since="1 week ago" | grep "cantrips\|incantations"

# Count commits this week
git log --oneline --since="1 week ago" --no-merges | wc -l
```

**Good commit messages** (see `GIT_WORKFLOW.md`):
```
cantrips(arrays): two-sum, container-water [two-pointers]
incantations(fundamentals): lru-cache with OrderedDict
incantations(designs): twitter-feed with fanout-on-write
cantrips(trees): revisited serialize-tree, now understand approach
```

### Secondary: Progress READMEs
Update checkboxes weekly:
- `packages/cantrips/README.md`
- `packages/incantations/README.md`

### Optional: Daily Notes
Add `PROGRESS.md` at root:

```markdown
# Week 1 (Dec 21-27)

## Day 1 (Mon, Dec 21)
**DSA** (3h): reverse-string, valid-palindrome, two-sum
**Systems** (2h): URL shortener design
**Patterns**: Two pointers clicking, base62 encoding understood
**Fuzzy**: Cache invalidation strategies

## Day 2 (Tue, Dec 22)
...

## Week Summary
- **DSA**: 12 problems solved (8 arrays, 4 strings)
- **Systems**: 2 designs, 3 fundamentals
- **Confidence**: 7/10 DSA, 6/10 Systems
- **Next week**: Linked lists, database sharding
```

### Don't Use: SuperProductivity, Toggl, etc.
**Why not during sprint:**
- Adds cognitive overhead
- Context switching between tools
- Perfectionism trap
- Slows you down

**After employment:** Go ahead, optimize your workflow then.

---

## Red Flags & Good Signs

### 🚩 Red Flags

- **>90 min on single Easy problem** → Move on, come back later
- **No commits for 2+ days** → You're stuck, invoke agents
- **Agents giving answers** → Reset, ask them to guide only
- **Studying >6 hours/day consistently** → Burnout incoming
- **Skipping lunch breaks** → Diminishing returns
- **Not practicing out loud** → Won't be ready for real interviews

### ✅ Good Signs

- **2-4 commits per day** → Steady progress
- **Problems getting faster** → Pattern recognition working
- **Can explain trade-offs** → Understanding deepening
- **Specific questions for agents** → Engaged learning
- **Taking breaks guilt-free** → Sustainable pace

---

## Problem-Solving Checklist

Copy this for each problem:

```
[ ] Understand: Read problem 2x, clarify constraints
[ ] Examples: Work through 2-3 examples by hand
[ ] Patterns: What pattern does this use? (two pointers, sliding window, etc.)
[ ] Plan: Write pseudocode or outline in comments
[ ] Edge cases: Empty input? Single element? Duplicates?
[ ] Implement: Write clean code with good naming
[ ] Test: Run against examples + edge cases
[ ] Complexity: Analyze time and space
[ ] Optimize: Can we do better?
[ ] Document: Fill in "What I Learned"
[ ] Commit: With good message
```

---

## System Design Checklist (RADIO)

```
[ ] Requirements (10 min)
    [ ] Functional: What must it do?
    [ ] Non-functional: Scale? Latency? Consistency?
    [ ] Scope: What's in/out of scope?

[ ] Architecture (15 min)
    [ ] High-level components diagram
    [ ] Data flow: User → System → Response
    [ ] Technology choices with justification

[ ] Data Model (10 min)
    [ ] Database schema
    [ ] Relationships
    [ ] Access patterns
    [ ] SQL vs NoSQL choice explained

[ ] Interface (10 min)
    [ ] API endpoints with request/response
    [ ] Authentication approach
    [ ] Error handling

[ ] Optimization (15 min)
    [ ] Bottleneck analysis
    [ ] Scaling strategy (sharding, replication, caching)
    [ ] Trade-offs documented
    [ ] Failure scenarios considered
```

---

## Quick Reference Commands

```bash
# Start day
cd ~/grimoire
# Then: "Start my study session"

# Copy templates
cp docs/templates/cantrip.py packages/cantrips/src/cantrips/[topic]/[name].py
cp docs/templates/fundamental.py packages/incantations/src/incantations/fundamentals/[name].py
cp docs/templates/design.py packages/incantations/src/incantations/designs/[name].py

# Review progress
git log --oneline --since="1 week ago"
git log --oneline --since="1 day ago"

# Commit work
git add packages/cantrips/
git commit -m "cantrips(arrays): two-sum, container-water"

git add packages/incantations/
git commit -m "incantations(fundamentals): lru-cache"

# Check status
git status
```

---

## Motivation Reminders

**When overwhelmed:**
- Focus on TODAY's 2-3 problems, 1 concept
- Review what you've ALREADY learned (git log)
- Trust the process - daily work compounds
- Rest is part of learning

**Daily mantras:**
- 🔮 "I'm building my grimoire, one spell at a time"
- 🔮 "Every problem teaches me a pattern"
- 🔮 "Struggle means growth"
- 🔮 "I explain clearly because I understand deeply"

**Remember:**
- You have 8 focused weeks - rare opportunity
- Interviews test preparation, not IQ
- Thousands pass these every year
- You're capable of this

---

## Related Documentation

- `INTERVIEW_SPRINT.md` - 8-week sprint overview
- `SYSTEMS_DESIGN_GUIDE.md` - Systems design reference
- `HYPOTHESIS_GUIDE.md` - Property-based testing
- `DAILY_RITUAL.md` - Alternative workflow options
- `GIT_WORKFLOW.md` - Git conventions and tracking (NEW)

---

**Now: Start today's session!**

```
"Start my study session"
```

Session-starter will take it from here. 🔮
