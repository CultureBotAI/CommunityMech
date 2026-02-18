#!/usr/bin/env python3
"""
Comprehensive Strain-Resolved Taxonomy Validation Script

Compares NCBITaxonomy and GTDB against literature-derived species names (preferred_term).
The preferred_term from literature is the SOURCE OF TRUTH.

Hierarchy of truth:
1. Literature strain designation (from preferred_term/notes) = PRIMARY SOURCE
2. Strain-specific NCBITaxon ID (if exists) = PREFERRED
3. Species-level NCBITaxon ID (if strain unavailable) = ACCEPTABLE FALLBACK
4. GTDB genome ID (alternative/validation)

Usage:
    python compare_ncbi_gtdb_taxonomy.py [--kb-dir PATH] [--gtdb-path PATH]
"""

import argparse
import csv
import sys
import yaml
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
from dataclasses import dataclass

try:
    from oaklib import get_adapter
    OAKLIB_AVAILABLE = True
except ImportError:
    OAKLIB_AVAILABLE = False
    print("WARNING: oaklib not available. Install with: pip install oaklib")

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("WARNING: requests not available. Install with: pip install requests")


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
class TaxonInfo:
    """Information about a taxon from YAML files"""
    preferred_term: str
    ncbi_id: str
    ncbi_label: str
    file_path: str
    file_name: str
    notes: str = ""


@dataclass
class NCBIValidation:
    """NCBI taxonomy validation result"""
    is_match: bool
    ncbi_current_label: Optional[str]
    suggested_ncbi_id: Optional[str]
    suggested_ncbi_label: Optional[str]
    is_synonym: bool = False
    synonym_type: Optional[str] = None
    taxonomy_rank: Optional[str] = None

    # Strain-level fields
    strain_level_id: Optional[str] = None
    strain_level_label: Optional[str] = None
    species_level_id: Optional[str] = None
    species_level_label: Optional[str] = None
    recommendation: Optional[str] = None  # USE_STRAIN, USE_SPECIES, NOT_FOUND


@dataclass
class GTDBInfo:
    """GTDB taxonomy information"""
    found: bool
    lineage: Optional[str]
    classification: Optional[Dict[str, str]]
    conflicts_with_ncbi: bool = False
    conflict_details: Optional[str] = None
    genome_id: Optional[str] = None
    genome_ids: List[str] = None


def extract_strain_info(preferred_term: str, notes: str = "") -> StrainInfo:
    """
    Extract strain/culture collection designations from preferred_term and notes.

    Examples:
    - "Desulfovibrio vulgaris Hildenborough" → strain: "Hildenborough"
    - "Escherichia coli K-12" → strain: "K-12"
    - "Acidithiobacillus caldus DSM 8584" → strain: "DSM 8584"
    - "Synechococcus elongatus PCC 7942" → strain: "PCC 7942"
    - "Geobacter metallireducens GS-15" → strain: "GS-15"
    - "Methanococcus maripaludis S2" → strain: "S2"
    """

    # Patterns for strain designation extraction
    patterns = [
        # Formal strain designation
        (r'^(.+?)\s+(?:str\.|strain)\s+(.+)$', 'formal'),
        # Culture collection patterns (DSM, ATCC, PCC, JCM, LMG, NCTC, etc.)
        (r'^(.+?)\s+((?:DSM|ATCC|PCC|JCM|LMG|NCTC|NBRC|CCM|CIP)\s+\d+.*)$', 'culture_collection'),
        # Strain with dashes/dots at end (GS-15, K-12, ML-04, etc.)
        (r'^(.+?)\s+([A-Z]{1,3}[\-\.]\d+)$', 'dash_number'),
        # Single word/alphanumeric at end (Hildenborough, S2, etc.)
        (r'^(.+?)\s+([A-Z][a-z]*\d*)$', 'suffix'),
        # Just alphanumeric code at end
        (r'^(.+?)\s+([A-Z0-9]+)$', 'code'),
    ]

    # Try each pattern
    for pattern, pattern_type in patterns:
        match = re.match(pattern, preferred_term.strip())
        if match:
            species_name = match.group(1).strip()
            strain_designation = match.group(2).strip()

            # Validate that species_name has at least genus + species
            # (should have at least 2 words)
            if len(species_name.split()) >= 2:
                return StrainInfo(
                    species_name=species_name,
                    strain_designation=strain_designation,
                    original_term=preferred_term
                )

    # No strain found - return species-level info
    return StrainInfo(
        species_name=preferred_term.strip(),
        strain_designation=None,
        original_term=preferred_term
    )


def extract_taxa_from_yaml(yaml_path: Path) -> List[TaxonInfo]:
    """Extract taxon information from a YAML file"""
    taxa = []

    try:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        if not data or 'taxonomy' not in data:
            return taxa

        for taxon_entry in data['taxonomy']:
            if 'taxon_term' not in taxon_entry:
                continue

            taxon_term = taxon_entry['taxon_term']

            # Extract preferred_term (source of truth)
            preferred_term = taxon_term.get('preferred_term', '')

            # Extract notes (may contain strain info)
            notes = taxon_term.get('notes', '')

            # Extract NCBI ID and label
            term_info = taxon_term.get('term', {})
            ncbi_id = term_info.get('id', '')
            ncbi_label = term_info.get('label', '')

            if preferred_term and ncbi_id:
                # Clean up NCBI ID (remove prefix if present)
                if ':' in ncbi_id:
                    ncbi_id = ncbi_id.split(':', 1)[1]

                taxa.append(TaxonInfo(
                    preferred_term=preferred_term,
                    ncbi_id=ncbi_id,
                    ncbi_label=ncbi_label,
                    file_path=str(yaml_path),
                    file_name=yaml_path.name,
                    notes=notes
                ))

    except Exception as e:
        print(f"{Colors.RED}Error reading {yaml_path}: {e}{Colors.RESET}")

    return taxa


def collect_all_taxa(kb_dir: Path) -> List[TaxonInfo]:
    """Collect all taxa from YAML files in the kb directory"""
    all_taxa = []

    communities_dir = kb_dir / 'communities'
    if not communities_dir.exists():
        print(f"{Colors.RED}Error: Communities directory not found: {communities_dir}{Colors.RESET}")
        return all_taxa

    yaml_files = list(communities_dir.glob('*.yaml')) + list(communities_dir.glob('*.yml'))

    print(f"\n{Colors.CYAN}Scanning {len(yaml_files)} YAML files...{Colors.RESET}")

    for yaml_file in yaml_files:
        taxa = extract_taxa_from_yaml(yaml_file)
        all_taxa.extend(taxa)

    print(f"{Colors.CYAN}Found {len(all_taxa)} taxa entries{Colors.RESET}\n")

    return all_taxa


def search_ncbi_taxonomy_multilevel(
    species_name: str,
    strain: Optional[str],
    ncbi_adapter
) -> Tuple[Optional[Dict], Optional[Dict]]:
    """
    Search NCBITaxonomy at strain and species levels.

    Returns: (strain_result, species_result)
    Each result is a dict with 'id', 'label', 'rank' or None
    """

    strain_result = None
    species_result = None

    # Search for strain-specific entry
    if strain:
        strain_queries = [
            f"{species_name} str. {strain}",
            f"{species_name} strain {strain}",
            f"{species_name} {strain}"
        ]

        for query in strain_queries:
            try:
                search_results = list(ncbi_adapter.basic_search(query))
                if search_results:
                    result_id = search_results[0]
                    result_label = ncbi_adapter.label(result_id)

                    # Check if it's actually a strain-level match
                    if result_label and strain.lower() in result_label.lower():
                        # Get rank information if available
                        rank = None
                        try:
                            # Try to get rank from adapter
                            # This may not be available in all OAK adapters
                            pass
                        except:
                            pass

                        strain_result = {
                            'id': result_id.split(':')[1] if ':' in result_id else result_id,
                            'label': result_label,
                            'rank': rank
                        }
                        break
            except Exception as e:
                pass

    # Search for species-level entry
    try:
        species_results = list(ncbi_adapter.basic_search(species_name))
        if species_results:
            result_id = species_results[0]
            result_label = ncbi_adapter.label(result_id)

            if result_label:
                species_result = {
                    'id': result_id.split(':')[1] if ':' in result_id else result_id,
                    'label': result_label,
                    'rank': None
                }
    except Exception as e:
        pass

    return strain_result, species_result


def validate_ncbi_taxonomy(taxon: TaxonInfo, ncbi_adapter) -> NCBIValidation:
    """Validate taxon against NCBITaxonomy using OAK with strain-level resolution"""
    if not OAKLIB_AVAILABLE or ncbi_adapter is None:
        return NCBIValidation(
            is_match=False,
            ncbi_current_label=None,
            suggested_ncbi_id=None,
            suggested_ncbi_label=None
        )

    try:
        # Extract strain information
        strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)

        # Check current NCBI ID
        ncbi_curie = f"NCBITaxon:{taxon.ncbi_id}"
        current_label = ncbi_adapter.label(ncbi_curie)

        # Check if label matches preferred_term
        is_match = False
        is_synonym = False

        if current_label:
            # Exact match
            if current_label.lower() == taxon.preferred_term.lower():
                is_match = True
            else:
                # Check if preferred_term is a synonym
                synonyms = list(ncbi_adapter.entity_aliases(ncbi_curie))
                for syn in synonyms:
                    if syn.lower() == taxon.preferred_term.lower():
                        is_match = True
                        is_synonym = True
                        break

        # Multi-level search for strain and species
        strain_result, species_result = search_ncbi_taxonomy_multilevel(
            strain_info.species_name,
            strain_info.strain_designation,
            ncbi_adapter
        )

        # Determine recommendation
        recommendation = None
        suggested_id = None
        suggested_label = None

        if strain_info.strain_designation:
            # Literature specifies a strain
            if strain_result:
                recommendation = "USE_STRAIN"
                if not is_match or taxon.ncbi_id != strain_result['id']:
                    suggested_id = strain_result['id']
                    suggested_label = strain_result['label']
            elif species_result:
                recommendation = "USE_SPECIES"
                if not is_match or taxon.ncbi_id != species_result['id']:
                    suggested_id = species_result['id']
                    suggested_label = species_result['label']
            else:
                recommendation = "NOT_FOUND"
        else:
            # No strain in literature - species level is expected
            if species_result:
                recommendation = "USE_SPECIES"
                if not is_match or taxon.ncbi_id != species_result['id']:
                    suggested_id = species_result['id']
                    suggested_label = species_result['label']
            else:
                recommendation = "NOT_FOUND"

        return NCBIValidation(
            is_match=is_match,
            ncbi_current_label=current_label,
            suggested_ncbi_id=suggested_id,
            suggested_ncbi_label=suggested_label,
            is_synonym=is_synonym,
            synonym_type="synonym" if is_synonym else None,
            strain_level_id=strain_result['id'] if strain_result else None,
            strain_level_label=strain_result['label'] if strain_result else None,
            species_level_id=species_result['id'] if species_result else None,
            species_level_label=species_result['label'] if species_result else None,
            recommendation=recommendation
        )

    except Exception as e:
        print(f"{Colors.RED}Error validating {taxon.preferred_term}: {e}{Colors.RESET}")
        return NCBIValidation(
            is_match=False,
            ncbi_current_label=None,
            suggested_ncbi_id=None,
            suggested_ncbi_label=None
        )


def query_gtdb_local(species_name: str, gtdb_conn) -> GTDBInfo:
    """Query GTDB database for taxonomy information using DuckDB"""
    try:
        # Try exact species match
        results = gtdb_conn.execute("""
            SELECT genome_id, species, taxonomy
            FROM gtdb_taxonomy
            WHERE species = ?
            LIMIT 1
        """, [species_name]).fetchall()

        if results:
            row = results[0]
            genome_id = row[0]
            species = row[1]
            lineage = row[2]

            # Parse lineage into classification
            classification = parse_gtdb_lineage(lineage)

            return GTDBInfo(
                found=True,
                lineage=lineage,
                classification=classification,
                genome_id=genome_id,
                genome_ids=[genome_id]
            )

        # Try genus-level match
        genus = species_name.split()[0] if species_name else ''
        if genus:
            results = gtdb_conn.execute("""
                SELECT genome_id, species, taxonomy
                FROM gtdb_taxonomy
                WHERE genus = ?
                LIMIT 5
            """, [genus]).fetchall()

            if results:
                # Return first match with all genome IDs
                genome_ids = [r[0] for r in results]
                lineage = results[0][2]
                classification = parse_gtdb_lineage(lineage)

                return GTDBInfo(
                    found=True,
                    lineage=lineage,
                    classification=classification,
                    genome_id=genome_ids[0],
                    genome_ids=genome_ids
                )

        return GTDBInfo(found=False, lineage=None, classification=None)

    except Exception as e:
        # GTDB database might not be loaded
        return GTDBInfo(found=False, lineage=None, classification=None)


def query_gtdb_api(species_name: str) -> GTDBInfo:
    """Query GTDB API for taxonomy information (deprecated - use query_gtdb_local)"""
    if not REQUESTS_AVAILABLE:
        return GTDBInfo(found=False, lineage=None, classification=None)

    try:
        # GTDB API endpoint (using the web API)
        # Note: This is a simplified version - actual GTDB API might differ
        url = f"https://api.gtdb.ecogenomic.org/search/taxa"
        params = {'search': species_name}

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            if data and len(data) > 0:
                first_result = data[0]
                lineage = first_result.get('lineage', '')

                # Parse lineage into classification
                classification = parse_gtdb_lineage(lineage)

                return GTDBInfo(
                    found=True,
                    lineage=lineage,
                    classification=classification
                )

        return GTDBInfo(found=False, lineage=None, classification=None)

    except Exception as e:
        # GTDB API might not be accessible - this is expected
        return GTDBInfo(found=False, lineage=None, classification=None)


def parse_gtdb_lineage(lineage: str) -> Dict[str, str]:
    """Parse GTDB lineage string into classification dictionary"""
    classification = {}

    if not lineage:
        return classification

    ranks = ['domain', 'phylum', 'class', 'order', 'family', 'genus', 'species']
    parts = lineage.split(';')

    for i, part in enumerate(parts):
        if i < len(ranks):
            # Remove rank prefix (d__, p__, etc.)
            value = part.strip()
            if '__' in value:
                value = value.split('__', 1)[1]
            classification[ranks[i]] = value

    return classification


def load_gtdb_local(gtdb_path: Optional[Path]) -> Optional[Dict]:
    """Load local GTDB database if available"""
    if not gtdb_path or not gtdb_path.exists():
        return None

    # This would load a local GTDB database file
    # Implementation depends on GTDB file format
    # For now, return None to indicate not implemented
    return None


def compare_classifications(ncbi_validation: NCBIValidation, gtdb_info: GTDBInfo) -> Tuple[bool, Optional[str]]:
    """Compare NCBI and GTDB classifications to identify conflicts"""
    if not gtdb_info.found:
        return False, None

    # This is a simplified comparison
    # In reality, would need to fetch NCBI lineage and compare
    # For now, just flag if GTDB has different species name

    conflicts = False
    details = None

    # Placeholder for actual comparison logic

    return conflicts, details


def generate_report(
    perfect_matches: List[Tuple[TaxonInfo, NCBIValidation, GTDBInfo]],
    species_fallbacks: List[Tuple[TaxonInfo, NCBIValidation, GTDBInfo]],
    wrong_level: List[Tuple[TaxonInfo, NCBIValidation, GTDBInfo]],
    strain_not_in_db: List[Tuple[TaxonInfo, NCBIValidation, GTDBInfo]],
    mismatches: List[Tuple[TaxonInfo, NCBIValidation, GTDBInfo]],
    taxonomy_updates: List[Tuple[TaxonInfo, NCBIValidation, GTDBInfo]],
    conflicts: List[Tuple[TaxonInfo, NCBIValidation, GTDBInfo]],
    not_in_gtdb: List[Tuple[TaxonInfo, NCBIValidation, GTDBInfo]],
    strain_stats: Dict
):
    """Generate comprehensive strain-aware comparison report"""

    total = (len(perfect_matches) + len(species_fallbacks) + len(wrong_level) +
             len(strain_not_in_db) + len(mismatches))

    print(f"\n{Colors.BOLD}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}STRAIN-RESOLVED TAXONOMY VALIDATION REPORT{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*80}{Colors.RESET}\n")

    # Summary Statistics
    print(f"{Colors.BOLD}{Colors.CYAN}SUMMARY STATISTICS{Colors.RESET}")
    print(f"{'-'*80}")
    print(f"Total taxa analyzed: {total}")
    print(f"Perfect strain-level matches: {len(perfect_matches)} ({len(perfect_matches)/total*100:.1f}%)" if total > 0 else "Perfect matches: 0")
    print(f"Species-level fallback (acceptable): {len(species_fallbacks)} ({len(species_fallbacks)/total*100:.1f}%)" if total > 0 else "Species fallback: 0")
    print(f"Wrong taxonomy level: {len(wrong_level)} ({len(wrong_level)/total*100:.1f}%)" if total > 0 else "Wrong level: 0")
    print(f"Strain not in databases: {len(strain_not_in_db)} ({len(strain_not_in_db)/total*100:.1f}%)" if total > 0 else "Strain not in DB: 0")
    print(f"NCBITaxon ID mismatches: {len(mismatches)} ({len(mismatches)/total*100:.1f}%)" if total > 0 else "Mismatches: 0")
    print(f"Taxonomy updates/synonyms: {len(taxonomy_updates)}")
    print(f"NCBI/GTDB conflicts: {len(conflicts)}")
    print(f"Not found in GTDB: {len(not_in_gtdb)}")
    print()

    # Strain resolution statistics
    print(f"{Colors.BOLD}{Colors.CYAN}STRAIN RESOLUTION STATISTICS{Colors.RESET}")
    print(f"{'-'*80}")
    print(f"Total taxa with strain designation: {strain_stats['with_strain']} ({strain_stats['with_strain']/total*100:.1f}%)" if total > 0 else "With strain: 0")
    print(f"  - Strain-specific NCBITaxon ID available: {strain_stats['strain_in_ncbi']} ({strain_stats['strain_in_ncbi']/strain_stats['with_strain']*100:.1f}%)" if strain_stats['with_strain'] > 0 else "  - Strain in NCBI: 0")
    print(f"  - Species-level fallback used: {strain_stats['species_fallback']} ({strain_stats['species_fallback']/strain_stats['with_strain']*100:.1f}%)" if strain_stats['with_strain'] > 0 else "  - Species fallback: 0")
    print(f"  - Strain in GTDB only: {strain_stats['strain_gtdb_only']}")
    print(f"  - Strain in neither database: {strain_stats['strain_neither']}")
    print()
    print(f"Total taxa without strain (species-level): {strain_stats['without_strain']} ({strain_stats['without_strain']/total*100:.1f}%)" if total > 0 else "Without strain: 0")
    print()
    print(f"Strain-level improvements possible: {len(wrong_level)}")
    print()

    # A. Perfect Strain-Level Matches
    if perfect_matches:
        print(f"{Colors.BOLD}{Colors.GREEN}A. PERFECT STRAIN-LEVEL MATCHES ({len(perfect_matches)}){Colors.RESET}")
        print(f"{'-'*80}")
        for taxon, ncbi_val, gtdb_info in perfect_matches[:5]:  # Show first 5
            strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)
            print(f"{Colors.GREEN}✓{Colors.RESET} {taxon.preferred_term}")
            print(f"  Literature: \"{taxon.preferred_term}\"")
            if strain_info.strain_designation:
                print(f"  Strain: {strain_info.strain_designation}")
            print(f"  Current NCBITaxon:{taxon.ncbi_id} → \"{ncbi_val.ncbi_current_label}\" {Colors.GREEN}✓{Colors.RESET}")
            if gtdb_info.found and gtdb_info.lineage:
                print(f"  GTDB: {gtdb_info.lineage}")
            print(f"  STATUS: CORRECT - Strain-specific ID used")
            print()

        if len(perfect_matches) > 5:
            print(f"  ... and {len(perfect_matches) - 5} more")
            print()

    # B. Species-Level Fallback (Acceptable)
    if species_fallbacks:
        print(f"{Colors.BOLD}{Colors.YELLOW}B. SPECIES-LEVEL FALLBACK (Acceptable) ({len(species_fallbacks)}){Colors.RESET}")
        print(f"{'-'*80}")
        for taxon, ncbi_val, gtdb_info in species_fallbacks:
            strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)
            print(f"{Colors.YELLOW}⚠{Colors.RESET} {taxon.preferred_term}")
            print(f"  Literature: \"{taxon.preferred_term}\" (strain specified: {strain_info.strain_designation})")
            print(f"  Current NCBITaxon:{taxon.ncbi_id} → \"{ncbi_val.ncbi_current_label}\" (species level)")
            print(f"  Strain search: No NCBITaxon entry for \"{strain_info.strain_designation}\"")
            if gtdb_info.found and gtdb_info.lineage:
                print(f"  GTDB: {gtdb_info.lineage}")
            print(f"  STATUS: ACCEPTABLE - Use species ID, document strain in notes")
            print(f"  SUGGESTION: Add to notes: \"Strain {strain_info.strain_designation}\"")
            print(f"  File: {taxon.file_name}")
            print()

    # C. Wrong Taxonomy Level
    if wrong_level:
        print(f"{Colors.BOLD}{Colors.RED}C. WRONG TAXONOMY LEVEL ({len(wrong_level)}){Colors.RESET}")
        print(f"{'-'*80}")
        for taxon, ncbi_val, gtdb_info in wrong_level:
            strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)
            print(f"{Colors.RED}✗{Colors.RESET} {taxon.preferred_term}")
            print(f"  Literature: \"{taxon.preferred_term}\" (strain: {strain_info.strain_designation})")
            print(f"  Current NCBITaxon:{taxon.ncbi_id} → \"{ncbi_val.ncbi_current_label}\" (species) ✓")
            if ncbi_val.strain_level_id:
                print(f"  Strain NCBITaxon:{ncbi_val.strain_level_id} → \"{ncbi_val.strain_level_label}\" EXISTS!")
                print(f"  {Colors.BOLD}ACTION: Update to NCBITaxon:{ncbi_val.strain_level_id} for strain resolution{Colors.RESET}")
            print(f"  File: {taxon.file_name}")
            print()

    # D. Strain Not in Databases
    if strain_not_in_db:
        print(f"{Colors.BOLD}{Colors.CYAN}D. STRAIN NOT IN DATABASES ({len(strain_not_in_db)}){Colors.RESET}")
        print(f"{'-'*80}")
        for taxon, ncbi_val, gtdb_info in strain_not_in_db:
            strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)
            print(f"{Colors.CYAN}ℹ{Colors.RESET} {taxon.preferred_term}")
            print(f"  Literature: \"{taxon.preferred_term}\"")
            print(f"  Strain: {strain_info.strain_designation}")
            if ncbi_val.species_level_id:
                print(f"  NCBITaxon species: {ncbi_val.species_level_id} \"{ncbi_val.species_level_label}\" (found)")
            print(f"  NCBITaxon strain: Not found for \"{strain_info.strain_designation}\"")
            print(f"  GTDB: Not found")
            print(f"  RECOMMENDATION: Use NCBITaxon:{ncbi_val.species_level_id} (species), add notes:")
            print(f"    \"Specific strain: {strain_info.strain_designation} (not in NCBITaxon/GTDB)\"")
            print(f"  File: {taxon.file_name}")
            print()

    # E. NCBITaxon ID Mismatches
    if mismatches:
        print(f"{Colors.BOLD}{Colors.RED}E. NCBITAXON ID MISMATCHES ({len(mismatches)}){Colors.RESET}")
        print(f"{'-'*80}")
        for taxon, ncbi_val, gtdb_info in mismatches:
            print(f"{Colors.RED}✗{Colors.RESET} {taxon.preferred_term}")
            print(f"  Literature: \"{taxon.preferred_term}\" {Colors.YELLOW}(SOURCE OF TRUTH){Colors.RESET}")
            print(f"  Current NCBITaxon:{taxon.ncbi_id} → \"{ncbi_val.ncbi_current_label}\" {Colors.RED}✗{Colors.RESET}")
            if ncbi_val.suggested_ncbi_id:
                print(f"  Suggested NCBITaxon:{ncbi_val.suggested_ncbi_id} → \"{ncbi_val.suggested_ncbi_label}\"")
            if gtdb_info.found and gtdb_info.lineage:
                print(f"  GTDB: {gtdb_info.lineage}")
            print(f"  File: {taxon.file_name}")
            print()

    print(f"{Colors.BOLD}{'='*80}{Colors.RESET}\n")


def write_output_files(
    all_results: List[Tuple[TaxonInfo, NCBIValidation, GTDBInfo]],
    output_dir: Path
):
    """Write output files with strain-aware validation results"""

    # 1. NCBITaxon corrections file with strain columns
    corrections_file = output_dir / 'ncbitaxon_corrections.tsv'
    with open(corrections_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['file', 'preferred_term', 'strain', 'current_id', 'current_label',
                        'recommended_id', 'recommended_label', 'taxonomy_level', 'action', 'notes'])

        for taxon, ncbi_val, gtdb_info in all_results:
            strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)

            # Determine if correction is needed
            if ncbi_val.suggested_ncbi_id and ncbi_val.suggested_ncbi_id != taxon.ncbi_id:
                action = "UPDATE"
                recommended_id = ncbi_val.suggested_ncbi_id
                recommended_label = ncbi_val.suggested_ncbi_label
            elif ncbi_val.recommendation == "USE_STRAIN" and ncbi_val.strain_level_id != taxon.ncbi_id:
                action = "UPGRADE_TO_STRAIN"
                recommended_id = ncbi_val.strain_level_id
                recommended_label = ncbi_val.strain_level_label
            elif ncbi_val.recommendation == "USE_SPECIES" and not strain_info.strain_designation:
                action = "OK"
                recommended_id = taxon.ncbi_id
                recommended_label = ncbi_val.ncbi_current_label
            elif ncbi_val.recommendation == "USE_SPECIES" and strain_info.strain_designation:
                action = "ACCEPTABLE_FALLBACK"
                recommended_id = ncbi_val.species_level_id or taxon.ncbi_id
                recommended_label = ncbi_val.species_level_label or ncbi_val.ncbi_current_label
            else:
                action = "REVIEW"
                recommended_id = ncbi_val.suggested_ncbi_id or taxon.ncbi_id
                recommended_label = ncbi_val.suggested_ncbi_label or ncbi_val.ncbi_current_label

            taxonomy_level = "STRAIN" if strain_info.strain_designation and ncbi_val.strain_level_id else "SPECIES"

            notes_text = ""
            if strain_info.strain_designation and not ncbi_val.strain_level_id:
                notes_text = f"Strain {strain_info.strain_designation} not in NCBITaxon - using species level"

            writer.writerow([
                taxon.file_name,
                taxon.preferred_term,
                strain_info.strain_designation or "",
                taxon.ncbi_id,
                ncbi_val.ncbi_current_label or 'NOT_FOUND',
                recommended_id,
                recommended_label or 'NO_SUGGESTION',
                taxonomy_level,
                action,
                notes_text
            ])

    print(f"{Colors.GREEN}✓{Colors.RESET} Written: {corrections_file}")

    # 2. Strain resolution summary file
    strain_summary_file = output_dir / 'strain_resolution_summary.tsv'
    with open(strain_summary_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['preferred_term', 'strain', 'has_strain_ncbi', 'has_strain_gtdb',
                        'ncbi_strain_id', 'gtdb_genome_id', 'resolution_status'])

        for taxon, ncbi_val, gtdb_info in all_results:
            strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)

            if strain_info.strain_designation:
                has_strain_ncbi = "YES" if ncbi_val.strain_level_id else "NO"
                has_strain_gtdb = "YES" if gtdb_info.found else "UNKNOWN"

                if ncbi_val.strain_level_id:
                    resolution_status = "STRAIN_LEVEL"
                elif ncbi_val.species_level_id:
                    resolution_status = "SPECIES_FALLBACK"
                else:
                    resolution_status = "NOT_FOUND"

                writer.writerow([
                    taxon.preferred_term,
                    strain_info.strain_designation,
                    has_strain_ncbi,
                    has_strain_gtdb,
                    ncbi_val.strain_level_id or "",
                    gtdb_info.genome_id or "",
                    resolution_status
                ])

    print(f"{Colors.GREEN}✓{Colors.RESET} Written: {strain_summary_file}")

    # 3. GTDB classifications file
    gtdb_file = output_dir / 'gtdb_classifications.tsv'
    with open(gtdb_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['preferred_term', 'strain', 'ncbi_id', 'gtdb_found', 'gtdb_lineage',
                        'domain', 'phylum', 'class', 'order', 'family', 'genus', 'species'])

        for taxon, ncbi_val, gtdb_info in all_results:
            strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)

            if gtdb_info.found:
                classification = gtdb_info.classification or {}
                writer.writerow([
                    taxon.preferred_term,
                    strain_info.strain_designation or "",
                    taxon.ncbi_id,
                    'YES',
                    gtdb_info.lineage,
                    classification.get('domain', ''),
                    classification.get('phylum', ''),
                    classification.get('class', ''),
                    classification.get('order', ''),
                    classification.get('family', ''),
                    classification.get('genus', ''),
                    classification.get('species', '')
                ])
            else:
                writer.writerow([
                    taxon.preferred_term,
                    strain_info.strain_designation or "",
                    taxon.ncbi_id,
                    'NO',
                    '',
                    '', '', '', '', '', '', ''
                ])

    print(f"{Colors.GREEN}✓{Colors.RESET} Written: {gtdb_file}")

    # 4. Detailed text report
    report_file = output_dir / 'taxonomy_comparison_report.txt'

    # Redirect stdout to capture the report
    import io
    old_stdout = sys.stdout
    sys.stdout = text_buffer = io.StringIO()

    # Categorize results for report
    perfect_matches = []
    species_fallbacks = []
    wrong_level = []
    strain_not_in_db = []
    mismatches = []
    taxonomy_updates = []
    conflicts = []
    not_in_gtdb = [r for r in all_results if not r[2].found]

    strain_stats = {
        'with_strain': 0,
        'without_strain': 0,
        'strain_in_ncbi': 0,
        'species_fallback': 0,
        'strain_gtdb_only': 0,
        'strain_neither': 0
    }

    for taxon, ncbi_val, gtdb_info in all_results:
        strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)

        if strain_info.strain_designation:
            strain_stats['with_strain'] += 1

            if ncbi_val.strain_level_id:
                strain_stats['strain_in_ncbi'] += 1
                if ncbi_val.is_match and taxon.ncbi_id == ncbi_val.strain_level_id:
                    perfect_matches.append((taxon, ncbi_val, gtdb_info))
                elif taxon.ncbi_id == ncbi_val.species_level_id:
                    wrong_level.append((taxon, ncbi_val, gtdb_info))
                else:
                    mismatches.append((taxon, ncbi_val, gtdb_info))
            elif ncbi_val.species_level_id:
                strain_stats['species_fallback'] += 1
                if taxon.ncbi_id == ncbi_val.species_level_id:
                    species_fallbacks.append((taxon, ncbi_val, gtdb_info))
                else:
                    mismatches.append((taxon, ncbi_val, gtdb_info))
            else:
                strain_stats['strain_neither'] += 1
                strain_not_in_db.append((taxon, ncbi_val, gtdb_info))
        else:
            strain_stats['without_strain'] += 1
            if ncbi_val.is_match:
                if ncbi_val.is_synonym:
                    taxonomy_updates.append((taxon, ncbi_val, gtdb_info))
                else:
                    perfect_matches.append((taxon, ncbi_val, gtdb_info))
            else:
                mismatches.append((taxon, ncbi_val, gtdb_info))

    # Generate the report
    generate_report(perfect_matches, species_fallbacks, wrong_level, strain_not_in_db,
                   mismatches, taxonomy_updates, conflicts, not_in_gtdb, strain_stats)

    # Get the report text
    report_text = text_buffer.getvalue()

    # Restore stdout
    sys.stdout = old_stdout

    # Write to file (without color codes)
    clean_text = re.sub(r'\033\[[0-9;]+m', '', report_text)

    with open(report_file, 'w') as f:
        f.write(clean_text)

    print(f"{Colors.GREEN}✓{Colors.RESET} Written: {report_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Compare NCBITaxonomy and GTDB against literature-derived species names with strain-level resolution'
    )
    parser.add_argument(
        '--kb-dir',
        type=Path,
        default=Path(__file__).parent.parent / 'kb',
        help='Path to kb directory containing YAML files (default: ../kb)'
    )
    parser.add_argument(
        '--gtdb-path',
        type=Path,
        default=None,
        help='Path to local GTDB database (optional)'
    )
    parser.add_argument(
        '--skip-gtdb',
        action='store_true',
        help='Skip GTDB validation (only validate against NCBI)'
    )
    parser.add_argument(
        '--use-gtdb',
        action='store_true',
        help='Use local GTDB database for validation (requires gtdb_integration.py --load)'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path.cwd(),
        help='Output directory for reports (default: current directory)'
    )
    parser.add_argument(
        '--db-path',
        type=Path,
        default=Path('kgm_taxonomy.duckdb'),
        help='DuckDB database path (default: kgm_taxonomy.duckdb)'
    )

    args = parser.parse_args()

    print(f"\n{Colors.BOLD}{Colors.CYAN}Strain-Resolved Taxonomy Validation Script{Colors.RESET}")
    print(f"{Colors.CYAN}Source of Truth: preferred_term (from literature){Colors.RESET}")
    print(f"{Colors.CYAN}Hierarchy: Literature Strain → NCBI Strain → NCBI Species → GTDB{Colors.RESET}\n")

    # Check dependencies
    if not OAKLIB_AVAILABLE:
        print(f"{Colors.RED}Error: oaklib is required. Install with: pip install oaklib{Colors.RESET}")
        sys.exit(1)

    # Initialize NCBI adapter
    print(f"{Colors.CYAN}Initializing NCBITaxon adapter...{Colors.RESET}")
    try:
        ncbi_adapter = get_adapter("sqlite:obo:ncbitaxon")
        print(f"{Colors.GREEN}✓{Colors.RESET} NCBITaxon adapter ready\n")
    except Exception as e:
        print(f"{Colors.RED}Error initializing NCBI adapter: {e}{Colors.RESET}")
        print(f"{Colors.YELLOW}You may need to run: runoak -i sqlite:obo:ncbitaxon info{Colors.RESET}")
        sys.exit(1)

    # Initialize GTDB connection if requested
    gtdb_conn = None
    if args.use_gtdb:
        try:
            import duckdb
            gtdb_conn = duckdb.connect(str(args.db_path))
            # Test if GTDB tables exist
            count = gtdb_conn.execute("SELECT COUNT(*) FROM gtdb_taxonomy").fetchone()[0]
            print(f"{Colors.GREEN}✓{Colors.RESET} GTDB database ready ({count:,} genomes)\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Warning: Could not load GTDB database: {e}{Colors.RESET}")
            print(f"{Colors.YELLOW}Run: python scripts/gtdb_integration.py --download --load{Colors.RESET}\n")
            gtdb_conn = None

    # Collect taxa from YAML files
    all_taxa = collect_all_taxa(args.kb_dir)

    if not all_taxa:
        print(f"{Colors.RED}No taxa found in {args.kb_dir}{Colors.RESET}")
        sys.exit(1)

    # Validate against NCBI
    print(f"{Colors.CYAN}Validating against NCBITaxonomy with strain-level resolution...{Colors.RESET}")
    results = []

    for i, taxon in enumerate(all_taxa, 1):
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(all_taxa)}")

        ncbi_validation = validate_ncbi_taxonomy(taxon, ncbi_adapter)

        # GTDB validation
        gtdb_info = GTDBInfo(found=False, lineage=None, classification=None)
        if not args.skip_gtdb:
            strain_info = extract_strain_info(taxon.preferred_term, taxon.notes)

            if gtdb_conn:
                # Use local GTDB database
                gtdb_info = query_gtdb_local(taxon.preferred_term, gtdb_conn)
            else:
                # Fallback to API (may not work)
                gtdb_info = query_gtdb_api(taxon.preferred_term)

        results.append((taxon, ncbi_validation, gtdb_info))

    print(f"{Colors.GREEN}✓{Colors.RESET} Validation complete\n")

    # Write output files (which also generates the report)
    print(f"{Colors.CYAN}Writing output files...{Colors.RESET}")
    write_output_files(results, args.output_dir)

    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Strain-resolved taxonomy validation complete!{Colors.RESET}\n")

    # Print GTDB note if applicable
    if not args.skip_gtdb and not gtdb_conn:
        print(f"{Colors.YELLOW}Note: GTDB validation not performed (database not loaded).{Colors.RESET}")
        print(f"{Colors.YELLOW}To enable GTDB validation:{Colors.RESET}")
        print(f"{Colors.YELLOW}  1. python scripts/gtdb_integration.py --download{Colors.RESET}")
        print(f"{Colors.YELLOW}  2. python scripts/gtdb_integration.py --load{Colors.RESET}")
        print(f"{Colors.YELLOW}  3. python scripts/compare_ncbi_gtdb_taxonomy.py --use-gtdb{Colors.RESET}\n")


if __name__ == '__main__':
    main()
