#!/usr/bin/env python3
"""
Fix Reference Format Issues in Community YAMLs

Standardizes references to proper formats:
- pmid:123 → PMID:123
- PMC123 → PMID:PMC123
- DOI:10.xxx → doi:10.xxx
"""

import yaml
import re
from pathlib import Path
from typing import Dict, List, Tuple


def fix_reference(ref: str) -> Tuple[str, bool]:
    """
    Fix reference format.

    Returns: (fixed_reference, was_changed)
    """
    original = ref

    # Fix lowercase pmid
    if ref.startswith('pmid:'):
        ref = 'PMID:' + ref[5:]

    # Fix PMC without prefix
    if re.match(r'^PMC\d+$', ref):
        ref = 'PMID:' + ref

    # Fix uppercase DOI
    if ref.startswith('DOI:'):
        ref = 'doi:' + ref[4:]

    # Fix doi without prefix (if looks like DOI pattern)
    if re.match(r'^10\.\d+/', ref):
        ref = 'doi:' + ref

    return (ref, ref != original)


def fix_yaml_file(yaml_path: Path, dry_run: bool = True) -> Dict:
    """Fix references in a YAML file"""

    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    changes = []

    # Fix taxonomy evidence
    if 'taxonomy' in data:
        for taxon in data['taxonomy']:
            if 'evidence' in taxon:
                for ev in taxon['evidence']:
                    if 'reference' in ev:
                        fixed, changed = fix_reference(ev['reference'])
                        if changed:
                            changes.append((ev['reference'], fixed, 'taxonomy'))
                            if not dry_run:
                                ev['reference'] = fixed

    # Fix interaction evidence
    if 'ecological_interactions' in data:
        for interaction in data['ecological_interactions']:
            if 'evidence' in interaction:
                for ev in interaction['evidence']:
                    if 'reference' in ev:
                        fixed, changed = fix_reference(ev['reference'])
                        if changed:
                            changes.append((ev['reference'], fixed, 'interaction'))
                            if not dry_run:
                                ev['reference'] = fixed

    # Fix environmental evidence
    if 'environmental_factors' in data:
        for factor in data['environmental_factors']:
            if 'evidence' in factor:
                for ev in factor['evidence']:
                    if 'reference' in ev:
                        fixed, changed = fix_reference(ev['reference'])
                        if changed:
                            changes.append((ev['reference'], fixed, 'environmental'))
                            if not dry_run:
                                ev['reference'] = fixed

    # Write back if not dry run
    if not dry_run and changes:
        # Create backup
        backup_path = yaml_path.with_suffix('.yaml.bak3')
        yaml_path.rename(backup_path)

        # Write updated YAML
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

    parser = argparse.ArgumentParser(description="Fix reference formats in YAML files")
    parser.add_argument('--apply', action='store_true', help="Apply changes (default: dry run)")
    args = parser.parse_args()

    kb_dir = Path('kb/communities')
    yaml_files = sorted(kb_dir.glob('*.yaml'))

    print(f"Reference Format Fixer")
    print(f"Mode: {'APPLY CHANGES' if args.apply else 'DRY RUN (no changes)'}")
    print("=" * 80)
    print()

    total_changes = 0
    files_affected = 0
    all_results = []

    for yaml_path in yaml_files:
        result = fix_yaml_file(yaml_path, dry_run=not args.apply)

        if result['count'] > 0:
            all_results.append(result)
            total_changes += result['count']
            files_affected += 1

            print(f"{result['file']}: {result['count']} changes")
            for old, new, context in result['changes'][:3]:  # Show first 3
                print(f"  {old} → {new} ({context})")
            if result['count'] > 3:
                print(f"  ... and {result['count']-3} more")
            print()

    print("=" * 80)
    print(f"Total: {total_changes} references in {files_affected} files")

    if not args.apply:
        print()
        print("This was a DRY RUN. To apply changes:")
        print("  python scripts/fix_reference_formats.py --apply")
    else:
        print()
        print("✓ Changes applied! Backups saved as .yaml.bak3")
        print()
        print("Next: Re-run literature review to validate improvements")


if __name__ == '__main__':
    main()
