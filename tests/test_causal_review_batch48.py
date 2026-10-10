"""Keep positive consortium outcomes distinct from unmeasured mechanisms."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-ginseng-s11-batch48.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_cl95_retains_distinct_strains_and_external_participants():
    _, (doc, _) = records()
    for index, node in enumerate(doc["ecological_interactions"]):
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert not {"interaction_type", "source_taxon", "target_taxon", "downstream"} & node.keys()
        assert len(node["participating_taxa"]) == 6
        members = node["participating_taxa"][:5]
        assert [p["term"] for p in members] == [t["taxon_term"]["term"] for t in doc["taxonomy"]]
        assert members[0]["term"] == members[1]["term"]
        assert members[0]["preferred_term"] != members[1]["preferred_term"]
        expected = "NCBITaxon:1079257" if index == 0 else "NCBITaxon:4054"
        assert node["participating_taxa"][-1]["term"]["id"] == expected


def test_cl95_positive_phenotypes_do_not_prove_mediation_or_nutrient_flux():
    _, (doc, _) = records()
    suppression, growth, _ = doc["ecological_interactions"]
    assert "66.67%" in suppression["description"] and "73%" in suppression["description"]
    assert "not necessarily viable pathogen" in suppression["description"]
    assert "not selectively manipulated" in suppression["description"]
    assert "13.00, 15.50 and 19.00 mm" in growth["description"]
    assert "not measurements of nutrient flux" in growth["description"]
    assert "metabolites" not in growth
    assert suppression["biological_processes"][0]["term"]["id"] == "GO:0044419"
    assert growth["biological_processes"][0]["term"]["id"] == "GO:0040007"


def test_cl95_marker_recovery_and_enzyme_response_keep_their_assay_limits():
    _, (doc, _) = records()
    node = doc["ecological_interactions"][2]
    assert "NJ13, NT35 and FG14" in node["description"]
    assert "do not independently track all five" in node["description"]
    assert "do not directly track individual cells" in node["description"]
    assert "do not identify their producing organism" in node["description"]
    assert node["biological_processes"][0]["term"]["id"] == "GO:0044419"
    assert "180% catalase" in node["evidence"][1]["explanation"]
    gap = doc["discussions"][0]
    assert "defense transcription is positive host-response evidence" in gap["rationale"]
    assert gap["status"] == "OPEN"


def test_s11_removal_is_not_reciprocal_fitness_or_resolved_flux():
    _, (_, doc) = records()
    (node,) = doc["ecological_interactions"]
    assert node["scope"] == "COMMUNITY_LEVEL"
    assert not {"interaction_type", "biological_processes", "downstream"} & node.keys()
    assert [p["term"] for p in node["participating_taxa"]] == [
        t["taxon_term"]["term"] for t in doc["taxonomy"]
    ]
    assert {m["term"]["id"] for m in node["metabolites"]} == {"CHEBI:28938", "CHEBI:16301"}
    assert "95% ammonium-N and 97% nitrite-N" in node["description"]
    assert "heterotrophic nitrification-aerobic denitrification" in node["description"]
    assert "does not partition consortium removal" in node["description"]
    assert "residual nitrite fractions are not removal percentages" in node["description"]
    assert doc["discussions"][-1]["status"] == "OPEN"


def test_s11_shared_evidence_and_prior_environment_fix_survive():
    _, (_, doc) = records()
    strain = doc["engineering_design"]["evidence"][0]
    assert strain is doc["taxonomy"][0]["evidence"][0]
    assert strain is doc["taxonomy"][1]["evidence"][0]
    design = doc["engineering_design"]["evidence"][1]
    graph = doc["ecological_interactions"][0]["evidence"][0]
    assert design is not graph
    assert design["explanation"].endswith("synergistic nitrogen-removal phenotype.")
    assert graph["snippet"] == design["snippet"]
    assert "not reciprocal fitness" in graph["explanation"]
    assert doc["modeled_environment"][0]["term"]["id"] == "ENVO:00002001"


def test_every_original_node_and_arrow_has_a_hash_bound_decision():
    ledger, docs = records()
    assert ledger["review_mode"] == "source_based_self_adversarial_review"
    assert ledger["independent_approval"] is False and ledger["issues"] == [1487, 1488]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert row["status"] == "reviewed"
        assert [n["node"] for n in row["node_decisions"]] == [
            n["name"] for n in doc["ecological_interactions"]
        ]
        assert (
            row["removed_node_decisions"]
            == row["edges_after"]
            == row["retained_edge_decisions"]
            == []
        )
        assert len(row["removed_edge_decisions"]) == len(row["edges_before"])
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        names = {n["name"] for n in doc["ecological_interactions"]}
        for gap in doc["discussions"]:
            assert all(a.split("#", 1)[1] in names for a in gap["attaches_to"] if "#" in a)
    assert sum(len(r["edges_before"]) for r in ledger["records"]) == 1
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    assert "abstract only" in ledger["records"][1]["source_review"]["PMID:41260371"]["scope"]
