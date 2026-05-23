# Cross-Repository Environmental Linking

## Overview

CommunityMech supports two levels of cross-repository linking:

1. **Cultivation linking** (existing) -- `growth_media` connects communities to media actually used for cultivation, with `culturemech_id` and `media_ingredient_mech_id` on components.

2. **Environmental linking** (new) -- `related_media` and `related_ingredients` connect communities to CultureMech media and MediaIngredientMech ingredients that are *environmentally relevant*, even if not directly used for cultivation.

This document covers the new environmental linking system.

## When to Use Which Field

| Field | Class | Purpose | Example |
|-------|-------|---------|---------|
| `growth_media` | GrowthMedia | Media **actually used** for cultivation | "We grew the community in R2A medium" |
| `related_media` | RelatedMedia | Media **environmentally relevant** to the community | "This peatland medium mimics the community's habitat" |
| `growth_media.composition` | GrowthMediaComponent | Ingredients **in** a cultivation medium | "R2A contains 0.5 g/L yeast extract" |
| `related_ingredients` | RelatedIngredient | Ingredients **relevant to the environment** | "Humic acid is the dominant organic matter in this peatland" |

A medium can appear in both `growth_media` and `related_media`. The two fields serve different query patterns: cultivation history vs. environment-based discovery.

## Schema Classes

### MediaRelationshipEnum

Describes how a medium relates to the community:

| Value | Use When |
|-------|----------|
| `CULTIVATION_MEDIUM` | Medium was actually used to cultivate community members |
| `ISOLATION_MEDIUM` | Medium was used for initial isolation from the environment |
| `ENVIRONMENT_ANALOG` | Medium mimics the community's natural environment |
| `REFERENCED_IN_STUDY` | Medium was referenced in a study of this community |
| `SELECTIVE_ENRICHMENT` | Medium selectively enriches for specific functional groups |

### RelatedMedia

Links a community to a CultureMech medium through environmental relevance.

| Attribute | Required | Description |
|-----------|----------|-------------|
| `preferred_term` | Yes | Human-readable media name |
| `culturemech_id` | No | CultureMech ID (format: `CultureMech:NNNNNN`) |
| `relationship_type` | No | MediaRelationshipEnum value |
| `shared_environment_term` | No | ENVO term linking community environment to medium |
| `relevance_notes` | No | Why this medium is relevant |
| `evidence` | No | Evidence items (multivalued) |

### RelatedIngredient

Links a community to a MediaIngredientMech ingredient through environmental or metabolic relevance.

| Attribute | Required | Description |
|-----------|----------|-------------|
| `preferred_term` | Yes | Human-readable ingredient name |
| `mediaingredientmech_id` | No | MediaIngredientMech ID (format: `MediaIngredientMech:NNNNNN`) |
| `chebi_term` | No | CHEBI ontology term for the compound |
| `relevance` | No | Why this ingredient is relevant |
| `evidence` | No | Evidence items (multivalued) |

## Cross-Repository ID Formats

| Repository | Pattern | Example |
|------------|---------|---------|
| CommunityMech | `CommunityMech:NNNNNN` | `CommunityMech:000024` |
| CultureMech | `CultureMech:NNNNNN` | `CultureMech:010001` |
| MediaIngredientMech | `MediaIngredientMech:NNNNNN` | `MediaIngredientMech:000523` |

IDs are validated by regex pattern. Cross-repository existence checks (verifying the ID exists in the partner repo) are optional and recommended as a periodic bulk validation step.

## Examples

### Minimal: Single Related Medium

```yaml
id: CommunityMech:000050
name: Hot Spring Thermophile Community

related_media:
  - preferred_term: Thermus Medium
    culturemech_id: CultureMech:003001
    relationship_type: ENVIRONMENT_ANALOG
```

### Full: SPRUCE Peatland Community

```yaml
id: CommunityMech:000024
name: SPRUCE Peatland Warming Microbial Community
ecological_state: STABLE
community_origin: NATURAL
community_category: METHANOGENESIS

environment_term:
  preferred_term: peatland
  term:
    id: ENVO:00000044
    label: peatland

# Existing: media actually used for cultivation
growth_media:
  - name: Anaerobic Basal Medium
    culturemech_id: CultureMech:005023
    ph: "4.5"
    temperature: "25"
    atmosphere: ANAEROBIC

# New: environmentally relevant media from CultureMech
related_media:
  - preferred_term: Acidic Peatland Medium
    culturemech_id: CultureMech:010001
    relationship_type: ENVIRONMENT_ANALOG
    shared_environment_term:
      id: ENVO:00000044
      label: peatland
    relevance_notes: "Medium mimics acidic peatland conditions (pH 3.5-4.5)"
    evidence:
      - reference: PMID:38515239
        supports: SUPPORT
        evidence_source: IN_VIVO
        snippet: "Peat microbial communities characterized from SPRUCE experimental plots"

  - preferred_term: Iron-Reducing Enrichment Medium
    culturemech_id: CultureMech:008012
    relationship_type: SELECTIVE_ENRICHMENT
    relevance_notes: "Selective for iron-reducing bacteria detected in SPRUCE metagenomes"
    evidence:
      - reference: PMID:35481924
        supports: SUPPORT
        evidence_source: COMPUTATIONAL
        snippet: "Geobacter-related MAGs enriched in deep peat with warming treatment"

# New: environmentally relevant ingredients from MediaIngredientMech
related_ingredients:
  - preferred_term: Humic acid
    mediaingredientmech_id: MediaIngredientMech:000523
    chebi_term:
      id: CHEBI:34818
      label: humic acid
    relevance: "Major peat organic matter component and electron acceptor"
    evidence:
      - reference: PMID:38515239
        supports: SUPPORT
        evidence_source: IN_VIVO
        snippet: "Humic substances dominate dissolved organic matter in peat porewater"

  - preferred_term: Ferrous sulfate
    mediaingredientmech_id: MediaIngredientMech:000089
    chebi_term:
      id: CHEBI:75832
      label: iron(2+) sulfate
    relevance: "Iron source for iron-cycling bacteria in deeper peat layers"
```

### All Relationship Types

```yaml
related_media:
  - preferred_term: Vent Medium
    culturemech_id: CultureMech:007001
    relationship_type: CULTIVATION_MEDIUM

  - preferred_term: Sulfide Isolation Agar
    culturemech_id: CultureMech:007015
    relationship_type: ISOLATION_MEDIUM

  - preferred_term: Synthetic Hydrothermal Fluid
    culturemech_id: CultureMech:007020
    relationship_type: ENVIRONMENT_ANALOG
    shared_environment_term:
      id: ENVO:01000030
      label: hydrothermal vent

  - preferred_term: Marine Broth 2216
    culturemech_id: CultureMech:000042
    relationship_type: REFERENCED_IN_STUDY

  - preferred_term: Chitin Enrichment Medium
    culturemech_id: CultureMech:007030
    relationship_type: SELECTIVE_ENRICHMENT
```

## Cross-Repository Query Patterns

### SPARQL: Find Media for Peatland Communities

```sparql
PREFIX cm: <https://w3id.org/communitymech/>

SELECT ?community_name ?media_name ?culturemech_id ?relationship
WHERE {
  ?community cm:environment_term/cm:term/cm:id "ENVO:00000044" ;
             cm:name ?community_name ;
             cm:related_media ?rm .
  ?rm cm:preferred_term ?media_name ;
      cm:culturemech_id ?culturemech_id .
  OPTIONAL { ?rm cm:relationship_type ?relationship }
}
```

### SPARQL: Find Ingredients for an Environment

```sparql
PREFIX cm: <https://w3id.org/communitymech/>

SELECT ?community_name ?ingredient ?mim_id ?relevance
WHERE {
  ?community cm:environment_term/cm:term/cm:id "ENVO:00000044" ;
             cm:name ?community_name ;
             cm:related_ingredients ?ri .
  ?ri cm:preferred_term ?ingredient ;
      cm:mediaingredientmech_id ?mim_id .
  OPTIONAL { ?ri cm:relevance ?relevance }
}
```

### SPARQL: Full Cross-Repo Join via Shared ENVO Terms

```sparql
PREFIX cm: <https://w3id.org/communitymech/>
PREFIX cult: <https://w3id.org/culturebot-ai/culturemech/>
PREFIX mim: <https://w3id.org/culturebot-ai/mediaingredientmech/>

SELECT ?community_name ?env_label ?media_name ?ingredient_name
WHERE {
  ?community cm:name ?community_name ;
             cm:environment_term/cm:term/cm:id ?envo_id ;
             cm:environment_term/cm:term/cm:label ?env_label .

  ?media cult:source_environment/cult:term/cult:id ?envo_id ;
         cult:name ?media_name .

  ?ingredient mim:environmental_context/mim:term/mim:id ?envo_id ;
              mim:name ?ingredient_name .
}
```

### SPARQL: Reverse Lookup -- Communities for a CultureMech Medium

```sparql
PREFIX cm: <https://w3id.org/communitymech/>

SELECT ?community_name ?environment ?relationship
WHERE {
  ?community cm:related_media ?rm ;
             cm:name ?community_name ;
             cm:environment_term/cm:preferred_term ?environment .
  ?rm cm:culturemech_id "CultureMech:010001" ;
      cm:relationship_type ?relationship .
}
```

## Python Dataclass Usage

```python
from communitymech.datamodel.communitymech import (
    MicrobialCommunity,
    RelatedMedia,
    RelatedIngredient,
    MediaRelationshipEnum,
    Term,
)

# Create a related medium
rm = RelatedMedia(
    preferred_term="Acidic Peatland Medium",
    culturemech_id="CultureMech:010001",
    relationship_type=MediaRelationshipEnum.ENVIRONMENT_ANALOG,
    shared_environment_term=Term(id="ENVO:00000044", label="peatland"),
    relevance_notes="Mimics acidic peatland conditions",
)

# Create a related ingredient
ri = RelatedIngredient(
    preferred_term="Humic acid",
    mediaingredientmech_id="MediaIngredientMech:000523",
    chebi_term=Term(id="CHEBI:34818", label="humic acid"),
    relevance="Major peat organic matter component",
)

# Add to a community
community = MicrobialCommunity(
    id="CommunityMech:000024",
    name="SPRUCE Peatland Community",
    related_media=[rm],
    related_ingredients=[ri],
)
```

## Backward Compatibility

All new fields are optional:
- Communities without `related_media` or `related_ingredients` remain valid
- Existing `growth_media` and its `composition` are unchanged
- No modifications to any existing classes or enums
- Generated Python dataclasses default new fields to empty lists

## Validation

Run the cross-repo linking tests:

```bash
cd CommunityMech
PYTHONPATH=src python -m pytest tests/test_cross_repo_linking.py -v
```

Test data files are in `tests/data/test_cross_repo_linking/`:
- `spruce_with_links.yaml` -- Full example with all features
- `community_no_links.yaml` -- Backward compatibility
- `community_all_relationship_types.yaml` -- All 5 enum values

## See Also

- [Growth Media Linking](media_linking.md) -- Existing cultivation-based linking
- Schema: `src/communitymech/schema/communitymech.yaml`
- Dataclasses: `src/communitymech/datamodel/communitymech.py`
- GitHub Issue: [CommunityMech#30](https://github.com/CultureBotAI/CommunityMech/issues/30)
