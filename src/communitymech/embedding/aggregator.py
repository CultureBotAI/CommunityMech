"""Aggregate node embeddings to community-level vectors."""

from pathlib import Path
from typing import Any

import numpy as np
import yaml


class CommunityVectorAggregator:
    """Aggregate taxonomic embeddings to create community-level vectors."""

    def __init__(self, embeddings: dict[str, np.ndarray]):
        """Initialize aggregator.

        Args:
            embeddings: Dictionary mapping node_id → embedding vector
        """
        self.embeddings = embeddings

    def aggregate_community(
        self,
        community_yaml_path: str,
        min_coverage: float = 0.5,
        aggregation_method: str = "mean",
        exclude_hosts: bool = False,
    ) -> tuple[np.ndarray, dict[str, Any]] | None:
        """Aggregate embeddings for a community from its YAML file.

        Args:
            community_yaml_path: Path to community YAML file
            min_coverage: Minimum fraction of taxa that must have embeddings
            aggregation_method: Aggregation method ("mean" or "sum")
            exclude_hosts: Deprecated; true fails without an independent host classifier.

        Returns:
            Tuple of (community_vector, metadata) or None if coverage too low

            Metadata includes:
                - coverage_pct: Percentage of taxa with embeddings
                - num_taxa: Number of unique requested taxa
                - num_embedded_taxa: Number of requested taxa with vectors
                - taxa_found: List of taxa IDs found in embeddings
                - taxa_missing: List of taxa IDs missing from embeddings
                - taxa_excluded: Empty; no host classification was attempted
                - aggregation_method: Method used for aggregation
        """
        if exclude_hosts:
            raise ValueError(
                "Host exclusion requires independent taxonomy evidence; "
                "missing vectors are not hosts"
            )
        if not 0 <= min_coverage <= 1:
            raise ValueError("min_coverage must be between 0 and 1")
        # Parse YAML
        with open(community_yaml_path) as f:
            community_data = yaml.safe_load(f)

        # Extract NCBITaxon IDs from taxonomy section
        taxon_ids = self._extract_taxon_ids(community_data)

        if not taxon_ids:
            return None

        # Lookup embeddings
        found_embeddings = []
        found_ids = []
        missing_ids = []

        for taxon_id in taxon_ids:
            if taxon_id in self.embeddings:
                found_embeddings.append(self.embeddings[taxon_id])
                found_ids.append(taxon_id)
            else:
                missing_ids.append(taxon_id)

        # Every unique requested taxon is in the denominator. An absent
        # graph vector is missing data, never evidence of a host classification.
        coverage = len(found_ids) / len(taxon_ids)
        if not found_embeddings or coverage < min_coverage:
            return None

        # Aggregate embeddings
        if aggregation_method == "mean":
            community_vector = np.mean(found_embeddings, axis=0)
        elif aggregation_method == "sum":
            community_vector = np.sum(found_embeddings, axis=0)
        else:
            raise ValueError(f"Unknown aggregation method: {aggregation_method}")

        # Build metadata
        metadata = {
            "coverage_pct": coverage * 100,
            "num_taxa": len(taxon_ids),
            "num_embedded_taxa": len(found_ids),
            "coverage_denominator": "unique_requested_taxa",
            "taxa_found": found_ids,
            "taxa_missing": missing_ids,
            "aggregation_method": aggregation_method,
        }

        metadata["taxa_excluded"] = []

        return community_vector, metadata

    def _extract_taxon_ids(self, community_data: dict[str, Any]) -> list[str]:
        """Extract NCBITaxon IDs from community YAML data.

        Args:
            community_data: Parsed YAML data

        Returns:
            List of NCBITaxon IDs (e.g., ["NCBITaxon:562", "NCBITaxon:1280"])
        """
        taxon_ids = []

        # Navigate to taxonomy section
        taxonomy = community_data.get("taxonomy", [])

        for taxon_entry in taxonomy:
            # Extract taxon_term.term.id
            taxon_term = taxon_entry.get("taxon_term", {})
            term = taxon_term.get("term", {})
            taxon_id = term.get("id")

            if taxon_id and taxon_id.startswith("NCBITaxon:"):
                taxon_ids.append(taxon_id)

        return list(dict.fromkeys(taxon_ids))

    def aggregate_communities(
        self,
        community_dir: str,
        min_coverage: float = 0.5,
        aggregation_method: str = "mean",
        exclude_hosts: bool = False,
    ) -> tuple[dict[str, np.ndarray], dict[str, dict[str, Any]]]:
        """Aggregate all communities in a directory.

        Args:
            community_dir: Directory containing community YAML files
            min_coverage: Minimum coverage threshold
            aggregation_method: Aggregation method
            exclude_hosts: Deprecated; true requires an independent host classifier.

        Returns:
            Tuple of:
                - Dictionary mapping community_id → community_vector
                - Dictionary mapping community_id → metadata
        """
        community_dir_path = Path(community_dir)
        community_vectors = {}
        community_metadata = {}

        yaml_files = sorted(community_dir_path.glob("*.yaml"))

        for yaml_path in yaml_files:
            community_id = yaml_path.stem

            result = self.aggregate_community(
                str(yaml_path),
                min_coverage=min_coverage,
                aggregation_method=aggregation_method,
                exclude_hosts=exclude_hosts,
            )

            if result is not None:
                vector, metadata = result
                community_vectors[community_id] = vector
                community_metadata[community_id] = metadata
            else:
                print(f"⚠️  Skipping {community_id} (no vectors or below minimum taxon coverage)")

        return community_vectors, community_metadata
