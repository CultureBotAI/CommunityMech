"""Dimensionality reduction using PaCMAP (default) or UMAP."""

import numpy as np
import pandas as pd
import umap  # type: ignore[import-untyped]
from sklearn.preprocessing import normalize  # type: ignore[import-untyped]


class UMAPReducer:
    """Reduce high-dimensional embeddings to 2D using PaCMAP or UMAP.

    PaCMAP (PCA-initialized, fixed seed) is the default reducer; UMAP is
    kept as a selectable option via ``method="umap"``. Regardless of the
    method, the returned DataFrame uses the columns ``community_id``,
    ``umap_x``, ``umap_y`` (the template/generator depend on them).
    """

    def __init__(
        self,
        method: str = "pacmap",
        n_neighbors: int = 15,
        min_dist: float = 0.1,
        metric: str = "cosine",
        random_state: int = 42,
        n_components: int = 2,
    ):
        """Initialize the 2D reducer.

        Args:
            method: Reduction method, "pacmap" (default) or "umap"
            n_neighbors: Number of neighbors for UMAP (controls local vs global structure)
            min_dist: Minimum distance between points in low-dimensional space (UMAP)
            metric: Distance metric (cosine recommended for embeddings; UMAP)
            random_state: Random seed for reproducibility
            n_components: Number of output dimensions (2 for visualization)
        """
        self.method = method
        self.random_state = random_state
        self.n_neighbors = n_neighbors
        self.min_dist = min_dist
        self.metric = metric
        self.n_components = n_components

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

        print(f"🔄 Running {self.method.upper()} on {len(community_ids)} communities...")
        print(f"   Input shape: {vectors_matrix.shape}")

        if self.method == "pacmap":
            import pacmap  # type: ignore[import-untyped]

            # L2-normalize rows to mirror cosine geometry, then PCA-init + fixed seed.
            normalized_vectors = normalize(vectors_matrix.astype("float32"))
            coords = pacmap.PaCMAP(
                n_components=self.n_components,
                random_state=self.random_state,
            ).fit_transform(normalized_vectors, init="pca")
        elif self.method == "sfdp":
            # Force-directed (Graphviz sfdp) layout of the mutual-kNN graph over
            # the KG embeddings — a global-structure-first graph view.
            from communitymech.embedding.graph_layout import sfdp_layout

            coords = sfdp_layout(vectors_matrix, k=15, seed=self.random_state)
        else:
            reducer = umap.UMAP(
                n_neighbors=self.n_neighbors,
                min_dist=self.min_dist,
                metric=self.metric,
                random_state=self.random_state,
                n_components=self.n_components,
            )
            coords = reducer.fit_transform(vectors_matrix)

        print(f"✅ {self.method.upper()} complete. Output shape: {coords.shape}")

        # Build DataFrame (columns kept as umap_x/umap_y for template compatibility)
        df = pd.DataFrame(
            {
                "community_id": community_ids,
                "umap_x": coords[:, 0],
                "umap_y": coords[:, 1],
            }
        )

        return df
