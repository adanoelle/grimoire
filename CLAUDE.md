# Grimoire - Claude Context Document

This document provides context about the grimoire workspace structure and study
workflow for AI assistants.

## Project Overview

**Grimoire** is a comprehensive interview preparation workspace for large tech companies containing:

- **Runes**: Data structures and algorithms implemented from scratch
- **Cantrips**: LeetCode problem solutions organized by topic
- **Incantations**: Systems design concepts and practice (NEW)

The goal is hands-on learning through implementation and practice, preparing for both:
1. **DSA Interviews**: Following LeetCode course structure
2. **Systems Design Interviews**: Studying distributed systems patterns

**Current Focus**: 8-week interview sprint for Jan/Feb interviews at large tech companies.

## Workspace Structure

```
grimoire/
├──  claude/
│   ├── agents/
│   │   ├── session-starter.md           # Start study sessions
│   │   ├── grimoire-keeper.md           # Progress tracking & accountability
│   │   ├── study-partner.md             # DSA learning guidance
│   │   ├── systems-sage.md              # Systems design guide
│   │   └── testing-sage.md              # Property-based testing expert
│   ├── skills/                          # Model-invoked autonomous capabilities
│   │   ├── progress-today/
│   │   ├── progress-week/
│   │   ├── progress-sprint/
│   │   ├── commit-suggest/
│   │   └── test-problem/
│   └── commands/                        # User-invoked slash commands
│       ├── start-session.md
│       ├── check-in.md
│       ├── commit-dsa.md
│       ├── commit-systems.md
│       ├── weekly-review.md
│       └── design.md
│
├── docs/
│   ├── templates/
│   │   ├── structure.md                 # Data structure template
│   │   ├── algorithm.md                 # Algorithm template
│   │   ├── cantrip.py                   # LeetCode solution template
│   │   ├── topic.md                     # Topic progress template
│   │   ├── fundamental.py               # Systems concept template
│   │   └── design.py                    # System design template
│   ├── CHEATSHEET.md                    # Quick reference - print this! ⭐
│   ├── DAILY_WORKFLOW.md                # Practical daily study guide
│   ├── INTERVIEW_SPRINT.md              # 8-week sprint overview
│   ├── GIT_WORKFLOW.md                  # Git for progress tracking
│   ├── SYSTEMS_DESIGN_GUIDE.md          # Systems design interview prep
│   ├── DAILY_RITUAL.md                  # Alternative workflow options
│   └── HYPOTHESIS_GUIDE.md              # Property-based testing reference
│
├── scripts/
│   ├── setup-git-workflow.sh            # Configure git aliases and tracking
│   ├── weekly-report.sh                 # Generate weekly progress report
│   ├── sprint-report.sh                 # Generate sprint progress report
│   ├── new-fundamental.sh               # Create new systems concept
│   ├── new-design.sh                    # Create new system design
│   └── commit-helper.sh                 # Interactive commit message builder
│
├── packages/
│   ├── runes/                           # Data structures from scratch
│   │   └── src/runes/
│   │       ├── structures/              # Directory per structure
│   │       │   ├── linked_list/
│   │       │   │   ├── __init__.py     # Implementation
│   │       │   │   └── README.md       # Documentation
│   │       │   ├── stack/
│   │       │   ├── queue/
│   │       │   └── ...
│   │       └── algorithms/              # Directory per algorithm category
│   │           ├── sorting/
│   │           ├── searching/
│   │           └── graph/
│   │
│   ├── cantrips/                        # LeetCode solutions
│   │   ├── README.md                    # Main progress dashboard
│   │   └── src/cantrips/
│   │       ├── arrays_strings/
│   │       │   ├── README.md           # Topic progress, patterns
│   │       │   ├── two_pointers.py     # Individual solutions
│   │       │   └── reverse_string.py
│   │       ├── hashing/
│   │       ├── linked_lists/
│   │       ├── stacks_queues/
│   │       ├── trees_graphs/
│   │       ├── heaps/
│   │       └── greedy/
│   │
│   └── incantations/                    # Systems design prep
│       ├── README.md                    # Systems design dashboard
│       └── src/incantations/
│           ├── fundamentals/            # Core concepts
│           │   ├── scaling.py
│           │   ├── caching.py
│           │   ├── databases.py
│           │   └── ...
│           ├── designs/                 # Full system designs
│           │   ├── url_shortener.py
│           │   ├── twitter_feed.py
│           │   ├── youtube.py
│           │   └── ...
│           └── patterns/                # Reusable patterns
│               ├── load_balancing.py
│               ├── sharding.py
│               └── ...
│
├── pyproject.toml                       # Workspace configuration
└── README.md                            # Project overview
```

## Naming Convention

- **Grimoire**: The workspace (book of knowledge)
- **Runes**: Fundamental building blocks (data structures & algorithms)
- **Cantrips**: Simple spells (LeetCode problems)
- **Incantations**: Complex spells (systems designs built from fundamentals)

Theme: Magical/witchy aesthetic for interview prep

Progression: Learn **runes** → Practice **cantrips** → Master **incantations**

## Interview Sprint Mode (Current: 8 Weeks)

**Context**: Preparing for interviews at large tech companies in Jan/Feb. Focus on interview-readiness, not perfection.

### Week-by-Week Focus

**Weeks 1-2**: DSA foundations (Arrays, Strings, Hashing) + Systems fundamentals (scaling, caching, databases)
- 25-30 LeetCode problems (Easy/Medium)
- 3-5 fundamental concepts in `incantations/fundamentals/`

**Weeks 3-4**: DSA depth (Linked Lists, Stacks, Queues, Trees) + First designs
- 25-30 problems (Medium focus)
- 4 easy system designs (URL shortener, Pastebin, Rate limiter)

**Weeks 5-6**: Advanced DSA (Binary Search, DFS/BFS, Heaps, DP) + Complex systems
- 30-35 problems (Medium/Hard)
- 6 medium designs (Twitter, Instagram, Uber, YouTube)

**Weeks 7-8**: Mock interviews + weak areas
- 20-25 problems (review + new)
- Mock system designs with timing
- Practice explaining out loud

### Daily Structure (5-6 hours)
- **Morning (3 hrs)**: 2-3 LeetCode problems + documentation
- **Afternoon (2-3 hrs)**: 1 systems concept/design + Python implementation
- **Evening (30 min)**: Review, commit, set goals

### Target Coverage
- **DSA**: 100-120 problems (70% Medium, 20% Easy, 10% Hard)
- **Systems**: 15-20 full designs, 10-15 fundamentals mastered

**See `docs/SYSTEMS_DESIGN_GUIDE.md` for detailed interview prep strategy.**

## Study Workflow (Long-term Learning)

### Phase 1: Learn & Implement Structure (per topic)

1. **Watch LeetCode video lesson** (e.g., "Arrays and strings")
2. **Take notes** in template's "Study Notes" section
3. **Implement data structure** in `runes/structures/[name]/`
   - Copy `docs/templates/data_structure_template.md` → `README.md`
   - Write class from scratch in `__init__.py`
   - Implement all core operations with docstrings
4. **Fill out README** with complexity, patterns, gotchas discovered

### Phase 2: Practice Easy Problems

5. **Read article problems first** (marked with "A" in LeetCode)
6. **Solve 2-3 Easy problems** from that section
   - Copy `docs/templates/cantrip_template.py`
   - Write solution in `cantrips/[topic]/[problem_name].py`
   - Use snake_case for all Python names (PEP 8)
7. **Update topic README** with problems solved and key insights

### Phase 3: Progress to Medium/Hard

8. **Solve Medium problems** - combine concepts
9. **Tackle Hard problems** - optimizations and advanced variations
10. **Identify patterns** - note when similar techniques reappear

### Phase 4: Move to Next Topic

11. **Review previous topics** periodically (spaced repetition)
12. **Update progress dashboard** in `cantrips/README.md`
13. **Start next section** following LeetCode course order

## Topic Order (LeetCode Course)

1. Arrays & Strings ← Start here
2. Hashing
3. Linked Lists
4. Stacks & Queues
5. Trees & Graphs
6. Heaps
7. Greedy

## Study Partner Agents

The grimoire includes five specialized agents in `.claude/agents/` to support
learning:

### session-starter

**Purpose**: Initialize study sessions **Invoke**: "Start my study session" or
"Invoke session-starter"

**What it does**:

- Reviews yesterday's progress (git log, READMEs)
- Checks current topic status
- Helps set today's specific goal
- Prepares workspace
- < 10 minute setup, then hands off

**Tools**: Read, Glob, Grep (read-only)

### grimoire-keeper

**Purpose**: Progress tracking and accountability partner **Invoke**: "Check in" or
"grimoire-keeper, check in" - any time during day

**What it does**:

- ✅ Tracks daily/weekly/sprint progress via git
- ✅ Provides check-ins throughout the day
- ✅ Structures commit messages for you
- ✅ Shows concrete data (commits, problems, pace)
- ✅ Keeps you accountable without nagging
- ✅ Celebrates wins, points out concerns
- ✅ Minimizes mental overhead (runs git commands for you)
- ❌ Not judgmental, just data-driven

**Key principle**: Objective tracking + supportive accountability

**Tools**: Read, Glob, Grep, Bash (for git commands)

### study-partner

**Purpose**: Guide learning without solving for you **Invoke**: "Invoke
study-partner" or ask naturally when stuck

**What it does**:

- ✅ Asks Socratic questions to guide thinking
- ✅ Helps debug by asking about your logic
- ✅ Explains concepts and complexity analysis
- ✅ Encourages productive struggle
- ✅ Reminds you to document learnings
- ❌ Never writes code or solutions for you
- ❌ Never solves problems directly

**Key principle**: Guide learning, don't do the work

**Tools**: Read, Glob, Grep (read-only, cannot Write/Edit)

### testing-sage

**Purpose**: Property-based testing expert **Invoke**: "Invoke testing-sage" when
you want help with Hypothesis test strategies

**What it does**:

- ✅ Suggests Hypothesis strategies based on problem constraints
- ✅ Recommends properties to test (invariants)
- ✅ Helps translate constraints into test generation code
- ✅ Guides debugging of failing property tests
- ✅ References `docs/HYPOTHESIS_GUIDE.md` for examples
- ❌ Never writes complete test implementations
- ❌ Never solves problems for you

**Key principle**: Teach property-based testing intuition

**Tools**: Read, Glob, Grep (read-only)

### systems-sage

**Purpose**: Systems design expert and guide **Invoke**: "Invoke systems-sage" when
working on system designs or learning distributed systems concepts

**What it does**:

- ✅ Guides through RADIO framework (Requirements, Architecture, Data, Interface, Optimization)
- ✅ Asks Socratic questions about architecture and trade-offs
- ✅ Points out missing considerations and bottlenecks
- ✅ Provides honest, direct feedback (not sycophantic)
- ✅ References real-world systems (Netflix, Uber, Twitter)
- ✅ Helps explain concepts and suggest implementations
- ❌ Never designs complete architectures for you
- ❌ Never draws diagrams without asking questions first

**Key principle**: Guide design thinking, don't design for you

**Tools**: Read, Glob, Grep (read-only)

## Claude Code Skills and Commands

The grimoire includes Claude Code Skills (model-invoked) and Slash Commands
(user-invoked) to optimize agent efficiency and reduce context usage.

### Skills (`.claude/skills/`)

Skills are autonomous capabilities that agents can use without verbose bash
commands. They save ~50,000-100,000 tokens over the 8-week sprint.

**Available skills:**

- **progress-today**: Shows today's git commits for daily check-ins
- **progress-week**: Runs weekly report with comprehensive stats
- **progress-sprint**: Shows 8-week sprint progress vs targets
- **commit-suggest**: Generates properly formatted commit messages
- **test-problem**: Intelligently detects and runs pytest tests

Agents automatically use these skills when appropriate. You don't need to invoke
them manually.

### Slash Commands (`.claude/commands/`)

Slash commands are user-invoked shortcuts that expand to prompts. Type them in
Claude Code for instant workflows.

**Available commands:**

- `/start-session` - Morning kickoff with session-starter agent
- `/check-in` - Quick progress check (shows today's commits)
- `/commit-dsa` - Commit DSA work with proper formatting
- `/commit-systems` - Commit systems work with proper formatting
- `/weekly-review` - Sunday review with comprehensive stats
- `/design` - Start system design session with systems-sage

Example usage:
```
/check-in
```

Expands to a prompt that shows today's progress with commit counts and
assessment.

### When to Use Agents

- **Start of day**: Use session-starter to get organized
- **Any time check-in**: Use grimoire-keeper to see progress, get accountability
- **Stuck on DSA problem (15-30 min)**: Invoke study-partner for guidance
- **Stuck on systems design**: Invoke systems-sage for architecture questions
- **Need concept explanation**: Ask study-partner (DSA) or systems-sage (distributed systems)
- **Debugging your code**: study-partner asks about your logic
- **Ready to commit**: Use grimoire-keeper to structure commit message
- **Want property-based tests**: Invoke testing-sage for Hypothesis strategies
- **Practicing system design**: Use systems-sage to simulate interviewer questions
- **End of session**: Use grimoire-keeper for daily review, set tomorrow's goals
- **Weekly review**: Use grimoire-keeper for progress analysis and planning

See `docs/DAILY_RITUAL.md` for integration with daily workflow.

## Import Structure

### Runes (Hybrid approach)

```python
# Option 1: Direct import of common items
from runes import LinkedList, Stack, binary_search

# Option 2: Namespace import
from runes import structures, algorithms
structures.LinkedList()
algorithms.binary_search()

# Option 3: Specific submodule
from runes.structures.linked_list import LinkedList
from runes.algorithms.sorting import merge_sort
```

### Cantrips (Organized by topic)

```python
# Solutions are standalone files
from cantrips.arrays_strings.two_pointers import Solution
```

## Key Principles

1. **Implement from scratch** - No copying, write everything for learning
2. **Document thoroughly** - Use templates, fill in all sections
3. **Track progress** - Update READMEs and checkboxes regularly
4. **Note patterns** - Identify recurring techniques across problems
5. **Link concepts** - Connect cantrips back to related runes
6. **Guide, don't solve** - Agents help the user learn, never do work for them

## Templates Usage

### Structure Template (`docs/templates/structure.md`)

- Use for each new structure in `runes/structures/[name]/README.md`
- Fill in: complexity, operations, patterns, interview tips, LeetCode problems
- Add personal notes in "Study Notes" section

### Algorithm Template (`docs/templates/algorithm.md`)

- Use for algorithms in `runes/algorithms/[category]/README.md`
- Fill in: approach, pseudocode, complexity, variations, proof (if needed)

### Cantrip Template (`docs/templates/cantrip.py`)

- Use for each LeetCode problem solution
- Copy to `cantrips/[topic]/[problem_name].py`
- Include: problem description, approach, implementation, tests, lessons learned
- **Important**: Use snake_case for all Python identifiers (PEP 8)

### Topic Template (`docs/templates/topic.md`)

- Already created for each cantrip subdirectory
- Update as you solve problems: check boxes, add insights, track time

## Python Conventions

- **Classes**: `PascalCase` (e.g., `Solution`, `LinkedList`)
- **Functions/methods**: `snake_case` (e.g., `problem_name`, `add_front`)
- **Variables**: `snake_case` (e.g., `input_data`, `max_sum`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_SIZE`)

## Progress Tracking

1. **Main dashboard**: `cantrips/README.md` - Overview of all topics
2. **Topic READMEs**: `cantrips/src/cantrips/[topic]/README.md` - Detailed per topic
3. **Structure READMEs**: `runes/structures/[name]/README.md` - Per data structure

Update checkboxes and counts as you complete problems and implementations.

## When Helping the User

- **Use agents appropriately**: Defer to session-starter/study-partner/testing-sage/systems-sage when applicable
- **Naming**: Respect the grimoire/runes/cantrips/incantations theme
- **Implementation**: User wants to write code themselves for learning
- **Guide, don't solve**: Ask questions, don't give solutions (like study-partner)
- **Templates**: Suggest using simplified template names (cantrip.py, fundamental.py, design.py, etc.)
- **Progress**: Help update READMEs and track completed work
- **Patterns**: Help identify and document recurring techniques
- **Connections**: Link problems to related data structures in runes, and systems concepts to incantations
- **Interview focus**: User is in 8-week sprint mode - prioritize interview-readiness over perfection
- **Python for speed**: Keep all implementations in Python for fast iteration during sprint

## Common Tasks

### Adding a new data structure

1. Create `runes/structures/[name]/` directory
2. Copy `docs/templates/structure.md` → `README.md`
3. Create `__init__.py` with implementation
4. Update `runes/structures/__init__.py` to export it
5. Update `runes/__init__.py` if it's commonly used

### Adding a new cantrip solution

1. Copy `docs/templates/cantrip.py`
2. Save as `cantrips/[topic]/[problem_name].py`
3. Implement solution with proper documentation
4. Update `cantrips/[topic]/README.md` checkbox
5. Update `cantrips/README.md` progress counts

### Starting a new study session

1. User says: "Start my study session" or invokes session-starter
2. session-starter reviews progress and helps set goals
3. User works independently or with study-partner guidance
4. At end, commit work and update documentation

### Creating a new algorithm category

1. Create `runes/algorithms/[category]/` directory
2. Add algorithm implementations as separate files or subdirectories
3. Update `runes/algorithms/__init__.py` to export them

### Adding property-based tests to a cantrip

1. Invoke testing-sage or reference `docs/HYPOTHESIS_GUIDE.md`
2. Uncomment Hypothesis imports in the cantrip file
3. Uncomment and modify the property test template
4. Adjust strategy to match problem constraints
5. Write properties (invariants) to test, not exact outputs
6. Run tests to discover edge cases

### Adding a systems design fundamental

1. Copy `docs/templates/fundamental.py`
2. Save as `incantations/fundamentals/[concept_name].py`
3. Document concept, variations, trade-offs
4. Implement key algorithms in Python (e.g., LRU cache, consistent hashing)
5. Include real-world examples and interview tips
6. Update `incantations/README.md` progress tracker

### Adding a full system design

1. Copy `docs/templates/design.py`
2. Save as `incantations/designs/[system_name].py`
3. Work through: requirements, estimation, high-level design, deep dive
4. Implement core algorithm/data structure in Python
5. Document trade-offs and follow-up questions
6. Practice explaining out loud (record yourself!)
7. Update `incantations/README.md` progress tracker

## File Organization Best Practices

- One data structure per directory in runes (allows for README, examples, variations)
- One problem per file in cantrips (clear separation)
- Use descriptive filenames matching problem names (snake_case)
- Keep implementations self-contained but link to runes when relevant

## Notes

- This is a learning project - prioritize understanding over efficiency
- User implements everything from scratch for educational purposes
- Templates ensure consistent documentation and tracking
- Witchy theme keeps it fun and memorable
