# /ritual - LeetCode Interview Ritual

Invoke the leetcode-sensei agent to guide you through the complete LeetCode interview ritual with discipline and accountability.

## Usage

```bash
# Start ritual for a specific problem
/ritual 1              # LC #1: Two Sum
/ritual 242            # LC #242

# Start ritual without specifying problem
/ritual                # Will ask which problem
```

## What This Does

The leetcode-sensei agent will guide you through all 4 phases of the ritual defined in `docs/LEETCODE_RITUAL.md`:

1. **Phase 1: Pre-Solve Analysis (7-10 min)**
   - Read & understand
   - Clarifying questions
   - Pattern recognition (30 sec timed!)
   - Constraint analysis
   - Brute force approach
   - Optimal approach
   - Edge cases

2. **Phase 2: Solution Development (25-35 min)**
   - Verbal walkthrough
   - State complexity
   - Code with narration
   - Dry run
   - Handle edge cases

3. **Phase 3: Verification (5-10 min)**
   - Solution walkthrough
   - Test examples
   - Test edge cases
   - Verify complexity
   - Consider follow-ups

4. **Phase 4: Reflection (5 min)**
   - Self-assessment scorecard (score out of 14)
   - Identify improvement area
   - Create commit message
   - Commit your work

**Total time: 45-60 minutes**

## Kata-First Philosophy

**Before diving into LeetCode problems, check your kata mastery!**

The ritual now includes kata readiness checks to ensure you have the prerequisite muscle memory:

### Pattern Recognition Check (Phase 1)

When you identify a pattern in Phase 1, the sensei will ask:
- "Have you mastered the prerequisite katas for this pattern?"
- "What's your current mastery level? (1-5)"
- "When did you last practice this kata?"

### Mastery Level Guidelines

**Level 1-2:** Focus on katas, only attempt Easy problems
**Level 3:** Ready for Easy and Medium problems
**Level 4-5:** Ready for all difficulties

### Kata Recommendations

If your kata mastery is below the recommended level:

**For Easy problems:**
- Recommended: Level 2 (Practicing) or higher
- If Level 1: Do 5-10 kata reps before attempting

**For Medium problems:**
- Recommended: Level 3 (Proficient) or higher
- If Level 2: Do 5 more kata reps, focus on zero bugs

**For Hard problems:**
- Recommended: Level 4 (Mastered) or higher
- If Level 3: Master advanced katas (4-5) first

### The Sensei's Response

**If kata mastery is sufficient:**
- Proceed with the ritual
- Track this as a successful pattern application

**If kata mastery is insufficient:**
- Recommend specific kata practice first
- Suggest: "Let's pause the ritual and practice [pattern] katas for 10 minutes"
- Offer to resume ritual after kata practice

**Integration with /kata:**
```bash
# Morning workflow (recommended)
/kata                          # 5-10 min warmup (builds muscle memory)
/ritual                        # 45-60 min LeetCode (applies patterns)
```

## The Agent Will:

- ✅ Keep you accountable to each step
- ✅ Give gentle time reminders
- ✅ Ask Socratic questions when you're stuck
- ✅ Enforce thinking out loud
- ✅ Help with self-assessment
- ✅ Create properly formatted commits
- ✅ Track your progress over time

## The Agent Will NOT:

- ❌ Solve problems for you
- ❌ Give away patterns or solutions
- ❌ Write code for you
- ❌ Let you skip steps

## Philosophy

This is interview practice, not just problem-solving. Every repetition builds habits that transfer to real interviews. Follow the ritual religiously for 8 weeks and watch your interview skills become second nature.

---

**Ready to practice with discipline? Start your ritual now!**
