"""Keep outcome evidence distinct from partner fitness and causal carbon fate."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch92.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_puer_association_needs_no_forced_mechanism_or_record_edit():
    _, rows, docs = records()
    row, doc = rows[0], docs[0]
    assert row["outcome"] == "unchanged" and row["allowed_changed_fields"] == []
    assert row["original_sha256"] == row["record_sha256"]
    assert row["history_files"] == [] and row["curation_events_added"] == 0
    (node,) = doc["ecological_interactions"]
    assert "interaction_type" not in node and "downstream" not in node
    assert "associated with" in node["description"]
    assert all(e["supports"] == "SUPPORT" for e in node["evidence"])


def test_qy2_feedback_is_a_hypothesis_not_a_demonstrated_partner_route():
    _, _, docs = records()
    (node,) = docs[1]["ecological_interactions"]
    assert node["description"].startswith("HYPOTHESIZED:")
    assert "hydrogen consumer" in node["description"]
    assert "not as a demonstrated hydrogen donor" in node["description"]
    assert "product-removal feedback" in node["description"]
    assert "interaction_type" not in node and "downstream" not in node
    assert node["evidence"][0]["supports"] == "PARTIAL"
    assert "does not assert obligacy" in docs[1]["discussions"][-1]["rationale"]


def test_scdy1_preserves_plant_benefit_without_inventing_reciprocal_fitness():
    _, _, docs = records()
    (node,) = docs[2]["ecological_interactions"]
    assert "120 mM NaCl" in node["description"]
    assert "not evidence of reciprocal fitness" in node["description"]
    assert "interaction_type" not in node and "downstream" not in node
    assert node["evidence"][0]["supports"] == "SUPPORT"
    assert "missing access is not evidence" in docs[2]["discussions"][-1]["rationale"]
    assert "growth_media" not in docs[2]


def test_rh1_keeps_two_endpoints_but_no_mutualism_or_carbon_fate_arrow():
    _, _, docs = records()
    removal, toc = docs[3]["ecological_interactions"]
    assert all("interaction_type" not in n and "downstream" not in n for n in [removal, toc])
    assert "previously reported single-strain" in removal["description"]
    assert "91.03%" in toc["description"]
    assert "centrifugation and filtration" in toc["description"]
    assert "does not distinguish mineralization" in toc["description"]
    assert "predicted, not an empirical carbon balance" in docs[3]["discussions"][-1]["rationale"]
    assert docs[3]["discussions"][0]["discussion_id"] == "rh1_glyphosate_pathway_genes"


def test_every_existing_node_and_removed_arrow_has_a_disposition():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 5
    assert sum(len(r["edges_before"]) for r in rows) == 1
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    for row, doc in zip(rows, docs, strict=True):
        assert not row["edges_after"] and not row["removed_node_decisions"]
        assert {r["node"] for r in row["node_decisions"]} == {
            n["name"] for n in doc["ecological_interactions"]
        }
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_provenance_does_not_disguise_selected_excerpts_as_independent_sources():
    ledger, _, _ = records()
    checks = ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    assert len(checks) == 10 and all(c["cache_matched"] for c in checks)
    assert sum(c["independent_primary_match"] for c in checks) == 8
    selected = [c for c in checks if c["cache_is_selected_excerpt"]]
    assert len(selected) == 1 and selected[0]["matched_artifact"].endswith("quinoa-abstract.txt")
    assert ledger["cache_changes"] == []
    for path, digest in ledger["primary_artifacts"].items():
        if not path.startswith("/"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest


def test_repair_history_and_approval_limits_are_explicit():
    ledger, rows, docs = records()
    assert ledger["issues"] == [1746, 1747, 1748] and not ledger["independent_approval"]
    assert [r["curation_events_added"] for r in rows] == [0, 1, 1, 1]
    assert sum(len(r["history_files"]) for r in rows) == 3
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"] == []
    for row, doc in zip(rows[1:], docs[1:], strict=True):
        assert doc["curation_history"][-1]["llm_assisted"]
        assert (ROOT / row["history_files"][0]).is_file()
