# The LeetCode Interview Ritual

> "Excellence is not an act, but a habit. Every problem is a dress rehearsal for the
> real interview."

This is your **daily practice ritual** for LeetCode problems. Follow it religiously
for every problem over the next 8 weeks. By interview day, these steps will be muscle
memory - pattern recognition will be instant, explanations will be crystal clear, and
Google interviewers will be amazed at the ease and confidence you bring.

## Philosophy: Every Problem is Interview Practice

**The Goal:** Walk into a Google interview and have the interviewer think:

- "Wow, they explain their reasoning so clearly"
- "They identified the pattern instantly"
- "Their complexity analysis is spot-on"
- "They handle edge cases like a senior engineer"

**How This Ritual Works:**

- **45-60 minutes per problem** (interview simulation timing)
- **Emphasis on verbal skills** - think out loud, explain like you're teaching
- **Pattern recognition speed** - train the 30-second reflex
- **Minimal documentation** - 5 minutes to capture what matters
- **Consistency over volume** - follow the ritual every single time

**The Secret:** It's not about solving more problems. It's about building habits that
transfer to high-pressure interviews.

---

## The Four Phases

Every problem follows this exact sequence:

1. **Pre-Solve Analysis** (7-10 min) - Understand, identify pattern, plan approach
2. **Solution Development** (25-35 min) - Code with think-aloud narration
3. **Verification & Testing** (5-10 min) - Test, verify, explain
4. **Post-Solve Reflection** (5 min max) - Quick documentation and self-assessment

**Total:** 45-60 minutes

---

## Phase 1: Pre-Solve Analysis (7-10 min)

**Goal:** Demonstrate expert problem-solving approach before writing a single line of
code.

This phase separates senior engineers from juniors. Great interviewers are watching
how you _think_, not just how you code.

### Step 1.1: Read & Understand (2 min)

**What to do:**

- Read the problem statement carefully
- Read the examples - they often reveal the pattern
- Identify what the problem is really asking

**Say out loud:**

- "So we're given [input], and we need to find/return [output]"
- "The key constraint is [constraint]"
- Restate the problem in your own words

**Example:**

> "We're given an array of integers and a target sum. We need to return the indices
> of two numbers that add up to the target. The key constraint is we can't use the
> same element twice."

### Step 1.2: Ask Clarifying Questions (1 min)

**Critical habit:** Always ask questions, even if they seem obvious. This shows
thoroughness.

**Standard questions to ask:**

- "Can the input be empty?"
- "Can there be negative numbers / duplicates?"
- "Is the input sorted?"
- "Can I modify the input array?"
- "Is there always a valid answer, or should I handle no solution?"
- "What's the expected time/space complexity?" (if not stated)

**Say out loud:**

> "Before I start, let me clarify a few things. Can the array be empty? Can there be
> duplicates? Is there guaranteed to be exactly one solution?"

**In practice:** Write these as comments at the top of your solution.

### Step 1.3: Pattern Recognition (30 seconds - TIMED!)

**This is your superpower.** Set a timer. Identify the pattern category in 30
seconds.

**Mental checklist (rapid-fire):**

- Is the input sorted? → Binary search or two pointers
- Looking for pairs/complements? → Hash map or two pointers
- Substring/subarray problem? → Sliding window
- Tree/graph traversal? → DFS, BFS, or specific traversal
- Connectivity/components? → Union-Find or DFS/BFS
- Optimization with choices? → DP or greedy

**Say out loud:**

> "This looks like a [PATTERN] problem because [REASON]"

**Example:**

> "This looks like a hash map problem because we're looking for complements - for
> each number, we need to check if target minus that number exists."

**Pro tip:** If you can't identify the pattern in 30 seconds, that's data - this
pattern needs more practice.

### Step 1.4: Constraint Analysis (1 min)

**Look at the constraints** - they tell you what complexity is acceptable.

**Reference table (memorize this):**

- n ≤ 10: O(2^n) or O(n!) - backtracking/brute force OK
- n ≤ 1,000: O(n²) - nested loops OK
- n ≤ 10⁵: O(n log n) - sorting or heap
- n ≤ 10⁶: O(n) - single pass only
- n ≤ 10⁹: O(log n) or O(1) - binary search or math

**Say out loud:**

> "The constraint is n ≤ 10⁴, so O(n²) would work, but we should aim for O(n) or O(n
> log n)."

### Step 1.5: Brute Force Approach (2 min)

**Always acknowledge the brute force solution first.** Don't code it, just explain
it.

**Why this matters:** Shows you understand the problem and can think in steps.

**Say out loud:**

> "The brute force approach would be to check every pair of numbers using nested
> loops. That would be O(n²) time and O(1) space. We can do better."

**Template:**

- What's the naive solution?
- What's the complexity?
- Why is it inefficient?

### Step 1.6: Optimal Approach (2 min)

**Now explain your optimized solution** - the pattern you identified.

**Structure your explanation:**

1. **High-level strategy:** "We'll use a hash map to store numbers we've seen"
2. **Why it's better:** "This lets us check for complements in O(1) instead of O(n)"
3. **Core insight:** "We can build the map as we go, no need for two passes"

**Say out loud:**

> "My approach is to use a hash map. As we iterate through the array, for each
> number, we check if target minus that number is already in our map. If yes, we've
> found our pair. If no, we add the current number to the map. This is O(n) time and
> O(n) space."

**Pro tip:** Explain this clearly enough that a non-technical person could understand
the strategy.

### Step 1.7: Edge Cases (1 min)

**List edge cases before coding.** This shows thoroughness that impresses
interviewers.

**Common edge cases:**

- Empty input
- Single element
- All elements the same
- Negative numbers / zero
- Very large or very small values
- No valid solution exists

**Say out loud:**

> "Edge cases to consider: empty array, single element (no pair possible), duplicate
> numbers, and verifying we don't use the same index twice."

**Write these as comments** - you'll test them later.

---

## Phase 2: Solution Development (25-35 min)

**Goal:** Code the solution with crystal-clear narration, like you're teaching.

This is where communication skills shine. Google interviewers want to hear your
thought process.

### Step 2.1: Verbal Walkthrough (3 min)

**Before writing code, walk through your solution with a small example.**

**Pick a simple example** (not the largest one from the problem):

- Use 3-5 elements
- Trace through your algorithm step by step
- Show how your data structures change

**Say out loud:**

> "Let me walk through this with an example. Given [2, 7, 11, 15], target 9:
>
> - i=0: num=2, looking for 9-2=7. Map is empty, so add 2→0 to map.
> - i=1: num=7, looking for 9-7=2. Map contains 2! Return [0, 1]."

**Why this matters:** Catches logic errors before you code. Shows you can explain.

### Step 2.2: State Complexity (30 seconds)

**Before coding, commit to your complexity analysis.**

**Say out loud:**

> "This will be O(n) time because we iterate through the array once, and each hash
> map lookup is O(1). Space complexity is O(n) for the hash map in the worst case."

**Why:** Stating this upfront shows confidence. You can verify later.

### Step 2.3: Code with Think-Aloud Narration (20-30 min)

**This is the heart of the interview.** Code while explaining every line.

**Think-aloud template:**

1. **Setup:**

   > "First, I'll create a hash map to store values we've seen"

2. **Main logic:**

   > "Now I'll iterate through the array. For each number..." "I'm checking if the
   > complement exists in my map" "If it does, we've found our answer and can return
   > immediately"

3. **Update state:**

   > "Otherwise, I'll add this number and its index to the map"

4. **Edge case handling:**
   > "At the end, if we haven't found a pair, we return an empty array"

**Best practices while coding:**

- Use descriptive variable names (`complement`, not `c`)
- Add brief comments for complex logic
- Think out loud for every decision
- If you make a mistake, say "Actually, let me fix that..."

**Example think-aloud:**

```python
def two_sum(nums, target):
    """
    Find indices of two numbers that sum to target.
    Approach: Hash map for O(1) complement lookup.
    Time: O(n), Space: O(n)
    """
    # "I'll use a dictionary to map values to their indices"
    seen = {}

    # "Now I'll iterate through with enumerate to get both value and index"
    for i, num in enumerate(nums):
        # "For each number, calculate what its complement would be"
        complement = target - num

        # "Check if we've seen the complement before"
        if complement in seen:
            # "If yes, return both indices - the stored one and current one"
            return [seen[complement], i]

        # "Otherwise, store this number and its index for future lookups"
        seen[num] = i

    # "If we finish the loop, no solution exists"
    return []
```

**Narration while typing:**

> "I'll call this `seen` because it tracks numbers we've seen so far. Using enumerate
> to get both index and value. For each number, the complement is target minus num.
> If that complement is already in my map, I found the pair - return both indices.
> Otherwise, add this number to the map and continue."

**Pro tip:** Pause occasionally to check if your logic makes sense. Say things like:

- "Does this handle the edge case where...?"
- "Let me make sure this is correct..."
- "Actually, I should check for..."

### Step 2.4: Dry Run with Example (2 min)

**Test your code by hand with one of the provided examples.**

**Say out loud as you trace:**

> "Let me trace through with [2, 7, 11, 15], target = 9:
>
> - i=0, num=2: complement=7, seen={}, 7 not in seen, add 2→0
> - i=1, num=7: complement=2, seen={2:0}, 2 in seen! Return [0, 1]
>
> That's correct!"

**Why:** Catches off-by-one errors, wrong variable usage, etc.

### Step 2.5: Handle Edge Cases (2 min)

**Go through the edge cases you listed earlier.**

**Say out loud:**

> "Let me verify edge cases:
>
> - Empty array: We'd immediately return [], correct.
> - Single element: Loop runs once, no complement found, return [].
> - No solution: We return [] at the end, correct.
> - Duplicate numbers: We store the latest index, which is fine since we return as
>   soon as we find a pair."

**If you spot an issue:** Fix it immediately and explain the fix.

---

## Phase 3: Verification & Testing (5-10 min)

**Goal:** Prove your solution works and demonstrate thoroughness.

### Step 3.1: Solution Walkthrough (3 min)

**Explain your solution like you're teaching a colleague.**

**Structure:**

1. **Overall approach:** "I used a hash map to track numbers we've seen"
2. **Why it works:** "For each number, we check if its complement exists in O(1)
   time"
3. **Key insight:** "We build the map as we go, so we find the pair in a single pass"
4. **Complexity:** "O(n) time, O(n) space"

**Say out loud:**

> "To summarize: I iterate through the array once, maintaining a hash map of values
> to indices. For each number, I calculate what the complement would need to be to
> reach the target. If that complement is already in my map, I've found the two
> numbers and return their indices. Otherwise, I add the current number to the map
> and continue. This gives us O(n) time instead of the O(n²) brute force approach."

### Step 3.2: Test with Examples (2 min)

**Run through the provided examples mentally or on paper.**

**For each example:**

- Input
- Expected output
- Trace through your code
- Verify output matches

**Say out loud:**

> "Example 1: [2,7,11,15], target=9. My code returns [0,1]. Correct. Example 2:
> [3,2,4], target=6. My code would return [1,2]. Correct."

### Step 3.3: Test Edge Cases (2 min)

**Actually trace through 1-2 edge cases.**

**Say out loud:**

> "Edge case: empty array []. My code returns []. Correct. Edge case: no solution
> [1,2,3], target=10. My code returns []. Correct."

### Step 3.4: Verify Complexity (1 min)

**Double-check your complexity analysis.**

**Say out loud:**

> "Time complexity: Single loop through n elements, each hash map operation is O(1),
> so total is O(n). Space complexity: Hash map stores at most n elements, so O(n).
> This matches what I stated earlier."

### Step 3.5: Consider Follow-ups (1 min)

**Think ahead to what the interviewer might ask.**

**Common follow-ups:**

- "What if the array is sorted?" → Two pointers would be O(1) space
- "What if there are multiple valid pairs?" → Return first found, or modify to return
  all
- "What if we can't use extra space?" → Would need O(n²) brute force

**Say out loud:**

> "If the array were sorted, I could use two pointers for O(1) space instead of O(n).
> If there could be multiple valid pairs, I'd modify this to collect all pairs
> instead of returning immediately."

---

## Phase 4: Post-Solve Reflection (5 min max)

**Goal:** Cement learning with minimal documentation. Fast iteration.

### Step 4.1: Quick Documentation (3 min)

**Update your cantrip file with essential information only.**

At the top of your solution file, add:

```python
"""
LeetCode #1: Two Sum (Easy)

Pattern: Hash Map (complement lookup)
Difficulty: Easy
Status: Solved ✓

Key Insight:
Instead of checking all pairs (O(n²)), store seen numbers in a hash map
to check for complements in O(1).

Complexity:
- Time: O(n) - single pass through array
- Space: O(n) - hash map storage

Edge Cases:
- Empty array → return []
- No solution → return []
- Duplicates → handled correctly (store latest index)

Pattern Recognition Trigger:
"Looking for pairs/complements" → hash map
"""
```

**Time limit: 3 minutes.** No more. This is all you need.

### Step 4.2: Update Topic README (30 sec)

**Quick checkbox update:**

Navigate to `cantrips/[topic]/README.md` and check off the problem:

```markdown
- [x] LC #1: Two Sum - Hash map complement lookup
```

**One line only.** Pattern + brief note.

### Step 4.3: Self-Assessment Scorecard (1 min)

**Answer these yes/no questions honestly:**

**Pattern Recognition:**

- [ ] Did I identify the pattern in < 30 seconds?
- [ ] Did I choose the optimal approach?

**Explanation Clarity:**

- [ ] Did I explain the brute force first?
- [ ] Did I clearly explain my optimal approach before coding?
- [ ] Did I use good variable names and comments?

**Complexity Analysis:**

- [ ] Did I state complexity before coding?
- [ ] Was my analysis correct?

**Edge Case Awareness:**

- [ ] Did I list edge cases before coding?
- [ ] Did I test them at the end?

**Coding Quality:**

- [ ] Did I code without major bugs?
- [ ] Did my solution pass all test cases?

**Communication:**

- [ ] Did I think out loud the entire time?
- [ ] Could someone understand my explanation?

**Time:**

- [ ] Did I finish in 45-60 minutes?

**Scoring:**

- 12-14 checks: Excellent - interview ready
- 9-11 checks: Good - keep practicing
- 6-8 checks: Fair - identify weak areas
- 0-5 checks: Needs work - slow down and focus on process

### Step 4.4: Identify Improvement Area (30 sec)

**Pick ONE thing to focus on next problem.**

**Examples:**

- "Pattern recognition too slow - need to drill hash map triggers"
- "Explanation unclear - practice verbalizing approach before coding"
- "Missed edge cases - make a standard checklist"
- "Took too long to code - need to practice this pattern more"

**Write it down** (in a notebook or comment):

```
Problem: LC #1
Focus next time: Explain complexity analysis more confidently
```

---

## The Self-Assessment Scorecard

**After each problem, fill this out.** Track your scores weekly to measure
improvement.

### Quick Score Sheet (Copy to notebook or file)

```
Date: _______  Problem: LC #___  Difficulty: _____

Pattern Recognition:
[ ] Identified in < 30 sec
[ ] Chose optimal approach

Explanation:
[ ] Explained brute force first
[ ] Clear optimal approach explanation
[ ] Good variable names & comments

Complexity:
[ ] Stated before coding
[ ] Analysis was correct

Edge Cases:
[ ] Listed before coding
[ ] Tested at the end

Code Quality:
[ ] No major bugs
[ ] Passed all tests

Communication:
[ ] Thought out loud throughout
[ ] Explanation was clear

Time:
[ ] Finished in 45-60 min

Score: __/14

Focus for next problem:
_________________________________
```

---

## Weekly Calibration

**Every Sunday, review your week's scorecards.**

### Weekly Review Questions:

1. **Pattern Recognition Speed:**
   - How many problems did I identify pattern in < 30 sec?
   - Which patterns am I still slow to recognize?
   - **Action:** Drill those patterns with template coding

2. **Explanation Clarity:**
   - Did my explanations improve over the week?
   - Am I comfortable thinking out loud?
   - **Action:** Record yourself on 1-2 problems next week

3. **Complexity Analysis:**
   - Am I consistently stating complexity before coding?
   - Are my analyses accurate?
   - **Action:** Review complexity table in ALGORITHM_MASTERY.md

4. **Edge Case Awareness:**
   - Am I catching edge cases before coding?
   - Do I test them at the end?
   - **Action:** Create a standard edge case checklist

5. **Overall Progress:**
   - Average score this week: \_\_/14
   - Improvement from last week: +\_\_
   - **Celebrate wins!** Acknowledge progress

### Calibration Actions:

**If your average score is:**

**12-14:** You're crushing it!

- Increase difficulty (more Medium/Hard)
- Practice explaining to others
- Do 1 full mock interview this week

**9-11:** Solid progress

- Keep current pace
- Focus on weak areas from scorecard
- Add 1 pattern drill per day

**6-8:** Need to slow down

- Focus on process over quantity
- Do fewer problems, follow ritual more carefully
- Review ALGORITHM_MASTERY.md patterns

**0-5:** Reset and focus

- Are you rushing? Slow down.
- Follow each phase timing strictly
- Focus on 1 pattern for entire week

---

## Interview Simulation Mode

**Once per week: Full pressure simulation.**

This is where you practice performing under pressure.

### Setup (5 min before):

1. **Pick a random Medium problem** you haven't seen
2. **Set timer for 45 minutes** - hard stop
3. **Optional but recommended:** Record yourself (audio or video)
4. **Turn off all references** - no ALGORITHM_MASTERY.md, no notes
5. **Get in interview mindset:** Dress appropriately, sit up straight

### During (45 min):

- Follow the ritual exactly as written
- Talk out loud the ENTIRE time, even when alone
- Pretend someone is watching
- If you get stuck, work through it out loud
- Don't give up - show problem-solving process

### After (15 min):

1. **Watch/listen to recording** (if you made one)
   - Did you explain clearly?
   - Did you think out loud enough?
   - Were there awkward pauses?

2. **Honest self-assessment:**
   - Would I pass an interview performing like this?
   - What impressed me about my performance?
   - What needs work?

3. **Action items:**
   - What will I do differently next mock?

### Weekly Progression:

- **Week 1-2:** Simulation with Easy problems (build confidence)
- **Week 3-4:** Simulation with Medium problems
- **Week 5-6:** Simulation with Medium/Hard, record yourself
- **Week 7-8:** Full mock interview with friend/mentor as interviewer

---

## Integration with Grimoire

### Where Files Go:

**Solution file:**

```
packages/cantrips/src/cantrips/[topic]/[problem_name].py
```

Use the cantrip template:

```bash
cp docs/templates/cantrip.py packages/cantrips/src/cantrips/hashing/two_sum.py
```

**Documentation:**

- Add quick notes at top of solution file (see Phase 4.1)
- Update topic README checkbox
- Update main dashboard (`packages/cantrips/README.md`) counts

### Commit Workflow:

**After each problem:**

Use the `/commit-dsa` slash command or:

```bash
git add packages/cantrips/src/cantrips/[topic]/[problem_name].py
git add packages/cantrips/src/cantrips/[topic]/README.md
git commit -m "cantrips([topic]): [problem-name]

Solved LC #[number]: [Problem Name] ([difficulty])
Pattern: [pattern-used]
Complexity: O(n) time, O(n) space

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Example:**

```bash
git commit -m "cantrips(hashing): two-sum

Solved LC #1: Two Sum (Easy)
Pattern: Hash map complement lookup
Complexity: O(n) time, O(n) space

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Daily Workflow Integration:

**Morning (5 min):**

- Review yesterday's self-assessment
- Pick today's problem (aligned with current pattern focus)
- Set timer for 60 minutes max

**During solving (45-60 min):**

- Follow the 4-phase ritual exactly
- Think out loud the entire time
- No rushing, follow the process

**After solving (5 min):**

- Quick documentation
- Self-assessment scorecard
- Commit your work

**Total time: ~70 minutes per problem**

2 problems per day = ~2.5 hours of focused practice

---

## The Communication Cheat Sheet

**Memorize these phrases.** Use them in every problem.

### Opening:

- "Let me make sure I understand the problem..."
- "Before I start, let me clarify a few things..."

### Pattern Recognition:

- "This looks like a [pattern] problem because..."
- "The key insight is..."

### Brute Force:

- "The naive approach would be..."
- "That would be O(\_\_\_) time, which is inefficient because..."

### Optimal Approach:

- "A better approach is..."
- "The key optimization is..."
- "This improves the complexity to..."

### During Coding:

- "I'm using [data structure] because..."
- "This handles the case where..."
- "Let me add a comment here to explain..."

### Complexity:

- "The time complexity is O(\_\_\_) because..."
- "The space complexity is O(\_\_\_) because..."
- "The trade-off here is..."

### Testing:

- "Let me trace through with an example..."
- "For the edge case where..."
- "This should return..."

### Confidence Phrases:

- "I'm confident this works because..."
- "The correctness argument is..."
- "This is optimal because..."

### If Stuck:

- "Let me think about this out loud..."
- "What if I approached it as..."
- "The constraint suggests I need..."

**Practice these until they're automatic.**

---

## Troubleshooting Common Issues

### "I'm too slow recognizing patterns"

**Solution:**

- Do the diagnostic test in ALGORITHM_MASTERY.md daily
- Before each problem, guess the pattern before reading full description
- Keep a pattern triggers cheat sheet visible
- Drill pattern templates 5 min before each session

### "I forget to think out loud"

**Solution:**

- Record yourself - you'll hear the silence
- Put a sticky note: "EXPLAIN OUT LOUD"
- Practice with a friend/colleague watching
- Narrate even trivial things: "I'm creating a variable called..."

### "My explanations are unclear"

**Solution:**

- Practice the "explain to a 5-year-old" test
- Write down your explanation, then read it - does it make sense?
- Ask: "Could someone implement this from my description?"
- Focus on WHY, not just WHAT

### "I always run out of time"

**Solution:**

- You're probably overcomplicating
- Set timers for each phase - hard stop and move on
- Practice coding templates until they're muscle memory
- Start with easier problems to build speed

### "I miss edge cases"

**Solution:**

- Create a standard checklist and use it every time:
  ```
  [ ] Empty input
  [ ] Single element
  [ ] All same elements
  [ ] Negatives/zero
  [ ] No valid solution
  [ ] Duplicates
  ```
- Test edge cases immediately after coding

### "I make too many coding mistakes"

**Solution:**

- You're going too fast
- Slow down and think out loud more
- Use descriptive variable names
- Test with small example before writing code
- Practice pattern templates daily

---

## The 8-Week Ritual Progression

Your ritual should evolve as you improve.

### Weeks 1-2: Building the Habit

**Focus:**

- Follow every step religiously, even if it feels slow
- Emphasis on thinking out loud
- Easy problems to build confidence
- Goal: Ritual becomes automatic

**Metrics:**

- Complete ritual for 10-15 problems
- Average score: aim for 8+/14
- Pattern recognition: < 1 min (working toward 30 sec)

### Weeks 3-4: Increasing Difficulty

**Focus:**

- Move to Medium problems
- Pattern combinations (sliding window + hash map)
- Record yourself 2-3 times
- Goal: Clear explanations become natural

**Metrics:**

- Complete ritual for 15-20 problems
- Average score: aim for 10+/14
- Pattern recognition: < 45 sec

### Weeks 5-6: Polishing Communication

**Focus:**

- Medium/Hard problems
- Emphasis on complexity analysis fluency
- Weekly mock interviews
- Goal: Interview-ready confidence

**Metrics:**

- Complete ritual for 15-20 problems
- Average score: aim for 11+/14
- Pattern recognition: < 30 sec consistently

### Weeks 7-8: Interview Simulation

**Focus:**

- Timed mocks (45 min hard limit)
- Hardest problems you're likely to see
- Practice with others watching
- Goal: Peak performance under pressure

**Metrics:**

- Complete ritual for 12-15 problems
- Average score: aim for 12+/14
- Pattern recognition: < 30 sec, 95%+ accuracy
- Can explain any pattern in sleep

---

## The Daily Commitment

**Every problem, every day, for 8 weeks:**

1. ✅ Follow all 4 phases in order
2. ✅ Set timer for 60 min max
3. ✅ Think out loud the entire time
4. ✅ Fill out self-assessment scorecard
5. ✅ Commit your work with proper message

**No exceptions. No shortcuts.**

**Why it works:**

- Habits compound over time
- Consistent practice beats sporadic intensity
- Interview skills are muscle memory, not intelligence

**The math:**

- 2 problems/day × 7 days/week × 8 weeks = **112 problems**
- Each one following this ritual
- By week 8, you'll have 112 repetitions of:
  - Pattern recognition
  - Clear explanation
  - Complexity analysis
  - Edge case identification
  - Think-aloud coding

**That's how you wow Google interviewers.**

---

## Final Thoughts: The Mindset

**This ritual is not about solving problems.**

It's about becoming the kind of engineer who:

- Makes complex things sound simple
- Sees patterns instantly
- Communicates clearly under pressure
- Handles edge cases like a senior engineer
- Analyzes complexity without thinking

**Every repetition of this ritual builds that person.**

By week 8, when you walk into that Google interview:

- Pattern recognition will feel like breathing
- Explaining your approach will feel natural
- Complexity analysis will roll off your tongue
- Edge cases will be obvious
- The interviewer will think: "This person really knows what they're doing"

**That's the goal.**

Not to memorize solutions. To build habits that make you interview-proof.

---

## Quick Reference: The Ritual Checklist

Print this. Keep it visible while solving.

```
⏱️ PHASE 1: PRE-SOLVE ANALYSIS (7-10 min)
[ ] 1.1: Read & understand (2 min) - Restate problem
[ ] 1.2: Ask clarifying questions (1 min) - Standard questions
[ ] 1.3: Pattern recognition (30 sec) - TIMED!
[ ] 1.4: Constraint analysis (1 min) - What complexity is OK?
[ ] 1.5: Brute force approach (2 min) - Explain, don't code
[ ] 1.6: Optimal approach (2 min) - Explain strategy clearly
[ ] 1.7: Edge cases (1 min) - List them out

⏱️ PHASE 2: SOLUTION DEVELOPMENT (25-35 min)
[ ] 2.1: Verbal walkthrough (3 min) - Trace with small example
[ ] 2.2: State complexity (30 sec) - Commit before coding
[ ] 2.3: Code with narration (20-30 min) - Think out loud!
[ ] 2.4: Dry run with example (2 min) - Test by hand
[ ] 2.5: Handle edge cases (2 min) - Verify they work

⏱️ PHASE 3: VERIFICATION (5-10 min)
[ ] 3.1: Solution walkthrough (3 min) - Explain like teaching
[ ] 3.2: Test with examples (2 min) - Provided test cases
[ ] 3.3: Test edge cases (2 min) - Your edge cases
[ ] 3.4: Verify complexity (1 min) - Double-check analysis
[ ] 3.5: Consider follow-ups (1 min) - What's next?

⏱️ PHASE 4: REFLECTION (5 min max)
[ ] 4.1: Quick documentation (3 min) - Pattern + insight + complexity
[ ] 4.2: Update README (30 sec) - Check the box
[ ] 4.3: Self-assessment (1 min) - Score out of 14
[ ] 4.4: Improvement area (30 sec) - Focus for next time

[ ] COMMIT YOUR WORK - Use /commit-dsa

Total time: 45-60 minutes
```

---

Now go practice. Follow this ritual religiously.

In 8 weeks, you'll walk into that Google interview and absolutely crush it.
