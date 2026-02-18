#!/usr/bin/env env python3
"""
Phase 2: Data Enhancement - Extract and populate strain designations

Strategy:
1. Parse YAML files for strain mentions (DSM, ATCC, PCC, etc.)
2. Query kg-microbe DuckDB for strain metadata
3. Query BacDive API for DSM strains
4. Query ATCC catalog
5. Extract from literature evidence snippets
6. Generate structured strain_designation YAML
7. Update YAML files with new data

Sources (in priority order):
1. Literature evidence snippets (highest priority - source of truth)
2. kg-microbe DuckDB (851K organisms, includes strains)
3. BacDive API (DSM strains, culture conditions)
4. ATCC catalog (type strains, genome links)
"""

import re
import yaml
import duckdb
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
import requests
import time
from collections import defaultdict

# Color codes for output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

@dataclass
class CultureCollectionID:
    """Culture collection identifier"""
    collection: str  # ATCC, DSM, JCM, PCC, etc.
    accession: str   # Accession number
    url: Optional[str] = None
    notes: Optional[str] = None

@dataclass
class StrainInfo:
    """Complete strain designation information"""
    strain_name: Optional[str] = None
    culture_collections: List[CultureCollectionID] = field(default_factory=list)
    type_strain: Optional[bool] = None
    genome_accession: Optional[str] = None
    genome_url: Optional[str] = None
    genetic_modification: Optional[str] = None
    isolation_source: Optional[str] = None
    notes: Optional[str] = None
    sources: Set[str] = field(default_factory=set)  # Track where info came from

# Culture collection patterns
COLLECTION_PATTERNS = {
    'DSM': r'\bDSM[:\s-]?(\d+)',
    'ATCC': r'\bATCC[:\s-]?(\d+)',
    'JCM': r'\bJCM[:\s-]?(\d+)',
    'PCC': r'\bPCC[:\s-]?(\d+)',
    'NCTC': r'\bNCTC[:\s-]?(\d+)',
    'CCUG': r'\bCCUG[:\s-]?(\d+)',
    'NCIMB': r'\bNCIMB[:\s-]?(\d+)',
    'LMG': r'\bLMG[:\s-]?(\d+)',
    'KCTC': r'\bKCTC[:\s-]?(\d+)',
    'CIP': r'\bCIP[:\s-]?(\d+)',
    'NBRC': r'\bNBRC[:\s-]?(\d+)',
    'VKM': r'\bVKM[:\s-]?(\d+)',
}

# Genome accession patterns
GENOME_PATTERNS = [
    r'\b(GCF_\d{9}\.\d+)',  # RefSeq
    r'\b(GCA_\d{9}\.\d+)',  # GenBank
]

# Culture collection URLs
COLLECTION_URLS = {
    'DSM': 'https://www.dsmz.de/collection/catalogue/details/culture/DSM-{accession}',
    'ATCC': 'https://www.atcc.org/products/{accession}',
    'JCM': 'https://jcm.brc.riken.jp/cgi-bin/jcm/jcm_number?JCM={accession}',
    'PCC': 'https://pcc.pasteur.fr/pcc-catalogue/products-page/pcc-{accession}',
    'NCTC': 'https://www.culturecollections.org.uk/nctc/strains/nctc-{accession}.html',
    'NCIMB': 'https://www.ncimb.com/products/search/details?id=NCIMB%20{accession}',
}

NCBI_ASSEMBLY_URL = 'https://www.ncbi.nlm.nih.gov/assembly/{accession}'

class StrainExtractor:
    """Extract strain information from multiple sources"""

    def __init__(self, kb_dir: Path, kgm_db_path: Path):
        self.kb_dir = kb_dir
        self.kgm_db_path = kgm_db_path
        self.conn = None
        self.stats = defaultdict(int)

    def connect_kgm(self):
        """Connect to kg-microbe DuckDB"""
        print(f"{Colors.CYAN}Connecting to kg-microbe DuckDB...{Colors.RESET}")
        self.conn = duckdb.connect(str(self.kgm_db_path), read_only=True)
        # Test connection
        count = self.conn.execute("SELECT COUNT(*) FROM ncbitaxon").fetchone()[0]
        print(f"{Colors.GREEN}✓{Colors.RESET} Connected: {count:,} taxonomy records available")

    def extract_from_text(self, text: str) -> Tuple[List[CultureCollectionID], List[str]]:
        """Extract culture collection IDs and genome accessions from text"""
        collections = []
        genomes = []

        # Extract culture collections
        for coll_name, pattern in COLLECTION_PATTERNS.items():
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                accession = match.group(1)
                url = COLLECTION_URLS.get(coll_name)
                if url:
                    url = url.format(accession=accession)
                collections.append(CultureCollectionID(
                    collection=coll_name,
                    accession=accession,
                    url=url
                ))

        # Extract genome accessions
        for pattern in GENOME_PATTERNS:
            matches = re.finditer(pattern, text)
            for match in matches:
                genomes.append(match.group(1))

        return collections, genomes

    def query_kgm_by_name(self, organism_name: str) -> Optional[Dict]:
        """Query kg-microbe by organism name"""
        if not self.conn:
            return None

        # Try exact match first (using indexed name_lower)
        query = """
        SELECT id, name, category, provided_by
        FROM ncbitaxon
        WHERE name_lower = LOWER(?)
        LIMIT 1
        """
        result = self.conn.execute(query, [organism_name]).fetchone()

        if result:
            return {
                'id': result[0],
                'name': result[1],
                'category': result[2],
                'provided_by': result[3]
            }

        # Try fuzzy match (contains)
        query = """
        SELECT id, name, category, provided_by
        FROM ncbitaxon
        WHERE name_lower LIKE '%' || LOWER(?) || '%'
        LIMIT 5
        """
        results = self.conn.execute(query, [organism_name]).fetchall()

        if results:
            # Return first result with highest confidence
            return {
                'id': results[0][0],
                'name': results[0][1],
                'category': results[0][2],
                'provided_by': results[0][3],
                'fuzzy': True,
                'alternatives': len(results)
            }

        return None

    def extract_strain_from_yaml(self, yaml_path: Path) -> Dict[str, StrainInfo]:
        """Extract strain information from a single YAML file"""
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        strain_data = {}

        if 'taxonomy' not in data:
            return strain_data

        for taxon_entry in data['taxonomy']:
            if 'taxon_term' not in taxon_entry:
                continue

            taxon = taxon_entry['taxon_term']
            preferred_term = taxon.get('preferred_term', '')
            notes = taxon.get('notes', '')

            strain_info = StrainInfo()

            # Extract from preferred_term
            collections, genomes = self.extract_from_text(preferred_term)
            strain_info.culture_collections.extend(collections)
            if collections:
                strain_info.sources.add('preferred_term')

            if genomes:
                strain_info.genome_accession = genomes[0]
                strain_info.genome_url = NCBI_ASSEMBLY_URL.format(accession=genomes[0])
                strain_info.sources.add('preferred_term')

            # Extract from notes
            if notes:
                collections, genomes = self.extract_from_text(notes)
                strain_info.culture_collections.extend(collections)
                if collections or genomes:
                    strain_info.sources.add('notes')

                if genomes and not strain_info.genome_accession:
                    strain_info.genome_accession = genomes[0]
                    strain_info.genome_url = NCBI_ASSEMBLY_URL.format(accession=genomes[0])

            # Extract from evidence snippets
            if 'evidence' in taxon_entry:
                for evidence in taxon_entry['evidence']:
                    snippet = evidence.get('snippet', '')
                    if snippet:
                        collections, genomes = self.extract_from_text(snippet)
                        strain_info.culture_collections.extend(collections)
                        if collections or genomes:
                            strain_info.sources.add('evidence')

                        if genomes and not strain_info.genome_accession:
                            strain_info.genome_accession = genomes[0]
                            strain_info.genome_url = NCBI_ASSEMBLY_URL.format(accession=genomes[0])

            # Extract strain name from preferred_term
            # Look for patterns like "DSM 8584" or "strain PCC 7942"
            strain_match = re.search(r'strain\s+([A-Z0-9\s-]+)', preferred_term, re.IGNORECASE)
            if strain_match:
                strain_info.strain_name = strain_match.group(1).strip()
            elif strain_info.culture_collections:
                # Use first collection ID as strain name
                first_coll = strain_info.culture_collections[0]
                strain_info.strain_name = f"{first_coll.collection} {first_coll.accession}"

            # Query kg-microbe for additional info
            kgm_result = self.query_kgm_by_name(preferred_term)
            if kgm_result:
                strain_info.sources.add('kg-microbe')
                # Extract strain info from kg-microbe ID if it contains strain designation
                kgm_id = kgm_result.get('id', '')
                collections, genomes = self.extract_from_text(kgm_id)
                strain_info.culture_collections.extend(collections)

            # Deduplicate culture collections
            seen = set()
            unique_collections = []
            for coll in strain_info.culture_collections:
                key = (coll.collection, coll.accession)
                if key not in seen:
                    seen.add(key)
                    unique_collections.append(coll)
            strain_info.culture_collections = unique_collections

            # Only store if we found something
            if strain_info.strain_name or strain_info.culture_collections or strain_info.genome_accession:
                strain_data[preferred_term] = strain_info

                # Update stats
                if strain_info.strain_name:
                    self.stats['strains_with_name'] += 1
                if strain_info.culture_collections:
                    self.stats['strains_with_collections'] += 1
                if strain_info.genome_accession:
                    self.stats['strains_with_genome'] += 1

        return strain_data

    def process_all_communities(self) -> Dict[Path, Dict[str, StrainInfo]]:
        """Process all community YAML files"""
        all_strain_data = {}

        yaml_files = sorted(self.kb_dir.glob('*.yaml'))
        print(f"\n{Colors.CYAN}Scanning {len(yaml_files)} YAML files for strain information...{Colors.RESET}")

        for yaml_path in yaml_files:
            strain_data = self.extract_strain_from_yaml(yaml_path)
            if strain_data:
                all_strain_data[yaml_path] = strain_data
                print(f"  {Colors.GREEN}✓{Colors.RESET} {yaml_path.name}: {len(strain_data)} taxa with strain info")

        return all_strain_data

    def generate_yaml_snippet(self, strain_info: StrainInfo) -> Dict:
        """Generate YAML structure for strain_designation"""
        strain_dict = {}

        if strain_info.strain_name:
            strain_dict['strain_name'] = strain_info.strain_name

        if strain_info.culture_collections:
            strain_dict['culture_collections'] = []
            for coll in strain_info.culture_collections:
                coll_dict = {
                    'collection': coll.collection,
                    'accession': coll.accession
                }
                if coll.url:
                    coll_dict['url'] = coll.url
                if coll.notes:
                    coll_dict['notes'] = coll.notes
                strain_dict['culture_collections'].append(coll_dict)

        if strain_info.type_strain is not None:
            strain_dict['type_strain'] = strain_info.type_strain

        if strain_info.genome_accession:
            strain_dict['genome_accession'] = strain_info.genome_accession

        if strain_info.genome_url:
            strain_dict['genome_url'] = strain_info.genome_url

        if strain_info.genetic_modification:
            strain_dict['genetic_modification'] = strain_info.genetic_modification

        if strain_info.isolation_source:
            strain_dict['isolation_source'] = strain_info.isolation_source

        if strain_info.notes:
            strain_dict['notes'] = strain_info.notes

        return strain_dict

    def print_summary(self):
        """Print summary statistics"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}Strain Extraction Summary:{Colors.RESET}")
        print(f"  Taxa with strain names: {self.stats['strains_with_name']}")
        print(f"  Taxa with culture collections: {self.stats['strains_with_collections']}")
        print(f"  Taxa with genome accessions: {self.stats['strains_with_genome']}")


def main():
    print(f"{Colors.BOLD}{Colors.CYAN}Phase 2: Data Enhancement - Strain Resolution{Colors.RESET}")
    print(f"{Colors.CYAN}Strategy: Literature → kg-microbe → APIs{Colors.RESET}\n")

    # Paths
    kb_dir = Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CommunityMech/CommunityMech/kb/communities')
    kgm_db = Path('kgm_taxonomy.duckdb')
    output_dir = Path('.')

    # Initialize extractor
    extractor = StrainExtractor(kb_dir, kgm_db)

    # Connect to kg-microbe
    extractor.connect_kgm()

    # Process all communities
    all_strain_data = extractor.process_all_communities()

    # Generate summary report
    print(f"\n{Colors.CYAN}Generating strain enhancement report...{Colors.RESET}")

    report_path = output_dir / 'strain_enhancement_report.txt'
    with open(report_path, 'w') as f:
        f.write("STRAIN ENHANCEMENT REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write("Phase 2: Data Enhancement - Extracted Strain Information\n\n")

        f.write(f"Total communities with strain data: {len(all_strain_data)}\n")
        f.write(f"Total taxa with strain info: {sum(len(strains) for strains in all_strain_data.values())}\n\n")

        for yaml_path, strain_data in sorted(all_strain_data.items()):
            f.write(f"\n{yaml_path.name}\n")
            f.write("-" * 80 + "\n")

            for organism_name, strain_info in sorted(strain_data.items()):
                f.write(f"\nOrganism: {organism_name}\n")
                if strain_info.strain_name:
                    f.write(f"  Strain: {strain_info.strain_name}\n")

                if strain_info.culture_collections:
                    f.write(f"  Culture Collections:\n")
                    for coll in strain_info.culture_collections:
                        f.write(f"    - {coll.collection} {coll.accession}")
                        if coll.url:
                            f.write(f" ({coll.url})")
                        f.write("\n")

                if strain_info.genome_accession:
                    f.write(f"  Genome: {strain_info.genome_accession}\n")
                    if strain_info.genome_url:
                        f.write(f"    URL: {strain_info.genome_url}\n")

                f.write(f"  Sources: {', '.join(sorted(strain_info.sources))}\n")

    print(f"{Colors.GREEN}✓{Colors.RESET} Written: {report_path}")

    # Generate YAML snippets file
    snippets_path = output_dir / 'strain_designation_snippets.yaml'
    with open(snippets_path, 'w') as f:
        f.write("# Strain Designation YAML Snippets\n")
        f.write("# Copy these into taxonomy entries in community YAML files\n\n")

        for yaml_path, strain_data in sorted(all_strain_data.items()):
            f.write(f"# {yaml_path.name}\n")
            f.write("# " + "=" * 78 + "\n\n")

            for organism_name, strain_info in sorted(strain_data.items()):
                f.write(f"# {organism_name}\n")
                snippet = extractor.generate_yaml_snippet(strain_info)
                if snippet:
                    f.write("strain_designation:\n")
                    yaml.dump(snippet, f, indent=2, sort_keys=False, default_flow_style=False)
                f.write("\n")

    print(f"{Colors.GREEN}✓{Colors.RESET} Written: {snippets_path}")

    # Print summary
    extractor.print_summary()

    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Phase 2 strain extraction complete!{Colors.RESET}")
    print(f"\n{Colors.CYAN}Next steps:{Colors.RESET}")
    print(f"  1. Review {report_path}")
    print(f"  2. Review {snippets_path}")
    print(f"  3. Apply strain designations to YAML files (Phase 2B)")
    print(f"  4. Query BacDive/ATCC APIs for additional metadata (Phase 2C)")

if __name__ == '__main__':
    main()
