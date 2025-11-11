# Daily Study Ritual

A structured approach to consistent interview preparation with the grimoire.

## Quick Start with Agents ⚡

**New to the session?** Let the agents help you get started:

```
"Start my study session"
```

or

```
"Invoke session-starter"
```

The **session-starter** agent will:

- Review yesterday's progress
- Check current topic status
- Help you set today's goal
- Prepare your workspace
- Get you focused in < 10 minutes

**During your session** when you need guidance:

```
"Invoke study-partner"
```

or just ask naturally - the **study-partner** agent will:

- Guide you with questions (not answers!)
- Help you debug by asking about your logic
- Explain concepts when needed
- Encourage you when stuck
- Remind you to document your learnings

See `docs/AGENT_GUIDE.md` for detailed agent usage.

---

## Manual Morning Ritual (15-30 min)

**Prefer to do it yourself?** Follow this checklist:

> 💡 **Tip**: The session-starter agent can automate steps 1-3 for you!

### 1. Review Yesterday

- [ ] Open `cantrips/README.md` - Check overall progress
- [ ] Review yesterday's problem solutions
- [ ] Read through your "Lessons Learned" sections
- [ ] Note any patterns you struggled with

### 2. Set Today's Goal

- [ ] Choose your focus: New topic or continue current?
- [ ] Decide: Structure implementation or problem solving?
- [ ] Set realistic target (e.g., "Implement stack" or "Solve 2 easy problems")

### 3. Prepare Workspace

```bash
cd grimoire
git status                    # Check what you worked on last
```

## Study Session (1-3 hours)

### Option A: New Topic Day

**When**: Starting a new topic (Arrays, Hashing, Trees, etc.)

1. **Watch & Learn (30-45 min)**

   - [ ] Watch LeetCode course video for topic
   - [ ] Take notes in a scratch file or notebook
   - [ ] Identify key concepts and patterns

2. **Implement Structure (45-60 min)**

   - [ ] Create directory: `runes/structures/[name]/`
   - [ ] Copy template:
         `cp docs/templates/data_structure_template.md runes/structures/[name]/README.md`
   - [ ] Implement from scratch in `__init__.py`
   - [ ] Write docstrings as you go
   - [ ] Test basic operations manually

3. **Document (15-30 min)**
   - [ ] Fill out README.md sections:
     - Complexity table
     - Visual representation
     - Key concepts you learned
     - Common pitfalls you discovered
   - [ ] Add to `runes/structures/__init__.py` imports

### Option B: Problem Solving Day

**When**: Practicing problems for current topic

1. **Warm Up (10 min)**

   - [ ] Review topic README: `cantrips/src/cantrips/[topic]/README.md`
   - [ ] Refresh pattern recognition
   - [ ] Review previous solutions briefly

2. **Solve Problems (40-90 min)**

   **For each problem:**

   a. **Understand (5-10 min)**

   - [ ] Read problem carefully
   - [ ] Write down input/output examples
   - [ ] Identify constraints
   - [ ] Think: "What pattern is this?"

   b. **Plan (5-10 min)**

   - [ ] Sketch approach on paper or comments
   - [ ] Consider edge cases
   - [ ] Estimate complexity
   - [ ] Don't code yet!

   c. **Implement (15-30 min)**

   - [ ] Copy template:
         `cp docs/templates/cantrip_template.py cantrips/[topic]/[problem_name].py`
   - [ ] Fill in problem description
   - [ ] Write your approach in comments
   - [ ] Implement solution
   - [ ] Add test cases

   d. **Verify (5-10 min)**

   - [ ] Run your tests
   - [ ] Test edge cases manually
   - [ ] Check LeetCode if needed
   - [ ] Fix bugs, understand why they happened

3. **Reflect & Document (15-20 min)**
   - [ ] Fill in "Lessons Learned" section
   - [ ] Update topic README checkboxes
   - [ ] Note similar problems
   - [ ] Update progress dashboard
   - [ ] Add to pattern checklist if you mastered one

### Option C: Review & Consolidation Day

**When**: Friday or after completing a topic

1. **Review Implementations (30 min)**

   - [ ] Re-read your runes implementations
   - [ ] Can you explain each operation's complexity?
   - [ ] Try to re-implement a simple structure from memory

2. **Pattern Analysis (30 min)**

   - [ ] Review all problems solved this week
   - [ ] Group by pattern (two pointers, sliding window, etc.)
   - [ ] Write down pattern recognition triggers
   - [ ] Update `cantrips/README.md` pattern checklist

3. **Solve a Mixed Problem (30 min)**
   - [ ] Pick a problem from a previous topic
   - [ ] Solve without looking at your notes
   - [ ] This tests retention and pattern transfer

## Evening Ritual (5-10 min)

### 1. Commit Your Work

```bash
git add .
git status                          # Review what changed
git commit -m "Topic: Problem(s) solved / Structure implemented"
```

### 2. Update Progress

- [ ] Check off completed items in topic README
- [ ] Update `cantrips/README.md` dashboard counts
- [ ] Add any insights to "Study Notes" sections

### 3. Tomorrow's Prep

- [ ] What's next? (Write it down)
- [ ] Any prerequisites to review?
- [ ] Set a specific start time

## Weekly Ritual (30 min - 1 hour)

**When**: Sunday or end of week

1. **Review the Week**

   - [ ] Count problems solved (easy/medium/hard)
   - [ ] Review all "Lessons Learned" sections
   - [ ] Identify strongest and weakest patterns

2. **Plan Next Week**

   - [ ] Choose next topic(s)
   - [ ] Set weekly goals (e.g., "Complete hashing section")
   - [ ] Schedule review days for previous topics

3. **Pattern Mastery Check**
   - [ ] Review pattern checklist in `cantrips/README.md`
   - [ ] For each pattern, can you:
     - [ ] Recognize it in new problems?
     - [ ] Explain when to use it?
     - [ ] Implement it from memory?

## Time Management Guidelines

### Minimum Daily (1 hour)

- 1 problem solved thoroughly OR
- 1 structure implemented partially

### Standard Daily (2 hours)

- 2-3 problems (easy/medium) OR
- 1 structure fully implemented + documented

### Intensive Daily (3+ hours)

- New topic video + structure implementation OR
- 3-4 problems (mixed difficulty) + review

## Troubleshooting

### "I'm stuck on a problem for 30+ minutes"

1. ✅ **Don't give up immediately** - Struggle is learning
2. ✅ **Invoke study-partner agent** - It will guide you with questions
3. ✅ **Review the pattern section** in topic README
4. ✅ **Look at a hint** (not full solution)
5. ❌ **Don't copy solutions** - Understand, then implement yourself
6. ✅ **Mark it for retry** - Come back in a few days

### "I can't remember the implementation"

1. ✅ **That's normal!** - Implementation details fade
2. ✅ **Focus on understanding** the concept and complexity
3. ✅ **Re-implement from scratch** - This is the best practice
4. ✅ **Compare with your old code** - See what you forgot

### "I'm not making progress"

1. ✅ **Quantity isn't everything** - Deep understanding beats rushing
2. ✅ **Review your READMEs** - See what you've actually learned
3. ✅ **Track patterns mastered** - Not just problems solved
4. ✅ **Take a break day** - Rest is part of learning

## Motivation Mantras

- 🔮 "Every problem teaches me a new spell"
- 🔮 "I'm building my grimoire, one rune at a time"
- 🔮 "Struggling means I'm learning, not failing"
- 🔮 "Each cantrip makes me more powerful"
- 🔮 "Consistency over intensity"

## Daily Checklist Template

Copy this to your daily note-taking:

```markdown
# Date: YYYY-MM-DD

## Morning (□ Complete)

- [ ] Reviewed yesterday's work
- [ ] Set today's goal: **\*\***\_\_\_**\*\***
- [ ] Checked progress dashboard

## Study Session (□ Complete)

- [ ] Main focus: **\*\***\_\_\_**\*\***
- [ ] Time spent: \_\_\_ hours
- [ ] What I implemented/solved: **\*\***\_\_\_**\*\***

## Progress Made

- [ ] Structure implemented: **\*\***\_\_\_**\*\***
- [ ] Problems solved: **\*\***\_\_\_**\*\***
- [ ] Patterns practiced: **\*\***\_\_\_**\*\***

## Lessons Learned

-
-

## Evening (□ Complete)

- [ ] Committed changes
- [ ] Updated READMEs
- [ ] Set tomorrow's goal: **\*\***\_\_\_**\*\***

## Energy Level: \_\_\_/10

## Understanding Level: \_\_\_/10

## Tomorrow's Focus: **\*\***\_\_\_**\*\***
```

---

Remember: **The grimoire grows with consistent practice, not perfection.** Every line
of code you write from scratch, every problem you struggle through, every insight you
document - these are your runes, your building blocks of mastery. 🔮✨
