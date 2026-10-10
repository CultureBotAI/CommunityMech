"""Keep cinnamate products bounded and preserve the supported isoDCA graph."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-two-records-batch16.yaml"


def cinnamate():
    return yaml.safe_load(
        (ROOT / "kb/communities/Cinnamate_Degradation_Consortium.yaml").read_text()
    )


def test_benzoate_connection_survives_without_unsupported_fatty_acid_typing():
    first, benzoate, methane = cinnamate()["ecological_interactions"]
    assert "interaction_type" not in first
    assert "biological_processes" not in first
    assert "BESA" in first["description"]
    assert first["downstream"][0]["target"] == benzoate["name"]
    assert "supplies substrate" in first["downstream"][0]["description"]
    assert benzoate["interaction_type"] == "SYNTROPHY"
    assert benzoate["downstream"][0]["target"] == methane["name"]


def test_hydrogen_route_is_not_promoted_to_measured_transfer():
    _, benzoate, methane = cinnamate()["ecological_interactions"]
    assert "HYPOTHESIZED" in benzoate["description"]
    assert benzoate["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert "HYPOTHESIZED" in methane["description"]
    assert methane["evidence"][0]["supports"] == "PARTIAL"
    assert all(
        m["term"]["id"] != "CHEBI:18276" for n in (benzoate, methane) for m in n["metabolites"]
    )
    assert "Acetate remains" in methane["description"]
    assert (
        "complete mineralization of all cinnamate carbon is not established"
        in methane["description"]
    )


def test_carrier_gap_has_valid_anchors_and_methanogen_provenance():
    doc = cinnamate()
    names = {n["name"] for n in doc["ecological_interactions"]}
    assert "replaced the original" in doc["ecological_interactions"][2]["description"]
    gap = doc["discussions"][0]
    assert gap["kind"] == "KNOWLEDGE_GAP"
    assert gap["status"] == "OPEN"
    assert {a.split("#", 1)[1] for a in gap["attaches_to"]} == names


def test_batch16_ledger_covers_all_structure_and_unchanged_isodca():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1313]
    assert ledger["open_nongraph_followups"] == [1314]
    changed, unchanged = ledger["records"]
    assert changed["curation_events_added"] == 1
    assert len(changed["history_files"]) == 1
    assert len(changed["edges_after"]) == 2
    assert unchanged["outcome"] == "no_change"
    assert unchanged["record_sha256"] == unchanged["original_sha256"]
    assert unchanged["history_files"] == []
    assert unchanged["allowed_changed_fields"] == []
    assert unchanged["edges_after"] == []
    for row in ledger["records"]:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        before = {(e["source"], e["target"]) for e in row["edges_before"]}
        after = {(e["source"], e["target"]) for e in row["edges_after"]}
        assert before == after
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
