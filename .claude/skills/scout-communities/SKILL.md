---
name: scout-communities
description: Discover newly published microbial communities to add to CommunityMech. Queries Europe PMC for recent papers describing defined/structured communities (consortia, SynComs, co-cultures, syntrophic pairs), dedups hits against the existing kb/communities/ records (by cited PMID/DOI and community-name overlap), scores each by how strongly it reads as a community paper, and emits a curator report + queue (+ optional draft stubs) ready to hand to deep-research-community.
category: research
requires_database: false
requires_internet: true
version: 1.0.0
---

# Scout New Communities (Europe PMC discovery)

## Overview

**Purpose**: find *new* microbial communities worth curating. This is the
**discovery** counterpart to `deep-research-community` (which *enriches* a
community you already have a record for). It queries Europe PMC for recently
published papers about defined/structured communities, filters out anything
already covered by `kb/communities/`, ranks what's left, and produces a
curator-facing shortlist.

Free + reproducible: Europe PMC REST search needs **no API key** and spends no
credits, so it is safe to run broadly and often.

**When NOT to use**: to go deep on a single already-known community — use
`deep-research-community` instead. This skill finds candidates; it does not
mine one paper in depth.

## What it does

1. **Query** Europe PMC (`resultType=core`, relevance-ranked, date-filtered to
   recent first-publication dates, abstract required).
2. **Dedup** each hit against existing records two ways:
   - cited **PMID/DOI** already present in any `kb/communities/*.yaml`
     (`ALREADY_CITED`), and
   - **community-name token overlap** with the hit title (`TITLE_OVERLAP`,
     ≥50% of a record's name tokens) — catches the same community reported in a
     different paper.
   - everything else is `NEW`.
3. **Score** by community signal: distinct community-phrase matches in
   title+abstract (`consortium`, `SynCom`, `cross-feeding`, `syntrophy`,
   `co-culture`, …), with title matches double-weighted. Higher = more clearly
   a *community* paper vs. a single-organism study.
4. **Emit** a Markdown report, a queue JSON, and (optionally) review-only draft
   stub records.

It **never** mutates `kb/communities/`. Minting IDs and writing records stays a
human decision — the handoff is described below.

## Inputs

Exactly one query source (mutually exclusive):
- `--query "<free text>"` — arbitrary Europe PMC query, or
- `--preset <name>` — a ready-made angle: `general`, `syntrophy`, `syncom`,
  `coculture`, `engineered`.

Optional:
- `--since YEAR` — earliest first-publication year (default `2024`).
- `--limit N` — max Europe PMC hits to fetch (default `40`).
- `--min-score N` — drop hits below this community-signal score (default `1`).
- `--include-cited` — keep hits already cited by a record (default: drop them).
- `--emit-stubs` — write review-only draft `*.stub.yaml` records for sourced
  `NEW` hits and a batch-compatible `*-stub-queue.json`. Hits without a PMID or
  DOI remain in the candidate report but do not produce stubs.
- `--out-dir PATH` — default `research/scouting/`.

## Workflow

### Step 1 — Run a scouting pass

```bash
# Preset angle:
just scout-communities --preset syntrophy --since 2024 --limit 40

# Or a targeted free-text query:
just scout-communities --query "gut butyrate cross-feeding defined community" --since 2023

# Direct invocation is equivalent:
uv run python scripts/scout_communities.py --preset syncom --emit-stubs
```

Europe PMC query tips: field qualifiers work (`TITLE:consortium`,
`METHODS:"synthetic community"`), boolean `AND`/`OR`, and phrases in quotes.
The script auto-appends the date range and `HAS_ABSTRACT:Y`.

### Step 2 — Read the report

`research/scouting/scout-<slug>.md` lists candidates ranked `NEW` first, then
by score, then recency. Each entry shows dedup status, score, matched signals,
year/journal, the PMID/DOI, and an abstract snippet. Focus on `NEW`, high-score
rows; `TITLE_OVERLAP` rows are likely already curated (verify before adding).

The machine-readable `scout-<slug>-queue.json` carries the same candidates
(reference, title, year, score, dedup) for scripting the next step.

With `--emit-stubs`, `scout-<slug>-stub-queue.json` contains `file_path`,
`reference`, and `title` for each emitted stub and can be passed directly to
`research-community-edison-batch`.

### Step 3 — Hand promising candidates to curation

For each candidate you want to add:
1. **Mint an id** and create the record with `manage-identifiers`
   (`CommunityMech:NNNNNN`, `id` first, sanitized filename).
2. **Deep-research it** with `deep-research-community <stem-or-id>` to gather
   source-backed taxa, interactions, environment, cultivation, and CURIEs.
3. **Validate + curate** with `review-communities` and `evidence-curation`.

With `--emit-stubs`, minimal drafts land in `research/scouting/stubs/` with a
`CommunityMech:XXXXXX` placeholder id and a `_scout` provenance block — these
are **review-only scaffolding**, not valid records. Move + mint before they
enter `kb/communities/`.

## Output at a glance

```
research/scouting/
├── scout-<slug>.md              # ranked candidate report (read this)
├── scout-<slug>-queue.json      # candidates as JSON (for scripting)
├── scout-<slug>-stub-queue.json # sourced stub paths; Edison batch-compatible
└── stubs/                       # only with --emit-stubs; review-only drafts
    └── <title-slug>.stub.yaml   # placeholder id — mint before adding
```

## Notes & limitations

- **Relevance, not date sort**: the script relies on Europe PMC's relevance
  ranking and re-ranks in Python. Do **not** add a `sort=P_PDATE_D` param — it
  silently broadens the query to thousands of off-topic hits.
- **Dedup is heuristic**: token-overlap can miss a community reported under a
  very different name, and can flag a genuinely new community that shares words
  with an existing one. Always eyeball `TITLE_OVERLAP` rows.
- **Preprints appear alongside published versions** (e.g. a bioRxiv DOI plus the
  PNAS PMID for the same study) — the report shows both; pick the version of
  record.
- **Signal list is tunable**: edit `COMMUNITY_SIGNALS` / `PRESETS` in
  `scripts/scout_communities.py` to bias toward a subfield.

## Related

- `deep-research-community` — go deep on one candidate once you've picked it.
- `manage-identifiers` — mint the id and place the new record file.
- `review-communities`, `evidence-curation` — validate/curate the new record.

## Related scripts

- `scripts/scout_communities.py` — this skill's runner (Europe PMC query,
  dedup, scoring, report/queue/stub emission).
