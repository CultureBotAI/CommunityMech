"""Graphviz must return one finite coordinate per actual projected row."""

import shutil

import numpy as np
import pytest

from communitymech.embedding.graph_layout import sfdp_layout


@pytest.mark.skipif(
    shutil.which("sfdp") is None, reason="Graphviz sfdp is an optional graph backend"
)
def test_real_sfdp_returns_all_rows_and_actual_graph_receipt():
    matrix = np.random.default_rng(42).normal(size=(12, 5))
    points, graph = sfdp_layout(
        matrix, k=3, return_receipt=True, record_ids=[f"row:{i}" for i in range(12)]
    )
    assert points.shape == (12, 2) and np.isfinite(points).all()
    assert graph["construction"] == "symmetric_union_knn"
    assert graph["effective_k"] == 3 and graph["edges"] > 0
    assert "graphviz" in graph["graphviz_version"].lower()
    assert graph["matrix"]["shape"] == [12, 5]
    assert graph["matrix"]["row_ids"][0] == "row:0"
