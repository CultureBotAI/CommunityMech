"""Keep machine-checked graph health distinct from recorded semantic review."""

import importlib.util
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "causal_review_inventory", REPO / "reports/causal_graph_review/build_inventory.py"
)
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


@pytest.fixture
def case():
    edge = {"target": "B", "description": "A enables B"}
    doc = {
        "id": "CommunityMech:1",
        "ecological_interactions": [
            {"name": "A", "downstream": [edge]},
            {"name": "B"},
        ],
    }
    review = {
        "id": doc["id"],
        "record_sha256": "current-digest",
        "status": "reviewed",
        "scope": "All nodes and edges compared with source passages",
        "references": ["PMID:1"],
        "node_decisions": [
            {"node": "A", "rationale": "Upstream perturbation is measured"},
            {"node": "B", "rationale": "Downstream change is measured"},
        ],
        "edges_after": [{"source": "A", **deepcopy(edge)}],
    }
    return doc, review


def test_unreviewed_and_stale_records_are_not_complete(case):
    doc, review = case
    assert inventory.review_status(doc, "current-digest", None) == "pending"
    assert inventory.review_status(doc, "changed-digest", review) == "stale"


def test_complete_review_passes(case):
    doc, review = case
    assert inventory.review_status(doc, "current-digest", review) == "reviewed"


@pytest.mark.parametrize("status", ["pending", "needs_research"])
def test_incomplete_review_does_not_require_completion_fields(case, status):
    doc, review = case
    review["status"] = status
    del review["node_decisions"]
    del review["edges_after"]
    assert inventory.review_status(doc, "current-digest", review) == status


@pytest.mark.parametrize("change", ["missing", "duplicate", "unknown", "blank"])
def test_node_decisions_must_cover_current_nodes_once(case, change):
    doc, review = case
    if change == "missing":
        review["node_decisions"].pop()
    elif change == "duplicate":
        review["node_decisions"].append(deepcopy(review["node_decisions"][0]))
    elif change == "unknown":
        review["node_decisions"][0]["node"] = "Not a node"
    else:
        review["node_decisions"][0]["rationale"] = "  "
    with pytest.raises(ValueError, match="[Nn]ode"):
        inventory.review_status(doc, "current-digest", review)


@pytest.mark.parametrize("change", ["missing", "direction", "description"])
def test_edge_snapshot_must_match_current_graph(case, change):
    doc, review = case
    if change == "missing":
        review["edges_after"] = []
    elif change == "direction":
        review["edges_after"][0].update(source="B", target="A")
    else:
        review["edges_after"][0]["description"] = "A inhibits B"
    with pytest.raises(ValueError, match="After-edge"):
        inventory.review_status(doc, "current-digest", review)


@pytest.mark.parametrize(
    "field,value", [("status", "done"), ("id", "wrong-id"), ("scope", ""), ("references", [])]
)
def test_invalid_metadata_rejected(case, field, value):
    doc, review = case
    review[field] = value
    with pytest.raises(ValueError):
        inventory.review_status(doc, "current-digest", review)


def test_review_pointer_must_name_loaded_artifact(tmp_path, monkeypatch):
    record = tmp_path / "kb/communities/record.yaml"
    record.parent.mkdir(parents=True)
    record.write_text("id: CommunityMech:1\n")
    output = tmp_path / "reports/causal_graph_review"
    decisions = output / "decisions"
    decisions.mkdir(parents=True)
    (decisions / "review.yaml").write_text(
        yaml.safe_dump({"records": [{"review_file": "wrong-artifact.yaml"}]})
    )
    monkeypatch.setattr(inventory, "ROOT", tmp_path)
    monkeypatch.setattr(inventory, "OUT", output)
    monkeypatch.setattr(inventory, "record_files", lambda: [record])
    monkeypatch.setattr(inventory, "default_record_roots", lambda: [record.parent])
    monkeypatch.setattr(inventory, "load_module", lambda *args: None)
    with pytest.raises(ValueError, match="review-file pointer"):
        inventory.main()
