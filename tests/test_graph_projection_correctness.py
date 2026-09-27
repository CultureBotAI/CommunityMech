"""Unknown vectors cannot supply host evidence or increase taxon coverage."""

import numpy as np
import pytest
import yaml

from communitymech.embedding.aggregator import CommunityVectorAggregator


def community(tmp_path, taxa):
    path = tmp_path / "example.yaml"
    path.write_text(
        yaml.safe_dump({"taxonomy": [{"taxon_term": {"term": {"id": taxon}}} for taxon in taxa]})
    )
    return str(path)


def test_default_threshold_counts_missing_taxa(tmp_path):
    path = community(tmp_path, ["NCBITaxon:1", "NCBITaxon:2"])
    aggregator = CommunityVectorAggregator({"NCBITaxon:1": np.array([1.0, 2.0])})
    assert aggregator.aggregate_community(path, min_coverage=0.9) is None
    vector, metadata = aggregator.aggregate_community(path, min_coverage=0.5)
    np.testing.assert_array_equal(vector, [1.0, 2.0])
    assert metadata["coverage_pct"] == 50.0
    assert metadata["num_taxa"] == 2
    assert metadata["num_embedded_taxa"] == 1
    assert metadata["taxa_missing"] == ["NCBITaxon:2"]
    assert metadata["taxa_excluded"] == []
    assert metadata["coverage_denominator"] == "unique_requested_taxa"
    assert "num_microbial_taxa" not in metadata


def test_duplicate_taxa_neither_reweight_vectors_nor_denominator(tmp_path):
    path = community(tmp_path, ["NCBITaxon:1", "NCBITaxon:1", "NCBITaxon:2"])
    aggregator = CommunityVectorAggregator(
        {"NCBITaxon:1": np.array([0.0, 2.0]), "NCBITaxon:2": np.array([2.0, 0.0])}
    )
    vector, metadata = aggregator.aggregate_community(path)
    np.testing.assert_array_equal(vector, [1.0, 1.0])
    assert metadata["num_taxa"] == 2
    summed, _ = aggregator.aggregate_community(path, aggregation_method="sum")
    np.testing.assert_array_equal(summed, [2.0, 2.0])


def test_unsupported_host_exclusion_and_invalid_threshold_fail(tmp_path):
    path = community(tmp_path, ["NCBITaxon:1"])
    aggregator = CommunityVectorAggregator({})
    with pytest.raises(ValueError, match="independent taxonomy evidence"):
        aggregator.aggregate_community(path, exclude_hosts=True)
    for invalid in (-0.1, 1.1):
        with pytest.raises(ValueError, match="min_coverage"):
            aggregator.aggregate_community(path, min_coverage=invalid)
    assert aggregator.aggregate_community(path, min_coverage=0) is None


def test_cli_defaults_include_all_requested_taxa():
    from communitymech.cli import generate_umap

    parameter = next(item for item in generate_umap.params if item.name == "include_hosts")
    assert parameter.default is True
