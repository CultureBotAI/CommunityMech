#!/usr/bin/env python3
"""
Automatically fix network data integrity issues in community YAML files.

Fixes:
1. NCBITaxon ID mismatches - replaces incorrect IDs with correct ones from taxonomy
2. Reports disconnected taxa and missing source/target for manual review
"""

import sys
from collections import defaultdict
from pathlib import Path

import yaml

from communitymech.curate.curation_event import record_curation_event
from communitymech.validation.write_validated import (
    ValidationFailedError,
    write_validated_community,
)


class NetworkIntegrityFixer:
    def __init__(self, communities_dir: Path = Path("kb/communities")):
        self.communities_dir = communities_dir
        self.fixes_applied = defaultdict(list)
        self.manual_review = defaultdict(list)

    def fix_all(self, dry_run: bool = True):
        """Fix all community YAML files."""
        yaml_files = sorted(self.communities_dir.glob("*.yaml"))

        print(f"\n🔧 {'DRY RUN: ' if dry_run else ''}Fixing network integrity issues in {len(yaml_files)} communities...\n")

        for yaml_file in yaml_files:
            self.fix_community(yaml_file, dry_run=dry_run)

        # Summary
        print(f"\n{'='*80}")
        print(f"Summary:")
        print(f"  Communities fixed: {len(self.fixes_applied)}")
        print(f"  Total ID fixes: {sum(len(fixes) for fixes in self.fixes_applied.values())}")
        print(f"  Communities needing manual review: {len(self.manual_review)}")
        print(f"{'='*80}\n")

        if self.manual_review:
            print("\n⚠️  Manual Review Required:\n")
            for community, issues in sorted(self.manual_review.items()):
                print(f"  {community}:")
                for issue in issues:
                    print(f"    • {issue}")

    def fix_community(self, yaml_path: Path, dry_run: bool = True) -> int:
        """Fix a single community file."""
        with open(yaml_path) as f:
            data = yaml.safe_load(f)

        # Build taxonomy lookup
        taxonomy_by_term = {}
        for taxon in data.get("taxonomy", []):
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")
            taxon_id = term.get("term", {}).get("id")

            if preferred:
                taxonomy_by_term[preferred] = {
                    "id": taxon_id,
                    "label": term.get("term", {}).get("label"),
                }

        fixes = 0
        interactions = data.get("ecological_interactions", [])
        connected_taxa = set()

        for interaction in interactions:
            int_name = interaction.get("name", "Unknown")

            # Fix source_taxon ID mismatches
            source = interaction.get("source_taxon")
            if source:
                source_term = source.get("preferred_term") or source.get("term", {}).get("label")
                if source_term in taxonomy_by_term:
                    connected_taxa.add(source_term)
                    expected_id = taxonomy_by_term[source_term]["id"]
                    actual_id = source.get("term", {}).get("id")

                    if actual_id != expected_id:
                        print(f"  ✓ {yaml_path.stem}: [{int_name}] source '{source_term}'")
                        print(f"    {actual_id} → {expected_id}")
                        source["term"]["id"] = expected_id
                        fixes += 1
                        self.fixes_applied[yaml_path.stem].append(
                            f"Fixed source '{source_term}' ID: {actual_id} → {expected_id}"
                        )
                else:
                    self.manual_review[yaml_path.stem].append(
                        f"[{int_name}] Unknown source taxon: {source_term}"
                    )
            else:
                self.manual_review[yaml_path.stem].append(
                    f"[{int_name}] Missing source_taxon"
                )

            # Fix target_taxon ID mismatches
            target = interaction.get("target_taxon")
            if target:
                target_term = target.get("preferred_term") or target.get("term", {}).get("label")
                if target_term in taxonomy_by_term:
                    connected_taxa.add(target_term)
                    expected_id = taxonomy_by_term[target_term]["id"]
                    actual_id = target.get("term", {}).get("id")

                    if actual_id != expected_id:
                        print(f"  ✓ {yaml_path.stem}: [{int_name}] target '{target_term}'")
                        print(f"    {actual_id} → {expected_id}")
                        target["term"]["id"] = expected_id
                        fixes += 1
                        self.fixes_applied[yaml_path.stem].append(
                            f"Fixed target '{target_term}' ID: {actual_id} → {expected_id}"
                        )
                else:
                    self.manual_review[yaml_path.stem].append(
                        f"[{int_name}] Unknown target taxon: {target_term}"
                    )

        # Check for disconnected taxa
        all_taxa = set(taxonomy_by_term.keys())
        disconnected = all_taxa - connected_taxa

        if disconnected and interactions:
            for taxon in sorted(disconnected):
                self.manual_review[yaml_path.stem].append(
                    f"Disconnected taxon: {taxon}"
                )

        # Write back if fixes were made and not dry run
        if fixes > 0 and not dry_run:
            applied = self.fixes_applied.get(yaml_path.stem, [])
            record_curation_event(
                data,
                curator="fix_network_integrity",
                action="FIX_NETWORK_INTEGRITY",
                changes=(
                    f"Repaired {fixes} taxon ID mismatch(es) in ecological_interactions: "
                    + "; ".join(applied[:5])
                    + (f"; +{len(applied) - 5} more" if len(applied) > 5 else "")
                ),
            )
            try:
                write_validated_community(data, yaml_path)
            except ValidationFailedError as exc:
                print(
                    f"  ✗ validation failed for {yaml_path.name}: {exc.summary()}",
                    file=sys.stderr,
                )
                return fixes
            print(f"    Wrote {fixes} fixes to {yaml_path.name}")

        return fixes


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Fix network integrity issues")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply fixes (default is dry run)",
    )
    parser.add_argument(
        "--community",
        help="Fix only this community (stem name)",
    )

    args = parser.parse_args()

    fixer = NetworkIntegrityFixer()

    if args.community:
        yaml_path = Path(f"kb/communities/{args.community}.yaml")
        if yaml_path.exists():
            print(f"\nFixing {args.community}...\n")
            fixer.fix_community(yaml_path, dry_run=not args.apply)
        else:
            print(f"Error: {yaml_path} not found")
    else:
        fixer.fix_all(dry_run=not args.apply)


if __name__ == "__main__":
    main()
