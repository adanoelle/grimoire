# Runes

> Fundamental data structures and algorithms implemented from scratch

## What's Inside

**Data Structures** (`structures/`)
- LinkedList, Stack, Queue, Tree, Graph, etc.
- Each implemented from scratch for deep understanding
- Comprehensive documentation and complexity analysis

**Algorithm Katas** (`algorithms/`)
- Daily practice drills for building muscle memory
- Core patterns: two pointers, sliding window, binary search, etc.
- Interactive practice system with timing and progress tracking

## Kata Practice System

The kata system helps you master algorithmic patterns through deliberate practice.

### Quick Start

**Interactive Menu (Recommended for beginners):**
```bash
runes kata menu
```

The interactive menu guides you through:
1. Select a pattern to practice
2. Opens in your editor with automatic timer
3. Run tests when you're ready (pytest with markers)
4. Log your session (time, bugs, notes)
5. View progress and mastery status

**What gets tracked:**
- Practice session history with dates
- Best times per kata
- Bug counts (helps identify weak areas)
- Mastery progression (Learning → Practicing → Mastered)

### Directory Structure

```
algorithms/
├── two_pointers/
│   ├── opposite_ends/
│   │   ├── __init__.py     # Reference templates (study these)
│   │   ├── kata.py         # Practice problems (code from memory)
│   │   ├── test_kata.py    # Pytest tests with markers
│   │   ├── README.md       # Pattern guide
│   │   └── mod.just        # Pattern-specific commands
│   └── fast_slow/
│
├── searching/
│   └── binary_search/
│
└── sliding_window/
    ├── fixed_window/       # Fixed-size windows (max sum, etc.)
    └── variable_window/    # Variable-size (longest substring)
```

### The Practice Workflow

**Philosophy:** Musicians practice scales, athletes drill fundamentals. You practice katas.

**Daily ritual:**
1. **Morning warmup (5-10 min):** Practice 2-3 katas from your current focus pattern
2. **LeetCode practice (45-60 min):** Apply the pattern in real problems
3. **Evening reinforcement (5 min):** Repeat katas from patterns used today

**Why this works:**
- Kata first → Fresh muscle memory
- LeetCode second → Immediate application
- Spaced repetition → Pattern becomes automatic

### Migration Status

**Migrated to pytest:**
- ✅ sliding_window/fixed_window (5 katas)
- ✅ sliding_window/variable_window (5 katas)
- ✅ two_pointers/opposite_ends (5 katas)

**Legacy (still uses doctest):**
- ⚠️ searching/binary_search
- ⚠️ two_pointers/fast_slow

*Pytest migration brings better test organization, granular test selection, and improved error messages.*

### Available Patterns

View all available patterns:
```bash
runes kata list
```

Each pattern includes:
- Comprehensive README with theory and examples
- Reference implementations in `__init__.py`
- Practice problems in `kata.py`
- Pytest tests with markers (`kata1`, `kata2`, etc.)
- Mastery tracking and progress logs

### Safety Features

**Automatic backups:**
- Every reset creates a timestamped backup
- Backups stored in `.kata_backups/`
- Never lose your practice logs or notes

**Undo capability:**
```bash
runes kata undo  # Restore most recent backup
```

**Dry-run mode:**
```bash
runes kata reset <pattern> --dry-run  # Preview without changes
```

### Testing with Pytest Markers

Migrated patterns use pytest markers for granular test selection:

```bash
# Run all tests for a pattern
runes kata test sliding-window/fixed-window

# Run just kata 1
runes kata test sliding-window/fixed-window -k 1

# Run katas 1 and 2
runes kata test sliding-window/fixed-window -m "kata1 or kata2"

# Run with verbose output
runes kata test sliding-window/fixed-window -v -k 1
```

**Available markers:**
- `kata1`, `kata2`, `kata3`, `kata4`, `kata5` - Individual katas
- `examples` - LeetCode example test cases
- `edge` - Edge case tests

### Pattern READMEs

Each pattern directory contains a comprehensive README:
- **Pattern Overview:** Core concept and visualization
- **When to Use:** Recognition criteria and anti-patterns
- **Complexity:** Time/space analysis
- **The Template:** Reusable code structure
- **Common Variations:** Problem categories and examples
- **Interview Tips:** What to say, common pitfalls
- **Progression Path:** Learning sequence
- **Related LeetCode Problems:** Practice problems by difficulty
- **Mastery Checklist:** Self-assessment guide

**Example:** `algorithms/sliding_window/fixed_window/README.md`

### Mastery Progression

**Learning (Weeks 1-2):**
- Study templates (`__init__.py`)
- Code katas with reference open
- Focus on understanding

**Practicing (Weeks 2-3):**
- Code katas from memory
- Small bugs acceptable
- Redo next day

**Refining (Weeks 3-4):**
- Zero bugs consistently
- Under target times
- Explain while coding

**Mastered (Week 4+):**
- Pattern is muscle memory
- Instant recognition in problems
- Can teach others

### Justfile Integration

For users who prefer justfile commands:

```bash
# Interactive menu
just kata::menu

# List patterns
just kata::list

# Practice (opens editor, runs timer)
just kata::practice two-pointers/opposite-ends

# Test (runs pytest)
just kata::test sliding-window/fixed-window

# Reset (with confirmation)
just kata::reset sliding-window/fixed-window

# Reset all (dangerous!)
just kata::reset-all
```

### Learn More

- **Philosophy and strategy:** `../../docs/KATA_PRACTICE.md`
- **Daily workflow integration:** `../../docs/DAILY_WORKFLOW.md`
- **Kata coach (AI):** Use `/kata` slash command in Claude Code

---

**Ready to start?**

```bash
runes kata menu
```

Pick your first pattern and practice! 🥋
