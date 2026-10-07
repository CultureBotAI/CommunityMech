"""Keep observed profiles, model predictions and process outcomes distinct."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch98.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_methane_potential_is_not_measured_flux_or_vertical_transfer():
    _, _, docs = records()
    tea, acetate, depth = docs[0]["ecological_interactions"]
    assert "interaction_type" not in tea and "interaction_type" not in depth
    assert acetate["interaction_type"] == "CROSS_FEEDING"
    assert acetate["name"] == "Inferred Acetate Supply to Methanogens"
    assert "do not demonstrate acetate transport" in acetate["description"]
    assert "hydrogenotrophy uses hydrogen and carbon dioxide" in acetate["description"]
    assert len(acetate["evidence"]) == 3
    assert all(n["downstream"][0]["description"].startswith("HYPOTHESIZED:") for n in [tea, depth])


def test_root_response_is_not_mutualism_or_a_uniform_positive_chain():
    _, _, docs = records()
    decomposers, ecm, roots, _ = docs[1]["ecological_interactions"]
    assert decomposers["scope"] == "COMMUNITY_LEVEL"
    assert not any("interaction_type" in n for n in [decomposers, ecm, roots])
    assert "metabolites" not in decomposers and "biological_processes" not in decomposers
    assert "metabolites" not in ecm and "biological_processes" not in ecm
    assert "increased ectomycorrhizal colonization" in ecm["description"]
    assert all(n["downstream"][0]["description"].startswith("PARTIAL:") for n in [ecm, roots])
    assert "elevated CO2 decreased saprotroph" in ecm["downstream"][0]["description"]
    assert "reported saprotroph response is opposite" in roots["downstream"][0]["description"]


def test_viral_predictions_do_not_become_measured_predation():
    _, _, docs = records()
    virus = docs[1]["ecological_interactions"][-1]
    assert virus["scope"] == "COMMUNITY_LEVEL"
    assert "interaction_type" not in virus and "biological_processes" not in virus
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in virus["evidence"])
    assert "not direct infection, predation, cell lysis" in virus["description"]
    assert "sampled column was saturated throughout" in virus["description"]
    assert "not evidence that such infections never occur" in virus["description"]


def test_saanich_retains_model_support_without_claiming_direct_transfer():
    _, _, docs = records()
    nitrite, niche, redox = docs[2]["ecological_interactions"]
    assert nitrite["interaction_type"] == "CROSS_FEEDING"
    assert "fitted parameter" in nitrite["description"]
    assert "interaction_type" not in niche and "interaction_type" not in redox
    assert "functions co-occur" in niche["description"]
    assert len(redox["downstream"]) == 2
    assert all(e["description"].startswith("HYPOTHESIZED:") for e in redox["downstream"])


def test_detox_productivity_and_one_replicate_wax_result_remain():
    _, _, docs = records()
    detox, wax, outcome = docs[3]["ecological_interactions"]
    assert "interaction_type" not in detox
    assert "facultative mutualism" in detox["description"]
    assert wax["interaction_type"] == "CROSS_FEEDING"
    assert "only one of four" in wax["description"]
    assert "Lactic acid yield was similar" in outcome["description"]
    assert all(n["downstream"][0]["description"].startswith("PARTIAL:") for n in [detox, wax])


def test_participants_use_exact_scoped_identity_fields():
    _, _, docs = records()
    for doc, index, members in [(docs[1], 0, [0, 2]), (docs[1], 3, [3, 0]), (docs[3], 2, [0, 1])]:
        node = doc["ecological_interactions"][index]
        expected = [
            {k: doc["taxonomy"][i]["taxon_term"][k] for k in ["preferred_term", "term"]}
            for i in members
        ]
        assert node["participating_taxa"] == expected
        assert not any(k in node for k in ["source_taxon", "target_taxon", "interaction_type"])


def test_all_nodes_directions_and_history_have_dispositions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 13
    assert sum(len(r["renamed_nodes"]) for r in rows) == 4
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 8
    assert len(ledger["snippet_checks"]) == ledger["primary_graph_snippet_count"] == 24
    assert len(ledger["discussion_snippet_checks"]) == 4
    for row, doc in zip(rows, docs, strict=True):
        assert row["removed_node_decisions"] == row["removed_edge_decisions"] == []
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"])
        assert row["curation_events_added"] == (
            2 if doc["id"] in ["CommunityMech:000140", "CommunityMech:000263"] else 1
        )
        assert doc["curation_history"][-1]["llm_assisted"]
        assert (ROOT / row["history_files"][0]).is_file()
        for e in row["retained_edge_decisions"]:
            assert all(
                row["renamed_nodes"].get(e["before"][k], e["before"][k]) == e["after"][k]
                for k in ["source", "target"]
            )


def test_unresolved_scope_and_source_access_are_explicit():
    ledger, _, _ = records()
    assert ledger["issues"] == [1778, 1779, 1780, 1781]
    assert ledger["unresolved_non_graph_issues"] == [1782]
    assert ledger["cache_changes"] == [] and not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )
    assert any("403" in s for s in ledger["limitations"])
    assert any("HTTP500" in s for s in ledger["limitations"])
