"""Streaming source-bound loading of selected KG-Microbe vectors."""

from pathlib import Path

import numpy as np

from communitymech.graph_embedding_receipts import GraphSource
from communitymech.paths import REPO_ROOT


class EmbeddingLoader:
    """Read node embeddings directly from the selected KG-Microbe source."""

    def __init__(self, embeddings_path: str, cache_dir: str | Path = REPO_ROOT / ".umap_cache"):
        """Initialize loader.

        Args:
            embeddings_path: Path to embeddings TSV.gz file
            cache_dir: Compatibility directory; legacy pickle caches are ignored
        """
        self.embeddings_path = Path(embeddings_path)
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

    def load_embeddings(
        self,
        prefixes: list[str] | None = None,
        force_reload: bool = False,
        node_ids=None,
    ) -> dict[str, np.ndarray]:
        """Load embeddings filtered by node ID prefixes.

        Args:
            prefixes: List of CURIE prefixes to filter (e.g., ["NCBITaxon"])
                     If None, selects NCBITaxon nodes
            force_reload: Compatibility option; the source is always read

        Returns:
            Dictionary mapping node_id to a source-dimensional numpy array
        """
        if prefixes is None:
            prefixes = ["NCBITaxon"]  # Default to taxonomy only

        # #905: legacy caches are not a source receipt. Read actual bytes.
        source = GraphSource(self.embeddings_path, prefixes, node_ids=node_ids)
        embeddings = {node: np.asarray(vector, dtype=np.float32) for node, vector in source}
        self.source_receipt = source.receipt
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
