"""Generate interactive UMAP visualization of community embedding space."""

import json
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader

from communitymech.embedding import (
    CommunityVectorAggregator,
    EmbeddingLoader,
    UMAPReducer,
)


class UMAPVisualizationGenerator:
    """Generate interactive UMAP HTML visualization of communities."""

    def generate(
        self,
        communities_dir: str = "kb/communities",
        embeddings_path: str = "data/embeddings/DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v2_2026-04-25_20_44_08.tsv.gz",
        output_path: str = "docs/community_umap.html",
        template_dir: str | None = None,
        cache_dir: str = ".umap_cache",
        force_reload: bool = False,
        n_neighbors: int = 15,
        min_dist: float = 0.1,
        min_coverage: float = 0.5,
        exclude_hosts: bool = True,
    ):
        """Generate interactive UMAP visualization.

        Args:
            communities_dir: Directory containing community YAML files
            embeddings_path: Path to KG-Microbe embeddings TSV.gz
            output_path: Output HTML file path
            template_dir: Template directory (auto-detected if None)
            cache_dir: Cache directory for embeddings
            force_reload: Force reload embeddings from TSV.gz
            n_neighbors: UMAP n_neighbors parameter
            min_dist: UMAP min_dist parameter
            min_coverage: Minimum embedding coverage for communities
            exclude_hosts: Exclude non-microbial taxa (hosts) from representation
        """
        print("=" * 60)
        print("🔬 CommunityMech UMAP Visualization Generator")
        print("=" * 60)

        # Step 1: Load embeddings
        loader = EmbeddingLoader(embeddings_path, cache_dir=cache_dir)
        embeddings = loader.load_embeddings(prefixes=["NCBITaxon"], force_reload=force_reload)

        embedding_dim = loader.get_embedding_dim(embeddings)
        print(f"📊 Embedding dimension: {embedding_dim}")

        # Step 2: Aggregate communities
        aggregator = CommunityVectorAggregator(embeddings)
        community_vectors, aggregation_metadata = aggregator.aggregate_communities(
            communities_dir, min_coverage=min_coverage, exclude_hosts=exclude_hosts
        )

        print(f"\n📦 Aggregated {len(community_vectors)} communities")
        if exclude_hosts:
            print(
                f"   (excluded non-microbial host taxa from {self._count_yaml_files(communities_dir) - len(community_vectors)} communities)"
            )
        else:
            print(
                f"   (skipped {self._count_yaml_files(communities_dir) - len(community_vectors)} due to low coverage)"
            )

        # Step 3: Run UMAP
        reducer = UMAPReducer(n_neighbors=n_neighbors, min_dist=min_dist, random_state=42)
        umap_df = reducer.fit_transform(community_vectors)

        # Step 4: Extract metadata from community YAMLs
        community_data = self._build_community_data(umap_df, aggregation_metadata, communities_dir)

        print(f"\n📝 Generated data for {len(community_data)} communities")

        # Step 5: Render HTML template
        self._render_html(community_data, output_path, template_dir)

        print(f"\n✅ UMAP visualization generated: {output_path}")
        print("=" * 60)

    def _count_yaml_files(self, communities_dir: str) -> int:
        """Count YAML files in directory."""
        return len(list(Path(communities_dir).glob("*.yaml")))

    def _build_community_data(
        self,
        umap_df,
        aggregation_metadata: dict[str, dict[str, Any]],
        communities_dir: str,
    ) -> list[dict[str, Any]]:
        """Build JSON data structure for visualization.

        Args:
            umap_df: DataFrame with community_id, umap_x, umap_y
            aggregation_metadata: Metadata from aggregation
            communities_dir: Directory with community YAMLs

        Returns:
            List of community data dictionaries
        """
        community_data = []
        communities_dir_path = Path(communities_dir)

        for _, row in umap_df.iterrows():
            community_id = row["community_id"]
            yaml_path = communities_dir_path / f"{community_id}.yaml"

            # Parse YAML for metadata
            with open(yaml_path) as f:
                yaml_data = yaml.safe_load(f)

            # Extract metadata
            metadata = aggregation_metadata.get(community_id, {})

            # Count interactions (ecological_interactions is a list directly)
            ecological_interactions = yaml_data.get("ecological_interactions", [])
            num_interactions = (
                len(ecological_interactions) if isinstance(ecological_interactions, list) else 0
            )

            # Get category, state, origin
            category = yaml_data.get("community_category", "UNKNOWN")
            ecological_state = yaml_data.get("ecological_state", "UNKNOWN")
            origin = yaml_data.get("community_origin", "UNKNOWN")

            # Get environment description
            env_term = yaml_data.get("environment_term", {})
            environment = env_term.get("preferred_term", "Not specified")

            # Get name
            name = yaml_data.get("name", community_id.replace("_", " "))

            # Use microbial taxa count if available (when exclude_hosts=True)
            num_taxa = metadata.get("num_microbial_taxa", metadata.get("num_taxa", 0))

            community_data.append(
                {
                    "id": community_id,
                    "name": name,
                    "umap_x": float(row["umap_x"]),
                    "umap_y": float(row["umap_y"]),
                    "category": category,
                    "ecological_state": ecological_state,
                    "origin": origin,
                    "environment": environment,
                    "num_taxa": num_taxa,
                    "num_interactions": num_interactions,
                    "coverage_pct": metadata.get("coverage_pct", 0.0),
                    "url": f"communities/{community_id}.html",
                }
            )

        return community_data

    def _render_html(
        self,
        community_data: list[dict[str, Any]],
        output_path: str,
        template_dir: str | None = None,
    ):
        """Render HTML template with community data.

        Args:
            community_data: List of community data dictionaries
            output_path: Output HTML file path
            template_dir: Template directory (auto-detected if None)
        """
        # Auto-detect template directory
        if template_dir is None:
            template_dir = str(Path(__file__).parent.parent / "templates")

        # Set up Jinja2 environment
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("community_umap.html")

        # Render template
        html_content = template.render(
            community_data_json=json.dumps(community_data, indent=2),
            num_communities=len(community_data),
        )

        # Write output
        output_path_obj = Path(output_path)
        output_path_obj.parent.mkdir(parents=True, exist_ok=True)
        output_path_obj.write_text(html_content)

        print(f"💾 Wrote {len(html_content):,} bytes to {output_path}")
