# METPO ROBOT Template Proposal — CommunityMech Lift (v1, 2026-05)

## Context

The [CommunityMech](https://github.com/CultureBotAI/CommunityMech) LinkML schema
(`src/communitymech/schema/communitymech.yaml`) defines 13 enums that classify
microbial community members, their interactions, and the evidence supporting
claims about them. The METPO proposal pipeline at
[kg-microbe/mappings/](https://github.com/Knowledge-Graph-Hub/kg-microbe/tree/main/mappings)
(with conventions documented in
[kg-microbe/.claude/skills/metpo-proposal/SKILL.md](https://github.com/Knowledge-Graph-Hub/kg-microbe/blob/main/.claude/skills/metpo-proposal/SKILL.md))
currently covers phenotypic traits, tolerance ranges,
and enzyme assays — but has **zero** coverage of community-level roles,
interaction types, and evidence framing. This proposal closes that gap by
lifting 9 community-shaped enums into METPO classes (with grouping parents to
give them a hierarchy) and proposing 14 object properties that connect them.

After upstream sign-off and ID minting, KGs in the KG-Microbe ecosystem will
be able to express CommunityMech assertions as METPO triples, so reasoners
that already work over phenotypic METPO triples can reason over community-
level assertions the same way.

## Scope

| CommunityMech enum | METPO parent | # leaf classes | # intermediate parents | Schema lines |
| --- | --- | ---: | ---: | --- |
| `FunctionalRoleEnum` | `microbial community member functional role` (`METPO:1007103`) | 5 | 2 (primary / secondary trophic role) | 214–226 |
| `InteractionTypeEnum` | `ecological interaction type` (`METPO:1007120`) | 10 (incl. `STRAIN_COMPETITION` ⊂ `COMPETITION`) | 3 (positive / negative / partitioning) | 157–189 |
| `EvidenceItemSupportEnum` | `evidence item support level` (`METPO:1007150`) | 5 | 0 (flat) | 33–69 |
| `EvidenceSourceEnum` | `evidence item source` (`METPO:1007160`) | 5 | 0 (flat) | 71–83 |
| `InteractionScopeEnum` | `interaction scope` (`METPO:1007140`) | 2 | 0 (flat) | 191–200 |
| `AbundanceEnum` | `taxon abundance level` (`METPO:1007170`) | 4 | 0 (flat) | 202–212 |
| `CommunityCategoryEnum` | `community functional category` (`METPO:1007200`) | 15 | 5 (thematic groupings) | 123–155 |
| `CommunityOriginEnum` | `community origin type` (`METPO:1007190`) | 3 | 0 (flat) | 97–105 |
| `EcologicalStateEnum` | `community ecological state` (`METPO:1007180`) | 4 | 0 (flat) | 85–95 |
| `AtmosphereEnum` (v1.1) | `atmosphere requirement` (`METPO:1007301`) | 6 | 0 (flat) | 228–243 |
| `MediaRelationshipEnum` (v1.1) | `growth media relationship type` (`METPO:1007310`) | 5 | 0 (flat) | 107–121 |
| `MetalElementEnum` (v1.2, **CHEBI-reuse**) | `community-relevant metal element` (`METPO:1008001`) | 0 in METPO (per-element leaves are CHEBI IRIs) | 0 (flat) | 348–402 |
| `RareEarthElementEnum` (v1.2, **CHEBI-reuse**) | `community-relevant rare earth element` (`METPO:1008002`) | 0 in METPO (per-REE leaves are CHEBI IRIs) | 0 (flat) | 403–453 |
| `MetalRelevanceEnum` (v1.2) | `community metal relevance level` (`METPO:1008003`) | 4 | 0 (flat) | 455–463 |

Plus five new **top-level domain classes** (children of `METPO:1000000`):

| ID | Label | Lifts CommunityMech class | Added in |
| --- | --- | --- | --- |
| `METPO:1007100` | microbial community | `MicrobialCommunity` | v1 |
| `METPO:1007101` | microbial community ecological interaction | `EcologicalInteraction` | v1 |
| `METPO:1007102` | microbial community evidence item | `EvidenceItem` | v1 |
| `METPO:1007300` | community-relevant growth medium | `GrowthMedia` and `RelatedMedia` | v1.1 |
| `METPO:1008000` | community-relevant metal context | `MicrobialCommunity.metals_present` / `.rare_earth_elements_present` / `.metal_relevance` framing | v1.2 |

Each `enum-parent` class is a child of one of those five domain classes (e.g.,
`community functional category` sits under `microbial community`;
`evidence item support level` sits under `microbial community evidence item`;
`atmosphere requirement` sits under `community-relevant growth medium`;
`community-relevant metal element` sits under `community-relevant metal context`).

Total class rows: **96** (5 top-level domain + 14 enum-parents + 10 intermediate
groupings + 67 leaves from enums; the v1.2 extension added 1 top-level +
3 enum-parents + 4 leaves on top of v1.1's totals).

## Hierarchy decisions

### `InteractionTypeEnum` — three valence groupings

The CommunityMech enum already distinguishes positive- vs negative-outcome
interactions in its `+/+, +/0, -/-, +/-` annotations and has explicit `comments:`
fields placing `NICHE_PARTITIONING` outside the positive/negative axis. Lifting
these into METPO with three intermediate parents (positive, negative,
partitioning) makes the implicit valence axis queryable and lets reasoners
collapse the 10 leaves to 3 groups when needed.

`STRAIN_COMPETITION` is a child of `COMPETITION` (not a sibling) per the
schema's own comment: *"Distinct from interspecific COMPETITION, this captures
strain-level competitive dynamics within a single species."* The class
hierarchy preserves this `is_a`.

### `FunctionalRoleEnum` — two trophic tiers

The five roles fall naturally into two tiers based on how they enter the
trophic network: `PRIMARY_PRODUCER` and `PRIMARY_DEGRADER` introduce carbon
or fixed substrate; `SECONDARY_FERMENTER`, `SYNTROPHIC_PARTNER`, and
`CROSS_FEEDER` all depend on metabolites that primary members produce. We
encode this as `primary trophic role` (`METPO:1007104`) and `secondary trophic
role` (`METPO:1007105`), each a child of the enum-parent.

### `CommunityCategoryEnum` — five thematic groupings

The 15 categories cluster into five thematic groups visible from the schema
descriptions:

| Group | Members |
| --- | --- |
| metal and waste processing | `BIOMINING`, `AMD`, `METAL_REDUCTION` |
| host-associated | `PHYTOPLANKTON`, `RHIZOSPHERE`, `ORAL` |
| engineered metabolic | `LIGNOCELLULOSE`, `METHANOGENESIS`, `DIET` |
| remediation and synthesis | `BIOREMEDIATION`, `CARBON_SEQUESTRATION`, `BIOTECHNOLOGY` |
| environmental-setting | `EXTREME_ENVIRONMENT`, `SYNTROPHY` |

`OTHER` stays flat under `community functional category`.

### `EvidenceItemSupportEnum`, `EvidenceSourceEnum`, and the small enums

These have no obvious internal hierarchy in the schema — every value is a
distinct mutually-exclusive state — so we keep them flat under their
enum-parent.

### `MetalElementEnum` and `RareEarthElementEnum` — CHEBI-reuse, no per-element leaves (v1.2)

Every permissible value in these two enums carries a `meaning: CHEBI:xxxxx`
annotation in the schema (e.g., `IRON: meaning: CHEBI:29033` iron(2+) cation;
`LANTHANUM: meaning: CHEBI:32359` lanthanum(3+) cation). Per the upstream
kg-microbe SKILL.md rule *"if the lifted concept already exists in METPO under
a different label, use the existing IRI; record the alias upstream"*, this
proposal deliberately mints **only the grouping-parent METPO classes**
(`community-relevant metal element` / `community-relevant rare earth
element`) and leaves the per-element values as CHEBI IRIs. The per-element
edges flow into `kg-microbe/mappings/metpo_existing_aliases.tsv` when the
cohort is copied upstream.

Predicate ranges for `has metal element present` and `has rare earth element
present` are set to the broad `CHEBI:24431` (chemical entity) because the
schema mixes atom-form (e.g., `URANIUM` → `CHEBI:27214` uranium atom,
`GOLD` → `CHEBI:29287` gold atom, `CHROMIUM` → `CHEBI:28073`,
`TITANIUM` → `CHEBI:33341`, `PALLADIUM` → `CHEBI:33373`) with cation-form
values; narrower CHEBI parents like `CHEBI:33521` (metal cation) or
`CHEBI:33709` (metal atom) would reject some valid existing data.

In contrast, `MetalRelevanceEnum` has four qualitative severity values
(PRIMARY / SIGNIFICANT / INCIDENTAL / NOT_APPLICABLE) with **no CHEBI
equivalent**, so v1.2 mints fresh METPO leaves for those four values under
`community metal relevance level` (`METPO:1008003`).

## Predicate proposals

19 object properties across the `METPO:2007NNN` (v1, v1.1) and `METPO:2008NNN`
(v1.2) placeholder ranges. Domains and ranges reuse either the new top-level
classes declared in this proposal or existing METPO/external IRIs (NCBITaxon,
CHEBI, GO).

| Property | Domain | Range | Source CommunityMech slot | Cohort |
| --- | --- | --- | --- | --- |
| `has source taxon` (`METPO:2007100`) | community interaction | NCBITaxon | `EcologicalInteraction.source_taxon` | v1 |
| `has target taxon` (`METPO:2007101`) | community interaction | NCBITaxon | `EcologicalInteraction.target_taxon` | v1 |
| `has interaction type` (`METPO:2007102`) | community interaction | interaction-type class | `EcologicalInteraction.interaction_type` | v1 |
| `has interaction scope` (`METPO:2007103`) | community interaction | scope class | `EcologicalInteraction.scope` | v1 |
| `has exchanged metabolite` (`METPO:2007104`) | community interaction | CHEBI | `EcologicalInteraction.metabolites` | v1 |
| `participates in biological process` (`METPO:2007105`) | community interaction | GO | `EcologicalInteraction.biological_processes` | v1 |
| `has supporting evidence` (`METPO:2007106`) | community interaction | evidence item | `EcologicalInteraction.evidence` | v1 |
| `has functional role` (`METPO:2007107`) | microbe (`METPO:1000525`) | functional role class | `TaxonomicComposition.functional_role` | v1 |
| `has abundance level` (`METPO:2007108`) | microbe (`METPO:1000525`) | abundance class | `TaxonomicComposition.abundance_level` | v1 |
| `has community category` (`METPO:2007109`) | microbial community | community category class | `MicrobialCommunity.community_category` | v1 |
| `has community origin` (`METPO:2007110`) | microbial community | community origin class | `MicrobialCommunity.community_origin` | v1 |
| `has ecological state` (`METPO:2007111`) | microbial community | ecological state class | `MicrobialCommunity.ecological_state` | v1 |
| `has evidence support level` (`METPO:2007112`) | evidence item | evidence support class | `EvidenceItem.supports` | v1 |
| `has evidence source type` (`METPO:2007113`) | evidence item | evidence source class | `EvidenceItem.evidence_source` | v1 |
| `has atmosphere requirement` (`METPO:2007200`) | community-relevant growth medium | atmosphere-requirement class | `GrowthMedia.atmosphere` | v1.1 |
| `has growth media relationship` (`METPO:2007201`) | community-relevant growth medium | media-relationship class | `RelatedMedia.relationship_type` | v1.1 |
| `has metal element present` (`METPO:2008000`) | microbial community | CHEBI:24431 (chemical entity) | `MicrobialCommunity.metals_present` | v1.2 |
| `has rare earth element present` (`METPO:2008001`) | microbial community | CHEBI:24431 (chemical entity) | `MicrobialCommunity.rare_earth_elements_present` | v1.2 |
| `has metal relevance` (`METPO:2008002`) | microbial community | metal-relevance-level class | `MicrobialCommunity.metal_relevance` | v1.2 |

No paired "does not X" predicates are proposed here. The SKILL.md
positive/negative pairing convention is intended for parametric
chemical-tolerance relationships (organism × chemical axis); the predicates in
this proposal are domain-modeling relationships (community ↔ category,
interaction ↔ taxa, evidence ↔ reference) for which a negative form is not
semantically meaningful.

## ID space and subset

- **Classes**:
  - v1: `METPO:1007100`–`METPO:1007220` (placeholder, within the KG-Microbe-reserved 1007xxx range per the SKILL.md placeholder policy)
  - v1.1 extension: `METPO:1007300`–`METPO:1007315` (AtmosphereEnum + MediaRelationshipEnum + new top-level domain class `community-relevant growth medium` at `METPO:1007300`)
  - v1.2 extension: `METPO:1008000`–`METPO:1008013` (MetalElementEnum + RareEarthElementEnum grouping parents + MetalRelevanceEnum + new top-level domain class `community-relevant metal context` at `METPO:1008000`). The v1.2 block starts at `1008000` rather than `1007320+` to visually separate the **CHEBI-reuse** metal classes from the all-leaves-minted v1/v1.1 enum classes.
- **Properties**:
  - v1: `METPO:2007100`–`METPO:2007113`
  - v1.1 extension: `METPO:2007200`–`METPO:2007201`
  - v1.2 extension: `METPO:2008000`–`METPO:2008002`
- **Subset tag** on every row: `metpo_communitymech_2026_05`
- **Definition source** on every leaf row: `CommunityMech:communitymech.yaml#<enum-name>.<value>`
  for direct enum lifts; `CommunityMech:proposals/metpo_communitymech_v1/proposal.md#hierarchy-decisions`
  for the 10 intermediate grouping parents introduced in this proposal.
- **Priority**: `HIGH` on all rows that come directly from CommunityMech enums;
  `MEDIUM` on `OTHER` catch-all leaves, `REFERENCED_IN_STUDY` medium-relationship value, and `INCIDENTAL`/`NOT_APPLICABLE` metal-relevance leaves.

## Files

| File | Rows | Notes |
| --- | --- | --- |
| `metpo_proposal_classes_robot.tsv` | 1 column header + 1 ROBOT header + 96 class rows = 98 lines (74 in v1 + 14 in v1.1 + 8 in v1.2) | mirror of `kg-microbe/mappings/metpo_proposal_classes_robot.tsv` schema |
| `metpo_proposal_properties_robot.tsv` | 1 column header + 1 ROBOT header + 19 property rows = 21 lines (14 in v1 + 2 in v1.1 + 3 in v1.2) | mirror of `kg-microbe/mappings/metpo_proposal_properties_robot.tsv` schema |
| `proposal.md` | (this file) | narrative for reviewer |

## Verification

Run ROBOT on each TSV against the existing METPO ontology to catch parse,
reasoning, or merge errors:

```bash
# Parse the two templates standalone
robot template \
    --template metpo_proposal_classes_robot.tsv \
    --output classes.owl
robot template \
    --template metpo_proposal_properties_robot.tsv \
    --output properties.owl

# Merge with the current METPO core and reason with ELK; assert no unsat
robot merge \
    --input metpo-edit.owl \
    --input classes.owl \
    --input properties.owl \
    --output merged.owl
robot reason --reasoner ELK \
    --input merged.owl \
    --output reasoned.owl
```

Manual cross-checks:

1. Every CommunityMech enum permissible value
   (e.g., `FunctionalRoleEnum.PRIMARY_DEGRADER`) maps to a leaf class row.
2. Every CommunityMech slot exercised by the community YAML corpus
   (e.g., `EcologicalInteraction.source_taxon`) maps to a property row.
3. Round-trip on three community YAMLs that span the scope:
   `kb/communities/Alaska_Tundra_Permafrost_Iron_Redox_Community.yaml`
   (Fe-redox cycling, metal-reduction category),
   `kb/communities/BioModels_MODEL2204300001_Kefir_Community_Model.yaml`
   (engineered metabolic, with external_resources evidence), and
   `kb/communities/Propanotrophic_Chlorinated_Ethene_Cometabolism_Enrichment.yaml`
   (bioremediation category, COMPETITION + CROSS_FEEDING interactions, PARTIAL
   and SUPPORT evidence levels). Confirm every enum value cited in these YAMLs
   resolves to a class in this proposal.

## Upstream path

When this proposal is approved here in CommunityMech:

1. Copy `metpo_proposal_classes_robot.tsv` and `metpo_proposal_properties_robot.tsv`
   into `kg-microbe/mappings/` (alongside the existing 2026_04 cohort files).
2. Run the SKILL.md validation checklist on the merged proposal.
3. METPO maintainers mint real IDs to replace the `METPO:1007xxx` /
   `METPO:2007xxx` placeholders.
4. The CommunityMech `datamodel/communitymech.py` regeneration can later be
   extended to emit METPO IRIs for the lifted enum values, enabling round-trip
   KGX export to KG-Microbe-compatible TSVs.

## Change log

- **v1, 2026-05**: Initial proposal. 74 class rows (9 enums, 3 top-level
  domain classes, 10 intermediate grouping parents) + 14 property rows.
- **v1.0.1, 2026-05 (revised)**: Addressed Copilot review on PR #74.
  Replaced kg-microbe relative link with absolute GitHub URL; added
  `kb/communities/` prefixes to verification example YAMLs; narrowed
  `has supporting evidence` (METPO:2007106) definition to match its
  domain METPO:1007101; replaced 10 `TODO:add_citation` placeholders
  with the proposal-narrative anchor URL; replaced overbroad
  `ecological interaction` synonym on METPO:1007101 with two precise
  variants.
- **v1.1, 2026-05**: Path B extension. Added `AtmosphereEnum`
  (`METPO:1007301`–`METPO:1007307`, 1 enum-parent + 6 leaves) and
  `MediaRelationshipEnum` (`METPO:1007310`–`METPO:1007315`, 1
  enum-parent + 5 leaves), under a shared new top-level domain class
  `community-relevant growth medium` (`METPO:1007300`). Added 2 new
  predicates: `has atmosphere requirement` (`METPO:2007200`) and
  `has growth media relationship` (`METPO:2007201`). New ID block
  starts at `1007300` / `2007200` per the skill's Path B rule
  (at least 10 above the v1 high-water marks of `1007220` /
  `2007113`). Total now: 88 class rows + 16 property rows. Same
  subset tag.
- **v1.2, 2026-05**: Path B extension absorbing what was previously
  a separate `metpo_communitymech_metals_v1` cohort. Added
  `MetalElementEnum` and `RareEarthElementEnum` enum-parents
  (`METPO:1008001`, `METPO:1008002`) without minting per-element
  METPO leaves — the per-element values reuse existing CHEBI IRIs
  (e.g., `IRON` → `CHEBI:29033`) recorded upstream in
  `metpo_existing_aliases.tsv`. Added `MetalRelevanceEnum`
  (`METPO:1008003` + 4 leaves `METPO:1008010`–`METPO:1008013`)
  which is minted in full because the four relevance levels have
  no CHEBI equivalent. Added a new top-level domain class
  `community-relevant metal context` (`METPO:1008000`, child of
  `METPO:1000000`). Added 3 predicates `METPO:2008000`–`METPO:2008002`
  (`has metal element present` / `has rare earth element present` /
  `has metal relevance`). The previously separate
  `metpo_communitymech_metals_v1/` proposal directory is removed in
  this commit because everything in it now lives here under the same
  subset tag. ID block starts at `1008000` / `2008000` to visually
  separate the **CHEBI-reuse** metal classes from the all-leaves-minted
  v1/v1.1 enum classes. Total now: 96 class rows + 19 property rows.
  Same subset tag.
