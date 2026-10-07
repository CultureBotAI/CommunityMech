"""Keep measured findings distinct from methods and unproven causal mediation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch87.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_prairie_retains_findings_and_two_qualified_directions():
    _, rows, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert len(nodes) == 4 and len(rows[0]["edges_after"]) == 2
    assert all("interaction_type" not in n for n in nodes)
    assert "genomic potential" in nodes[0]["description"]
    assert nodes[1]["description"].startswith("HYPOTHESIZED:")
    assert "false positives" in nodes[2]["description"]
    assert nodes[3]["description"].startswith("HYPOTHESIZED:")
    assert all(e["description"].startswith("HYPOTHESIZED:") for e in rows[0]["edges_after"])


def test_prairie_does_not_invent_crossfeeding_or_signed_viral_effect():
    _, _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert [len(n["participating_taxa"]) for n in nodes] == [1, 1, 3, 4]
    assert nodes[1]["participating_taxa"][0]["term"]["id"] == "NCBITaxon:2157"
    assert "no established net sign" in nodes[2]["downstream"][0]["description"]
    assert "interspecies producer-to-consumer transfer" in nodes[1]["description"]


def test_infant_methods_removed_but_observation_retained():
    _, rows, docs = records()
    (node,) = docs[1]["ecological_interactions"]
    assert "four-infant observational" in node["description"]
    assert "not directly measured hypoxia" in node["description"]
    assert "Twenty repeated samples" in node["description"]
    assert len(rows[1]["removed_node_decisions"]) == 2
    assert "downstream" not in node and "interaction_type" not in node
    assert node["participating_taxa"][0]["term"]["id"] == "NCBITaxon:561"


def test_infant_confounding_and_other_positive_observations_remain():
    _, _, docs = records()
    text = docs[1]["discussions"][-1]["rationale"]
    for value in [
        "lower NO-related ratios",
        "osmotic-ratio",
        "p>0.05",
        "Gestational age",
        "birth weight",
        "#1722",
    ]:
        assert value in text


def test_rice_preserves_two_host_endpoints_without_mutualism():
    _, _, docs = records()
    nodes = docs[2]["ecological_interactions"]
    assert len(nodes) == 2
    assert "reduced arsenic accumulation" in nodes[0]["description"]
    assert "PARTIAL:" in nodes[0]["description"]
    assert "improved photosynthesis" in nodes[1]["description"]
    for n in nodes:
        assert "interaction_type" not in n and "downstream" not in n
        assert [p["term"]["id"] for p in n["participating_taxa"]] == [
            "NCBITaxon:86664",
            "NCBITaxon:303",
            "NCBITaxon:4530",
        ]


def test_helper_positive_protection_survives_distinct_from_co2_mediation():
    _, rows, docs = records()
    protection, co2, growth = docs[3]["ecological_interactions"]
    assert protection["downstream"][0]["target"] == growth["name"]
    assert not protection["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert co2["downstream"][0]["target"] == protection["name"]
    assert co2["downstream"][0]["description"].startswith("PARTIAL:")
    assert "sixfold lower peroxide removal" in co2["description"]
    assert "post-transfer lag" in co2["description"]
    assert len(rows[3]["edges_after"]) == 2
    assert all("interaction_type" not in n for n in [protection, co2, growth])


def test_helper_access_limits_and_assay_distinctions_are_not_hidden():
    _, _, docs = records()
    text = docs[3]["discussions"][-1]["rationale"]
    assert "No full-methods" in text and "retrieval failures" in text
    assert "missing access does not prove experiments are absent" in text
    assert (
        "separate temperature and CO2 experiments"
        in docs[3]["ecological_interactions"][2]["description"]
    )


def test_all_original_nodes_edges_and_anchors_have_dispositions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 2
    assert sum(len(r["edges_before"]) for r in rows) == 4
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 4
    assert all(not r["removed_edge_decisions"] for r in rows)
    assert ledger["primary_graph_snippet_count"] == 17
    assert len(ledger["discussion_snippet_checks"]) == 8
    for row, doc in zip(rows, docs, strict=True):
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(e["target"] in names for e in row["edges_after"])
        assert all(
            a.split("#", 1)[1] in names for d in doc["discussions"] for a in d["attaches_to"]
        )


def test_history_no_spend_and_unfinished_lifecycle_are_explicit():
    ledger, rows, docs = records()
    assert not ledger["independent_approval"]
    assert ledger["issues"] == [1718, 1719, 1720, 1721]
    assert ledger["unresolved_non_graph_issues"] == [1722]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"] == []
    for row, doc in zip(rows, docs, strict=True):
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert row["status"] == "reviewed" and doc["curation_history"][-1]["llm_assisted"]


def test_reviewed_records_and_all_evidence_caches_are_hash_bound():
    ledger, rows, _ = records()
    assert ledger["cache_changes"] == []
    for row in rows:
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    for path, digest in ledger["primary_artifacts"].items():
        if path.startswith("references_cache/"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
