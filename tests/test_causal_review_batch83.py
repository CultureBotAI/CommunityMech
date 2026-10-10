"""Preserve measured degradation, syntrophy and plant phenotypes with scoped causality."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch83.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_pes_measured_removal_survives_candidate_mechanism_qualification():
    _, _, docs = records()
    handoff, emulsion, removal = docs[0]["ecological_interactions"]
    assert "approached complete removal" in removal["description"]
    assert "49.95%" in removal["description"]
    assert "carbon mineralization" in removal["description"]
    assert handoff["evidence"][1]["supports"] == "PARTIAL"
    for node in [handoff, emulsion]:
        assert node["downstream"][0]["target"] == removal["name"]
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED -")


def test_pes_emulsion_assay_is_not_pyrene_flux_or_mutualism():
    _, _, docs = records()
    emulsion = docs[0]["ecological_interactions"][1]
    assert "soybean-oil" in emulsion["description"]
    assert "yeast extract" in emulsion["description"]
    assert "68%" in emulsion["description"]
    assert "interaction_type" not in emulsion
    assert any(
        d["discussion_id"] == "hphtc5_decarboxylase_candidate_unresolved"
        for d in docs[0]["discussions"]
    )


def test_syntrophy_retains_growth_and_corrects_universal_partner_dependence():
    _, _, docs = records()
    prop, alternative, methane = docs[1]["ecological_interactions"]
    assert prop["target_taxon"]["term"]["id"] == "NCBITaxon:145262"
    assert methane["target_taxon"]["term"]["id"] == "NCBITaxon:110500"
    assert "pure-culture growth on pyruvate and fumarate" in prop["description"]
    assert prop["evidence"][0]["snippet"].startswith("The strain grew on propionate")
    assert "growth on propionate" in prop["evidence"][0]["explanation"]
    assert "ethylene glycol" in alternative["description"]
    assert all(m["term"]["id"] != "CHEBI:30089" for m in alternative["metabolites"])


def test_coaggregation_is_positive_but_not_direct_electron_conduction():
    _, rows, docs = records()
    methane = docs[1]["ecological_interactions"][2]
    assert "stronger coaggregation on propionate" in methane["description"]
    assert "Fick-law" in methane["description"]
    assert "2-BES" in methane["description"]
    assert len([e for e in methane["evidence"] if e["reference"] == "PMID:16332758"]) == 2
    assert rows[1]["status"] == "needs_research" and 1689 in rows[1]["issues"]


def test_pepper_workflow_removed_but_author_model_retained_as_hypothesis():
    _, _, docs = records()
    diversity, native, plant = docs[2]["ecological_interactions"]
    assert "increased fungal and bacterial Chao richness" in diversity["description"]
    assert diversity["downstream"][0]["target"] == native["name"]
    assert native["downstream"][0]["target"] == plant["name"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED -") for n in [diversity, native]
    )
    assert "total genus-level Scedosporium decreased" in native["description"]
    assert "OTU451 also increased" in native["description"]
    assert len(docs[2]["taxonomy"]) == 4
    assert docs[2]["taxonomy"][-1]["taxon_term"]["term"]["label"] == "Aspergillus"


def test_plant_growth_is_not_reciprocal_microbe_fitness():
    _, _, docs = records()
    for doc in docs[2:]:
        assert all("interaction_type" not in n for n in doc["ecological_interactions"])
        assert doc["ecological_interactions"][-1]["evidence"][0]["evidence_source"] == "IN_VIVO"
    assert "45 days" in docs[2]["ecological_interactions"][-1]["description"]


def test_biocontrol_heterogeneous_screens_do_not_credit_all_members_with_antagonism():
    _, _, docs = records()
    traits, antagonism, _ = docs[3]["ecological_interactions"]
    assert "not re-quantified in rhizosphere soil" in traits["description"]
    assert "58.4% and 17.6%" in antagonism["description"]
    assert {t["term"]["id"] for t in antagonism["participating_taxa"]} == {
        "NCBITaxon:1931",
        "NCBITaxon:306",
    }
    assert "biological_processes" not in antagonism
    assert "oomycete" in antagonism["description"]


def test_biocontrol_positive_host_proxies_are_not_direct_disease_scores():
    _, rows, docs = records()
    plant = docs[3]["ecological_interactions"][-1]
    assert "improved root length, height, biomass" in plant["description"]
    assert "direct disease-severity scoring" in plant["description"]
    assert "were not performed" in plant["description"]
    assert "no SynCom-only control" in plant["description"]
    assert "metabolites" not in plant
    assert rows[3]["status"] == "needs_research" and 1690 in rows[3]["issues"]


def test_every_original_node_arrow_and_anchor_has_a_disposition():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 12
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 1
    assert sum(len(r["edges_before"]) for r in rows) == 9
    assert sum(len(r["edges_after"]) for r in rows) == 8
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    assert ledger["primary_graph_snippet_count"] == 18
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


def test_history_short_cache_and_pending_lifecycle_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1685, 1686, 1687, 1688]
    assert ledger["unresolved_research_issues"] == [1689, 1690]
    assert ledger["unresolved_non_graph_issues"] == [1691]
    assert len(ledger["cache_changes"]) == 1
    cache = ledger["cache_changes"][0]
    assert cache["quoted_words"] == 20
    assert hashlib.sha256((ROOT / cache["path"]).read_bytes()).hexdigest() == cache["sha256"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    for row, doc in zip(rows, docs, strict=True):
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
