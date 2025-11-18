# Daily Study Workflow - Practical Guide

Your executable guide for productive study days during the 8-week interview
sprint.

## Time Allocation (5-6 hours/day)

- **Morning (3 hours)**: DSA - Peak cognitive energy for algorithms
- **Lunch (3 hours)**: Break - Essential recovery time
- **Afternoon (2-3 hours)**: Systems - Architecture and design thinking
- **Evening (30 min)**: Review and planning

## ⭐ The Kata-First System (NEW!)

**The breakthrough approach:** Drill patterns BEFORE solving problems.

### The Magic Formula

```
Morning:
1. /kata (5-10 min)    → Build muscle memory (pure drills)
2. /ritual (45-60 min) → Apply patterns (LeetCode problems)

Evening (optional):
3. /kata (5 min)       → Reinforce patterns used today
```

**Why it works:**

- **Kata first** = Fresh muscle memory of the pattern
- **LeetCode second** = Immediate application (pattern already in your fingers!)
- **Spaced repetition** = Morning drill + evening drill = 2x exposure

**The difference:**

- **Without katas**: "I know the pattern exists... let me think through it...
  _struggles for 20 min_"
- **With katas**: "I just coded this 10 minutes ago... _fingers start typing
  automatically_"

### Mastery Level Progression

Each pattern has 5 levels that tell you what problems you're ready for:

- **Level 1 (Learning)**: Understanding the pattern - Practice with reference
- **Level 2 (Practicing)**: Coding from memory - **Ready for Easy cantrips**
- **Level 3 (Proficient)**: Zero bugs, under target time - **Ready for Medium
  cantrips**
- **Level 4 (Mastered)**: 10+ perfect reps - **Ready for Hard cantrips**
- **Level 5 (Breathing)**: Automatic, can teach others - **Interview ready**

**Check your level before each LeetCode problem:**

- Want to solve LC Easy? → Need Level 2 on that pattern
- Want to solve LC Medium? → Need Level 3 on that pattern
- Want to solve LC Hard? → Need Level 4 on that pattern

**If you struggle on a problem:** Return to katas for 5-10 more reps, then
retry.

See `docs/KATA_PRACTICE.md` for full kata philosophy.

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

### ⭐ KATA WARMUP (5-10 min) - NEW!

**BEFORE solving LeetCode problems, drill your patterns!**

This is the most important change: kata practice FIRST builds muscle memory that
makes LeetCode problems easier.

```bash
/kata    # Invoke kata-master agent
```

**kata-master will guide you:**

1. Pick today's pattern (based on your week/focus)
2. Show your current mastery level
3. Recommend which katas to practice
4. Time your attempts
5. Track progress and bugs
6. Update mastery logs

**Example session:**

```
User: /kata

kata-master: 🥋 KATA PRACTICE SESSION
             What would you like to do?
             1. Start kata session
             2. View mastery progress
             3. Weekly correlation report

User: 1

kata-master: Pick today's pattern:
             - Two Pointers (Level 2 - Practicing)
             - Sliding Window (Level 2 - Practicing)

User: two pointers

kata-master: Practice Kata 1 (two_sum_sorted)
             Target: < 2 min, zero bugs
             Type "START" when ready!

[You code from memory, run tests]

User: Done! 1:45, all tests passed

kata-master: ✓ New personal best: 1:45!
             Zero bugs - excellent!
             Ready for Easy cantrips!
```

**Why this works:**

- Fresh muscle memory of the pattern
- Fingers remember the mechanics
- Pattern recognition primed
- Transitions to LeetCode immediately apply what you drilled

**Check your mastery level:**

- Level 1-2: Practice Easy cantrips only
- Level 3: Ready for Medium cantrips
- Level 4-5: Ready for all difficulties

### Problem Solving with /ritual (2.5 hours)

**Problem 1 (45-60 min) - Use /ritual command**

```bash
/ritual 344    # Or /ritual and specify problem
```

**leetcode-sensei guides you through 4 phases:**

**Phase 1: Pre-Solve Analysis (7-10 min)**

```
Sensei: What pattern do you recognize?
You: Two pointers - I just practiced this!

Sensei: What's your kata mastery level?
You: Level 2 (Practicing)

Sensei: ✓ Perfect! Level 2 is ready for Easy.
        You just drilled this pattern 5 minutes ago.
        Your muscle memory is fresh. Let's proceed!
```

**Phase 2: Solution Development (25-35 min)**

- Code with think-aloud narration
- Your kata practice makes this smoother!

**Phase 3: Verification (5-10 min)**

- Test examples and edge cases

**Phase 4: Reflection (5 min)**

- Self-assessment scorecard
- Update kata mastery log: "Used successfully in LC #344"
- Commit your work

**If you struggle on a cantrip:**

```
Sensei: I notice you're struggling with the pointer logic.
        Recommend: Pause the ritual, practice
        two_pointers/opposite_ends kata 1 five times.

        Would you like to do that now?

User: Yes

[Return to /kata for 5-10 min, then resume /ritual]
```

**Problem 2 (45-60 min)**

- Same process: /ritual for guided practice
- Sensei checks kata readiness
- Correlates patterns you've drilled

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

### ⭐ Evening Kata Reinforcement (5 min) - OPTIONAL

**Spaced repetition of patterns used today:**

```bash
/kata    # Quick evening drill
```

**kata-master helps you:**

- Practice patterns you used in today's cantrips
- 1-2 quick katas (2-3 min each)
- Reinforces muscle memory before bed

**Example:**

```
kata-master: You used Two Pointers in LC #344 today.
             Quick reinforcement?

User: Yes

kata-master: Kata 1 (two_sum_sorted) - same one from this morning!
             Let's see if you're even faster now.

[You code it]

User: Done! 1:40, all tests passed

kata-master: ✓ 1:40! 5 seconds faster than this morning!
             The pattern is solidifying. Perfect!
```

**Why evening practice works:**

- Spaced repetition (morning + evening = 2x exposure)
- Consolidates learning from the day
- Ends day on a win (quick, easy katas)
- Only 5 minutes - sustainable

**Skip if:**

- You're tired (rest > practice when exhausted)
- You already practiced 3+ times today
- Evening commitments

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

**When**: First thing when sitting down **Invocation**:
`"Start my study session"` **Purpose**: Focus and goal-setting (<10 min)

### ⭐ kata-master (Morning warmup + Evening reinforcement)

**When**:

- START of DSA practice (every morning)
- END of day (optional evening reinforcement)

**Invocations**: `/kata`

**What it does**:

- Guides pattern selection (based on your week/goals)
- Times your kata attempts
- Tracks progress and bugs
- Shows mastery levels (Learning → Practicing → Mastered)
- Correlates kata practice with LeetCode success
- Celebrates milestones (zero bugs, target times, 100 reps)

**Morning flow**:

```bash
/kata              # 5-10 min kata warmup
/ritual            # 45-60 min LeetCode problem
```

**Purpose**: Build muscle memory BEFORE applying patterns in LeetCode

### ⭐ leetcode-sensei (During LeetCode practice)

**When**: Solving LeetCode problems **Invocation**: `/ritual [problem-number]`

**What it does**:

- Guides through all 4 phases of the ritual
- Checks kata mastery level before proceeding
- Recommends kata practice if struggling
- Enforces thinking out loud
- Tracks self-assessment scores
- Creates properly formatted commits

**Purpose**: Disciplined, interview-ready LeetCode practice

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

**Purpose**: Socratic guidance without solving for you

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

**Purpose**: Systems design interview practice

### testing-sage (Optional)

**When**: Adding property-based tests **Invocation**:
`"Help me add Hypothesis tests for two-sum on sorted array."`

**Purpose**: Property-based testing with Hypothesis

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

**DSA** (3h): reverse-string, valid-palindrome, two-sum **Systems** (2h): URL
shortener design **Patterns**: Two pointers clicking, base62 encoding understood
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

- **`KATA_PRACTICE.md`** - ⭐ Complete kata philosophy and practice guide (NEW!)
- `INTERVIEW_SPRINT.md` - 8-week sprint overview
- `SYSTEMS_DESIGN_GUIDE.md` - Systems design reference
- `HYPOTHESIS_GUIDE.md` - Property-based testing
- `DAILY_RITUAL.md` - Alternative workflow options
- `GIT_WORKFLOW.md` - Git conventions and tracking
- `.claude/commands/ritual.md` - /ritual command documentation
- `.claude/agents/kata-master.md` - kata-master agent documentation

---

**Now: Start today's session!**

```
"Start my study session"
```

Session-starter will take it from here. 🔮
