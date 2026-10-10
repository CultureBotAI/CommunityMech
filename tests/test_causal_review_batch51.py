"""Preserve positive outcomes without upgrading inferred mediators to proven ones."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-enrichments-core20-batch51.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def canonical(doc, indices):
    return [
        {
            "preferred_term": doc["taxonomy"][i]["taxon_term"]["preferred_term"],
            "term": doc["taxonomy"][i]["taxon_term"]["term"],
        }
        for i in indices
    ]


def test_ammonia_canonical_directions_and_bulk_conversion_are_preserved():
    _, (doc, _, _) = records()
    nodes = doc["ecological_interactions"]
    for node, source, target in zip(nodes, [0, 1, 1], [1, 2, 3], strict=True):
        assert node["scope"] == "PAIRWISE" and node["interaction_type"] == "SYNTROPHY"
        assert node["source_taxon"] == canonical(doc, [source])[0]
        assert node["target_taxon"] == canonical(doc, [target])[0]
        assert node["description"].startswith("PARTIAL -")
        assert node["evidence"][0]["supports"] == "PARTIAL"
    assert nodes[0]["evidence"][-1]["supports"] == "SUPPORT"
    assert nodes[0]["evidence"][-1]["evidence_source"] == "IN_VITRO"
    assert "single long-term 0B" in nodes[0]["description"]
    assert "without a completely annotated Wood-Ljungdahl pathway" in nodes[1]["description"]
    assert "does not establish an improved" in nodes[2]["description"]
    assert "distinct from acetoclastic" in nodes[2]["description"]
    gap = doc["discussions"][0]
    assert gap["discussion_id"] == "kg-high-ammonia-mag2-sao-inference"
    assert gap["evidence"][0]["supports"] == "PARTIAL"
    assert len(gap["attaches_to"]) == 3


def test_switchgrass_participants_are_explicit_without_pairwise_niche_claims():
    _, (_, doc, _) = records()
    for node, indices in zip(doc["ecological_interactions"], [range(5), [2, 3], [4]], strict=True):
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert node["participating_taxa"] == canonical(doc, indices)
        assert not {"source_taxon", "target_taxon", "interaction_type"} & node.keys()
    conversion, profiles, methane = doc["ecological_interactions"]
    assert "one sequentially operated reactor" in conversion["description"]
    assert "Vitamins, medium optimization, mixing and adaptation" in conversion["description"]
    assert "not direct catalytic activities" in conversion["description"]
    assert profiles["name"] == "Fraction-Associated CAZyme Protein Profiles"
    assert "protein adsorption" in profiles["description"]
    assert methane["evidence"][0]["supports"] == "SUPPORT"
    assert methane["evidence"][1]["supports"] == "PARTIAL"
    assert "do not quantify its fraction" in methane["description"]
    assert "do not mean absent turnover" in methane["description"]


def test_core20_retains_positive_transcripts_and_load_without_mediation():
    _, (_, _, doc) = records()
    colonization, immune, reduction = doc["ecological_interactions"]
    for node in [colonization, immune, reduction]:
        assert node["participating_taxa"] == canonical(doc, [0])
        assert node["evidence"][0]["supports"] == "SUPPORT"
    assert "W8131" in colonization["description"]
    assert "not unchanged composition" in colonization["description"]
    assert "separate passaging experiment" in colonization["description"]
    assert "qPCR transcriptional responses" in immune["description"]
    assert "not direct AMP protein" in immune["description"]
    assert reduction["name"] == "Core-20-Associated Hafnia alvei Load Reduction"
    assert immune["downstream"][0]["target"] == reduction["name"]
    assert "78-fold relative to microbiota-free" in reduction["description"]
    assert "normalized to host actin" in reduction["description"]
    assert "does not isolate richness from strain identity" in reduction["description"]


def test_unrepresented_proposals_are_disclosed_without_new_structure():
    ledger, docs = records()
    assert [len(d["ecological_interactions"]) for d in docs] == [3, 3, 3]
    assert "Direct MAG1-to-methanogen" in docs[0]["discussions"][0]["rationale"]
    assert "AA6 enrichment" in docs[1]["discussions"][0]["rationale"]
    assert "PTS-linked immune stimulation" in docs[2]["discussions"][0]["rationale"]
    assert "No new causal structure or paid Edison job" in ledger["limitations"][1]


def test_every_node_and_arrow_has_a_hash_bound_decision():
    ledger, docs = records()
    assert ledger["independent_approval"] is False and ledger["issues"] == [1497, 1498, 1499]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for row, doc in zip(ledger["records"], docs, strict=True):
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {n["node"] for n in row["node_decisions"]} == names
        assert len(row["edges_before"]) == len(row["edges_after"]) == 2
        assert len(row["retained_edge_decisions"]) == 2
        assert row["removed_node_decisions"] == row["removed_edge_decisions"] == []
        for node in doc["ecological_interactions"]:
            for edge in node.get("downstream", []):
                assert edge["target"] in names
                assert edge["description"].startswith("PARTIAL -")
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        for gap in doc["discussions"]:
            assert all(a.split("#", 1)[1] in names for a in gap["attaches_to"])
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
