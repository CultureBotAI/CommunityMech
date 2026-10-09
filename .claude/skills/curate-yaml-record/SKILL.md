---
name: curate-yaml-record
description: Review and curate one CommunityMech community, isolate, or reusable taxon YAML record for ecological scope, taxonomy, interactions, cultivation, environment, claim-level evidence, completeness, and resolvable gaps. Use for a named record audit or improvement; do not use for bulk scouting/ingestion or as permission to contact anyone, spend provider credits, or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Curate one CommunityMech YAML record

## Structured Review Output

For every new review or audit, follow
[docs/record-reviews.md](../../../docs/record-reviews.md) and
[the local profile](../../../docs/record-review-profile.md).
Capture exact targets and input hashes before judging, preserve this skill's
native rubric, rule IDs, scores and evidence requirements, then author the
structured assessment and run:

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
uv run python scripts/record_review.py validate /tmp/completed-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-review.yaml
```

Choose session-unique temporary paths. Save authoritative YAML and derived
Markdown under `reviews/structured/<timestamp>-<slug>/`; link both in the
final response. This output contract supersedes prose-only report examples.
A single record uses `kind: record`; batches declare exact selection,
population, reviewed targets and limits. Categories also state boundary decisions.
Every reviewed target must have an assessment. Keep P1-P4 and other native
severity/rule information with a justified common severity, and metric definitions,
scales and denominators. Do not infer scientific approval from a native score.

Raw provider drafts and deterministic validator/scan reports are diagnostic
inputs, not completed scientific reviews. Use `scientific_review: false`
for deterministic-only or provenance-only assessments; mark required unavailable
checks and incomplete coverage explicitly. A valid bundle does not change native
status, clear release holds, authorize edits, or append curation history.
For audit-only requests, stop after assessment and persistence; any application
steps below require curation intent.

Produce a defensible community or taxon record and an explicit account of what
is supported, corrected, missing, and genuinely unknown. Search results and raw
research reports are leads; only inspected sources can support a claim.

## Shared Contract

<!-- canonical:begin the-contract -->
Produce a defensible record and an explicit account of four things: what is
**supported**, what was **corrected**, what is **still unresolved**, and what is
**genuinely unknown**. The last two are different — a gap you searched for and
could not close is a finding; a gap you did not look at is not.

**One target.** Resolve exactly one record before touching anything. If a label
matches several, or a request names a family rather than a member, stop and
disambiguate. Silently substituting a similar record is the error that no later
check catches, because everything downstream is then correct about the wrong
thing.

**Audit preserves scientific inputs. Curation authorises edits to the named
record only.** A review or audit request changes no scientific record, status,
or curation history. It does save a new timestamped structured review through
`docs/record-reviews.md` and the native rubric in `docs/record-review-profile.md`.
A curate, improve, complete, correct or add-evidence request authorises local edits to that record and the smallest
maintained path its provenance requires — not to neighbours, not to whatever
else looked wrong on the way.

**Search results are leads. Only an inspected source supports a claim.** A
search hit, a deep-research report, a rendered page, and a generated artifact are
each somewhere to look, and none is evidence. Evidence is text you read in the
source, attached to the narrowest assertion it actually supports.
<!-- canonical:end the-contract -->

## Shared Boundaries

<!-- canonical:begin boundaries -->
- **A generated artifact is never the fix.** Pages, merged products, exports and
  derived indexes are outputs. Correct the input or rule that owns the value and
  regenerate; patching the output makes it look right once and diverge on the
  next build.
- **No outbound action without explicit authorisation for that action.** Do not
  launch paid research, contact an author, or create or edit a GitHub issue, PR
  or comment because curation seemed to call for it. Authorisation to curate a
  record is not authorisation to spend or to speak.
- **Absence is not evidence of falsity, and coverage is not a goal.** Never
  infer that an unstated optional property is false. Never fill an optional
  slot to make the record look more complete. An empty field the source does
  not address is correct.
- **Search before declaring anything absent — and search past `.gitignore`.**
  Before treating a record, evidence source, decision row or overlay as missing,
  search for its identifier, label and slug with an ignore-independent tool
  (`rg --no-ignore --hidden`, `grep -r`, or `find`). Ordinary search skips
  ignored files, so an ordinary miss is a search over a subset, not a result.
- **Preserve unrelated work.** Use a branch, and a separate worktree when the
  checkout is dirty or occupied by something else.
<!-- canonical:end boundaries -->

## Shared Evidence Standard

<!-- canonical:begin evidence-standard -->
- Each claim is its own object. A definition, an example, a relation and a
  mechanism edge are separate assertions; attach a source to the narrowest one
  it supports, never to the record as a whole.
- Resolve every DOI, PMID and CURIE, and read enough of the source to establish
  support for the *exact* claim and scope. A matching string from the wrong
  paper, or an unrelated sentence from the right one, is not support.
- A snippet is short verbatim text from the source. Interpretation belongs in a
  notes field, never inside the quotation.
- **The kind of source is part of the citation.** A database assertion, a
  primary experiment, a review, a prediction and a search snippet are different
  strengths of support. Cite each as what it is; never present a database row
  or a review as if it were the primary study.
- Association and prediction do not establish mechanism or causality. Do not
  let a co-occurrence or a computed score become a mechanism edge.
- **A near-miss is not a match.** Never ground to a CURIE or canonical label
  because it looks plausible, and never use a broader or related term as an
  exact identity. Unresolved stays unresolved, recorded as such, until a source
  resolves it.
- **Evidence about one thing supports a claim about that thing.** Do not
  generalise one organism, strain, protein instance, construct or experiment
  into a family-wide, universal or "optimal" claim. Scope inflation is the most
  common way a true observation becomes a false record.
- Keep conflicts. When sources disagree, record both and the disagreement; do
  not resolve it by omission.
- A bounded search that found nothing is a result. Report it as "not found,
  searched X" rather than leaving the field silently empty.
<!-- canonical:end evidence-standard -->

## Shared Write Contract

<!-- canonical:begin writing-back -->
**Write only through the path that preserves formatting and records history.**
Never hand-edit a curated YAML with a text editor or a generic dump: canonical
key order, quoting and derived metadata are what make the corpus diffable, and a
dump destroys them in one save.

Repositories in this fleet do this in three different, equally correct ways, and
which one applies is a property of the corpus:

- **Direct guarded write** — a narrowly scoped mutator loads the record, asserts
  its identity, changes only the reviewed nodes, appends a curation event, and
  writes through the repository's validated writer.
- **Registered editor** — no generic writer exists on purpose; in-place changes
  use text-preserving operations through an editor that is registered and
  behaviourally tested, and the writer audit rejects anything else.
- **Regenerate from inputs** — the record is a build product. The fix goes into
  the decision row, term request, overlay or source inventory that owns the
  value, and the record is regenerated; the YAML is never edited directly.

The section below says which one this repository uses and names the exact
functions or files. Do not guess from a sibling.

Inspect the diff before committing. Whole-file presentation churn — reordered
keys, requoted strings, a hundred lines changed to alter one value — means the
write path was bypassed; abandon and repair rather than commit it.
<!-- canonical:end writing-back -->

## Shared History And Attribution

<!-- canonical:begin history-and-attribution -->
- Use `curator="claude"` when no curator identity was supplied. **Never
  attribute an agent's judgement to the user.** The history entry is a record
  of who decided, and it will be read when the decision is questioned.
- Mark LLM assistance where the schema records it.
- **Do not append a history event when nothing substantive changed.** A
  no-op event is noise that makes real events harder to find.
- The history entry describes the actual diff. If the corpus derives status or
  history from inputs, never set them directly — change the input.
- A REVIEWED status means a human reviewed it. Do not invent one, and do not
  promote to it on the strength of an agent pass.
<!-- canonical:end history-and-attribution -->

## Boundaries

- Resolve one target under `kb/communities/`, `data/isolates/`, or `kb/taxa/`.
  If a name matches several communities, experiments, or taxon records, stop
  and disambiguate before editing.
- Audit/review preserves scientific inputs and saves a new structured review.
  Curate, improve, complete, correct, or
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
