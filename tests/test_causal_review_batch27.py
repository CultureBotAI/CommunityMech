"""Bound CPR lipid inference and distinguish completed from unresolved reviews."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch27.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in ledger["records"]]


def test_crystal_geyser_participants_are_scoped_without_resolved_donor_pairs():
    _, docs = records()
    carbon, acquisition, adaptation = docs[0]["ecological_interactions"]
    for node, ids in zip(
        [carbon, acquisition, adaptation],
        [["NCBITaxon:131567"], ["NCBITaxon:1783273", "NCBITaxon:131567"], ["NCBITaxon:1783273"]],
        strict=True,
    ):
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert [p["term"]["id"] for p in node["participating_taxa"]] == ids
        assert not {"source_taxon", "target_taxon"} & node.keys()
    assert "interaction_type" not in carbon and "interaction_type" not in adaptation
    assert acquisition["interaction_type"] == "CROSS_FEEDING"


def test_crystal_geyser_retains_positive_measurements_and_alternative_explanations():
    _, docs = records()
    carbon, acquisition, adaptation = docs[0]["ecological_interactions"]
    assert "predominantly autotrophic origin" in carbon["description"]
    assert "fractionation assumptions" in carbon["description"]
    assert "allow heterotrophic reuse" in carbon["description"]
    for phrase in [
        "HYPOTHESIZED",
        "Scavenging degraded biomass and direct host-derived acquisition",
        "unknown ACP-independent biosynthesis cannot be excluded",
        "not proof of archaeal-to-CPR donation",
        "Product-removal syntrophy was not demonstrated",
    ]:
        assert phrase in acquisition["description"]
    assert all(e["supports"] == "PARTIAL" for e in acquisition["evidence"])
    assert acquisition["evidence"][-1]["evidence_source"] == "OTHER"
    assert "FTIR" in adaptation["description"]
    assert "not purified CPR isolates" in adaptation["description"]
    assert "Sulfurimonas" in adaptation["description"]
    assert "not a tested membrane-mechanical or fitness effect" in adaptation["description"]


def test_crystal_geyser_arrows_remain_explicitly_hypothetical():
    _, docs = records()
    carbon, acquisition, adaptation = docs[0]["ecological_interactions"]
    assert carbon["downstream"][0]["target"] == acquisition["name"]
    assert acquisition["downstream"][0]["target"] == adaptation["name"]
    arrows = [e for n in [carbon, acquisition, adaptation] for e in n.get("downstream", [])]
    assert len(arrows) == 2
    assert all(e["description"].startswith("HYPOTHESIZED -") for e in arrows)
    assert "do not trace transfer" in arrows[0]["description"]
    assert "do not demonstrate that acquisition causes" in arrows[1]["description"]


def test_nitrifier_retains_bounded_aggregate_conversion_without_new_arrows():
    ledger, docs = records()
    row, doc = ledger["records"][1], docs[1]
    assert row["status"] == "reviewed" and row["outcome"] == "unchanged"
    assert row["original_sha256"] == row["record_sha256"]
    (node,) = doc["ecological_interactions"]
    assert "selected organic" in node["description"]
    assert "no residual nitrite" in node["description"]
    assert len(node["participating_taxa"]) == 3 and not node.get("downstream")
    assert doc["discussions"][0]["status"] == "OPEN"
    assert row["history_files"] == [] and row["curation_events_added"] == 0


def test_dcpp_access_gap_is_not_certified_as_completed_review():
    ledger, docs = records()
    row, doc = ledger["records"][2], docs[2]
    assert row["status"] == "needs_research" and row["outcome"] == "unchanged"
    assert row["original_sha256"] == row["record_sha256"]
    assert row["history_files"] == [] and row["curation_events_added"] == 0
    assert row["allowed_changed_fields"] == [] and row["issues"] == [596]
    assert len(doc["ecological_interactions"]) == 3
    assert not any(n.get("downstream") for n in doc["ecological_interactions"])
    source = row["source_review"]["PMID:42613016"]
    assert "HTTP 403" in source["reviewed_scope"]
    assert "not proof that all 19 biological claims are false" in source["snippet_status"]
    assert all(d["rationale"].startswith("Unresolved:") for d in row["node_decisions"])


def test_batch27_accounts_for_every_node_arrow_history_and_source_limit():
    ledger, docs = records()
    rows = ledger["records"]
    assert ledger["independent_approval"] is False
    assert Counter(r["status"] for r in rows) == {"reviewed": 2, "needs_research": 1}
    assert sum(len(r["node_decisions"]) for r in rows) == 7
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 2
    assert sum(len(r["renamed_nodes"]) for r in rows) == 3
    assert not any(r["removed_edge_decisions"] for r in rows)
    assert sum(len(r["history_files"]) for r in rows) == 1
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        arrows = [
            {"source": n["name"], **edge}
            for n in doc["ecological_interactions"]
            for edge in n.get("downstream", [])
        ]
        assert arrows == row["edges_after"]
        rename = row["renamed_nodes"]
        assert {(e["source"], e["target"]) for e in arrows} == {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        assert all(
            a.split("#", 1)[1] in names
            for d in doc.get("discussions", [])
            for a in d.get("attaches_to", [])
            if a.startswith("ecological_interactions#")
        )
    source = rows[0]["source_review"]["PMID:32203118"]
    assert "Complete independently retrieved main body" in source["reviewed_scope"]
    assert "No figure images or supplementary files inspected" in source["reviewed_scope"]
    assert len(ledger["reference_cache_original_hashes"]) == 4
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
