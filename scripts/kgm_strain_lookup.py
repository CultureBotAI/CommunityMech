#!/usr/bin/env python3
"""
KG-Microbe DuckDB-based Strain Lookup System

Uses kg-microbe data as the unified source of truth for organism taxonomy.
Provides fast strain-specific and fuzzy search capabilities using DuckDB.

Author: CommunityMech Project
Data Source: KG-Microbe (https://github.com/Knowledge-Graph-Hub/kg-microbe)
"""

import argparse
import csv
import json
import re
import sys
import yaml
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import time

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
class StrainInfo:
    """Extracted strain information"""
    species_name: str
    strain_designation: Optional[str]
    original_term: str


@dataclass
class KGMMatch:
    """A match from kg-microbe database"""
    id: str
    name: str
    category: str
    synonym: Optional[str]
    xref: Optional[str]
    confidence: str  # EXACT, STRAIN_MATCH, SPECIES_MATCH, FUZZY, SYNONYM
    match_type: str  # name, synonym
    provided_by: Optional[str] = None
    iri: Optional[str] = None

    def to_dict(self):
        return asdict(self)


@dataclass
class ResolutionRecommendation:
    """Recommendation for resolving a taxon"""
    query: str
    current_id: Optional[str]
    kgm_matches: List[KGMMatch]
    action: str  # KEEP, UPDATE, REVIEW, NOT_FOUND
    suggested_id: Optional[str]
    reason: str

    def to_dict(self):
        return {
            'query': self.query,
            'current_id': self.current_id,
            'kgm_matches': [m.to_dict() for m in self.kgm_matches],
            'action': self.action,
            'suggested_id': self.suggested_id,
            'reason': self.reason
        }


@dataclass
class TaxonInfo:
    """Information about a taxon from YAML files"""
    preferred_term: str
    ncbi_id: str
    ncbi_label: str
    file_path: str
    file_name: str
    notes: str = ""


class KGMStrainLookup:
    """KG-Microbe DuckDB-based strain lookup system"""

    def __init__(self,
                 kgm_data_dir="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/paper_KGM/kg-microbe-paper/data/Input_Files",
                 db_path="kgm_taxonomy.duckdb",
                 force_reload=False):
        """Initialize DuckDB connection and load kg-microbe data."""
        self.kgm_data_dir = Path(kgm_data_dir)
        self.db_path = Path(db_path)
        self.conn = duckdb.connect(str(self.db_path))

        # Check if database exists and has data
        needs_loading = force_reload
        if not needs_loading:
            try:
                count = self.conn.execute("SELECT COUNT(*) FROM ncbitaxon").fetchone()[0]
                if count == 0:
                    needs_loading = True
            except:
                needs_loading = True

        if needs_loading:
            self._load_kgm_data()
        else:
            count = self.conn.execute("SELECT COUNT(*) FROM ncbitaxon").fetchone()[0]
            print(f"{Colors.GREEN}Using existing database with {count:,} NCBITaxon records{Colors.RESET}")

    def _load_kgm_data(self):
        """Load NCBITaxon nodes from kg-microbe into DuckDB."""
        print(f"{Colors.CYAN}Loading kg-microbe data into DuckDB...{Colors.RESET}")
        start_time = time.time()

        ncbi_path = self.kgm_data_dir / "ncbitaxon_nodes.tsv"

        if not ncbi_path.exists():
            print(f"{Colors.RED}ERROR: NCBITaxon nodes file not found: {ncbi_path}{Colors.RESET}")
            sys.exit(1)

        # Drop table if exists
        self.conn.execute("DROP TABLE IF EXISTS ncbitaxon")

        # Load data with explicit schema to handle special characters
        print(f"  Reading from: {ncbi_path}")
        self.conn.execute(f"""
            CREATE TABLE ncbitaxon AS
            SELECT * FROM read_csv_auto(
                '{ncbi_path}',
                delim='\t',
                header=true,
                max_line_size=1048576,
                ignore_errors=true
            )
        """)

        # Create indexes for fast lookup
        print(f"  Creating indexes...")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_ncbi_id ON ncbitaxon(id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_ncbi_name ON ncbitaxon(name)")

        # Create FTS index for fuzzy search (if supported)
        try:
            # Create a normalized name column for better searching
            self.conn.execute("""
                ALTER TABLE ncbitaxon ADD COLUMN IF NOT EXISTS name_lower VARCHAR
            """)
            self.conn.execute("""
                UPDATE ncbitaxon SET name_lower = LOWER(name)
            """)
            self.conn.execute("CREATE INDEX IF NOT EXISTS idx_ncbi_name_lower ON ncbitaxon(name_lower)")
        except Exception as e:
            print(f"{Colors.YELLOW}  Warning: Could not create normalized name index: {e}{Colors.RESET}")

        count = self.conn.execute("SELECT COUNT(*) FROM ncbitaxon").fetchone()[0]
        elapsed = time.time() - start_time

        print(f"{Colors.GREEN}Loaded {count:,} NCBITaxon records in {elapsed:.1f} seconds{Colors.RESET}")
        print(f"{Colors.GREEN}Database created: {self.db_path}{Colors.RESET}")

    def extract_strain_info(self, organism_name: str, notes: str = "") -> StrainInfo:
        """
        Extract strain/culture collection designations from organism name.

        Examples:
        - "Desulfovibrio vulgaris Hildenborough" -> strain: "Hildenborough"
        - "Escherichia coli K-12" -> strain: "K-12"
        - "Acidithiobacillus caldus DSM 8584" -> strain: "DSM 8584"
        """
        patterns = [
            # Formal strain designation
            (r'^(.+?)\s+(?:str\.|strain)\s+(.+)$', 'formal'),
            # Culture collection patterns (DSM, ATCC, PCC, etc.)
            (r'^(.+?)\s+((?:DSM|ATCC|PCC|JCM|LMG|NCTC|NBRC|CCM|CIP)\s+\S+)$', 'culture_collection'),
            # Strain with dashes/dots (GS-15, K-12, etc.)
            (r'^(.+?)\s+([A-Z]{1,3}[\-\.]\d+[A-Za-z]*)$', 'dash_number'),
            # Single word/alphanumeric at end (Hildenborough, S2, etc.)
            (r'^(.+?)\s+([A-Z][a-z]+[0-9]*)$', 'suffix'),
            # Alphanumeric code at end
            (r'^(.+?)\s+([A-Z0-9]+)$', 'code'),
        ]

        for pattern, pattern_type in patterns:
            match = re.match(pattern, organism_name.strip())
            if match:
                species_name = match.group(1).strip()
                strain_designation = match.group(2).strip()

                # Validate species_name has at least genus + species
                if len(species_name.split()) >= 2:
                    return StrainInfo(
                        species_name=species_name,
                        strain_designation=strain_designation,
                        original_term=organism_name
                    )

        # No strain found
        return StrainInfo(
            species_name=organism_name.strip(),
            strain_designation=None,
            original_term=organism_name
        )

    def search_by_exact_name(self, organism_name: str) -> List[KGMMatch]:
        """Exact match search in kg-microbe."""
        results = self.conn.execute("""
            SELECT id, name, category, synonym, xref, provided_by, iri
            FROM ncbitaxon
            WHERE name = ?
        """, [organism_name]).fetchall()

        matches = []
        for row in results:
            matches.append(KGMMatch(
                id=row[0],
                name=row[1],
                category=row[2],
                synonym=row[3],
                xref=row[4],
                provided_by=row[5],
                iri=row[6],
                confidence='EXACT',
                match_type='name'
            ))

        return matches

    def search_by_synonym(self, organism_name: str) -> List[KGMMatch]:
        """Search by synonym in kg-microbe."""
        results = self.conn.execute("""
            SELECT id, name, category, synonym, xref, provided_by, iri
            FROM ncbitaxon
            WHERE synonym IS NOT NULL
            AND (
                synonym = ? OR
                synonym LIKE ? OR
                synonym LIKE ? OR
                synonym LIKE ?
            )
        """, [
            organism_name,
            f"{organism_name}|%",
            f"%|{organism_name}|%",
            f"%|{organism_name}"
        ]).fetchall()

        matches = []
        for row in results:
            matches.append(KGMMatch(
                id=row[0],
                name=row[1],
                category=row[2],
                synonym=row[3],
                xref=row[4],
                provided_by=row[5],
                iri=row[6],
                confidence='SYNONYM',
                match_type='synonym'
            ))

        return matches

    def search_by_fuzzy_name(self, organism_name: str, include_synonyms=True, limit=10) -> List[KGMMatch]:
        """
        Fuzzy search with LIKE operator.
        Returns ranked results by relevance.
        """
        matches = []

        # Try exact match first
        exact_matches = self.search_by_exact_name(organism_name)
        matches.extend(exact_matches)

        if not matches:
            # Try case-insensitive exact match
            results = self.conn.execute("""
                SELECT id, name, category, synonym, xref, provided_by, iri
                FROM ncbitaxon
                WHERE LOWER(name) = LOWER(?)
                LIMIT ?
            """, [organism_name, limit]).fetchall()

            for row in results:
                matches.append(KGMMatch(
                    id=row[0],
                    name=row[1],
                    category=row[2],
                    synonym=row[3],
                    xref=row[4],
                    provided_by=row[5],
                    iri=row[6],
                    confidence='EXACT',
                    match_type='name_case_insensitive'
                ))

        if not matches:
            # Try fuzzy match with LIKE
            results = self.conn.execute("""
                SELECT id, name, category, synonym, xref, provided_by, iri
                FROM ncbitaxon
                WHERE name LIKE ?
                ORDER BY LENGTH(name)
                LIMIT ?
            """, [f"%{organism_name}%", limit]).fetchall()

            for row in results:
                matches.append(KGMMatch(
                    id=row[0],
                    name=row[1],
                    category=row[2],
                    synonym=row[3],
                    xref=row[4],
                    provided_by=row[5],
                    iri=row[6],
                    confidence='FUZZY',
                    match_type='name_fuzzy'
                ))

        # Search synonyms if requested
        if include_synonyms and len(matches) < limit:
            synonym_matches = self.search_by_synonym(organism_name)
            matches.extend(synonym_matches[:limit - len(matches)])

        return matches[:limit]

    def search_strain_specific(self, species_name: str, strain: str) -> List[KGMMatch]:
        """
        Search for strain-specific entries.

        Example: search_strain_specific("Desulfovibrio vulgaris", "Hildenborough")
        Returns NCBITaxon IDs for the specific strain.
        """
        queries = [
            f"{species_name} str. {strain}",
            f"{species_name} strain {strain}",
            f"{species_name} {strain}",
        ]

        all_matches = []
        seen_ids = set()

        for query in queries:
            # Try exact match first
            matches = self.search_by_exact_name(query)
            for match in matches:
                if match.id not in seen_ids:
                    match.confidence = 'STRAIN_MATCH'
                    all_matches.append(match)
                    seen_ids.add(match.id)

            if all_matches:
                break

            # Try case-insensitive
            results = self.conn.execute("""
                SELECT id, name, category, synonym, xref, provided_by, iri
                FROM ncbitaxon
                WHERE LOWER(name) = LOWER(?)
            """, [query]).fetchall()

            for row in results:
                if row[0] not in seen_ids:
                    all_matches.append(KGMMatch(
                        id=row[0],
                        name=row[1],
                        category=row[2],
                        synonym=row[3],
                        xref=row[4],
                        provided_by=row[5],
                        iri=row[6],
                        confidence='STRAIN_MATCH',
                        match_type='name_case_insensitive'
                    ))
                    seen_ids.add(row[0])

            if all_matches:
                break

        # If no strain match, try species-level
        if not all_matches:
            species_matches = self.search_by_exact_name(species_name)
            for match in species_matches:
                if match.id not in seen_ids:
                    match.confidence = 'SPECIES_MATCH'
                    all_matches.append(match)
                    seen_ids.add(match.id)

        return all_matches

    def get_taxonomy_hierarchy(self, ncbitaxon_id: str) -> Dict[str, str]:
        """
        Get full taxonomic lineage for an NCBITaxon ID.
        Uses xref field to extract lineage information.
        """
        # Clean ID
        if ':' in ncbitaxon_id:
            ncbitaxon_id = ncbitaxon_id.split(':')[1]

        curie = f"NCBITaxon:{ncbitaxon_id}"

        result = self.conn.execute("""
            SELECT id, name, category, xref
            FROM ncbitaxon
            WHERE id = ?
        """, [curie]).fetchone()

        if not result:
            return {}

        hierarchy = {
            'id': result[0],
            'name': result[1],
            'category': result[2],
            'xref': result[3]
        }

        # Parse xref for additional info
        if result[3]:
            xref_parts = result[3].split('|')
            for part in xref_parts:
                if part.startswith('GC_ID:'):
                    hierarchy['genetic_code'] = part.split(':')[1]

        return hierarchy

    def resolve_strain(self, preferred_term: str, current_ncbi_id: str = None) -> ResolutionRecommendation:
        """
        Resolve a strain designation using kg-microbe as source of truth.

        Returns ResolutionRecommendation with action plan.
        """
        # Extract strain info
        strain_info = self.extract_strain_info(preferred_term)

        # Search kg-microbe
        if strain_info.strain_designation:
            # Strain-specific search
            kgm_matches = self.search_strain_specific(
                strain_info.species_name,
                strain_info.strain_designation
            )
        else:
            # Species-level search
            kgm_matches = self.search_by_fuzzy_name(preferred_term)

        # Determine recommendation
        action = 'NOT_FOUND'
        suggested_id = None
        reason = ''

        if not kgm_matches:
            action = 'NOT_FOUND'
            reason = f"'{preferred_term}' not found in kg-microbe database"
        elif len(kgm_matches) == 1:
            # Single match
            match = kgm_matches[0]
            match_id = match.id.split(':')[1] if ':' in match.id else match.id

            if current_ncbi_id and match_id == current_ncbi_id:
                action = 'KEEP'
                suggested_id = current_ncbi_id
                reason = f"Current ID matches kg-microbe ({match.confidence} match)"
            else:
                action = 'UPDATE'
                suggested_id = match_id
                if current_ncbi_id:
                    reason = f"kg-microbe suggests NCBITaxon:{match_id} (currently {current_ncbi_id})"
                else:
                    reason = f"kg-microbe found NCBITaxon:{match_id}"
        else:
            # Multiple matches - need review
            action = 'REVIEW'
            # Prefer strain-level matches
            strain_matches = [m for m in kgm_matches if m.confidence == 'STRAIN_MATCH']
            exact_matches = [m for m in kgm_matches if m.confidence == 'EXACT']

            if strain_matches:
                match = strain_matches[0]
                suggested_id = match.id.split(':')[1] if ':' in match.id else match.id
                reason = f"Multiple matches found, suggest strain-level: NCBITaxon:{suggested_id}"
            elif exact_matches:
                match = exact_matches[0]
                suggested_id = match.id.split(':')[1] if ':' in match.id else match.id
                reason = f"Multiple matches found, suggest exact match: NCBITaxon:{suggested_id}"
            else:
                match = kgm_matches[0]
                suggested_id = match.id.split(':')[1] if ':' in match.id else match.id
                reason = f"{len(kgm_matches)} matches found - manual review needed"

        return ResolutionRecommendation(
            query=preferred_term,
            current_id=current_ncbi_id,
            kgm_matches=kgm_matches,
            action=action,
            suggested_id=suggested_id,
            reason=reason
        )

    def collect_all_taxa(self, yaml_dir: Path) -> List[TaxonInfo]:
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

                        all_taxa.append(TaxonInfo(
                            preferred_term=preferred_term,
                            ncbi_id=ncbi_id,
                            ncbi_label=ncbi_label,
                            file_path=str(yaml_file),
                            file_name=yaml_file.name,
                            notes=notes
                        ))
            except Exception as e:
                print(f"{Colors.RED}Error reading {yaml_file}: {e}{Colors.RESET}")

        print(f"{Colors.GREEN}Found {len(all_taxa)} taxa entries{Colors.RESET}\n")
        return all_taxa

    def validate_community_taxa(self,
                                yaml_dir="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CommunityMech/CommunityMech/kb/communities") -> Dict:
        """
        Validate all taxa in community YAMLs against kg-microbe database.
        """
        yaml_dir = Path(yaml_dir)
        all_taxa = self.collect_all_taxa(yaml_dir)

        results = {
            'perfect_match': [],      # KGM ID matches YAML ID
            'name_match_diff_id': [], # Found in KGM but different ID
            'not_found_in_kgm': [],   # Not found in kg-microbe
            'kgm_suggests': []        # KGM has alternative matches
        }

        print(f"{Colors.CYAN}Validating {len(all_taxa)} taxa against kg-microbe...{Colors.RESET}")

        for i, taxon in enumerate(all_taxa, 1):
            if i % 25 == 0:
                print(f"  Progress: {i}/{len(all_taxa)}")

            resolution = self.resolve_strain(taxon.preferred_term, taxon.ncbi_id)

            result_entry = {
                'taxon': taxon,
                'resolution': resolution
            }

            if resolution.action == 'KEEP':
                results['perfect_match'].append(result_entry)
            elif resolution.action == 'UPDATE':
                results['name_match_diff_id'].append(result_entry)
            elif resolution.action == 'REVIEW':
                results['kgm_suggests'].append(result_entry)
            elif resolution.action == 'NOT_FOUND':
                results['not_found_in_kgm'].append(result_entry)

        print(f"{Colors.GREEN}Validation complete!{Colors.RESET}\n")

        return results

    def generate_corrections_report(self,
                                   output_dir="./",
                                   yaml_dir="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CommunityMech/CommunityMech/kb/communities"):
        """
        Generate comprehensive correction recommendations based on kg-microbe.
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{Colors.BOLD}{Colors.CYAN}Generating KG-Microbe Validation Report{Colors.RESET}\n")

        # Run validation
        results = self.validate_community_taxa(yaml_dir)

        total = sum(len(v) for v in results.values())
        perfect = len(results['perfect_match'])
        diff_id = len(results['name_match_diff_id'])
        not_found = len(results['not_found_in_kgm'])
        review = len(results['kgm_suggests'])

        # Generate TSV corrections file
        corrections_file = output_dir / 'kgm_corrections.tsv'
        with open(corrections_file, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow([
                'file', 'preferred_term', 'strain', 'current_id', 'kgm_suggested_id',
                'kgm_name', 'action', 'confidence', 'reason'
            ])

            for category, entries in results.items():
                for entry in entries:
                    taxon = entry['taxon']
                    resolution = entry['resolution']
                    strain_info = self.extract_strain_info(taxon.preferred_term, taxon.notes)

                    kgm_name = resolution.kgm_matches[0].name if resolution.kgm_matches else ''
                    kgm_confidence = resolution.kgm_matches[0].confidence if resolution.kgm_matches else ''

                    writer.writerow([
                        taxon.file_name,
                        taxon.preferred_term,
                        strain_info.strain_designation or '',
                        taxon.ncbi_id,
                        resolution.suggested_id or '',
                        kgm_name,
                        resolution.action,
                        kgm_confidence,
                        resolution.reason
                    ])

        print(f"{Colors.GREEN}Written: {corrections_file}{Colors.RESET}")

        # Generate statistics JSON
        stats = {
            'total_taxa': total,
            'perfect_match': perfect,
            'perfect_match_pct': round(perfect / total * 100, 1) if total > 0 else 0,
            'name_match_diff_id': diff_id,
            'name_match_diff_id_pct': round(diff_id / total * 100, 1) if total > 0 else 0,
            'not_found_in_kgm': not_found,
            'not_found_pct': round(not_found / total * 100, 1) if total > 0 else 0,
            'requires_review': review,
            'review_pct': round(review / total * 100, 1) if total > 0 else 0,
        }

        stats_file = output_dir / 'kgm_statistics.json'
        with open(stats_file, 'w') as f:
            json.dump(stats, f, indent=2)

        print(f"{Colors.GREEN}Written: {stats_file}{Colors.RESET}")

        # Generate human-readable report
        report_file = output_dir / 'kgm_validation_report.txt'
        with open(report_file, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("KG-MICROBE TAXONOMY VALIDATION REPORT\n")
            f.write("=" * 80 + "\n\n")

            f.write("SUMMARY STATISTICS\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total taxa analyzed: {total}\n")
            f.write(f"Perfect matches (ID matches kg-microbe): {perfect} ({stats['perfect_match_pct']}%)\n")
            f.write(f"Name matches but different ID: {diff_id} ({stats['name_match_diff_id_pct']}%)\n")
            f.write(f"Not found in kg-microbe: {not_found} ({stats['not_found_pct']}%)\n")
            f.write(f"Requires manual review: {review} ({stats['review_pct']}%)\n\n")

            f.write("=" * 80 + "\n")
            f.write("A. PERFECT MATCHES (No action needed)\n")
            f.write("=" * 80 + "\n\n")
            for entry in results['perfect_match'][:10]:
                taxon = entry['taxon']
                resolution = entry['resolution']
                f.write(f"  {taxon.preferred_term}\n")
                f.write(f"    Current ID: NCBITaxon:{taxon.ncbi_id}\n")
                f.write(f"    kg-microbe: {resolution.kgm_matches[0].name if resolution.kgm_matches else 'N/A'}\n")
                f.write(f"    Status: {resolution.reason}\n\n")
            if len(results['perfect_match']) > 10:
                f.write(f"  ... and {len(results['perfect_match']) - 10} more\n\n")

            f.write("=" * 80 + "\n")
            f.write("B. RECOMMENDED UPDATES (ID differs from kg-microbe)\n")
            f.write("=" * 80 + "\n\n")
            for entry in results['name_match_diff_id']:
                taxon = entry['taxon']
                resolution = entry['resolution']
                f.write(f"  {taxon.preferred_term}\n")
                f.write(f"    Current ID: NCBITaxon:{taxon.ncbi_id}\n")
                f.write(f"    kg-microbe suggests: NCBITaxon:{resolution.suggested_id}\n")
                f.write(f"    kg-microbe name: {resolution.kgm_matches[0].name if resolution.kgm_matches else 'N/A'}\n")
                f.write(f"    Reason: {resolution.reason}\n")
                f.write(f"    File: {taxon.file_name}\n\n")

            f.write("=" * 80 + "\n")
            f.write("C. REQUIRES REVIEW (Multiple matches)\n")
            f.write("=" * 80 + "\n\n")
            for entry in results['kgm_suggests']:
                taxon = entry['taxon']
                resolution = entry['resolution']
                f.write(f"  {taxon.preferred_term}\n")
                f.write(f"    Current ID: NCBITaxon:{taxon.ncbi_id}\n")
                f.write(f"    kg-microbe matches ({len(resolution.kgm_matches)}):\n")
                for match in resolution.kgm_matches[:3]:
                    match_id = match.id.split(':')[1] if ':' in match.id else match.id
                    f.write(f"      - NCBITaxon:{match_id}: {match.name} ({match.confidence})\n")
                f.write(f"    Reason: {resolution.reason}\n")
                f.write(f"    File: {taxon.file_name}\n\n")

            f.write("=" * 80 + "\n")
            f.write("D. NOT FOUND IN KG-MICROBE\n")
            f.write("=" * 80 + "\n\n")
            for entry in results['not_found_in_kgm']:
                taxon = entry['taxon']
                f.write(f"  {taxon.preferred_term}\n")
                f.write(f"    Current ID: NCBITaxon:{taxon.ncbi_id}\n")
                f.write(f"    Status: Not found in kg-microbe database\n")
                f.write(f"    File: {taxon.file_name}\n\n")

            f.write("=" * 80 + "\n")
            f.write("END OF REPORT\n")
            f.write("=" * 80 + "\n")

        print(f"{Colors.GREEN}Written: {report_file}{Colors.RESET}")

        # Print summary to console
        print(f"\n{Colors.BOLD}{Colors.CYAN}VALIDATION SUMMARY{Colors.RESET}")
        print(f"{Colors.GREEN}Perfect matches: {perfect}/{total} ({stats['perfect_match_pct']}%){Colors.RESET}")
        print(f"{Colors.YELLOW}Different IDs: {diff_id}/{total} ({stats['name_match_diff_id_pct']}%){Colors.RESET}")
        print(f"{Colors.MAGENTA}Needs review: {review}/{total} ({stats['review_pct']}%){Colors.RESET}")
        print(f"{Colors.RED}Not found: {not_found}/{total} ({stats['not_found_pct']}%){Colors.RESET}")

        return results


def main():
    parser = argparse.ArgumentParser(
        description="KG-Microbe strain lookup and validation system"
    )
    parser.add_argument(
        "--load",
        action="store_true",
        help="Load/reload kg-microbe data into DuckDB"
    )
    parser.add_argument(
        "--search",
        type=str,
        help="Search for organism by name"
    )
    parser.add_argument(
        "--strain",
        type=str,
        nargs=2,
        metavar=("SPECIES", "STRAIN"),
        help="Search for specific strain (e.g., --strain 'Desulfovibrio vulgaris' 'Hildenborough')"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate all community YAMLs against kg-microbe"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate comprehensive correction report"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./",
        help="Output directory for reports (default: current directory)"
    )
    parser.add_argument(
        "--kgm-data-dir",
        type=str,
        default="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/paper_KGM/kg-microbe-paper/data/Input_Files",
        help="Path to kg-microbe data directory"
    )
    parser.add_argument(
        "--db-path",
        type=str,
        default="kgm_taxonomy.duckdb",
        help="Path to DuckDB database file"
    )

    args = parser.parse_args()

    # Initialize lookup system
    print(f"\n{Colors.BOLD}{Colors.CYAN}KG-Microbe Strain Lookup System{Colors.RESET}\n")

    lookup = KGMStrainLookup(
        kgm_data_dir=args.kgm_data_dir,
        db_path=args.db_path,
        force_reload=args.load
    )

    if args.search:
        print(f"\n{Colors.CYAN}Searching for: {args.search}{Colors.RESET}\n")
        results = lookup.search_by_fuzzy_name(args.search)

        if not results:
            print(f"{Colors.RED}No matches found{Colors.RESET}")
        else:
            print(f"{Colors.GREEN}Found {len(results)} match(es):{Colors.RESET}\n")
            for i, match in enumerate(results, 1):
                match_id = match.id.split(':')[1] if ':' in match.id else match.id
                print(f"{i}. {Colors.BOLD}{match.name}{Colors.RESET}")
                print(f"   ID: NCBITaxon:{match_id}")
                print(f"   Confidence: {match.confidence}")
                print(f"   Category: {match.category}")
                if match.synonym:
                    synonyms = match.synonym.split('|') if '|' in match.synonym else [match.synonym]
                    print(f"   Synonyms: {', '.join(synonyms[:3])}")
                if match.xref:
                    print(f"   Xref: {match.xref[:100]}")
                print()

    if args.strain:
        species, strain_name = args.strain
        print(f"\n{Colors.CYAN}Searching for strain: {species} {strain_name}{Colors.RESET}\n")
        results = lookup.search_strain_specific(species, strain_name)

        if not results:
            print(f"{Colors.RED}No strain-specific match found{Colors.RESET}")
            print(f"{Colors.YELLOW}Trying species-level search...{Colors.RESET}\n")
            results = lookup.search_by_fuzzy_name(species)

        if results:
            print(f"{Colors.GREEN}Found {len(results)} match(es):{Colors.RESET}\n")
            for i, match in enumerate(results, 1):
                match_id = match.id.split(':')[1] if ':' in match.id else match.id
                print(f"{i}. {Colors.BOLD}{match.name}{Colors.RESET}")
                print(f"   ID: NCBITaxon:{match_id}")
                print(f"   Confidence: {match.confidence}")
                print(f"   Category: {match.category}")
                print()

    if args.validate or args.report:
        lookup.generate_corrections_report(output_dir=args.output_dir)

    print(f"\n{Colors.GREEN}Done!{Colors.RESET}\n")


if __name__ == "__main__":
    main()
