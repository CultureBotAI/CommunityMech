"""Keep positive outcomes, source boundaries, and unchanged reviews explicit."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch73.yaml"
A = "Microcoleus_Massilia_Cyanosphere_Urea_Mutualism"
B = "Microhabitat_Mineral_Fungal_Bacterial_SOM_SynCom"
C = "Miscanthus_REE_Tailings_Nitrogen_SynCom10"
D = "Mixed_Gallium_LED_Recovery_Consortium"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {s: yaml.safe_load((ROOT / r["path"]).read_text()) for s, r in rows.items()}
    return ledger, rows, docs


def test_cyanosphere_preserves_positive_experiments_and_corrects_the_responder():
    _, _, docs = records()
    growth, urea, signal = docs[A]["ecological_interactions"]
    assert growth["interaction_type"] == "MUTUALISM"
    assert urea["interaction_type"] == "CROSS_FEEDING"
    assert "increases extracellular urea release" in urea["description"]
    assert "5 micromolar, but not 2 micromolar" in urea["description"]
    assert "total coculture biomass" in urea["description"]
    assert all(e["supports"] == "PARTIAL" for e in urea["evidence"])
    assert "did not show true chemotaxis" in signal["description"]
    assert "high GABA can destabilize" in signal["description"]
    assert "Natural-bundle assays" in signal["description"]
    assert "GO:0006935" not in {p["term"]["id"] for p in signal["biological_processes"]}
    for node in [urea, signal]:
        assert node["downstream"][0]["description"].startswith("PARTIAL -")
        assert node["downstream"][0]["target"] == growth["name"]
    assert "responding motile organism is Microcoleus" in signal["downstream"][0]["description"]


def test_mineral_litter_is_reviewed_without_rewriting_an_already_bounded_graph():
    _, rows, docs = records()
    row, doc = rows[B], docs[B]
    assert row["outcome"] == "unchanged" and row["status"] == "reviewed"
    assert row["allowed_changed_fields"] == row["history_files"] == []
    assert row["curation_events_added"] == 0
    assert row["record_sha256"] == row["original_sha256"]
    assert len(doc["ecological_interactions"]) == 1 and row["edges_after"] == []
    assert len(doc["ecological_interactions"][0]["participating_taxa"]) == 4
    assert len(doc["discussions"]) == 2
    assert "abiotic CO2" in doc["discussions"][0]["rationale"]
    assert "not directly quantified" in doc["discussions"][1]["rationale"]
    assert doc["curation_history"][-1]["action"] == "ADDRESS_ADVERSARIAL_REVIEW"


def test_miscanthus_preserves_comparators_without_asserting_selective_mediation():
    _, _, docs = records()
    capability, removal, biomass = docs[C]["ecological_interactions"]
    for node in [capability, removal, biomass]:
        assert len(node["participating_taxa"]) == 5
        assert "interaction_type" not in node
    assert capability["downstream"][0]["description"].startswith("PARTIAL -")
    assert removal["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    for value in ["24.8%", "32.6%", "25.5%"]:
        assert value in removal["description"]
    assert "dead SynCom" in biomass["description"]
    assert "39.8% and 49.7%" in biomass["description"]
    assert "seven" in biomass["description"].lower()
    assert removal["evidence"][0]["snippet"].startswith("this SynCom")
    assert docs[C]["taxonomy"][-1]["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"


def test_gallium_separates_exact_system_roles_and_preserves_the_recovery_effect():
    _, rows, docs = records()
    nodes = docs[D]["ecological_interactions"]
    assert rows[D]["status"] == "needs_research"
    assert all("interaction_type" not in n for n in nodes)
    assert all(
        e["reference"] == "doi:10.1016/j.jece.2025.120403" for n in nodes for e in n["evidence"]
    )
    assert all(e["supports"] == "PARTIAL" for n in nodes[:3] for e in n["evidence"])
    assert nodes[-1]["evidence"][0]["supports"] == "SUPPORT"
    assert nodes[2]["downstream"][0]["target"] == nodes[3]["name"]
    assert not nodes[2]["downstream"][0]["description"].startswith("HYPOTHESIZED")
    for value in ["99.5%", "45.59%", "21.43%"]:
        assert value in nodes[-1]["description"]
    ions = {m["term"]["id"] for n in nodes for m in n.get("metabolites", [])}
    assert "CHEBI:84043" in ions and "CHEBI:49631" not in ions
    assert "selected" in nodes[0]["description"]


def test_batch73_accounts_for_all_original_structure_and_source_limits():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 11
    assert sum(len(r["edges_before"]) for r in rows.values()) == 7
    assert sum(len(r["edges_after"]) for r in rows.values()) == 7
    assert ledger["cache_matched_graph_snippet_count"] == 17
    assert ledger["primary_graph_snippet_count"] == 14
    assert sum(not c["independent_primary_match"] for c in ledger["snippet_checks"]) == 3
    for stem, row in rows.items():
        assert not row["removed_node_decisions"] and not row["removed_edge_decisions"]
        renames = row["renamed_nodes"]
        assert {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        } == {(e["source"], e["target"]) for e in row["edges_after"]}
        names = {n["name"] for n in docs[stem]["ecological_interactions"]}
        assert {n["node"] for n in row["node_decisions"]} == names
        assert all(
            a.split("#", 1)[1] in names
            for d in docs[stem]["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_batch73_canonical_participants_and_exact_changed_record_histories():
    _, rows, docs = records()
    for stem, doc in docs.items():
        canonical = {
            (t["taxon_term"]["preferred_term"], t["taxon_term"]["term"]["id"])
            for t in doc["taxonomy"]
        }
        for node in doc["ecological_interactions"]:
            assert all(
                (p["preferred_term"], p["term"]["id"]) in canonical
                for p in node.get("participating_taxa", [])
            )
        row = rows[stem]
        assert row["curation_events_added"] == len(row["history_files"]) == (0 if stem == B else 1)
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        if stem != B:
            assert doc["curation_history"][-1]["llm_assisted"] is True
            assert (ROOT / row["history_files"][0]).is_file()


def test_batch73_does_not_promote_dry_run_or_self_review_to_approval():
    ledger, _, _ = records()
    assert ledger["issues"] == [1614, 1615, 1616]
    assert ledger["unresolved_research_issues"] == [1617]
    assert ledger["unresolved_non_graph_issues"] == [1618]
    assert ledger["edison"]["dry_run_complete"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert "pending" in ledger["edison"]["authorization"]
    assert not ledger["independent_approval"]
