#!/usr/bin/env bash
# Interactive commit helper for grimoire work

set -euo pipefail

# Check if there are any changes
if git diff --quiet && git diff --cached --quiet; then
    echo "No changes to commit."
    exit 0
fi

# Get changed files
CHANGED_FILES=$(git diff --name-only --cached)
if [ -z "$CHANGED_FILES" ]; then
    CHANGED_FILES=$(git diff --name-only)
fi

# Detect work type
CANTRIP_FILES=$(echo "$CHANGED_FILES" | grep "packages/cantrips/" || true)
INCANTATION_FILES=$(echo "$CHANGED_FILES" | grep "packages/incantations/" || true)

if [ -n "$CANTRIP_FILES" ] && [ -n "$INCANTATION_FILES" ]; then
    echo "⚠️  Warning: Both cantrips and incantations changed."
    echo "Consider committing them separately for cleaner history."
    echo ""
    read -p "Continue with mixed commit? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
fi

# Generate commit message suggestion
if [ -n "$CANTRIP_FILES" ]; then
    echo "📚 Cantrip files changed:"
    echo "$CANTRIP_FILES" | sed 's/^/  - /'
    echo ""

    # Extract topic and problems
    TOPIC=$(echo "$CANTRIP_FILES" | head -1 | sed -n 's|packages/cantrips/src/cantrips/\([^/]*\)/.*|\1|p')
    PROBLEMS=$(echo "$CANTRIP_FILES" | sed -n 's|packages/cantrips/src/cantrips/[^/]*/\(.*\)\.py|\1|p' | tr '\n' ', ' | sed 's/, $//')

    SUGGESTED_MSG="cantrips(${TOPIC}): ${PROBLEMS}"

elif [ -n "$INCANTATION_FILES" ]; then
    echo "🔮 Incantation files changed:"
    echo "$INCANTATION_FILES" | sed 's/^/  - /'
    echo ""

    # Extract type and concept
    TYPE=$(echo "$INCANTATION_FILES" | head -1 | sed -n 's|packages/incantations/src/incantations/\([^/]*\)/.*|\1|p')
    CONCEPTS=$(echo "$INCANTATION_FILES" | sed -n 's|packages/incantations/src/incantations/[^/]*/\(.*\)\.py|\1|p' | tr '\n' ', ' | sed 's/, $//')

    SUGGESTED_MSG="incantations(${TYPE}): ${CONCEPTS}"
else
    # Other files
    echo "📝 Files changed:"
    echo "$CHANGED_FILES" | sed 's/^/  - /'
    echo ""
    SUGGESTED_MSG="docs: update documentation"
fi

# Show suggestion
echo "Suggested commit message:"
echo "  $SUGGESTED_MSG"
echo ""

# Prompt for message
read -p "Accept suggestion? (Y/n/edit) " -r
echo

if [[ $REPLY =~ ^[Ee]dit$ ]]; then
    # Open editor for custom message
    COMMIT_MSG_FILE=$(mktemp)
    echo "$SUGGESTED_MSG" > "$COMMIT_MSG_FILE"
    echo "" >> "$COMMIT_MSG_FILE"
    echo "# Enter commit message above" >> "$COMMIT_MSG_FILE"
    echo "# Lines starting with # will be ignored" >> "$COMMIT_MSG_FILE"

    ${EDITOR:-vim} "$COMMIT_MSG_FILE"

    # Read the edited message
    FINAL_MSG=$(grep -v '^#' "$COMMIT_MSG_FILE" | sed '/^$/d')
    rm "$COMMIT_MSG_FILE"
elif [[ $REPLY =~ ^[Nn]$ ]]; then
    # Enter message manually
    read -p "Enter commit message: " FINAL_MSG
else
    # Accept suggestion
    FINAL_MSG="$SUGGESTED_MSG"
fi

if [ -z "$FINAL_MSG" ]; then
    echo "Commit cancelled (empty message)"
    exit 0
fi

# Stage files if not already staged
if git diff --cached --quiet; then
    if [ -n "$CANTRIP_FILES" ]; then
        git add packages/cantrips/
    elif [ -n "$INCANTATION_FILES" ]; then
        git add packages/incantations/
    else
        git add .
    fi
fi

# Show what will be committed
echo ""
echo "Staging changes:"
git diff --cached --stat
echo ""

# Confirm
read -p "Commit these changes? (Y/n) " -r
echo

if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    git commit -m "$FINAL_MSG"
    echo "✅ Committed successfully!"
else
    echo "Commit cancelled"
    exit 0
fi
