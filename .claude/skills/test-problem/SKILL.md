---
name: test-problem
description: Intelligently detects and runs tests for current work. Use when user says "test this", "run tests", or wants to verify their solution. Automatically finds the right pytest command based on files changed.
---

# Smart Test Runner

This skill detects what you're working on and runs the appropriate tests.

## When to Use

Use this skill when:
- User says "test this" or "run tests"
- User asks "does my solution work?"
- After implementing a solution
- User wants to verify their code

## What It Does

1. Checks `git status` or `git diff` to see what files changed
2. Detects if it's a cantrip (DSA) or incantation (systems)
3. Extracts topic and problem name from file path
4. Runs appropriate pytest command
5. Shows results

## Detection Logic

### For Cantrips (DSA):
Path pattern: `packages/cantrips/src/cantrips/<topic>/<problem>.py`

Extract:
- topic: arrays_strings, hashing, linked_lists, etc.
- problem: two_sum, reverse_string, etc.

Run:
```bash
uv run pytest packages/cantrips/src/cantrips/<topic>/<problem>.py -v
```

### For Incantations (Systems):
These typically don't have automated tests, but may have examples.

Check for:
- Implementation examples in the file
- Run any `if __name__ == "__main__"` blocks
- Or inform user that manual testing is needed

## How to Use

1. Check what's changed:
```bash
git status --short
```

2. If single file changed:
   - Extract path components
   - Run pytest on that file

3. If multiple files:
   - Ask user which to test, or
   - Test all changed files

4. Show output with color (pytest -v shows verbose)

## Example Interactions

**User:** "Test this"

**Skill detects:**
- File: packages/cantrips/src/cantrips/arrays_strings/two_sum.py

**Runs:**
```bash
uv run pytest packages/cantrips/src/cantrips/arrays_strings/two_sum.py -v
```

**Shows:**
```
=== test session starts ===
test_two_sum PASSED [100%]
=== 1 passed in 0.05s ===
✅ All tests passed!
```

## Alternatives

If no changes detected:
- "No changes detected. What would you like to test?"
- Suggest: `just test-all` for full test suite
- Suggest: `just test-topic <topic>` for topic tests

## Notes

- Uses pytest with -v flag for verbose output
- Assumes tests are in same file as implementation (per grimoire template)
- Can fall back to justfile commands if detection fails
- Always shows full pytest output (don't hide failures!)
