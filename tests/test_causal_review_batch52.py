"""Keep genomic and proteomic observations separate from untested mediation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-urls-amd-proteome-batch52.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in ledger["records"]]


def canonical(doc, indices):
    return [
        {
            "preferred_term": doc["taxonomy"][i]["taxon_term"]["preferred_term"],
            "term": doc["taxonomy"][i]["taxon_term"]["term"],
        }
        for i in indices
    ]


def test_urls_keep_distinct_habitat_participants_without_contextual_arrows():
    _, (doc, _, _) = records()
    nodes = doc["ecological_interactions"]
    for node, indexes in zip(nodes, [[0, 1], [0, 1], [0], [0]], strict=True):
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert node["participating_taxa"] == canonical(doc, indexes)
        assert not node.get("downstream")
        assert not {"source_taxon", "target_taxon"} & node.keys()
    participants = nodes[0]["participating_taxa"]
    assert participants[0]["term"]["id"] == participants[1]["term"]["id"]
    assert participants[0]["preferred_term"] != participants[1]["preferred_term"]
    assert all("interaction_type" not in nodes[i] for i in [0, 1, 3])
    assert nodes[2]["interaction_type"] == "CROSS_FEEDING"
    assert nodes[2]["description"].startswith("PARTIAL -")
    assert "simultaneous sulfate reduction and hydrogen export" in nodes[2]["description"]


def test_urls_bound_genomic_functions_and_replication_estimates():
    _, (doc, _, _) = records()
    sites, functions, _, genotypes = doc["ecological_interactions"]
    assert "not an isolated lithology effect" in sites["description"]
    assert "coding potential" in functions["description"]
    assert "not measurement of pathway expression" in functions["description"]
    assert functions["evidence"][0]["supports"] == "SUPPORT"
    assert functions["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert "Coverage-qualified iRep" in genotypes["description"]
    assert "not direct absolute growth rates" in genotypes["description"]
    assert genotypes["evidence"][1]["supports"] == "PARTIAL"


def test_hualgayoc_preserves_existing_participant_subsets_and_partial_flux():
    _, (_, doc, _) = records()
    glycerol, acetate = doc["ecological_interactions"]
    assert glycerol["participating_taxa"] == canonical(doc, [0])
    assert acetate["participating_taxa"] == canonical(doc, [0, 1])
    for node in [glycerol, acetate]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert node["interaction_type"] == "CROSS_FEEDING"
        assert node["description"].startswith("PARTIAL -")
        assert all(ev["supports"] == "PARTIAL" for ev in node["evidence"])
    assert "both dominant MAGs encode" in glycerol["description"]
    assert "days 32 and 86" in glycerol["description"]
    assert "residual acetate remained" in acetate["description"]
    assert "selectively established pH threshold" in acetate["description"]
    assert doc["discussions"][0]["discussion_id"] == "HUALGAYOC_MINOR_ACIDOGENS"


def test_hualgayoc_extension_remains_unresolved_after_existing_graph_repairs():
    ledger, (_, doc, _) = records()
    assert ledger["records"][1]["status"] == "needs_research"
    assert ledger["unresolved_research_issues"] == [1504]
    assert [row["status"] for row in ledger["records"]] == [
        "reviewed",
        "needs_research",
        "reviewed",
    ]
    rationale = doc["discussions"][-1]["rationale"]
    assert "positive sulfate-reducing chemistry" in rationale
    assert "Bulk 16S rRNA transcripts were measured" in rationale
    assert "dry run succeeded without API calls or charges" in rationale
    assert "#1504" in rationale and "#816" in rationale


def test_proteome_positive_controls_and_exact_yield_benchmark_are_preserved():
    _, (_, _, doc) = records()
    expression, overlap, productivity = doc["ecological_interactions"]
    for node in [expression, overlap, productivity]:
        assert node["participating_taxa"] == canonical(doc, range(4))
        assert not {"interaction_type", "source_taxon", "target_taxon"} & node.keys()
        assert node["evidence"][0]["supports"] == "SUPPORT"
    assert "Abundance-matched mixed-isolate" in expression["description"]
    assert "Both community context and carbon source" in expression["description"]
    assert "Pooled human/rumen" in expression["description"]
    assert "does not directly measure competition" in overlap["description"]
    assert all("not a measured interspecies exchange" in t["notes"] for t in overlap["metabolites"])
    assert "divided by mean monoculture abundance" in productivity["description"]
    assert "not the sum or best monoculture" in productivity["description"]
    assert "does not demonstrate reciprocal benefit" in productivity["description"]


def test_every_node_and_arrow_has_a_hash_bound_decision():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1501, 1502, 1503]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for index, (row, doc) in enumerate(zip(ledger["records"], docs, strict=True)):
        nodes = doc["ecological_interactions"]
        names = {node["name"] for node in nodes}
        assert len(nodes) == [4, 2, 3][index]
        assert {decision["node"] for decision in row["node_decisions"]} == names
        assert len(row["edges_before"]) == [2, 1, 2][index]
        assert len(row["retained_edge_decisions"]) == [0, 1, 2][index]
        assert len(row["removed_edge_decisions"]) == [2, 0, 0][index]
        assert row["removed_node_decisions"] == []
        for node in nodes:
            for edge in node.get("downstream", []):
                assert edge["target"] in names
                assert edge["description"].startswith("PARTIAL -")
        for gap in doc["discussions"]:
            for anchor in gap["attaches_to"]:
                if anchor.startswith("ecological_interactions#"):
                    assert anchor.split("#", 1)[1] in names
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
