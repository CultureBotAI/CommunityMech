"""Separate measured outcomes, predicted functions and proposed causal routes."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-four-records-batch28.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in ledger["records"]]


def test_cultivated_meat_unchanged_review_does_not_invent_edit_history():
    ledger, docs = records()
    row = ledger["records"][0]
    assert row["status"] == "reviewed" and row["outcome"] == "unchanged"
    assert row["original_sha256"] == row["record_sha256"]
    assert not row["history_files"] and row["curation_events_added"] == 0
    assert not row["allowed_changed_fields"]
    assert len(docs[0]["ecological_interactions"]) == 2
    assert not any(n.get("downstream") for n in docs[0]["ecological_interactions"])
    assert "No primary body" in row["source_review"]["PMID:42425643"]["reviewed_scope"]


def test_fahmy_preserves_prediction_and_positive_removal_without_mutualism():
    _, docs = records()
    doc = docs[1]
    prediction, removal = doc["ecological_interactions"]
    for node in [prediction, removal]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert len(node["participating_taxa"]) == 6
        assert not {"interaction_type", "source_taxon", "target_taxon", "downstream"} & node.keys()
    assert prediction["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert "predicted functions" in prediction["description"]
    assert "four-strain design" in prediction["description"]
    assert "not experimentally validated" in prediction["description"]
    for phrase in [
        "57.79 mg/L",
        "1.00 mg/L",
        "98.27%",
        "nominal 60 mg/L",
        "native water microbiota",
    ]:
        assert phrase in removal["description"]
    assert "does not establish complete mineralization" in removal["description"]
    assert removal["evidence"][0]["supports"] == "SUPPORT"
    assert "workflow arrow is not restored" in doc["discussions"][0]["rationale"]


def test_cyprus_removes_analysis_order_arrows_and_unmeasured_fitness_types():
    _, docs = records()
    composition, repertoire, crispr = docs[2]["ecological_interactions"]
    assert all(
        "downstream" not in n and "interaction_type" not in n
        for n in [composition, repertoire, crispr]
    )
    assert len(composition["participating_taxa"]) == 4
    assert "do not isolate Fe" in composition["description"]
    assert "pooled replicate" in composition["description"]
    assert "biological_processes" not in composition
    assert len(repertoire["participating_taxa"]) == 2
    assert "not every host or every listed function" in repertoire["description"]
    assert "not assigned specifically" in repertoire["description"]
    assert repertoire["evidence"][0]["evidence_source"] == "COMPUTATIONAL"


def test_cyprus_crispr_is_host_capability_not_taxon_competition():
    _, docs = records()
    doc = docs[2]
    crispr = doc["ecological_interactions"][2]
    assert crispr["scope"] == "PAIRWISE"
    assert crispr["source_taxon"]["term"] == doc["taxonomy"][0]["taxon_term"]["term"]
    assert (
        not {"target_taxon", "participating_taxa", "interaction_type", "biological_processes"}
        & crispr.keys()
    )
    assert crispr["description"].startswith("HYPOTHESIZED -")
    assert "two unbinned" in crispr["description"]
    assert "do not demonstrate target cleavage" in crispr["description"]
    assert crispr["evidence"][0]["supports"] == "PARTIAL"


def test_dietsimp_retains_two_parallel_hypotheses_and_intrinsic_methanogen():
    _, docs = records()
    doc = docs[3]
    first, second, reduction = doc["ecological_interactions"]
    for donor in [first, second]:
        assert donor["scope"] == "PAIRWISE" and donor["interaction_type"] == "SYNTROPHY"
        assert donor["description"].startswith("HYPOTHESIZED -")
        assert "does not assign every substrate" in donor["description"]
        assert "hydrogen/formate" in donor["description"]
        (arrow,) = donor["downstream"]
        assert arrow["target"] == reduction["name"]
        assert arrow["description"].startswith("HYPOTHESIZED -")
        assert (
            "does not assert a dependency between the two bacterial donors" in arrow["description"]
        )
    assert reduction["scope"] == "PAIRWISE"
    assert reduction["source_taxon"]["term"] == doc["taxonomy"][0]["taxon_term"]["term"]
    assert (
        not {"target_taxon", "participating_taxa", "interaction_type", "downstream"}
        & reduction.keys()
    )
    assert "positive community-level observations" in reduction["description"]
    assert reduction["evidence"][-1]["evidence_source"] == "IN_VITRO"
    assert all(
        e["supports"] == "PARTIAL" for n in [first, second, reduction] for e in n["evidence"]
    )
    (gap,) = doc["discussions"]
    assert gap["discussion_id"] == "kg-dietsimp-proposed-diet-no-causal-edge"
    assert "Both existing arrows are retained as hypotheses" in gap["rationale"]


def test_batch28_accounts_for_every_node_arrow_history_and_source_limit():
    ledger, docs = records()
    rows = ledger["records"]
    assert ledger["independent_approval"] is False
    assert Counter(r["status"] for r in rows) == {"reviewed": 4}
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 2
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 2
    assert sum(len(r["renamed_nodes"]) for r in rows) == 6
    assert sum(len(r["history_files"]) for r in rows) == 3
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        arrows = [
            {"source": n["name"], **e}
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        ]
        assert arrows == row["edges_after"]
        renames = row["renamed_nodes"]
        removed = {(e["source"], e["target"]) for e in row["removed_edge_decisions"]}
        assert {(e["source"], e["target"]) for e in arrows} == {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
            if (e["source"], e["target"]) not in removed
        }
        assert all(
            a.split("#", 1)[1] in names
            for d in doc.get("discussions", [])
            for a in d.get("attaches_to", [])
            if a.startswith("ecological_interactions#")
        )
    assert ledger["open_nongraph_followups"] == [1371, 1372, 1373]
    assert len(ledger["reference_cache_original_hashes"]) == 5
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
