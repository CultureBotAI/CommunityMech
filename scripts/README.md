# Taxonomy Validation Scripts

This directory contains scripts for validating and correcting taxonomy information in the CommunityMech knowledge base.

## Scripts

### compare_ncbi_gtdb_taxonomy.py

Comprehensive taxonomy validation script that compares NCBITaxonomy and GTDB against literature-derived species names.

**Purpose**: Validate that NCBITaxon IDs in YAML files correctly correspond to the species names from literature (preferred_term).

**Key Principle**: The `preferred_term` (from literature) is the **SOURCE OF TRUTH**. NCBITaxon IDs should accurately represent this name.

## Quick Start

### 1. Basic Validation (NCBI only)

```bash
# From project root directory
.venv/bin/python scripts/compare_ncbi_gtdb_taxonomy.py --skip-gtdb
```

This will:
- Scan all YAML files in `kb/communities/`
- Extract preferred_term (literature name) and NCBITaxon ID
- Validate each ID against NCBITaxonomy using OAK
- Generate three output files

### 2. Output Files

The script generates:

1. **ncbitaxon_corrections.tsv** - Tab-separated file with corrections needed
   - Lists all mismatches
   - Shows suggested NCBITaxon IDs
   - Organized by YAML file

2. **taxonomy_comparison_report.txt** - Human-readable detailed report
   - Section A: Perfect matches (correct IDs)
   - Section B: Mismatches (wrong IDs)
   - Section C: Taxonomy updates (NCBI renamed species)
   - Summary statistics

3. **gtdb_classifications.tsv** - GTDB lineage information
   - Currently empty (GTDB integration pending)
   - See GTDB_INTEGRATION_GUIDE.md for setup

### 3. Command-Line Options

```bash
# Show help
.venv/bin/python scripts/compare_ncbi_gtdb_taxonomy.py --help

# Specify custom kb directory
.venv/bin/python scripts/compare_ncbi_gtdb_taxonomy.py \
    --kb-dir /path/to/kb \
    --skip-gtdb

# Specify output directory
.venv/bin/python scripts/compare_ncbi_gtdb_taxonomy.py \
    --output-dir reports/ \
    --skip-gtdb

# With GTDB (after setup)
.venv/bin/python scripts/compare_ncbi_gtdb_taxonomy.py \
    --gtdb-path ~/data/gtdb
```

## Understanding the Results

### Perfect Match Example

```
✓ Acidiphilium multivorum
  Literature: "Acidiphilium multivorum"
  NCBITaxon:62140 → "Acidiphilium multivorum" ✓
```

**Status**: No action needed. ID is correct.

### Mismatch Example

```
✗ Ferrimicrobium acidiphilum
  Literature: "Ferrimicrobium acidiphilum" (SOURCE OF TRUTH)
  Current NCBITaxon:525909 → "Acidimicrobium ferrooxidans" ✗
  Suggested NCBITaxon:121039 → "Ferrimicrobium acidiphilum"
  File: AMD_Acidophile_Heterotroph_Network.yaml
```

**Status**: Action required. Update NCBITaxon:525909 → 121039 in the YAML file.

### Taxonomy Update Example

```
⚠ Desulfovibrio vulgaris
  Literature: "Desulfovibrio vulgaris"
  NCBITaxon:881 current name: "Nitratidesulfovibrio vulgaris"
  → Literature name is a synonym
  → Keep literature name, note NCBI synonym
```

**Status**: Informational. NCBI has renamed the species, but we keep the literature name as source of truth.

## Correcting Errors

### Step 1: Review the Report

```bash
# View the full report
cat taxonomy_comparison_report.txt

# View only mismatches
grep -A 4 "✗" taxonomy_comparison_report.txt
```

### Step 2: Check the Corrections File

```bash
# View corrections in table format
column -t -s $'\t' ncbitaxon_corrections.tsv | less

# Find specific corrections
grep "Ferrimicrobium" ncbitaxon_corrections.tsv
```

### Step 3: Update YAML Files

Manually edit the YAML file and update the NCBITaxon ID:

```yaml
# BEFORE (incorrect)
taxon_term:
  preferred_term: Ferrimicrobium acidiphilum
  term:
    id: NCBITaxon:525909  # WRONG
    label: Ferrimicrobium acidiphilum

# AFTER (corrected)
taxon_term:
  preferred_term: Ferrimicrobium acidiphilum
  term:
    id: NCBITaxon:121039  # CORRECT
    label: Ferrimicrobium acidiphilum
```

### Step 4: Re-run Validation

```bash
# Verify the fix
.venv/bin/python scripts/compare_ncbi_gtdb_taxonomy.py --skip-gtdb
```

## Current Validation Results

**Last Run**: 2026-02-14

- Total taxa: **249**
- Perfect matches: **77 (30.9%)**
- Mismatches: **161 (64.7%)**
- Taxonomy updates: **11 (4.4%)**

See `TAXONOMY_VALIDATION_SUMMARY.md` for detailed analysis.

## Priority Corrections

The following files have the most errors and should be corrected first:

1. MSC1_Dominant_Core.yaml (92.9% errors)
2. Dangl_SynComm_35.yaml (87.5% errors)
3. At_RSPHERE_SynCom.yaml (85.7% errors)
4. Sorghum_SRC1_Subset.yaml (83.3% errors)
5. AMD_Acidophile_Heterotroph_Network.yaml (66.7% errors)

## Critical Errors

These entries have completely wrong NCBITaxon IDs (pointing to different organisms):

| File | Species | Wrong ID | Correct ID |
|------|---------|----------|------------|
| AMD_Acidophile_Heterotroph_Network.yaml | Ferrimicrobium acidiphilum | 525909 | 121039 |
| AMD_Acidophile_Heterotroph_Network.yaml | Acidiphilium cryptum | 524384 | 524 |
| AMD_Acidophile_Heterotroph_Network.yaml | Acidocella facilis | 80865 | 525 |
| Copper_Biomining_Heap_Leach.yaml | Ferroplasma acidiphilum | 97398 | 74969 |
| Iberian_Pit_Lake_Stratified_Community.yaml | Leptospirillum | 171 | 179 |

## GTDB Integration

To compare against GTDB taxonomy:

1. Read `GTDB_INTEGRATION_GUIDE.md`
2. Download GTDB taxonomy files
3. Update the script to load GTDB data
4. Re-run with `--gtdb-path` option

## Troubleshooting

### OAKlib not found

```bash
# Install oaklib
pip install oaklib

# Or install all dependencies
pip install -e .
```

### NCBITaxon database not available

```bash
# Initialize NCBITaxon via OAK
runoak -i sqlite:obo:ncbitaxon info

# This will download and cache the NCBI taxonomy
```

### Script runs but finds no taxa

Check that:
- You're running from the project root
- YAML files exist in `kb/communities/`
- YAML files have proper structure with `taxonomy` section

### No suggested ID for a mismatch

This means:
- Species name not found in NCBI
- Name might be misspelled
- Species might be uncultured/environmental
- Need to search NCBI manually

## Integration with CI/CD

Add this to your GitHub Actions or CI pipeline:

```yaml
- name: Validate Taxonomy
  run: |
    .venv/bin/python scripts/compare_ncbi_gtdb_taxonomy.py \
        --skip-gtdb \
        --output-dir reports/

    # Fail if too many mismatches
    mismatches=$(grep -c "✗" reports/taxonomy_comparison_report.txt || true)
    if [ "$mismatches" -gt 50 ]; then
        echo "Too many taxonomy mismatches: $mismatches"
        exit 1
    fi
```

## Dependencies

- Python 3.9+
- oaklib >= 0.5.0
- pyyaml >= 6.0
- requests (optional, for GTDB API)
- pandas (optional, for GTDB local files)

## Related Documentation

- `TAXONOMY_VALIDATION_SUMMARY.md` - Detailed analysis of current validation results
- `GTDB_INTEGRATION_GUIDE.md` - How to integrate GTDB taxonomy
- `../kb/communities/*.yaml` - Source data files

## Support

For questions or issues:
1. Check the validation report
2. Review `TAXONOMY_VALIDATION_SUMMARY.md`
3. Consult NCBI Taxonomy Browser: https://www.ncbi.nlm.nih.gov/taxonomy
4. File an issue with details of the specific taxon

## Future Enhancements

- [ ] Automated YAML file updating
- [ ] GTDB integration (in progress)
- [ ] Additional database cross-references (LPSN, MycoBank)
- [ ] Periodic validation scheduling
- [ ] Web interface for reviewing mismatches
- [ ] Synonym tracking database
- [ ] Historical taxonomy change tracking

---

**Last Updated**: 2026-02-14
**Script Version**: 1.0
