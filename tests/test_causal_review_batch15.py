"""Keep measured physiology and concentrations distinct from proposed mechanisms."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-three-records-batch15.yaml"


def load(stem):
    return yaml.safe_load((ROOT / "kb/communities" / (stem + ".yaml")).read_text())


def test_chlorochromatium_retains_physiology_without_asserting_transfer():
    doc = load("Chlorochromatium_Aggregatum_Phototrophic_Consortium")
    exchange, navigation, quinone = doc["ecological_interactions"]
    assert exchange["description"].startswith("HYPOTHESIZED")
    assert "external 2-oxoglutarate" in exchange["description"]
    assert "metabolites" not in exchange
    assert "interaction_type" not in navigation
    assert "recombinant" in navigation["description"]
    assert "necessity" in navigation["description"]
    assert {e["evidence_source"] for e in navigation["evidence"]} == {
        "COMPUTATIONAL",
        "IN_VITRO",
    }
    assert any(e["reference"] == "PMID:9446684" for e in navigation["evidence"])
    assert "enriched fractions, not purified" in quinone["description"]
    assert "biological_processes" not in quinone
    assert all(e["supports"] == "PARTIAL" for e in quinone["evidence"])
    assert all(
        e["description"].startswith("HYPOTHESIZED")
        for n in doc["ecological_interactions"]
        for e in n.get("downstream", [])
    )


def test_synlav_separates_soil_and_plant_endpoints_and_bounds_mediation():
    doc = load("Choysum_SynLAV_DEHP_Rhizobacterial_SynCom")
    soil, plant = doc["ecological_interactions"]
    assert "rhizosphere-soil DEHP residues" in soil["description"]
    assert "not measured mineralization" in soil["description"]
    assert "biological_processes" not in soil
    assert all(e["supports"] == "PARTIAL" for e in soil["evidence"][:-1])
    assert soil["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert "mg/kg, not total accumulated plant mass" in plant["description"]
    assert all("participating_taxa" not in n for n in (soil, plant))
    endpoint = doc["discussions"][0]
    assert "10-day" in endpoint["prompt"] and "two weeks" in endpoint["prompt"]
    assert "unique viable-strain detection" in endpoint["rationale"]
    assert any(d["discussion_id"] == "synlav_dehp_mediation" for d in doc["discussions"])


def test_chromium_chemistry_does_not_promote_vfa_class_to_acetate():
    doc = load("Chromium_Sulfur_Reduction_Enrichment")
    donor, reduction, deposition = doc["ecological_interactions"]
    assert donor["metabolites"][0]["term"] == {
        "id": "CHEBI:33403",
        "label": "elemental sulfur",
    }
    assert "separate" in donor["description"]
    assert donor["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert "early abiotic Fe-associated" in reduction["description"]
    assert "XPS" in reduction["downstream"][0]["description"]
    assert "interaction_type" not in deposition
    assert "not cross-feeding" in deposition["description"]
    for node in (donor, reduction, deposition):
        assert "biological_processes" not in node
        assert not {m["term"]["id"] for m in node["metabolites"]} & {
            "CHEBI:30089",
            "CHEBI:49544",
            "CHEBI:26833",
        }


def test_batch15_ledger_covers_every_node_and_retained_edge():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1308, 1309, 1310]
    assert ledger["open_nongraph_followups"] == [1311]
    assert len(ledger["records"]) == 3
    for row in ledger["records"]:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        before = {(e["source"], e["target"]) for e in row["edges_before"]}
        after = {(e["source"], e["target"]) for e in row["edges_after"]}
        assert before == after
        assert after == {(e["source"], e["target"]) for e in row["retained_edge_decisions"]}
        assert row["removed_edge_decisions"] == []
        assert set(row["allowed_changed_fields"]) <= {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        assert row["curation_events_added"] == 1
        assert len(row["history_files"]) == 1
        assert all((ROOT / p).is_file() for p in row["history_files"])
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d.get("attaches_to", [])
            if a.startswith("ecological_interactions#")
        )
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
