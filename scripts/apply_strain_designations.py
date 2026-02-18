#!/usr/bin/env python3
"""
Phase 2B: Apply Strain Designations - Update YAML files with strain data

Automatically applies extracted strain designations to community YAML files.
"""

import re
import yaml
import duckdb
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict

# Import from enhance_strain_data
import sys
sys.path.insert(0, str(Path(__file__).parent))
from enhance_strain_data import (
    StrainExtractor,
    Colors,
    CultureCollectionID,
    StrainInfo
)

class YAMLUpdater:
    """Updates YAML files with strain designations"""

    def __init__(self, kb_dir: Path):
        self.kb_dir = kb_dir
        self.stats = defaultdict(int)

    def update_yaml_file(self, yaml_path: Path, strain_data: Dict[str, StrainInfo]) -> bool:
        """Update a single YAML file with strain designations"""

        # Read original YAML content as text to preserve formatting
        with open(yaml_path, 'r') as f:
            content = f.read()

        # Parse YAML to get structure
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        if 'taxonomy' not in data:
            return False

        updates_made = False

        # Process each taxon
        for taxon_entry in data['taxonomy']:
            if 'taxon_term' not in taxon_entry:
                continue

            taxon = taxon_entry['taxon_term']
            preferred_term = taxon.get('preferred_term', '')

            # Check if we have strain data for this organism
            if preferred_term not in strain_data:
                continue

            # Check if strain_designation already exists
            if 'strain_designation' in taxon_entry:
                print(f"  {Colors.YELLOW}⊙{Colors.RESET} {preferred_term}: strain_designation already exists, skipping")
                continue

            strain_info = strain_data[preferred_term]

            # Generate YAML snippet
            snippet = self.generate_yaml_snippet(strain_info)
            if not snippet:
                continue

            # Find the position to insert the strain_designation
            # We want to add it after taxon_term but before abundance_level or functional_role

            # Find the taxon_term block for this organism
            # This is a simplified approach - we'll use ruamel.yaml for better control
            taxon_entry['strain_designation'] = snippet

            updates_made = True
            self.stats['taxa_updated'] += 1
            print(f"  {Colors.GREEN}✓{Colors.RESET} {preferred_term}: added strain_designation")

        if not updates_made:
            return False

        # Create backup
        backup_path = yaml_path.with_suffix('.yaml.bak')
        yaml_path.rename(backup_path)

        # Write updated content with PyYAML
        try:
            with open(yaml_path, 'w') as f:
                yaml.dump(data, f,
                         default_flow_style=False,
                         sort_keys=False,
                         allow_unicode=True,
                         width=120,
                         indent=2)
            print(f"{Colors.GREEN}✓{Colors.RESET} Updated: {yaml_path.name}")
            self.stats['files_updated'] += 1
            return True
        except Exception as e:
            # Restore backup on error
            backup_path.rename(yaml_path)
            print(f"{Colors.RED}✗{Colors.RESET} Error updating {yaml_path.name}: {e}")
            return False

    def generate_yaml_snippet(self, strain_info: StrainInfo) -> Optional[Dict]:
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

        return strain_dict if strain_dict else None

    def print_summary(self):
        """Print summary statistics"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}Update Summary:{Colors.RESET}")
        print(f"  Files updated: {self.stats['files_updated']}")
        print(f"  Taxa updated: {self.stats['taxa_updated']}")


def main():
    print(f"{Colors.BOLD}{Colors.CYAN}Phase 2B: Apply Strain Designations{Colors.RESET}")
    print(f"{Colors.CYAN}Automatically updating YAML files with strain data{Colors.RESET}\n")

    # Paths
    kb_dir = Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CommunityMech/CommunityMech/kb/communities')
    kgm_db = Path('kgm_taxonomy.duckdb')

    # Extract strain data first
    print(f"{Colors.CYAN}Step 1: Extracting strain information...{Colors.RESET}")
    extractor = StrainExtractor(kb_dir, kgm_db)
    extractor.connect_kgm()
    all_strain_data = extractor.process_all_communities()

    # Update YAML files
    print(f"\n{Colors.CYAN}Step 2: Updating YAML files...{Colors.RESET}")
    updater = YAMLUpdater(kb_dir)

    for yaml_path, strain_data in sorted(all_strain_data.items()):
        print(f"\n{Colors.BLUE}{yaml_path.name}{Colors.RESET}")
        updater.update_yaml_file(yaml_path, strain_data)

    # Print summary
    updater.print_summary()

    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Phase 2B complete!{Colors.RESET}")
    print(f"\n{Colors.CYAN}Next: Validate updated files with 'just validate'{Colors.RESET}")

if __name__ == '__main__':
    main()
