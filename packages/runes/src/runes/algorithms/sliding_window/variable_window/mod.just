# Sliding Window: Variable Size - Pattern-Specific Commands
#
# Pattern: Window size changes dynamically based on condition (expand/contract)
# When to use: Longest/shortest subarray meeting condition, "at most K", "at least X" constraints
# Example problems: LC 3 (Longest Substring), LC 209 (Min Subarray Sum), LC 904 (Fruit Baskets)
#
# Usage from root:
#   just variable-window::test-one TestKata1LongestSubstring
#   just variable-window::cycle
#
# Recognition triggers:
#   ✓ "Longest substring with..." or "minimum subarray with..."
#   ✓ Window size is NOT fixed (changes based on condition)
#   ✓ "At most K" or "at least X" constraints
#   ✓ Expand until constraint violated, then contract

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
    uv run runes kata reset sliding_window/variable_window

# Full cycle: test → auto-reset if all pass
cycle:
    @pytest test_kata.py -v && echo "\n✅ All tests passed! Resetting..." && uv run runes kata reset sliding_window/variable_window -f || echo "\n❌ Tests failed - fix bugs first"

# Show help
help:
    @echo "Sliding Window: Variable Size - Pattern Commands"
    @echo ""
    @echo "Pattern: Dynamic window size, expand/contract based on condition"
    @echo "Use when: Longest/shortest subarray, 'at most K' constraints"
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
