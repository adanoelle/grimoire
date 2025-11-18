# Kata Practice System - Central Module
#
# Pattern names reinforce LeetCode vocabulary through daily typing:
# - just kata::practice two_pointers/opposite_ends
# - just kata::test sliding_window/variable_window
# - just kata::reset searching/binary_search
#
# Every command types the full pattern = spaced repetition of interview strategies.

# Get algorithms directory (relative to root grimoire directory)
algo_dir := justfile_directory() + "/packages/runes/src/runes/algorithms"

# Launch interactive kata practice menu (no need to memorize commands!)
menu:
    @uv run runes kata menu

# List all patterns with mastery status
list:
    @uv run runes kata list

# Show detailed progress for a pattern
progress pattern:
    @uv run runes kata progress {{pattern}}

# Practice a kata (opens Helix once, code all katas in one session)
practice pattern:
    @echo "🥋 Practicing {{pattern}}"
    @cd {{algo_dir}} && hx {{pattern}}/kata.py

# Run tests for a pattern
test pattern kata="":
    #!/usr/bin/env bash
    set -e
    test_file="{{algo_dir}}/{{pattern}}/test_kata.py"
    if [ ! -f "$test_file" ]; then
        echo "Error: Test file not found: $test_file"
        exit 1
    fi
    if [ -z "{{kata}}" ]; then
        uv run pytest "$test_file" -v
    else
        uv run pytest "$test_file" -m kata{{kata}} -v
    fi

# Run all kata tests
test-all:
    @cd {{algo_dir}} && uv run pytest **/test_kata.py -v

# Reset pattern to 'pass' (preserves docstrings and mastery log)
reset pattern:
    @uv run runes kata reset {{pattern}}

# Reset all patterns
reset-all:
    @uv run runes kata reset-all

# Undo last reset (restore from backup)
undo pattern:
    @uv run runes kata undo {{pattern}}

# Quick log a practice session
# Usage: just kata::log two_pointers/opposite_ends 1 2:30 [bugs] [notes]
# Examples:
#   just kata::log two_pointers/opposite_ends 1 2:30
#   just kata::log two_pointers/opposite_ends 1 2:30 1
#   just kata::log two_pointers/opposite_ends 1 2:30 1 "Fixed off-by-one"
log pattern kata time bugs="0" notes="":
    #!/usr/bin/env bash
    if [ -z "{{notes}}" ]; then
        uv run runes kata log {{pattern}} {{kata}} {{time}} -b {{bugs}}
    else
        uv run runes kata log {{pattern}} {{kata}} {{time}} -b {{bugs}} -n "{{notes}}"
    fi

# ==============================================================================
# PATTERN-SPECIFIC MODULES (Optional - for advanced/granular commands)
# ==============================================================================
# Use pattern::command syntax for granular control:
#   just opposite-ends::test-one TestKata1TwoSum
#   just opposite-ends::cycle

mod? opposite-ends 'two_pointers/opposite_ends'
mod? fast-slow 'two_pointers/fast_slow'
mod? same-direction 'two_pointers/same_direction'
mod? fixed-window 'sliding_window/fixed_window'
mod? variable-window 'sliding_window/variable_window'
mod? binary-search 'searching/binary_search'
