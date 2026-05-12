"""
Media linking utilities for CommunityMech.

Links growth media to CultureMech and MediaIngredientMech via fuzzy matching
and external data fetching.
"""

import json
import time
from difflib import SequenceMatcher
from pathlib import Path

import requests
import yaml


class MediaFetcher:
    """Fetch and cache CultureMech + MediaIngredientMech YAML from local or remote sources."""

    # Default local paths (relative to project root)
    DEFAULT_CULTUREMECH_INDEX = "../CultureMech/data/normalized_yaml/recipe_index.json"
    DEFAULT_CULTUREMECH_DATA = "../CultureMech/data/normalized_yaml"
    DEFAULT_MEDIAINGREDIENTMECH_INDEX = (
        "../MediaIngredientMech/data/curated/all_ingredients_index.json"
    )

    CULTUREMECH_RAW_URL = (
        "https://raw.githubusercontent.com/CultureBotAI/CultureMech/main/kb/media/"
    )
    MEDIA_INGREDIENT_MECH_RAW_URL = (
        "https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/main/kb/ingredients/"
    )

    def __init__(
        self,
        cache_dir: str = "media_cache",
        cache_ttl: int = 86400,
        culturemech_index_path: str | None = None,
        culturemech_data_path: str | None = None,
        mediaingredientmech_index_path: str | None = None,
    ):
        """Initialize media fetcher.

        Args:
            cache_dir: Directory for caching external data
            cache_ttl: Cache time-to-live in seconds (default: 24 hours)
            culturemech_index_path: Path to local CultureMech recipe_index.json
            culturemech_data_path: Path to local CultureMech data directory
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.cache_ttl = cache_ttl
        self.session = requests.Session()
        self.session.headers.update(
            {"User-Agent": "CommunityMech/0.1.0 (https://github.com/CultureBotAI/CommunityMech)"}
        )

        # Set up local paths if provided
        if culturemech_index_path:
            self.culturemech_index_path = Path(culturemech_index_path).resolve()
            # If index path provided, derive data path from it
            if not culturemech_data_path:
                self.culturemech_data_path = self.culturemech_index_path.parent
            else:
                self.culturemech_data_path = Path(culturemech_data_path).resolve()
        else:
            self.culturemech_index_path = Path(self.DEFAULT_CULTUREMECH_INDEX)
            self.culturemech_data_path = Path(self.DEFAULT_CULTUREMECH_DATA)

        # Set up MediaIngredientMech index path
        if mediaingredientmech_index_path:
            self.mediaingredientmech_index_path = Path(mediaingredientmech_index_path).resolve()
        else:
            self.mediaingredientmech_index_path = Path(self.DEFAULT_MEDIAINGREDIENTMECH_INDEX)

        # Cache for loaded indices
        self._recipe_index: dict | None = None
        self._ingredient_index: list[dict] | None = None

    def _is_cache_valid(self, cache_file: Path) -> bool:
        """Check if cache file exists and is within TTL."""
        if not cache_file.exists():
            return False
        age = time.time() - cache_file.stat().st_mtime
        return age < self.cache_ttl

    def fetch_culturemech_media(self, media_id: str, use_cache: bool = True) -> dict | None:
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

    def fetch_media_ingredient(self, ingredient_id: str, use_cache: bool = True) -> dict | None:
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

    def load_recipe_index(self) -> dict:
        """Load CultureMech recipe index from local file.

        Returns:
            Recipe index dictionary

        Raises:
            FileNotFoundError: If index file doesn't exist
        """
        if self._recipe_index is not None:
            return self._recipe_index

        if not self.culturemech_index_path.exists():
            raise FileNotFoundError(
                f"CultureMech index not found at {self.culturemech_index_path}. "
                f"Please clone CultureMech repo or specify correct path."
            )

        with open(self.culturemech_index_path) as f:
            self._recipe_index = json.load(f)

        return self._recipe_index

    def list_all_culturemech_media(self) -> list[tuple[str, str]]:
        """Get all CultureMech media as (id, name) tuples for matching.

        Returns:
            List of (media_id, media_name) tuples
        """
        try:
            index = self.load_recipe_index()
            recipes = index.get("recipes", {})
            return [(recipe_id, recipe["name"]) for recipe_id, recipe in recipes.items()]
        except FileNotFoundError as e:
            print(f"Warning: {e}")
            return []

    def fetch_culturemech_recipe_by_id(self, recipe_id: str) -> dict | None:
        """Fetch a CultureMech recipe by ID from local files.

        Args:
            recipe_id: CultureMech ID (e.g., "CultureMech:000001")

        Returns:
            Recipe data or None if not found
        """
        try:
            index = self.load_recipe_index()
            recipe_info = index.get("recipes", {}).get(recipe_id)

            if not recipe_info:
                return None

            # Construct path to recipe file
            category_dir = recipe_info.get("category_dir", "bacterial")
            filename = recipe_info.get("filename")

            if not filename:
                return None

            recipe_path = self.culturemech_data_path / category_dir / filename

            if not recipe_path.exists():
                print(f"Warning: Recipe file not found: {recipe_path}")
                return None

            with open(recipe_path) as f:
                return yaml.safe_load(f)

        except Exception as e:
            print(f"Error loading recipe {recipe_id}: {e}")
            return None

    def load_ingredient_index(self) -> list[dict]:
        """Load MediaIngredientMech ingredient index from local file.

        Returns:
            List of ingredient records

        Raises:
            FileNotFoundError: If index file doesn't exist
        """
        if self._ingredient_index is not None:
            return self._ingredient_index

        if not self.mediaingredientmech_index_path.exists():
            raise FileNotFoundError(
                f"MediaIngredientMech index not found at {self.mediaingredientmech_index_path}. "
                f"Please clone MediaIngredientMech repo or specify correct path."
            )

        with open(self.mediaingredientmech_index_path) as f:
            self._ingredient_index = json.load(f)

        return self._ingredient_index

    def list_all_mediaingredientmech_ingredients(self) -> list[tuple[str, str]]:
        """Get all MediaIngredientMech ingredients as (id, name) tuples for matching.

        Returns:
            List of (ingredient_id, ingredient_name) tuples
        """
        try:
            ingredients = self.load_ingredient_index()
            return [(ing["id"], ing["preferred_term"]) for ing in ingredients]
        except FileNotFoundError as e:
            print(f"Warning: {e}")
            return []


class MediaMatcher:
    """Fuzzy match media names and ingredient names."""

    def __init__(self, fuzzy_threshold: float = 0.85, manual_overrides: dict | None = None):
        """Initialize media matcher.

        Args:
            fuzzy_threshold: Minimum similarity score (0-1) for fuzzy match
            manual_overrides: Manual mapping overrides from conf/media_mappings.yaml
        """
        self.fuzzy_threshold = fuzzy_threshold
        self.manual_overrides = manual_overrides or {}

    def match_media_name(
        self, query: str, candidates: list[tuple[str, str]]
    ) -> tuple[str, str, float] | None:
        """Match media name to CultureMech records.

        Args:
            query: Media name to match
            candidates: List of (media_id, media_name) tuples

        Returns:
            Tuple of (media_id, media_name, score) or None if no match
        """
        # Check manual overrides first
        if self.manual_overrides and "media_overrides" in self.manual_overrides:
            media_overrides = self.manual_overrides["media_overrides"]
            if media_overrides and query in media_overrides:
                override = media_overrides[query]
                return (override["culturemech_id"], query, 1.0)

        # Exact match (case-insensitive)
        query_lower = query.lower().strip()
        for media_id, media_name in candidates:
            if media_name.lower().strip() == query_lower:
                return (media_id, media_name, 1.0)

        # Substring match (higher priority for exact substring)
        for media_id, media_name in candidates:
            cand_lower = media_name.lower().strip()
            # Check if candidate name is in query or query is in candidate
            if cand_lower in query_lower or query_lower in cand_lower:
                # Calculate a score based on length ratio
                shorter = min(len(query_lower), len(cand_lower))
                longer = max(len(query_lower), len(cand_lower))
                score = 0.9 * (shorter / longer)  # Score between 0.0-0.9
                if score >= self.fuzzy_threshold:
                    return (media_id, media_name, score)

        # Token-based matching (check if all tokens from shorter name are in longer name)
        query_tokens = set(query_lower.split())
        best_token_match = None
        best_token_score = 0.0

        for media_id, media_name in candidates:
            cand_lower = media_name.lower().strip()
            cand_tokens = set(cand_lower.split())

            # Use smaller token set as reference
            if len(query_tokens) <= len(cand_tokens):
                matched_tokens = query_tokens & cand_tokens
                score = len(matched_tokens) / len(query_tokens) if query_tokens else 0
            else:
                matched_tokens = query_tokens & cand_tokens
                score = len(matched_tokens) / len(cand_tokens) if cand_tokens else 0

            # Boost score if key terms match
            if score > 0.5 and score > best_token_score:
                best_token_score = score
                best_token_match = (
                    media_id,
                    media_name,
                    score * 0.95,
                )  # Slightly lower than exact match

        if best_token_match and best_token_score >= self.fuzzy_threshold:
            return best_token_match

        # Fuzzy sequence match (fallback)
        best_match = None
        best_score = 0.0

        for media_id, media_name in candidates:
            score = SequenceMatcher(None, query_lower, media_name.lower().strip()).ratio()
            if score >= self.fuzzy_threshold and score > best_score:
                best_score = score
                best_match = (media_id, media_name, score)

        return best_match

    def match_ingredient_name(
        self, query: str, candidates: list[tuple[str, str]]
    ) -> tuple[str, str, float] | None:
        """Match ingredient name to MediaIngredientMech records.

        Args:
            query: Ingredient name to match
            candidates: List of (ingredient_id, ingredient_name) tuples

        Returns:
            Tuple of (ingredient_id, ingredient_name, score) or None if no match
        """
        # Check manual overrides first
        if self.manual_overrides and "ingredient_overrides" in self.manual_overrides:
            ingredient_overrides = self.manual_overrides["ingredient_overrides"]
            if ingredient_overrides and query in ingredient_overrides:
                override = ingredient_overrides[query]
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
            score = SequenceMatcher(None, query_lower, ingredient_name.lower().strip()).ratio()
            if score >= self.fuzzy_threshold and score > best_score:
                best_score = score
                best_match = (ingredient_id, ingredient_name, score)

        return best_match


class CompositionMerger:
    """Merge CultureMech ingredients with existing community ingredients."""

    def merge_compositions(
        self,
        existing: list[dict],
        culturemech: list[dict],
        mark_source: bool = True,
    ) -> list[dict]:
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
