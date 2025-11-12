#!/usr/bin/env bash
# Create a new system design from template

set -euo pipefail

if [ $# -eq 0 ]; then
    echo "Usage: $0 <design-name>"
    echo "Example: $0 url-shortener"
    exit 1
fi

DESIGN_NAME="$1"
# Convert kebab-case to snake_case for Python filename
PYTHON_NAME="${DESIGN_NAME//-/_}"

INCANTATIONS_DIR="packages/incantations/src/incantations/designs"
TEMPLATE_FILE="docs/templates/design.py"
TARGET_FILE="${INCANTATIONS_DIR}/${PYTHON_NAME}.py"

# Check if template exists
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "Error: Template not found at $TEMPLATE_FILE"
    exit 1
fi

# Create incantations directory if it doesn't exist
mkdir -p "$INCANTATIONS_DIR"

# Check if file already exists
if [ -f "$TARGET_FILE" ]; then
    echo "Error: File already exists at $TARGET_FILE"
    exit 1
fi

# Copy template and replace placeholder
cp "$TEMPLATE_FILE" "$TARGET_FILE"

# Replace the placeholder name in the file
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' "s/system_name/${PYTHON_NAME}/g" "$TARGET_FILE"
else
    # Linux
    sed -i "s/system_name/${PYTHON_NAME}/g" "$TARGET_FILE"
fi

echo "✅ Created system design: $TARGET_FILE"
echo ""
echo "Next steps:"
echo "  1. Work through RADIO framework"
echo "  2. Fill in requirements, architecture, data model, APIs"
echo "  3. Add deep dive sections"
echo "  4. Commit: incantations(designs): ${DESIGN_NAME}"
echo ""
echo "Opening in editor..."

# Try to open in editor (optional, will fail silently if no editor configured)
if [ -n "${EDITOR:-}" ]; then
    $EDITOR "$TARGET_FILE"
elif command -v code &> /dev/null; then
    code "$TARGET_FILE"
fi
