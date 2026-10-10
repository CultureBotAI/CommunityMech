"""Distinguish recipient processes, conditional support and sulfide inhibition."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch30.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def assert_intrinsic(node, taxon):
    assert node["scope"] == "PAIRWISE"
    assert node["source_taxon"]["term"]["id"] == taxon
    assert not {"target_taxon", "participating_taxa", "interaction_type"} & node.keys()


def test_lactate_recipient_activity_and_conditional_sulfide_inhibition():
    _, docs = records()
    fermentation, output, inhibition = docs[0]["ecological_interactions"]
    assert_intrinsic(output, "NCBITaxon:243164")
    assert "maximum dechlorination rate, not every growth endpoint" in output["description"]
    assert fermentation["interaction_type"] == "SYNTROPHY"
    assert "not establish that DvH supplies every required cofactor" in fermentation["description"]
    assert inhibition["name"] == "Sulfide-Associated Inhibition Of Dechlorination"
    assert "interaction_type" not in inhibition
    assert inhibition["source_taxon"]["term"]["id"] == "NCBITaxon:882"
    assert inhibition["target_taxon"]["term"]["id"] == "NCBITaxon:243164"
    assert (
        "Donor-limited butyrate-triculture and enrichment outcomes are separate"
        in inhibition["description"]
    )
    assert "despite available hydrogen" in inhibition["downstream"][0]["description"]
    assert (
        "not sufficient evidence that hydrogen competition caused"
        in inhibition["downstream"][0]["description"]
    )
    for node in [fermentation, inhibition]:
        assert node["downstream"][0]["target"] == output["name"]


def test_pelosinus_remodeling_belongs_to_recipient_and_expression_is_measured():
    _, docs = records()
    hydrogen, provision, remodeling, output = docs[1]["ecological_interactions"]
    assert_intrinsic(remodeling, "NCBITaxon:243164")
    assert remodeling["evidence"][1]["evidence_source"] == "IN_VITRO"
    assert "not a selective gene-necessity experiment" in remodeling["evidence"][1]["explanation"]
    assert "PfR7 can also form some cobalamin" in provision["description"]
    assert "Externally supplied lower ligand" in provision["metabolites"][1]["notes"]
    assert hydrogen["interaction_type"] == "SYNTROPHY"
    assert provision["interaction_type"] == "CROSS_FEEDING"
    assert output["scope"] == "COMMUNITY_LEVEL"
    assert "interaction_type" not in output
    assert {t["term"]["id"] for t in output["participating_taxa"]} == {
        "NCBITaxon:243164",
        "NCBITaxon:882",
        "NCBITaxon:1122947",
    }


def test_pelosinus_all_retained_arrows_expose_the_dmb_condition():
    _, docs = records()
    hydrogen, provision, remodeling, output = docs[1]["ecological_interactions"]
    for node in [hydrogen, provision, remodeling]:
        assert len(node["downstream"]) == 1
        assert "DMB" in node["downstream"][0]["description"]
    assert hydrogen["downstream"][0]["target"] == output["name"]
    assert provision["downstream"][0]["target"] == remodeling["name"]
    assert remodeling["downstream"][0]["target"] == output["name"]
    assert "when DMB is supplied" in output["description"]
    assert "does not selectively separate" in remodeling["downstream"][0]["description"]


def test_fusaro_compatibility_failure_is_not_toxicity_or_reverse_exchange():
    _, docs = records()
    support, insufficient, output = docs[2]["ecological_interactions"]
    assert_intrinsic(output, "NCBITaxon:216389")
    assert support["interaction_type"] == "CROSS_FEEDING"
    assert "not endogenous DMB supply or reciprocal nutrient exchange" in support["description"]
    assert "interaction_type" not in insufficient and "metabolites" not in insufficient
    assert "not commensalism, active factor-III toxicity" in insufficient["description"]
    assert "not active inhibition by factor III" in insufficient["downstream"][0]["description"]
    assert (
        "direct compatible-cobalamin supplementation"
        in insufficient["downstream"][0]["description"]
    )
    for node in [support, insufficient]:
        assert node["downstream"][0]["target"] == output["name"]
    assert "Pooled BAV1, GT and FL2 responses are not all assigned" in output["description"]


def test_batch30_canonical_sources_participants_and_exact_anchors():
    _, docs = records()
    for doc in docs:
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


def test_batch30_preserves_topology_and_records_all_decisions_history_and_limits():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1382, 1383, 1384]
    assert ledger["open_nongraph_followups"] == [1385, 1386]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 10
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 7
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert row["status"] == "reviewed" and row["outcome"] == "changed"
        assert not row["removed_node_decisions"] and not row["removed_edge_decisions"]
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        renames = row["renamed_nodes"]
        assert {(e["source"], e["target"]) for e in row["edges_after"]} == {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
    assert (
        "Full body not retrieved" in ledger["records"][0]["source_review"]["PMID:21881617"]["scope"]
    )
    assert (
        "Not complete full text" in ledger["records"][2]["source_review"]["PMID:23479750"]["scope"]
    )
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
