---
name: next-tasks
description: Assess and maintain the CommunityMech backlog. Reconciles NEXT_TASKS.md against what actually shipped (merged PRs, git log, open issues/PRs), separates genuinely-pending actionable work from done/stale/upstream-blocked items, surfaces a short prioritized menu with a recommendation, and — when asked — picks one up. Also the maintenance path for NEXT_TASKS.md itself — marking done items, adding new deferrals, bumping the reconcile date, and keeping cross-Mech items in sync. Use whenever the user asks "next tasks", "what's next", "is the backlog current", or after finishing a work thread.
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
---

# Next Tasks (backlog assessment + maintenance)

## Overview

**Purpose**: answer "what should I work on next?" *accurately*, and keep
`NEXT_TASKS.md` honest. The backlog file drifts — items marked "pending" get
shipped in PRs, new threads (whole capabilities) never get logged, and some
items are upstream-blocked and will never be actionable here. This skill
reconciles the written backlog against reality, then produces a short,
prioritized, *actionable* menu.

`NEXT_TASKS.md` is the source of truth for deferred work, but it is only as good
as its last reconciliation. **Always reconcile before recommending** — never
read the file and relay it verbatim.

**When to use**: the user says "next tasks" / "what's next" / "anything left?",
asks whether the backlog is current, or you've just closed a work thread and
want to record state + pick the next thing.

**When NOT to use**: to discover brand-new curation candidates from the
literature — that's `scout-communities`. This skill works the *existing*
backlog, not the outside world.

## What it does

1. **Read** `NEXT_TASKS.md` (the whole file — sections are numbered and each
   carries enough context to pick up cold).
2. **Reconcile** every "pending"/"in progress" claim against reality:
   - **merged PRs** since the file's `Last reconciled:` date (`gh pr list
     --state merged`), and the **git log** — an item whose deliverable is in a
     merged PR is DONE, even if the file still says pending.
   - **open PRs / issues** (`gh pr list`, `gh issue list`) — an item may already
     be in flight, or tracked as a GitHub issue.
   - **the code/schema** — verify a slot/recipe/test the file references still
     exists (memories and stale notes cite things that were later renamed).
3. **Classify** each item into: **DONE** (ship it out of the file), **PENDING &
   actionable** (real work you could start now), **IN PROGRESS** (has an open
   PR/branch), or **UPSTREAM-BLOCKED / not-actionable** (e.g. needs a minted
   ChEBI/ENVO/NCBITaxon term you can't create — keep, but never recommend as
   "next").
4. **Surface** a short prioritized menu (3–6 items) of PENDING & actionable
   work, each one line, with a clear recommendation for the top pick and why.
   Prefer the item that continues the current thread or unblocks the most.
5. **Maintain** `NEXT_TASKS.md`: mark done items done (with the PR number +
   date), add any newly-discovered threads as sections, bump `Last reconciled:`
   to today, and — for cross-Mech items — note if the sibling repos need the
   same edit.

## Workflow

### Step 1 — Reconcile

```bash
# Read the backlog, then check it against what shipped.
sed -n '1,400p' NEXT_TASKS.md
git log --oneline -20
gh pr list --state merged --limit 20 --json number,title,mergedAt \
  -q '.[] | "\(.number)\t\(.mergedAt[:10])\t\(.title)"'
gh pr list  --state open   --limit 20 2>/dev/null | head
gh issue list --state open  --limit 30 2>/dev/null | head -30
```

For each pending item, ask: *is its deliverable already in a merged PR or in the
code?* If yes → DONE. Spot-check any file/slot/recipe the item names before
treating the note as current (`grep -rl <slot> src/communitymech/schema/`).

### Step 2 — Present the menu

Give the user a tight, honest picture:
- one line per PENDING & actionable item, grouped/ranked by value;
- call out what's newly DONE (so they see progress) and what's
  UPSTREAM-BLOCKED (so they know why it's not on the menu);
- **recommend one** — usually the item that continues the active thread, is
  fully specified, or unblocks the most downstream work.

Use `AskUserQuestion` only when the directions genuinely diverge and picking
wrong wastes real effort; otherwise recommend and proceed on confirmation.

### Step 3 — Maintain NEXT_TASKS.md (do this every time, even if only bookkeeping)

- Mark shipped items **DONE (YYYY-MM-DD, PR #NNN)** in place, or move them out.
- Add any work thread that isn't logged yet as its own `##` section with enough
  context to pick up cold (what/why/next, PRs, key ids).
- Convert relative dates to **absolute** ones.
- Bump `Last reconciled:` to today's date.
- If a changed item is one of the **cross-Mech** items (kept in sync with
  CultureMech / MIM / TraitMech `NEXT_TASKS.md`), say so — the sibling repos may
  need the same edit (do not edit sibling repos unless asked).
- Link related memories with `[[name]]` where useful.

Commit the `NEXT_TASKS.md` reconciliation (doc-only → CI passes trivially; the
path-filtered lint/validate gates may report no checks, which is expected and
mergeable).

### Step 4 — Pick it up (only if the user says to)

Hand off to the right skill for the chosen item and drive it to a merged PR the
usual way (branch → curate/implement → `just qc` / targeted validation → PR →
watch CI → squash-merge `--delete-branch` → sync main). Then re-run Step 3 to
record the new state.

## Conventions this skill enforces

- **Reconcile-before-relay**: the file is a starting point, not ground truth.
- **Honest classification**: don't recommend upstream-blocked items; don't hide
  them either — they explain gaps.
- **Every invocation updates the file** (at minimum the reconcile date), so the
  backlog never silently rots.
- **Absolute dates**, PR numbers on done items, cold-start context on new items.

## Notes & limitations

- `validate-references` is **not** a CI gate; don't treat a green PR as proof
  its snippets validate. `label-correspondence`, `lint`, `validate-strict`, and
  `validator-pin` are the gates.
- Doc-only PRs may show "no checks reported" on path-filtered workflows — that's
  `MERGEABLE`/`CLEAN`, not a failure.
- Cross-Mech sync is **advisory here** — this skill flags divergence but only
  edits this repo's `NEXT_TASKS.md`.

## Related

- `scout-communities` — find *new* work from the literature (this skill only
  works the existing backlog).
- `deep-research-community`, `add-growth-conditions`, `review-communities`,
  `evidence-curation`, `manage-identifiers` — the skills a chosen backlog item
  is usually handed off to.

## Related files

- `NEXT_TASKS.md` — the backlog this skill reads and maintains.
