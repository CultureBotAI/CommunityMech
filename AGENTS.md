# CommunityMech Agent Entry Point

Read [CLAUDE.md](CLAUDE.md) for the authoritative working agreements, validation gates, and curation rules for this repository.

- Project skills live in `.claude/skills/` and are exposed at `.agents/skills/` so both Claude Code and `.agents/skills`-aware agents (Antigravity, Codex) discover the same canonical skill definitions (including `review-open-issues`).
- Before running record or category reviews, read [docs/record-reviews.md](docs/record-reviews.md).
