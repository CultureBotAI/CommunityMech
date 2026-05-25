#!/usr/bin/env python
"""Add sequential CommunityMech IDs to all community YAML files."""

import sys
from pathlib import Path

import yaml

from communitymech.curate.curation_event import record_curation_event
from communitymech.validation.write_validated import (
    ValidationFailedError,
    write_validated_community,
)


def add_ids_to_communities(communities_dir: Path = Path("kb/communities"), dry_run: bool = False):
    """Add sequential IDs to all community YAML files."""
    yaml_files = sorted(communities_dir.glob("*.yaml"))

    print(f"Adding IDs to {len(yaml_files)} communities...\n")

    for idx, yaml_file in enumerate(yaml_files, start=1):
        # Generate ID
        community_id = f"CommunityMech:{idx:06d}"

        # Load YAML
        with open(yaml_file) as f:
            data = yaml.safe_load(f)

        # Add ID as first field
        data_with_id = {"id": community_id}
        data_with_id.update(data)

        # Record curation event before write
        record_curation_event(
            data_with_id,
            curator="add_community_ids",
            action="ASSIGN_COMMUNITY_ID",
            changes=f"Assigned id={community_id}",
        )

        if dry_run:
            print(f"  (dry-run) would assign {community_id} → {yaml_file.name}")
            continue

        # Write back via validated writer (replaces direct yaml.dump)
        try:
            write_validated_community(data_with_id, yaml_file)
        except ValidationFailedError as exc:
            print(
                f"  ✗ validation failed for {yaml_file.name}: {exc.summary()}",
                file=sys.stderr,
            )
            continue

        print(f"  ✓ {community_id} → {yaml_file.name}")

    print(f"\n✅ Added IDs to {len(yaml_files)} communities")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Add sequential CommunityMech IDs to YAML files")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files",
    )
    args = parser.parse_args()

    add_ids_to_communities(dry_run=args.dry_run)
