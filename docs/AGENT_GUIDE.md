# Agent Quick Reference Guide

Quick reference for using the grimoire study partner agents.

## Two Agents

### 🎯 session-starter

**Role**: Get your study session organized **When**: Start of every study session
**Time**: < 10 minutes

### 🧙 study-partner

**Role**: Guide your learning without solving for you **When**: Stuck, need
explanation, debugging help **Time**: Throughout your session

---

## How to Invoke

### Starting Your Session

Say any of these:

```
"Start my study session"
"Invoke session-starter"
"Begin study session"
"Help me get started"
```

### During Your Session

Say any of these:

```
"Invoke study-partner"
"I need help understanding this"
"I'm stuck on this problem"
"Can you help me debug?"
```

Or just ask naturally - Claude will use the agent automatically when appropriate.

---

## session-starter: What It Does

✅ **Reviews your progress**

- Checks git log for yesterday's work
- Reviews cantrips/README.md dashboard
- Looks at current topic status

✅ **Helps you set goals**

- Suggests what to work on next
- Helps you choose: structure implementation or problems
- Sets realistic targets (1-3 problems, 1 structure, etc.)

✅ **Prepares workspace**

- Shows git status
- Identifies uncommitted work
- Gets you focused quickly

✅ **Hands off**

- Quick setup, then you're on your own
- Mentions study-partner is available if needed

### What session-starter WON'T do

- ❌ Solve problems for you
- ❌ Write code
- ❌ Make decisions for you (just suggests)
- ❌ Explain concepts (that's study-partner's job)

---

## study-partner: What It Does

✅ **Guides with questions**

- "What approach have you tried?"
- "What pattern does this remind you of?"
- "What's the complexity of your solution?"
- "Have you considered this edge case?"

✅ **Helps you debug**

- Asks about your logic step by step
- Points out where your thinking might be off
- Suggests what to check, not what to fix

✅ **Explains concepts**

- Time/space complexity
- How data structures work
- When to use which pattern
- Trade-offs between approaches

✅ **Encourages you**

- Reminds you that struggle = learning
- Celebrates your attempts and progress
- Suggests when to take a break or retry later

✅ **Tracks progress**

- Reminds you to update READMEs
- Suggests documenting learnings
- Prompts you to commit work

### What study-partner WON'T do

- ❌ Write your solutions
- ❌ Implement data structures for you
- ❌ Give you the answer directly
- ❌ Copy code for you
- ❌ Skip the learning process

**Core principle**: Make you a better problem solver, not solve problems for you.

---

## Common Scenarios

### Scenario: "I don't know where to start on this problem"

**study-partner will ask**:

- Have you read the problem carefully?
- What are the constraints?
- What pattern might this be?
- Check your topic README - see any similar problems?

**study-partner won't**:

- Tell you the pattern directly
- Give you the solution approach
- Write pseudocode for you

### Scenario: "My code isn't working"

**study-partner will ask**:

- What do you expect vs. what's happening?
- Walk me through your logic step by step
- What edge cases are you testing?
- What's this variable's value at this point?

**study-partner won't**:

- Debug your code for you
- Rewrite your implementation
- Point out the bug directly (helps you find it)

### Scenario: "I've been stuck for 30 minutes"

**study-partner will**:

- Acknowledge the good effort
- Suggest reviewing pattern section
- Ask guiding questions to unstick you
- Recommend marking for retry if truly blocked

**study-partner won't**:

- Give up and show you the solution
- Tell you to look at answers
- Let you copy code

### Scenario: "I don't understand this concept"

**study-partner will**:

- Explain the concept clearly
- Give examples and analogies
- Draw ASCII diagrams if helpful
- Connect to what you already know

**This is when direct explanation is appropriate!**

---

## Tips for Working with Agents

### Get the Most from session-starter

- Be honest about yesterday's progress
- Have a rough idea what you want to work on
- Commit your work from yesterday first
- Use it EVERY session for consistency

### Get the Most from study-partner

- **Struggle first** (15-20 min) before asking
- Be specific: "I'm stuck on the two-pointer logic" not "help"
- Show what you've tried
- Ask "why" questions to deepen understanding
- Use it to review your thinking, not get answers

### When NOT to Use Agents

- Quick syntax questions → just ask Claude directly
- Git commands → use bash/docs
- Template locations → check CLAUDE.md
- Simple file operations → do them yourself

---

## Agent Limitations

### What They Can Access

- ✅ Read files (Read tool)
- ✅ Search files (Glob, Grep tools)
- ✅ Your git history
- ✅ Your READMEs and documentation

### What They CANNOT Access

- ❌ Cannot write files (no Write/Edit tools)
- ❌ Cannot run code
- ❌ Cannot access LeetCode directly
- ❌ Cannot browse the web

This is **intentional** - they guide, you implement.

---

## Example Interactions

### Good Interaction with study-partner ✅

**You**: I'm stuck on reversing a linked list **Agent**: What approach have you tried
so far? **You**: I'm trying to update the next pointers but losing references
**Agent**: Good observation! When you update the next pointer, what happens to the
rest of the list? Do you still have a reference to it? **You**: Oh! I need to save it
first **Agent**: Exactly! That's the key insight. What variables do you need?

### Bad Interaction (if agent gave answers) ❌

**You**: I'm stuck on reversing a linked list **~~Agent~~**: Use three pointers:
prev, curr, next. Here's the code... ❌

This would rob you of learning!

---

## Integration with Daily Ritual

**Morning** (15-30 min):

1. Invoke session-starter
2. Review, set goals, prepare

**During Session** (1-3 hours):

- Work independently
- Invoke study-partner when stuck (15-30 min)
- Get guidance, keep implementing yourself

**Evening** (5-10 min):

- Commit work (agents may remind you)
- Update READMEs
- Set tomorrow's goal

---

## Quick Command Cheat Sheet

```bash
# Start session
"Start my study session"

# Get help during session
"Invoke study-partner"

# Specific help
"Help me understand [concept]"
"I'm stuck on [problem]"
"Can you explain [topic]?"
"Review my thinking on this"

# Don't say (these would make agent solve for you)
❌ "Show me the solution"
❌ "Write this code for me"
❌ "What's the answer?"
```

---

## Remember

**The agents exist to make you a better programmer**, not to program for you.

- Every question they ask makes you think deeper
- Every bug you fix yourself makes you stronger
- Every struggle is growth
- The grimoire grows through YOUR effort 🔮

If you ever feel the agent is doing too much, tell it: "Guide me, don't solve for
me."

---

For more details, see:

- `.claude/agents/session-starter.md` - Full agent configuration
- `.claude/agents/study-partner.md` - Full agent configuration
- `docs/DAILY_RITUAL.md` - How agents fit into daily workflow
- `CLAUDE.md` - Complete project context
