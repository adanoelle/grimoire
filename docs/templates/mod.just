# [PATTERN NAME] - Pattern-Specific Module Commands
#
# This module provides granular control for advanced kata practice.
#
# Usage from root justfile:
#   just [pattern-name]::test-one TestKata1
#   just [pattern-name]::test-examples
#   just [pattern-name]::cycle
#
# Pattern recognition reinforcement:
#   Pattern: [DESCRIBE THE TECHNIQUE]
#   When to use: [CONDITIONS THAT TRIGGER THIS PATTERN]
#   Example problems: [LEETCODE PROBLEM NUMBERS]

# Run all tests for this pattern
test:
    pytest test_kata.py -v

# Test specific kata class (for targeted debugging)
test-one KATA:
    pytest test_kata.py::{{KATA}} -v

# Test by difficulty level (matches pytest marks)
test-kata1:
    pytest test_kata.py -m kata1 -v

test-kata2:
    pytest test_kata.py -m kata2 -v

test-kata3:
    pytest test_kata.py -m kata3 -v

test-kata4:
    pytest test_kata.py -m kata4 -v

test-kata5:
    pytest test_kata.py -m kata5 -v

# Test by category (reinforces what to check in interviews)
test-examples:
    pytest test_kata.py -k "leetcode_examples" -v

test-edges:
    pytest test_kata.py -k "edge_cases" -v

test-constraints:
    pytest test_kata.py -k "constraints" -v

# Open for practice (uses Helix)
practice:
    hx kata.py

# Reset using CLI (consistent with main workflow)
# REPLACE [pattern-name] with actual pattern (e.g., opposite_ends)
reset:
    uv run runes kata reset [pattern-name]

# Full cycle: test → auto-reset if all pass
# REPLACE [pattern-name] with actual pattern
cycle:
    @pytest test_kata.py -v && echo "\n✅ All tests passed! Resetting..." && uv run runes kata reset [pattern-name] -f || echo "\n❌ Tests failed - fix bugs first"

# Show help for this pattern
help:
    @echo "[PATTERN NAME] - Pattern Commands"
    @echo ""
    @echo "Testing:"
    @echo "  just test              # Run all tests"
    @echo "  just test-one NAME     # Test specific kata class"
    @echo "  just test-kata1        # Test difficulty level 1"
    @echo "  just test-examples     # LeetCode examples only"
    @echo "  just test-edges        # Edge cases only"
    @echo ""
    @echo "Workflow:"
    @echo "  just practice          # Open in Helix"
    @echo "  just reset             # Reset to 'pass'"
    @echo "  just cycle             # Test + auto-reset"
