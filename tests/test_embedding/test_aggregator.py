"""Tests for community vector aggregator."""

import tempfile
from pathlib import Path

import numpy as np

from communitymech.embedding.aggregator import CommunityVectorAggregator


def test_aggregator_mean_pooling():
    """Test mean pooling aggregation."""
    # Create mock embeddings
    embeddings = {
        "NCBITaxon:1": np.array([1.0, 2.0, 3.0]),
        "NCBITaxon:2": np.array([4.0, 5.0, 6.0]),
        "NCBITaxon:3": np.array([7.0, 8.0, 9.0]),
    }

    # Create mock YAML file
    yaml_content = """
name: Test Community
taxonomy:
  - taxon_term:
      term:
        id: NCBITaxon:1
        label: Taxon 1
  - taxon_term:
      term:
        id: NCBITaxon:2
        label: Taxon 2
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(yaml_content)
        yaml_path = f.name

    try:
        aggregator = CommunityVectorAggregator(embeddings)
        result = aggregator.aggregate_community(yaml_path, min_coverage=0.5)

        assert result is not None
        vector, metadata = result

        # Check mean pooling: (1+4)/2, (2+5)/2, (3+6)/2
        expected = np.array([2.5, 3.5, 4.5])
        np.testing.assert_array_almost_equal(vector, expected)

        # Check metadata
        assert metadata["num_taxa"] == 2
        assert metadata["coverage_pct"] == 100.0
        assert len(metadata["taxa_found"]) == 2
        assert len(metadata["taxa_missing"]) == 0

    finally:
        Path(yaml_path).unlink()


def test_aggregator_low_coverage():
    """Test that low coverage communities are skipped."""
    embeddings = {
        "NCBITaxon:1": np.array([1.0, 2.0, 3.0]),
    }

    yaml_content = """
name: Test Community
taxonomy:
  - taxon_term:
      term:
        id: NCBITaxon:1
        label: Taxon 1
  - taxon_term:
      term:
        id: NCBITaxon:2
        label: Taxon 2
  - taxon_term:
      term:
        id: NCBITaxon:3
        label: Taxon 3
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(yaml_content)
        yaml_path = f.name

    try:
        aggregator = CommunityVectorAggregator(embeddings)
        # Only 1/3 taxa have embeddings, below 0.5 threshold.
        # Pass exclude_hosts=False so the strict coverage check applies;
        # the default exclude_hosts=True treats missing taxa as hosts and
        # would consider this community fully covered.
        result = aggregator.aggregate_community(yaml_path, min_coverage=0.5, exclude_hosts=False)

        assert result is None

    finally:
        Path(yaml_path).unlink()


def test_extract_taxon_ids():
    """Test extraction of NCBITaxon IDs from YAML."""
    embeddings = {}
    aggregator = CommunityVectorAggregator(embeddings)

    yaml_data = {
        "taxonomy": [
            {"taxon_term": {"term": {"id": "NCBITaxon:562", "label": "E. coli"}}},
            {"taxon_term": {"term": {"id": "NCBITaxon:1280", "label": "S. aureus"}}},
        ]
    }

    taxon_ids = aggregator._extract_taxon_ids(yaml_data)

    assert len(taxon_ids) == 2
    assert "NCBITaxon:562" in taxon_ids
    assert "NCBITaxon:1280" in taxon_ids
