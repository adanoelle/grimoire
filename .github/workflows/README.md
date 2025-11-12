# GitHub Actions Workflows

This directory contains automated workflows for the grimoire workspace.

## Active Workflows

### 1. CI - Test & Lint (`ci.yml`)

**Triggers:** On every push to `main` and all pull requests

**What it does:**
- ✅ Runs ruff linting
- ✅ Runs ruff formatting check
- ✅ Runs basedpyright type checking
- ✅ Runs pytest on all cantrip tests

**Why:** Ensures code quality and that all your solutions actually work before merging.

**Nix-based:** Uses your `flake.nix` for reproducible testing environment.

---

### 2. Weekly Progress Report (`weekly-progress.yml`)

**Triggers:**
- Automatically every Sunday at 8:00 PM UTC
- Manually via GitHub Actions UI or CLI

**What it does:**
1. Runs `./scripts/weekly-report.sh`
2. Saves report to `progress/weekly/YYYY-WWW.md`
3. Creates a GitHub issue with the report (labeled `progress-tracker`)
4. Commits the report file back to the repo

**Why:**
- Automatic accountability
- Historical record of progress
- Motivational weekly check-ins
- Shows interview preparation discipline

**Manual trigger:**
```bash
gh workflow run weekly-progress.yml
```

Or via GitHub UI: Actions → Weekly Progress Report → Run workflow

---

## Workflow Features

### Test Summary in PRs
The CI workflow adds a summary to each PR showing:
- Linting status
- Formatting status
- Type checking status
- Test results

### Progress Tracking
Weekly reports create searchable GitHub issues and markdown files in `progress/weekly/`.

### Nix Integration
Both workflows use the Nix flake for reproducible environments, ensuring tests run in the same environment as local development.

---

## Permissions

These workflows require:
- `contents: write` - To commit weekly reports
- `issues: write` - To create progress report issues

Configured in workflow files via `permissions:` block.

---

## Future Workflow Ideas

Potential additions (not implemented yet):
- **Nix Flake Check**: Validate flake builds on multiple platforms
- **Streak Tracker**: Count consecutive days with commits, celebrate milestones
- **Pattern Recognition**: Analyze commit messages for problem patterns
- **Mock Interview Bot**: Auto-create weekly mock interview challenges

Want to add these? Check `docs/` for GitHub Actions planning notes.

---

🔮 **Automated workflows help you focus on learning, not tracking.**
