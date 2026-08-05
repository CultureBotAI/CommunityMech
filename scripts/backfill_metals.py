#!/usr/bin/env python3
"""Backfill metal and REE data for all community YAML files.

This script uses the metal_extraction module to automatically extract metal and REE
data from all communities and update the YAML files with the new fields.

Usage:
    python scripts/backfill_metals.py --dry-run          # Preview changes
    python scripts/backfill_metals.py                    # Apply changes
    python scripts/backfill_metals.py --community-id foo # Process single community
"""

import argparse
import sys
from pathlib import Path

import yaml

# Add src to path so we can import from communitymech
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.metal_extraction import extract_metals_from_community


def update_yaml_with_metals(
    yaml_path: Path, metals: list[str], ree: list[str], relevance: str, notes: str
) -> None:
    """Update a YAML file with metal/REE data.

    Preserves comments and formatting as much as possible using ruamel.yaml would be better,
    but for now we'll use standard yaml with manual formatting.
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    # Update the fields
    if metals:
        data["metals_present"] = metals
    if ree:
        data["rare_earth_elements_present"] = ree
    if relevance != "NOT_APPLICABLE":
        data["metal_relevance"] = relevance
    if notes:
        data["metal_notes"] = notes

    # Write back with clean formatting
    with open(yaml_path, "w") as f:
        yaml.dump(
            data,
            f,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=100,
        )


def backfill_single_community(community_id: str, dry_run: bool = True) -> None:
    """Backfill a single community by ID."""
    community_dir = Path("kb/communities")
    yaml_file = community_dir / f"{community_id}.yaml"

    if not yaml_file.exists():
        print(f"ERROR: Community file not found: {yaml_file}")
        return

    metals, ree, relevance, notes = extract_metals_from_community(yaml_file)

    print(f"\n{yaml_file.stem}:")
    print(f"  Metals: {metals if metals else 'None'}")
    print(f"  REE: {ree if ree else 'None'}")
    print(f"  Relevance: {relevance}")
    if notes:
        print(f"  Notes: {notes}")

    if not dry_run:
        update_yaml_with_metals(yaml_file, metals, ree, relevance, notes)
        print(f"  ✓ Updated {yaml_file.name}")


def backfill_all_communities(dry_run: bool = True, limit: int | None = None) -> None:
    """Backfill metal/REE data for all communities.

    Args:
        dry_run: If True, only print what would be done
        limit: If set, only process this many communities (for testing)
    """
    community_dir = Path("kb/communities")

    if not community_dir.exists():
        print(f"ERROR: Community directory not found: {community_dir}")
        return

    yaml_files = sorted(community_dir.glob("*.yaml"))

    if limit:
        yaml_files = yaml_files[:limit]

    print(f"Processing {len(yaml_files)} communities...")
    if dry_run:
        print("DRY RUN - No files will be modified\n")

    # Statistics
    stats = {
        "total": 0,
        "with_metals": 0,
        "with_ree": 0,
        "primary": 0,
        "significant": 0,
        "incidental": 0,
        "not_applicable": 0,
    }

    for yaml_file in yaml_files:
        metals, ree, relevance, notes = extract_metals_from_community(yaml_file)

        stats["total"] += 1
        if metals:
            stats["with_metals"] += 1
        if ree:
            stats["with_ree"] += 1

        relevance_key = relevance.lower()
        if relevance_key in stats:
            stats[relevance_key] += 1

        # Only print if there's metal/REE data
        if metals or ree or relevance != "NOT_APPLICABLE":
            print(f"\n{yaml_file.stem}:")
            print(f"  Metals: {metals if metals else 'None'}")
            print(f"  REE: {ree if ree else 'None'}")
            print(f"  Relevance: {relevance}")
            if notes:
                print(f"  Notes: {notes}")

            if not dry_run:
                update_yaml_with_metals(yaml_file, metals, ree, relevance, notes)
                print("  ✓ Updated")

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total communities: {stats['total']}")
    print(f"Communities with metals: {stats['with_metals']}")
    print(f"Communities with REE: {stats['with_ree']}")
    print("\nRelevance distribution:")
    print(f"  PRIMARY: {stats['primary']}")
    print(f"  SIGNIFICANT: {stats['significant']}")
    print(f"  INCIDENTAL: {stats['incidental']}")
    print(f"  NOT_APPLICABLE: {stats['not_applicable']}")

    if dry_run:
        print("\nTo apply these changes, run without --dry-run")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Backfill metal/REE data for communities")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files",
    )
    parser.add_argument(
        "--community-id",
        type=str,
        help="Process only a single community by ID",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of communities to process (for testing)",
    )

    args = parser.parse_args()

    if args.community_id:
        backfill_single_community(args.community_id, dry_run=args.dry_run)
    else:
        backfill_all_communities(dry_run=args.dry_run, limit=args.limit)


if __name__ == "__main__":
    main()
