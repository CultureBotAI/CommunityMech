---
name: deep-research-community
description: Run Edison Scientific deep research (PaperQA3) for a CommunityMech microbial-community record to gather source-backed composition, ecological interactions/mechanisms, environment, cultivation conditions, and ontology grounding (NCBITaxon/ENVO/CHEBI/GO). Captures a full provenance bundle and produces a curation-focused report for a curator to review and apply.
category: research
requires_database: false
requires_internet: true
version: 1.0.0
---

# Deep Research for a Community (Edison API)

## Overview

**Purpose**: For one CommunityMech community record, run an Edison
Scientific `LITERATURE` (PaperQA3) deep-research job that mines primary
literature, PubMed/PMC, NCBI, BioProject/SRA, and ontology resources
for: confirmed taxa & strain designations, mechanistic interactions
(cross-feeding, syntrophy, competition, ...), environment & cultivation
conditions, and candidate CURIEs (NCBITaxon / ENVO / CHEBI / GO /
PMID / DOI).

This is the CommunityMech port of CultureMech's `deep-research-medium`.
It ships the **phase-1 single-record** flow; the per-entity follow-up
("phase 2") is deferred. The response-capture plumbing
(`_edison_capture.py`) is vendored verbatim from CultureMech and is
byte-identical across the Mech repos.

**When NOT to use**: skip if a recent research output already exists for
the target community — re-running spends API credits. For a quick
non-Edison pass, `just research-community <provider> <target>` uses
`deep-research-client` instead.

## Prerequisites

- `EDISON_PLATFORM_API_KEY` (or the legacy `EDISON_API_KEY` already in
  this repo's `.env`) set in repo-root `.env` or environment.
- `edison-client` SDK installed: `uv sync --extra dev`.
- Template: `templates/community_mechanism_research.md` (shared with the
  DRC wrapper — same `{placeholder}` variables).

## Inputs

The skill expects one of:
- A community **filename stem** (e.g. `Yogurt_TwoSpecies_Starter_Culture`),
- A **CommunityMech id** (e.g. `CommunityMech:000164`), or
- A **YAML path** under `kb/communities/`.

Optional:
- `--job` (default `literature`; alternatives: `literature-high`,
  `precedent`, `phoenix`).
- `--dry-run` to render the query + write meta yaml without spending
  credits.

## Workflow

### Step 1 — Resolve the community

Resolve the user's input to a single YAML file under `kb/communities/`:

```bash
uv run --extra dev python -c "
import sys; sys.path.insert(0, 'scripts')
import research_community as rc
print(rc.resolve_community_file('<TARGET>'))
"
```

If the target is not found, the resolver lists available communities;
surface those to the user.

### Step 2 — Check for existing research output

```bash
ls research/communities/<stem>-edison-*.md 2>/dev/null
```

If a recent output exists (`meta.yaml` shows a real `task_id` and
`submitted_at`), tell the user and ask whether to re-run. **Do not
silently re-spend credits.**

### Step 3 — Run the deep-research job

Dry-run first so the rendered query is auditable before spending:

```bash
just research-community-edison <stem-or-id> --dry-run
```

Then for real:

```bash
just research-community-edison <stem-or-id>
# or with overrides:
uv run --extra dev python scripts/research_community_edison.py \
    --target <stem-or-id-or-path> \
    --job literature \
    --template templates/community_mechanism_research.md \
    --out-dir research/communities
```

Outputs (per task; `<stem>` is `<community-stem>-edison-literature`):
- `<stem>.md` — primary Markdown answer (`formatted_answer` preferred).
- `<stem>-meta.yaml` — task_id, cost, status, `query_sha256`, full
  rendered query, template_vars, char counts, sidecar inventory.
- `<stem>-response.json` — full `response.model_dump(mode="json")`.
- `<stem>-citations.md` — parsed reference list (DOI/PMID/URL).
- `<stem>-agent-state.json` — PaperQA tool-call trace + env frame.
- `<stem>-files.json` — inventory of any artifacts Edison produced.

In `--dry-run` mode only the meta yaml is written; the `query_sha256`
still lets you diff a planned prompt against prior runs.

**Retroactive enrichment**: if a meta yaml has a `task_id` but is
missing sidecars (e.g. captured by an older script), run
`just enrich-edison-response` to pull verbose + files + parse citations
without re-billing.

### Step 4 — Hand off to the curator

Read `<stem>.md` and summarize for the user:
- Confirmed taxa / strain designations and how they compare to the
  record's existing `taxonomy`.
- Candidate interaction updates (source taxon, target taxon, exchanged
  metabolite/process, evidence snippet, explanation).
- Candidate environmental-factor / growth-media updates and CURIEs.
- The total reported cost.

Do **not** mutate `kb/communities/` files in this skill — that is the
curator's call after reading the report. The per-task markdown + meta
files are the audit trail and source of truth for citations.

## File outputs at a glance

```
research/communities/
├── <stem>-edison-literature.md             # answer
├── <stem>-edison-literature-meta.yaml      # audit (task_id, cost, query, ...)
├── <stem>-edison-literature-response.json  # full SDK response
├── <stem>-edison-literature-citations.md   # parsed refs
├── <stem>-edison-literature-agent-state.json
└── <stem>-edison-literature-files.json
```

## Cost & safety

- `LITERATURE` typically costs a few cents per community;
  `LITERATURE_HIGH` is several times more expensive.
- Run `--dry-run` first on new communities to audit the rendered query.
- Use `research-community-edison-batch <queue.json>` to go *wide*
  across many communities (JSON list of stems/ids/paths); use this
  skill to go *deep* on one.

## Error handling

- **`edison-client` not installed**: run `uv sync --extra dev`.
- **Missing API key**: add `EDISON_PLATFORM_API_KEY=...` (or
  `EDISON_API_KEY=...`) to repo-root `.env`.
- **Target not found**: the resolver lists available communities; ask
  the user to pick.
- **API failure**: surface the error; do not auto-retry (avoids
  accidental double-billing).

## Related skills

- `review-communities`, `evidence-curation` — validate and curate the
  evidence the report recommends.
- `metpo-proposal`, `manage-identifiers` — propose new terms / mint IDs.

## Related scripts

- `scripts/research_community_edison.py` — this skill's runner.
- `scripts/_edison_capture.py` — shared response-capture helpers
  (vendored from CultureMech, byte-identical across Mech repos).
- `scripts/enrich_edison_response.py` — retroactive sidecar backfill
  (no re-billing).
- `scripts/research_community.py` — the non-Edison `deep-research-client`
  wrapper (provider-based).

## Quick reference

```bash
# Single community (dry-run to audit the query first):
just research-community-edison <stem-or-id> --dry-run
just research-community-edison <stem-or-id>

# Deeper job:
just research-community-edison <stem-or-id> --job literature-high

# Batch (JSON list of stems/ids/paths):
just research-community-edison-batch queue.json --limit 5

# Backfill provenance for older runs (no re-billing):
just enrich-edison-response
```
