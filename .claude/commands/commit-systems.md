---
description: Commit systems design (incantations) work with proper formatting
---

Help me commit my systems design work following grimoire conventions.

1. Check what incantation files have changed
2. Generate a properly formatted commit message following the pattern:
   `incantations(type): concept-or-design-name`
3. Provide the exact git commands to stage and commit the work

Example format:
```
incantations(fundamentals): lru-cache with OrderedDict

Implemented LRU using OrderedDict for O(1) operations.
Also explored doubly-linked list approach.
```
