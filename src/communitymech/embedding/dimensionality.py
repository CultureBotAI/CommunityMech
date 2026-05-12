"""Dimensionality reduction using UMAP."""

import numpy as np
import pandas as pd
import umap


class UMAPReducer:
    """Reduce high-dimensional embeddings to 2D using UMAP."""

    def __init__(
        self,
        n_neighbors: int = 15,
        min_dist: float = 0.1,
        metric: str = "cosine",
        random_state: int = 42,
        n_components: int = 2,
    ):
        """Initialize UMAP reducer.

        Args:
            n_neighbors: Number of neighbors for UMAP (controls local vs global structure)
            min_dist: Minimum distance between points in low-dimensional space
            metric: Distance metric (cosine recommended for embeddings)
            random_state: Random seed for reproducibility
            n_components: Number of output dimensions (2 for visualization)
        """
        self.reducer = umap.UMAP(
            n_neighbors=n_neighbors,
            min_dist=min_dist,
            metric=metric,
            random_state=random_state,
            n_components=n_components,
        )

    def fit_transform(
        self,
        community_vectors: dict[str, np.ndarray],
    ) -> pd.DataFrame:
        """Reduce community vectors to 2D.

        Args:
            community_vectors: Dictionary mapping community_id → embedding vector

        Returns:
            DataFrame with columns:
                - community_id: str
                - umap_x: float
                - umap_y: float
        """
        if not community_vectors:
            return pd.DataFrame(columns=["community_id", "umap_x", "umap_y"])

        # Convert dict to matrix
        community_ids = list(community_vectors.keys())
        vectors_matrix = np.vstack([community_vectors[cid] for cid in community_ids])

        print(f"🔄 Running UMAP on {len(community_ids)} communities...")
        print(f"   Input shape: {vectors_matrix.shape}")

        # Run UMAP
        umap_coords = self.reducer.fit_transform(vectors_matrix)

        print(f"✅ UMAP complete. Output shape: {umap_coords.shape}")

        # Build DataFrame
        df = pd.DataFrame(
            {
                "community_id": community_ids,
                "umap_x": umap_coords[:, 0],
                "umap_y": umap_coords[:, 1],
            }
        )

        return df
