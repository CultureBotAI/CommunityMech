#!/usr/bin/env python3
"""
GTDB (Genome Taxonomy Database) Integration for CommunityMech

Provides comprehensive GTDB taxonomy lookup and NCBI comparison for microbial communities.
GTDB provides an alternative microbial taxonomy based on genome phylogeny.

Features:
- Download and load GTDB taxonomy files
- Parse GTDB lineage strings
- Search by species/genus in GTDB
- Compare GTDB vs NCBI taxonomic classifications
- Generate conflict reports

Data Source: https://gtdb.ecogenomic.org/
Latest Release: https://data.gtdb.ecogenomic.org/releases/latest/

Usage:
    # Download GTDB data (first time setup)
    python gtdb_integration.py --download

    # Load GTDB data into DuckDB
    python gtdb_integration.py --load

    # Search for organism
    python gtdb_integration.py --search "Desulfovibrio vulgaris"

    # Generate comparison reports
    python gtdb_integration.py --report
"""

import argparse
import csv
import gzip
import json
import re
import shutil
import sys
import time
import urllib.request
import yaml
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import duckdb
except ImportError:
    print("ERROR: duckdb not available. Install with: pip install duckdb")
    sys.exit(1)

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


@dataclass
class GTDBTaxonomy:
    """GTDB taxonomic classification"""
    genome_id: str
    domain: str
    phylum: str
    class_name: str  # 'class' is a Python keyword
    order: str
    family: str
    genus: str
    species: str
    full_lineage: str

    def to_dict(self):
        return asdict(self)


@dataclass
class GTDBMatch:
    """GTDB search result"""
    genome_id: str
    species: str
    genus: str
    taxonomy: GTDBTaxonomy
    confidence: str  # EXACT_SPECIES, GENUS_MATCH, FUZZY

    def to_dict(self):
        result = asdict(self)
        result['taxonomy'] = self.taxonomy.to_dict()
        return result


@dataclass
class NCBIGTDBComparison:
    """Comparison between NCBI and GTDB classifications"""
    organism_name: str
    ncbi_id: str
    ncbi_classification: Optional[Dict[str, str]]
    gtdb_matches: List[GTDBMatch]
    agreements: List[str]  # Ranks where they agree
    conflicts: List[Dict[str, any]]  # Ranks where they differ
    recommendation: str
    notes: str


class GTDBIntegration:
    """GTDB taxonomy integration system"""

    # GTDB release version
    GTDB_VERSION = "r214"
    GTDB_BASE_URL = "https://data.gtdb.ecogenomic.org/releases/release214/214.0/"

    def __init__(self,
                 gtdb_data_dir="./gtdb_data",
                 db_path="kgm_taxonomy.duckdb",
                 force_reload=False):
        """Initialize GTDB integration system."""
        self.gtdb_data_dir = Path(gtdb_data_dir)
        self.db_path = Path(db_path)
        self.conn = duckdb.connect(str(self.db_path))

        # Check if GTDB tables exist
        needs_loading = force_reload
        if not needs_loading:
            try:
                count = self.conn.execute("""
                    SELECT COUNT(*) FROM gtdb_taxonomy
                """).fetchone()[0]
                if count == 0:
                    needs_loading = True
            except:
                needs_loading = True

        if needs_loading and self.gtdb_data_dir.exists():
            self._load_gtdb_data()
        elif not needs_loading:
            try:
                count = self.conn.execute("SELECT COUNT(*) FROM gtdb_taxonomy").fetchone()[0]
                print(f"{Colors.GREEN}Using existing GTDB database with {count:,} genomes{Colors.RESET}")
            except:
                print(f"{Colors.YELLOW}GTDB data not loaded. Run with --load to load data.{Colors.RESET}")

    def download_gtdb_taxonomy(self, version=None):
        """
        Download GTDB taxonomy files.

        Files downloaded:
        - bac120_taxonomy_r214.tsv.gz (bacteria)
        - ar53_taxonomy_r214.tsv.gz (archaea)
        """
        if version is None:
            version = self.GTDB_VERSION

        print(f"\n{Colors.BOLD}{Colors.CYAN}Downloading GTDB Taxonomy ({version}){Colors.RESET}\n")

        # Create data directory
        self.gtdb_data_dir.mkdir(parents=True, exist_ok=True)

        # Files to download
        files = [
            f"bac120_taxonomy_{version}.tsv.gz",
            f"ar53_taxonomy_{version}.tsv.gz"
        ]

        base_url = self.GTDB_BASE_URL

        for file in files:
            url = base_url + file
            output_path = self.gtdb_data_dir / file

            print(f"{Colors.CYAN}Downloading {file}...{Colors.RESET}")
            print(f"  URL: {url}")

            try:
                # Download with progress
                def reporthook(blocknum, blocksize, totalsize):
                    readsofar = blocknum * blocksize
                    if totalsize > 0:
                        percent = readsofar * 1e2 / totalsize
                        s = f"\r  Progress: {percent:5.1f}% {readsofar:,} / {totalsize:,} bytes"
                        sys.stderr.write(s)
                        if readsofar >= totalsize:
                            sys.stderr.write("\n")
                    else:
                        sys.stderr.write(f"\r  Read: {readsofar:,} bytes")

                urllib.request.urlretrieve(url, output_path, reporthook)

                # Decompress
                print(f"{Colors.CYAN}  Decompressing...{Colors.RESET}")
                tsv_path = output_path.with_suffix('')
                with gzip.open(output_path, 'rb') as f_in:
                    with open(tsv_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)

                print(f"{Colors.GREEN}  Downloaded and decompressed: {tsv_path}{Colors.RESET}")

                # Remove compressed file to save space
                output_path.unlink()

            except Exception as e:
                print(f"{Colors.RED}  Error downloading {file}: {e}{Colors.RESET}")
                print(f"{Colors.YELLOW}  Please download manually from:{Colors.RESET}")
                print(f"{Colors.YELLOW}  {base_url}{Colors.RESET}")
                return False

        print(f"\n{Colors.GREEN}{Colors.BOLD}GTDB taxonomy downloaded successfully!{Colors.RESET}")
        print(f"{Colors.CYAN}Data location: {self.gtdb_data_dir}{Colors.RESET}\n")

        return True

    def parse_gtdb_taxonomy(self, lineage_string: str) -> GTDBTaxonomy:
        """
        Parse GTDB taxonomy string into structured object.

        Input: "d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;..."
        Output: GTDBTaxonomy object
        """
        ranks = ['domain', 'phylum', 'class', 'order', 'family', 'genus', 'species']
        parts = lineage_string.split(';')

        taxonomy_dict = {}
        for i, part in enumerate(parts):
            if i < len(ranks):
                # Remove rank prefix (d__, p__, c__, etc.)
                value = part.strip()
                if '__' in value:
                    value = value.split('__', 1)[1]

                rank_name = ranks[i]
                # Handle Python keyword 'class'
                if rank_name == 'class':
                    taxonomy_dict['class_name'] = value
                else:
                    taxonomy_dict[rank_name] = value

        # Extract genome ID from first part if present
        genome_id = ""
        if parts and '__' in parts[0]:
            genome_id = parts[0].split('__')[0]

        return GTDBTaxonomy(
            genome_id=genome_id,
            domain=taxonomy_dict.get('domain', ''),
            phylum=taxonomy_dict.get('phylum', ''),
            class_name=taxonomy_dict.get('class_name', ''),
            order=taxonomy_dict.get('order', ''),
            family=taxonomy_dict.get('family', ''),
            genus=taxonomy_dict.get('genus', ''),
            species=taxonomy_dict.get('species', ''),
            full_lineage=lineage_string
        )

    def _load_gtdb_data(self):
        """Load GTDB taxonomy from TSV files into DuckDB."""
        print(f"\n{Colors.CYAN}Loading GTDB data into DuckDB...{Colors.RESET}")
        start_time = time.time()

        bac_file = self.gtdb_data_dir / f"bac120_taxonomy_{self.GTDB_VERSION}.tsv"
        ar_file = self.gtdb_data_dir / f"ar53_taxonomy_{self.GTDB_VERSION}.tsv"

        # Check if files exist
        if not bac_file.exists() and not ar_file.exists():
            print(f"{Colors.RED}ERROR: GTDB taxonomy files not found in {self.gtdb_data_dir}{Colors.RESET}")
            print(f"{Colors.YELLOW}Run with --download to download GTDB data{Colors.RESET}")
            return False

        # Drop existing tables
        self.conn.execute("DROP TABLE IF EXISTS gtdb_bacteria")
        self.conn.execute("DROP TABLE IF EXISTS gtdb_archaea")
        self.conn.execute("DROP TABLE IF EXISTS gtdb_taxonomy")

        # Load bacteria taxonomy
        if bac_file.exists():
            print(f"  Loading bacteria taxonomy from: {bac_file}")
            self.conn.execute(f"""
                CREATE TABLE gtdb_bacteria AS
                SELECT
                    column0 as genome_id,
                    column1 as taxonomy
                FROM read_csv(
                    '{bac_file}',
                    delim='\t',
                    header=false,
                    columns={{'column0': 'VARCHAR', 'column1': 'VARCHAR'}}
                )
            """)

            bac_count = self.conn.execute("SELECT COUNT(*) FROM gtdb_bacteria").fetchone()[0]
            print(f"{Colors.GREEN}    Loaded {bac_count:,} bacterial genomes{Colors.RESET}")

        # Load archaea taxonomy
        if ar_file.exists():
            print(f"  Loading archaea taxonomy from: {ar_file}")
            self.conn.execute(f"""
                CREATE TABLE gtdb_archaea AS
                SELECT
                    column0 as genome_id,
                    column1 as taxonomy
                FROM read_csv(
                    '{ar_file}',
                    delim='\t',
                    header=false,
                    columns={{'column0': 'VARCHAR', 'column1': 'VARCHAR'}}
                )
            """)

            ar_count = self.conn.execute("SELECT COUNT(*) FROM gtdb_archaea").fetchone()[0]
            print(f"{Colors.GREEN}    Loaded {ar_count:,} archaeal genomes{Colors.RESET}")

        # Create unified view
        print(f"  Creating unified taxonomy view...")
        self.conn.execute("""
            CREATE TABLE gtdb_taxonomy AS
            SELECT * FROM gtdb_bacteria
            UNION ALL
            SELECT * FROM gtdb_archaea
        """)

        # Parse taxonomy strings into structured columns
        print(f"  Parsing taxonomy strings...")
        self.conn.execute("""
            ALTER TABLE gtdb_taxonomy ADD COLUMN domain VARCHAR
        """)
        self.conn.execute("""
            ALTER TABLE gtdb_taxonomy ADD COLUMN phylum VARCHAR
        """)
        self.conn.execute("""
            ALTER TABLE gtdb_taxonomy ADD COLUMN class VARCHAR
        """)
        self.conn.execute("""
            ALTER TABLE gtdb_taxonomy ADD COLUMN "order" VARCHAR
        """)
        self.conn.execute("""
            ALTER TABLE gtdb_taxonomy ADD COLUMN family VARCHAR
        """)
        self.conn.execute("""
            ALTER TABLE gtdb_taxonomy ADD COLUMN genus VARCHAR
        """)
        self.conn.execute("""
            ALTER TABLE gtdb_taxonomy ADD COLUMN species VARCHAR
        """)

        # Extract taxonomic ranks using SQL string functions
        self.conn.execute("""
            UPDATE gtdb_taxonomy SET
                domain = TRIM(SPLIT_PART(SPLIT_PART(taxonomy, ';', 1), '__', 2)),
                phylum = TRIM(SPLIT_PART(SPLIT_PART(taxonomy, ';', 2), '__', 2)),
                class = TRIM(SPLIT_PART(SPLIT_PART(taxonomy, ';', 3), '__', 2)),
                "order" = TRIM(SPLIT_PART(SPLIT_PART(taxonomy, ';', 4), '__', 2)),
                family = TRIM(SPLIT_PART(SPLIT_PART(taxonomy, ';', 5), '__', 2)),
                genus = TRIM(SPLIT_PART(SPLIT_PART(taxonomy, ';', 6), '__', 2)),
                species = TRIM(SPLIT_PART(SPLIT_PART(taxonomy, ';', 7), '__', 2))
        """)

        # Create indexes for fast lookup
        print(f"  Creating indexes...")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_gtdb_genome ON gtdb_taxonomy(genome_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_gtdb_species ON gtdb_taxonomy(species)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_gtdb_genus ON gtdb_taxonomy(genus)")

        total_count = self.conn.execute("SELECT COUNT(*) FROM gtdb_taxonomy").fetchone()[0]
        elapsed = time.time() - start_time

        print(f"{Colors.GREEN}{Colors.BOLD}Loaded {total_count:,} GTDB genomes in {elapsed:.1f} seconds{Colors.RESET}\n")

        return True

    def search_by_species(self, species_name: str, limit=100) -> List[GTDBMatch]:
        """
        Search GTDB for a species name.

        Returns all genome assemblies with matching species designation.
        """
        try:
            results = self.conn.execute("""
                SELECT genome_id, species, genus, taxonomy
                FROM gtdb_taxonomy
                WHERE species = ?
                LIMIT ?
            """, [species_name, limit]).fetchall()

            matches = []
            for row in results:
                taxonomy = self.parse_gtdb_taxonomy(row[3])
                taxonomy.genome_id = row[0]

                matches.append(GTDBMatch(
                    genome_id=row[0],
                    species=row[1],
                    genus=row[2],
                    taxonomy=taxonomy,
                    confidence='EXACT_SPECIES'
                ))

            return matches
        except Exception as e:
            print(f"{Colors.RED}Error searching GTDB: {e}{Colors.RESET}")
            return []

    def search_by_genus(self, genus_name: str, limit=100) -> List[GTDBMatch]:
        """
        Search GTDB for all species in a genus.
        """
        try:
            results = self.conn.execute("""
                SELECT genome_id, species, genus, taxonomy
                FROM gtdb_taxonomy
                WHERE genus = ?
                LIMIT ?
            """, [genus_name, limit]).fetchall()

            matches = []
            for row in results:
                taxonomy = self.parse_gtdb_taxonomy(row[3])
                taxonomy.genome_id = row[0]

                matches.append(GTDBMatch(
                    genome_id=row[0],
                    species=row[1],
                    genus=row[2],
                    taxonomy=taxonomy,
                    confidence='GENUS_MATCH'
                ))

            return matches
        except Exception as e:
            print(f"{Colors.RED}Error searching GTDB: {e}{Colors.RESET}")
            return []

    def search_fuzzy(self, organism_name: str, limit=10) -> List[GTDBMatch]:
        """
        Fuzzy search across GTDB taxonomy.

        Tries:
        1. Exact species match
        2. Genus match (first word of organism name)
        3. Fuzzy species match
        """
        matches = []

        # Try exact species match
        exact_matches = self.search_by_species(organism_name, limit=limit)
        if exact_matches:
            return exact_matches[:limit]

        # Extract genus (first word)
        words = organism_name.split()
        if words:
            genus = words[0]
            genus_matches = self.search_by_genus(genus, limit=limit)
            matches.extend(genus_matches)

        # Try fuzzy match on species
        if len(matches) < limit:
            try:
                results = self.conn.execute("""
                    SELECT genome_id, species, genus, taxonomy
                    FROM gtdb_taxonomy
                    WHERE species LIKE ?
                    ORDER BY LENGTH(species)
                    LIMIT ?
                """, [f"%{organism_name}%", limit - len(matches)]).fetchall()

                for row in results:
                    taxonomy = self.parse_gtdb_taxonomy(row[3])
                    taxonomy.genome_id = row[0]

                    matches.append(GTDBMatch(
                        genome_id=row[0],
                        species=row[1],
                        genus=row[2],
                        taxonomy=taxonomy,
                        confidence='FUZZY'
                    ))
            except Exception as e:
                print(f"{Colors.RED}Error in fuzzy search: {e}{Colors.RESET}")

        return matches[:limit]

    def get_species_representatives(self, organism_name: str) -> List[GTDBMatch]:
        """
        Get representative genomes for a species.

        Returns genomes that match the species name, prioritizing:
        1. Reference genomes (GCF prefix)
        2. Representative genomes
        """
        matches = self.search_by_species(organism_name, limit=1000)

        # Sort by genome ID to prioritize reference genomes
        # GCF = GenBank RefSeq (reference), GCA = GenBank (non-reference)
        matches.sort(key=lambda m: (
            0 if m.genome_id.startswith('GCF_') else 1,
            m.genome_id
        ))

        return matches

    def compare_ncbi_gtdb_nomenclature(self,
                                       ncbi_name: str,
                                       gtdb_matches: List[GTDBMatch]) -> Dict[str, any]:
        """
        Compare NCBI and GTDB nomenclature for an organism.

        Identifies:
        - Phylum name changes (Proteobacteria -> Pseudomonadota)
        - Species reclassifications
        - Genus transfers
        """
        if not gtdb_matches:
            return {
                'has_conflicts': False,
                'conflicts': [],
                'notes': 'Not found in GTDB'
            }

        # Use first match as representative
        gtdb_match = gtdb_matches[0]
        gtdb_tax = gtdb_match.taxonomy

        conflicts = []

        # Extract NCBI genus and species from name
        ncbi_parts = ncbi_name.split()
        ncbi_genus = ncbi_parts[0] if ncbi_parts else ''
        ncbi_species_epithet = ncbi_parts[1] if len(ncbi_parts) > 1 else ''

        # Compare genus
        if ncbi_genus and gtdb_tax.genus and ncbi_genus != gtdb_tax.genus:
            conflicts.append({
                'rank': 'genus',
                'ncbi': ncbi_genus,
                'gtdb': gtdb_tax.genus,
                'type': 'GENUS_TRANSFER',
                'note': f"Organism transferred from {ncbi_genus} to {gtdb_tax.genus} in GTDB"
            })

        # Compare species epithet
        gtdb_species_parts = gtdb_tax.species.split()
        gtdb_species_epithet = gtdb_species_parts[1] if len(gtdb_species_parts) > 1 else ''

        if ncbi_species_epithet and gtdb_species_epithet and ncbi_species_epithet != gtdb_species_epithet:
            conflicts.append({
                'rank': 'species',
                'ncbi': f"{ncbi_genus} {ncbi_species_epithet}",
                'gtdb': gtdb_tax.species,
                'type': 'SPECIES_RECLASSIFICATION',
                'note': f"Species name differs between NCBI and GTDB"
            })

        # Check for known phylum nomenclature updates
        phylum_updates = {
            'Proteobacteria': 'Pseudomonadota',
            'Firmicutes': 'Bacillota',
            'Actinobacteria': 'Actinomycetota',
            'Bacteroidetes': 'Bacteroidota',
            'Chloroflexi': 'Chloroflexota'
        }

        for old_name, new_name in phylum_updates.items():
            if gtdb_tax.phylum == new_name:
                conflicts.append({
                    'rank': 'phylum',
                    'ncbi': old_name,
                    'gtdb': new_name,
                    'type': 'NOMENCLATURE_UPDATE',
                    'note': f"GTDB uses updated phylum nomenclature: {old_name} -> {new_name}"
                })

        return {
            'has_conflicts': len(conflicts) > 0,
            'conflicts': conflicts,
            'gtdb_taxonomy': gtdb_tax.to_dict()
        }

    def collect_all_taxa(self, yaml_dir: Path) -> List[Dict]:
        """Collect all taxa from YAML files."""
        all_taxa = []

        if not yaml_dir.exists():
            print(f"{Colors.RED}Error: Directory not found: {yaml_dir}{Colors.RESET}")
            return all_taxa

        yaml_files = list(yaml_dir.glob('*.yaml')) + list(yaml_dir.glob('*.yml'))

        print(f"{Colors.CYAN}Scanning {len(yaml_files)} YAML files...{Colors.RESET}")

        for yaml_file in yaml_files:
            try:
                with open(yaml_file, 'r') as f:
                    data = yaml.safe_load(f)

                if not data or 'taxonomy' not in data:
                    continue

                for taxon_entry in data['taxonomy']:
                    if 'taxon_term' not in taxon_entry:
                        continue

                    taxon_term = taxon_entry['taxon_term']
                    preferred_term = taxon_term.get('preferred_term', '')
                    notes = taxon_term.get('notes', '')
                    term_info = taxon_term.get('term', {})
                    ncbi_id = term_info.get('id', '')
                    ncbi_label = term_info.get('label', '')

                    if preferred_term and ncbi_id:
                        # Clean up NCBI ID
                        if ':' in ncbi_id:
                            ncbi_id = ncbi_id.split(':', 1)[1]

                        all_taxa.append({
                            'preferred_term': preferred_term,
                            'ncbi_id': ncbi_id,
                            'ncbi_label': ncbi_label,
                            'file_path': str(yaml_file),
                            'file_name': yaml_file.name,
                            'notes': notes
                        })
            except Exception as e:
                print(f"{Colors.RED}Error reading {yaml_file}: {e}{Colors.RESET}")

        print(f"{Colors.GREEN}Found {len(all_taxa)} taxa entries{Colors.RESET}\n")
        return all_taxa

    def generate_comparison_report(self,
                                   yaml_dir: Path,
                                   output_dir: Path = Path("./")):
        """
        Generate comprehensive GTDB vs NCBI comparison report.

        Outputs:
        - gtdb_ncbi_comparison.tsv: Side-by-side comparison
        - gtdb_conflicts.txt: Cases where GTDB differs from NCBI
        - gtdb_coverage_report.txt: Coverage statistics
        - gtdb_nomenclature_updates.txt: GTDB's updated names
        """
        output_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{Colors.BOLD}{Colors.CYAN}Generating GTDB vs NCBI Comparison Report{Colors.RESET}\n")

        # Collect taxa
        all_taxa = self.collect_all_taxa(yaml_dir)

        # Statistics
        stats = {
            'total_taxa': len(all_taxa),
            'in_gtdb': 0,
            'not_in_gtdb': 0,
            'genus_transfers': 0,
            'species_reclassifications': 0,
            'phylum_updates': 0,
            'nomenclature_conflicts': []
        }

        # Results storage
        all_results = []

        # Process each taxon
        print(f"{Colors.CYAN}Comparing {len(all_taxa)} taxa against GTDB...{Colors.RESET}")
        for i, taxon in enumerate(all_taxa, 1):
            if i % 25 == 0:
                print(f"  Progress: {i}/{len(all_taxa)}")

            preferred_term = taxon['preferred_term']

            # Search GTDB
            gtdb_matches = self.search_fuzzy(preferred_term, limit=5)

            if gtdb_matches:
                stats['in_gtdb'] += 1
            else:
                stats['not_in_gtdb'] += 1

            # Compare nomenclature
            comparison = self.compare_ncbi_gtdb_nomenclature(preferred_term, gtdb_matches)

            # Count conflict types
            if comparison.get('has_conflicts'):
                for conflict in comparison['conflicts']:
                    if conflict['type'] == 'GENUS_TRANSFER':
                        stats['genus_transfers'] += 1
                    elif conflict['type'] == 'SPECIES_RECLASSIFICATION':
                        stats['species_reclassifications'] += 1
                    elif conflict['type'] == 'NOMENCLATURE_UPDATE':
                        stats['phylum_updates'] += 1

                stats['nomenclature_conflicts'].append({
                    'organism': preferred_term,
                    'conflicts': comparison['conflicts']
                })

            # Store result
            all_results.append({
                'taxon': taxon,
                'gtdb_matches': gtdb_matches,
                'comparison': comparison
            })

        print(f"{Colors.GREEN}Comparison complete!{Colors.RESET}\n")

        # Write reports
        self._write_comparison_tsv(all_results, output_dir / 'gtdb_ncbi_comparison.tsv')
        self._write_conflicts_report(stats, output_dir / 'gtdb_conflicts.txt')
        self._write_coverage_report(stats, all_results, output_dir / 'gtdb_coverage_report.txt')
        self._write_nomenclature_updates(stats, output_dir / 'gtdb_nomenclature_updates.txt')

        # Print summary
        print(f"\n{Colors.BOLD}{Colors.CYAN}GTDB COVERAGE SUMMARY{Colors.RESET}")
        print(f"{Colors.GREEN}Taxa in GTDB: {stats['in_gtdb']}/{stats['total_taxa']} ({stats['in_gtdb']/stats['total_taxa']*100:.1f}%){Colors.RESET}")
        print(f"{Colors.YELLOW}Not in GTDB: {stats['not_in_gtdb']}/{stats['total_taxa']} ({stats['not_in_gtdb']/stats['total_taxa']*100:.1f}%){Colors.RESET}")
        print(f"\n{Colors.BOLD}{Colors.CYAN}NOMENCLATURE DIFFERENCES{Colors.RESET}")
        print(f"Genus transfers: {stats['genus_transfers']}")
        print(f"Species reclassifications: {stats['species_reclassifications']}")
        print(f"Phylum nomenclature updates: {stats['phylum_updates']}")
        print()

        return stats

    def _write_comparison_tsv(self, results: List[Dict], output_file: Path):
        """Write side-by-side NCBI vs GTDB comparison TSV."""
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow([
                'file', 'preferred_term', 'ncbi_id', 'in_gtdb',
                'gtdb_genome_count', 'gtdb_species', 'gtdb_genus',
                'gtdb_domain', 'gtdb_phylum', 'gtdb_class', 'gtdb_order', 'gtdb_family',
                'has_conflicts', 'conflict_types'
            ])

            for result in results:
                taxon = result['taxon']
                gtdb_matches = result['gtdb_matches']
                comparison = result['comparison']

                in_gtdb = 'YES' if gtdb_matches else 'NO'
                genome_count = len(gtdb_matches)

                if gtdb_matches:
                    first_match = gtdb_matches[0]
                    gtdb_tax = first_match.taxonomy

                    conflict_types = []
                    if comparison.get('has_conflicts'):
                        conflict_types = [c['type'] for c in comparison['conflicts']]

                    writer.writerow([
                        taxon['file_name'],
                        taxon['preferred_term'],
                        taxon['ncbi_id'],
                        in_gtdb,
                        genome_count,
                        gtdb_tax.species,
                        gtdb_tax.genus,
                        gtdb_tax.domain,
                        gtdb_tax.phylum,
                        gtdb_tax.class_name,
                        gtdb_tax.order,
                        gtdb_tax.family,
                        'YES' if comparison.get('has_conflicts') else 'NO',
                        '|'.join(conflict_types)
                    ])
                else:
                    writer.writerow([
                        taxon['file_name'],
                        taxon['preferred_term'],
                        taxon['ncbi_id'],
                        in_gtdb,
                        0,
                        '', '', '', '', '', '', '',
                        'NO',
                        ''
                    ])

        print(f"{Colors.GREEN}Written: {output_file}{Colors.RESET}")

    def _write_conflicts_report(self, stats: Dict, output_file: Path):
        """Write detailed conflicts report."""
        with open(output_file, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("GTDB vs NCBI NOMENCLATURE CONFLICTS\n")
            f.write("=" * 80 + "\n\n")

            f.write("SUMMARY\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total organisms with conflicts: {len(stats['nomenclature_conflicts'])}\n")
            f.write(f"Genus transfers: {stats['genus_transfers']}\n")
            f.write(f"Species reclassifications: {stats['species_reclassifications']}\n")
            f.write(f"Phylum nomenclature updates: {stats['phylum_updates']}\n\n")

            if stats['nomenclature_conflicts']:
                f.write("DETAILED CONFLICTS\n")
                f.write("=" * 80 + "\n\n")

                for entry in stats['nomenclature_conflicts']:
                    f.write(f"Organism: {entry['organism']}\n")
                    f.write(f"Conflicts:\n")
                    for conflict in entry['conflicts']:
                        f.write(f"  - {conflict['rank'].upper()}: ")
                        f.write(f"NCBI='{conflict['ncbi']}' -> GTDB='{conflict['gtdb']}'\n")
                        f.write(f"    Type: {conflict['type']}\n")
                        f.write(f"    Note: {conflict['note']}\n")
                    f.write("\n")

        print(f"{Colors.GREEN}Written: {output_file}{Colors.RESET}")

    def _write_coverage_report(self, stats: Dict, results: List[Dict], output_file: Path):
        """Write GTDB coverage statistics."""
        with open(output_file, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("GTDB COVERAGE REPORT\n")
            f.write("=" * 80 + "\n\n")

            f.write("OVERALL STATISTICS\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total taxa analyzed: {stats['total_taxa']}\n")
            f.write(f"Found in GTDB: {stats['in_gtdb']} ({stats['in_gtdb']/stats['total_taxa']*100:.1f}%)\n")
            f.write(f"Not in GTDB: {stats['not_in_gtdb']} ({stats['not_in_gtdb']/stats['total_taxa']*100:.1f}%)\n\n")

            # List organisms not in GTDB
            not_found = [r for r in results if not r['gtdb_matches']]
            if not_found:
                f.write("ORGANISMS NOT FOUND IN GTDB\n")
                f.write("=" * 80 + "\n\n")
                for result in not_found:
                    taxon = result['taxon']
                    f.write(f"  {taxon['preferred_term']}\n")
                    f.write(f"    NCBI ID: NCBITaxon:{taxon['ncbi_id']}\n")
                    f.write(f"    File: {taxon['file_name']}\n\n")

        print(f"{Colors.GREEN}Written: {output_file}{Colors.RESET}")

    def _write_nomenclature_updates(self, stats: Dict, output_file: Path):
        """Write GTDB nomenclature updates."""
        with open(output_file, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("GTDB NOMENCLATURE UPDATES\n")
            f.write("=" * 80 + "\n\n")

            f.write("These are the updated taxonomic names used by GTDB based on\n")
            f.write("genome phylogeny and the principle of phylogenetic consistency.\n\n")

            f.write("PHYLUM-LEVEL UPDATES\n")
            f.write("-" * 80 + "\n")
            f.write("NCBI Name              -> GTDB Name\n")
            f.write("-" * 80 + "\n")
            f.write("Proteobacteria         -> Pseudomonadota\n")
            f.write("Firmicutes             -> Bacillota\n")
            f.write("Actinobacteria         -> Actinomycetota\n")
            f.write("Bacteroidetes          -> Bacteroidota\n")
            f.write("Chloroflexi            -> Chloroflexota\n\n")

            f.write("GENUS/SPECIES TRANSFERS\n")
            f.write("-" * 80 + "\n")

            # Group by type
            genus_transfers = [c for c in stats['nomenclature_conflicts']
                              if any(conf['type'] == 'GENUS_TRANSFER' for conf in c['conflicts'])]

            for entry in genus_transfers:
                for conflict in entry['conflicts']:
                    if conflict['type'] == 'GENUS_TRANSFER':
                        f.write(f"{conflict['ncbi']} -> {conflict['gtdb']}\n")
                        f.write(f"  Organism: {entry['organism']}\n")
                        f.write(f"  Note: {conflict['note']}\n\n")

        print(f"{Colors.GREEN}Written: {output_file}{Colors.RESET}")


def main():
    parser = argparse.ArgumentParser(
        description='GTDB (Genome Taxonomy Database) Integration for CommunityMech'
    )
    parser.add_argument(
        '--download',
        action='store_true',
        help='Download GTDB taxonomy files'
    )
    parser.add_argument(
        '--load',
        action='store_true',
        help='Load GTDB data into DuckDB'
    )
    parser.add_argument(
        '--search',
        type=str,
        help='Search for organism in GTDB'
    )
    parser.add_argument(
        '--report',
        action='store_true',
        help='Generate GTDB vs NCBI comparison report'
    )
    parser.add_argument(
        '--gtdb-dir',
        type=Path,
        default=Path('./gtdb_data'),
        help='GTDB data directory (default: ./gtdb_data)'
    )
    parser.add_argument(
        '--db-path',
        type=Path,
        default=Path('kgm_taxonomy.duckdb'),
        help='DuckDB database path (default: kgm_taxonomy.duckdb)'
    )
    parser.add_argument(
        '--yaml-dir',
        type=Path,
        default=Path(__file__).parent.parent / 'kb' / 'communities',
        help='YAML communities directory'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('./'),
        help='Output directory for reports'
    )

    args = parser.parse_args()

    print(f"\n{Colors.BOLD}{Colors.CYAN}GTDB Integration System{Colors.RESET}\n")

    # Initialize GTDB integration
    gtdb = GTDBIntegration(
        gtdb_data_dir=args.gtdb_dir,
        db_path=args.db_path,
        force_reload=args.load
    )

    # Download GTDB data
    if args.download:
        success = gtdb.download_gtdb_taxonomy()
        if success:
            print(f"\n{Colors.CYAN}Run with --load to load data into DuckDB{Colors.RESET}\n")

    # Load data
    if args.load:
        gtdb._load_gtdb_data()

    # Search
    if args.search:
        print(f"\n{Colors.CYAN}Searching GTDB for: {args.search}{Colors.RESET}\n")
        matches = gtdb.search_fuzzy(args.search, limit=10)

        if not matches:
            print(f"{Colors.RED}No matches found{Colors.RESET}")
        else:
            print(f"{Colors.GREEN}Found {len(matches)} match(es):{Colors.RESET}\n")
            for i, match in enumerate(matches, 1):
                print(f"{i}. {Colors.BOLD}{match.species}{Colors.RESET}")
                print(f"   Genome: {match.genome_id}")
                print(f"   Genus: {match.genus}")
                print(f"   Phylum: {match.taxonomy.phylum}")
                print(f"   Confidence: {match.confidence}")
                print(f"   Full lineage: {match.taxonomy.full_lineage}")
                print()

    # Generate report
    if args.report:
        gtdb.generate_comparison_report(
            yaml_dir=args.yaml_dir,
            output_dir=args.output_dir
        )

    print(f"\n{Colors.GREEN}Done!{Colors.RESET}\n")


if __name__ == '__main__':
    main()
