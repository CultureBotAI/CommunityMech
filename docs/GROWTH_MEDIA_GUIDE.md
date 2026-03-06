# Growth Media Documentation Guide

## Overview

CommunityMech now supports comprehensive documentation of growth media used for cultivating microbial communities and their member organisms. This includes media composition, growth parameters, and links to the CultureMech media database.

## Schema Structure

### Classes

**GrowthMedia** - Main class for documenting growth medium
- `name` (required): Name of the growth medium
- `culturemech_id`: Identifier in CultureMech database (e.g., `MEDIUM:0000001`)
- `culturemech_url`: Direct URL to CultureMech media entry
- `composition`: List of GrowthMediaComponent items
- `ph`: pH of the medium
- `temperature`: Incubation temperature
- `temperature_unit`: Unit for temperature (default: °C)
- `atmosphere`: Atmospheric conditions (aerobic, anaerobic, microaerobic)
- `preparation_notes`: Additional preparation details
- `evidence`: Evidence items supporting this media documentation

**GrowthMediaComponent** - Component of growth medium
- `name` (required): Name of the component
- `concentration`: Concentration value
- `unit`: Unit of measurement
- `chebi_term`: CHEBI term for the component (links to chemical ontology)

## Integration with CultureMech

[CultureMech](https://github.com/CultureBotAI/CultureMech) is a comprehensive microbial culture media database with normalized YAML files for thousands of media from culture collections worldwide.

### CultureMech Repository Structure

Media are organized by organism type:
- `bacterial/` - Bacterial culture media
- `fungal/` - Fungal culture media
- `algae/` - Algal culture media
- `archaea/` - Archaeal culture media
- `specialized/` - Specialized or multi-domain media

Each medium is a YAML file with standardized structure.

### Finding and Linking CultureMech Media

**1. Browse the repository:**
https://github.com/CultureBotAI/CultureMech/tree/main/data/normalized_yaml

**2. Find your medium:**
- Navigate to appropriate category (e.g., `bacterial/`)
- Search for medium name (e.g., `CCAP_C100_S_W_AMP.yaml`)
- Open the file to view details

**3. Get the media ID:**
Look for `media_term.term.id` in the YAML file:
```yaml
media_term:
  term:
    id: mediadive.medium:C100  # ← This is the culturemech_id
```

**4. Construct the GitHub URL:**
Format: `https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/{category}/{filename}.yaml`

Example:
```
https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/bacterial/CCAP_C100_S_W_AMP.yaml
```

**5. Add to your community YAML:**
```yaml
growth_media:
  - name: CCAP Medium C100
    culturemech_id: mediadive.medium:C100
    culturemech_url: https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/bacterial/CCAP_C100_S_W_AMP.yaml
    # ... rest of fields
```

## Usage Examples

### Example 1: CCAP Medium with CultureMech Link

```yaml
growth_media:
  - name: CCAP Medium C100 (Soil/Water + AMP)
    culturemech_id: mediadive.medium:C100
    culturemech_url: https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/bacterial/CCAP_C100_S_W_AMP.yaml
    ph: "7.0"
    temperature: "37"
    temperature_unit: "°C"
    atmosphere: aerobic
    composition:
      - name: Sodium phosphate dibasic
        concentration: "6.78"
        unit: "g/L"
        chebi_term:
          preferred_term: disodium hydrogen phosphate
          term:
            id: CHEBI:34683
            label: disodium hydrogen phosphate
      - name: Potassium phosphate monobasic
        concentration: "3.0"
        unit: "g/L"
        chebi_term:
          preferred_term: potassium dihydrogen phosphate
          term:
            id: CHEBI:63036
            label: potassium dihydrogen phosphate
      - name: Glucose
        concentration: "4.0"
        unit: "g/L"
        chebi_term:
          preferred_term: D-glucose
          term:
            id: CHEBI:17634
            label: D-glucose
    preparation_notes: "Autoclave all components except glucose. Add glucose from sterile stock."
    evidence:
      - reference: PMID:12345678
        supports: SUPPORT
        evidence_source: IN_VITRO
        snippet: "Cultures were grown in M9 minimal medium at 37°C."
```

### Example 2: Simple Medium without CultureMech Link

```yaml
growth_media:
  - name: LB Medium
    ph: "7.0"
    temperature: "37"
    temperature_unit: "°C"
    atmosphere: aerobic
    composition:
      - name: Tryptone
        concentration: "10.0"
        unit: "g/L"
      - name: Yeast extract
        concentration: "5.0"
        unit: "g/L"
      - name: Sodium chloride
        concentration: "10.0"
        unit: "g/L"
```

### Example 3: Anaerobic Medium

```yaml
growth_media:
  - name: Hungate Medium for Methanogens
    ph: "7.2"
    temperature: "55"
    temperature_unit: "°C"
    atmosphere: anaerobic
    composition:
      - name: Yeast extract
        concentration: "2.0"
        unit: "g/L"
      - name: Sodium bicarbonate
        concentration: "5.0"
        unit: "g/L"
        chebi_term:
          preferred_term: sodium hydrogen carbonate
          term:
            id: CHEBI:32139
            label: sodium hydrogen carbonate
      - name: Sodium sulfide
        concentration: "0.5"
        unit: "g/L"
        chebi_term:
          preferred_term: sodium sulfide
          term:
            id: CHEBI:75837
            label: sodium sulfide
    preparation_notes: "Prepare under 80% N2 / 20% CO2 atmosphere. Add sodium sulfide last."
```

### Example 4: Multiple Media (Different Growth Conditions)

```yaml
growth_media:
  # Enrichment medium
  - name: Enrichment Medium
    ph: "7.0"
    temperature: "30"
    atmosphere: aerobic
    composition:
      - name: Complex nutrient mix
        concentration: "variable"
    evidence:
      - reference: PMID:11111111
        supports: SUPPORT
        evidence_source: IN_VITRO
        snippet: "Enriched on complex medium for 3 weeks."

  # Maintenance medium
  - name: Maintenance Medium (Minimal)
    ph: "7.0"
    temperature: "25"
    atmosphere: aerobic
    composition:
      - name: Glucose
        concentration: "1.0"
        unit: "g/L"
      - name: Mineral salts
        concentration: "basal"
    evidence:
      - reference: PMID:22222222
        supports: SUPPORT
        evidence_source: IN_VITRO
        snippet: "Maintained on minimal medium at reduced temperature."
```

## Best Practices

### 1. Use CHEBI Terms Where Possible

Link chemical components to CHEBI for ontological grounding:

```yaml
- name: Glucose
  concentration: "4.0"
  unit: "g/L"
  chebi_term:
    preferred_term: D-glucose
    term:
      id: CHEBI:17634
      label: D-glucose
```

### 2. Document Evidence

Always include evidence for media composition:

```yaml
evidence:
  - reference: PMID:12345678
    supports: SUPPORT
    evidence_source: IN_VITRO
    snippet: "Exact quote from paper mentioning the medium composition."
```

### 3. Link to CultureMech

When available, link to CultureMech for standardized media:

```yaml
culturemech_id: MEDIUM:0000123
culturemech_url: https://culturebotai.github.io/CultureMech/app/media/M9
```

### 4. Include Preparation Notes

Document important preparation details:

```yaml
preparation_notes: "Autoclave at 121°C for 15 min. Add heat-sensitive components by filter sterilization."
```

### 5. Specify Atmosphere

Always document atmospheric conditions:

```yaml
atmosphere: anaerobic  # or aerobic, microaerobic
```

## HTML Rendering

Growth media information is automatically rendered in community HTML pages with:

- **Medium name** and CultureMech ID
- **Link to CultureMech** entry (if provided)
- **Growth parameters** (pH, temperature, atmosphere)
- **Composition table** with concentrations and CHEBI links
- **Preparation notes**
- **Evidence** with PMID/DOI links and snippets

Example output:

```
Growth Media
────────────

M9 Minimal Medium (MEDIUM:0000001)
View in CultureMech →

pH: 7.0    Temperature: 37 °C    Atmosphere: aerobic

Composition
─────────────────────────────────────────────────────
Component                  Concentration  Unit  CHEBI
─────────────────────────────────────────────────────
Sodium phosphate dibasic   6.78          g/L   CHEBI:34683
Glucose                    4.0           g/L   CHEBI:17634
...
─────────────────────────────────────────────────────

Preparation notes: Autoclave all components except glucose.

Evidence
  PMID:12345678
  "Cultures were grown in M9 minimal medium at 37°C."
```

## Validation

Growth media entries are validated like all CommunityMech data:

```bash
# Validate schema
just validate kb/communities/YourCommunity.yaml

# Validate ontology terms (CHEBI)
just validate-terms kb/communities/YourCommunity.yaml

# Validate evidence
just validate-references kb/communities/YourCommunity.yaml
```

## Finding CHEBI Terms

1. Visit [CHEBI](https://www.ebi.ac.uk/chebi/)
2. Search for your chemical (e.g., "glucose")
3. Use the CHEBI ID (e.g., `CHEBI:17634`)
4. Add to your component:

```yaml
chebi_term:
  preferred_term: D-glucose
  term:
    id: CHEBI:17634
    label: D-glucose
```

## Migration from Environmental Factors

If you previously documented growth conditions in `environmental_factors`, consider moving them to `growth_media`:

**Before:**
```yaml
environmental_factors:
  - name: Growth medium
    value: M9 minimal medium
  - name: Temperature
    value: "37"
    unit: "°C"
  - name: pH
    value: "7.0"
```

**After:**
```yaml
growth_media:
  - name: M9 Minimal Medium
    ph: "7.0"
    temperature: "37"
    temperature_unit: "°C"
    composition:
      # ... detailed composition
```

Keep `environmental_factors` for *in situ* environmental conditions (field samples), use `growth_media` for *laboratory* cultivation conditions.

## Complete Example

See `examples/growth_media_example.yaml` for a complete working example with multiple media types.

## Commands

```bash
# Regenerate datamodel after schema changes
just gen-python

# Validate communities with growth media
just validate-all

# Generate HTML pages with growth media display
just gen-html

# View generated HTML
open docs/communities/YourCommunity.html
```

## Questions?

- Schema: `src/communitymech/schema/communitymech.yaml`
- Example: `examples/growth_media_example.yaml`
- Template: `src/communitymech/templates/community.html`
- CultureMech: https://culturebotai.github.io/CultureMech/app/
- CHEBI: https://www.ebi.ac.uk/chebi/

---

**Last Updated**: March 6, 2026
**Feature**: Growth Media Support v1.0
