"""
Media linking utilities for CommunityMech.

Links growth media to CultureMech and MediaIngredientMech via fuzzy matching
and external data fetching.
"""

import json
import time
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
import yaml


class MediaFetcher:
    """Fetch and cache CultureMech + MediaIngredientMech YAML from GitHub."""

    CULTUREMECH_RAW_URL = (
        "https://raw.githubusercontent.com/CultureBotAI/CultureMech/main/kb/media/"
    )
    MEDIA_INGREDIENT_MECH_RAW_URL = (
        "https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/main/kb/ingredients/"
    )

    def __init__(self, cache_dir: str = "media_cache", cache_ttl: int = 86400):
        """Initialize media fetcher.

        Args:
            cache_dir: Directory for caching external data
            cache_ttl: Cache time-to-live in seconds (default: 24 hours)
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.cache_ttl = cache_ttl
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "CommunityMech/0.1.0 (https://github.com/CultureBotAI/CommunityMech)"
        })

    def _is_cache_valid(self, cache_file: Path) -> bool:
        """Check if cache file exists and is within TTL."""
        if not cache_file.exists():
            return False
        age = time.time() - cache_file.stat().st_mtime
        return age < self.cache_ttl

    def fetch_culturemech_media(self, media_id: str, use_cache: bool = True) -> Optional[Dict]:
        """Fetch a CultureMech media record by ID.

        Args:
            media_id: CultureMech ID (e.g., "CultureMech:000001")
            use_cache: Whether to use cached data

        Returns:
            Media record as dict or None if not found
        """
        # Clean ID
        media_id_clean = media_id.replace("CultureMech:", "").strip()
        cache_file = self.cache_dir / f"culturemech_{media_id_clean}.json"

        # Check cache
        if use_cache and self._is_cache_valid(cache_file):
            return json.loads(cache_file.read_text())

        # Fetch from GitHub
        # Construct filename: assume pattern like "CultureMech_000001.yaml"
        yaml_filename = f"CultureMech_{media_id_clean}.yaml"
        url = f"{self.CULTUREMECH_RAW_URL}{yaml_filename}"

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            data = yaml.safe_load(response.text)

            # Cache the result
            cache_file.write_text(json.dumps(data, indent=2))
            return data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching CultureMech media {media_id}: {e}")
            return None

    def fetch_media_ingredient(
        self, ingredient_id: str, use_cache: bool = True
    ) -> Optional[Dict]:
        """Fetch a MediaIngredientMech ingredient record by ID.

        Args:
            ingredient_id: MediaIngredientMech ID (e.g., "MediaIngredientMech:000001")
            use_cache: Whether to use cached data

        Returns:
            Ingredient record as dict or None if not found
        """
        # Clean ID
        ingredient_id_clean = ingredient_id.replace("MediaIngredientMech:", "").strip()
        cache_file = self.cache_dir / f"mediaingredientmech_{ingredient_id_clean}.json"

        # Check cache
        if use_cache and self._is_cache_valid(cache_file):
            return json.loads(cache_file.read_text())

        # Fetch from GitHub
        # Construct filename: assume pattern like "MediaIngredientMech_000001.yaml"
        yaml_filename = f"MediaIngredientMech_{ingredient_id_clean}.yaml"
        url = f"{self.MEDIA_INGREDIENT_MECH_RAW_URL}{yaml_filename}"

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            data = yaml.safe_load(response.text)

            # Cache the result
            cache_file.write_text(json.dumps(data, indent=2))
            return data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching MediaIngredientMech ingredient {ingredient_id}: {e}")
            return None

    def list_all_culturemech_media(self, use_cache: bool = True) -> List[Dict]:
        """Fetch all CultureMech media records (for matching).

        This would require an index or API. For now, return empty list.
        TODO: Implement when CultureMech provides an index.

        Args:
            use_cache: Whether to use cached data

        Returns:
            List of media records
        """
        # Placeholder - would need index file or API
        return []


class MediaMatcher:
    """Fuzzy match media names and ingredient names."""

    def __init__(
        self, fuzzy_threshold: float = 0.85, manual_overrides: Optional[Dict] = None
    ):
        """Initialize media matcher.

        Args:
            fuzzy_threshold: Minimum similarity score (0-1) for fuzzy match
            manual_overrides: Manual mapping overrides from conf/media_mappings.yaml
        """
        self.fuzzy_threshold = fuzzy_threshold
        self.manual_overrides = manual_overrides or {}

    def match_media_name(
        self, query: str, candidates: List[Tuple[str, str]]
    ) -> Optional[Tuple[str, str, float]]:
        """Match media name to CultureMech records.

        Args:
            query: Media name to match
            candidates: List of (media_id, media_name) tuples

        Returns:
            Tuple of (media_id, media_name, score) or None if no match
        """
        # Check manual overrides first
        if "media_overrides" in self.manual_overrides:
            if query in self.manual_overrides["media_overrides"]:
                override = self.manual_overrides["media_overrides"][query]
                return (override["culturemech_id"], query, 1.0)

        # Exact match (case-insensitive)
        query_lower = query.lower().strip()
        for media_id, media_name in candidates:
            if media_name.lower().strip() == query_lower:
                return (media_id, media_name, 1.0)

        # Fuzzy match
        best_match = None
        best_score = 0.0

        for media_id, media_name in candidates:
            score = SequenceMatcher(None, query_lower, media_name.lower().strip()).ratio()
            if score >= self.fuzzy_threshold and score > best_score:
                best_score = score
                best_match = (media_id, media_name, score)

        return best_match

    def match_ingredient_name(
        self, query: str, candidates: List[Tuple[str, str]]
    ) -> Optional[Tuple[str, str, float]]:
        """Match ingredient name to MediaIngredientMech records.

        Args:
            query: Ingredient name to match
            candidates: List of (ingredient_id, ingredient_name) tuples

        Returns:
            Tuple of (ingredient_id, ingredient_name, score) or None if no match
        """
        # Check manual overrides first
        if "ingredient_overrides" in self.manual_overrides:
            if query in self.manual_overrides["ingredient_overrides"]:
                override = self.manual_overrides["ingredient_overrides"][query]
                return (override["media_ingredient_mech_id"], query, 1.0)

        # Exact match (case-insensitive)
        query_lower = query.lower().strip()
        for ingredient_id, ingredient_name in candidates:
            if ingredient_name.lower().strip() == query_lower:
                return (ingredient_id, ingredient_name, 1.0)

        # Fuzzy match
        best_match = None
        best_score = 0.0

        for ingredient_id, ingredient_name in candidates:
            score = SequenceMatcher(
                None, query_lower, ingredient_name.lower().strip()
            ).ratio()
            if score >= self.fuzzy_threshold and score > best_score:
                best_score = score
                best_match = (ingredient_id, ingredient_name, score)

        return best_match


class CompositionMerger:
    """Merge CultureMech ingredients with existing community ingredients."""

    def merge_compositions(
        self,
        existing: List[Dict],
        culturemech: List[Dict],
        mark_source: bool = True,
    ) -> List[Dict]:
        """Merge ingredient lists, preserving existing and adding new from CultureMech.

        Args:
            existing: Existing community-curated ingredients
            culturemech: Ingredients from CultureMech recipe
            mark_source: Whether to add source metadata

        Returns:
            Merged ingredient list
        """
        # Build set of existing ingredient names (case-insensitive)
        existing_names = {ing["name"].lower().strip() for ing in existing}

        # Mark existing ingredients as community-curated
        merged = []
        for ing in existing:
            if mark_source and "from" not in ing:
                ing_copy = ing.copy()
                ing_copy["from"] = "community_curated"
                merged.append(ing_copy)
            else:
                merged.append(ing.copy())

        # Add new ingredients from CultureMech
        for ing in culturemech:
            ing_name = ing.get("name", "").lower().strip()
            if ing_name and ing_name not in existing_names:
                ing_copy = ing.copy()
                if mark_source:
                    ing_copy["from"] = "CultureMech"
                merged.append(ing_copy)

        return merged
