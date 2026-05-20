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

Plus three new **top-level domain classes** (children of `METPO:1000000`):

| ID | Label | Lifts CommunityMech class |
| --- | --- | --- |
| `METPO:1007100` | microbial community | `MicrobialCommunity` |
| `METPO:1007101` | microbial community ecological interaction | `EcologicalInteraction` |
| `METPO:1007102` | microbial community evidence item | `EvidenceItem` |

Each `enum-parent` class is a child of one of those three domain classes (e.g.,
`community functional category` sits under `microbial community`;
`evidence item support level` sits under `microbial community evidence item`).

Total class rows: **74** (3 top-level domain + 9 enum-parents + 10 intermediate
groupings + 52 leaves from enums).

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

## Predicate proposals

14 object properties, all in the `METPO:2007NNN` placeholder range. Domains and
ranges reuse either the new top-level classes declared in this proposal or
existing METPO/external IRIs (NCBITaxon, CHEBI, GO).

| Property | Domain | Range | Source CommunityMech slot |
| --- | --- | --- | --- |
| `has source taxon` (`METPO:2007100`) | community interaction | NCBITaxon | `EcologicalInteraction.source_taxon` |
| `has target taxon` (`METPO:2007101`) | community interaction | NCBITaxon | `EcologicalInteraction.target_taxon` |
| `has interaction type` (`METPO:2007102`) | community interaction | interaction-type class | `EcologicalInteraction.interaction_type` |
| `has interaction scope` (`METPO:2007103`) | community interaction | scope class | `EcologicalInteraction.scope` |
| `has exchanged metabolite` (`METPO:2007104`) | community interaction | CHEBI | `EcologicalInteraction.metabolites` |
| `participates in biological process` (`METPO:2007105`) | community interaction | GO | `EcologicalInteraction.biological_processes` |
| `has supporting evidence` (`METPO:2007106`) | community interaction | evidence item | `EcologicalInteraction.evidence` |
| `has functional role` (`METPO:2007107`) | microbe (`METPO:1000525`) | functional role class | `TaxonomicComposition.functional_role` |
| `has abundance level` (`METPO:2007108`) | microbe (`METPO:1000525`) | abundance class | `TaxonomicComposition.abundance_level` |
| `has community category` (`METPO:2007109`) | microbial community | community category class | `MicrobialCommunity.community_category` |
| `has community origin` (`METPO:2007110`) | microbial community | community origin class | `MicrobialCommunity.community_origin` |
| `has ecological state` (`METPO:2007111`) | microbial community | ecological state class | `MicrobialCommunity.ecological_state` |
| `has evidence support level` (`METPO:2007112`) | evidence item | evidence support class | `EvidenceItem.supports` |
| `has evidence source type` (`METPO:2007113`) | evidence item | evidence source class | `EvidenceItem.evidence_source` |

No paired "does not X" predicates are proposed here. The SKILL.md
positive/negative pairing convention is intended for parametric
chemical-tolerance relationships (organism × chemical axis); the predicates in
this proposal are domain-modeling relationships (community ↔ category,
interaction ↔ taxa, evidence ↔ reference) for which a negative form is not
semantically meaningful.

## ID space and subset

- **Classes**: `METPO:1007100`–`METPO:1007220` (placeholder, within the
  KG-Microbe-reserved 1007xxx range per the SKILL.md placeholder policy)
- **Properties**: `METPO:2007100`–`METPO:2007113` (placeholder)
- **Subset tag** on every row: `metpo_communitymech_2026_05`
- **Definition source** on every leaf row: `CommunityMech:communitymech.yaml#<enum-name>.<value>`
  for direct enum lifts; `TODO:add_citation` for the 10 intermediate grouping
  parents (which are introduced in this proposal, not lifted from the schema).
- **Priority**: `HIGH` on all rows that come directly from CommunityMech enums;
  `MEDIUM` on `OTHER` catch-all leaves.

## Files

| File | Rows | Notes |
| --- | --- | --- |
| `metpo_proposal_classes_robot.tsv` | 1 column header + 1 ROBOT header + 74 class rows = 76 lines | mirror of `kg-microbe/mappings/metpo_proposal_classes_robot.tsv` schema |
| `metpo_proposal_properties_robot.tsv` | 1 column header + 1 ROBOT header + 14 property rows = 16 lines | mirror of `kg-microbe/mappings/metpo_proposal_properties_robot.tsv` schema |
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
