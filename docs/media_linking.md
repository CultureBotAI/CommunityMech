# Growth Media Linking to CultureMech and MediaIngredientMech

## Overview

This feature links CommunityMech growth media records to external databases:
- **CultureMech**: Standard microbiology media database
- **MediaIngredientMech**: Media ingredient/component database

## Architecture

### Core Utilities (`src/communitymech/utils/media_linker.py`)

**MediaFetcher**
- Fetches and caches YAML data from CultureMech and MediaIngredientMech GitHub repos
- Implements TTL-based caching (default: 24 hours)
- Cache stored in `media_cache/` (gitignored)

**MediaMatcher**
- Fuzzy matching for media and ingredient names
- Exact match (case-insensitive) → fuzzy match (≥0.85 threshold)
- Supports manual overrides from `conf/media_mappings.yaml`

**CompositionMerger**
- Merges CultureMech ingredients with existing community-curated data
- Marks source: "CultureMech" vs "community_curated"
- Preserves existing ingredients, adds new ones

### CLI Script (`scripts/link_growth_media.py`)

Command-line tool for batch processing all community YAML files.

**Features:**
- Dry-run mode for previewing changes
- Single community or batch processing
- Configurable fuzzy matching threshold
- Cache control (TTL, no-cache flag)
- Color-coded output with statistics
- Backup originals before modification

## Usage

### Preview changes (dry-run)
```bash
just link-media-dry
```

### Apply changes
```bash
just link-media
```

### Generate mapping reports
```bash
just link-media-report
```

This generates three reports in `reports/`:
- `ingredient_mapping.csv` - All ingredients with mapping status
- `media_mapping.csv` - All media with mapping status
- `media_linking_summary.txt` - Human-readable summary

### Process single community
```bash
uv run python scripts/link_growth_media.py --community-id EcoFAB_Ring_Trial_SynCom17 --dry-run
```

### Advanced options
```bash
uv run python scripts/link_growth_media.py \
  --dry-run \
  --fuzzy-threshold 0.9 \
  --cache-ttl 3600 \
  --no-cache \
  --limit 10 \
  --ingredient-report reports/ingredients.csv \
  --media-report reports/media.csv \
  --summary-report reports/summary.txt
```

## Reporting

### Report Formats

**Ingredient Mapping CSV** (`ingredient_mapping.csv`)
```csv
ingredient_name,community_id,media_name,mapped_id,match_score,status
yeast extract,EcoFAB_Ring_Trial_SynCom17,R2A medium,MediaIngredientMech:000015,1.000,mapped
peptone,EcoFAB_Ring_Trial_SynCom17,R2A medium,,0.850,unmapped
```

**Media Mapping CSV** (`media_mapping.csv`)
```csv
media_name,community_id,mapped_id,match_score,status
R2A medium,EcoFAB_Ring_Trial_SynCom17,CultureMech:000042,1.000,mapped
LB medium,Synechococcus_Ecoli_SPC,CultureMech:000001,1.000,mapped
```

**Summary Report** (`media_linking_summary.txt`)
- Human-readable text report
- Statistics on mapping success
- Lists of mapped and unmapped items
- Communities where each ingredient appears

### Using Reports for Curation

1. **Identify unmapped ingredients**: Review `ingredient_mapping.csv` for `status=unmapped`
2. **Add manual overrides**: Update `conf/media_mappings.yaml` with corrections
3. **Re-run with reports**: Generate updated reports to verify fixes
4. **Track progress**: Use summary report to monitor curation completeness

## Configuration

### Manual Overrides (`conf/media_mappings.yaml`)

Provide explicit mappings when fuzzy matching fails:

```yaml
media_overrides:
  "R2A medium":
    culturemech_id: "CultureMech:000042"
    note: "Standard R2A for heterotrophs"

ingredient_overrides:
  "yeast extract":
    media_ingredient_mech_id: "MediaIngredientMech:000015"
    note: "Standard yeast extract component"
```

## Schema Structure

Each `MicrobialCommunity` can have `growth_media[]`:

```yaml
growth_media:
  - name: R2A medium
    culturemech_id: CultureMech:000042
    culturemech_url: https://github.com/CultureBotAI/CultureMech/...
    composition:
      - name: yeast extract
        media_ingredient_mech_id: MediaIngredientMech:000015
        media_ingredient_mech_url: https://github.com/CultureBotAI/MediaIngredientMech/...
        concentration: "0.5"
        unit: g/L
        from: CultureMech
      - name: glucose
        concentration: "1.0"
        unit: g/L
        chebi_term:
          id: CHEBI:17234
          label: glucose
        from: community_curated
    ph: "7.0"
    temperature: "30"
    temperature_unit: "°C"
    atmosphere: aerobic
```

## External Data Sources

### CultureMech
- Repository: https://github.com/CultureBotAI/CultureMech
- Raw YAML: `https://raw.githubusercontent.com/CultureBotAI/CultureMech/main/kb/media/CultureMech_XXXXXX.yaml`

### MediaIngredientMech
- Repository: https://github.com/CultureBotAI/MediaIngredientMech
- Raw YAML: `https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/main/kb/ingredients/MediaIngredientMech_XXXXXX.yaml`

## Implementation Notes

1. **Cache Management**: The `media_cache/` directory is gitignored. Cached data is stored as JSON with timestamp validation.

2. **Fuzzy Matching**: Uses `difflib.SequenceMatcher` with default threshold 0.85. Adjust via `--fuzzy-threshold` flag.

3. **Source Tracking**: Ingredients are marked with `from` field to distinguish CultureMech imports from manual curation.

4. **Validation**: All changes preserve LinkML schema compliance. Run `just validate-all` after applying.

5. **Future Work**:
   - CultureMech/MediaIngredientMech need to provide index files for full matching
   - Current implementation has placeholder logic for media/ingredient discovery
   - Consider adding evidence tracking for media assignments

## Verification

After running the script, validate the results:

```bash
just link-media
just validate-all
```

## See Also

- LinkML schema: `src/communitymech/schema/communitymech.yaml`
- GrowthMedia class definition (lines 631-658)
- GrowthMediaComponent class definition (lines 613-630)
