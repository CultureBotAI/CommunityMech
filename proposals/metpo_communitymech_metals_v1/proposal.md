# METPO ROBOT Template Proposal — CommunityMech Metals Cohort (v1, 2026-05)

## Context

CommunityMech's metal-related schema slots
(`MicrobialCommunity.metals_present`, `.rare_earth_elements_present`,
`.metal_relevance`) are populated across the biomining, AMD,
metal-reduction, and metal-tailings community YAMLs in
`kb/communities/`. Lifting these into METPO lets KG-Microbe consumers
filter communities by metal/REE membership and by how central metal
cycling is to community function.

A scoping choice deserves emphasis at the top: **the per-element enum
values in `MetalElementEnum` and `RareEarthElementEnum` already carry
`meaning: CHEBI:xxxxx` cross-references in the schema, so this proposal
does NOT mint per-element METPO classes**. Doing so would duplicate
CHEBI's `Iron(2+) cation` (CHEBI:29033) etc. as parallel
`METPO:iron`-style identifiers, contradicting the upstream kg-microbe
SKILL.md rule that "if the lifted concept already exists in METPO
under a different label, use the existing IRI; record the alias in
mappings/metpo_existing_aliases.tsv". This proposal instead lifts
only:

- The two **grouping parents** (`community-relevant metal element`,
  `community-relevant rare earth element`) that anchor the METPO side
  of the alias mapping.
- The 4 **MetalRelevanceEnum** leaves (PRIMARY / SIGNIFICANT /
  INCIDENTAL / NOT_APPLICABLE), which have no CHEBI equivalent — they
  are qualitative severity categories, not chemical entities.
- Three **predicates** wiring all of the above to
  `MicrobialCommunity`.

The per-element CHEBI IRIs flow upstream into
`kg-microbe/mappings/metpo_existing_aliases.tsv` when this proposal is
copied to the kg-microbe pipeline.

## Scope

| CommunityMech enum / slot | METPO parent | Leaves |
| --- | --- | --- |
| `MetalElementEnum` (17 values) | `community-relevant metal element` (`METPO:1008001`) | none in METPO — reuse CHEBI IRIs |
| `RareEarthElementEnum` (16 values) | `community-relevant rare earth element` (`METPO:1008002`) | none in METPO — reuse CHEBI IRIs |
| `MetalRelevanceEnum` (4 values) | `community metal relevance level` (`METPO:1008003`) | 4 leaves (`METPO:1008010`–`METPO:1008013`) |

Plus one new top-level domain class:

| ID | Label | Lifts |
| --- | --- | --- |
| `METPO:1008000` | community-relevant metal context | the metal-context framing of `MicrobialCommunity` (parent `METPO:1007100`) |

Total class rows: **8** (1 top-level + 3 enum-parents + 4
MetalRelevance leaves).

## Hierarchy decisions

### Why no per-element METPO classes

The kg-microbe upstream SKILL.md states:

> If the lifted concept already exists in METPO under a different
> label, use the existing IRI; record the alias in
> `mappings/metpo_existing_aliases.tsv`.

Each `MetalElementEnum` value (e.g., `IRON: meaning: CHEBI:29033`)
already exists in CHEBI as a chemical entity. Minting a new METPO IRI
per metal would:

1. Force downstream consumers to choose between two competing IRIs
   for the same chemical.
2. Multiply maintenance burden when CHEBI updates labels or adds
   synonyms.
3. Leak the schema-internal enum design into the public ontology
   without semantic justification (an enum is a serialization
   convenience, not a new ontological category).

The same reasoning applies to `RareEarthElementEnum`. Both
grouping-parent METPO classes (`METPO:1008001`, `METPO:1008002`) are
included so the alias-mapping table has a METPO-side anchor; the
actual per-element edges are CHEBI IRIs.

### Why mint METPO leaves for MetalRelevanceEnum

`MetalRelevanceEnum`'s four values (PRIMARY / SIGNIFICANT /
INCIDENTAL / NOT_APPLICABLE) are **qualitative severity categories
specific to CommunityMech**. They do not exist in CHEBI, PATO, GO,
or other ontologies we cross-reference, and they describe the
community's relationship to metal cycling rather than a chemical
entity. Minting fresh METPO leaves under
`community metal relevance level` is the right call.

### Flat hierarchy under each enum-parent

None of the three enums has internal `is_a` structure in the schema
(no comments indicating one value is a specialization of another).
The 4 MetalRelevance leaves are mutually exclusive severity bins.
Kept flat.

## Predicate proposals

3 object properties, all in the `METPO:2008NNN` placeholder range.
All have `MicrobialCommunity` (`METPO:1007100`) as domain.

| Property | Range | Source slot |
| --- | --- | --- |
| `has metal element present` (`METPO:2008000`) | `CHEBI:24431` (chemical entity) | `MicrobialCommunity.metals_present` |
| `has rare earth element present` (`METPO:2008001`) | `CHEBI:24431` (chemical entity) | `MicrobialCommunity.rare_earth_elements_present` |
| `has metal relevance` (`METPO:2008002`) | `METPO:1008003` (metal relevance level) | `MicrobialCommunity.metal_relevance` |

The first two predicates use the broad `CHEBI:24431` (chemical
entity) as range because the schema-side enums mix atom-form and
cation-form CHEBI values: `MetalElementEnum` includes atom-form
entries (`URANIUM` → `CHEBI:27214` uranium atom, `GOLD` → `CHEBI:29287`
gold atom, `CHROMIUM` → `CHEBI:28073`, `TITANIUM` → `CHEBI:33341`,
`PALLADIUM` → `CHEBI:33373`) alongside cation-form entries
(`IRON` → `CHEBI:29033` iron(2+) cation, etc.); narrower CHEBI parents
like `CHEBI:33521` (metal cation) or `CHEBI:33709` (metal atom) would
reject some valid existing data. The intent is to keep per-element
edges as CHEBI IRIs (no METPO per-element leaves minted); the range
type-hint is deliberately loose to accommodate the heterogeneous
schema values.

## ID space and subset

- **Classes**: `METPO:1008000`–`METPO:1008013` (placeholder, in a
  fresh `1008NNN` block to keep the metals cohort cleanly separated
  from the `metpo_communitymech_v1` cohort which uses `1007NNN`)
- **Properties**: `METPO:2008000`–`METPO:2008002` (placeholder)
- **Subset tag** on every row: `metpo_communitymech_metals_2026_05`
- **Definition source**: `CommunityMech:communitymech.yaml#<EnumName>.<VALUE>`
  for enum lifts; `CommunityMech:communitymech.yaml#MicrobialCommunity.<slot>`
  for the top-level domain class.
- **Priority**: `HIGH` on all enum-parent and PRIMARY/SIGNIFICANT
  rows; `MEDIUM` on `INCIDENTAL` and `NOT_APPLICABLE` leaves (these
  are catch-all categories).

## Files

| File | Rows | Notes |
| --- | --- | --- |
| `metpo_proposal_classes_robot.tsv` | 1 column header + 1 ROBOT header + 8 class rows = 10 lines | mirror of `kg-microbe/mappings/metpo_proposal_classes_robot.tsv` schema |
| `metpo_proposal_properties_robot.tsv` | 1 column header + 1 ROBOT header + 3 property rows = 5 lines | mirror of `kg-microbe/mappings/metpo_proposal_properties_robot.tsv` schema |
| `proposal.md` | (this file) | narrative for reviewer |

## Verification

```bash
# Column-count sanity
awk -F'\t' 'NF != 11 {print NR": "NF" cols"}' proposals/metpo_communitymech_metals_v1/metpo_proposal_classes_robot.tsv
awk -F'\t' 'NF != 12 {print NR": "NF" cols"}' proposals/metpo_communitymech_metals_v1/metpo_proposal_properties_robot.tsv

# Parse with ROBOT if available
robot template --template proposals/metpo_communitymech_metals_v1/metpo_proposal_classes_robot.tsv --output /tmp/metals_classes.owl
robot template --template proposals/metpo_communitymech_metals_v1/metpo_proposal_properties_robot.tsv --output /tmp/metals_properties.owl
```

Round-trip check: pick two metal-relevant community YAMLs that
exercise the enums:
- `kb/communities/Alaska_Tundra_Permafrost_Iron_Redox_Community.yaml`
  (Fe-redox, `metal_relevance: SIGNIFICANT`, single-metal IRON)
- `kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml`
  (rare-earth elements + `metal_relevance: PRIMARY`)

Confirm that every `MetalRelevanceEnum` value cited in these YAMLs
maps to a leaf class in this proposal, and that each
`MetalElementEnum` / `RareEarthElementEnum` value resolves to its
CHEBI IRI (which sits under the METPO grouping parent via the
alias-table mapping).

## Upstream path

When this cohort is approved here:

1. Copy both TSVs to `kg-microbe/mappings/`.
2. Generate an `metpo_existing_aliases.tsv` entry for every
   `MetalElementEnum.<X>` and `RareEarthElementEnum.<X>` value,
   mapping the schema-side enum name to the existing CHEBI IRI from
   the schema's `meaning:` annotation. Format follows the existing
   `kg-microbe/mappings/metpo_existing_aliases.tsv` rows.
3. METPO maintainers mint real IDs to replace the `METPO:1008NNN`
   placeholders for the 8 minted classes; CHEBI IRIs need no minting.
4. The CommunityMech `datamodel/communitymech.py` regeneration can
   later emit either the METPO IRI (for grouping queries) or the
   CHEBI IRI (for chemical-entity queries) when serializing
   `metals_present` and `rare_earth_elements_present` values.

## Change log

- **v1, 2026-05**: Initial proposal for the metals cohort. 8 class
  rows (1 top-level + 3 enum-parents + 4 MetalRelevance leaves) +
  3 property rows. Per-element CHEBI IRIs deferred to
  `metpo_existing_aliases.tsv` upstream rather than minting fresh
  METPO leaves.
