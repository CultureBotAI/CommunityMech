#!/usr/bin/env python3
"""
Phase 3: Apply Taxonomy Corrections - Auto-update NCBITaxon IDs

Applies recommended taxonomy corrections from ncbitaxon_corrections.tsv
while preserving preferred_term (literature source of truth).
"""

import csv
import yaml
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

# Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


class TaxonomyCorrector:
    """Applies taxonomy corrections to YAML files"""

    def __init__(self, kb_dir: Path, corrections_file: Path):
        self.kb_dir = kb_dir
        self.corrections_file = corrections_file
        self.corrections = []
        self.stats = defaultdict(int)

    def load_corrections(self):
        """Load corrections from TSV file"""
        print(f"{Colors.CYAN}Loading corrections from {self.corrections_file.name}...{Colors.RESET}")

        with open(self.corrections_file, 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                if row['action'] == 'UPDATE':
                    self.corrections.append(row)

        print(f"{Colors.GREEN}✓{Colors.RESET} Loaded {len(self.corrections)} corrections")

    def apply_correction(self, yaml_path: Path, correction: Dict) -> bool:
        """Apply a single correction to a YAML file"""

        # Read YAML
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        if 'taxonomy' not in data:
            return False

        updated = False

        # Find matching taxon by preferred_term (source of truth)
        for taxon_entry in data['taxonomy']:
            if 'taxon_term' not in taxon_entry:
                continue

            taxon = taxon_entry['taxon_term']
            preferred_term = taxon.get('preferred_term', '')

            # Match by preferred_term
            if preferred_term == correction['preferred_term']:
                current_id = taxon.get('term', {}).get('id', '')

                # Strip NCBITaxon: prefix if present for comparison
                current_id_stripped = current_id.replace('NCBITaxon:', '')
                expected_id_stripped = correction['current_id']

                # Check if current ID matches what we expect
                if current_id_stripped == expected_id_stripped:
                    # Update the ID (keeping NCBITaxon: prefix if it was there)
                    if 'term' not in taxon:
                        taxon['term'] = {}

                    old_id = taxon['term'].get('id', 'None')
                    recommended_id = correction['recommended_id']

                    # Add NCBITaxon: prefix if original had it
                    if current_id.startswith('NCBITaxon:'):
                        recommended_id = f"NCBITaxon:{recommended_id}"

                    taxon['term']['id'] = recommended_id
                    taxon['term']['label'] = correction['recommended_label']

                    print(f"  {Colors.GREEN}✓{Colors.RESET} {preferred_term}")
                    print(f"    {old_id} → {recommended_id}")

                    updated = True
                    self.stats['taxa_updated'] += 1
                else:
                    # ID doesn't match expected - may have been manually fixed
                    print(f"  {Colors.YELLOW}⊙{Colors.RESET} {preferred_term}: ID mismatch (expected {expected_id_stripped}, found {current_id_stripped})")
                    self.stats['skipped_mismatch'] += 1

        if not updated:
            return False

        # Create backup
        backup_path = yaml_path.with_suffix('.yaml.bak2')
        yaml_path.rename(backup_path)

        # Write updated YAML
        try:
            with open(yaml_path, 'w') as f:
                yaml.dump(data, f,
                         default_flow_style=False,
                         sort_keys=False,
                         allow_unicode=True,
                         width=120,
                         indent=2)
            self.stats['files_updated'] += 1
            return True
        except Exception as e:
            # Restore backup on error
            backup_path.rename(yaml_path)
            print(f"{Colors.RED}✗{Colors.RESET} Error updating {yaml_path.name}: {e}")
            return False

    def apply_all_corrections(self):
        """Apply all corrections to relevant YAML files"""
        print(f"\n{Colors.CYAN}Applying corrections to YAML files...{Colors.RESET}\n")

        # Group corrections by file
        corrections_by_file = defaultdict(list)
        for correction in self.corrections:
            yaml_filename = correction['file']
            corrections_by_file[yaml_filename].append(correction)

        # Process each file
        for yaml_filename, file_corrections in sorted(corrections_by_file.items()):
            yaml_path = self.kb_dir / yaml_filename
            if not yaml_path.exists():
                print(f"{Colors.RED}✗{Colors.RESET} File not found: {yaml_filename}")
                continue

            print(f"{Colors.BLUE}{yaml_filename}{Colors.RESET}")

            for correction in file_corrections:
                self.apply_correction(yaml_path, correction)

            print()

    def print_summary(self):
        """Print summary statistics"""
        print(f"{Colors.BOLD}{Colors.CYAN}Correction Summary:{Colors.RESET}")
        print(f"  Total corrections attempted: {len(self.corrections)}")
        print(f"  Files updated: {self.stats['files_updated']}")
        print(f"  Taxa updated: {self.stats['taxa_updated']}")
        print(f"  Skipped (ID mismatch): {self.stats['skipped_mismatch']}")


def main():
    print(f"{Colors.BOLD}{Colors.CYAN}Phase 3: Apply Taxonomy Corrections{Colors.RESET}")
    print(f"{Colors.CYAN}Auto-updating NCBITaxon IDs (preserving preferred_term){Colors.RESET}\n")

    # Paths
    kb_dir = Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CommunityMech/CommunityMech/kb/communities')
    corrections_file = Path('ncbitaxon_corrections.tsv')

    if not corrections_file.exists():
        print(f"{Colors.RED}✗{Colors.RESET} Corrections file not found: {corrections_file}")
        print(f"{Colors.CYAN}Run 'poetry run python scripts/compare_ncbi_gtdb_taxonomy.py' first{Colors.RESET}")
        return

    # Initialize corrector
    corrector = TaxonomyCorrector(kb_dir, corrections_file)

    # Load corrections
    corrector.load_corrections()

    # Apply corrections
    corrector.apply_all_corrections()

    # Print summary
    corrector.print_summary()

    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Phase 3 complete!{Colors.RESET}")
    print(f"\n{Colors.CYAN}Next steps:{Colors.RESET}")
    print(f"  1. Validate updated files: just validate kb/communities/*.yaml")
    print(f"  2. Review changes: git diff kb/communities/")
    print(f"  3. Test browser: just gen-browser && just serve")

if __name__ == '__main__':
    main()
