"""Preserve observed carbon flow and syntrophy while bounding inferred mechanisms."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch84.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_diatom_attachment_survives_competition_qualification():
    _, _, docs = records()
    attachment, competition = docs[0]["ecological_interactions"]
    assert "SEM showed" in attachment["description"]
    assert competition["description"].startswith("HYPOTHESIZED -")
    assert all(e["supports"] == "PARTIAL" for e in competition["evidence"])
    assert "Medium-matched axenic HAC" in competition["description"]
    assert all("downstream" not in n for n in docs[0]["ecological_interactions"])


def test_diatom_physiological_and_transcriptomic_controls_are_distinct():
    _, rows, docs = records()
    discussion = docs[0]["discussions"][-1]["rationale"]
    assert "Matched late physiological controls exist" in discussion
    assert "no day-8 axenic transcriptome" in discussion
    assert "model predictions, not measured" in discussion
    assert rows[0]["status"] == "needs_research" and 1698 in rows[0]["issues"]


def test_phenol_positive_perturbation_arrows_survive():
    _, _, docs = records()
    oxidation, sink, endpoint = docs[1]["ecological_interactions"]
    assert "5 mM 2-BES blocked" in sink["description"]
    assert "AQDS enabled acetate production without methane" in sink["description"]
    assert oxidation["downstream"][0]["target"] == endpoint["name"]
    assert {e["target"] for e in sink["downstream"]} == {oxidation["name"], endpoint["name"]}
    assert all(not e["description"].startswith("HYPOTHESIZED") for e in sink["downstream"])


def test_phenol_conversion_is_not_complete_mineralization_or_enzyme_proof():
    _, _, docs = records()
    oxidation, _, endpoint = docs[1]["ecological_interactions"]
    assert "enzymes and mechanism unresolved" in oxidation["description"]
    assert oxidation["evidence"][-1]["supports"] == "PARTIAL"
    assert "Conversion" in endpoint["name"] and "Mineralization" not in endpoint["name"]
    assert "residual substrate at 100 days" in endpoint["description"]
    assert "formate or other carriers" in docs[1]["ecological_interactions"][1]["description"]


def test_phormidium_real_carbon_flow_has_explicit_major_participants():
    _, _, docs = records()
    fixation, carbon, _, _ = docs[2]["ecological_interactions"]
    assert fixation["downstream"][0]["target"] == carbon["name"]
    assert {t["term"]["id"] for t in carbon["participating_taxa"]} == {
        "NCBITaxon:1807132",
        "NCBITaxon:1979961",
        "NCBITaxon:203682",
    }
    assert "Protein/SIP supports" in carbon["description"]
    assert "metabolites" not in carbon and "downstream" not in carbon
    assert "interaction_type" not in fixation


def test_phormidium_gene_capacity_does_not_prove_reciprocal_services():
    _, _, docs = records()
    nodes = docs[2]["ecological_interactions"]
    assert len(nodes) == 4
    assert all(n.get("interaction_type") != "MUTUALISM" for n in nodes)
    polymers, alpha = nodes[2:]
    assert polymers["source_taxon"]["term"]["id"] == "NCBITaxon:1807132"
    assert polymers["target_taxon"]["term"]["id"] == "NCBITaxon:74201"
    assert polymers["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert "lower-peptide" in alpha["description"]
    assert all(
        p["term"]["id"] != "GO:0033013" for n in nodes for p in n.get("biological_processes", [])
    )


def test_phosphite_syntrophy_survives_intracellular_model_qualification():
    _, _, docs = records()
    donor, transfer, sink = docs[3]["ecological_interactions"]
    assert donor["evidence"][1]["supports"] == "PARTIAL"
    assert "not direct enzyme perturbation" in donor["description"]
    assert "inhibited by BES and by excess H2" in transfer["description"]
    assert "G11 in BES" in transfer["description"]
    assert "remains exergonic" in transfer["description"]
    assert donor["downstream"][0]["target"] == transfer["name"]
    assert transfer["downstream"][0]["target"] == sink["name"]


def test_phosphite_sink_actor_and_enrichment_boundaries():
    _, rows, docs = records()
    sink = docs[3]["ecological_interactions"][-1]
    assert sink["source_taxon"]["term"]["id"] == "NCBITaxon:45989"
    assert sink["target_taxon"]["term"]["id"] == "NCBITaxon:1918507"
    assert "not a demonstrated two-member pure culture" in sink["description"]
    assert "seven taxa" in docs[3]["discussions"][-1]["rationale"]
    assert "downstream" not in sink
    assert rows[3]["status"] == "needs_research" and 1700 in rows[3]["issues"]


def test_every_original_node_arrow_and_anchor_has_a_disposition():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 12
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 3
    assert sum(len(r["edges_before"]) for r in rows) == 8
    assert sum(len(r["edges_after"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 2
    assert ledger["primary_graph_snippet_count"] == 18
    assert ledger["independent_fresh_primary_graph_snippet_count"] == 11
    for row, doc in zip(rows, docs, strict=True):
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            e["target"] in names
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        )
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_history_sources_and_pending_lifecycle_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1694, 1695, 1696, 1697]
    assert ledger["unresolved_research_issues"] == [1698, 1699, 1700]
    assert ledger["unresolved_non_graph_issues"] == [1701]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert [d["query_chars"] for d in ledger["edison"]["dry_runs"]] == [11324, 18291, 8897]
    for row, doc in zip(rows, docs, strict=True):
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
