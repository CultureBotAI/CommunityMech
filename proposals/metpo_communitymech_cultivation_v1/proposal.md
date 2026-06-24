# METPO proposal — CommunityMech cultivation setup cohort

## Context

CommunityMech PR #171 added an optional `cultivation_setup` to
`MicrobialCommunity`, capturing the **hardware/instrumentation** and
**operating mode** used to grow or sustain a community — information that
KG-Microbe consumers want to filter and query (e.g. "communities grown in a
microbial fuel cell", "chemostat vs batch enrichments"). The new controlled
terms live in two LinkML enums (`CultivationModeEnum`, `CultivationSystemEnum`)
plus the `CultivationSetup` class, and are mirrored in
`vocab/cultivation_terms.yaml` (label/definition/synonyms/mapping/status). This
cohort lifts that slice into METPO so the terms are first-class ontology classes
and predicates rather than schema-only strings.

This is a **new cohort** (distinct thematic block), complementing the v1 cohort
(`proposals/metpo_communitymech_v1/`) which lifted the community/interaction/
evidence/atmosphere/metal enums.

## Scope

| Source | METPO parent | Leaf count |
|---|---|---|
| `CultivationSetup` (class) | `METPO:1000000` (root) → `METPO:1008100` top-level domain | — |
| `CultivationModeEnum` | `METPO:1008101` (enum-parent) | 10 |
| `CultivationSystemEnum` | `METPO:1008102` (enum-parent) | 13 minted + 1 mapped to OBI |

26 class rows total (1 top-level domain + 2 enum-parents + 23 leaves) and 3 object
properties.

## Hierarchy decisions

- **`METPO:1008100` "microbial community cultivation setup"** is a new top-level
  domain class (under the METPO root), mirroring how the v1 cohort lifted
  `GrowthMedia` to `METPO:1007300` "community-relevant growth medium". A
  cultivation setup is conceptually orthogonal to medium composition, so it gets
  its own domain rather than hanging under growth medium.
- The two enums are kept **flat** under their enum-parents (`cultivation mode`,
  `cultivation system`). Their schema descriptions carry no valence or
  is-a groupings (unlike `InteractionTypeEnum`'s +/− annotations), so no
  intermediate parents are warranted. Several system leaves are bioreactor
  subtypes and could be re-parented to OBI:0001046 upstream if a reviewer
  prefers a deeper hierarchy; left flat here for clarity.
- **`CultivationSystemEnum.BIOREACTOR_UNSPECIFIED` is NOT minted.** It maps to the
  existing **OBI:0001046 "bioreactor"** (recorded in the schema enum as
  `meaning: OBI:0001046` and in `vocab/cultivation_terms.yaml` with
  `status: mapped`). Per the kg-microbe SKILL.md "use the existing IRI" rule —
  the same convention the v1 metal/REE enums followed by leaving per-element
  values as CHEBI IRIs — this proposal references OBI:0001046 rather than minting
  a duplicate. Record the alias in `mappings/metpo_existing_aliases.tsv` upstream.
- **`OTHER` catch-alls** (`METPO:1008119`, `METPO:1008132`) are minted at
  `priority: MEDIUM` with an observation flag; they are candidates to drop during
  upstream review.

## Predicate proposals

| ID | label | domain | range | source slot |
|---|---|---|---|---|
| `METPO:2008100` | has cultivation setup | `METPO:1007100` microbial community | `METPO:1008100` cultivation setup | `MicrobialCommunity.cultivation_setup` |
| `METPO:2008101` | has cultivation mode | `METPO:1008100` cultivation setup | `METPO:1008101` cultivation mode | `CultivationSetup.cultivation_mode` |
| `METPO:2008102` | has cultivation system | `METPO:1008100` cultivation setup | `METPO:1008102` cultivation system | `CultivationSetup.system_type` |

`has cultivation setup` is exercised in `kb/communities/` (e.g.
`Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community` →
`BIOELECTROCHEMICAL_SYSTEM`). The mode/system structural predicates are part of
the new feature and proposed alongside; no negative (`does not …`) forms apply
(these are domain-modeling relations, not microbe↔capability relations).

## ID space and subset

- **Classes:** `METPO:1008100`–`METPO:1008132` (contiguous, above the v1 cohort
  high-water mark of `METPO:1008013`; verified no overlap with v1).
  - `1008100` domain; `1008101`/`1008102` enum-parents; `1008110`–`1008119` mode
    leaves; `1008120`–`1008132` system leaves.
- **Predicates:** `METPO:2008100`–`METPO:2008102` (above the v1 high-water mark of
  `METPO:2008002`).
- **Subset tag (all rows):** `metpo_communitymech_2026_06`.

These are placeholder IDs in the `1007NNN`/`1008NNN` / `2008NNN` range; real METPO
IDs are minted upstream after sign-off.

## Files

| File | Rows |
|---|---|
| `metpo_proposal_classes_robot.tsv` | 28 (2 header + 26 classes) |
| `metpo_proposal_properties_robot.tsv` | 5 (2 header + 3 properties) |
| `proposal.md` | this narrative |

## Verification

```bash
# Column-count sanity (must print nothing)
awk -F'\t' 'NF != 11 {print NR": "NF" cols"}' proposals/metpo_communitymech_cultivation_v1/metpo_proposal_classes_robot.tsv
awk -F'\t' 'NF != 12 {print NR": "NF" cols"}' proposals/metpo_communitymech_cultivation_v1/metpo_proposal_properties_robot.tsv
```
Performed and passing: enum coverage (every permissible value lifted to a leaf, or
externally mapped: `BIOREACTOR_UNSPECIFIED` → `OBI:0001046`); parent integrity
(every `SC %` parent resolves in-file or to `METPO:1000000`); no duplicate IDs; no
ID overlap with `metpo_communitymech_v1`.

If ROBOT is installed locally:
```bash
robot template --template proposals/metpo_communitymech_cultivation_v1/metpo_proposal_classes_robot.tsv --output /tmp/cult_classes.owl
robot template --template proposals/metpo_communitymech_cultivation_v1/metpo_proposal_properties_robot.tsv --output /tmp/cult_props.owl
robot merge --input metpo-edit.owl --input /tmp/cult_classes.owl --input /tmp/cult_props.owl --output /tmp/cult_merged.owl
robot reason --reasoner ELK --input /tmp/cult_merged.owl --output /tmp/cult_reasoned.owl
```

## Upstream path

After CommunityMech sign-off: copy both TSVs into `kg-microbe/mappings/`, run the
kg-microbe metpo-proposal SKILL.md pre-submission checklist, record
`BIOREACTOR_UNSPECIFIED → OBI:0001046` in `mappings/metpo_existing_aliases.tsv`,
and mint real METPO IDs for the 26 minted classes + 3 predicates.

## Change log

- v1, 2026-06 — initial cultivation cohort: lift `CultivationModeEnum` (10) and
  `CultivationSystemEnum` (13 minted + OBI:0001046 mapping) under a new
  `microbial community cultivation setup` domain, with 3 cultivation predicates.
