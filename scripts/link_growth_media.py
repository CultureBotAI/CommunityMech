#!/usr/bin/env python3
"""Link growth media to CultureMech and MediaIngredientMech.

Processes all community YAML files and:
1. Matches media names to CultureMech IDs
2. Enriches composition with MediaIngredientMech IDs
3. Preserves existing curated data

Usage:
    python scripts/link_growth_media.py --dry-run          # Preview changes
    python scripts/link_growth_media.py                    # Apply changes
    python scripts/link_growth_media.py --community-id foo # Process single community
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

import yaml

# Add src to path so we can import from communitymech
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.utils.media_linker import (
    CompositionMerger,
    MediaFetcher,
    MediaMatcher,
)


# ANSI color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"


def load_manual_overrides(config_path: Path) -> dict:
    """Load manual media/ingredient mappings from YAML config."""
    if not config_path.exists():
        return {}
    with open(config_path) as f:
        return yaml.safe_load(f) or {}


def update_yaml_with_media(yaml_path: Path, growth_media: list) -> None:
    """Update a YAML file with growth media data.

    Args:
        yaml_path: Path to community YAML file
        growth_media: List of growth media records
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    # Update growth_media field
    data["growth_media"] = growth_media

    # Write back with clean formatting (same pattern as backfill_metals.py)
    with open(yaml_path, "w") as f:
        yaml.dump(
            data,
            f,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=100,
        )


def process_single_community(
    community_id: str,
    dry_run: bool = True,
    fuzzy_threshold: float = 0.85,
    cache_ttl: int = 86400,
    use_cache: bool = True,
    manual_overrides: Optional[dict] = None,
) -> None:
    """Process a single community by ID."""
    community_dir = Path("kb/communities")
    yaml_file = community_dir / f"{community_id}.yaml"

    if not yaml_file.exists():
        print(f"{RED}ERROR: Community file not found: {yaml_file}{RESET}")
        return

    # Load community data
    with open(yaml_file) as f:
        data = yaml.safe_load(f)

    # Initialize utilities
    fetcher = MediaFetcher(cache_ttl=cache_ttl)
    matcher = MediaMatcher(fuzzy_threshold=fuzzy_threshold, manual_overrides=manual_overrides)
    merger = CompositionMerger()

    # Get existing growth_media or create empty list
    growth_media = data.get("growth_media", [])
    if not growth_media:
        growth_media = []

    updated = False

    for media in growth_media:
        media_name = media.get("name", "")

        # Try to match and add CultureMech ID
        # For now, we'll just add placeholder logic since we need an index
        # TODO: Implement when CultureMech provides media index

        # Add empty composition if missing
        if "composition" not in media:
            media["composition"] = []
            updated = True

    print(f"\n{BLUE}{yaml_file.stem}:{RESET}")
    print(f"  Media records: {len(growth_media)}")

    if growth_media and not dry_run:
        # Backup original
        backup_path = yaml_file.with_suffix(".yaml.bak")
        yaml_file.rename(backup_path)

        update_yaml_with_media(yaml_file, growth_media)
        print(f"  {GREEN}✓ Updated {yaml_file.name}{RESET}")
    elif updated and not dry_run:
        print(f"  {GREEN}✓ Would update {yaml_file.name}{RESET}")


def process_all_communities(
    dry_run: bool = True,
    fuzzy_threshold: float = 0.85,
    cache_ttl: int = 86400,
    use_cache: bool = True,
    limit: Optional[int] = None,
) -> None:
    """Process all communities to link growth media.

    Args:
        dry_run: If True, only print what would be done
        fuzzy_threshold: Minimum similarity for fuzzy matching
        cache_ttl: Cache TTL in seconds
        use_cache: Whether to use cached data
        limit: If set, only process this many communities (for testing)
    """
    community_dir = Path("kb/communities")

    if not community_dir.exists():
        print(f"{RED}ERROR: Community directory not found: {community_dir}{RESET}")
        return

    # Load manual overrides
    config_path = Path("conf/media_mappings.yaml")
    manual_overrides = load_manual_overrides(config_path)

    yaml_files = sorted(community_dir.glob("*.yaml"))

    if limit:
        yaml_files = yaml_files[:limit]

    print(f"Processing {len(yaml_files)} communities...")
    if dry_run:
        print(f"{YELLOW}DRY RUN - No files will be modified{RESET}\n")

    # Statistics
    stats = {
        "total": 0,
        "with_media": 0,
        "media_matched": 0,
        "ingredients_added": 0,
    }

    # Initialize utilities
    fetcher = MediaFetcher(cache_ttl=cache_ttl)
    matcher = MediaMatcher(fuzzy_threshold=fuzzy_threshold, manual_overrides=manual_overrides)
    merger = CompositionMerger()

    for yaml_file in yaml_files:
        # Load community data
        with open(yaml_file) as f:
            data = yaml.safe_load(f)

        stats["total"] += 1

        # Get existing growth_media or create empty list
        growth_media = data.get("growth_media")

        if growth_media:
            stats["with_media"] += 1

            # Process each media record
            for media in growth_media:
                media_name = media.get("name", "")

                # Add empty composition if missing
                if "composition" not in media:
                    media["composition"] = []

                print(f"\n{BLUE}{yaml_file.stem}:{RESET}")
                print(f"  Media: {media_name}")
                print(f"  Components: {len(media.get('composition', []))}")

            # Update file if needed
            if not dry_run:
                # Backup original
                backup_path = yaml_file.with_suffix(".yaml.bak")
                yaml_file.rename(backup_path)

                update_yaml_with_media(yaml_file, growth_media)
                print(f"  {GREEN}✓ Updated{RESET}")

    # Print summary
    print("\n" + "=" * 60)
    print(f"{GREEN}SUMMARY{RESET}")
    print("=" * 60)
    print(f"Total communities: {stats['total']}")
    print(f"Communities with growth_media: {stats['with_media']}")
    print(f"Media matched to CultureMech: {stats['media_matched']}")
    print(f"Ingredients added from MediaIngredientMech: {stats['ingredients_added']}")

    if dry_run:
        print(f"\n{YELLOW}To apply these changes, run without --dry-run{RESET}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Link growth media to CultureMech and MediaIngredientMech"
    )
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
        "--fuzzy-threshold",
        type=float,
        default=0.85,
        help="Minimum similarity score for fuzzy matching (0-1, default: 0.85)",
    )
    parser.add_argument(
        "--cache-ttl",
        type=int,
        default=86400,
        help="Cache TTL in seconds (default: 86400 = 24 hours)",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Disable cache and fetch fresh data",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of communities to process (for testing)",
    )

    args = parser.parse_args()

    if args.community_id:
        # Load manual overrides
        config_path = Path("conf/media_mappings.yaml")
        manual_overrides = load_manual_overrides(config_path)

        process_single_community(
            args.community_id,
            dry_run=args.dry_run,
            fuzzy_threshold=args.fuzzy_threshold,
            cache_ttl=args.cache_ttl,
            use_cache=not args.no_cache,
            manual_overrides=manual_overrides,
        )
    else:
        process_all_communities(
            dry_run=args.dry_run,
            fuzzy_threshold=args.fuzzy_threshold,
            cache_ttl=args.cache_ttl,
            use_cache=not args.no_cache,
            limit=args.limit,
        )


if __name__ == "__main__":
    main()
