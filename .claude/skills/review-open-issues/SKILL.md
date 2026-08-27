---
name: review-open-issues
description: Sweep and triage the full open-issue queue for CommunityMech — not just NEXT_TASKS.md. Fetches every open issue with its comments, orders them by where they sit in the schema→records→gates→products pipeline, tests each claim against the current schema, records, validators, and committed artifacts, flags stale/superseded/duplicate items with citable evidence, and assigns a priority tier (P0 stop-the-line, P1 real-but-schedulable, P2 low-severity) plus a separate cost annotation for sequencing. Read-only by default. Use when the user asks to "review issues", "prioritize the backlog", "triage open issues", "what's actually urgent", or after a review pass has filed a batch of issues that need sorting.
category: workflow
requires_database: false
requires_internet: true
version: 2.0.0
---

# Review & Prioritize Open Issues

## Overview

**Purpose**: the raw GitHub issue queue and `NEXT_TASKS.md` are different
surfaces. `next-tasks` reconciles a small, curated, actively-maintained backlog
file. This skill sweeps the *entire* open-issue queue — which grows much larger
and drifts independently (issues opened by review passes, other agents, or
humans, many never transcribed into `NEXT_TASKS.md`) — tests every claim in it
against the current repository, and produces an honest, dependency-ordered
ranking.

**Why this is a distinct skill, not a `next-tasks` step**: `next-tasks` Step 1
runs `gh issue list --limit 30` as *context* for reconciling the backlog file;
it stops at the first page and never assesses issue validity individually. This
skill is the deep pass: paginate the whole queue, check each issue against
current code and data, and produce a full triage — expensive enough that it
should not run on every "what's next" invocation.

**When to use**: the user asks to "review issues", "prioritize open issues",
"triage the backlog", "what issues are actually urgent", or after a large
review pass has filed a batch of new issues. CommunityMech maintains a tracker
issue (#669 as of this writing — verify before trusting it); this skill is how
you refresh it, not a replacement for it.

**When NOT to use**: for `NEXT_TASKS.md` upkeep, or for picking up and
implementing a single known issue. This skill produces a ranking, not a fix.

This is a **read-only review by default**. It does not implement fixes, close
or edit issues, change labels, apply generated curation, or make billed network
calls unless the user separately authorizes that exact mutation.

## Sources of truth

Check these before relying on an issue title or an older planning document:

- `CLAUDE.md` — the canonical/generated file table, the evidence policy, and
  which commands are gates versus advisory;
- `src/communitymech/schema/communitymech.yaml` — what a slot actually is;
  `src/communitymech/datamodel/communitymech.py` is *generated* and proves
  nothing on its own;
- `.github/workflows/*.yaml` — what CI genuinely runs, and, critically, each
  workflow's `paths:` filter, which decides whether it runs at all;
- `justfile` — what a named recipe actually does today;
- `conf/id_label_targets.yaml` (id↔label targets and curator-accepted
  exceptions), `conf/qc_config.yaml` (thresholds), `conf/reference_validator.yaml`;
- `history/` and `history/README.md` — append-only curation provenance;
- `NEXT_TASKS.md` — deferred work, but only as current as its last reconcile;
- the records themselves (`kb/communities/`, `data/isolates/`, `kb/taxa/`),
  `references_cache/`, the committed `docs/` site, and the KGX export — which
  is **not** committed (`output/kgx/` is gitignored), so it exists only where
  someone has run `just kgx-export`.

Treat issue bodies and titles as **claims, not current status**. Read the
comments: corrections, withdrawals, and narrowed residual scope are recorded
there. A merged PR is evidence only after its code and the issue's acceptance
criteria have both been checked.

## Workflow

### Step 1 — Fetch the full open-issue queue

```bash
queue_file="${TMPDIR:-/tmp}/communitymech-open-issues.json"
gh issue list --state open --limit 5000 \
  --json number,title,body,labels,comments,createdAt,updatedAt,author > "$queue_file"
jq -r '.[] | [.number, .createdAt[:10], .title] | @tsv' "$queue_file"
jq length "$queue_file"
gh label list --limit 200
```

The first command preserves every requested field; the second derives a
scannable overview without throwing away the bodies and comments needed below.
Read and group from the saved JSON, not from the overview alone. Omitting
`--limit` silently caps at gh's default of 30. If the saved array has exactly
5000 entries, treat that as possible truncation and re-run higher before
claiming full-queue coverage.

State the exact number reviewed and whether coverage was complete.

### Step 2 — Place each issue in the pipeline before ranking it

CommunityMech is a chain, and a defect upstream invalidates everything
downstream of it:

```text
schema (communitymech.yaml)
  -> generated datamodel (just gen-python)
  -> curated records (kb/communities, data/isolates, kb/taxa)
  -> evidence (references_cache, snippets, history/)
  -> validators and CI gates (lint, validate-strict, label-correspondence,
     docs-current, curation-history, network-quality, vendored-sync)
  -> generated products (docs/ site, output/kgx, browser, UMAP)
  -> published Pages / KGX release / an external claim about the corpus
```

An upstream correctness or identity problem blocks the downstream consumers.
Recommend fixing or auditing the root before polishing what it feeds. Group
issues that share a root cause, but never hide the individual issue numbers.

For each issue record, where applicable:

- the pipeline stage it belongs to, and the owning repository (cross-Mech
  issues are common in this org);
- which records, CURIEs, references, or generated artifacts are affected;
- whether a *gate* is implicated, and if so whether that gate's `paths:` filter
  even causes it to run on the change class in question;
- prerequisites, blockers, duplicates, and superseding issues;
- the cheapest decisive evidence and the acceptance test;
- execution class: read-only inspection, local validator run, corpus-wide
  sweep, regeneration of committed products, or a networked/billed call.

### Step 3 — Group and dedupe

Issues filed from the same review pass often overlap — several may describe one
root cause from different angles. Group by shared PR/commit reference, the same
file or function named, or a near-identical failure scenario.

A group is an organizational aid, not permission to skip its members. Note
groups explicitly in the report; do not silently merge them — a human may want
to close duplicates deliberately rather than have them disappear.

### Step 4 — Check each issue against current reality

- **Already fixed on the default branch?** Refresh the base ref with
  `git fetch origin main`, then:

  ```bash
  git log --oneline origin/main --perl-regexp --grep "#<N>\b"
  ```

  The `\b` boundary is required: plain `--grep "#48"` substring-matches `#480`
  and `#4823`. Do **not** use `--all` — a commit found only on an unmerged
  branch is work in progress, not evidence that the issue is fixed.

- **Closed by a merged PR?** Get exact linked candidates, then verify each one
  actually merged:

  ```bash
  gh issue view <N> --json closedByPullRequestsReferences \
    --jq '.closedByPullRequestsReferences[] | [.number, .url] | @tsv'
  gh pr view <PR> --json mergedAt,state
  ```

  Do not use a bare-number `gh pr list --search <N>`: it matches the number
  anywhere in indexed text and returns unrelated PRs. Every hit is a lead to
  open, never a citation on its own.

- **Still reproducible?** If the issue names a file, line, function, slot, or
  recipe, confirm it still exists in that shape (`rg`, `git log -p`, `just
  --show <recipe>`). Code moves; an issue pointing at a renamed function is
  noise, not a live defect. Inspect the tests as well as the implementation —
  a fix without a test that can fail is the recurring defect class here.

- **Fully fixed, or partly?** Compare the issue's acceptance criteria against
  what merged. If only part landed, keep the issue open with a **narrowed
  residual** and say which part is done; do not recommend closure merely
  because a related PR merged.

- **Observation or action?** Prefer closing a fully-recorded observation as
  superseded when a separate open issue owns the only remaining work.

- **Superseded?** Does a newer issue, or a merged PR description, explicitly
  supersede this one?

### Step 5 — Apply the stop-the-line checks

Treat these as P0 when live — each has actually happened in this repository:

- **Unsupported evidence reaching the KB.** A snippet not present in the cited
  source, a paraphrase presented as a quote, supplement text moved into the
  article cache, or a slot value the source is silent on. Also: strain-pair
  experimental findings generalized to a natural community, and a
  `cultivation_setup` sourced from a paper that never studied the community
  (#529).
- **A gate that reports clean because it never ran.** A workflow whose `paths:`
  filter does not cover the directory its own steps read (`kb/taxa` was in no
  filter at all — #471; `data/isolates` was outside every filter — #310), or a
  check that passes by skipping what it cannot resolve.
- **A check that cannot notice a new member.** A hard-coded list of record
  roots, directories, or writers that a newly added one silently bypasses.
- **Identifier collisions or dangling references** across `kb/communities`,
  `data/isolates`, and `kb/taxa`, or an id↔label MISMATCH / nonexistent CURIE
  reaching the committed `docs/` site or a KGX export.
- **Generated artifacts diverging from their source** — a hand-edited
  datamodel, or a committed `docs/` site that no longer matches the records it
  claims to render. Note that KGX products are *generated, not committed*, so a
  gate configured against `output/kgx/` may be skipping rather than passing
  (#686) — check which before citing it.
- **A corpus-rewriting tool that leaves no trace** (#325), or an in-place edit
  with no history entry.
- **An externally-facing claim** — a release, a Pages site, a count quoted
  outside the repo — that rests on any of the above.

Never recommend loosening a schema, validator, exception list, threshold, or
baseline so that generated output passes. That is a P0 in itself, not a fix.

### Step 6 — Assign priority, and cost separately

Priority states consequence. Cost/readiness orders the work. Keep them apart.

- **P0 — stop the line.** Corruption or fabrication in the curated corpus,
  leakage of unsupported claims into published products, a gate that is green
  by blindness, or a blocker in front of an already-planned expensive step.
- **P1 — real and schedulable.** Genuine defects, reproducibility and
  provenance gaps, evidence-policy violations that are contained, missing
  guards for a likely workflow, test-coverage gaps on safety-critical paths.
- **P2 — low-severity.** Documentation drift, stale comments, refactors,
  theoretical edge cases, optional audits, work confined to paths with no
  active consumer.
- **CLOSE / UPDATE.** Fixed, superseded, duplicate, no longer applicable, or a
  title materially broader than the remaining work. Cite the exact commit, PR,
  code location, or comment that supports the disposition.

Calibrate P0 sparingly, then order within and across tiers by:

1. upstream unblockers before downstream consumers;
2. a gate hole before the findings that gate would have caught — a fix landing
   behind a filter that does not run is not protected;
3. recovering evidence you already hold before fetching or regenerating it;
4. read-only and local checks before corpus sweeps or networked calls;
5. combining issues only when one patch genuinely satisfies each one's
   acceptance criteria.

Do not prioritize by age, by sunk effort, or by a `P0` string in a stale title.

### Step 7 — Report

Return a compact report with:

1. **Coverage** — repository, timestamp, number reviewed, completeness;
2. **Top 2–3 next actions**, and why each unblocks later work;
3. a **dependency-ordered P0/P1/P2 table**: issue number, current status,
   evidence, blockers, cost class, next acceptance test;
4. **CLOSE/UPDATE candidates** with specific cited evidence;
5. **unresolved evidence gaps** and cross-repository ownership;
6. a short **sequence** showing which costly work must wait on what.

Call out old issues explicitly rather than dropping them silently — a
six-month-old open issue is itself a signal. Keep measured findings, code
inspection, inference, and proposed-but-untested work visibly separate.

### Step 8 — Act only when asked

This skill does not close issues, comment, relabel, retitle, or create/update a
tracker on its own, and a general "yes, go ahead" is not blanket approval to
loop over every CLOSE candidate unattended.

- **Closing stale/duplicate issues**: confirm the specific issue number(s)
  before each closure. Once confirmed, `gh issue close <N> --comment "<reason>"`,
  one at a time, with the Step 4 evidence in the comment.
- **Maintaining the tracker**: verify it is still open
  (`gh issue view 669 --json state`) and update it in place rather than opening
  a second one. Only create a new tracker if the existing one is confirmed
  closed or superseded and the user wants a fresh one.

Never bulk-close without per-item confirmation. An agent closing a live issue
because it *looks* stale is worse than leaving noise in the queue.

## Conventions this skill enforces

- **Full-queue coverage, not first-page sampling.** State exactly how many
  issues were reviewed and whether coverage was complete.
- **Evidence over vibes.** Every CLOSE/UPDATE/duplicate recommendation cites a
  specific commit, PR, artifact, or code location — never "this looks done."
- **P0 is rare.** If more than ~10% of the queue lands P0, the calibration is
  wrong; recheck. A stale `P0:` string in a title is not evidence.
- **Titles are claims and they drift.** Issues get retitled mid-life —
  including to `[WITHDRAWN]` or `[RESOLVED]` — while staying open. Re-read
  titles at report time rather than trusting the ones fetched at the start.
- **The queue moves during the sweep.** A parallel PR can resolve an issue
  while triage is in progress. Re-check the open set immediately before
  reporting, and say so if it changed.
- **Read-only by default.** Ranking happens automatically; every GitHub
  mutation requires explicit per-item confirmation.

## Measurement discipline

The recurring failure here is not misreading evidence, it is **mismeasuring**
it. Before citing any of the following, confirm how it was obtained:

- **Exit codes through pipes.** `cmd | tail -3; echo $?` reports `tail`'s
  status, not `cmd`'s, so a fail-closed validator looks like it succeeded. Use
  `cmd >/tmp/o 2>/tmp/e; echo $?`, or `${PIPESTATUS[0]}`.
- **A count that counts the wrong thing.** `Total checks: N` in this repo's
  validator output counts *issues found*, not checks performed — a small number
  is not coverage. Only a planted, deliberately-wrong value proves a record was
  actually validated.
- **A green gate that never ran.** A PR showing "no checks reported" on a
  path-filtered workflow is not a pass. Confirm the workflow's `paths:` filter
  matches the files in question before treating CI as evidence.
- **Advisory commands mistaken for gates.** `just qc-references` is *not* a CI
  gate and may use the network; a green PR says nothing about whether its
  snippets validate. Read `CLAUDE.md` for which is which rather than assuming.
- **Whitespace-splitting file lists.** `git status --porcelain | awk '{print $2}'`
  turns one path containing spaces into several bogus entries. Use
  `--porcelain -z | tr '\0' '\n'`.
- **Glob patterns tested by shape.** A regex check on a `.gitignore` pattern
  tests what it looks like; `git check-ignore --no-index <path>` tests what it
  does. Only the second is evidence.
- **Truncated tool output.** Long lines get elided. Re-read the cited file at
  the cited line before acting on it — filenames guessed from a truncated
  console dump are a known way to produce a test that fails at baseline.
- **Backticks inside a double-quoted argument.** `gh issue create --title
  "... \`just qc\` ..."` *executes* the backticked text and ships its output in
  place of the example. Write any report, comment, or title containing shell
  examples via `--body-file` or a quoted heredoc (`<<'EOF'`), then read the
  result back before posting.
- **An outage is not a verdict.** A provider returning 403/402, or a fetch
  failing, means the check did not run — it does not mean the thing is absent.

## Notes & limitations

- `gh issue list --json` omits `comments` unless explicitly requested. This
  repository records corrections, withdrawals, and narrowed residuals in
  comments, so a body-only fetch systematically overstates what is open.
- An issue may be fully addressed in code while its acceptance criteria are
  not. Partial fixes stay open with a narrowed residual.
- Evidence recovery is sometimes impossible — when a residual asks for an
  artifact the repository records as absent, say so and recommend superseding
  rather than leaving the issue open indefinitely.
- Cross-Mech issues (a defect described once but relevant to CultureMech, MIM,
  or TraitMech) are common. Note where a fix should propagate, but do not open
  issues in sibling repos without being asked.
- No @-mentions in issue comments, tracker updates, or reports without explicit
  per-mention authorization (standing rule).
- The tracker issue predates this skill; reconcile it against reality the same
  as any other issue before trusting its contents.

## Mutation boundary

Do not close, comment on, relabel, retitle, or create issues or trackers during
the review. If the user later asks to act, present the exact issue numbers and
the proposed mutation first, then apply them one at a time with cited evidence.

Do not apply generated curation, edit records, regenerate committed products, or
make billed provider/network calls as part of triage. A recommended command is a
proposal, not permission to run it.

Do not open cross-repository issues, and do not use `@` mentions, without
explicit authorization.

## Related

- `next-tasks` — the lighter, `NEXT_TASKS.md`-scoped backlog check; run that for
  "what's next" during active work, this skill for a full-queue sweep.
- `review-communities` — record-level quality review, where a curation-shaped
  issue is usually handed off.
- `evidence-curation` — where an evidence/snippet issue is handed off.

## Related files

- `NEXT_TASKS.md` — items promoted from this ranking often get logged here too,
  so `next-tasks` picks them up on the next reconcile.
- `CLAUDE.md` — the canonical/generated table and the evidence policy this
  triage tests issues against.
