# Sliding Window: Fixed Size - Pattern-Specific Commands
#
# Pattern: Maintain window of exactly k elements, slide one position at a time
# When to use: Process all subarrays of exact size k, max/min/avg of k consecutive elements
# Example problems: LC 643 (Max Average), LC 1343 (Threshold Count), LC 438 (Find Anagrams)
#
# Usage from root:
#   just fixed-window::test-one TestKata1MaxAverage
#   just fixed-window::cycle
#
# Recognition triggers:
#   ✓ Problem mentions "subarray of size k" or "k consecutive elements"
#   ✓ Need to process ALL windows of fixed size
#   ✓ Can maintain window state incrementally (sum, frequency, etc.)
#   ✓ O(n) time required (can't recalculate entire window each time)

# Run all tests for this pattern
test:
    pytest test_kata.py -v

# Test specific kata class (for targeted debugging)
test-one KATA:
    pytest test_kata.py::{{KATA}} -v

# Test by difficulty level
test-kata1:
    pytest test_kata.py -m kata1 -v

test-kata2:
    pytest test_kata.py -m kata2 -v

# Test by category (reinforces interview thinking)
test-examples:
    pytest test_kata.py -k "examples" -v

test-edges:
    pytest test_kata.py -k "edge_cases" -v

test-properties:
    pytest test_kata.py -k "Properties" -v

# Open for practice
practice:
    hx kata.py

# Reset using CLI (consistent with main workflow)
reset:
    uv run runes kata reset sliding_window/fixed_window

# Full cycle: test → auto-reset if all pass
cycle:
    @pytest test_kata.py -v && echo "\n✅ All tests passed! Resetting..." && uv run runes kata reset sliding_window/fixed_window -f || echo "\n❌ Tests failed - fix bugs first"

# Show help
help:
    @echo "Sliding Window: Fixed Size - Pattern Commands"
    @echo ""
    @echo "Pattern: Fixed-size window slides across array/string"
    @echo "Use when: Process all k-sized subarrays, maintain incremental state"
    @echo ""
    @echo "Testing:"
    @echo "  just test              # Run all tests"
    @echo "  just test-one NAME     # Test specific kata class"
    @echo "  just test-kata1        # Test difficulty level 1"
    @echo "  just test-examples     # LeetCode examples only"
    @echo "  just test-edges        # Edge cases only"
    @echo "  just test-properties   # Property-based tests"
    @echo ""
    @echo "Workflow:"
    @echo "  just practice          # Open in Helix"
    @echo "  just reset             # Reset to 'pass'"
    @echo "  just cycle             # Test + auto-reset"
