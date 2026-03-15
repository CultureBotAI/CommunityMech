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
import csv
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

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


class IngredientMappingTracker:
    """Track ingredient mapping results across all communities."""

    def __init__(self):
        # ingredient_name -> list of (community_id, media_name, mapped_id, match_score)
        self.ingredient_records: Dict[str, List[Tuple[str, str, Optional[str], Optional[float]]]] = defaultdict(list)
        self.media_records: Dict[str, List[Tuple[str, Optional[str], Optional[float]]]] = defaultdict(list)
        self.communities_processed: Set[str] = set()

    def record_ingredient(
        self,
        ingredient_name: str,
        community_id: str,
        media_name: str,
        mapped_id: Optional[str] = None,
        match_score: Optional[float] = None,
    ):
        """Record an ingredient mapping attempt."""
        self.ingredient_records[ingredient_name].append(
            (community_id, media_name, mapped_id, match_score)
        )

    def record_media(
        self,
        media_name: str,
        community_id: str,
        mapped_id: Optional[str] = None,
        match_score: Optional[float] = None,
    ):
        """Record a media mapping attempt."""
        self.media_records[media_name].append((community_id, mapped_id, match_score))

    def record_community(self, community_id: str):
        """Mark a community as processed."""
        self.communities_processed.add(community_id)

    def get_mapped_ingredients(self) -> Dict[str, List]:
        """Get all successfully mapped ingredients."""
        return {
            name: records
            for name, records in self.ingredient_records.items()
            if any(r[2] is not None for r in records)
        }

    def get_unmapped_ingredients(self) -> Dict[str, List]:
        """Get all unmapped ingredients."""
        return {
            name: records
            for name, records in self.ingredient_records.items()
            if all(r[2] is None for r in records)
        }

    def get_mapped_media(self) -> Dict[str, List]:
        """Get all successfully mapped media."""
        return {
            name: records
            for name, records in self.media_records.items()
            if any(r[1] is not None for r in records)
        }

    def get_unmapped_media(self) -> Dict[str, List]:
        """Get all unmapped media."""
        return {
            name: records
            for name, records in self.media_records.items()
            if all(r[1] is None for r in records)
        }

    def export_ingredient_csv(self, output_path: Path):
        """Export ingredient mapping results to CSV."""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "ingredient_name",
                "community_id",
                "media_name",
                "mapped_id",
                "match_score",
                "status",
            ])

            for ingredient_name in sorted(self.ingredient_records.keys()):
                for community_id, media_name, mapped_id, match_score in self.ingredient_records[ingredient_name]:
                    status = "mapped" if mapped_id else "unmapped"
                    score_str = f"{match_score:.3f}" if match_score else ""
                    writer.writerow([
                        ingredient_name,
                        community_id,
                        media_name,
                        mapped_id or "",
                        score_str,
                        status,
                    ])

    def export_media_csv(self, output_path: Path):
        """Export media mapping results to CSV."""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "media_name",
                "community_id",
                "mapped_id",
                "match_score",
                "status",
            ])

            for media_name in sorted(self.media_records.keys()):
                for community_id, mapped_id, match_score in self.media_records[media_name]:
                    status = "mapped" if mapped_id else "unmapped"
                    score_str = f"{match_score:.3f}" if match_score else ""
                    writer.writerow([
                        media_name,
                        community_id,
                        mapped_id or "",
                        score_str,
                        status,
                    ])

    def export_summary_report(self, output_path: Path):
        """Export a human-readable summary report."""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        mapped_ingredients = self.get_mapped_ingredients()
        unmapped_ingredients = self.get_unmapped_ingredients()
        mapped_media = self.get_mapped_media()
        unmapped_media = self.get_unmapped_media()

        with open(output_path, "w") as f:
            f.write("=" * 80 + "\n")
            f.write("GROWTH MEDIA LINKING REPORT\n")
            f.write("=" * 80 + "\n\n")

            f.write(f"Communities processed: {len(self.communities_processed)}\n")
            f.write(f"Total unique ingredients: {len(self.ingredient_records)}\n")
            f.write(f"Mapped ingredients: {len(mapped_ingredients)}\n")
            f.write(f"Unmapped ingredients: {len(unmapped_ingredients)}\n")
            f.write(f"Total unique media: {len(self.media_records)}\n")
            f.write(f"Mapped media: {len(mapped_media)}\n")
            f.write(f"Unmapped media: {len(unmapped_media)}\n\n")

            if unmapped_ingredients:
                f.write("=" * 80 + "\n")
                f.write("UNMAPPED INGREDIENTS (need manual curation)\n")
                f.write("=" * 80 + "\n\n")
                for ingredient_name in sorted(unmapped_ingredients.keys()):
                    records = unmapped_ingredients[ingredient_name]
                    f.write(f"• {ingredient_name}\n")
                    communities = {r[0] for r in records}
                    f.write(f"  Found in {len(communities)} communities: {', '.join(sorted(communities)[:5])}")
                    if len(communities) > 5:
                        f.write(f" ... (+{len(communities) - 5} more)")
                    f.write("\n\n")

            if mapped_ingredients:
                f.write("=" * 80 + "\n")
                f.write("SUCCESSFULLY MAPPED INGREDIENTS\n")
                f.write("=" * 80 + "\n\n")
                for ingredient_name in sorted(mapped_ingredients.keys()):
                    records = mapped_ingredients[ingredient_name]
                    mapped = [r for r in records if r[2]]
                    if mapped:
                        mapped_id = mapped[0][2]
                        score = mapped[0][3]
                        f.write(f"• {ingredient_name} → {mapped_id}")
                        if score:
                            f.write(f" (score: {score:.3f})")
                        f.write("\n")

            if unmapped_media:
                f.write("\n" + "=" * 80 + "\n")
                f.write("UNMAPPED MEDIA (need manual curation)\n")
                f.write("=" * 80 + "\n\n")
                for media_name in sorted(unmapped_media.keys()):
                    records = unmapped_media[media_name]
                    communities = {r[0] for r in records}
                    f.write(f"• {media_name}\n")
                    f.write(f"  Found in {len(communities)} communities: {', '.join(sorted(communities)[:5])}")
                    if len(communities) > 5:
                        f.write(f" ... (+{len(communities) - 5} more)")
                    f.write("\n\n")

            if mapped_media:
                f.write("=" * 80 + "\n")
                f.write("SUCCESSFULLY MAPPED MEDIA\n")
                f.write("=" * 80 + "\n\n")
                for media_name in sorted(mapped_media.keys()):
                    records = mapped_media[media_name]
                    mapped = [r for r in records if r[1]]
                    if mapped:
                        mapped_id = mapped[0][1]
                        score = mapped[0][2]
                        f.write(f"• {media_name} → {mapped_id}")
                        if score:
                            f.write(f" (score: {score:.3f})")
                        f.write("\n")


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
    ingredient_report: Optional[Path] = None,
    media_report: Optional[Path] = None,
    summary_report: Optional[Path] = None,
) -> None:
    """Process all communities to link growth media.

    Args:
        dry_run: If True, only print what would be done
        fuzzy_threshold: Minimum similarity for fuzzy matching
        cache_ttl: Cache TTL in seconds
        use_cache: Whether to use cached data
        limit: If set, only process this many communities (for testing)
        ingredient_report: Path to export ingredient mapping CSV
        media_report: Path to export media mapping CSV
        summary_report: Path to export summary report
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
    tracker = IngredientMappingTracker()

    for yaml_file in yaml_files:
        # Load community data
        with open(yaml_file) as f:
            data = yaml.safe_load(f)

        stats["total"] += 1
        community_id = data.get("id", yaml_file.stem)
        tracker.record_community(community_id)

        # Get existing growth_media or create empty list
        growth_media = data.get("growth_media")

        if growth_media:
            stats["with_media"] += 1

            # Process each media record
            for media in growth_media:
                media_name = media.get("name", "")

                # Track media (placeholder for actual matching when CultureMech index available)
                culturemech_id = media.get("culturemech_id")
                tracker.record_media(media_name, community_id, culturemech_id)

                # Add empty composition if missing
                if "composition" not in media:
                    media["composition"] = []

                # Track ingredients
                for ingredient in media.get("composition", []):
                    ingredient_name = ingredient.get("name", "")
                    if ingredient_name:
                        mapped_id = ingredient.get("media_ingredient_mech_id")
                        tracker.record_ingredient(
                            ingredient_name,
                            community_id,
                            media_name,
                            mapped_id,
                        )

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
    print(f"Total unique ingredients: {len(tracker.ingredient_records)}")
    print(f"Mapped ingredients: {len(tracker.get_mapped_ingredients())}")
    print(f"Unmapped ingredients: {len(tracker.get_unmapped_ingredients())}")
    print(f"Total unique media: {len(tracker.media_records)}")
    print(f"Mapped media: {len(tracker.get_mapped_media())}")
    print(f"Unmapped media: {len(tracker.get_unmapped_media())}")

    # Export reports if requested
    if ingredient_report:
        tracker.export_ingredient_csv(ingredient_report)
        print(f"\n{GREEN}✓ Ingredient report: {ingredient_report}{RESET}")

    if media_report:
        tracker.export_media_csv(media_report)
        print(f"{GREEN}✓ Media report: {media_report}{RESET}")

    if summary_report:
        tracker.export_summary_report(summary_report)
        print(f"{GREEN}✓ Summary report: {summary_report}{RESET}")

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
    parser.add_argument(
        "--ingredient-report",
        type=str,
        help="Export ingredient mapping results to CSV (e.g., reports/ingredients.csv)",
    )
    parser.add_argument(
        "--media-report",
        type=str,
        help="Export media mapping results to CSV (e.g., reports/media.csv)",
    )
    parser.add_argument(
        "--summary-report",
        type=str,
        help="Export summary report to text file (e.g., reports/summary.txt)",
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
            ingredient_report=Path(args.ingredient_report) if args.ingredient_report else None,
            media_report=Path(args.media_report) if args.media_report else None,
            summary_report=Path(args.summary_report) if args.summary_report else None,
        )


if __name__ == "__main__":
    main()
