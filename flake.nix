{
  description = "Grimoire - Interview prep workspace with DSA and Systems Design";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};

        # Python environment with required packages
        pythonEnv = pkgs.python312.withPackages (ps: with ps; [
          pytest
          ipython
        ]);

      in
      {
        devShells.default = pkgs.mkShell {
          name = "grimoire-dev";

          packages = with pkgs; [
            # Core development tools
            pythonEnv
            uv
            just
            git

            # Editor and language servers
            helix
            basedpyright  # Community fork of pyright, actively maintained
            ruff  # Python linter/formatter with built-in LSP support

            # For Claude Code (installed via npm in shellHook)
            nodejs_22

            # Markdown support for docs
            marksman
            nodePackages.prettier

            # TOML support for pyproject.toml
            taplo

            # Useful utilities
            ripgrep
            fd
            tree
          ];

          shellHook = ''
            # Colors for output
            GREEN='\033[0;32m'
            BLUE='\033[0;34m'
            YELLOW='\033[1;33m'
            NC='\033[0m'

            echo -e "''${BLUE}╭───────────────────────────────────────╮''${NC}"
            echo -e "''${BLUE}│  🔮 Grimoire Development Environment  │''${NC}"
            echo -e "''${BLUE}╰───────────────────────────────────────╯''${NC}"
            echo ""

            # Set up git aliases for workflow
            if [ -f ./scripts/setup-git-workflow.sh ]; then
              echo -e "''${GREEN}→''${NC} Configuring git workflow aliases..."
              bash ./scripts/setup-git-workflow.sh 2>/dev/null || true
            fi

            # Install Claude Code if not already installed
            if ! command -v claude &> /dev/null; then
              echo -e "''${GREEN}→''${NC} Installing Claude Code CLI..."
              npm install -g @anthropic-ai/claude-code@latest
            fi

            # Use project-specific Helix config
            export HELIX_RUNTIME="''${PWD}/.helix"
            if [ -d ".helix" ]; then
              echo -e "''${GREEN}→''${NC} Helix configured for Python development"
            else
              echo -e "''${YELLOW}⚠''${NC}  No .helix/ directory found - using global config"
            fi

            # Set up Python path for grimoire packages
            export PYTHONPATH="''${PWD}/packages/cantrips/src:''${PWD}/packages/runes/src:''${PYTHONPATH}"

            # Create and activate uv virtual environment
            if [ ! -d ".venv" ]; then
              echo -e "''${GREEN}→''${NC} Creating uv virtual environment..."
              uv venv --quiet
            fi

            # Activate virtual environment
            if [ -f ".venv/bin/activate" ]; then
              source .venv/bin/activate

              # Sync dependencies
              echo -e "''${GREEN}→''${NC} Syncing dependencies with uv..."
              uv sync --quiet 2>/dev/null || true
            fi

            # Custom shell prompt indicator
            export PS1="(grimoire) ''${PS1}"

            # Display versions
            echo ""
            echo -e "''${GREEN}✓''${NC} Python $(python --version | cut -d' ' -f2)"
            echo -e "''${GREEN}✓''${NC} uv $(uv --version | awk '{print $2}')"
            echo -e "''${GREEN}✓''${NC} just $(just --version | cut -d' ' -f2)"
            echo -e "''${GREEN}✓''${NC} Claude Code $(claude --version 2>/dev/null | head -1 || echo '(installing...)')"
            echo -e "''${GREEN}✓''${NC} Helix $(hx --version | head -1 | awk '{print $2}')"
            echo -e "''${GREEN}✓''${NC} basedpyright $(basedpyright --version 2>/dev/null | head -1 | awk '{print $2}' || echo 'available')"
            echo -e "''${GREEN}✓''${NC} ruff $(ruff --version | awk '{print $2}')"
            echo ""

            echo "Quick start:"
            echo "  just                # List all commands"
            echo "  just start          # Start study session"
            echo "  hx .                # Open workspace in Helix"
            echo "  claude              # Run Claude Code"
            echo ""
            echo "Slash commands (in Claude Code):"
            echo "  /start-session      # Morning kickoff"
            echo "  /check-in           # Progress check"
            echo "  /commit-dsa         # Commit DSA work"
            echo ""
          '';

          # Allow network access for uv and npm
          NIX_ENFORCE_PURITY = false;
        };
      }
    );
}
