"""Preserve measured coculture outcomes without overstating causal mediation."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-three-records-batch18.yaml"


def load(stem):
    return yaml.safe_load((ROOT / "kb/communities" / (stem + ".yaml")).read_text())


def test_ethanol_feedback_is_not_reverse_donation_or_exclusive_mechanism():
    doc = load("Clostridium_Autoethanogenum_Kluyveri_Syngas_Coculture")
    gas, chain, pull = doc["ecological_interactions"]
    assert "reverse-calculated" in gas["description"]
    assert gas["interaction_type"] == chain["interaction_type"] == "CROSS_FEEDING"
    assert chain["source_taxon"]["term"]["id"] == "NCBITaxon:1534"
    assert chain["target_taxon"]["term"]["id"] == "NCBITaxon:84023"
    assert "acid-supplemented C. autoethanogenum pure cultures" in chain["description"]
    assert gas["downstream"][0]["target"] == chain["name"]
    assert "interaction_type" not in pull
    assert pull["description"].startswith("HYPOTHESIZED")
    assert "post-translational regulation" in pull["description"]
    assert "not ethanol donation" in pull["description"]
    assert pull["downstream"][0]["target"] == gas["name"]
    assert pull["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert all(e["supports"] == "PARTIAL" for e in pull["evidence"])


def test_medium_context_does_not_become_a_causal_maintenance_edge():
    doc = load("Clostridium_Caldicellulosiruptor_Minimal_Medium_Coculture")
    medium, maintenance, capacity = doc["ecological_interactions"]
    assert all("interaction_type" not in n for n in (medium, maintenance, capacity))
    assert all("downstream" not in n for n in (medium, maintenance, capacity))
    assert "biological_processes" not in medium
    assert "biological_processes" not in maintenance
    assert maintenance["name"].startswith("Observed Co-Maintenance")
    assert "duration" in maintenance["description"]
    assert "experimental transcriptomics and proteomics" in capacity["description"]
    assert capacity["evidence"][1]["evidence_source"] == "IN_VITRO"
    assert "member assays do not demonstrate niche partitioning" in capacity["description"]
    assert len(doc["curation_history"]) == 2
    assert "capacity to stable" in doc["curation_history"][0]["changes"]
    assert "full body was not obtained" in doc["discussions"][0]["rationale"]


def test_reactor_staging_preserves_covariates_and_monoculture_capacity():
    doc = load("Clostridium_Carboxidivorans_Kluyveri_CO_Chain_Elongation_Coculture")
    supply, alcohol, stage = doc["ecological_interactions"]
    assert supply["interaction_type"] == alcohol["interaction_type"] == "CROSS_FEEDING"
    assert "144-hour batch" in alcohol["description"]
    assert "condition-specific" in alcohol["description"]
    assert "C. carboxidivorans alone" in alcohol["description"]
    assert alcohol["metabolites"][1]["term"] == {
        "id": "CHEBI:17120",
        "label": "hexanoate",
    }
    assert "interaction_type" not in stage
    assert "pH 6.0" in stage["description"] and "pH 5.0" in stage["description"]
    assert "dilution rate also differed" in stage["description"]
    assert "CO-only effect" in stage["description"]
    assert "de novo alcohol synthesis" in stage["downstream"][0]["description"]
    assert supply["downstream"][0]["target"] == stage["downstream"][0]["target"]
    assert "86%" in doc["discussions"][0]["rationale"]
    assert "complete inhibition at 800 mbar" in doc["discussions"][0]["rationale"]


def test_batch18_ledger_accounts_for_every_node_and_arrow():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1319, 1320, 1321]
    assert ledger["open_nongraph_followups"] == [1322]
    assert len(ledger["records"]) == 3
    removed_count = 0
    for row in ledger["records"]:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert len(names) == 3
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        renames = row["renamed_nodes"]
        before = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        after = {(e["source"], e["target"]) for e in row["edges_after"]}
        removed = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        assert before == after | removed
        assert not after & removed
        assert after == {(e["source"], e["target"]) for e in row["retained_edge_decisions"]}
        assert after == {
            (n["name"], e["target"])
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        }
        removed_count += len(removed)
        assert set(row["allowed_changed_fields"]) == {
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
    assert removed_count == 1
    assert len(ledger["reference_cache_original_hashes"]) == 7
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
