# Nix Flake Setup for Grimoire

This document explains the Nix flake configuration for the grimoire workspace, providing
a reproducible development environment across macOS and NixOS.

## Overview

The flake provides:

- Python 3.12 with uv for fast package management
- Helix editor with LSP configuration for Python
- Claude Code CLI automatically installed
- All grimoire scripts and workflows
- Consistent environment on MacBook (Nix) and desktop (NixOS)

## Quick Start

### First Time Setup

```bash
# Enter the development environment
nix develop

# That's it! Everything is configured automatically:
# - Git aliases set up
# - Claude Code installed
# - Virtual environment created and activated
# - Helix configured for Python with LSP
```

### With direnv (Recommended)

For automatic environment loading:

```bash
# 1. Install direnv
brew install direnv  # macOS
# or on NixOS, add to configuration.nix

# 2. Add to ~/.zshrc or ~/.bashrc
eval "$(direnv hook zsh)"  # for zsh
eval "$(direnv hook bash)" # for bash

# 3. Allow the .envrc in grimoire
cd ~/grimoire
direnv allow

# 4. Now it activates automatically!
cd ~/grimoire  # Environment loads
cd ~          # Environment unloads
cd ~/grimoire  # Loads again
```

## What's Included

### Core Tools

| Tool       | Version | Purpose                     |
| ---------- | ------- | --------------------------- |
| **Python** | 3.12    | Programming language        |
| **uv**     | Latest  | Fast Python package manager |
| **just**   | Latest  | Task runner for workflows   |
| **git**    | Latest  | Version control             |

### Editor & LSP

| Tool             | Purpose                       |
| ---------------- | ----------------------------- |
| **Helix**        | Your editor                   |
| **basedpyright** | Python type checking LSP      |
| **ruff**         | Python linting and formatting |

### Documentation Tools

| Tool         | Purpose                |
| ------------ | ---------------------- |
| **marksman** | Markdown LSP           |
| **prettier** | Markdown formatter     |
| **taplo**    | TOML LSP and formatter |

### Claude Code

Automatically installed via npm on first `nix develop`.

```bash
# Check version
claude --version

# Run Claude Code
claude

# Use slash commands (see .claude/commands/)
/start-session
/check-in
/commit-dsa
```

## Project-Specific Helix Configuration

The `.helix/` directory contains Python-optimized settings:

### `.helix/config.toml`

- Auto-save enabled
- Line numbers (relative)
- File picker shows hidden files
- Ignores build artifacts

### `.helix/languages.toml`

- **basedpyright**: Type checking with grimoire package paths
- **ruff**: Linting and formatting (auto-format on save)
- Configured for Python, Markdown, TOML, JSON, and Bash

### Using the LSP

```bash
# Open grimoire in Helix
hx .

# Open a Python file
hx packages/cantrips/src/cantrips/arrays_strings/reverse_string.py

# LSP features automatically work:
# - Type checking (basedpyright)
# - Linting (ruff)
# - Auto-formatting on save (ruff)
# - Go to definition (gd)
# - Show documentation (K)
# - Code actions (Space + a)
```

## Daily Workflow

### Morning

```bash
cd ~/grimoire  # direnv loads automatically, or run: nix develop
just start     # Begin study session
```

### During Study

```bash
# Create new DSA problem
just cantrip-array two_sum

# Edit with Helix (LSP active)
hx packages/cantrips/src/cantrips/arrays_strings/two_sum.py

# Test your solution
just test-array two_sum

# Check progress
just check-in
```

### Evening

```bash
# Review day
just review

# Commit work
just commit-dsa  # Or use interactive: just commit
```

## Shell Hook Features

When you enter `nix develop`, the shell automatically:

1. ✅ Configures git aliases (`git today`, `git week`, etc.)
2. ✅ Installs Claude Code if not present
3. ✅ Sets `HELIX_RUNTIME` to use `.helix/` config
4. ✅ Adds grimoire packages to `PYTHONPATH`
5. ✅ Creates/activates uv virtual environment
6. ✅ Syncs Python dependencies from `pyproject.toml`
7. ✅ Sets custom prompt `(grimoire) $`
8. ✅ Displays versions of all tools

## Updating the Flake

### Update All Inputs

```bash
# Update nixpkgs to latest
nix flake update

# This updates flake.lock with new package versions
```

### Update Specific Package

```bash
# Update just nixpkgs
nix flake lock --update-input nixpkgs
```

### After Updating

```bash
# Re-enter shell to use new versions
exit
nix develop
```

## Troubleshooting

### Claude Code Not Installing

```bash
# Manually install
npm install -g @anthropic-ai/claude-code

# Check it's available
which claude
claude --version
```

### LSP Not Working in Helix

```bash
# Check language servers are available
which basedpyright-langserver  # Should show path
which ruff                      # Should show path

# Check Helix is using project config
echo $HELIX_RUNTIME  # Should show: /path/to/grimoire/.helix

# Debug LSP in Helix
# Open a Python file, then: Space + ? (to see LSP status)
```

### Virtual Environment Issues

```bash
# Manually recreate
rm -rf .venv
uv venv
source .venv/bin/activate
uv sync
```

### direnv Not Loading

```bash
# Check direnv is installed
which direnv

# Check hook is in shell config
grep "direnv hook" ~/.zshrc  # or ~/.bashrc

# Re-allow the .envrc
direnv allow
```

## Cross-Platform Notes

### macOS (Nix)

- Uses Apple Silicon (aarch64-darwin) or Intel (x86_64-darwin)
- Some packages may be built from source
- Claude Code installs via npm

### NixOS (Desktop)

- Native Nix integration
- Faster package installation (binary cache)
- Can add flake to system configuration

### Sharing Between Machines

The `flake.lock` ensures identical package versions:

```bash
# On MacBook - commit the lock file
git add flake.lock
git commit -m "nix: update flake.lock"
git push

# On Desktop - pull and use
git pull
nix develop  # Uses exact same package versions!
```

## Advanced Usage

### Running Without Shell

```bash
# Run a command in the Nix environment without entering shell
nix develop -c just test-all

# Run Python from the Nix environment
nix develop -c python -c "print('Hello from Nix Python')"
```

### Building Derivations

```bash
# Show what will be built
nix flake show

# Build all outputs
nix build

# Build and show result
nix build && ls -la result/
```

### Using in GitHub Actions

```yaml
steps:
  - uses: cachix/install-nix-action@v24
  - run: nix develop --command just test-all
```

## File Reference

| File                    | Purpose                                     |
| ----------------------- | ------------------------------------------- |
| `flake.nix`             | Main flake definition with dev shell        |
| `flake.lock`            | Locked dependency versions (auto-generated) |
| `.helix/config.toml`    | Helix editor settings                       |
| `.helix/languages.toml` | LSP configuration for languages             |
| `.envrc`                | direnv integration                          |
| `.gitignore`            | Ignores Nix build artifacts                 |

## Why Nix for Grimoire?

### Reproducibility

Same environment on MacBook and desktop. No "works on my machine" problems.

### Isolation

Won't conflict with other Python projects or system packages.

### Documentation

`flake.nix` documents all dependencies. New contributor can `nix develop` and start
immediately.

### Version Locking

`flake.lock` pins exact versions. Can recreate environment months later.

### Composability

Can layer multiple flakes. Add Rust support later without conflicts.

## Next Steps

1. **Daily Use**: Just run `nix develop` (or use direnv)
2. **Customize**: Edit `.helix/config.toml` for personal preferences
3. **Extend**: Add more tools to `flake.nix` as needed
4. **Share**: Commit `flake.lock` so both machines stay in sync

## Resources

- [Nix Flakes Guide](https://nixos.wiki/wiki/Flakes)
- [Helix Editor Docs](https://docs.helix-editor.com/)
- [direnv Documentation](https://direnv.net/)
- [uv Documentation](https://docs.astral.sh/uv/)

---

**🔮 The grimoire environment is now reproducible across all your machines!**
