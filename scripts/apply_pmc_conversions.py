#!/usr/bin/env python3
"""
Apply PMC to PMID Conversions

Uses the conversions from special_references_report.txt to update
YAML files with proper PMID references.

Known conversions:
- PMC3694112 → PMID:23840525
- PMC9666448 → PMID:36123522
- PMC3911102 → PMID:24242252
- PMC9275249 → PMID:35708325
- PMC10785750 → PMID:38150661
- PMC10746061 → PMID:38138568
- PMC11678928 → PMID:39770610
- PMC6637823 → PMID:31354691
- PMC4187173 → PMID:25369810
"""

import yaml
import re
from pathlib import Path
from typing import Dict, List
from collections import defaultdict


# Known PMC → PMID conversions from special_references_report.txt
PMC_TO_PMID = {
    'PMC3694112': 'PMID:23840525',
    'PMC9666448': 'PMID:36123522',
    'PMC3911102': 'PMID:24242252',
    'PMC9275249': 'PMID:35708325',
    'PMC10785750': 'PMID:38150661',
    'PMC10746061': 'PMID:38138568',
    'PMC11678928': 'PMID:39770610',
    'PMC6637823': 'PMID:31354691',
    'PMC4187173': 'PMID:25369810',
}


def apply_pmc_conversions(yaml_path: Path, dry_run: bool = True) -> Dict:
    """Apply PMC→PMID conversions to a YAML file"""

    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    changes = []

    # Process taxonomy
    if 'taxonomy' in data:
        for taxon_entry in data['taxonomy']:
            if 'evidence' not in taxon_entry:
                continue

            for ev in taxon_entry['evidence']:
                ref = ev.get('reference', '')

                # Check for PMC-only format
                if ref.startswith('PMID:PMC'):
                    pmc_id = ref.replace('PMID:', '')
                    if pmc_id in PMC_TO_PMID:
                        old_ref = ref
                        new_ref = PMC_TO_PMID[pmc_id]
                        ev['reference'] = new_ref
                        changes.append((old_ref, new_ref, 'taxonomy'))
                elif ref in PMC_TO_PMID:
                    # PMC without PMID: prefix
                    old_ref = ref
                    new_ref = PMC_TO_PMID[ref]
                    ev['reference'] = new_ref
                    changes.append((old_ref, new_ref, 'taxonomy'))

    # Process interactions
    if 'ecological_interactions' in data:
        for interaction in data['ecological_interactions']:
            if 'evidence' not in interaction:
                continue

            for ev in interaction['evidence']:
                ref = ev.get('reference', '')

                if ref.startswith('PMID:PMC'):
                    pmc_id = ref.replace('PMID:', '')
                    if pmc_id in PMC_TO_PMID:
                        old_ref = ref
                        new_ref = PMC_TO_PMID[pmc_id]
                        ev['reference'] = new_ref
                        changes.append((old_ref, new_ref, 'interaction'))
                elif ref in PMC_TO_PMID:
                    old_ref = ref
                    new_ref = PMC_TO_PMID[ref]
                    ev['reference'] = new_ref
                    changes.append((old_ref, new_ref, 'interaction'))

    # Process environmental
    if 'environmental_factors' in data:
        for factor in data['environmental_factors']:
            if 'evidence' not in factor:
                continue

            for ev in factor['evidence']:
                ref = ev.get('reference', '')

                if ref.startswith('PMID:PMC'):
                    pmc_id = ref.replace('PMID:', '')
                    if pmc_id in PMC_TO_PMID:
                        old_ref = ref
                        new_ref = PMC_TO_PMID[pmc_id]
                        ev['reference'] = new_ref
                        changes.append((old_ref, new_ref, 'environmental'))
                elif ref in PMC_TO_PMID:
                    old_ref = ref
                    new_ref = PMC_TO_PMID[ref]
                    ev['reference'] = new_ref
                    changes.append((old_ref, new_ref, 'environmental'))

    # Write back if changes and not dry run
    if changes and not dry_run:
        # Backup
        backup_path = yaml_path.with_suffix('.yaml.bak_pmc')
        yaml_path.rename(backup_path)

        # Write updated
        with open(yaml_path, 'w') as f:
            yaml.dump(data, f,
                     default_flow_style=False,
                     sort_keys=False,
                     allow_unicode=True,
                     width=120,
                     indent=2)

    return {
        'file': yaml_path.name,
        'changes': changes,
        'count': len(changes)
    }


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Apply PMC→PMID conversions")
    parser.add_argument('--apply', action='store_true', help="Apply changes (default: dry run)")
    args = parser.parse_args()

    kb_dir = Path('kb/communities')
    yaml_files = sorted(kb_dir.glob('*.yaml'))

    print("PMC→PMID Conversion Tool")
    print("=" * 80)
    print(f"Mode: {'APPLY' if args.apply else 'DRY RUN'}")
    print(f"Known conversions: {len(PMC_TO_PMID)}")
    print()

    all_results = []
    total_changes = 0

    for yaml_path in yaml_files:
        result = apply_pmc_conversions(yaml_path, dry_run=not args.apply)

        if result['count'] > 0:
            all_results.append(result)
            total_changes += result['count']

            print(f"{result['file']}: {result['count']} conversions")
            for old, new, context in result['changes'][:3]:
                print(f"  {old} → {new} ({context})")
            if result['count'] > 3:
                print(f"  ... and {result['count']-3} more")
            print()

    print("=" * 80)
    print(f"Total: {total_changes} references converted in {len(all_results)} files")

    if not args.apply:
        print()
        print("This was a DRY RUN. To apply changes:")
        print("  python scripts/apply_pmc_conversions.py --apply")
    else:
        print()
        print("✓ Conversions applied! Backups saved as .yaml.bak_pmc")
        print()
        print("Next: Re-run curation audit to measure improvement")


if __name__ == '__main__':
    main()
