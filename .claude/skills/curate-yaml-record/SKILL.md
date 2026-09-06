---
name: curate-yaml-record
description: Review and curate one CommunityMech community, isolate, or reusable taxon YAML record for ecological scope, taxonomy, interactions, cultivation, environment, claim-level evidence, completeness, and resolvable gaps. Use for a named record audit or improvement; do not use for bulk scouting/ingestion or as permission to contact anyone, spend provider credits, or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Curate one CommunityMech YAML record

Produce a defensible community or taxon record and an explicit account of what
is supported, corrected, missing, and genuinely unknown. Search results and raw
research reports are leads; only inspected sources can support a claim.

## Boundaries

- Resolve one target under `kb/communities/`, `data/isolates/`, or `kb/taxa/`.
  If a name matches several communities, experiments, or taxon records, stop
  and disambiguate before editing.
- An audit/review request is read-only. Curate, improve, complete, correct, or
  add-evidence requests authorize local edits to the named record and the
  smallest necessary history/generated-product paths.
- Do not generalize a strain pair, enrichment, synthetic consortium, or
  cultivation experiment into a natural-community claim.
- Never make an external provider call, spend credits, contact authors, or
  create/edit a GitHub item or other outbound message without explicit
  authorization for that action.
- Preserve unrelated work and use a dedicated branch/worktree for multi-file
  changes.
- Never fill an optional field merely for coverage or interpret absence as
  evidence of absence.

## Read before judging the record

Read the full target plus:

- `CLAUDE.md`;
- the applicable `MicrobialCommunity` or `CommonTaxon` class and the taxonomy,
  interaction, environment, cultivation, evidence, discussion, and history
  classes in `src/communitymech/schema/communitymech.yaml`;
- `history/README.md`;
- [references/review-checklist.md](references/review-checklist.md).

Inspect reusable `kb/taxa/` records, related communities, committed reference
cache entries, and any source data named by the record. Rendered pages and raw
research prose are not independent evidence.

## Workflow

### 1. Establish the baseline

Read the entire YAML. Record its ID, name, category/state/origin, environment,
taxa, interactions, factors, cultivation/growth media, external resources,
datasets, discussions, evidence, and curation history. For a community record:

```bash
just validate <record-path>
just validate-strict <record-path>
just validate-terms <record-path>
just validate-references-explained <record-path>
```

For `kb/taxa/`, use the dedicated taxon and term gates (`just validate-taxa`
and `just validate-terms-taxa`). A green schema result proves structure, not
ecological or evidentiary correctness.

### 2. Verify identity, scope, and taxonomy first

Confirm whether the record represents a natural community, enrichment,
synthetic consortium, isolate inventory, or another defined scope. Verify every
NCBITaxon/GTDB identifier, canonical label, strain designation, reusable taxon
reference, and community membership claim. Preserve source taxonomic names and
reclassification context instead of silently translating uncertain taxa.

### 3. Review every scientific claim

For each taxon, ecological interaction, environmental condition, metal,
metabolite, growth medium, cultivation condition, dataset, and causal direction,
verify that the cited source supports the exact participants, strain/taxon
scope, setting, direction, and strength of wording.

Every curated assertion should carry evidence at the claim it supports. Confirm
stable identifiers and exact snippets against committed abstract, full-text,
or supplement caches. Do not paraphrase a snippet, join non-contiguous text, or
present a database/search assertion as a primary experiment.

### 4. Assess completeness and resolve supported gaps

Apply the checklist and use bounded searches for consequential gaps. Prioritize:

1. wrong community scope or member identity;
2. unsupported or reversed interactions and causal edges;
3. missing strain, experimental, spatial, or environmental context;
4. cultivation/growth claims linked to the wrong community or medium;
5. missing evidence on material composition, function, or outcome claims.

Do not add a generic discussion for every empty slot. A discussion should name
a concrete uncertainty, what was checked, why it matters, and what source would
resolve it.

### 5. Write through the guarded path

Use a narrowly scoped mutator that loads the record, asserts its ID/path,
changes only reviewed nodes, calls
`communitymech.curate.curation_event.record_curation_event` with
`llm_assisted=True`, and writes through
`communitymech.validation.write_validated.write_validated_community`.
For a reusable taxon, pass `target_class="CommonTaxon"`; the default is
`MicrobialCommunity`.

Use `curator="claude"` when no identity was supplied. Do not attribute agent
judgement to the user and do not append an event if content is unchanged.
Create the required append-only repository history entry with `just
new-history`; never revise an older history record.

### 6. Verify and report

Repeat the focused validation and run proportional wider gates:

```bash
just validate-history
just audit-writers
just qc
git diff --check
git diff -- <record-path> history src scripts docs
```

If a community record changed, regenerate/check committed pages with `just
gen-html` and `just check-docs-current` as required. Re-read the result and
ensure citations, snippets, and history describe the actual diff.

Report corrections/additions and sources, retained claims checked, unresolved
gaps and bounded searches, target class used, history artifact, and validation
results. CommunityMech has no record-level REVIEWED flag; never invent one.
