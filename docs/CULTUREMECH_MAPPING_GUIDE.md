# CultureMech Media Mapping Guide

## Overview

This guide explains how to find and link CultureMech media entries to CommunityMech growth media records.

## CultureMech Repository Structure

**Repository**: https://github.com/CultureBotAI/CultureMech

**Media Location**: `data/normalized_yaml/`

**Categories**:
- `bacterial/` - Bacterial culture media (DSMZ, ATCC, CCAP, etc.)
- `fungal/` - Fungal culture media
- `algae/` - Algal culture media
- `archaea/` - Archaeal culture media
- `specialized/` - Multi-domain or specialized media

## Finding Media in CultureMech

### Method 1: Browse GitHub

1. **Navigate to media directory**:
   https://github.com/CultureBotAI/CultureMech/tree/main/data/normalized_yaml

2. **Select organism category**:
   - For bacterial community → `bacterial/`
   - For fungal community → `fungal/`
   - For algal community → `algae/`
   - For archaeal community → `archaea/`

3. **Search for medium**:
   - Use GitHub's file search (press `/`)
   - Search by:
     - Medium name (e.g., "LB", "M9", "CCAP")
     - Collection ID (e.g., "DSMZ", "ATCC")
     - Original name

4. **Open the YAML file** to view details

### Method 2: Clone Repository

```bash
# Clone CultureMech
git clone https://github.com/CultureBotAI/CultureMech.git

# Search for media by name
cd CultureMech/data/normalized_yaml
grep -r "name: LB" .

# Search for media by collection
grep -r "DSMZ" bacterial/
```

### Method 3: API Search (if available)

```bash
# Search using GitHub API
curl -s "https://api.github.com/search/code?q=repo:CultureBotAI/CultureMech+M9+path:data/normalized_yaml" \
  | jq '.items[].name'
```

## Extracting Media Information

### Example: CCAP Medium C100

**File**: `data/normalized_yaml/bacterial/CCAP_C100_S_W_AMP.yaml`

**Contents**:
```yaml
name: S/W + AMP
original_name: S/W + AMP
category: imported
medium_type: COMPLEX
physical_state: LIQUID
ph_range: 7-8
media_term:
  preferred_term: CCAP Medium C100
  term:
    id: mediadive.medium:C100  # ← Use this as culturemech_id
    label: S/W + AMP
notes: 'Source: CCAP | Link: https://www.ccap.ac.uk/...'
ingredients:
  - preferred_term: Soil
    concentration:
      value: variable
      unit: VARIABLE
  - preferred_term: (NH4)MgPO4
    concentration:
      value: '0.01'
      unit: G_PER_L
preparation_steps:
  - step_number: 1
    action: AUTOCLAVE
    description: "Put a layer about 1 cm deep..."
```

### Key Fields to Extract

1. **`media_term.term.id`** → Use as `culturemech_id`
2. **`name`** → Medium name
3. **`ph_range`** → Use as `ph`
4. **`ingredients`** → Map to `composition`
5. **`notes`** → Include in `preparation_notes`

## Mapping to CommunityMech

### Step 1: Identify the Medium

From CultureMech YAML:
```yaml
media_term:
  term:
    id: mediadive.medium:C100
    label: S/W + AMP
```

### Step 2: Construct GitHub URL

Format:
```
https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/{category}/{filename}.yaml
```

Example:
```
https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/bacterial/CCAP_C100_S_W_AMP.yaml
```

### Step 3: Add to CommunityMech

```yaml
growth_media:
  - name: CCAP Medium C100 (Soil/Water + AMP)
    culturemech_id: mediadive.medium:C100
    culturemech_url: https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/bacterial/CCAP_C100_S_W_AMP.yaml
    ph: "7-8"
    temperature: "20"
    temperature_unit: "°C"
    atmosphere: aerobic
    composition:
      - name: Soil (garden loam)
        concentration: "variable"
      - name: Ammonium magnesium phosphate
        concentration: "0.01"
        unit: "g/L"
    preparation_notes: "See CultureMech for full preparation protocol."
```

## Common Culture Collections in CultureMech

### Bacterial Media

**DSMZ (German Collection of Microorganisms and Cell Cultures)**:
- Files: `bacterial/DSMZ_*.yaml`
- ID format: `mediadive.medium:DSMZ###`
- Example: `DSMZ_Medium_1.yaml`

**ATCC (American Type Culture Collection)**:
- Files: `bacterial/ATCC_*.yaml`
- ID format: `mediadive.medium:ATCC###`
- Example: `ATCC_Medium_1.yaml`

**CCAP (Culture Collection of Algae and Protozoa)**:
- Files: `bacterial/CCAP_*.yaml`
- ID format: `mediadive.medium:C###`
- Example: `CCAP_C100_S_W_AMP.yaml`

### Fungal Media

**CBS (Westerdijk Fungal Biodiversity Institute)**:
- Files: `fungal/CBS_*.yaml`
- ID format: `mediadive.medium:CBS###`

**PDA (Potato Dextrose Agar)**:
- Files: `fungal/PDA*.yaml`
- Common fungal medium

### Algal Media

**CCAP Algal Media**:
- Files: `algae/CCAP_*.yaml`
- Specific to photosynthetic organisms

## Bulk Mapping Script

For mapping multiple media at once:

```python
#!/usr/bin/env python3
"""Map CultureMech media to CommunityMech communities."""

import yaml
from pathlib import Path

CULTUREMECH_BASE = "https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml"

def find_culturemech_media(medium_name: str, category: str = "bacterial") -> dict:
    """Search for medium in CultureMech repository."""
    # Clone repo first: git clone https://github.com/CultureBotAI/CultureMech.git

    culturemech_dir = Path("CultureMech/data/normalized_yaml") / category

    for yaml_file in culturemech_dir.glob("*.yaml"):
        with open(yaml_file) as f:
            data = yaml.safe_load(f)

        if medium_name.lower() in data.get("name", "").lower():
            return {
                "culturemech_id": data["media_term"]["term"]["id"],
                "culturemech_url": f"{CULTUREMECH_BASE}/{category}/{yaml_file.name}",
                "name": data["media_term"]["preferred_term"],
                "ph": data.get("ph_range"),
            }

    return None

# Example usage
if __name__ == "__main__":
    result = find_culturemech_media("LB", "bacterial")
    if result:
        print(f"Found: {result['name']}")
        print(f"ID: {result['culturemech_id']}")
        print(f"URL: {result['culturemech_url']}")
```

## Media ID Formats

Different collections use different ID formats:

| Collection | ID Format | Example |
|------------|-----------|---------|
| DSMZ | `mediadive.medium:DSMZ###` | `mediadive.medium:DSMZ1` |
| ATCC | `mediadive.medium:ATCC###` | `mediadive.medium:ATCC1` |
| CCAP | `mediadive.medium:C###` | `mediadive.medium:C100` |
| CBS | `mediadive.medium:CBS###` | `mediadive.medium:CBS1` |
| Generic | `mediadive.medium:###` | `mediadive.medium:001` |

## When CultureMech Doesn't Have Your Medium

If your medium is not in CultureMech:

1. **Document it fully in CommunityMech**:
   ```yaml
   growth_media:
     - name: Custom Lab Medium
       # No culturemech_id or culturemech_url
       composition:
         # ... full details
   ```

2. **Consider contributing to CultureMech**:
   - Fork CultureMech repository
   - Add your medium in normalized YAML format
   - Submit pull request

3. **Reference original source**:
   ```yaml
   preparation_notes: "Custom medium from Smith et al. 2024"
   evidence:
     - reference: PMID:12345678
       snippet: "Cells were grown in custom medium..."
   ```

## Validation

After adding CultureMech links:

```bash
# Validate schema
just validate kb/communities/YourCommunity.yaml

# Generate HTML to verify links
just gen-html

# Check generated link
grep "CultureMech" docs/communities/YourCommunity.html
```

## Example Mappings

### LB Medium (Luria-Bertani)

**CultureMech**: `bacterial/LB_*.yaml` (various versions)

```yaml
growth_media:
  - name: LB Medium
    culturemech_id: mediadive.medium:LB001
    culturemech_url: https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/bacterial/LB_standard.yaml
```

### M9 Minimal Medium

**CultureMech**: `bacterial/M9_*.yaml`

```yaml
growth_media:
  - name: M9 Minimal Medium
    culturemech_id: mediadive.medium:M9001
    culturemech_url: https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/bacterial/M9_minimal.yaml
```

### YPD (Yeast Extract Peptone Dextrose)

**CultureMech**: `fungal/YPD_*.yaml`

```yaml
growth_media:
  - name: YPD Medium
    culturemech_id: mediadive.medium:YPD001
    culturemech_url: https://github.com/CultureBotAI/CultureMech/blob/main/data/normalized_yaml/fungal/YPD.yaml
```

## Resources

- **CultureMech Repository**: https://github.com/CultureBotAI/CultureMech
- **Normalized Media**: https://github.com/CultureBotAI/CultureMech/tree/main/data/normalized_yaml
- **CommunityMech Growth Media Guide**: `docs/GROWTH_MEDIA_GUIDE.md`
- **Example**: `examples/growth_media_example.yaml`

## Questions?

- Check existing CultureMech media: Browse repository
- Need help finding a medium: Search GitHub issues
- Want to add a medium: Fork and submit PR to CultureMech
- Integration questions: See `docs/GROWTH_MEDIA_GUIDE.md`

---

**Last Updated**: March 6, 2026
**Version**: CultureMech Mapping Guide v1.0
