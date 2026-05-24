"""Efficient loading of KG-Microbe embeddings with caching."""

import gzip
import pickle
from pathlib import Path

import numpy as np
from tqdm import tqdm


class EmbeddingLoader:
    """Load and cache node embeddings from KG-Microbe TSV.gz file."""

    def __init__(self, embeddings_path: str, cache_dir: str = ".umap_cache"):
        """Initialize loader.

        Args:
            embeddings_path: Path to embeddings TSV.gz file
            cache_dir: Directory for pickle cache
        """
        self.embeddings_path = Path(embeddings_path)
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

    def load_embeddings(
        self,
        prefixes: list[str] | None = None,
        force_reload: bool = False,
    ) -> dict[str, np.ndarray]:
        """Load embeddings filtered by node ID prefixes.

        Args:
            prefixes: List of CURIE prefixes to filter (e.g., ["NCBITaxon"])
                     If None, loads all embeddings (not recommended for 3.2GB file)
            force_reload: If True, ignore cache and reload from TSV.gz

        Returns:
            Dictionary mapping node_id → 512-dim numpy array
        """
        if prefixes is None:
            prefixes = ["NCBITaxon"]  # Default to taxonomy only

        # Generate cache filename based on prefixes
        cache_name = "_".join(sorted(prefixes)) + "_embeddings.pkl"
        cache_path = self.cache_dir / cache_name

        # Try loading from cache
        if not force_reload and cache_path.exists():
            print(f"📦 Loading embeddings from cache: {cache_path}")
            # S301: cache file is written by this same module to a path
            # under self.cache_dir (a developer-controlled location); never
            # loaded from an untrusted source.
            with open(cache_path, "rb") as f:
                embeddings = pickle.load(f)  # noqa: S301
            print(f"✅ Loaded {len(embeddings):,} embeddings from cache")
            return embeddings

        # Load from TSV.gz
        print(f"📂 Loading embeddings from {self.embeddings_path.name}")
        print(f"   Filtering to prefixes: {', '.join(prefixes)}")

        embeddings = {}

        # First pass: count total lines for progress bar
        print("   Counting lines...")
        with gzip.open(self.embeddings_path, "rt") as f:
            total_lines = sum(1 for _ in f)

        # Second pass: parse and filter
        with gzip.open(self.embeddings_path, "rt") as f:
            for line in tqdm(f, total=total_lines, desc="   Parsing", unit=" nodes"):
                parts = line.strip().split("\t")
                if len(parts) < 2:
                    continue

                node_id = parts[0]

                # Check if node_id matches any prefix
                if not any(node_id.startswith(f"{prefix}:") for prefix in prefixes):
                    continue

                # Parse embedding vector
                try:
                    vector = np.array([float(x) for x in parts[1:]], dtype=np.float32)
                    embeddings[node_id] = vector
                except (ValueError, IndexError):
                    continue

        print(f"✅ Loaded {len(embeddings):,} embeddings")

        # Save to cache
        print(f"💾 Caching to {cache_path}")
        with open(cache_path, "wb") as f:
            pickle.dump(embeddings, f, protocol=pickle.HIGHEST_PROTOCOL)

        return embeddings

    def get_embedding_dim(self, embeddings: dict[str, np.ndarray]) -> int:
        """Get dimensionality of embeddings.

        Args:
            embeddings: Dictionary of embeddings

        Returns:
            Embedding dimension (e.g., 512)
        """
        if not embeddings:
            return 0
        first_embedding = next(iter(embeddings.values()))
        return len(first_embedding)
