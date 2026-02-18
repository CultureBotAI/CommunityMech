#!/usr/bin/env python3
"""
GTDB Integration Demo and Test Script

Demonstrates GTDB functionality without requiring full data download.
Uses sample data to show taxonomy parsing and comparison features.

Usage:
    python scripts/gtdb_demo.py
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from gtdb_integration import GTDBIntegration, GTDBTaxonomy, GTDBMatch
except ImportError:
    print("Error: Could not import gtdb_integration module")
    sys.exit(1)

# ANSI color codes
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def demo_taxonomy_parsing():
    """Demo GTDB taxonomy string parsing."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}DEMO 1: GTDB Taxonomy Parsing{Colors.RESET}\n")

    # Sample GTDB lineages
    samples = [
        "d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;o__Pseudomonadales;f__Pseudomonadaceae;g__Pseudomonas;s__Pseudomonas aeruginosa",
        "d__Bacteria;p__Bacillota;c__Bacilli;o__Bacillales;f__Bacillaceae;g__Bacillus;s__Bacillus subtilis",
        "d__Bacteria;p__Desulfobacterota;c__Desulfovibrionia;o__Desulfovibrionales;f__Desulfovibrionaceae;g__Desulfovibrio;s__Desulfovibrio vulgaris",
        "d__Archaea;p__Euryarchaeota;c__Methanomicrobia;o__Methanococcales;f__Methanococcaceae;g__Methanococcus;s__Methanococcus maripaludis"
    ]

    gtdb = GTDBIntegration(gtdb_data_dir="./gtdb_data", db_path=":memory:")

    for lineage in samples:
        taxonomy = gtdb.parse_gtdb_taxonomy(lineage)

        print(f"{Colors.BOLD}Species: {taxonomy.species}{Colors.RESET}")
        print(f"  Domain:  {taxonomy.domain}")
        print(f"  Phylum:  {taxonomy.phylum}")
        print(f"  Class:   {taxonomy.class_name}")
        print(f"  Order:   {taxonomy.order}")
        print(f"  Family:  {taxonomy.family}")
        print(f"  Genus:   {taxonomy.genus}")
        print()


def demo_nomenclature_comparison():
    """Demo NCBI vs GTDB nomenclature comparison."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}DEMO 2: NCBI vs GTDB Nomenclature Comparison{Colors.RESET}\n")

    # Known differences
    comparisons = [
        {
            'ncbi_name': 'Escherichia coli',
            'ncbi_phylum': 'Proteobacteria',
            'gtdb_lineage': 'd__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;o__Enterobacterales;f__Enterobacteriaceae;g__Escherichia;s__Escherichia coli',
            'expected_conflict': 'Phylum: Proteobacteria → Pseudomonadota'
        },
        {
            'ncbi_name': 'Bacillus subtilis',
            'ncbi_phylum': 'Firmicutes',
            'gtdb_lineage': 'd__Bacteria;p__Bacillota;c__Bacilli;o__Bacillales;f__Bacillaceae;g__Bacillus;s__Bacillus subtilis',
            'expected_conflict': 'Phylum: Firmicutes → Bacillota'
        },
        {
            'ncbi_name': 'Methylobacterium extorquens',
            'ncbi_genus': 'Methylobacterium',
            'gtdb_lineage': 'd__Bacteria;p__Pseudomonadota;c__Alphaproteobacteria;o__Hyphomicrobiales;f__Methylobacteriaceae;g__Methylorubrum;s__Methylorubrum extorquens',
            'expected_conflict': 'Genus: Methylobacterium → Methylorubrum'
        }
    ]

    gtdb = GTDBIntegration(gtdb_data_dir="./gtdb_data", db_path=":memory:")

    for comp in comparisons:
        ncbi_name = comp['ncbi_name']
        gtdb_lineage = comp['gtdb_lineage']

        taxonomy = gtdb.parse_gtdb_taxonomy(gtdb_lineage)

        print(f"{Colors.BOLD}Organism: {ncbi_name}{Colors.RESET}")
        print(f"{Colors.YELLOW}Expected Conflict: {comp['expected_conflict']}{Colors.RESET}")

        if 'ncbi_phylum' in comp:
            if comp['ncbi_phylum'] != taxonomy.phylum:
                print(f"{Colors.RED}  CONFLICT DETECTED:{Colors.RESET}")
                print(f"    NCBI Phylum:  {comp['ncbi_phylum']}")
                print(f"    GTDB Phylum:  {taxonomy.phylum}")
            else:
                print(f"{Colors.GREEN}  No phylum conflict{Colors.RESET}")

        if 'ncbi_genus' in comp:
            if comp['ncbi_genus'] != taxonomy.genus:
                print(f"{Colors.RED}  CONFLICT DETECTED:{Colors.RESET}")
                print(f"    NCBI Genus:   {comp['ncbi_genus']}")
                print(f"    GTDB Genus:   {taxonomy.genus}")
            else:
                print(f"{Colors.GREEN}  No genus conflict{Colors.RESET}")

        print()


def demo_phylum_updates():
    """Demo phylum nomenclature updates."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}DEMO 3: Phylum Nomenclature Updates{Colors.RESET}\n")

    updates = {
        'Proteobacteria': 'Pseudomonadota',
        'Firmicutes': 'Bacillota',
        'Actinobacteria': 'Actinomycetota',
        'Bacteroidetes': 'Bacteroidota',
        'Chloroflexi': 'Chloroflexota'
    }

    print(f"{Colors.BOLD}NCBI Phylum Name    →  GTDB Phylum Name{Colors.RESET}")
    print("-" * 60)
    for ncbi, gtdb in updates.items():
        print(f"{ncbi:20s} → {Colors.GREEN}{gtdb}{Colors.RESET}")

    print(f"\n{Colors.YELLOW}Note: GTDB uses updated nomenclature following the")
    print(f"International Code of Nomenclature of Prokaryotes.{Colors.RESET}\n")


def demo_example_organisms():
    """Demo GTDB classification for community organisms."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}DEMO 4: Example Organisms from CommunityMech{Colors.RESET}\n")

    # Sample organisms from our communities
    organisms = [
        {
            'name': 'Geobacter sulfurreducens',
            'gtdb_lineage': 'd__Bacteria;p__Pseudomonadota;c__Deltaproteobacteria;o__Desulfuromonadales;f__Geobacteraceae;g__Geobacter;s__Geobacter sulfurreducens'
        },
        {
            'name': 'Desulfovibrio vulgaris',
            'gtdb_lineage': 'd__Bacteria;p__Desulfobacterota;c__Desulfovibrionia;o__Desulfovibrionales;f__Desulfovibrionaceae;g__Desulfovibrio;s__Desulfovibrio vulgaris'
        },
        {
            'name': 'Methanococcus maripaludis',
            'gtdb_lineage': 'd__Archaea;p__Euryarchaeota;c__Methanomicrobia;o__Methanococcales;f__Methanococcaceae;g__Methanococcus;s__Methanococcus maripaludis'
        },
        {
            'name': 'Synechococcus elongatus',
            'gtdb_lineage': 'd__Bacteria;p__Cyanobacteriota;c__Cyanobacteriia;o__Synechococcales;f__Synechococcaceae;g__Synechococcus_C;s__Synechococcus elongatus'
        }
    ]

    gtdb = GTDBIntegration(gtdb_data_dir="./gtdb_data", db_path=":memory:")

    for org in organisms:
        taxonomy = gtdb.parse_gtdb_taxonomy(org['gtdb_lineage'])

        print(f"{Colors.BOLD}{org['name']}{Colors.RESET}")
        print(f"  Domain:  {taxonomy.domain}")
        print(f"  Phylum:  {Colors.GREEN}{taxonomy.phylum}{Colors.RESET}")
        print(f"  Class:   {taxonomy.class_name}")
        print(f"  Order:   {taxonomy.order}")
        print(f"  Family:  {taxonomy.family}")
        print(f"  Genus:   {taxonomy.genus}")
        print()


def demo_usage_examples():
    """Show usage examples."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}USAGE EXAMPLES{Colors.RESET}\n")

    examples = [
        {
            'title': 'Download GTDB Data',
            'command': 'python scripts/gtdb_integration.py --download',
            'description': 'Downloads ~500MB of GTDB taxonomy files'
        },
        {
            'title': 'Load into DuckDB',
            'command': 'python scripts/gtdb_integration.py --load',
            'description': 'Parses and loads ~85,000 genomes into database'
        },
        {
            'title': 'Search for Organism',
            'command': 'python scripts/gtdb_integration.py --search "Geobacter"',
            'description': 'Searches GTDB for matching organisms'
        },
        {
            'title': 'Generate Comparison Report',
            'command': 'python scripts/gtdb_integration.py --report',
            'description': 'Compares all community organisms against GTDB'
        },
        {
            'title': 'Validate with GTDB',
            'command': 'python scripts/compare_ncbi_gtdb_taxonomy.py --use-gtdb',
            'description': 'Validates YAMLs using both NCBI and GTDB'
        }
    ]

    for example in examples:
        print(f"{Colors.BOLD}{example['title']}{Colors.RESET}")
        print(f"  {Colors.CYAN}$ {example['command']}{Colors.RESET}")
        print(f"  {example['description']}")
        print()


def main():
    """Run all demos."""
    print(f"\n{Colors.BOLD}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}GTDB Integration Demo{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*70}{Colors.RESET}")

    demo_taxonomy_parsing()
    demo_nomenclature_comparison()
    demo_phylum_updates()
    demo_example_organisms()
    demo_usage_examples()

    print(f"\n{Colors.GREEN}{Colors.BOLD}Demo Complete!{Colors.RESET}")
    print(f"\n{Colors.YELLOW}To use GTDB with real data:{Colors.RESET}")
    print(f"  1. {Colors.CYAN}python scripts/gtdb_integration.py --download{Colors.RESET}")
    print(f"  2. {Colors.CYAN}python scripts/gtdb_integration.py --load{Colors.RESET}")
    print(f"  3. {Colors.CYAN}python scripts/gtdb_integration.py --report{Colors.RESET}")
    print(f"\n{Colors.YELLOW}See GTDB_INTEGRATION_GUIDE.md for full documentation.{Colors.RESET}\n")


if __name__ == '__main__':
    main()
