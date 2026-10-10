"""Retain positive assay results without invented mechanisms or panel ecology."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-four-records-batch68.yaml"
A = "Maize_SC2_RootRot_Biocontrol_SynCom"
B = "Mangrove_Benzene_MFC_Bioanode_Consortium"
C = "Mars_Meteorite_EETA79001_Growth_Panel"
D = "Mars_Regolith_Cyanobacteria_Biofertilizer_Panel"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / r["path"]).read_text()) for name, r in rows.items()}
    return ledger, rows, docs


def test_sc2_keeps_external_participants_and_positive_plant_assays():
    _, _, docs = records()
    inhibition, growth, _ = docs[A]["ecological_interactions"]
    assert "seven days" in inhibition["description"]
    assert "14 days" in growth["description"]
    assert inhibition["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    for node, external in [(inhibition, "NCBITaxon:4799"), (growth, "NCBITaxon:4577")]:
        assert external in {t["term"]["id"] for t in node["participating_taxa"]}
        assert external not in {t["taxon_term"]["term"]["id"] for t in docs[A]["taxonomy"]}
    assert "biological_processes" not in inhibition
    assert growth["biological_processes"][0]["term"]["id"] == "GO:0040007"


def test_sc2_biochemical_assays_are_not_molecular_or_host_transfer_proof():
    _, _, docs = records()
    node = docs[A]["ecological_interactions"][2]
    for phrase in ["Salkowski", "45 ug/mL", "65 ug/mL", "0.50 cm", "p=0.015", "pure-IAA"]:
        assert phrase in node["description"]
    assert "biological_processes" not in node
    assert len(node["participating_taxa"]) == 3
    assert all("notes" in m for m in node["metabolites"])
    old_gap = docs[A]["discussions"][0]
    assert "ecological_interactions#SC2 Salkowski and CAS assay outputs" in old_gap["attaches_to"]


def test_mfc_partial_roster_and_composition_mediation_remain_qualified():
    _, _, docs = records()
    shift, output = docs[B]["ecological_interactions"]
    assert "relative 16S" in shift["description"]
    assert "partial roster" in output["description"]
    assert len(shift["participating_taxa"]) == len(output["participating_taxa"]) == 4
    assert shift["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert "biological_processes" not in shift
    assert "PRIMARY_DEGRADER" not in docs[B]["taxonomy"][0].get("functional_role", [])


def test_mfc_retains_positive_removal_and_correct_voltage_cycle():
    _, _, docs = records()
    text = docs[B]["ecological_interactions"][1]["description"]
    for phrase in ["98.7", "96 h", "250 mg/L", "330 mg/L", "899.9", "238.8", "390.1"]:
        assert phrase in text
    assert "not a 100-fold acetate" in text
    assert "abiotic control" in text and "transient acetate/butyrate" in text
    assert "DET versus mediated transfer" in text


def test_meteorite_keeps_positive_persistence_and_control_exceptions():
    _, rows, docs = records()
    resource, hydration, persistence = docs[C]["ecological_interactions"]
    assert resource["downstream"][0]["description"].startswith("PARTIAL -")
    assert "earlier leachate" in resource["evidence"][1]["explanation"]
    assert "downstream" not in hydration
    for phrase in ["Chr20", "1:5", "14-17 days", "water alone", "MPN versus CFU", "extinction"]:
        assert phrase in persistence["description"]
    assert len(rows[C]["removed_edge_decisions"]) == 1
    assert all(
        "separately, not as a coculture" in n["description"]
        for n in [resource, hydration, persistence]
    )


def test_regolith_separates_growth_from_mechanism_and_material_benefit():
    _, rows, docs = records()
    resource, growth, fertilizer = docs[D]["ecological_interactions"]
    for phrase in ["5 mL", "75 mL", "Phosphorus was not detected", "Element totals"]:
        assert phrase in resource["description"]
    for phrase in [
        "OD440",
        "day 15",
        "clumping",
        "not measured oxygen",
        "not directly measured N2",
    ]:
        assert phrase in growth["description"]
    assert {p["term"]["id"] for p in growth["biological_processes"]} == {"GO:0015979", "GO:0040007"}
    assert "downstream" not in growth
    for phrase in [
        "Chlorella filtrate",
        "frond yields remained lower",
        "not live commensalism",
        "lowest Lemna yield",
    ]:
        assert phrase in fertilizer["description"]
    assert len(rows[D]["removed_edge_decisions"]) == 1


def test_batch68_caches_anchors_and_unresolved_metadata_are_explicit():
    ledger, rows, docs = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    raw = (ROOT / rows[B]["path"]).read_text()
    assert "&benzene\n" in raw and "&benzene_term\n" in raw
    assert "*benzene" in raw and "*benzene_term" in raw
    assert ledger["unresolved_non_graph_issues"] == [1586, 573]
    for name in [C, D]:
        assert "#573" in docs[name]["discussions"][-1]["rationale"]
    for doc in docs.values():
        assert all("interaction_type" not in n for n in doc["ecological_interactions"])
        assert "#1586" in doc["discussions"][-1]["rationale"]


def test_batch68_complete_node_arrow_accounting_and_append_only_history():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1582, 1583, 1584, 1585]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["primary_graph_snippet_count"] == 17
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 11
    assert sum(len(r["retained_edge_decisions"]) for r in rows.values()) == 4
    assert sum(len(r["removed_edge_decisions"]) for r in rows.values()) == 2
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1 and row["status"] == "reviewed"
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {d["node"] for d in row["node_decisions"]} == names
        renames = row["renamed_nodes"]

        def mapped(edge, renames=renames):
            return (
                renames.get(edge["source"], edge["source"]),
                renames.get(edge["target"], edge["target"]),
            )

        before = {mapped(e) for e in row["edges_before"]}
        kept = {(e["source"], e["target"]) for e in row["retained_edge_decisions"]}
        removed = {mapped(e) for e in row["removed_edge_decisions"]}
        assert not kept & removed and kept | removed == before
        for discussion in doc["discussions"]:
            assert {
                a.split("#", 1)[1]
                for a in discussion["attaches_to"]
                if a.startswith("ecological_interactions#")
            } <= names
