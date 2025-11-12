# 8-Week Interview Sprint - Quick Start

**Goal**: Pass technical interviews at large tech companies in Jan/Feb

**Timeline**: 8 weeks intensive preparation (Dec holidays → Feb interviews)

**Focus**: Interview-readiness, not perfection. Build confidence + demonstrate competence.

---

## Week 1-2: Foundations (Starting Now - Holiday Sprint!)

### DSA Focus: Arrays, Strings, Hashing
**Target**: 25-30 problems (mostly Easy, some Medium)

**Daily routine**:
- Morning (3 hours): Solve 2-3 LeetCode problems
  - Use `docs/templates/cantrip.py` template
  - Save to `packages/cantrips/src/cantrips/[topic]/`
  - Document patterns and learnings
- Afternoon (2 hours): Systems fundamentals
  - Study 1 concept (scaling, caching, load balancing, databases)
  - Use `docs/templates/fundamental.py` template
  - Implement key algorithms (LRU cache, etc.) in Python
  - Save to `packages/incantations/src/incantations/fundamentals/`

### Systems Focus: Core Concepts
1. **Scaling basics** (vertical vs horizontal, stateless vs stateful)
2. **Load balancing** (algorithms, health checks)
3. **Caching** (strategies, eviction, LRU implementation)
4. **Databases** (SQL vs NoSQL, indexing, when to use each)
5. **CAP theorem** (consistency, availability, partition tolerance)

**Resources**:
- `docs/SYSTEMS_DESIGN_GUIDE.md` - Your reference guide
- `docs/DAILY_RITUAL.md` - Updated with testing options
- Alex Xu's "System Design Interview" book (skim)
- ByteByteGo YouTube videos (15-20 min each)

---

## Week 3-4: Pattern Recognition

### DSA Focus: Linked Lists, Stacks, Queues, Trees
**Target**: 25-30 problems (Medium focus)

**Key patterns to master**:
- Two pointers (slow/fast, opposite ends)
- Stack for matching/parsing
- Queue for BFS
- Tree traversals (in-order, pre-order, post-order, level-order)

### Systems Focus: First Designs
**Target**: 4 easy system designs

1. **URL Shortener** - Hashing, encoding, caching
2. **Pastebin** - Text storage, expiration
3. **Rate Limiter** - Token bucket, sliding window (implement in Python!)
4. **Key-Value Store** - Consistent hashing, sharding

**Practice**:
- Use `docs/templates/design.py` for each
- Work through full RADIO framework (Requirements, Architecture, Data, Interface, Optimization)
- Implement core algorithm in Python
- Practice explaining out loud (record yourself with phone!)

---

## Week 5-6: Advanced Topics

### DSA Focus: Binary Search, DFS/BFS, Heaps, Dynamic Programming
**Target**: 30-35 problems (Medium + some Hard)

**Challenging but high-value patterns**:
- Binary search variations
- Graph traversals (DFS/BFS, detecting cycles)
- Heap for top-K problems
- DP for optimization (start simple: fibonacci, climbing stairs)

### Systems Focus: Complex Designs
**Target**: 6 medium complexity designs

1. **Twitter Feed** - Fanout, timeline generation, caching
2. **Instagram** - Image storage, CDN, feed ranking
3. **Uber** - Geolocation, matching algorithm, WebSockets
4. **Web Crawler** - Distributed crawling, politeness, deduplication
5. **YouTube** - Video upload, transcoding, CDN delivery
6. **Chat System** - Real-time messaging, presence, history

**Deep dive topics**:
- Database sharding strategies
- Message queues (Kafka, RabbitMQ)
- CDN and static content delivery
- Real-time communication (WebSockets, polling)

---

## Week 7-8: Interview Simulation

### DSA Focus: Mock Interviews
**Target**: 20-25 problems (review weak areas + new Medium/Hard)

**Practice format**:
- Set timer: 45 minutes per problem
- Talk out loud while solving
- Explain complexity analysis
- Discuss alternative approaches
- Review afterwards: what you missed, what was good

**Resources**:
- Pramp.com (free mock interviews)
- Interviewing.io (paid but valuable)
- LeetCode mock interview feature

### Systems Focus: Timed Design Practice
**Target**: 8-10 full designs (mix of new + review)

**Practice format**:
- Set timer: 45 minutes
- Work through RADIO framework
- Draw diagrams (on paper or whiteboard app)
- Explain trade-offs out loud
- Record yourself and review

**Common designs to practice**:
- Design [your favorite app] - motivating and relevant
- Mix of read-heavy (Twitter) and write-heavy (analytics)
- Mix of consistency (banking) and availability (feed)

---

## Daily Structure During Sprint

### High-Intensity Days (Mon-Sat)

**Morning Block (8am-11am): DSA**
- Invoke session-starter
- Solve 2-3 LeetCode problems
- Document in cantrips with tests
- Update progress tracker
- Commit work

**Afternoon Block (2pm-5pm): Systems**
- Study 1 fundamental OR practice 1 design
- Implement key algorithm in Python
- Document in incantations
- Practice explaining out loud
- Commit work

**Evening (8pm-8:30pm): Review**
- What did I learn today?
- What patterns did I practice?
- What am I unsure about?
- Set tomorrow's specific goals

### Recovery Day (Sunday)

**Morning (10am-12pm): Review**
- Redo tricky problems from scratch
- Review system designs
- Identify weak areas

**Afternoon (2pm-4pm): Mock Interview**
- 1 hour DSA mock (2 problems)
- 1 hour systems design mock
- Review performance

---

## Progress Tracking

### Weekly Check-in (Friday evening or Sunday)

**DSA Progress**:
- [ ] Problems solved this week: ___ / 25-35 target
- [ ] New patterns mastered: ___
- [ ] Weak areas identified: ___

**Systems Progress**:
- [ ] Fundamentals studied: ___
- [ ] Designs completed: ___
- [ ] Can explain these out loud: ___

**Confidence Level** (1-10):
- DSA: ___
- Systems: ___
- Overall readiness: ___

### Mid-Sprint Check (Week 4)

**DSA**:
- [ ] 50+ problems solved
- [ ] Comfortable with Easy, can solve most Medium
- [ ] Arrays, strings, hashing, linked lists, stacks/queues mastered

**Systems**:
- [ ] 5+ fundamental concepts mastered
- [ ] 4+ easy designs completed
- [ ] Can draw high-level diagrams confidently
- [ ] Understand major trade-offs (CAP, consistency, caching)

**Action if behind**:
- Adjust daily hours (6-7 hours if needed)
- Focus on high-frequency patterns
- Skip lowest-value topics temporarily
- Get accountability partner

---

## Interview Day Checklist

### Night Before
- [ ] Review 3-5 recent problems (don't solve new ones)
- [ ] Review 2-3 system designs (focus on trade-offs)
- [ ] Get 8 hours of sleep
- [ ] Set out clothes, snacks, water

### Day Of

**For DSA Interview**:
- [ ] Warm up with 1 easy problem (not new!)
- [ ] Review common patterns cheat sheet
- [ ] Remember: think out loud, ask clarifying questions
- [ ] Start with brute force, then optimize

**For Systems Design Interview**:
- [ ] Review RADIO framework
- [ ] Review back-of-envelope estimation shortcuts
- [ ] Remember: it's a conversation, not a test
- [ ] Ask about requirements, scale, constraints first

---

## Resources Quick Reference

### Grimoire Files
- `docs/DAILY_RITUAL.md` - Daily workflow
- `docs/SYSTEMS_DESIGN_GUIDE.md` - Comprehensive systems reference
- `docs/HYPOTHESIS_GUIDE.md` - Testing reference (optional during sprint)
- `docs/templates/cantrip.py` - LeetCode solution template
- `docs/templates/fundamental.py` - Systems concept template
- `docs/templates/design.py` - System design template

### External Resources
- **DSA**: LeetCode Explore cards, NeetCode roadmap, "Cracking the Coding Interview"
- **Systems**: Alex Xu books, ByteByteGo, Educative "Grokking System Design"
- **Mock Interviews**: Pramp (free), Interviewing.io (paid)
- **Engineering Blogs**: Netflix, Uber, Twitter, Instagram (for real-world examples)

### Grimoire Agents
- **session-starter**: "Start my study session" - Get organized
- **grimoire-keeper**: "Check in" any time - Progress tracking & accountability
- **study-partner**: When stuck on DSA problem - Guides with questions
- **systems-sage**: When working on system designs - Guides architecture thinking
- **testing-sage**: When adding property tests - Suggests strategies

---

## Motivation & Mindset

### Remember
- **You have 8 weeks of focused time** - This is a rare opportunity
- **Struggle means learning** - Don't expect to solve everything first try
- **Interview questions are learnable** - They test preparation, not just IQ
- **Systems design is about thinking, not memorization** - Show your process
- **You're capable of this** - Thousands pass these interviews every year

### When Feeling Overwhelmed
1. **Break it down**: Focus on today's 2-3 problems, 1 concept
2. **Trust the process**: You're building skills every day
3. **Review your progress**: Look at what you've learned already
4. **Take breaks**: Rest is part of learning
5. **Remember your goal**: Better job, better opportunities, better growth

### Daily Mantras
- 🔮 "I'm building my grimoire, one spell at a time"
- 🔮 "Every problem teaches me a pattern"
- 🔮 "I explain clearly because I understand deeply"
- 🔮 "Interviews are conversations, not interrogations"
- 🔮 "I've prepared well and I'm ready"

---

## After the Sprint: Continuing Growth

Once you land a job:

1. **Keep grimoire alive**: Continue adding to runes, cantrips, incantations
2. **Add new section**: `packages/craft/` for engineering practices, design patterns
3. **Switch to Rust**: For deep systems learning (create separate repo)
4. **Build real projects**: Apply what you've learned in production
5. **Teach others**: Write blog posts, mentor juniors, contribute to open source

The grimoire is not just for interviews - it's your personal knowledge base that grows with your career.

---

**Now: Invoke session-starter and begin Week 1! 🔮**
