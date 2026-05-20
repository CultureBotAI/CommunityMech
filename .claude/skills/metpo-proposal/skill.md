---
name: metpo-proposal
description: Generate a ROBOT-template METPO proposal that lifts CommunityMech LinkML enums, classes, and slots into METPO classes and predicates with a curated hierarchy
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
tags: [metpo, ontology, robot, linkml, proposal, schema-lift, kg-microbe]
---

# METPO Proposal Skill

## Overview

Turn a slice of the CommunityMech LinkML schema (one or more `*Enum`
permissible-value sets, plus the slots that connect them) into a METPO
ROBOT-template proposal that can be merged with the existing kg-microbe
METPO proposal pipeline.

Three artifacts are produced under `proposals/<cohort-name>/`:

| File | Format |
|---|---|
| `metpo_proposal_classes_robot.tsv` | 11-column ROBOT template (mirrors kg-microbe convention) |
| `metpo_proposal_properties_robot.tsv` | 12-column ROBOT template |
| `proposal.md` | Reviewer narrative: scope, hierarchy decisions, predicate rationale, verification, upstream path |

**Run from `CommunityMech/CommunityMech/` directory.** Reference example:
[PR #74](https://github.com/CultureBotAI/CommunityMech/pull/74) and the files
under `proposals/metpo_communitymech_v1/`.

---

## When to use this skill

- A new CommunityMech enum (or set of enums) is added to
  `src/communitymech/schema/communitymech.yaml` and should be exposed to
  KG-Microbe consumers as METPO classes.
- An existing METPO proposal cohort needs an additional batch of community
  scope (e.g., lifting `AtmosphereEnum` after a previous round shipped the
  9 community-shaped enums).
- A reviewer asks for "the METPO version" of a CommunityMech slot
  (e.g., `EcologicalInteraction.source_taxon` → `has source taxon` object
  property).

Do NOT use for: lifting PATO/GO/CHEBI cross-references (those already exist
upstream), lifting tolerance ranges (use the upstream
[kg-microbe metpo-proposal skill](https://github.com/Knowledge-Graph-Hub/kg-microbe/blob/main/.claude/skills/metpo-proposal/SKILL.md)
which handles the paired positive/negative predicate convention).

---

## Required reading

Before generating a proposal, read:

1. **[kg-microbe/.claude/skills/metpo-proposal/SKILL.md](https://github.com/Knowledge-Graph-Hub/kg-microbe/blob/main/.claude/skills/metpo-proposal/SKILL.md)**
   (local clone path: `~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/.claude/skills/metpo-proposal/SKILL.md`) —
   the upstream metpo-proposal skill. Defines:
   - Aristotelian definition style
   - `definition_source` citation forms (PMID, DOI, BacDive, `TODO:add_citation`)
   - Numeric ID-range conventions
   - Parent-class selection (audit for siblings before falling back to
     `METPO:1000000`)
   - The 12-point pre-submission checklist
2. **[kg-microbe/mappings/metpo_proposal_classes_robot.tsv](https://github.com/Knowledge-Graph-Hub/kg-microbe/blob/main/mappings/metpo_proposal_classes_robot.tsv)** —
   the canonical 11-column class template. Copy the two-row header verbatim.
3. **[kg-microbe/mappings/metpo_proposal_properties_robot.tsv](https://github.com/Knowledge-Graph-Hub/kg-microbe/blob/main/mappings/metpo_proposal_properties_robot.tsv)** —
   the canonical 12-column property template.
4. **`proposals/metpo_communitymech_v1/`** in this repo — the reference
   example. Read all three files end-to-end before writing a new cohort.

---

## ROBOT template column conventions

These are the only column structures that will parse cleanly. Tab-separated,
two header rows.

**Classes** (11 columns):

```
proposed_id<TAB>label<TAB>definition<TAB>definition_source<TAB>parent<TAB>synonyms<TAB>xrefs<TAB>subset<TAB>priority<TAB>observations<TAB>traits_addressed
ID<TAB>LABEL<TAB>A IAO:0000115<TAB>>A IAO:0000119<TAB>SC %<TAB>A oboInOwl:hasExactSynonym SPLIT=|<TAB>A oboInOwl:hasDbXref SPLIT=|<TAB>A oboInOwl:inSubset<TAB><TAB><TAB>
```

**Properties** (12 columns):

```
proposed_id<TAB>label<TAB>definition<TAB>definition_source<TAB>type<TAB>domain<TAB>range<TAB>xrefs<TAB>subset<TAB>priority<TAB>traits_addressed<TAB>observations
ID<TAB>LABEL<TAB>A IAO:0000115<TAB>>A IAO:0000119<TAB>TYPE<TAB>DOMAIN<TAB>RANGE<TAB>A oboInOwl:hasDbXref SPLIT=|<TAB>A oboInOwl:inSubset<TAB><TAB><TAB>
```

The **second row (ROBOT header) must have trailing tabs to reach the full
column count**, even when the trailing columns are blank. Validate with:

```bash
awk -F'\t' 'NF != 11 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_classes_robot.tsv
awk -F'\t' 'NF != 12 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_properties_robot.tsv
```

Both commands should print nothing.

---

## ID-space conventions

| Range | Use |
|---|---|
| `METPO:1000000` | METPO root (use as `SC %` parent only when no closer parent exists) |
| `METPO:1000525` | "microbe" — use as `DOMAIN` for predicates whose subject is a microbial taxon |
| `METPO:1007NNN` | **Placeholder** range for new class proposals from KG-Microbe / CommunityMech (reserved per the SKILL.md placeholder policy). Real METPO IDs are minted upstream after sign-off. |
| `METPO:2007NNN` | **Placeholder** range for new predicate proposals from this pipeline. |

Within `METPO:1007NNN` and `METPO:2007NNN`, allocate contiguous numeric blocks
per enum so the file scans easily. The v1 proposal uses:

- `1007100`–`1007102` — top-level domain classes
- `1007103`–`1007110` — `FunctionalRoleEnum`
- `1007120`–`1007132` — `InteractionTypeEnum`
- `1007140`–`1007142` — `InteractionScopeEnum`
- `1007150`–`1007155` — `EvidenceItemSupportEnum`
- `1007160`–`1007165` — `EvidenceSourceEnum`
- `1007170`–`1007174` — `AbundanceEnum`
- `1007180`–`1007184` — `EcologicalStateEnum`
- `1007190`–`1007193` — `CommunityOriginEnum`
- `1007200`–`1007220` — `CommunityCategoryEnum`

Future cohorts should pick a fresh block starting at `1007300+` or higher to
avoid collision; document the new block in `proposal.md`.

---

## Subset tag

Every row must carry the same `oboInOwl:inSubset` value in column 8 (classes)
or column 9 (properties). Format: `metpo_<repo-id>_<YYYY>_<MM>`.

Examples:
- `metpo_communitymech_2026_05` — initial CommunityMech cohort (v1)
- `metpo_kgmicrobe_2026_04` — existing kg-microbe cohort

---

## Workflow

### 1. Pick the scope

For each LinkML enum or class you intend to lift, write a one-line statement
of why it belongs in METPO. If the answer is "because KG-Microbe consumers
need to filter by it", proceed; if it's "because it's in the schema",
reconsider — METPO is a curated ontology, not a schema dump.

Skip enums that are pure machine identifiers (e.g., `DatasetTypeEnum`,
`CultureCollectionEnum`); those belong in NMDC / re3data, not METPO.

### 2. Design the hierarchy

For each enum:

- **Pick a parent class** (will be `METPO:1007NNN` enum-parent — invent one if
  none exists). Definition source: schema enum's own `description:` field.
  Cite as `CommunityMech:communitymech.yaml#<EnumName>`.
- **Decide on intermediate parents**:
  - Use them when the enum description or comments group values by valence
    (e.g., InteractionTypeEnum's `+/+, -/-` annotations → positive/negative
    parents).
  - Use them when the schema has explicit `is_a` hints in comments
    (e.g., `STRAIN_COMPETITION` ⊂ `COMPETITION`).
  - Use them when there is an obvious ecological / functional grouping (e.g.,
    `CommunityCategoryEnum` clusters into metal-processing, host-associated,
    etc.).
  - Otherwise leave the enum flat.
- **Lift each permissible value as a leaf class**. The leaf's
  `definition_source` is `CommunityMech:communitymech.yaml#<EnumName>.<VALUE>`.
  The leaf's `parent` (`SC %`) is the appropriate intermediate parent or the
  enum-parent.

For each top-level CommunityMech class (e.g., `MicrobialCommunity`,
`EcologicalInteraction`, `EvidenceItem`) that is referenced as a predicate
domain or range, declare a **top-level domain class** under `METPO:1000000`.
These get IDs like `1007100`–`1007102` in the v1 cohort.

### 3. Design the predicates

For each LinkML slot that:
- has a non-primitive range (i.e., references another class or enum), AND
- is exercised by at least one community YAML in `kb/communities/`,

write one object-property row. Domain and range MUST resolve either to:
- another row in the same proposal (e.g., `METPO:1007101` for community
  interaction), or
- an existing METPO IRI (`METPO:1000525` for microbe), or
- an external IRI (`NCBITaxon:1`, `CHEBI:24431`, `GO:0008150`).

Skip slots that just hold metadata (e.g., `community_id`, `created_at`).

Use the `does not X` paired-negative convention only when the predicate
relates a microbe to a chemical/physical capability (per the kg-microbe
SKILL.md). Domain-modeling slots (community ↔ taxon, interaction ↔ scope)
have no meaningful negative form; do not pair them.

### 4. Write the TSVs

Write `metpo_proposal_classes_robot.tsv` and
`metpo_proposal_properties_robot.tsv` directly with the `Write` tool. Build
each row as a literal tab-separated string. After writing, fix the ROBOT
header row's trailing tabs:

```bash
python3 -c "
lines = open('proposals/<cohort>/metpo_proposal_classes_robot.tsv').readlines()
lines[1] = lines[1].rstrip('\n') + '\t\t\t\n'  # 3 trailing tabs to reach 11 cols
with open('proposals/<cohort>/metpo_proposal_classes_robot.tsv', 'w') as f:
    f.writelines(lines)
"
```

### 5. Verify

```bash
# Column-count sanity (must print nothing)
awk -F'\t' 'NF != 11 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_classes_robot.tsv
awk -F'\t' 'NF != 12 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_properties_robot.tsv

# Enum coverage — every CommunityMech permissible value should appear as a leaf row
# Use the per-enum-value definition_source markers (e.g., "FunctionalRoleEnum.PRIMARY_DEGRADER")
python3 <<'EOF'
import re
schema = open('src/communitymech/schema/communitymech.yaml').read()
target_enums = ['FunctionalRoleEnum', 'InteractionTypeEnum', 'EvidenceItemSupportEnum']
# ... see proposals/metpo_communitymech_v1/ for the canonical coverage check
EOF

# Parent integrity — every SC % parent must resolve in-file or to a known METPO IRI
# See proposals/metpo_communitymech_v1/ for the canonical integrity check
```

If you have ROBOT installed locally, also run:

```bash
robot template --template proposals/<cohort>/metpo_proposal_classes_robot.tsv \
    --output /tmp/classes.owl
robot template --template proposals/<cohort>/metpo_proposal_properties_robot.tsv \
    --output /tmp/properties.owl
robot merge --input metpo-edit.owl --input /tmp/classes.owl --input /tmp/properties.owl \
    --output /tmp/merged.owl
robot reason --reasoner ELK --input /tmp/merged.owl --output /tmp/reasoned.owl
```

ROBOT must parse both TSVs and ELK must reason without unsatisfiable classes.

### 6. Write the narrative

`proposal.md` is the reviewer's entry point. Required sections:

| Section | Content |
|---|---|
| **Context** | Why this cohort exists; what gap it fills in METPO |
| **Scope** | Table of enums lifted × parent class × leaf count |
| **Hierarchy decisions** | Per intermediate-parent: why you grouped these enum values together (cite schema comments where possible) |
| **Predicate proposals** | Table of property rows × domain × range × source slot |
| **ID space and subset** | The blocks you allocated and the subset tag |
| **Files** | Three-row table listing each artifact and row count |
| **Verification** | ROBOT commands plus the column-count and coverage checks |
| **Upstream path** | What happens after CommunityMech sign-off (typically: copy TSVs to `kg-microbe/mappings/`, run SKILL.md checklist, mint real METPO IDs) |
| **Change log** | Version + date + headline change |

### 7. Open a PR

Standard CommunityMech workflow:

```bash
git checkout -b claude/metpo-<cohort>-proposal
git add proposals/<cohort>/
git commit -m "Add METPO ROBOT-template proposal: <cohort>"
git push -u origin claude/metpo-<cohort>-proposal
gh pr create --title "METPO ROBOT-template proposal: <cohort>"
gh api repos/CultureBotAI/CommunityMech/pulls/<n>/requested_reviewers -X POST -f "reviewers[]=Copilot"
```

---

## Updating an existing proposal

The workflow above produces a **new** cohort. When work on an existing cohort
isn't finished, pick one of three update paths instead of starting fresh.

### Decision rule

| Situation | Path | Why |
|---|---|---|
| Reviewer (human or Copilot) asks for changes on an open PR before merge | **Edit in place** | The IDs and subset tag are still proposal-stage; no downstream consumer has pinned them yet. |
| Cohort is merged on main and you want to add more enum lifts (e.g., `AtmosphereEnum` after the original 9 enums) | **Extend in place** | Append-only is non-breaking; reviewers can diff the new rows against the same cohort. |
| Cohort is merged and the underlying schema changed in a way that invalidates existing rows (e.g., an enum value was renamed or removed, or a definition was sharpened in a way that breaks substring lifts) | **New cohort version** | A breaking semantic change needs a fresh subset tag and ID block so consumers can pin to the old or new version. |
| Real METPO IDs have been minted upstream and a row has been re-IDed | **New cohort version** | Mutating an already-minted ID is hostile to downstream consumers. |

### Path A — Edit in place (open PR)

Modify rows directly in
`proposals/<cohort>/metpo_proposal_*.tsv`. Keep the original
`proposed_id`, `subset`, and column structure. Update
`definition`, `definition_source`, `parent`, `synonyms`, or
`label` in place. Re-run the verification steps (column-count,
enum-coverage, parent-integrity). Commit on the same branch and
let the Copilot review thread close.

If the edit is to the narrative only (no TSV change), edit
`proposal.md` and add a one-line note under the Change log
section: `- v1, 2026-05 (revised <date>): <one-line summary>`.

### Path B — Extend in place (merged cohort)

Add new rows to the **same** `metpo_proposal_*.tsv` files in the
**same** cohort directory. Append-only — never reorder or
renumber existing rows. Conventions:

- New rows use a **contiguous fresh block** within the same
  `METPO:1007NNN` / `METPO:2007NNN` range. Pick a block at least
  10 above the highest existing ID to leave room for v1 patches.
  Document the new block in `proposal.md` under the ID space
  section.
- Same `subset` tag as the rest of the cohort. The tag identifies
  the cohort, not the round of additions.
- New `parent` references may point at existing rows in the cohort
  (this is the main reason to extend rather than re-version).
- Update `proposal.md`:
  - Add the new enum(s) to the Scope table.
  - Add the new ID block to the ID space section.
  - Append a Change log entry: `- v1.N, <date>: extended with
    <enum names> (+<row count> classes / +<row count>
    properties)`.

Open a new PR titled `Extend METPO proposal <cohort> with
<enum-names>`. Re-request Copilot review.

### Path C — New cohort version

Create a fresh directory
`proposals/<base-name>_v<N>/` (e.g., `metpo_communitymech_v2/`)
with:

- Fresh `subset` tag: bump the month-year suffix
  (`metpo_communitymech_2026_05` → `metpo_communitymech_2026_07`).
- Fresh **ID block** in the `1007NNN` / `2007NNN` placeholder
  range, **not overlapping with v1**. Document the new block in
  v2's `proposal.md`.
- v2 `proposal.md` must include a `## Relationship to v1` section
  that names every v1 ID retired or redefined, with the reason.
- v1 stays on disk read-only. Add a top-of-file note to v1's
  `proposal.md`: `> Superseded by
  proposals/<base-name>_v<N>/proposal.md (<date>). v1 is retained
  for traceability.`

Use this path sparingly — the kg-microbe pipeline assumes one
active cohort per source repository at a time, and re-versioning
forces downstream consumers to switch their queries.

### What not to do

- Do **not** edit IDs after they've been merged on main (use
  Path B or C instead).
- Do **not** mix Path B (extend) and Path C (re-version) in the
  same PR — reviewers can't tell what's append-only vs. breaking.
- Do **not** delete rows in Path B. If a row is obsolete, mark it
  by setting `priority` to `LOW` and adding an observation note;
  let Path C retire it cleanly.

---

## Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| `awk` reports row 2 has 8/9 columns | Trailing tabs missing on ROBOT header | Append `\t\t\t` to row 2 (see step 4) |
| ROBOT error "subject of axiom is not a class" | Property row referencing a class IRI in the `RANGE` column when ROBOT expects a class declaration | Declare the range class as its own row in the classes TSV first |
| ELK reports unsatisfiable class | Intermediate parent created with conflicting `SC %` axioms | Inspect the parent chain — usually a copy-paste error in the `parent` column |
| Copilot flags "schema lifted incorrectly" | The leaf's definition doesn't match the schema enum's description verbatim | Copy the schema description verbatim into the `definition` column; reword in the proposal narrative if you want a different phrasing |
| Reviewer asks for an existing METPO ID | The lifted concept already exists in METPO under a different label | Use the existing IRI; record the alias in `mappings/metpo_existing_aliases.tsv` upstream when copying to kg-microbe |

---

## Canonical example

The v1 cohort `proposals/metpo_communitymech_v1/` lifts 9 CommunityMech enums
(74 leaf + parent classes) and 14 predicates. Inspect that directory before
writing a new cohort — every convention in this skill was instantiated there.

Coverage check from v1: **52/52 enum permissible values** mapped to leaf class
rows; **74/74 `SC %` parent references** resolved. PR #74 in the CommunityMech
repo has the full reviewer trace.
