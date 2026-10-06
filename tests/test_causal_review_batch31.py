"""Keep exact-system rescue, modeled flux and condition-specific outcomes distinct."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch31.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_pelobacter_recipient_and_exact_pair_rescue_are_not_anas_or_reverse_exchange():
    _, docs = records()
    fermentation, output, relief = docs[0]["ecological_interactions"]
    assert fermentation["interaction_type"] == "SYNTROPHY"
    assert output["source_taxon"]["term"]["id"] == "NCBITaxon:243164"
    assert not {"target_taxon", "interaction_type"} & output.keys()
    assert "unchanged tceA transcript abundance" in output["description"]
    assert output["evidence"][1]["supports"] == "PARTIAL"
    assert relief["scope"] == "PAIRWISE" and "interaction_type" not in relief
    assert relief["source_taxon"]["term"]["id"] == "NCBITaxon:18"
    assert relief["target_taxon"]["term"]["id"] == "NCBITaxon:243164"
    assert "restored TCE reductive dechlorination" in relief["description"]
    assert relief["evidence"][0]["supports"] == "PARTIAL"
    assert "refers to ANAS, not the defined pair" in relief["evidence"][0]["explanation"]
    assert "Figure 2" in relief["downstream"][0]["description"]
    assert all(n["downstream"][0]["target"] == output["name"] for n in [fermentation, relief])
    pin = docs[0]["taxonomy"][1]["taxon_term"]["gtdb_classification"]
    assert pin["curated"] is True and pin["gtdb_id"] == "GTDB:g__Syntrophotalea"
    assert pin["majority_fraction"] == 0.5


def test_syntrophomonas_recipient_phenotype_and_observed_vs_modeled_aggregation():
    _, docs = records()
    fermentation, output, aggregation = docs[1]["ecological_interactions"]
    assert fermentation["interaction_type"] == "SYNTROPHY"
    assert "externally cobalamin-supplemented" in fermentation["description"]
    assert "donor-limited minimum-threshold assay" in fermentation["downstream"][0]["description"]
    assert output["scope"] == "PAIRWISE"
    assert output["source_taxon"]["term"]["id"] == "NCBITaxon:243164"
    assert not {"target_taxon", "interaction_type"} & output.keys()
    assert "cometabolic, not demonstrated growth-coupled" in output["description"]
    assert aggregation["scope"] == "COMMUNITY_LEVEL"
    assert not {"source_taxon", "target_taxon", "interaction_type"} & aggregation.keys()
    assert {p["term"]["id"] for p in aggregation["participating_taxa"]} == {
        "NCBITaxon:243164",
        "NCBITaxon:863",
    }
    assert aggregation["evidence"][0]["evidence_source"] == "IN_VITRO"
    model = aggregation["evidence"][1]
    assert model["evidence_source"] == "COMPUTATIONAL" and model["supports"] == "PARTIAL"
    assert aggregation["downstream"][0]["description"].startswith("PARTIAL -")
    assert "not from selective disruption and rescue" in aggregation["downstream"][0]["description"]


def test_cwv2_common_amendment_outcomes_are_not_an_outcome_to_outcome_arrow():
    _, docs = records()
    amendment, activity, tce, vc, _ = docs[2]["ecological_interactions"]
    assert len(docs[2]["ecological_interactions"]) == 5
    assert amendment["downstream"][0]["target"] == activity["name"]
    assert activity["downstream"][0]["target"] == tce["name"]
    assert activity["downstream"][0]["description"].startswith("PARTIAL -")
    assert "does not selectively isolate colonization" in activity["downstream"][0]["description"]
    assert "downstream" not in tce
    assert "BC700" in activity["description"]
    assert "not asserted to have the strongest adsorption" in activity["description"]
    assert "high-inoculum" in vc["description"] and "lower-inoculum" in vc["description"]
    assert "could instead increase vinyl chloride" in vc["description"]


def test_cwv2_guild_profiles_do_not_establish_flux_or_field_stability():
    _, docs = records()
    guild = docs[2]["ecological_interactions"][-1]
    assert "interaction_type" not in guild
    assert "HYPOTHESIZED" in guild["description"]
    assert "do not demonstrate hydrogen or electron flux" in guild["description"]
    assert "long-term field stability" in guild["description"]
    assert guild["evidence"][0]["supports"] == "PARTIAL"
    assert "downstream" not in guild
    assert "UNCO" in records()[0]["records"][2]["source_review"]["PMID:41442978"]["scope"]
    assert (
        "Final published full body not accessed"
        in records()[0]["records"][2]["source_review"]["PMID:41442978"]["scope"]
    )


def test_batch31_canonical_terms_exact_anchors_and_append_only_history():
    ledger, docs = records()
    for row, doc in zip(ledger["records"], docs, strict=True):
        canonical = {t["taxon_term"]["term"]["id"]: t["taxon_term"] for t in doc["taxonomy"]}
        names = {n["name"] for n in doc["ecological_interactions"]}
        for node in doc["ecological_interactions"]:
            terms = node.get("participating_taxa", []) + [
                node[k] for k in ["source_taxon", "target_taxon"] if k in node
            ]
            for term in terms:
                original = canonical[term["term"]["id"]]
                assert {k: term[k] for k in ["preferred_term", "term"]} == {
                    k: original[k] for k in ["preferred_term", "term"]
                }
            assert all(
                e["target"] in names and e["target"] != node["name"]
                for e in node.get("downstream", [])
            )
        (gap,) = doc["discussions"]
        assert gap["kind"] == "KNOWLEDGE_GAP" and gap["status"] == "OPEN"
        assert set(gap["attaches_to"]) == {"ecological_interactions#" + n for n in names}
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    assert "Removed the vinyl-chloride mitigation" in docs[2]["curation_history"][0]["changes"]


def test_batch31_complete_decisions_and_pending_co_research_are_honest():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1388, 1389, 1390]
    assert ledger["open_nongraph_followups"] == [765, 1391]
    assert ledger["open_graph_research"] == [1392]
    assert [r["status"] for r in ledger["records"]] == ["reviewed", "needs_research", "reviewed"]
    assert ledger["edison"]["status"] == "dry_run_only_no_provider_job_or_charge"
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 11
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 1
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert not row["renamed_nodes"] and not row["removed_node_decisions"]
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        retained = {(e["source"], e["target"]) for e in row["edges_after"]}
        removed = {(e["source"], e["target"]) for e in row["removed_edge_decisions"]}
        assert not retained & removed
        assert retained | removed == {(e["source"], e["target"]) for e in row["edges_before"]}
    assert "#1392" in docs[1]["discussions"][0]["rationale"]
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
