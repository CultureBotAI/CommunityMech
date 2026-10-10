"""Keep wild-type fusion evidence distinct from reporter and engineered assays."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml"
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-one-record-batch17.yaml"


def record():
    return yaml.safe_load(PATH.read_text())


def test_engineered_dna_is_not_a_wild_type_graph_endpoint():
    doc = record()
    nodes = doc["ecological_interactions"]
    assert len(nodes) == 8
    assert not any("genomic integration" in n["name"] for n in nodes)
    fusion = nodes[6]
    assert "Wild-type electron microscopy" in fusion["description"]
    assert "protein-dye exchange" in fusion["description"]
    assert "C. acetobutylicum-Halo reporter" in fusion["description"]
    assert "outside this wild-type graph" in fusion["description"]
    assert "interaction_type" not in fusion
    assert len(fusion["downstream"]) == 1
    assert fusion["downstream"][0]["target"] == nodes[7]["name"]
    assert fusion["downstream"][0]["description"].startswith("HYPOTHESIZED")


def test_supplementation_is_preserved_without_asserting_traced_cross_feeding():
    nodes = record()["ecological_interactions"]
    for node in nodes[1:3]:
        assert node["description"].startswith("PARTIAL")
        assert "supplementation" in node["description"]
        assert "monoculture" in node["description"]
        assert "HYPOTHESIZED" in node["description"]
        assert node["evidence"][0]["supports"] == "PARTIAL"
        assert any("two biological replicates" in e["explanation"] for e in node["evidence"])
    assert "ATP-mediated effect" in nodes[1]["description"]
    assert "not directly trace donor-derived carbon" in nodes[2]["description"]


def test_hydrogen_and_growth_nodes_name_the_measured_endpoints():
    gas, _, _, hydrogen, growth, competition, _, _ = record()["ecological_interactions"]
    assert gas["interaction_type"] == "CROSS_FEEDING"
    assert "different substrate and gas conditions" in gas["description"]
    assert gas["downstream"][0]["target"] == hydrogen["name"]
    assert gas["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert "early glucose-consumption rates" in hydrogen["description"]
    assert "not a direct hydrogenase assay" in hydrogen["description"]
    assert "not direct species-specific growth-rate measurements" in growth["description"]
    assert "does not isolate nutrient competition" in competition["description"]
    assert all("interaction_type" not in n for n in (hydrogen, growth, competition))


def test_product_emergence_is_condition_specific():
    products = record()["ecological_interactions"][-1]
    assert "isopropanol and 2,3-butanediol" in products["name"]
    assert "condition-specific emergence" in products["description"]
    assert "can in principle produce 2,3-butanediol alone" in products["description"]
    assert products["evidence"][1]["supports"] == "PARTIAL"
    assert {m["term"]["id"] for m in products["metabolites"]} == {
        "CHEBI:17824",
        "CHEBI:62064",
    }


def test_gap_anchors_resolve_after_all_renames_and_removal():
    doc = record()
    names = {n["name"] for n in doc["ecological_interactions"]}
    assert len(doc["discussions"]) == 2
    anchored = set()
    for discussion in doc["discussions"]:
        assert discussion["kind"] == "KNOWLEDGE_GAP"
        assert discussion["status"] == "OPEN"
        anchors = {a.split("#", 1)[1] for a in discussion["attaches_to"]}
        assert anchors <= names
        anchored.update(anchors)
    assert anchored == names


def test_batch17_ledger_preserves_removed_evidence_and_every_review_decision():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1316]
    assert ledger["open_nongraph_followups"] == [1317]
    row = ledger["records"][0]
    assert hashlib.sha256(PATH.read_bytes()).hexdigest() == row["record_sha256"]
    assert row["curation_events_added"] == 1
    assert len(row["history_files"]) == 1
    assert len(row["renamed_nodes"]) == 4
    assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
        n["name"] for n in record()["ecological_interactions"]
    )
    removed = row["removed_node_decisions"][0]
    assert removed["original_node"]["evidence"][0]["reference"] == "PMID:38214507"
    assert "plasmid-carrying" in removed["original_node"]["evidence"][0]["snippet"]
    assert len(row["edges_before"]) == 3
    assert len(row["edges_after"]) == 2
    assert len(row["removed_edge_decisions"]) == 1
    renames = row["renamed_nodes"]
    assert {(e["source"], e["target"]) for e in row["edges_after"]} == {
        (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
        for e in row["edges_before"]
        if e["target"] != removed["node"]
    }
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
