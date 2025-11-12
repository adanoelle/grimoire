# Grimoire - Just recipes for interview prep workflow

# Default recipe - show available commands
default:
    @just --list

# Create a new cantrip (LeetCode solution) from template
# Usage: just cantrip arrays_strings reverse_string
cantrip topic problem:
    @./scripts/new-cantrip.sh {{topic}} {{problem}}

# Quick shortcut for arrays_strings topic
cantrip-array problem:
    @just cantrip arrays_strings {{problem}}

# Quick shortcut for hashing topic
cantrip-hash problem:
    @just cantrip hashing {{problem}}

# Quick shortcut for linked_lists topic
cantrip-linked problem:
    @just cantrip linked_lists {{problem}}

# Quick shortcut for stacks_queues topic
cantrip-stack problem:
    @just cantrip stacks_queues {{problem}}

# Quick shortcut for trees_graphs topic
cantrip-tree problem:
    @just cantrip trees_graphs {{problem}}

# Quick shortcut for heaps topic
cantrip-heap problem:
    @just cantrip heaps {{problem}}

# Quick shortcut for greedy topic
cantrip-greedy problem:
    @just cantrip greedy {{problem}}

# List all available topics
topics:
    @echo "Available cantrip topics:"
    @ls -1 packages/cantrips/src/cantrips | grep -v "^__" | sed 's/^/  - /'
