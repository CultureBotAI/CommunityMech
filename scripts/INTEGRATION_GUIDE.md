# Integration Guide: KG-Microbe + OAK + GTDB Validation

## Overview

This guide explains how to use the three-tier taxonomy validation system for CommunityMech:

1. **kg-microbe** (Primary): Fast, strain-aware, offline validation
2. **OAK/NCBITaxon** (Secondary): API-based validation with lineage
3. **GTDB** (Tertiary): Genome-based taxonomy validation

## Validation Workflow

### Step 1: kg-microbe Validation (Fast Pass)

Run the DuckDB-based kg-microbe validation first:

```bash
cd /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CommunityMech/CommunityMech

# Load kg-microbe data (first time only, ~2 seconds)
uv run python scripts/kgm_strain_lookup.py --load

# Generate validation report
uv run python scripts/kgm_strain_lookup.py --report --output-dir ./kgm_validation_output
```

**Output**:
- `kgm_corrections.tsv` - Detailed corrections
- `kgm_statistics.json` - Summary stats
- `kgm_validation_report.txt` - Human-readable report
- `kgm_taxonomy.duckdb` - Indexed database (172 MB)

**Performance**: 5 seconds for 249 taxa

**Coverage**:
- 75 perfect matches (30.1%)
- 93 suggested updates (37.3%)
- 17 need review (6.8%)
- 64 not found (25.7%)

### Step 2: OAK/NCBI Validation (Comprehensive)

For organisms not found in kg-microbe or requiring verification:

```bash
# Run OAK-based validation with strain resolution
python scripts/compare_ncbi_gtdb_taxonomy.py \
    --kb-dir kb \
    --output-dir ./oak_validation_output
```

**Output**:
- `ncbitaxon_corrections.tsv` - File-by-file corrections
- `strain_resolution_summary.tsv` - Strain-level details
- `gtdb_classifications.tsv` - GTDB lineages
- `taxonomy_comparison_report.txt` - Full report

**Performance**: ~45 seconds for 249 taxa

**Coverage**:
- Full NCBI Taxonomy database access
- Real-time API queries
- Lineage information
- Synonym detection

### Step 3: Cross-Reference Results

Compare kg-microbe and OAK results to make informed decisions:

```python
# Example: Cross-reference validation results

import pandas as pd

# Load both validation results
kgm_df = pd.read_csv('kgm_validation_output/kgm_corrections.tsv', sep='\t')
oak_df = pd.read_csv('oak_validation_output/ncbitaxon_corrections.tsv', sep='\t')

# Merge on preferred_term
merged = kgm_df.merge(oak_df, on='preferred_term', how='outer', suffixes=('_kgm', '_oak'))

# Find consensus
consensus = merged[
    (merged['kgm_suggested_id'] == merged['recommended_id_oak']) &
    (merged['action_kgm'] == 'UPDATE')
]

# Find conflicts
conflicts = merged[
    (merged['kgm_suggested_id'] != merged['recommended_id_oak']) &
    (merged['action_kgm'] == 'UPDATE') &
    (merged['action_oak'] == 'UPDATE')
]

print(f"Consensus updates: {len(consensus)}")
print(f"Conflicts requiring review: {len(conflicts)}")
```

## Decision Matrix

Use this matrix to decide which ID to use:

| kg-microbe | OAK/NCBI | GTDB | Decision |
|------------|----------|------|----------|
| EXACT match | Match | Match | **Keep current ID** ✓ |
| UPDATE suggested | Match new ID | - | **Update to new ID** (high confidence) |
| NOT_FOUND | Found | Found | **Use OAK ID** (kg-microbe snapshot outdated) |
| Multiple matches | Single match | Match OAK | **Use OAK ID** (disambiguation) |
| Single match | Different ID | - | **Review manually** (conflict) |
| NOT_FOUND | NOT_FOUND | Found | **Use GTDB** (genome-based) |

## Common Scenarios

### Scenario 1: Perfect Agreement

```
Organism: Methanococcus maripaludis S2
kg-microbe: NCBITaxon:267377 (EXACT, STRAIN_MATCH)
OAK: NCBITaxon:267377 ✓
GTDB: g__Methanococcus; s__Methanococcus maripaludis

Decision: KEEP NCBITaxon:267377 ✓
```

### Scenario 2: kg-microbe Suggests Update

```
Organism: Syntrophobacter fumaroxidans
Current ID: NCBITaxon:28197
kg-microbe: NCBITaxon:119484 (UPDATE, EXACT)
OAK: NCBITaxon:119484 ✓

Decision: UPDATE to NCBITaxon:119484
Reason: Taxonomy reclassification
```

### Scenario 3: Not in kg-microbe

```
Organism: Chlamydomonas reinhardtii
Current ID: NCBITaxon:3055
kg-microbe: NOT_FOUND
OAK: NCBITaxon:3055 ✓ "Chlamydomonas reinhardtii"
GTDB: Not applicable (eukaryote)

Decision: KEEP NCBITaxon:3055 (verified by OAK)
Reason: Recent or non-bacterial organism not in kg-microbe
```

### Scenario 4: Conflict Requires Review

```
Organism: Leptospirillum ferriphilum
Current ID: NCBITaxon:178899
kg-microbe: NCBITaxon:178606 (UPDATE)
OAK: NCBITaxon:178606 ✓
Note: Multiple YAML files use different IDs (178899, 178306)

Decision: UPDATE ALL to NCBITaxon:178606
Reason: Consensus between kg-microbe and OAK
Action: Update both Copper_Biomining_Heap_Leach.yaml and Australian_Lead_Zinc_Polymetallic.yaml
```

### Scenario 5: Strain Designation Without Strain ID

```
Organism: Enterobacter cloacae AA4
Current ID: NCBITaxon:550 (species-level)
kg-microbe: NCBITaxon:550 (SPECIES_MATCH)
OAK: No strain-specific ID found for "AA4"

Decision: KEEP NCBITaxon:550
Action: Document strain in notes field
YAML update:
  notes: "Specific strain AA4. No strain-specific NCBITaxon ID available."
```

## Batch Update Workflow

### 1. Extract High-Confidence Updates

```bash
# From kg-microbe corrections
grep "UPDATE.*EXACT" kgm_validation_output/kgm_corrections.tsv > high_confidence_updates.tsv

# Count
wc -l high_confidence_updates.tsv
```

### 2. Generate Update Script

Create a Python script to apply updates:

```python
#!/usr/bin/env python3
"""Apply kg-microbe corrections to YAML files"""

import yaml
from pathlib import Path
import pandas as pd

# Load corrections
corrections = pd.read_csv('kgm_validation_output/kgm_corrections.tsv', sep='\t')
updates = corrections[corrections['action'] == 'UPDATE']

# Group by file
for file_name, group in updates.groupby('file'):
    yaml_path = Path('kb/communities') / file_name

    # Load YAML
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    # Apply updates
    for _, row in group.iterrows():
        for taxon_entry in data['taxonomy']:
            if taxon_entry['taxon_term']['preferred_term'] == row['preferred_term']:
                old_id = taxon_entry['taxon_term']['term']['id']
                new_id = f"NCBITaxon:{row['kgm_suggested_id']}"

                print(f"Updating {row['preferred_term']}: {old_id} → {new_id}")
                taxon_entry['taxon_term']['term']['id'] = new_id

    # Write updated YAML
    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

    print(f"✓ Updated {file_name}")
```

### 3. Validate Changes

```bash
# Re-run validation after updates
uv run python scripts/kgm_strain_lookup.py --report --output-dir ./kgm_validation_output_v2

# Compare statistics
diff kgm_validation_output/kgm_statistics.json kgm_validation_output_v2/kgm_statistics.json
```

## Search Utilities

### Quick Organism Lookup

```bash
# Find organism in kg-microbe
uv run python scripts/kgm_strain_lookup.py --search "Organism name"

# Find specific strain
uv run python scripts/kgm_strain_lookup.py --strain "Species name" "Strain"

# Examples:
uv run python scripts/kgm_strain_lookup.py --search "Geobacter"
uv run python scripts/kgm_strain_lookup.py --strain "Escherichia coli" "K-12"
```

### Batch Organism Resolution

```python
from kgm_strain_lookup import KGMStrainLookup

lookup = KGMStrainLookup()

organisms = [
    "Desulfovibrio vulgaris Hildenborough",
    "Methanococcus maripaludis S2",
    "Geobacter metallireducens GS-15"
]

for org in organisms:
    result = lookup.resolve_strain(org)
    print(f"{org}:")
    print(f"  Action: {result.action}")
    print(f"  Suggested ID: {result.suggested_id}")
    print(f"  Reason: {result.reason}")
    print()
```

## Handling Special Cases

### Case 1: Taxonomy Reclassifications

When organisms have been reclassified (genus/species name changed):

```yaml
# Before
taxon_term:
  preferred_term: Desulfovibrio vulgaris
  term:
    id: NCBITaxon:881
    label: Desulfovibrio vulgaris

# After (kg-microbe shows synonym)
taxon_term:
  preferred_term: Desulfovibrio vulgaris
  term:
    id: NCBITaxon:881
    label: Nitratidesulfovibrio vulgaris
  notes: >
    Historically known as Desulfovibrio vulgaris. Genus reclassified
    to Nitratidesulfovibrio based on phylogenetic analysis.
```

### Case 2: Multiple IDs for Same Organism

When different files use different IDs:

```bash
# Find duplicates
grep "Leptospirillum ferriphilum" kgm_validation_output/kgm_corrections.tsv

# Output shows:
# Copper_Biomining_Heap_Leach.yaml: 178899 → 178606
# Australian_Lead_Zinc_Polymetallic.yaml: 178306 → 178606

# Decision: Standardize to 178606 in both files
```

### Case 3: Strain-Specific but No Strain ID

For organisms like "Enterobacter cloacae AA4" where strain is specified but no strain-specific ID exists:

```yaml
taxon_term:
  preferred_term: Enterobacter cloacae AA4
  term:
    id: NCBITaxon:550  # Species-level ID
    label: Enterobacter cloacae
  notes: >
    Strain AA4 isolated from maize root. No strain-specific NCBITaxon
    ID available; using species-level ID. Strain designation documented
    for future reference and potential genome sequencing.
```

## Performance Comparison

| Validation Method | Time | Coverage | Offline | Strain-Aware | Lineage Info |
|-------------------|------|----------|---------|--------------|--------------|
| **kg-microbe** | 5s | 75% | ✓ | ✓✓✓ | Limited |
| **OAK/NCBI** | 45s | 100% | ✗ | ✓✓ | ✓✓✓ |
| **GTDB** | N/A | Bacteria/Archaea | ✓ | ✓✓✓ | ✓✓✓ |
| **Combined** | 50s | 100% | Partial | ✓✓✓ | ✓✓✓ |

## Maintenance Schedule

### Weekly
- Run kg-microbe validation on new/updated YAMLs
- Review and apply high-confidence updates

### Monthly
- Run full OAK validation
- Cross-reference with kg-microbe results
- Update strain documentation

### Quarterly
- Download latest kg-microbe data
- Rebuild DuckDB database
- Run full three-tier validation
- Document taxonomy changes

## Troubleshooting

### Issue: Organism Not Found in Any System

```
Organism: Obscure Strain X
kg-microbe: NOT_FOUND
OAK: NOT_FOUND
GTDB: NOT_FOUND

Actions:
1. Verify spelling and nomenclature
2. Check if organism has been renamed
3. Search NCBI directly: https://www.ncbi.nlm.nih.gov/taxonomy
4. If confirmed valid, document as custom entry
```

### Issue: Conflicting IDs Between Systems

```
Organism: Example species
kg-microbe: NCBITaxon:12345
OAK: NCBITaxon:67890

Actions:
1. Check when kg-microbe snapshot was created
2. Verify current NCBI entry via web interface
3. Prefer newer/OAK ID if kg-microbe is outdated
4. Document conflict in notes
```

### Issue: Database Loading Fails

```bash
# Error: File not found
# Solution: Check kg-microbe data path
python scripts/kgm_strain_lookup.py \
    --load \
    --kgm-data-dir /correct/path/to/kg-microbe/data

# Error: Out of memory
# Solution: Close other applications, increase swap space
# DuckDB is efficient but needs ~500MB free RAM
```

## Advanced Usage

### Custom Queries via DuckDB

```python
import duckdb

conn = duckdb.connect('kgm_taxonomy.duckdb')

# Find all Geobacter species
result = conn.execute("""
    SELECT id, name, xref
    FROM ncbitaxon
    WHERE name LIKE '%Geobacter%'
    AND category = 'biolink:OrganismTaxon'
    ORDER BY name
""").fetchall()

for row in result:
    print(f"{row[0]}: {row[1]}")

# Find all organisms with specific genetic code
result = conn.execute("""
    SELECT id, name, xref
    FROM ncbitaxon
    WHERE xref LIKE '%GC_ID:11%'
    LIMIT 10
""").fetchall()
```

### Export to Different Formats

```python
from kgm_strain_lookup import KGMStrainLookup
import json

lookup = KGMStrainLookup()
results = lookup.validate_community_taxa()

# Export to JSON
with open('validation_results.json', 'w') as f:
    json.dump({
        'perfect_match': [
            {
                'preferred_term': r['taxon'].preferred_term,
                'ncbi_id': r['taxon'].ncbi_id,
                'file': r['taxon'].file_name
            }
            for r in results['perfect_match']
        ],
        # ... other categories
    }, f, indent=2)
```

## Integration with CI/CD

Add validation to GitHub Actions:

```yaml
# .github/workflows/taxonomy-validation.yml
name: Taxonomy Validation

on: [pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install duckdb pyyaml

      - name: Run kg-microbe validation
        run: |
          python scripts/kgm_strain_lookup.py --report

      - name: Check for errors
        run: |
          # Fail if > 10% NOT_FOUND
          python -c "
          import json
          with open('kgm_statistics.json') as f:
              stats = json.load(f)
          if stats['not_found_pct'] > 10:
              raise Exception('Too many organisms not found')
          "

      - name: Upload results
        uses: actions/upload-artifact@v2
        with:
          name: validation-report
          path: kgm_validation_output/
```

## Summary

The integrated validation system provides:

1. **Speed**: kg-microbe validates 249 taxa in 5 seconds
2. **Accuracy**: Cross-validation catches conflicts and errors
3. **Completeness**: OAK fills gaps in kg-microbe coverage
4. **Strain Resolution**: Intelligent strain designation handling
5. **Reproducibility**: Offline DuckDB database for consistent results

**Recommended Workflow**:
```bash
# 1. Fast validation (5 seconds)
uv run python scripts/kgm_strain_lookup.py --report

# 2. Review results
cat kgm_validation_output/kgm_validation_report.txt

# 3. For organisms not found, run OAK validation (45 seconds)
python scripts/compare_ncbi_gtdb_taxonomy.py

# 4. Apply high-confidence updates
# 5. Document edge cases in YAML notes
```

This integrated approach ensures CommunityMech maintains accurate, up-to-date taxonomy while minimizing manual review effort.
