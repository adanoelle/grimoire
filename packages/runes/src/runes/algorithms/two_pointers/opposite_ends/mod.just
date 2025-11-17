# Two Pointers: Opposite Ends - Pattern-Specific Commands
#
# Pattern: Start at opposite ends (left/right), move toward center
# When to use: Sorted array + find pair/triplet, palindrome check, container problems
# Example problems: LC 167 (Two Sum II), LC 15 (3Sum), LC 11 (Container With Most Water)
#
# Usage from root:
#   just opposite-ends::test-one TestKata1TwoSum
#   just opposite-ends::cycle
#
# Recognition triggers:
#   ✓ Array is sorted (or can be sorted)
#   ✓ Need to find pair/triplet with condition
#   ✓ Checking symmetry (palindrome)
#   ✓ Comparing elements from both ends

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

test-kata3:
    pytest test_kata.py -m kata3 -v

test-kata4:
    pytest test_kata.py -m kata4 -v

test-kata5:
    pytest test_kata.py -m kata5 -v

# Test by category (reinforces interview thinking)
test-examples:
    pytest test_kata.py -k "leetcode_examples" -v

test-edges:
    pytest test_kata.py -k "edge_cases" -v

# Open for practice
practice:
    hx kata.py

# Reset using CLI (consistent with main workflow)
reset:
    uv run runes kata reset opposite_ends

# Full cycle: test → auto-reset if all pass
cycle:
    @pytest test_kata.py -v && echo "\n✅ All tests passed! Resetting..." && uv run runes kata reset opposite_ends -f || echo "\n❌ Tests failed - fix bugs first"

# Show help
help:
    @echo "Two Pointers: Opposite Ends - Pattern Commands"
    @echo ""
    @echo "Pattern: Left and right pointers converge toward center"
    @echo "Use when: Sorted array, find pairs, palindrome check"
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
