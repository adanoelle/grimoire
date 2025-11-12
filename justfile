# Grimoire - Just recipes for interview prep workflow
#
# Quick Start Guide:
# ------------------
# 1. View all commands:           just
# 2. Create a new problem:        just cantrip-array <problem_name>
# 3. Implement your solution in the opened file
# 4. Test your solution:          just test-array <problem_name>
# 5. View available topics:       just topics
#
# Common Workflows:
# ------------------
# Create and test a problem:
#   just cantrip-array reverse_string
#   # ... implement solution ...
#   just test-array reverse_string
#
# Test all problems in a topic:
#   just test-topic arrays_strings
#
# Run all tests:
#   just test-all

# ============================================================================
# Main Commands
# ============================================================================

# Show all available commands (default)
default:
    @just --list

# Show quick start guide and common workflows
help:
    @echo "Grimoire - Interview Prep Workflow"
    @echo ""
    @echo "Quick Start:"
    @echo "  1. View all commands:        just"
    @echo "  2. Create a new problem:     just cantrip-array <problem_name>"
    @echo "  3. Implement your solution in the opened file"
    @echo "  4. Test your solution:       just test-array <problem_name>"
    @echo "  5. View available topics:    just topics"
    @echo ""
    @echo "Common Workflows:"
    @echo "  Create and test:    just cantrip-array reverse_string"
    @echo "                      # ... implement solution ..."
    @echo "                      just test-array reverse_string"
    @echo ""
    @echo "  Test a topic:       just test-topic arrays_strings"
    @echo "  Test everything:    just test-all"
    @echo ""
    @echo "Available topic shortcuts:"
    @echo "  cantrip-array, cantrip-hash, cantrip-linked, cantrip-stack,"
    @echo "  cantrip-tree, cantrip-heap, cantrip-greedy"
    @echo ""
    @echo "Run 'just topics' to see all available topics."

# List all available cantrip topics (arrays_strings, hashing, etc.)
topics:
    @echo "Available cantrip topics:"
    @ls -1 packages/cantrips/src/cantrips | grep -v "^__" | sed 's/^/  - /'

# ============================================================================
# Creating Cantrips (LeetCode Solutions)
# ============================================================================
# Use these commands to create new problem solutions from the template.
# The script will copy the template and optionally open it in your $EDITOR.

# Create a new cantrip from template
# Arguments: <topic> <problem_name>
# Example: just cantrip arrays_strings reverse_string
cantrip topic problem:
    @./scripts/new-cantrip.sh {{topic}} {{problem}}

# Topic shortcuts - faster way to create cantrips for common topics
# Usage: just cantrip-<topic> <problem_name>
# Examples:
#   just cantrip-array reverse_string
#   just cantrip-hash two_sum
#   just cantrip-linked merge_two_lists
cantrip-array problem: (cantrip "arrays_strings" problem)
cantrip-hash problem: (cantrip "hashing" problem)
cantrip-linked problem: (cantrip "linked_lists" problem)
cantrip-stack problem: (cantrip "stacks_queues" problem)
cantrip-tree problem: (cantrip "trees_graphs" problem)
cantrip-heap problem: (cantrip "heaps" problem)
cantrip-greedy problem: (cantrip "greedy" problem)

# ============================================================================
# Testing Cantrips
# ============================================================================
# Run pytest tests for your implemented solutions. Tests are defined in the
# TEST_CASES constant within each cantrip file.

# Run pytest for a specific cantrip
# Arguments: <topic> <problem_name>
# Example: just test arrays_strings reverse_string
test topic problem:
    @uv run pytest packages/cantrips/src/cantrips/{{topic}}/{{problem}}.py -v

# Run all tests in a specific topic directory
# Useful after solving multiple problems in one topic
# Example: just test-topic arrays_strings
test-topic topic:
    @uv run pytest packages/cantrips/src/cantrips/{{topic}}/ -v

# Run all cantrip tests across all topics
# Good for verification before committing
test-all:
    @uv run pytest packages/cantrips/src/cantrips/ -v

# Topic shortcuts - faster way to test cantrips for common topics
# Usage: just test-<topic> <problem_name>
# Examples:
#   just test-array reverse_string
#   just test-hash two_sum
#   just test-linked merge_two_lists
test-array problem: (test "arrays_strings" problem)
test-hash problem: (test "hashing" problem)
test-linked problem: (test "linked_lists" problem)
test-stack problem: (test "stacks_queues" problem)
test-tree problem: (test "trees_graphs" problem)
test-heap problem: (test "heaps" problem)
test-greedy problem: (test "greedy" problem)
