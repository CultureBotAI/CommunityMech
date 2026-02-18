# GTDB Integration Guide

This guide explains how to integrate GTDB (Genome Taxonomy Database) validation into the taxonomy comparison script.

## Overview

GTDB is an alternative taxonomy database that uses genome-based phylogeny to classify bacteria and archaea. It often differs from NCBI taxonomy, especially at higher taxonomic ranks.

## Why Compare NCBI and GTDB?

1. **Different nomenclature**: GTDB uses different phylum names (e.g., "Pseudomonadota" instead of "Proteobacteria")
2. **More recent classifications**: GTDB is updated regularly based on genomic data
3. **Resolving conflicts**: When NCBI and GTDB disagree, it highlights taxonomic uncertainty
4. **Validation**: Cross-referencing helps identify potential errors in either database

## Methods to Access GTDB

### Option 1: GTDB Web API (Recommended for Small Datasets)

The GTDB website provides a web-based search interface:
- URL: https://gtdb.ecogenomic.org/

However, there is no official public API for programmatic access. The script currently includes placeholder code for API access that would need implementation if such an API becomes available.

### Option 2: Download GTDB Database Files

Download the latest GTDB taxonomy files:

```bash
# Download GTDB taxonomy files (Release 220, adjust version as needed)
cd /path/to/your/data/directory

# Bacteria taxonomy
wget https://data.gtdb.ecogenomic.org/releases/latest/bac120_taxonomy.tsv.gz
gunzip bac120_taxonomy.tsv.gz

# Archaea taxonomy
wget https://data.gtdb.ecogenomic.org/releases/latest/ar53_taxonomy.tsv.gz
gunzip ar53_taxonomy.tsv.gz

# Metadata (optional, contains additional information)
wget https://data.gtdb.ecogenomic.org/releases/latest/bac120_metadata.tsv.gz
gunzip bac120_metadata.tsv.gz
```

File format example (bac120_taxonomy.tsv):
```
genome_accession    taxonomy
GB_GCA_000005845.2  d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;o__Enterobacterales;f__Enterobacteriaceae;g__Escherichia;s__Escherichia coli
```

### Option 3: Use GTDB-Tk (Recommended for Genome-based Classification)

GTDB-Tk is a toolkit for assigning taxonomic classifications to bacterial and archaeal genomes:

```bash
# Install via conda
conda create -n gtdbtk -c conda-forge -c bioconda gtdbtk
conda activate gtdbtk

# Download GTDB-Tk reference data (~80GB)
download-db.sh

# Classify genomes
gtdbtk classify_wf --genome_dir genomes/ --out_dir output/ --cpus 4
```

### Option 4: Local Database Search Script

Create a Python script to search local GTDB files:

```python
import pandas as pd

def load_gtdb_taxonomy(bac_file, ar_file):
    """Load GTDB taxonomy files into memory"""
    bac_df = pd.read_csv(bac_file, sep='\t', header=0)
    ar_df = pd.read_csv(ar_file, sep='\t', header=0)

    # Combine bacteria and archaea
    taxonomy_df = pd.concat([bac_df, ar_df], ignore_index=True)

    # Parse taxonomy strings
    taxonomy_df['species'] = taxonomy_df['taxonomy'].str.extract(r's__([^;]+)')

    return taxonomy_df

def search_gtdb_species(species_name, taxonomy_df):
    """Search for a species in GTDB"""
    # Clean species name
    clean_name = species_name.strip().replace('Candidatus ', '')

    # Search
    results = taxonomy_df[taxonomy_df['species'].str.contains(clean_name, case=False, na=False)]

    if len(results) > 0:
        return results.iloc[0]['taxonomy']
    return None

# Usage
taxonomy_df = load_gtdb_taxonomy('bac120_taxonomy.tsv', 'ar53_taxonomy.tsv')
lineage = search_gtdb_species('Acidiphilium multivorum', taxonomy_df)
print(lineage)
```

## Integrating GTDB into the Validation Script

### Method 1: Modify the Script to Use Local GTDB Files

Edit `compare_ncbi_gtdb_taxonomy.py` and replace the `load_gtdb_local()` function:

```python
import pandas as pd

def load_gtdb_local(gtdb_path: Optional[Path]) -> Optional[Dict]:
    """Load local GTDB database files"""
    if not gtdb_path or not gtdb_path.exists():
        return None

    try:
        # Assume gtdb_path is a directory containing taxonomy files
        bac_file = gtdb_path / 'bac120_taxonomy.tsv'
        ar_file = gtdb_path / 'ar53_taxonomy.tsv'

        if not bac_file.exists() or not ar_file.exists():
            return None

        # Load both files
        bac_df = pd.read_csv(bac_file, sep='\t', header=0)
        ar_df = pd.read_csv(ar_file, sep='\t', header=0)

        # Combine and index by species
        taxonomy_df = pd.concat([bac_df, ar_df], ignore_index=True)
        taxonomy_df['species'] = taxonomy_df['taxonomy'].str.extract(r's__([^;]+)')

        # Create lookup dictionary
        gtdb_dict = {}
        for _, row in taxonomy_df.iterrows():
            species = row['species']
            if pd.notna(species):
                gtdb_dict[species.lower()] = row['taxonomy']

        return gtdb_dict

    except Exception as e:
        print(f"Error loading GTDB: {e}")
        return None
```

Then update `query_gtdb_api()` to use local data:

```python
def query_gtdb_local(species_name: str, gtdb_dict: Dict) -> GTDBInfo:
    """Query local GTDB database"""
    if not gtdb_dict:
        return GTDBInfo(found=False, lineage=None, classification=None)

    # Clean and search
    clean_name = species_name.strip().replace('Candidatus ', '').lower()

    lineage = gtdb_dict.get(clean_name)

    if lineage:
        classification = parse_gtdb_lineage(lineage)
        return GTDBInfo(
            found=True,
            lineage=lineage,
            classification=classification
        )

    return GTDBInfo(found=False, lineage=None, classification=None)
```

### Method 2: Run with Local GTDB Data

```bash
# Download GTDB files to a directory
mkdir -p ~/data/gtdb
cd ~/data/gtdb
wget https://data.gtdb.ecogenomic.org/releases/latest/bac120_taxonomy.tsv.gz
wget https://data.gtdb.ecogenomic.org/releases/latest/ar53_taxonomy.tsv.gz
gunzip *.gz

# Run the script with GTDB path
python scripts/compare_ncbi_gtdb_taxonomy.py --gtdb-path ~/data/gtdb
```

## Understanding GTDB Taxonomy Format

GTDB uses a standardized format with rank prefixes:

```
d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;o__Burkholderiales;f__Burkholderiaceae;g__Acidiphilium;s__Acidiphilium multivorum
```

Rank prefixes:
- `d__` = Domain
- `p__` = Phylum
- `c__` = Class
- `o__` = Order
- `f__` = Family
- `g__` = Genus
- `s__` = Species

## Common NCBI vs GTDB Differences

| Taxonomic Rank | NCBI Name | GTDB Name |
|----------------|-----------|-----------|
| Phylum | Proteobacteria | Pseudomonadota |
| Phylum | Actinobacteria | Actinomycetota |
| Phylum | Firmicutes | Bacillota |
| Phylum | Bacteroidetes | Bacteroidota |
| Phylum | Acidobacteria | Acidobacteriota |

## Expected Output with GTDB Integration

When GTDB is properly integrated, the report will include:

```
A. PERFECT MATCHES (X)
✓ Acidiphilium multivorum
  Literature: "Acidiphilium multivorum"
  NCBITaxon:62140 → "Acidiphilium multivorum" ✓
  GTDB: d__Bacteria;p__Pseudomonadota;c__Alphaproteobacteria;o__Acetobacterales;f__Acetobacteraceae;g__Acidiphilium;s__Acidiphilium multivorum

D. NCBI vs GTDB CONFLICTS (X)
⚠ Desulfovibrio vulgaris
  Literature: "Desulfovibrio vulgaris"
  NCBI: Genus Desulfovibrio (Phylum Proteobacteria)
  GTDB: Genus Nitratidesulfovibrio (Phylum Pseudomonadota)
  → NCBI renamed genus, GTDB uses updated nomenclature
```

## Troubleshooting

### GTDB files not found
- Ensure you've downloaded the latest GTDB release
- Check file paths are correct
- Verify files are unzipped (.tsv not .tsv.gz)

### Species not found in GTDB
- Some species may not have genome representatives in GTDB
- Try searching at genus level
- Check for synonyms or alternative names

### Memory issues with large GTDB files
- GTDB taxonomy files can be large (~100MB-1GB)
- Consider using a database (SQLite) instead of in-memory dictionary
- Filter to relevant species before loading

## References

- GTDB Website: https://gtdb.ecogenomic.org/
- GTDB Publication: Parks et al. (2022) "GTDB: an ongoing census of bacterial and archaeal diversity through a phylogenetically consistent, rank normalized and complete genome-based taxonomy"
- GTDB-Tk: https://github.com/Ecogenomics/GTDBTk
- GTDB Downloads: https://data.gtdb.ecogenomic.org/

## Next Steps

1. Download GTDB taxonomy files
2. Modify the script to load local GTDB data
3. Re-run validation with GTDB integration
4. Analyze NCBI vs GTDB conflicts
5. Document any systematic differences for your community
