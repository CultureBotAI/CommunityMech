# KG-Microbe Strain Lookup System

## Overview

A comprehensive DuckDB-based strain lookup and validation system using kg-microbe data as the unified source of truth for organism taxonomy. This system provides fast, strain-specific search capabilities and validates community YAML taxonomic assignments against the kg-microbe knowledge graph.

## Features

- **Fast DuckDB-based indexing**: Loads 850K+ NCBITaxon records in ~2 seconds
- **Strain-specific search**: Resolves strain designations like "Desulfovibrio vulgaris Hildenborough"
- **Multiple search strategies**: Exact, fuzzy, synonym-based, and strain-specific matching
- **Automated validation**: Compares all community YAML taxa against kg-microbe
- **Comprehensive reporting**: Generates TSV corrections, JSON statistics, and human-readable reports

## Installation

The script requires `duckdb` and `pyyaml`. Install using:

```bash
# Using uv (recommended)
uv pip install duckdb pyyaml

# Or using pip in virtual environment
pip install duckdb pyyaml
```

## Quick Start

### 1. Load kg-microbe data into DuckDB

```bash
uv run python scripts/kgm_strain_lookup.py --load
```

This creates `kgm_taxonomy.duckdb` (172MB) with indexed NCBITaxon data.

### 2. Search for organisms

```bash
# Search by name
uv run python scripts/kgm_strain_lookup.py --search "Methanococcus maripaludis"

# Search for specific strain
uv run python scripts/kgm_strain_lookup.py --strain "Desulfovibrio vulgaris" "Hildenborough"
```

### 3. Validate community YAMLs

```bash
uv run python scripts/kgm_strain_lookup.py --validate
```

### 4. Generate full correction report

```bash
uv run python scripts/kgm_strain_lookup.py --report --output-dir ./kgm_validation_output
```

## Output Files

### kgm_corrections.tsv
File-by-file corrections with recommendations:
- Current NCBITaxon ID
- kg-microbe suggested ID
- Action required (KEEP, UPDATE, REVIEW)
- Confidence level (EXACT, STRAIN_MATCH, SPECIES_MATCH, FUZZY, SYNONYM)

### kgm_statistics.json
Summary statistics:
```json
{
  "total_taxa": 249,
  "perfect_match": 75,
  "perfect_match_pct": 30.1,
  "name_match_diff_id": 93,
  "name_match_diff_id_pct": 37.3,
  "not_found_in_kgm": 64,
  "not_found_pct": 25.7,
  "requires_review": 17,
  "review_pct": 6.8
}
```

### kgm_validation_report.txt
Human-readable report with:
- **Section A**: Perfect matches (no action needed)
- **Section B**: Recommended updates (different IDs)
- **Section C**: Requires manual review (multiple matches)
- **Section D**: Not found in kg-microbe

## Validation Results Summary

From the latest run (249 taxa analyzed):

| Category | Count | Percentage |
|----------|-------|------------|
| **Perfect matches** | 75 | 30.1% |
| **Different IDs** | 93 | 37.3% |
| **Needs review** | 17 | 6.8% |
| **Not found** | 64 | 25.7% |

### Key Findings

#### Perfect Matches (30.1%)
- Taxa where current NCBITaxon ID exactly matches kg-microbe
- Includes exact matches, synonym matches, and species-level matches
- Examples:
  - Methanococcus maripaludis S2 → NCBITaxon:267377 ✓
  - Acidithiobacillus ferrooxidans → NCBITaxon:920 ✓
  - Syntrophus aciditrophicus SB → NCBITaxon:56780 ✓

#### Recommended Updates (37.3%)
- Taxa where kg-microbe suggests a different NCBITaxon ID
- Often due to taxonomy updates, reclassifications, or ID changes
- Examples:
  - Syntrophobacter fumaroxidans: 28197 → 119484
  - Leptospirillum ferriphilum: 178899 → 178606
  - Acidiphilium cryptum: 226539 → 524

#### Not Found in kg-microbe (25.7%)
- Taxa not present in the kg-microbe database
- May be recent strains, uncharacterized organisms, or higher taxonomic levels
- Requires manual verification with NCBI or other sources

#### Requires Review (6.8%)
- Multiple potential matches found in kg-microbe
- Manual inspection needed to select the correct ID

## Strain Resolution

The system intelligently extracts and resolves strain designations:

### Recognized Patterns

1. **Formal designation**: "str." or "strain"
   - `Desulfovibrio vulgaris str. Hildenborough`

2. **Culture collections**: DSM, ATCC, PCC, JCM, LMG, NCTC, etc.
   - `Acidithiobacillus caldus DSM 8584`

3. **Strain codes**: Single letters/numbers after species
   - `Methanococcus maripaludis S2`
   - `Geobacter metallireducens GS-15`
   - `Escherichia coli K-12`

### Search Strategy

1. **Strain-specific search**: Look for exact strain designation
   - `"Species str. Strain"`
   - `"Species strain Strain"`
   - `"Species Strain"`

2. **Species-level fallback**: If strain not found, use species-level ID

3. **Fuzzy matching**: Case-insensitive and partial matching

## Data Sources

### kg-microbe NCBITaxon Nodes
- **Source**: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/paper_KGM/kg-microbe-paper/data/Input_Files/ncbitaxon_nodes.tsv`
- **Records**: 851,837 organism taxonomy entries
- **Fields**: id, category, name, description, xref, provided_by, synonym, iri, same_as

### Community YAMLs
- **Source**: `kb/communities/*.yaml`
- **Count**: 60 community files
- **Taxa**: 249 unique organism entries

## Performance

- **Database loading**: ~2 seconds for 850K records
- **Single query**: < 100ms
- **Full validation**: ~5 seconds for 249 taxa
- **Database size**: 172MB (indexed)

## API Reference

### KGMStrainLookup Class

```python
from kgm_strain_lookup import KGMStrainLookup

# Initialize
lookup = KGMStrainLookup(
    kgm_data_dir="/path/to/kg-microbe/data",
    db_path="kgm_taxonomy.duckdb",
    force_reload=False
)

# Search methods
lookup.search_by_exact_name("Methanococcus maripaludis")
lookup.search_by_fuzzy_name("Desulfovibrio", limit=10)
lookup.search_strain_specific("Desulfovibrio vulgaris", "Hildenborough")

# Strain extraction
strain_info = lookup.extract_strain_info("Escherichia coli K-12")
# Returns: StrainInfo(species_name="Escherichia coli", strain_designation="K-12", ...)

# Resolution
recommendation = lookup.resolve_strain("Methanococcus maripaludis S2", current_ncbi_id="267377")
# Returns: ResolutionRecommendation with action plan

# Validation
results = lookup.validate_community_taxa(yaml_dir="kb/communities")

# Reporting
lookup.generate_corrections_report(output_dir="./output")
```

## Command-Line Interface

```bash
# Load data
python kgm_strain_lookup.py --load

# Search
python kgm_strain_lookup.py --search "Organism name"

# Strain-specific search
python kgm_strain_lookup.py --strain "Species name" "Strain designation"

# Validate
python kgm_strain_lookup.py --validate

# Generate report
python kgm_strain_lookup.py --report --output-dir ./output

# Custom data directory
python kgm_strain_lookup.py --kgm-data-dir /custom/path --db-path custom.duckdb
```

## Integration with Existing Validation

The KGM strain lookup complements the existing OAK/GTDB validation system:

### Validation Hierarchy
1. **kg-microbe** (primary): Fast, comprehensive, strain-aware
2. **OAK/NCBITaxon** (secondary): API-based validation
3. **GTDB** (tertiary): Genome-based taxonomy

### Recommended Workflow

```bash
# Step 1: Run kg-microbe validation (fast)
uv run python scripts/kgm_strain_lookup.py --report

# Step 2: Run OAK/GTDB validation (comprehensive)
python scripts/compare_ncbi_gtdb_taxonomy.py

# Step 3: Compare results and make informed decisions
# - kg-microbe: 249 taxa in 5 seconds
# - OAK: Detailed lineage and synonym information
# - GTDB: Genome-based validation
```

## Examples

### Example 1: Find strain-specific entry

```bash
$ uv run python scripts/kgm_strain_lookup.py --strain "Methanococcus maripaludis" "S2"

Searching for strain: Methanococcus maripaludis S2

Found 1 match(es):

1. Methanococcus maripaludis S2
   ID: NCBITaxon:267377
   Confidence: STRAIN_MATCH
   Category: biolink:OrganismTaxon
   Synonyms: Methanococcus maripaludis LL, Methanococcus maripaludis str. S2
   Xref: GC_ID:11|PMID:15466049
```

### Example 2: Handle taxonomy updates

```bash
# Syntrophobacter fumaroxidans ID changed
Current:   NCBITaxon:28197
kg-microbe: NCBITaxon:119484

Action: UPDATE
Reason: kg-microbe suggests NCBITaxon:119484 (taxonomy update)
```

### Example 3: Species-level fallback

```bash
# Strain not in database - use species level
Preferred term: "Desulfovibrio vulgaris Hildenborough"
Strain search: No strain-specific entry found
Species search: NCBITaxon:881 (Nitratidesulfovibrio vulgaris)

Action: KEEP (species-level)
Note: Document strain designation in notes field
```

## Troubleshooting

### Database not loading
- Ensure kg-microbe data files exist at the specified path
- Check disk space (needs ~200MB)
- Try `--load` flag to force reload

### No matches found
- Check organism name spelling
- Try fuzzy search: `--search "partial name"`
- Verify organism is in NCBITaxon (not all strains have IDs)

### Multiple matches
- Review the `kgm_validation_report.txt` Section C
- Compare with OAK validation results
- Check synonyms and xref fields for context

## Future Enhancements

- [ ] Add GTDB genome mapping
- [ ] Integrate with OAK adapter for unified lookup
- [ ] Support for batch updates to YAML files
- [ ] Web interface for interactive search
- [ ] Export to BioLink format
- [ ] Lineage traversal queries

## Citation

If you use this tool, please cite:

- **kg-microbe**: Reese et al. (2024) "kg-microbe: A Microbiology Knowledge Graph"
- **CommunityMech**: This project

## License

BSD-3-Clause (same as CommunityMech project)

## Contact

For questions or issues, please open an issue on the CommunityMech GitHub repository.
