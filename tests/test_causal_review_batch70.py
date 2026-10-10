"""Keep positive outcomes distinct from cross-study and mediation inferences."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-four-records-batch70.yaml"
A = "Mercury_SFA_EFPC_Sediment_Community"
B = "Mesorhizobium_Synechococcus_B12_Synthetic_Consortium"
C = "Methane_MFC_Electrogenesis_Nitrogen_Fixation_Consortium"
D = "Methane_Oxidation_CrVI_Reduction_SynCom"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {stem: yaml.safe_load((ROOT / row["path"]).read_text()) for stem, row in rows.items()}
    return ledger, rows, docs


def edge_key(edge, renames):
    return (
        renames.get(edge["source"], edge["source"]),
        renames.get(edge["target"], edge["target"]),
    )


def test_efpc_potential_does_not_import_external_methanogen_phenotypes():
    _, rows, docs = records()
    exposure, methylation, resistance, selenium = docs[A]["ecological_interactions"]
    assert "Potential" in methylation["name"]
    assert "not measured hgcAB" in methylation["description"]
    assert {e["reference"] for e in methylation["evidence"]} == {"PMID:33927032"}
    assert methylation["evidence"][0]["supports"] == "PARTIAL"
    assert "eight of nine" in docs[A]["discussions"][-1]["rationale"]
    assert "M. methylutens did not" in docs[A]["discussions"][-1]["rationale"]
    assert len(exposure["downstream"]) == 1
    assert exposure["downstream"][0]["target"] == resistance["name"]
    assert len(rows[A]["removed_edge_decisions"]) == 1
    assert "27 of 28" in resistance["description"]
    assert "17 of 28" in selenium["description"]
    assert selenium["participating_taxa"][0]["preferred_term"] == "Eisenbacteria"


def test_syn7002_retains_biological_observations_without_workflow_arrows():
    _, rows, docs = records()
    salinity, sorting, provision, spatial, expression, rescue = docs[B]["ecological_interactions"]
    assert len(rows[B]["removed_edge_decisions"]) == 3
    assert "downstream" not in salinity and "downstream" not in sorting
    assert "PseTH extinction" in sorting["description"]
    assert "day-20 pelleted" in provision["description"]
    assert "not an extracellular assay" in provision["description"]
    assert "log2 fold changes" in expression["description"]
    assert "absolute cross-species" in expression["description"]
    assert "positive control" in rescue["description"]
    assert "promoted" in rescue["description"]
    assert "biological_processes" not in rescue
    for node in [provision, spatial, expression]:
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert provision["interaction_type"] == "CROSS_FEEDING"
    assert all(
        "interaction_type" not in n for n in [salinity, sorting, spatial, expression, rescue]
    )


def test_mfc_keeps_isotope_and_electrochemical_evidence_at_correct_scope():
    _, _, docs = records()
    overview, eet, diazotrophs, nitrogen, current = docs[C]["ecological_interactions"]
    for phrase in ["15N2", "13.55%", "7.15%", "0.22 +/- 0.01 mg/L", "30 days"]:
        assert phrase in nitrogen["description"]
    for phrase in ["1.17 +/- 0.18 mA", "78.1%", "inhibitor", "Raman", "15N"]:
        assert phrase in current["description"]
    assert "not a complete roster" in overview["description"]
    assert len(eet["participating_taxa"]) == 2
    assert len(diazotrophs["participating_taxa"]) == 3
    assert len(nitrogen["participating_taxa"]) == len(current["participating_taxa"]) == 6
    assert eet["downstream"][0]["description"].startswith("PARTIAL -")
    assert diazotrophs["downstream"][0]["description"].startswith("PARTIAL -")
    assert "downstream" not in nitrogen


def test_chromium_keeps_positive_perturbation_without_resolving_eet_routes():
    _, _, docs = records()
    methane, transfer, removal = docs[D]["ecological_interactions"]
    assert "6.30%" in methane["description"]
    assert "oxygen-independent" in methane["description"]
    assert methane["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert "alternative route" in transfer["description"]
    assert "20.63 mg/L/d" in removal["description"]
    assert "Inhibiting methane oxidation reduced" in removal["description"]
    assert "off-target" in removal["description"]
    assert all(p["term"]["id"] != "GO:0009372" for p in removal["biological_processes"])
    assert len(removal["participating_taxa"]) == 3
    assert all(
        n["downstream"][0]["description"].startswith("PARTIAL -") for n in [methane, transfer]
    )
    assert docs[D]["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"


def test_batch70_canonical_ids_and_non_graph_aliases_are_preserved():
    _, _, docs = records()
    for doc in docs.values():
        canonical = {
            (t["taxon_term"]["preferred_term"], t["taxon_term"]["term"]["id"])
            for t in doc["taxonomy"]
        }
        for n in doc["ecological_interactions"]:
            for t in n.get("participating_taxa", []):
                assert (t["preferred_term"], t["term"]["id"]) in canonical
    doc = docs[D]
    assert doc["engineering_design"]["evidence"][0] == doc["taxonomy"][0]["evidence"][0]
    assert (
        doc["environmental_factors"][0]["evidence"][0] == doc["engineering_design"]["evidence"][0]
    )
    assert all(
        "interaction_type" not in n
        for stem in [A, C, D]
        for n in docs[stem]["ecological_interactions"]
    )


def test_batch70_every_original_node_and_arrow_has_a_decision():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 18
    assert sum(len(r["retained_edge_decisions"]) for r in rows.values()) == 8
    assert sum(len(r["removed_edge_decisions"]) for r in rows.values()) == 4
    for stem, row in rows.items():
        assert row["removed_node_decisions"] == []
        names = {n["name"] for n in docs[stem]["ecological_interactions"]}
        assert {n["node"] for n in row["node_decisions"]} == names
        renames = row["renamed_nodes"]
        original = {edge_key(e, renames) for e in row["edges_before"]}
        retained = {(e["source"], e["target"]) for e in row["edges_after"]}
        removed = {edge_key(e, renames) for e in row["removed_edge_decisions"]}
        assert original == retained | removed and not retained & removed
        for d in docs[stem]["discussions"]:
            assert {
                a.split("#", 1)[1]
                for a in d["attaches_to"]
                if a.startswith("ecological_interactions#")
            } <= names


def test_batch70_reviews_are_hash_bound_with_honest_limits():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1596, 1597, 1598, 1599]
    assert ledger["unresolved_non_graph_issues"] == [1600]
    assert ledger["primary_graph_snippet_count"] == 23
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for stem, row in rows.items():
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["status"] == "reviewed" and len(row["history_files"]) == 1
        assert docs[stem]["curation_history"][-1]["llm_assisted"] is True
    for stem in [C, D]:
        assert "abstract only" in next(iter(rows[stem]["source_review"].values()))["scope"]
