#!/usr/bin/env python
"""Add sequential CommunityMech IDs to all community YAML files."""

import yaml
from pathlib import Path


def add_ids_to_communities(communities_dir: Path = Path("kb/communities")):
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

        # Write back with proper formatting
        with open(yaml_file, "w") as f:
            # Use default_flow_style=False for block style
            yaml.dump(
                data_with_id,
                f,
                default_flow_style=False,
                sort_keys=False,
                allow_unicode=True,
                width=100,
            )

        print(f"  ✓ {community_id} → {yaml_file.name}")

    print(f"\n✅ Added IDs to {len(yaml_files)} communities")


if __name__ == "__main__":
    add_ids_to_communities()
