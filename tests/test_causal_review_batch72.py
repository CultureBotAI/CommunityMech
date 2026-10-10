"""Preserve gas physiology, carbon transfer, and a justified empty peptide graph."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch72.yaml"
A = "Methylomicrobium_Chlorella_Methane_Sequestration_Coculture"
B = "Methylotuvimicrobium_Synechococcus_Gas_Feedstock_Coculture"
C = "Microalgae_Cyanobacteria_Bioactive_Peptide_Consortia"
D = "Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {s: yaml.safe_load((ROOT / r["path"]).read_text()) for s, r in rows.items()}
    return ledger, rows, docs


def test_chlorella_retains_mutual_growth_but_not_cross_system_mechanisms():
    _, _, docs = records()
    growth, carbon, ph = docs[A]["ecological_interactions"]
    assert growth["interaction_type"] == "MUTUALISM"
    assert "enhanced growth of both" in growth["description"]
    assert "order of magnitude" in carbon["description"]
    for node in [carbon, ph]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert len(node["participating_taxa"]) == 2
        assert not {"source_taxon", "target_taxon", "interaction_type"} & node.keys()
    assert growth["downstream"][0]["description"].startswith("PARTIAL -")
    assert ph["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert all(
        ev["reference"] == "doi:10.1016/j.biortech.2024.130607"
        for node in docs[A]["ecological_interactions"]
        for ev in node["evidence"]
    )
    rationale = docs[A]["discussions"][-1]["rationale"]
    assert "M. buryatense 5GB1/A. platensis" in rationale
    assert "prediction awaiting experimental validation" in rationale


def test_gas_coculture_preserves_oxygen_support_but_identifies_estimated_rates():
    _, _, docs = records()
    oxygen, carbon, biomass = docs[B]["ecological_interactions"]
    assert "interaction_type" not in oxygen and "interaction_type" not in biomass
    assert not oxygen["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert "does not imply anaerobic" in oxygen["description"]
    assert carbon["description"].startswith("PARTIAL -")
    assert "stoichiometric estimates" in carbon["downstream"][0]["description"]
    assert "equations 3-9" in carbon["evidence"][1]["explanation"]
    assert "validates biomass estimates" in carbon["evidence"][1]["explanation"]
    assert all(ev["supports"] == "PARTIAL" for ev in carbon["evidence"])
    assert len(biomass["participating_taxa"]) == 2
    assert "20ZR derivative" in biomass["description"]


def test_peptide_panel_retains_empty_graph_without_losing_the_positive_assays():
    _, rows, docs = records()
    doc = docs[C]
    assert doc["ecological_interactions"] == []
    assert rows[C]["node_decisions"] == rows[C]["edges_after"] == []
    assert set(rows[C]["allowed_changed_fields"]) == {"discussions", "curation_history"}
    discussion = doc["discussions"][-1]
    assert discussion["attaches_to"] == []
    assert discussion["status"] == "OPEN"
    for phrase in [
        "not a five-member",
        "commercial Alcalase",
        "not evidence that no interaction",
        "ABTS",
        "ORAC",
    ]:
        assert phrase in discussion["rationale"]
    assert "C1 combined" in doc["description"] and "consortium C2 combined" in doc["description"]
    assert doc["cultivation_setup"][0]["instrument_detail"] == "flat photobioreactor"
    assert "environmental_factors" not in doc
    assert {d["accession"] for d in doc["associated_datasets"]} == {"PXD077201", "PXD077149"}


def test_sulfadiazine_retains_supported_cross_feeding_without_nitrogen_overclaim():
    _, _, docs = records()
    release, assimilation, degradation = docs[D]["ecological_interactions"]
    assert release["interaction_type"] == "CROSS_FEEDING"
    assert release["downstream"][0]["target"] == assimilation["name"]
    assert assimilation["downstream"][0]["target"] == degradation["name"]
    for node in [release, assimilation]:
        assert not node["downstream"][0]["description"].startswith(("HYPOTHESIZED", "PARTIAL"))
    for phrase in [
        "13C incorporation",
        "does not independently establish 15N",
        "42.8 +/- 1.8%",
        "45.9 +/- 3.2%",
        "subthreshold",
    ]:
        assert phrase in assimilation["description"]
    assert (
        "day 2 in Microbacterium alone and day 4 in coculture"
        in assimilation["downstream"][0]["description"]
    )
    assert "sampled days 0, 2 and 4" in degradation["description"]
    assert "closed carbon balance" in degradation["description"]
    assert docs[D]["discussions"][0]["discussion_id"] == "exact-brunner-msm-vitamin-composition"
    assert (
        "13C- and 15N-diazine labeled"
        in docs[D]["environmental_factors"][0]["evidence"][0]["snippet"]
    )


def test_batch72_accounts_for_every_original_node_and_arrow_without_extensions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 9
    assert sum(len(r["edges_before"]) for r in rows.values()) == 6
    assert sum(len(r["edges_after"]) for r in rows.values()) == 6
    for stem, row in rows.items():
        assert not row["removed_node_decisions"] and not row["removed_edge_decisions"]
        assert not row["renamed_nodes"]
        assert {(e["source"], e["target"]) for e in row["edges_before"]} == {
            (e["source"], e["target"]) for e in row["edges_after"]
        }
        names = {n["name"] for n in docs[stem]["ecological_interactions"]}
        assert {n["node"] for n in row["node_decisions"]} == names
        assert all(e["target"] in names for e in row["edges_after"])
        assert all(
            a.split("#", 1)[1] in names
            for d in docs[stem]["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0


def test_batch72_participants_are_canonical_and_histories_are_explicit():
    _, rows, docs = records()
    for stem, doc in docs.items():
        canonical = {
            (t["taxon_term"]["preferred_term"], t["taxon_term"]["term"]["id"])
            for t in doc["taxonomy"]
        }
        for node in doc["ecological_interactions"]:
            for taxon in node.get("participating_taxa", []):
                assert (taxon["preferred_term"], taxon["term"]["id"]) in canonical
        row = rows[stem]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    assert docs[D]["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"
    assert docs[C]["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] == "AMBIGUOUS"


def test_batch72_review_is_bounded_and_non_graph_followup_stays_open():
    ledger, _, _ = records()
    assert not ledger["independent_approval"]
    assert ledger["issues"] == [1608, 1609, 1610, 1611]
    assert ledger["unresolved_non_graph_issues"] == [1612]
    assert ledger["primary_graph_snippet_count"] == 17
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"]
    assert "primary-abstract-supported" in " ".join(ledger["limitations"])
    assert "equation pages10-11 visually checked" in " ".join(ledger["limitations"])
