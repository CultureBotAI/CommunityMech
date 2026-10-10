"""Keep genomic models, attachment proxies and aggregate outcomes distinct."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch38.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_ensifer_keeps_a_genomic_hypothesis_not_measured_exchange():
    _, docs = records()
    model, performance, surface = docs[0]["ecological_interactions"]
    assert model["scope"] == "PAIRWISE"
    assert model["source_taxon"]["preferred_term"] == "Ensifer sp. YF2"
    assert model["target_taxon"]["preferred_term"] == "Sphingobacterium sp. Y2"
    assert model["description"].startswith("HYPOTHESIZED -")
    assert model["evidence"][0]["supports"] == "PARTIAL"
    assert model["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert [e["target"] for e in model["downstream"]] == [performance["name"]]
    assert model["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert "not measured donor export" in model["description"]
    for node in [performance, surface]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert len(node["participating_taxa"]) == 2
        assert "downstream" not in node
    assert all(
        not {"interaction_type", "biological_processes"} & n.keys()
        for n in [model, performance, surface]
    )
    assert "MF1 is a comparator" in performance["description"]
    assert "not demonstrated reciprocal fitness" in performance["description"]
    assert "do not by themselves establish complete mineralization" in surface["description"]


def test_cpr_records_a_multisite_framework_and_imperfect_attachment_proxy():
    _, docs = records()
    coexist, sites, fractions, attachment, replication = docs[1]["ecological_interactions"]
    assert "eight Northern California" in coexist["description"]
    assert "not one defined three-member culture" in coexist["description"]
    assert "founder effects" in sites["description"]
    assert "not direct taxonomic identification" in fractions["description"]
    assert "DNA yield and genome-size corrections" in fractions["description"]
    assert fractions["evidence"][0]["supports"] == "PARTIAL"
    assert fractions["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    for node in [coexist, sites, fractions, attachment]:
        assert len(node["participating_taxa"]) == 3
    assert len(replication["participating_taxa"]) == 2
    assert all("interaction_type" not in n for n in docs[1]["ecological_interactions"])
    assert all("downstream" not in n for n in [coexist, sites, fractions, replication])
    assert "2026-10-02" in docs[1]["discussions"][-1]["rationale"]
    assert "separate Oak Ridge groundwater" in docs[1]["discussions"][-1]["rationale"]


def test_cpr_replication_does_not_include_archaea_or_prove_host_neutrality():
    _, docs = records()
    *_, attachment, replication = docs[1]["ecological_interactions"]
    assert [e["target"] for e in attachment["downstream"]] == [replication["name"]]
    assert attachment["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert "not selectively perturbed" in attachment["downstream"][0]["description"]
    assert "inferred from size" in attachment["description"]
    assert [p["term"]["id"] for p in attachment["biological_processes"]] == ["GO:0007155"]
    assert "three of four" in replication["description"]
    assert "average genome-replication state" in replication["description"]
    assert "not a single-cell growth rate or doubling time" in replication["description"]
    assert "Archaea were excluded" in replication["description"]
    assert "host fitness was not measured" in replication["description"]
    assert "biological_processes" not in replication
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in replication["evidence"])
    assert all(e["supports"] == "PARTIAL" for e in replication["evidence"][:2])


def test_euglena_profiles_are_intrinsic_without_specific_tocopherol_export():
    _, docs = records()
    eg, cp, complement, output = docs[2]["ecological_interactions"]
    for node in [eg, cp]:
        assert node["scope"] == "PAIRWISE"
        assert (
            not {"interaction_type", "target_taxon", "participating_taxa", "downstream"}
            & node.keys()
        )
        assert node["description"].startswith("PARTIAL -")
        assert all(e["supports"] == "PARTIAL" for e in node["evidence"])
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
    assert eg["source_taxon"]["preferred_term"] == "Euglena gracilis"
    assert cp["source_taxon"]["preferred_term"] == "Chlorella pyrenoidosa"
    assert cp["source_taxon"]["term"] == {
        "id": "NCBITaxon:3078",
        "label": "Auxenochlorella pyrenoidosa",
    }
    assert "metabolites" not in eg
    assert "alpha-tocopherol was exported" in eg["description"]
    assert output["metabolites"][0]["term"]["id"] == "CHEBI:22470"
    assert complement["description"].startswith("HYPOTHESIZED -")


def test_microalgal_total_output_does_not_establish_reciprocal_fitness():
    _, docs = records()
    _, _, complement, output = docs[2]["ecological_interactions"]
    assert [e["target"] for e in complement["downstream"]] == [output["name"]]
    assert complement["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert all(e["supports"] == "PARTIAL" for e in complement["evidence"])
    assert "downstream" not in output
    for node in [complement, output]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert len(node["participating_taxa"]) == 2
        assert "interaction_type" not in node
    assert "3:7 coculture in TAP" in output["description"]
    assert "do not establish that both species benefit" in output["description"]
    assert "exogenous alpha-lipoic acid" in output["description"]
    assert "not proof of endogenous cross-feeding" in output["description"]


def test_batch38_canonical_participants_anchors_history_and_hashes():
    ledger, docs = records()
    for row, doc in zip(ledger["records"], docs, strict=True):
        canonical = {
            (t["taxon_term"]["term"]["id"], t["taxon_term"]["preferred_term"]): t["taxon_term"]
            for t in doc["taxonomy"]
        }
        names = {n["name"] for n in doc["ecological_interactions"]}
        for node in doc["ecological_interactions"]:
            terms = node.get("participating_taxa", []) + [
                node[k] for k in ["source_taxon", "target_taxon"] if k in node
            ]
            for term in terms:
                assert (
                    term["term"] == canonical[(term["term"]["id"], term["preferred_term"])]["term"]
                )
            assert all(
                e["target"] in names and e["target"] != node["name"]
                for e in node.get("downstream", [])
            )
        assert len(doc["discussions"]) == 1
        gap = doc["discussions"][0]
        assert gap["kind"] == "KNOWLEDGE_GAP" and gap["status"] == "OPEN"
        assert set(gap["attaches_to"]) == {"ecological_interactions#" + n for n in names}
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_batch38_all_nodes_and_arrows_have_explicit_dispositions():
    ledger, docs = records()
    assert ledger["independent_approval"] is False and ledger["issues"] == [1438, 1439, 1440]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 12
    assert all(
        not r["removed_node_decisions"] and not r["renamed_nodes"] for r in ledger["records"]
    )
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 3
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 3
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert row["status"] == "reviewed"
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        assert {(e["source"], e["target"]) for e in row["edges_before"]} == {
            (e["source"], e["target"]) for e in row["edges_after"] + row["removed_edge_decisions"]
        }
        assert len(row["edges_after"]) == 1
        assert row["edges_after"][0]["description"].startswith("HYPOTHESIZED -")
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest


def test_batch38_does_not_certify_nongraph_fields_or_unread_sources():
    ledger, docs = records()
    assert ledger["open_nongraph_followups"] == [1441, 1442, 1443]
    assert ledger["open_graph_research"] == []
    assert "no_provider_job_or_charge" in ledger["edison"]["status"]
    assert docs[0]["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] == "AMBIGUOUS"
    assert len(docs[0]["taxonomy"]) == 2
    assert "paywalled" in docs[0]["growth_media"][0]["preparation_notes"]
    source = ledger["records"][0]["source_review"]["PMID:41996795"]["scope"]
    assert "Open access" in source and "retrieval returned403" in source
    assert "Remaining main body" in ledger["records"][1]["source_review"]["PMID:32252814"]["scope"]
    cache = (ROOT / "references_cache/PMID_33495623.md").read_text()
    assert "content_type: abstract_only" in cache and "OPEN-ACCESS FULL TEXT" in cache
    assert ledger["issue_deduplication"]["ignored_hidden_local_files_included"] is True
    assert ledger["issue_deduplication"]["comments_exhaustive"] is False
