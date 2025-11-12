#!/bin/bash
# Setup git workflow for grimoire study tracking

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔮 Setting up Grimoire Git Workflow"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Add git aliases
echo "📝 Configuring git aliases..."
git config --global alias.today "log --oneline --since='1 day ago'"
git config --global alias.week "log --oneline --since='1 week ago' --no-merges"
git config --global alias.study "log --oneline --grep='cantrips\\|incantations' --since='1 week ago'"
git config --global alias.dsa "log --oneline --grep='cantrips' --since='1 week ago'"
git config --global alias.sys "log --oneline --grep='incantations' --since='1 week ago'"
git config --global alias.last "log -1 --stat"

echo "✓ Git aliases configured"
echo ""

# Check if scripts directory exists
if [ ! -d "scripts" ]; then
    mkdir -p scripts
    echo "✓ Scripts directory created"
else
    echo "✓ Scripts directory exists"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Git workflow configured successfully!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Try these commands:"
echo "  git today    # See today's commits"
echo "  git week     # See this week's commits"
echo "  git study    # Study commits only"
echo "  git dsa      # DSA commits only"
echo "  git sys      # Systems commits only"
echo "  git last     # Last commit details"
echo ""
echo "Optional git hooks available in docs/GIT_WORKFLOW.md"
echo "To add hooks, copy examples to .git/hooks/ and chmod +x"
echo ""
