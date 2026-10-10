"""Keep assay observations, strain mechanisms and field hypotheses distinct."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch29.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_syncom35_preserves_immune_observations_without_invented_exchanges():
    _, docs = records()
    immune, wrky, secretion, colonization = docs[0]["ecological_interactions"]
    assert immune["scope"] == wrky["scope"] == "COMMUNITY_LEVEL"
    assert len(immune["participating_taxa"]) == len(wrky["participating_taxa"]) == 2
    assert "not the complete 35-strain roster" in immune["description"]
    assert "not a demonstrated MF79-specific WRKY mechanism" in wrky["description"]
    assert wrky["evidence"][0]["supports"] == "PARTIAL"
    assert "not validated by the abstract snippet" in (
        yaml.safe_load(LEDGER.read_text())["records"][0]["source_review"]["PMID:33879573"]["scope"]
    )
    assert secretion["scope"] == "PAIRWISE"
    assert secretion["source_taxon"]["term"]["id"] == "NCBITaxon:231455"
    assert secretion["target_taxon"]["term"]["id"] == "NCBITaxon:3702"
    assert "not assigned to every SynCom35 member" in secretion["description"]
    assert all("interaction_type" not in n for n in [immune, wrky, secretion])
    assert colonization["scope"] == "COMMUNITY_LEVEL"
    assert colonization["interaction_type"] == "COLONIZATION_FACILITATION"
    assert len(colonization["participating_taxa"]) == 3
    assert "not a proven MF79/Pseudomonas mutualism" in colonization["description"]


def test_syncom35_two_arrows_keep_experiment_specific_scope():
    _, docs = records()
    immune, wrky, secretion, colonization = docs[0]["ecological_interactions"]
    (upstream,) = secretion["downstream"]
    (downstream,) = immune["downstream"]
    assert upstream["target"] == immune["name"]
    assert "not necessity of T2SS for the entire SynCom35 phenotype" in upstream["description"]
    assert downstream["target"] == colonization["name"]
    assert "Ochrobactrum MF370" in downstream["description"]
    assert "unlike T2SS-mutant material" in downstream["description"]
    assert "downstream" not in wrky and "downstream" not in colonization


def test_deepwater_retains_positive_results_with_two_qualified_arrows():
    _, docs = records()
    degradation, floc, partition = docs[1]["ecological_interactions"]
    assert all(n["scope"] == "COMMUNITY_LEVEL" for n in [degradation, floc, partition])
    assert all("interaction_type" not in n for n in [degradation, floc, partition])
    assert "potential" in degradation["description"]
    assert "not a distinct oxygen-conservation mechanism" in degradation["description"]
    assert "downstream" not in degradation
    assert degradation["evidence"][1]["supports"] == "PARTIAL"
    assert "separate positive result" in floc["description"]
    assert "room temperature without added dispersant" in partition["description"]
    assert "alternative to unknown enzymes or incomplete assemblies" in partition["description"]
    assert partition["evidence"][-1]["evidence_source"] == "IN_VITRO"
    assert partition["evidence"][-1]["supports"] == "SUPPORT"
    for node in [floc, partition]:
        (arrow,) = node["downstream"]
        assert arrow["target"] == degradation["name"]
        assert arrow["description"].startswith("HYPOTHESIZED -")
    assert len(partition["participating_taxa"]) == 4
    assert "NCBITaxon:40222" not in {t["term"]["id"] for t in partition["participating_taxa"]}


def test_enamel_preserves_treatment_endpoints_not_crossfeeding_or_competition():
    _, docs = records()
    formation, counts, minerals = docs[2]["ecological_interactions"]
    for node in [formation, counts, minerals]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert len(node["participating_taxa"]) == 4
        assert not {"interaction_type", "source_taxon", "target_taxon", "downstream"} & node.keys()
    assert "S. sanguinis was below detection in the calcium arms" in formation["description"]
    assert "calcium did not significantly change total counts or S. mutans" in counts["description"]
    assert "not a selectively perturbed mechanism" in counts["description"]
    assert "not every mineral-loss endpoint" in minerals["description"]
    assert "biological_processes" not in minerals
    assert "Results prose and Table 2 superscripts differ" in docs[2]["discussions"][0]["rationale"]


def test_batch29_uses_only_canonical_participants_and_valid_discussion_anchors():
    _, docs = records()
    for doc in docs:
        canonical = {t["taxon_term"]["term"]["id"]: t["taxon_term"] for t in doc["taxonomy"]}
        names = {n["name"] for n in doc["ecological_interactions"]}
        for node in doc["ecological_interactions"]:
            for term in node.get("participating_taxa", []):
                original = canonical[term["term"]["id"]]
                assert term == {k: original[k] for k in ["preferred_term", "term"]}
        assert len(doc["discussions"]) == 1
        (gap,) = doc["discussions"]
        assert gap["kind"] == "KNOWLEDGE_GAP" and gap["status"] == "OPEN"
        assert set(gap["attaches_to"]) == {"ecological_interactions#" + name for name in names}


def test_batch29_accounts_for_removed_nodes_edges_histories_and_cache_preservation():
    ledger, docs = records()
    rows = ledger["records"]
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1375, 1376, 1377]
    assert ledger["open_nongraph_followups"] == [1378, 1379, 1380]
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 4
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 3
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 4
    for row, doc in zip(rows, docs, strict=True):
        assert row["status"] == "reviewed" and row["outcome"] == "changed"
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        names = [n["name"] for n in doc["ecological_interactions"]]
        assert Counter(n["node"] for n in row["node_decisions"]) == Counter(names)
        arrows = [
            {"source": n["name"], **e}
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        ]
        assert arrows == row["edges_after"]
        removed = {(e["source"], e["target"]) for e in row["removed_edge_decisions"]}
        rename = row["renamed_nodes"]
        assert {(e["source"], e["target"]) for e in arrows} == {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["edges_before"]
            if (e["source"], e["target"]) not in removed
        }
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
