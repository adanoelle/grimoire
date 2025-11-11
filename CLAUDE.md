# Grimoire - Claude Context Document

This document provides context about the grimoire workspace structure and study
workflow for AI assistants.

## Project Overview

**Grimoire** is a personal interview preparation workspace containing:

- **Runes**: Data structures and algorithms implemented from scratch
- **Cantrips**: LeetCode problem solutions organized by topic

The goal is hands-on learning through implementation and practice, following the
LeetCode DSA course structure.

## Workspace Structure

```
grimoire/
├──  claude/
│   └── agents/
│       ├── session-starter.md           # Start study sessions
│       └── study-partner.md             # Learning guidance agent
│
├── docs/
│   ├── templates/
│   │   ├── structure.md                 # Data structure template
│   │   ├── algorithm.md                 # Algorithm template
│   │   ├── cantrip.py                   # LeetCode solution template
│   │   └── topic.md                     # Topic progress template
│   └── DAILY_RITUAL.md                  # Daily study workflow
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
│   └── cantrips/                        # LeetCode solutions
│       ├── README.md                    # Main progress dashboard
│       └── src/cantrips/
│           ├── arrays_strings/
│           │   ├── README.md           # Topic progress, patterns
│           │   ├── two_pointers.py     # Individual solutions
│           │   └── reverse_string.py
│           ├── hashing/
│           ├── linked_lists/
│           ├── stacks_queues/
│           ├── trees_graphs/
│           ├── heaps/
│           └── greedy/
│
├── pyproject.toml                       # Workspace configuration
└── README.md                            # Project overview
```

## Naming Convention

- **Grimoire**: The workspace (book of knowledge)
- **Runes**: Fundamental building blocks (data structures & algorithms)
- **Cantrips**: Practice spells (LeetCode problems)

Theme: Magical/witchy aesthetic for interview prep

## Study Workflow

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

The grimoire includes two specialized agents in `.claude/agents/` to support
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

### When to Use Agents

- **Start of session**: Use session-starter to get organized
- **Stuck on problem (15-30 min)**: Invoke study-partner for guidance
- **Need concept explanation**: Ask study-partner
- **Debugging your code**: study-partner asks about your logic
- **End of session**: Agents remind you to commit and update READMEs

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

- **Use agents appropriately**: Defer to session-starter/study-partner when
  applicable
- **Naming**: Respect the grimoire/runes/cantrips theme
- **Implementation**: User wants to write code themselves for learning
- **Guide, don't solve**: Ask questions, don't give solutions (like study-partner)
- **Templates**: Suggest using simplified template names (structure.md, cantrip.py,
  etc.)
- **Progress**: Help update READMEs and track completed work
- **Patterns**: Help identify and document recurring techniques
- **Connections**: Link problems to related data structures in runes

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
