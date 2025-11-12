<p align="center">
  <img src="assets/grimoire.gif" alt="Grimoire" width="200">
</p>

<h1 align="center">𝔊ℜ𝔐𝔒ℑℜ𝔈</h1>

<p align="center">
  <em>A structured workspace for interview preparation through hands-on implementation<br>
  of data structures, algorithms, and LeetCode problems.</em>
</p>

<hr>

## Quick Start

```bash
# View available commands
just help

# Create a new problem solution
just cantrip-array reverse_string

# Run tests
just test-array reverse_string
```

## What's Inside

**Runes** - Data structures and algorithms implemented from scratch for deep
understanding.

**Cantrips** - LeetCode problem solutions organized by topic with test cases and
complexity analysis.

## Workflow

The grimoire follows a learn-by-doing approach:

1. **Learn** - Watch LeetCode video lessons, take notes
2. **Implement** - Build data structures from scratch in `runes/`
3. **Practice** - Solve related problems in `cantrips/`
4. **Test** - Verify solutions with pytest
5. **Reflect** - Document patterns and insights

## Project Structure

```
grimoire/
├── packages/
│   ├── runes/           # Data structures & algorithms
│   │   ├── structures/  # LinkedList, Stack, Queue, etc.
│   │   └── algorithms/  # Sorting, searching, graph algorithms
│   │
│   └── cantrips/        # LeetCode solutions by topic
│       └── src/cantrips/
│           ├── arrays_strings/
│           ├── hashing/
│           ├── linked_lists/
│           └── ...
│
├── docs/
│   └── templates/       # Templates for new implementations
│
└── justfile             # Task automation recipes
```

## Creating Solutions

Each cantrip follows a consistent structure:

- Problem description and constraints
- Approach and complexity analysis
- Implementation with type hints
- Test cases using pytest
- Reflections and alternative approaches

```bash
# Create from template
just cantrip-array <problem_name>

# The template includes:
# - Problem description section
# - TEST_CASES constant (single source of truth)
# - Parametrized pytest tests
# - Reflections section
```

## Testing

Tests live alongside implementations using pytest's parametrize feature:

```bash
# Test a specific problem
just test-array reverse_string

# Test all problems in a topic
just test-topic arrays_strings

# Test everything
just test-all
```

## Topic Organization

Problems follow the LeetCode course structure:

1. Arrays & Strings
2. Hashing
3. Linked Lists
4. Stacks & Queues
5. Trees & Graphs
6. Heaps
7. Greedy

View available topics: `just topics`

## Progress Tracking

Each topic has a README with:

- Problem checklist with completion status
- Key patterns and insights
- Common mistakes and learnings
- Links to related data structures in runes

## Development

Built with:

- **Python 3.12+** for implementations
- **pytest** for testing
- **uv** for dependency management
- **just** for task automation

## Philosophy

This workspace prioritizes understanding over completion. Each implementation is
written from scratch to build intuition. Solutions are documented thoroughly to
capture learnings and patterns that emerge across problems.

## Additional Resources

- See `docs/DAILY_RITUAL.md` for the recommended daily workflow
- Templates in `docs/templates/` provide structure for new implementations
- Check `CLAUDE.md` for AI assistant context and study partner usage
