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
# 
# just cantrip-array reverse_string
# # ... implement solution ...
# just test-array reverse_string
#
# Test all problems in a topic:
# 
# just test-topic arrays_strings
#
# Run all tests:
# just test-all

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
    @echo ""
    @echo "  1. View all commands:        just"
    @echo "  2. Create a new problem:     just cantrip-array <problem_name>"
    @echo "  3. Implement your solution in the opened file"
    @echo "  4. Test your solution:       just test-array <problem_name>"
    @echo "  5. View available topics:    just topics"
    @echo ""
    @echo "Common Workflows:"
    @echo ""
    @echo "Create and test:"
    @echo "  just cantrip-array reverse_string"                   
    @echo "  # ... implement solution ..."
    @echo "  just test-array reverse_string"
    @echo ""
    @echo "Test a topic:"
    @echo ""
    @echo "  just test-topic arrays_strings"
    @echo "  Test everything:    just test-all"
    @echo ""
    @echo "Available topic shortcuts:"
    @echo ""
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

# ============================================================================
# Systems Design (Incantations)
# ============================================================================
# Commands for systems design practice and implementation

# Create a new fundamental systems concept
# Example: just fundamental lru-cache
fundamental name:
    @./scripts/new-fundamental.sh {{name}}

# Create a new system design
# Example: just design url-shortener
design name:
    @./scripts/new-design.sh {{name}}

# List all fundamentals
fundamentals:
    @echo "Fundamental concepts:"
    @ls -1 packages/incantations/src/incantations/fundamentals 2>/dev/null | grep -v "^__" | sed 's/\.py$//' | sed 's/^/  - /' || echo "  (none yet)"

# List all system designs
designs:
    @echo "System designs:"
    @ls -1 packages/incantations/src/incantations/designs 2>/dev/null | grep -v "^__" | sed 's/\.py$//' | sed 's/^/  - /' || echo "  (none yet)"

# Run a fundamental concept (if it has __main__ block)
# Example: just run-fundamental lru_cache
run-fundamental name:
    @uv run python packages/incantations/src/incantations/fundamentals/{{name}}.py

# Run a system design (if it has __main__ block)
# Example: just run-design url_shortener
run-design name:
    @uv run python packages/incantations/src/incantations/designs/{{name}}.py

# ============================================================================
# Progress Tracking
# ============================================================================
# Git-based progress tracking and accountability

# Show today's commits and progress
today:
    @echo "📊 Today's Progress:"
    @echo ""
    @git log --oneline --since="1 day ago" --no-merges || echo "No commits today yet"
    @echo ""
    @echo "DSA commits: $(git log --oneline --since='1 day ago' --grep='cantrips' --no-merges | wc -l | tr -d ' ')"
    @echo "Systems commits: $(git log --oneline --since='1 day ago' --grep='incantations' --no-merges | wc -l | tr -d ' ')"

# Show this week's progress
week:
    @./scripts/weekly-report.sh

# Show overall sprint progress (requires sprint start date)
# Example: just sprint 2024-12-20
sprint start-date:
    @./scripts/sprint-report.sh {{start-date}}

# Quick status check
status:
    @echo "Current status:"
    @git status --short
    @echo ""
    @echo "Recent work:"
    @git log --oneline -5

# ============================================================================
# Git Workflow Helpers
# ============================================================================
# Streamlined git operations for study workflow

# Interactive commit helper with smart message generation
commit:
    @./scripts/commit-helper.sh

# Quick commit for DSA work (auto-detect files and generate message)
commit-dsa:
    @echo "Committing DSA work..."
    @git add packages/cantrips/
    @./scripts/commit-helper.sh

# Quick commit for systems work (auto-detect files and generate message)
commit-systems:
    @echo "Committing systems design work..."
    @git add packages/incantations/
    @./scripts/commit-helper.sh

# Show git log with nice formatting
log:
    @git log --oneline --graph --decorate -20

# Show what changed today
diff-today:
    @git diff --stat @{1.day.ago}..HEAD

# ============================================================================
# Session Management
# ============================================================================
# Daily study session helpers

# Start a study session (morning kickoff)
start:
    @echo "🔮 Starting study session..."
    @echo ""
    @just today
    @echo ""
    @echo "Ready to work! Use 'just check-in' anytime to see progress."

# Quick check-in during study session
check-in:
    @just today

# End of day review
review:
    @echo "📝 Daily Review:"
    @echo ""
    @just today
    @echo ""
    @just status
    @echo ""
    @echo "Don't forget to commit your work if you haven't already!"

# Sunday weekly review
weekly:
    @just week

# ============================================================================
# Quick Workflows
# ============================================================================
# Common multi-step workflows combined

# Create and test a cantrip in one go (opens editor, then prompts for test)
# Example: just work-array reverse_string
work-array problem:
    @just cantrip-array {{problem}}
    @echo ""
    @echo "When ready to test, run: just test-array {{problem}}"

work-hash problem:
    @just cantrip-hash {{problem}}
    @echo ""
    @echo "When ready to test, run: just test-hash {{problem}}"

work-linked problem:
    @just cantrip-linked {{problem}}
    @echo ""
    @echo "When ready to test, run: just test-linked {{problem}}"

# Clean up Python cache files
clean:
    @find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    @find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    @echo "✅ Cleaned up Python cache files"
