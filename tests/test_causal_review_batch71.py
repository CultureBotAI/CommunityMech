"""Preserve positive methane-coculture results without cross-system causality."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch71.yaml"
A = "Methylacidiphilum_Galdieria_Thermoacidophilic_Coculture"
B = "Methylocaldum_Cupriavidus_Methane_Acetate_Crossfeeding_Coculture"
C = "Methylocaldum_Methyloceanibacter_Methane_Crossfeeding_Coculture"
D = "Methylocystis_Rhodococcus_Methane_VFA_PHBV_Coculture"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {s: yaml.safe_load((ROOT / r["path"]).read_text()) for s, r in rows.items()}
    return ledger, rows, docs


def test_galdieria_preserves_oxygen_interventions_and_system_carbon_endpoint():
    _, _, docs = records()
    oxygen, competition, carbon = docs[A]["ecological_interactions"]
    assert "interaction_type" not in oxygen
    assert competition["interaction_type"] == "COMPETITION"
    for phrase in ["66-100%", "44-62%", "without oxygen addition", "proposed molecular"]:
        assert phrase in competition["description"]
    assert "No O2 was added at any point." in competition["evidence"][2]["snippet"]
    assert carbon["scope"] == "COMMUNITY_LEVEL"
    assert len(carbon["participating_taxa"]) == 2
    assert "source_taxon" not in carbon and "target_taxon" not in carbon
    assert "17-28%" in carbon["description"]
    assert "gas concentrations" in carbon["description"]
    assert "0.124 +/- 0.001 mmol/L/h" in carbon["description"]
    for n in [oxygen, competition]:
        assert n["downstream"][0]["target"] == carbon["name"]
        assert not n["downstream"][0]["description"].startswith("HYPOTHESIZED")


def test_cupriavidus_does_not_inherit_gela4_oxygen_or_acetate_findings():
    _, rows, docs = records()
    transfer, growth = docs[B]["ecological_interactions"]
    assert transfer["description"].startswith("PARTIAL -")
    assert "separate Gela4 system" in transfer["description"]
    assert transfer["evidence"][0]["supports"] == "PARTIAL"
    assert transfer["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert transfer["downstream"][0]["target"] == growth["name"]
    assert "grew when cocultured" in growth["description"]
    assert "metabolites" not in growth and "biological_processes" not in growth
    assert len(rows[B]["removed_node_decisions"]) == 1
    assert len(rows[B]["removed_edge_decisions"]) == 1
    assert "3.5-6% and 20-31%" in docs[B]["discussions"][-1]["rationale"]
    assert "full Methods and controls were unavailable" in docs[B]["discussions"][-1]["rationale"]


def test_gela4_retains_growth_and_reference_expression_without_excluding_flux():
    _, _, docs = records()
    transfer, growth, response = docs[C]["ecological_interactions"]
    assert "0.02/h versus 0.03/h" in growth["description"]
    assert "high-turnover" in growth["description"]
    for phrase in ["3.57", "15.6", "12.4", "310 nM", "early-phase difference was not significant"]:
        assert phrase in response["description"]
    assert transfer["downstream"][0]["target"] == response["name"]
    assert transfer["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert transfer["downstream"][1]["description"].startswith("PARTIAL -")
    assert "partner presence and supplied carbon source" in transfer["downstream"][0]["description"]


def test_phbv_retains_two_outcomes_not_workflow_or_mutualism():
    _, rows, docs = records()
    valerate, mixture = docs[D]["ecological_interactions"]
    assert len(rows[D]["removed_node_decisions"]) == 3
    assert len(rows[D]["removed_edge_decisions"]) == 4
    assert "35.9 +/- 8.6%" in valerate["description"]
    assert "68 +/- 7%" in valerate["description"]
    assert "PHV without PHB" in valerate["description"]
    for phrase in [
        "73.7 +/- 2.5%",
        "49.6 +/- 13%",
        "94:6",
        "oxygen supply also differs",
        "not actual waste",
    ]:
        assert phrase in mixture["description"]
    for n in [valerate, mixture]:
        assert "downstream" not in n and "interaction_type" not in n
        assert n["scope"] == "COMMUNITY_LEVEL" and len(n["participating_taxa"]) == 2
        assert all(m["term"]["id"] != "CHEBI:53389" for m in n["metabolites"])
        assert all("Externally supplied" in m["notes"] for m in n["metabolites"])


def test_batch71_accounts_for_every_original_node_and_arrow_without_extensions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 10
    assert sum(len(r["removed_node_decisions"]) for r in rows.values()) == 4
    assert sum(len(r["edges_before"]) for r in rows.values()) == 10
    assert sum(len(r["edges_after"]) for r in rows.values()) == 5
    assert sum(len(r["removed_edge_decisions"]) for r in rows.values()) == 5
    for stem, r in rows.items():
        renames = r["renamed_nodes"]
        before = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in r["edges_before"]
        }
        after = {(e["source"], e["target"]) for e in r["edges_after"]}
        removed = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in r["removed_edge_decisions"]
        }
        assert after.isdisjoint(removed) and before == after | removed
        names = {n["name"] for n in docs[stem]["ecological_interactions"]}
        assert {n["node"] for n in r["node_decisions"]} == names
        assert all(
            e["target"] in names
            for n in docs[stem]["ecological_interactions"]
            for e in n.get("downstream", [])
        )
        assert all(
            a.split("#", 1)[1] in names
            for d in docs[stem]["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0


def test_batch71_participants_are_canonical_and_histories_are_explicit():
    _, rows, docs = records()
    for stem, doc in docs.items():
        canonical = {
            (t["taxon_term"]["preferred_term"], t["taxon_term"]["term"]["id"])
            for t in doc["taxonomy"]
        }
        for n in doc["ecological_interactions"]:
            for t in n.get("participating_taxa", []):
                assert (t["preferred_term"], t["term"]["id"]) in canonical
        row = rows[stem]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
    assert docs[D]["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] == "AMBIGUOUS"


def test_batch71_review_is_bounded_and_followup_remains_open():
    ledger, _, _ = records()
    assert not ledger["independent_approval"]
    assert ledger["issues"] == [1602, 1603, 1604, 1605]
    assert ledger["unresolved_non_graph_issues"] == [1606]
    assert ledger["primary_graph_snippet_count"] == 20
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"]
    assert "abstract-only" in " ".join(ledger["limitations"])
    assert "Formate primary text was fetched but not independently reread" in " ".join(
        ledger["limitations"]
    )
