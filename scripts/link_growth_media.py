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

import yaml

# Add src to path so we can import from communitymech
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.curate.curation_event import record_curation_event
from communitymech.utils.media_linker import (
    CompositionMerger,
    MediaFetcher,
    MediaMatcher,
)
from communitymech.validation.write_validated import (
    ValidationFailedError,
    write_validated_community,
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
        self.ingredient_records: dict[str, list[tuple[str, str, str | None, float | None]]] = (
            defaultdict(list)
        )
        self.media_records: dict[str, list[tuple[str, str | None, float | None]]] = defaultdict(
            list
        )
        self.communities_processed: set[str] = set()

    def record_ingredient(
        self,
        ingredient_name: str,
        community_id: str,
        media_name: str,
        mapped_id: str | None = None,
        match_score: float | None = None,
    ):
        """Record an ingredient mapping attempt."""
        self.ingredient_records[ingredient_name].append(
            (community_id, media_name, mapped_id, match_score)
        )

    def record_media(
        self,
        media_name: str,
        community_id: str,
        mapped_id: str | None = None,
        match_score: float | None = None,
    ):
        """Record a media mapping attempt."""
        self.media_records[media_name].append((community_id, mapped_id, match_score))

    def record_community(self, community_id: str):
        """Mark a community as processed."""
        self.communities_processed.add(community_id)

    def get_mapped_ingredients(self) -> dict[str, list]:
        """Get all successfully mapped ingredients."""
        return {
            name: records
            for name, records in self.ingredient_records.items()
            if any(r[2] is not None for r in records)
        }

    def get_unmapped_ingredients(self) -> dict[str, list]:
        """Get all unmapped ingredients."""
        return {
            name: records
            for name, records in self.ingredient_records.items()
            if all(r[2] is None for r in records)
        }

    def get_mapped_media(self) -> dict[str, list]:
        """Get all successfully mapped media."""
        return {
            name: records
            for name, records in self.media_records.items()
            if any(r[1] is not None for r in records)
        }

    def get_unmapped_media(self) -> dict[str, list]:
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
            writer.writerow(
                [
                    "ingredient_name",
                    "community_id",
                    "media_name",
                    "mapped_id",
                    "match_score",
                    "status",
                ]
            )

            for ingredient_name in sorted(self.ingredient_records.keys()):
                for community_id, media_name, mapped_id, match_score in self.ingredient_records[
                    ingredient_name
                ]:
                    status = "mapped" if mapped_id else "unmapped"
                    score_str = f"{match_score:.3f}" if match_score else ""
                    writer.writerow(
                        [
                            ingredient_name,
                            community_id,
                            media_name,
                            mapped_id or "",
                            score_str,
                            status,
                        ]
                    )

    def export_media_csv(self, output_path: Path):
        """Export media mapping results to CSV."""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "media_name",
                    "community_id",
                    "mapped_id",
                    "match_score",
                    "status",
                ]
            )

            for media_name in sorted(self.media_records.keys()):
                for community_id, mapped_id, match_score in self.media_records[media_name]:
                    status = "mapped" if mapped_id else "unmapped"
                    score_str = f"{match_score:.3f}" if match_score else ""
                    writer.writerow(
                        [
                            media_name,
                            community_id,
                            mapped_id or "",
                            score_str,
                            status,
                        ]
                    )

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
                    f.write(
                        f"  Found in {len(communities)} communities: {', '.join(sorted(communities)[:5])}"
                    )
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
                    f.write(
                        f"  Found in {len(communities)} communities: {', '.join(sorted(communities)[:5])}"
                    )
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


def update_yaml_with_media(yaml_path: Path, data: dict) -> None:
    """Update a YAML file with community data including growth media.

    Routes through ``write_validated_community`` so the doc is refused
    if it would violate the closed-schema contract.

    Args:
        yaml_path: Path to community YAML file to write
        data: Community data dict with updated growth_media
    """
    write_validated_community(data, yaml_path)


def process_single_community(
    community_id: str,
    dry_run: bool = True,
    fuzzy_threshold: float = 0.85,
    cache_ttl: int = 86400,
    use_cache: bool = True,
    manual_overrides: dict | None = None,
    culturemech_index_path: str | None = None,
    mediaingredientmech_index_path: str | None = None,
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
    fetcher = MediaFetcher(
        cache_ttl=cache_ttl,
        culturemech_index_path=culturemech_index_path,
        mediaingredientmech_index_path=mediaingredientmech_index_path,
    )
    matcher = MediaMatcher(fuzzy_threshold=fuzzy_threshold, manual_overrides=manual_overrides)
    merger = CompositionMerger()

    # Load all CultureMech media for matching
    all_media = fetcher.list_all_culturemech_media()

    # Load all MediaIngredientMech ingredients for matching
    all_ingredients = fetcher.list_all_mediaingredientmech_ingredients()

    # Get existing growth_media or create empty list
    growth_media = data.get("growth_media", [])
    if not growth_media:
        growth_media = []

    updated = False

    for media in growth_media:
        media_name = media.get("name", "")

        # Try to match media name to CultureMech
        match = matcher.match_media_name(media_name, all_media)
        if match:
            culturemech_id, matched_name, score = match
            if "culturemech_id" not in media:
                media["culturemech_id"] = culturemech_id
                media["culturemech_url"] = (
                    f"https://github.com/CultureBotAI/CultureMech/tree/main/kb/media/{culturemech_id}"
                )
                updated = True
                print(
                    f"  {GREEN}✓ Matched '{media_name}' → {culturemech_id} (score: {score:.3f}){RESET}"
                )

            # Fetch recipe to get ingredients
            recipe = fetcher.fetch_culturemech_recipe_by_id(culturemech_id)
            if recipe and "ingredients" in recipe:
                # Merge composition
                existing_comp = media.get("composition", [])
                culturemech_comp = recipe["ingredients"]

                # Convert CultureMech ingredients to CommunityMech format
                converted_comp = []
                for ing in culturemech_comp:
                    new_ing = {"name": ing.get("preferred_term", "")}
                    if "concentration" in ing:
                        conc = ing["concentration"]
                        if isinstance(conc, dict):
                            new_ing["concentration"] = conc.get("value", "")
                            new_ing["unit"] = conc.get("unit", "")
                        else:
                            new_ing["concentration"] = str(conc)
                    converted_comp.append(new_ing)

                merged = merger.merge_compositions(existing_comp, converted_comp, mark_source=True)
                if len(merged) > len(existing_comp):
                    media["composition"] = merged
                    updated = True
        else:
            print(f"  {YELLOW}No match for '{media_name}'{RESET}")

        # Add empty composition if missing
        if "composition" not in media:
            media["composition"] = []
            updated = True

        # Match and link ingredients to MediaIngredientMech
        composition = media.get("composition", [])
        ingredients_matched = 0
        for ingredient in composition:
            ingredient_name = ingredient.get("name", "")
            if ingredient_name and "media_ingredient_mech_id" not in ingredient:
                # Try to match ingredient to MediaIngredientMech
                ing_match = matcher.match_ingredient_name(ingredient_name, all_ingredients)
                if ing_match:
                    ing_id, matched_name, score = ing_match
                    ingredient["media_ingredient_mech_id"] = ing_id
                    ingredient["media_ingredient_mech_url"] = (
                        f"https://github.com/CultureBotAI/MediaIngredientMech/tree/main/data/ingredients/{ing_id}"
                    )
                    ingredients_matched += 1
                    updated = True

        if ingredients_matched > 0:
            print(
                f"  {GREEN}✓ Linked {ingredients_matched} ingredients to MediaIngredientMech{RESET}"
            )

    print(f"\n{BLUE}{yaml_file.stem}:{RESET}")
    print(f"  Media records: {len(growth_media)}")

    if updated and not dry_run:
        # Backup original
        backup_path = yaml_file.with_suffix(".yaml.bak")
        if yaml_file.exists():
            yaml_file.rename(backup_path)

        media_names = [m.get("name", "") for m in growth_media if m.get("name")]
        record_curation_event(
            data,
            curator="link_growth_media",
            action="LINK_GROWTH_MEDIA",
            changes=(
                f"Linked growth media to CultureMech / MediaIngredientMech for "
                f"{len(media_names)} media record(s): "
                + ", ".join(media_names[:5])
                + (f", +{len(media_names) - 5} more" if len(media_names) > 5 else "")
            ),
        )
        try:
            update_yaml_with_media(yaml_file, data)
        except ValidationFailedError as exc:
            # Restore backup so the original file isn't left missing.
            if backup_path.exists():
                backup_path.rename(yaml_file)
            print(
                f"  {RED}✗ validation failed for {yaml_file.name}: {exc.summary()}{RESET} "
                "(original restored from backup)",
                file=sys.stderr,
            )
            return
        print(f"  {GREEN}✓ Updated {yaml_file.name}{RESET}")
    elif updated:
        print(f"  {YELLOW}Would update {yaml_file.name}{RESET}")


def process_all_communities(
    dry_run: bool = True,
    fuzzy_threshold: float = 0.85,
    cache_ttl: int = 86400,
    use_cache: bool = True,
    limit: int | None = None,
    ingredient_report: Path | None = None,
    media_report: Path | None = None,
    summary_report: Path | None = None,
    culturemech_index_path: str | None = None,
    mediaingredientmech_index_path: str | None = None,
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
        culturemech_index_path: Path to CultureMech recipe_index.json
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
    fetcher = MediaFetcher(
        cache_ttl=cache_ttl,
        culturemech_index_path=culturemech_index_path,
        mediaingredientmech_index_path=mediaingredientmech_index_path,
    )
    matcher = MediaMatcher(fuzzy_threshold=fuzzy_threshold, manual_overrides=manual_overrides)
    merger = CompositionMerger()
    tracker = IngredientMappingTracker()

    # Load all CultureMech media for matching
    print("Loading CultureMech recipe index...")
    all_media = fetcher.list_all_culturemech_media()
    print(f"Loaded {len(all_media)} CultureMech recipes")

    # Load all MediaIngredientMech ingredients for matching
    print("Loading MediaIngredientMech ingredient index...")
    all_ingredients = fetcher.list_all_mediaingredientmech_ingredients()
    print(f"Loaded {len(all_ingredients)} MediaIngredientMech ingredients\n")

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
            updated = False

            # Process each media record
            for media in growth_media:
                media_name = media.get("name", "")

                print(f"\n{BLUE}{yaml_file.stem}:{RESET}")
                print(f"  Media: {media_name}")

                # Try to match media name to CultureMech
                match = matcher.match_media_name(media_name, all_media)
                if match:
                    culturemech_id, matched_name, score = match
                    stats["media_matched"] += 1

                    if "culturemech_id" not in media:
                        media["culturemech_id"] = culturemech_id
                        media["culturemech_url"] = (
                            f"https://github.com/CultureBotAI/CultureMech/tree/main/kb/media/{culturemech_id}"
                        )
                        updated = True
                        print(f"  {GREEN}✓ Matched → {culturemech_id} (score: {score:.3f}){RESET}")

                    # Track media match
                    tracker.record_media(media_name, community_id, culturemech_id, score)

                    # Fetch recipe to get ingredients
                    recipe = fetcher.fetch_culturemech_recipe_by_id(culturemech_id)
                    if recipe and "ingredients" in recipe:
                        # Merge composition
                        existing_comp = media.get("composition", [])

                        # Convert CultureMech ingredients to CommunityMech format
                        converted_comp = []
                        for ing in recipe["ingredients"]:
                            new_ing = {"name": ing.get("preferred_term", "")}
                            if "concentration" in ing:
                                conc = ing["concentration"]
                                if isinstance(conc, dict):
                                    new_ing["concentration"] = conc.get("value", "")
                                    new_ing["unit"] = conc.get("unit", "")
                                else:
                                    new_ing["concentration"] = str(conc)
                            converted_comp.append(new_ing)

                        merged = merger.merge_compositions(
                            existing_comp, converted_comp, mark_source=True
                        )
                        added_count = len(merged) - len(existing_comp)
                        if added_count > 0:
                            media["composition"] = merged
                            stats["ingredients_added"] += added_count
                            updated = True
                            print(
                                f"  {GREEN}✓ Added {added_count} ingredients from CultureMech{RESET}"
                            )
                else:
                    # No match found
                    tracker.record_media(media_name, community_id, None, None)
                    print(f"  {YELLOW}No CultureMech match{RESET}")

                # Add empty composition if missing
                if "composition" not in media:
                    media["composition"] = []

                # Match and link ingredients to MediaIngredientMech
                composition = media.get("composition", [])
                ingredients_matched = 0
                for ingredient in composition:
                    ingredient_name = ingredient.get("name", "")
                    if ingredient_name and "media_ingredient_mech_id" not in ingredient:
                        # Try to match ingredient to MediaIngredientMech
                        ing_match = matcher.match_ingredient_name(ingredient_name, all_ingredients)
                        if ing_match:
                            ing_id, matched_name, score = ing_match
                            ingredient["media_ingredient_mech_id"] = ing_id
                            ingredient["media_ingredient_mech_url"] = (
                                f"https://github.com/CultureBotAI/MediaIngredientMech/tree/main/data/ingredients/{ing_id}"
                            )
                            ingredients_matched += 1
                            updated = True

                # Track ingredients
                for ingredient in composition:
                    ingredient_name = ingredient.get("name", "")
                    if ingredient_name:
                        mapped_id = ingredient.get("media_ingredient_mech_id")
                        tracker.record_ingredient(
                            ingredient_name,
                            community_id,
                            media_name,
                            mapped_id,
                        )

                print(f"  Components: {len(composition)}")
                if ingredients_matched > 0:
                    print(
                        f"  {GREEN}✓ Linked {ingredients_matched} ingredients to MediaIngredientMech{RESET}"
                    )

            # Update file if needed
            if updated and not dry_run:
                # Backup original
                backup_path = yaml_file.with_suffix(".yaml.bak")
                if yaml_file.exists():
                    yaml_file.rename(backup_path)

                media_names = [m.get("name", "") for m in growth_media if m.get("name")]
                record_curation_event(
                    data,
                    curator="link_growth_media",
                    action="LINK_GROWTH_MEDIA",
                    changes=(
                        f"Linked growth media to CultureMech / MediaIngredientMech for "
                        f"{len(media_names)} media record(s): "
                        + ", ".join(media_names[:5])
                        + (f", +{len(media_names) - 5} more" if len(media_names) > 5 else "")
                    ),
                )
                try:
                    update_yaml_with_media(yaml_file, data)
                except ValidationFailedError as exc:
                    # Restore backup so the original file isn't left missing.
                    if backup_path.exists():
                        backup_path.rename(yaml_file)
                    print(
                        f"  {RED}✗ validation failed for {yaml_file.name}: "
                        f"{exc.summary()}{RESET} (original restored from backup)",
                        file=sys.stderr,
                    )
                    continue
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
    parser.add_argument(
        "--culturemech-index",
        type=str,
        help="Path to CultureMech recipe_index.json (default: ../../CultureMech/data/normalized_yaml/recipe_index.json)",
    )
    parser.add_argument(
        "--mediaingredientmech-index",
        type=str,
        help="Path to MediaIngredientMech all_ingredients_index.json (default: ../../MediaIngredientMech/data/curated/all_ingredients_index.json)",
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
            culturemech_index_path=args.culturemech_index,
            mediaingredientmech_index_path=args.mediaingredientmech_index,
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
            culturemech_index_path=args.culturemech_index,
            mediaingredientmech_index_path=args.mediaingredientmech_index,
        )


if __name__ == "__main__":
    main()
