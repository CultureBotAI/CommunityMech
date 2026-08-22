---
name: review-open-issues
description: Sweep and triage the full open-issue queue for CommunityMech — not just NEXT_TASKS.md. Fetches every open issue, checks each against the current code/schema for staleness (already fixed, superseded, or no longer reproducible), flags likely duplicates, and assigns a priority tier (P0 blocking/correctness/security, P1 real-but-schedulable, P2 low-severity/process/doc). Produces a short, ranked report; only touches GitHub (closing stale issues, updating/creating a tracker issue) when asked. Use when the user asks to "review issues", "prioritize the backlog", "triage open issues", or the open-issue count has grown large enough that NEXT_TASKS.md-only review is insufficient.
category: workflow
requires_database: false
requires_internet: true
version: 1.0.0
---

# Review & Prioritize Open Issues

## Overview

**Purpose**: the raw GitHub issue queue and `NEXT_TASKS.md` are different
surfaces. `next-tasks` reconciles a small, curated, actively-maintained backlog
file. This skill sweeps the *entire* open-issue queue — which grows much
larger and drifts independently (issues opened by review passes, other agents,
or humans, many of which are never transcribed into `NEXT_TASKS.md`) — and
produces an honest, current priority ranking.

**Why this is a distinct skill, not a `next-tasks` step**: `next-tasks`
Step 1 already runs `gh issue list --limit 30` as *context* for reconciling the
backlog file: it stops at the first page and never assesses issue validity
individually. This skill is the deep pass: paginate the whole queue, check each
issue against current code, and produce a full triage — expensive enough that
it should not run on every "what's next" invocation, only when explicitly
asked or when the backlog has clearly gone stale.

**When to use**: the user asks to "review issues", "prioritize open issues",
"triage the backlog", "what issues are actually urgent", or after a large
review pass (like a fleet PR review) has filed a batch of new issues that need
sorting. CommunityMech already has an active tracker issue (#669) — this
skill is how you refresh it, not a replacement for it.

**When NOT to use**: for `NEXT_TASKS.md` upkeep or picking the next unit of
work to implement — that's `next-tasks`. This skill produces a priority
ranking; it does not implement fixes.

## Workflow

### Step 1 — Fetch the full open-issue queue

```bash
queue_file="${TMPDIR:-/tmp}/communitymech-open-issues.json"
gh issue list --state open --limit 5000 \
  --json number,title,body,labels,comments,createdAt,updatedAt > "$queue_file"
jq -r '.[] | [.number, .createdAt[:10], .title] | @tsv' "$queue_file"
jq length "$queue_file"
```

The first command preserves every requested field; the second derives a
scannable overview without throwing away the bodies and labels needed below.
Read and group from the saved JSON, not from the overview alone. Omitting
`--limit` silently caps at gh's default of 30. If the saved array has exactly
5000 entries, treat that as possible truncation and re-run with a higher limit
before claiming full-queue coverage.

### Step 2 — Group and dedupe

Issues filed from the same review pass (same PR, same session) often overlap —
several may describe the same root cause from different angles. Group by:
- shared PR/commit reference in the title or body,
- same file/function named,
- near-identical failure scenario.

Inspect each saved issue object's title, body, labels, and comments while
grouping. A group is an organizational aid, not permission to skip its
individual issues.
Note groups explicitly in the report; do not silently merge them (a human may
want to close duplicates deliberately, not have them hidden).

### Step 3 — Check each issue against current reality

For every issue, check:

- **Already fixed on the default branch?** Refresh the base ref with `git fetch
  origin main`, then use `git log --oneline origin/main --perl-regexp --grep
  "#<N>\b"`. Plain `--grep "#<N>"` substring-matches unrelated numbers (`#48`
  also matches `#480`, `#4823`, ...), so the `\b` boundary is required. Do not
  use `--all`: commits found only on an unmerged branch are work in progress,
  not evidence that the issue is fixed.
- **Closed by a merged PR?** Get exact linked candidates with `gh issue view
  <N> --json closedByPullRequestsReferences --jq
  '.closedByPullRequestsReferences[] | [.number, .url] | @tsv'`, then verify
  each candidate's `mergedAt` using `gh pr view <PR> --json mergedAt`. Do not
  use a bare-number `gh pr list --search`: it substring-matches unrelated PR
  text. An issue whose fix actually reached `main` should be flagged
  STALE/CLOSE, not re-surfaced as open work.
- **Still reproducible?** If the issue names a specific file/line/function,
  confirm it still exists in that shape (`grep`/`git log -p` the cited
  location) — code moves, and a stale issue pointing at a renamed/removed
  function is noise, not a live defect.
- **Superseded?** Does a newer issue or a merged PR's description explicitly
  supersede this one?

### Step 4 — Assign priority

- **P0 — blocking/correctness/security.** Data corruption, a crash/hang in a
  path every caller hits, a security-relevant defect (injection, secret
  exposure, auth bypass), or something that silently produces wrong output
  with no detection. Fix before anything else ships.
- **P1 — real, schedulable.** A genuine defect or gap that doesn't block
  everything but should be fixed soon — most test-coverage gaps for
  safety-critical code, real (if narrow) bugs, process gaps that have already
  caused a near-miss.
- **P2 — low-severity/process/doc.** Documentation drift, stale comments,
  minor test-coverage gaps in non-critical paths, style/convention issues.

Do not default everything to P1 — that makes the tier meaningless. Use P0
sparingly and justify it; most issues are P1 or P2.

### Step 5 — Present the report

- Ranked list, P0 first, one line per issue/group with number + one-sentence
  why.
- Explicitly call out: issues recommended for closing (fixed/stale/duplicate),
  with the evidence (commit/PR that fixed it, or why it no longer applies).
- **Recommend a top 2–3** to act on next, with reasoning.
- Do not silently drop old issues from the report — if something is 6 months
  old and still open, say so; that itself is a signal.

### Step 6 — Act only when asked

This skill does not close issues, comment, or create/update a tracker issue on
its own, and a general "yes, go ahead" is not blanket approval to loop over
every STALE/CLOSE candidate unattended:
- **Closing stale/duplicate issues**: confirm with the user which specific
  issue number(s) to close before each closure — do not treat one general
  approval as authorization for an unattended `gh issue close` loop. Once
  confirmed, use `gh issue close <N> --comment "<reason>"`, one at a time,
  with the evidence from Step 3 in the comment.
- **Maintaining the tracker issue**: as of this skill's authoring, this repo
  had one open — **#669**, "[P0-P2 tracker] Repository safety, test,
  documentation, CI, and packaging remediation". Verify it's still open
  before trusting this note (`gh issue view 669 --json state`); update it in
  place rather than creating a second one. Only create a new tracker if #669
  is confirmed closed/superseded and the user wants a fresh one.

Never bulk-close without per-item confirmation of the evidence — an agent
closing a live issue because it *looks* stale is worse than leaving noise in
the queue.

## Conventions this skill enforces

- **Full-queue coverage, not first-page sampling.** State exactly how many
  issues were reviewed and whether coverage was complete.
- **Evidence over vibes.** Every STALE/CLOSE/duplicate recommendation cites a
  specific commit, PR, or code location — never "this looks done."
- **P0 is rare.** If more than ~10% of issues land P0, the tier calibration is
  probably wrong; recheck.
- **Read-only by default.** Reporting and ranking happen automatically;
  closing issues or touching a tracker issue requires explicit confirmation.

## Notes & limitations

- `comments` must remain in Step 1's explicit `--json` field list; otherwise a
  "fixed already" claim buried in a later comment thread will not be present
  in the saved queue.
- Cross-repo issues (a defect described once but relevant to multiple Mechs)
  are common in this org — note if an issue's fix should propagate elsewhere,
  but do not open issues in sibling repos without being asked.
- No @-mentions in issue comments or tracker updates without explicit
  per-mention authorization (standing rule).
- The existing tracker (#669) predates this skill; reconcile it against
  reality the same as any other issue before trusting its current contents.

## Related

- `next-tasks` — the lighter, `NEXT_TASKS.md`-scoped backlog check; run that
  for "what's next" during active work. Run this skill for a full-queue sweep.

## Related files

- `NEXT_TASKS.md` — items promoted from this skill's ranking often get logged
  here too, so `next-tasks` picks them up on the next reconcile.
