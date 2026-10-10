"""Pin study scope, iron-oxidizer assignments and positive biofilm interventions."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = (
    ROOT / "reports/causal_graph_review/decisions/20261006-pitlakes-bioleach-biofilm-batch53.yaml"
)


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


def test_all_nodes_use_explicit_canonical_community_participants():
    _, docs = records()
    subsets = [
        [[0, 1, 4, 2], [3, 4], [7], [5], [6]],
        [[0], [0], [6], [1, 3], [0, 6], [4], [7], [2, 1], [5, 3]],
        [list(range(4)), [3, 2], list(range(4))],
    ]
    for doc, expected in zip(docs, subsets, strict=True):
        for node, indexes in zip(doc["ecological_interactions"], expected, strict=True):
            assert node["scope"] == "COMMUNITY_LEVEL"
            assert node["participating_taxa"] == canonical(doc, indexes)
            assert not {"source_taxon", "target_taxon", "interaction_type"} & node.keys()


def test_pit_lake_findings_keep_site_scope_without_cross_site_arrows():
    _, (doc, _, _) = records()
    iron, sulfur, algae, archaea, methane = doc["ecological_interactions"]
    assert all(not n.get("downstream") for n in doc["ecological_interactions"])
    assert "NSC/Concepcion" in iron["description"]
    assert "precipitated sulfides, not dissolved sulfides" in sulfur["description"]
    assert "not demonstrated pairwise syntrophy" in sulfur["description"]
    assert "did not infer that organic carbon was necessarily" in algae["description"]
    assert "not measured methane production" in methane["description"]
    assert all(
        "concentration" not in term
        for node in doc["ecological_interactions"]
        for term in node.get("metabolites", [])
    )
    assert [p["term"]["id"] for p in sulfur["biological_processes"]] == ["GO:0019420"]
    assert [p["term"]["id"] for p in archaea["biological_processes"]] == ["GO:0019418"]
    assert all(m["term"]["id"] != "CHEBI:29033" for m in algae["metabolites"])


def test_bioleaching_preserves_population_and_yield_results_not_false_iron_owner():
    _, (_, doc, _) = records()
    early, _, middle, _, output, _, lepto, _, _ = doc["ecological_interactions"]
    assert early["name"] == "Initial Acidithiobacillus caldus Predominance"
    assert "metabolites" not in early and "biological_processes" not in early
    assert "does not identify A. caldus as a ferrous-iron oxidizer" in early["description"]
    assert "S. acidophilus rather than A. caldus" in middle["evidence"][0]["snippet"]
    assert "60.4 percent" in output["description"]
    assert "more than two years" in output["description"]
    assert "supported subset, not the complete culture" in output["description"]
    assert "60.4% of copper" in output["evidence"][0]["snippet"]
    assert "does not prove extinction" in lepto["description"]
    assert all(not n.get("downstream") for n in doc["ecological_interactions"])


def test_bioleaching_genomic_capabilities_do_not_substitute_for_other_study_taxa():
    ledger, (_, doc, _) = records()
    _, sulfur, _, late, _, organic, _, ferro, temperature = doc["ecological_interactions"]
    assert sulfur["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert "2014 F. thermophilum" in late["description"]
    assert "biological_processes" not in organic
    assert "not measured transfer" in organic["description"]
    assert "do not demonstrate functional redundancy" in ferro["description"]
    assert "single reactor runs per condition" in temperature["description"]
    assert ledger["records"][1]["status"] == "needs_research"
    assert ledger["unresolved_research_issues"] == [1509]
    assert "#1509" in doc["discussions"][-1]["rationale"]


def test_milk_preserves_both_positive_genetic_intervention_arrows():
    _, (_, _, doc) = records()
    network, inhibition, robustness = doc["ecological_interactions"]
    assert [e["target"] for e in inhibition["downstream"]] == [
        network["name"],
        robustness["name"],
    ]
    assert "positive genetic evidence" in inhibition["description"]
    assert "about 50-fold" in inhibition["description"]
    assert "mainly pellet-associated or unstable" in inhibition["description"]
    assert "did not report complementation" in inhibition["description"]
    assert all(ev["supports"] == "SUPPORT" for ev in inhibition["evidence"])
    assert "causal contribution" in inhibition["downstream"][0]["description"]
    assert "genetic intervention supports" in inhibition["downstream"][1]["description"]


def test_milk_robustness_is_an_establishment_endpoint_not_universal_recovery():
    _, (_, _, doc) = records()
    network, _, robustness = doc["ecological_interactions"]
    assert "laboratory substitution" in network["description"]
    assert "72-hour compositions" in robustness["description"]
    assert "not a recovery time course" in robustness["description"]
    assert (
        "Neither community resisted strong continuous changes uniformly"
        in robustness["description"]
    )
    assert doc["taxonomy"][1]["strain_designation"]["strain_name"] == "CLL49"
    assert "#529" in doc["discussions"][-1]["rationale"]


def test_source_excerpt_update_keeps_original_cache_prefix_and_provenance():
    ledger, _ = records()
    update = ledger["reference_cache_update"]
    raw = (ROOT / update["path"]).read_bytes()
    original, marker, extra = raw.partition(b"\n\n## Primary-Source Excerpts (2026-10-06)")
    assert marker and extra
    assert hashlib.sha256(original).hexdigest() == update["original_sha256"]
    assert hashlib.sha256(raw).hexdigest() == update["updated_sha256"]
    assert update["primary_xml_sha256"].encode() in extra
    assert b"CC BY 4.0" in extra
    assert b"not a complete full-text cache" in extra
    assert sum(len(q.split()) for q in update["verified_excerpts"]) == update["quoted_words"] == 24
    assert all(q.encode() in extra for q in update["verified_excerpts"])


def test_every_node_and_arrow_has_a_hash_bound_decision_and_history():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1506, 1507, 1508]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for index, (row, doc) in enumerate(zip(ledger["records"], docs, strict=True)):
        nodes = doc["ecological_interactions"]
        names = {n["name"] for n in nodes}
        assert len(nodes) == [5, 9, 3][index]
        assert {d["node"] for d in row["node_decisions"]} == names
        assert row["removed_node_decisions"] == []
        assert len(row["edges_before"]) == [3, 3, 2][index]
        assert len(row["retained_edge_decisions"]) == [0, 0, 2][index]
        assert len(row["removed_edge_decisions"]) == [3, 3, 0][index]
        for node in nodes:
            for edge in node.get("downstream", []):
                assert edge["target"] in names
        for discussion in doc["discussions"]:
            assert all(a.split("#", 1)[1] in names for a in discussion["attaches_to"])
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
