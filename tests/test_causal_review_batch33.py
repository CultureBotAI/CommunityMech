"""Keep assay attribution, genomic potential and host mediation distinct."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch33.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_diclofenac_mc_does_not_inherit_isolate_metabolites():
    _, docs = records()
    loss, _ = docs[0]["ecological_interactions"]
    assert "5-OH-DCF was not detected in MC" in loss["description"]
    assert "CHEBI:59612" not in {m["term"]["id"] for m in loss["metabolites"]}
    assert loss["evidence"][1]["supports"] == "PARTIAL"
    assert "pools separate isolate and MC assays" in loss["evidence"][1]["explanation"]
    assert "mineralization or detoxification" in loss["description"]


def test_diclofenac_profiles_do_not_assert_degraders_or_workflow_causality():
    _, docs = records()
    doc = docs[0]
    loss, profile = doc["ecological_interactions"]
    assert "separate denominators" in profile["description"]
    assert "biological_processes" not in profile
    assert all("downstream" not in n and "interaction_type" not in n for n in [loss, profile])
    assert all(len(n["participating_taxa"]) == 10 for n in [loss, profile])
    assert doc["discussions"][0]["discussion_id"] == "diclofenac_mc_direct_degrader_assignment"
    assert "taxonomy#Burkholderia" in doc["discussions"][0]["attaches_to"]


def test_dolichospermum_potential_is_not_exchange_or_canonical_cobalamin():
    _, docs = records()
    biotin, corrinoid = docs[1]["ecological_interactions"]
    assert all("interaction_type" not in n and "downstream" not in n for n in [biotin, corrinoid])
    assert not {"metabolites", "biological_processes"} & corrinoid.keys()
    assert "DMB lower-ligand" in corrinoid["description"]
    assert "not a complete culture census" in biotin["description"]
    assert all(
        e["supports"] == "PARTIAL" and e["evidence_source"] == "COMPUTATIONAL"
        for n in [biotin, corrinoid]
        for e in n["evidence"]
    )
    assert docs[1]["discussions"][0]["discussion_id"] == "direct_cofactor_exchange_unresolved"


def test_drosophila_joint_outcomes_do_not_invent_exchange_or_mutualism():
    _, docs = records()
    tag, _, nutrition = docs[2]["ecological_interactions"]
    for node in [tag, nutrition]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert "interaction_type" not in node and "target_taxon" not in node
        assert {p["term"]["id"] for p in node["participating_taxa"]} == {
            "NCBITaxon:434",
            "NCBITaxon:1578",
            "NCBITaxon:7227",
        }
    assert "downstream" not in tag
    assert "no significant weight, protein or glycogen response" in nutrition["description"]
    assert "2015 host-genotype study" in nutrition["description"]


def test_drosophila_abundance_is_species_bounded_and_mediation_partial():
    _, docs = records()
    tag, abundance, _ = docs[2]["ecological_interactions"]
    assert abundance["source_taxon"]["term"]["id"] == "NCBITaxon:1578"
    assert abundance["target_taxon"]["term"]["id"] == "NCBITaxon:434"
    assert "interaction_type" not in abundance
    assert "GO:0040007" not in {p["term"]["id"] for p in abundance["biological_processes"]}
    assert "not significantly with L. plantarum" in abundance["description"]
    assert abundance["downstream"][0]["target"] == tag["name"]
    assert abundance["downstream"][0]["description"].startswith("PARTIAL -")


def test_batch33_canonical_terms_anchors_histories_and_exact_hashes():
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
        assert {a for a in gap["attaches_to"] if a.startswith("ecological_interactions#")} == {
            "ecological_interactions#" + n for n in names
        }
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_batch33_complete_node_and_arrow_decisions_without_invented_structure():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1402, 1403, 1404]
    assert [r["status"] for r in ledger["records"]] == ["reviewed", "reviewed", "needs_research"]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 7
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 1
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 1
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert not row["renamed_nodes"] and not row["removed_node_decisions"]
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        assert {(e["source"], e["target"]) for e in row["edges_before"]} == {
            (e["source"], e["target"]) for e in row["edges_after"] + row["removed_edge_decisions"]
        }
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest


def test_batch33_pending_work_and_withdrawn_issue_are_not_claimed_fixed():
    ledger, docs = records()
    assert ledger["open_nongraph_followups"] == [765, 1406, 1407]
    assert ledger["open_graph_research"] == [1408]
    assert ledger["withdrawn_issue"]["number"] == 1405
    assert "Incorrect premise" in ledger["withdrawn_issue"]["reason"]
    assert len(docs[0]["related_ingredients"]) == 1
    assert docs[0]["related_ingredients"][0]["chebi_term"]["id"] == "CHEBI:4509"
    assert ledger["edison"]["status"] == "dry_run_only_no_provider_job_or_charge"
    assert "#1408" in docs[2]["discussions"][0]["rationale"]
    assert "#765" in docs[2]["discussions"][0]["rationale"]
