---
name: commit-suggest
description: Generates properly formatted commit messages based on git changes. Use when user says "ready to commit", "I finished [work]", or needs help with commit message. Follows grimoire conventions (cantrips/incantations).
---

# Commit Message Generator

This skill helps structure commit messages according to grimoire conventions.

## When to Use

Use this skill when:
- User says "ready to commit" or "I finished [work]"
- User asks "how should I commit this?"
- grimoire-keeper needs to suggest commit message
- User has staged or unstaged changes

## What It Does

1. Checks what files changed (`git status`, `git diff --stat`)
2. Determines type (cantrips vs incantations)
3. Extracts topic/scope from file paths
4. Generates properly formatted message
5. Provides exact git command to run

## Commit Message Format

### For DSA (cantrips):
```
cantrips(<topic>): <problem1>, <problem2> [optional pattern]

[optional body with insights]
```

Example:
```
cantrips(arrays): two-sum, container-water [two-pointers]

Practiced two-pointers on sorted arrays.
- two-sum: O(n) with opposite ends approach
- container-water: Greedy, always move shorter side

Time: ~90 min. Pattern clicking!
```

### For Systems (incantations):
```
incantations(<type>): <concept-or-design-name>

[optional body with details]
```

Example:
```
incantations(fundamentals): lru-cache with OrderedDict

Implemented LRU using OrderedDict for O(1) operations.
Also explored doubly-linked list approach.
```

## How to Use

1. Check current changes:
```bash
git status
git diff --name-only
```

2. Identify pattern:
- `packages/cantrips/src/cantrips/<topic>/` → cantrips(<topic>)
- `packages/incantations/src/incantations/<type>/` → incantations(<type>)
- Extract filenames (without .py) as problem/concept names

3. Generate message following format above

4. Provide exact command:
```bash
git add <appropriate path>
git commit -m "<generated message>"
```

## Tips

- Keep subject line under 72 characters
- Use present tense ("add" not "added")
- Mention patterns in brackets when relevant: [two-pointers], [bfs], [dp]
- Include time and insights in body when interesting
- Group related problems in one commit

## Notes

- Follows conventional commits style adapted for grimoire
- Helps maintain consistent git history
- Makes progress tracking easier
- Future you will appreciate clear commit messages
