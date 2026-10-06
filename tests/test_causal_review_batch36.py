"""Preserve treatment, assay, strain and causal-mediation boundaries."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch36.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_ecofab_excludes_sterile_plant_experiment_and_keeps_treatment_effects():
    ledger, docs = records()
    treatment, trait, assembly, medium, biomass = docs[0]["ecological_interactions"]
    assert [n["node"] for n in ledger["records"][0]["removed_node_decisions"]] == [
        "Nitrogen-Status EcoFAB Root Exudation"
    ]
    assert {e["target"] for e in treatment["downstream"]} == {
        assembly["name"],
        medium["name"],
        biomass["name"],
    }
    for node in [treatment, assembly, medium, biomass]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert len(node["participating_taxa"]) == 17
        assert "interaction_type" not in node
    assert "10-day-old" in treatment["description"]
    assert "sterile" in docs[0]["discussions"][-1]["rationale"]
    assert "14 bacterial bioassays were individual" in docs[0]["discussions"][-1]["rationale"]


def test_ecofab_trait_mechanism_is_intrinsic_and_hypothesized():
    _, docs = records()
    treatment, trait, assembly, medium, _ = docs[0]["ecological_interactions"]
    assert trait["scope"] == "PAIRWISE"
    assert trait["source_taxon"]["preferred_term"] == "Paraburkholderia sp. OAS925"
    assert not {"target_taxon", "participating_taxa", "interaction_type"} & trait.keys()
    assert trait["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert "sixth, not first" in trait["description"]
    assert all("biological_processes" not in n for n in [treatment, trait, assembly])
    assert "downstream" not in assembly
    assert "16S reads" in assembly["description"]
    assert "extracellular enzyme activity" in medium["description"]
    assert "not identified donor-to-recipient cross-feeding" in medium["description"]


def test_hmo_retains_reciprocal_exchange_not_part_whole_summary_arrow():
    _, docs = records()
    cysteine, sugars, mutualism = docs[1]["ecological_interactions"]
    assert [e["target"] for e in cysteine["downstream"]] == [sugars["name"]]
    assert [e["target"] for e in sugars["downstream"]] == [cysteine["name"]]
    assert sugars["downstream"][0]["description"].startswith("PARTIAL -")
    assert "downstream" not in mutualism
    assert [n["interaction_type"] for n in [cysteine, sugars, mutualism]] == [
        "CROSS_FEEDING",
        "CROSS_FEEDING",
        "MUTUALISM",
    ]
    assert cysteine["source_taxon"] == sugars["target_taxon"]
    assert cysteine["target_taxon"] == sugars["source_taxon"]
    assert "part/whole restatement" in docs[1]["discussions"][-1]["rationale"]


def test_hmo_bounds_release_route_ph_and_host_inference():
    _, docs = records()
    cysteine, sugars, mutualism = docs[1]["ecological_interactions"]
    assert "E. coli K12" in cysteine["description"]
    assert "delta-cysE" in cysteine["description"]
    assert "overflow or lysis" in cysteine["description"]
    assert "fucose and galactose" in sugars["description"]
    assert "pH readjustment from 4.3 to 6.3" in sugars["description"]
    assert "0.5%" in mutualism["description"]
    assert "without added cysteine or casamino acids" in mutualism["description"]
    assert "living infants remain untested" in mutualism["description"]


def test_gl10_specialization_is_overlapping_not_direct_cross_feeding():
    _, docs = records()
    doc = docs[2]
    (node,) = doc["ecological_interactions"]
    assert "downstream" not in node
    assert node["interaction_type"] == "NICHE_PARTITIONING"
    assert "partial, overlapping" in node["description"]
    assert "GL10 retains xylose metabolism" in node["description"]
    assert "XL12 still consumes glucose" in node["description"]
    assert len({p["term"]["id"] for p in node["participating_taxa"]}) == 1
    assert [p["preferred_term"] for p in node["participating_taxa"]] == [
        "Escherichia coli GL10",
        "Escherichia coli XL12",
    ]
    assert node["evidence"][1]["supports"] == "PARTIAL"
    assert "1.22 g/L at 36 h" in node["evidence"][1]["explanation"]
    assert doc["discussions"][0]["discussion_id"] == "gl10_xl12_direct_cross_feeding"
    assert len(doc["discussions"]) == 2


def test_batch36_canonical_participants_anchors_history_and_hashes():
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
        for gap in doc["discussions"]:
            assert gap["kind"] == "KNOWLEDGE_GAP" and gap["status"] == "OPEN"
            assert set(gap["attaches_to"]) <= {"ecological_interactions#" + n for n in names}
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_batch36_all_original_nodes_and_arrows_have_dispositions():
    ledger, docs = records()
    assert ledger["independent_approval"] is False and ledger["issues"] == [1424, 1425, 1426]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 9
    assert sum(len(r["removed_node_decisions"]) for r in ledger["records"]) == 1
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 2
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert not row["renamed_nodes"]
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        assert {(e["source"], e["target"]) for e in row["edges_before"]} == {
            (e["source"], e["target"]) for e in row["edges_after"] + row["removed_edge_decisions"]
        }
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest


def test_batch36_nongraph_metadata_and_unread_sources_are_not_certified():
    ledger, docs = records()
    assert ledger["open_nongraph_followups"] == [1427, 1428, 1429]
    assert ledger["open_graph_research"] == []
    assert "no_provider_job_or_charge" in ledger["edison"]["status"]
    assert docs[0]["taxonomy"][6]["taxon_term"]["term"]["id"] == "NCBITaxon:85413"
    assert docs[0]["taxonomy"][6]["taxon_term"]["term"]["label"] == "Allobosea"
    assert "0.1%" in docs[1]["growth_media"][0]["name"]
    assert ledger["issue_deduplication"]["ignored_hidden_local_files_included"] is True
    assert ledger["issue_deduplication"]["comments_exhaustive"] is False
