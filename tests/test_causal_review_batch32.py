"""Keep host mediation, intrinsic machinery and substrate inhibition distinct."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch32.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_tomato_participants_host_context_and_distinct_assays():
    _, docs = records()
    doc = docs[0]
    nodes = doc["ecological_interactions"]
    canonical = {t["taxon_term"]["term"]["id"] for t in doc["taxonomy"]}
    assert len(nodes) == 4 and len(canonical) == 5
    for node in nodes:
        assert node["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in node
        assert {t["term"]["id"] for t in node["participating_taxa"]} == canonical
        assert all(e["evidence_source"] == "IN_VIVO" for e in node["evidence"])
    assert "sterile river sand" in nodes[0]["description"]
    assert "nonsterile screen" in nodes[0]["description"]
    assert "downstream" not in nodes[3]
    assert "workflow" in doc["curation_history"][0]["action"].lower()


def test_tomato_mediation_is_qualified_and_shared_metadata_anchor_is_unchanged():
    _, docs = records()
    doc = docs[0]
    biomass, expression, ions, _ = doc["ecological_interactions"]
    assert expression["downstream"][0]["target"] == ions["name"]
    assert ions["downstream"][0]["target"] == biomass["name"]
    assert all(
        n["downstream"][0]["description"].startswith("PARTIAL -") for n in [expression, ions]
    )
    assert doc["engineering_design"]["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert doc["environmental_factors"][0]["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert "#1397" in doc["discussions"][0]["rationale"]


def test_methanococcus_intrinsic_machinery_and_real_feedback_cycle():
    _, docs = records()
    donor, machinery, sink = docs[1]["ecological_interactions"]
    assert donor["target_taxon"]["term"]["id"] == "NCBITaxon:267377"
    assert sink["target_taxon"]["term"]["id"] == "NCBITaxon:882"
    assert machinery["scope"] == "PAIRWISE"
    assert machinery["source_taxon"]["term"]["id"] == "NCBITaxon:882"
    assert not {"target_taxon", "interaction_type"} & machinery.keys()
    assert "Hyd/Hyn mutations slow growth" in machinery["description"]
    assert "Hmc also affects respiratory growth" in machinery["description"]
    assert "lactate-to-pyruvate" in donor["description"]
    assert donor["downstream"][0]["target"] == machinery["name"]
    assert machinery["downstream"][0]["target"] == sink["name"]
    assert sink["downstream"][0]["target"] == donor["name"]
    assert all(
        n["downstream"][0]["description"].startswith("PARTIAL -") for n in [donor, machinery]
    )
    assert all(e["supports"] == "PARTIAL" for e in sink["evidence"])


def test_methanosarcina_recipient_and_conditional_inhibition_without_new_structure():
    _, docs = records()
    donor, recipient, inhibition = docs[2]["ecological_interactions"]
    assert donor["interaction_type"] == "SYNTROPHY"
    assert recipient["scope"] == "PAIRWISE"
    assert recipient["source_taxon"]["term"]["id"] == "NCBITaxon:2208"
    assert not {"target_taxon", "interaction_type"} & recipient.keys()
    assert "interaction_type" not in inhibition
    assert inhibition["source_taxon"]["term"]["id"] == "NCBITaxon:876"
    assert inhibition["target_taxon"]["term"]["id"] == "NCBITaxon:2208"
    assert "not all methanogenesis" in inhibition["description"]
    assert "YE and RV" in inhibition["description"]
    assert inhibition["evidence"][0]["supports"] == "PARTIAL"
    assert {e["target"] for e in donor["downstream"]} == {recipient["name"], inhibition["name"]}
    assert donor["downstream"][1]["description"].startswith("PARTIAL -")
    assert "downstream" not in inhibition and "#1400" in docs[2]["discussions"][0]["rationale"]


def test_batch32_canonical_terms_anchors_history_and_exact_record_hashes():
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


def test_batch32_complete_decisions_and_pending_negative_arrow_are_honest():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1394, 1395, 1396]
    assert ledger["open_nongraph_followups"] == [1397, 1398, 1399]
    assert ledger["open_graph_research"] == [1400]
    assert [r["status"] for r in ledger["records"]] == ["reviewed", "reviewed", "needs_research"]
    assert ledger["edison"]["status"] == "dry_run_only_no_provider_job_or_charge"
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 10
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 7
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert (
            not row["renamed_nodes"]
            and not row["removed_node_decisions"]
            and not row["removed_edge_decisions"]
        )
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        assert {(e["source"], e["target"]) for e in row["edges_after"]} == {
            (e["source"], e["target"]) for e in row["edges_before"]
        }
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
