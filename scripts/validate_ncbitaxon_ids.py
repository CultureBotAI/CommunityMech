#!/usr/bin/env python3
"""
Validate NCBITaxon IDs in Community YAML Files using OAK

This script:
1. Extracts all NCBITaxon IDs from community YAML files
2. Validates each ID against NCBITaxonomy using OAK
3. Checks if the ID label matches the preferred_term (species name)
4. Generates a detailed validation report with suggestions for corrections
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import yaml
from collections import defaultdict

try:
    from oaklib import get_adapter
    from oaklib.interfaces import OboGraphInterface
except ImportError:
    print("ERROR: OAK (oaklib) not installed. Install with: pip install oaklib")
    sys.exit(1)


class NCBITaxonValidator:
    """Validates NCBITaxon IDs using OAK"""

    def __init__(self, communities_dir: str):
        self.communities_dir = Path(communities_dir)
        self.adapter = None
        self.results = {
            'matches': [],
            'mismatches': [],
            'missing': [],
            'errors': []
        }
        self.taxa_data = []

    def initialize_adapter(self):
        """Initialize OAK adapter for NCBITaxon"""
        print("Initializing OAK adapter for NCBITaxon...")
        print("This may take a few minutes on first run to download the database...")

        try:
            self.adapter = get_adapter("sqlite:obo:ncbitaxon")
            print("✓ NCBITaxon adapter initialized successfully\n")
        except Exception as e:
            print(f"ERROR: Failed to initialize OAK adapter: {e}")
            print("\nTroubleshooting:")
            print("1. Ensure you have internet connection (first run downloads NCBITaxon)")
            print("2. Try: runoak -i sqlite:obo:ncbitaxon info")
            print("3. Check OAK installation: pip install --upgrade oaklib")
            sys.exit(1)

    def extract_taxa_from_yaml(self, yaml_file: Path) -> List[Dict]:
        """Extract all taxa from a single YAML file"""
        taxa = []

        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if not data or 'taxonomy' not in data:
                return taxa

            for taxon_entry in data['taxonomy']:
                if 'taxon_term' in taxon_entry:
                    taxon_term = taxon_entry['taxon_term']

                    preferred_term = taxon_term.get('preferred_term', '')
                    term = taxon_term.get('term', {})
                    taxon_id = term.get('id', '')
                    term_label = term.get('label', '')

                    if taxon_id and taxon_id.startswith('NCBITaxon:'):
                        taxa.append({
                            'preferred_term': preferred_term,
                            'taxon_id': taxon_id,
                            'yaml_label': term_label,
                            'source_file': yaml_file.name
                        })

        except Exception as e:
            print(f"WARNING: Error parsing {yaml_file.name}: {e}")

        return taxa

    def extract_all_taxa(self):
        """Extract taxa from all YAML files"""
        print(f"Scanning YAML files in {self.communities_dir}...")

        yaml_files = list(self.communities_dir.glob("*.yaml"))
        print(f"Found {len(yaml_files)} YAML files\n")

        for yaml_file in sorted(yaml_files):
            taxa = self.extract_taxa_from_yaml(yaml_file)
            self.taxa_data.extend(taxa)

        print(f"Extracted {len(self.taxa_data)} NCBITaxon IDs from {len(yaml_files)} files\n")

    def validate_taxon(self, taxon_data: Dict) -> Tuple[str, Optional[str], Optional[str]]:
        """
        Validate a single taxon ID

        Returns:
            (status, oak_label, suggested_id)
            status: 'match', 'mismatch', 'missing', or 'error'
        """
        taxon_id = taxon_data['taxon_id']
        preferred_term = taxon_data['preferred_term']

        try:
            # Get label from OAK
            oak_label = self.adapter.label(taxon_id)

            if oak_label is None:
                return ('missing', None, None)

            # Check if labels match (case-insensitive comparison)
            if oak_label.lower() == preferred_term.lower():
                return ('match', oak_label, None)
            else:
                # Try to find correct ID
                suggested_id = self.find_correct_id(preferred_term)
                return ('mismatch', oak_label, suggested_id)

        except Exception as e:
            return ('error', None, str(e))

    def find_correct_id(self, species_name: str) -> Optional[str]:
        """Try to find the correct NCBITaxon ID for a species name"""
        try:
            # Search for the species name in NCBITaxon
            results = list(self.adapter.basic_search(species_name, config=None))

            if results:
                # Return the first exact match or best match
                for result in results[:3]:  # Check top 3 results
                    label = self.adapter.label(result)
                    if label and label.lower() == species_name.lower():
                        return result

                # If no exact match, return the first result
                return results[0]

        except Exception:
            pass

        return None

    def validate_all_taxa(self):
        """Validate all extracted taxa"""
        print("Validating NCBITaxon IDs...\n")

        total = len(self.taxa_data)
        for i, taxon_data in enumerate(self.taxa_data, 1):
            if i % 10 == 0 or i == total:
                print(f"Progress: {i}/{total} taxa validated", end='\r')

            status, oak_label, suggested_id = self.validate_taxon(taxon_data)

            result_data = {
                **taxon_data,
                'oak_label': oak_label,
                'suggested_id': suggested_id
            }

            if status == 'match':
                self.results['matches'].append(result_data)
            elif status == 'mismatch':
                self.results['mismatches'].append(result_data)
            elif status == 'missing':
                self.results['missing'].append(result_data)
            else:  # error
                result_data['error'] = suggested_id  # suggested_id contains error message
                self.results['errors'].append(result_data)

        print(f"\nValidation complete!\n")

    def generate_report(self):
        """Generate a detailed validation report"""
        print("=" * 80)
        print("NCBITaxon ID Validation Report")
        print("=" * 80)
        print()

        # Summary statistics
        total = len(self.taxa_data)
        matches = len(self.results['matches'])
        mismatches = len(self.results['mismatches'])
        missing = len(self.results['missing'])
        errors = len(self.results['errors'])

        print("SUMMARY")
        print("-" * 80)
        print(f"Total taxa checked:      {total}")
        print(f"✓ Matching IDs:          {matches} ({matches/total*100:.1f}%)")
        print(f"✗ Mismatched IDs:        {mismatches} ({mismatches/total*100:.1f}%)")
        print(f"? Missing/Invalid IDs:   {missing} ({missing/total*100:.1f}%)")
        print(f"⚠ Errors:                {errors} ({errors/total*100:.1f}%)")
        print()

        # Matching IDs
        if self.results['matches']:
            print("=" * 80)
            print(f"MATCHING IDs ({len(self.results['matches'])} taxa)")
            print("=" * 80)
            print()

            # Group by file
            by_file = defaultdict(list)
            for item in self.results['matches']:
                by_file[item['source_file']].append(item)

            for filename in sorted(by_file.keys()):
                print(f"File: {filename}")
                for item in by_file[filename]:
                    print(f"  ✓ {item['preferred_term']} → {item['taxon_id']}")
                print()

        # Mismatched IDs
        if self.results['mismatches']:
            print("=" * 80)
            print(f"MISMATCHED IDs ({len(self.results['mismatches'])} taxa)")
            print("=" * 80)
            print()

            for item in self.results['mismatches']:
                print(f"✗ {item['preferred_term']} → {item['taxon_id']}")
                print(f"  File: {item['source_file']}")
                print(f"  Expected: '{item['preferred_term']}'")
                print(f"  OAK says ID points to: '{item['oak_label']}'")

                if item['suggested_id']:
                    suggested_label = self.adapter.label(item['suggested_id'])
                    print(f"  💡 Suggestion: Use {item['suggested_id']} for '{suggested_label}'")
                else:
                    print(f"  💡 Suggestion: Could not find correct ID for '{item['preferred_term']}'")
                    print(f"     Manual verification needed!")

                print()

        # Missing/Invalid IDs
        if self.results['missing']:
            print("=" * 80)
            print(f"MISSING/INVALID IDs ({len(self.results['missing'])} taxa)")
            print("=" * 80)
            print()

            for item in self.results['missing']:
                print(f"? {item['preferred_term']} → {item['taxon_id']}")
                print(f"  File: {item['source_file']}")
                print(f"  Issue: ID not found in NCBITaxon database")

                suggested_id = self.find_correct_id(item['preferred_term'])
                if suggested_id:
                    suggested_label = self.adapter.label(suggested_id)
                    print(f"  💡 Suggestion: Use {suggested_id} for '{suggested_label}'")
                else:
                    print(f"  💡 Suggestion: Could not find ID for '{item['preferred_term']}'")
                    print(f"     Species may not exist in NCBITaxon or name is incorrect")

                print()

        # Errors
        if self.results['errors']:
            print("=" * 80)
            print(f"ERRORS ({len(self.results['errors'])} taxa)")
            print("=" * 80)
            print()

            for item in self.results['errors']:
                print(f"⚠ {item['preferred_term']} → {item['taxon_id']}")
                print(f"  File: {item['source_file']}")
                print(f"  Error: {item['error']}")
                print()

        # Final recommendations
        print("=" * 80)
        print("RECOMMENDATIONS")
        print("=" * 80)
        print()

        if mismatches > 0 or missing > 0:
            print("Action items:")
            print()

            if mismatches > 0:
                print(f"1. Review {mismatches} mismatched IDs:")
                print("   - Verify if the preferred_term is correct")
                print("   - Update the NCBITaxon ID to match the intended species")
                print("   - Use suggested IDs where provided")
                print()

            if missing > 0:
                print(f"2. Investigate {missing} missing/invalid IDs:")
                print("   - Check if species name spelling is correct")
                print("   - Verify species exists in NCBI Taxonomy")
                print("   - Consider if species has been renamed/merged")
                print()

            print("3. Tools for manual verification:")
            print("   - NCBI Taxonomy Browser: https://www.ncbi.nlm.nih.gov/taxonomy")
            print("   - OAK CLI: runoak -i sqlite:obo:ncbitaxon search 'species name'")
            print()
        else:
            print("✓ All NCBITaxon IDs are valid and match their preferred terms!")
            print("  No action needed.")
            print()

        print("=" * 80)

    def save_detailed_report(self, output_file: str):
        """Save detailed report to a text file"""
        import io
        from contextlib import redirect_stdout

        with open(output_file, 'w', encoding='utf-8') as f:
            with redirect_stdout(f):
                self.generate_report()

        print(f"\nDetailed report saved to: {output_file}")

    def run(self, save_report: bool = True):
        """Run the complete validation workflow"""
        self.initialize_adapter()
        self.extract_all_taxa()
        self.validate_all_taxa()
        self.generate_report()

        if save_report:
            base_dir = self.communities_dir.parent.parent
            report_file = base_dir / "ncbitaxon_validation_report.txt"
            self.save_detailed_report(str(report_file))


def main():
    """Main entry point"""
    # Set the communities directory
    script_dir = Path(__file__).parent
    communities_dir = script_dir.parent / "kb" / "communities"

    # Check if directory exists
    if not communities_dir.exists():
        print(f"ERROR: Communities directory not found: {communities_dir}")
        sys.exit(1)

    # Create validator and run
    validator = NCBITaxonValidator(str(communities_dir))
    validator.run()


if __name__ == "__main__":
    main()
