"""Guard observation/mechanism, comparator and member-scope boundaries."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch105.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_colony_recovery_does_not_assert_competition_or_viability_loss():
    _, _, docs = records()
    (node,) = docs[0]["ecological_interactions"]
    assert "interaction_type" not in node and not node.get("downstream")
    assert "not definitive loss of viability" in node["description"]
    assert "reciprocal negative effects" in node["description"]
    assert node["participating_taxa"][0]["preferred_term"] == "Bacillus subtilis W2-B1-K4"
    assert len(node["evidence"]) == 2
    assert "confirmed metabolite activity" in docs[0]["discussions"][-1]["evidence"][1]["snippet"]


def test_phenanthrene_pot_outcomes_keep_observed_support():
    _, _, docs = records()
    removal, carbon = docs[1]["ecological_interactions"]
    assert "90.02%" in removal["description"] and "81.07%" in removal["description"]
    for node in [removal, carbon]:
        assert node["evidence"][0]["supports"] == "SUPPORT"
        assert node["evidence"][0]["evidence_source"] == "IN_VIVO"
        assert not node.get("downstream")


def test_carbon_stocks_and_models_do_not_become_fixation_flux():
    _, _, docs = records()
    carbon = docs[1]["ecological_interactions"][1]
    assert "metabolites" not in carbon and "biological_processes" not in carbon
    assert "do not themselves quantify carbon-fixation flux" in carbon["description"]
    model = carbon["evidence"][1]
    assert model["supports"] == "PARTIAL" and model["evidence_source"] == "COMPUTATIONAL"
    provenance = model["computational_provenance"]
    assert provenance["prediction_type"] == "STATISTICAL_INFERENCE"
    assert [t["tool_name"] for t in provenance["tools"]] == [
        "random forest model",
        "partial least-squares path modeling",
    ]
    assert all("version" not in t for t in provenance["tools"])


def test_lignin_conversion_preserves_gallate_qualification_and_identity():
    _, _, docs = records()
    coupling, conversion, substrates = docs[2]["ecological_interactions"]
    assert len(coupling["evidence"]) == 1
    assert coupling["evidence"][0]["supports"] == "PARTIAL"
    assert "HYPOTHESIZED:" in coupling["description"]
    assert "simultaneous production" in conversion["description"]
    assert "showed potential" in conversion["evidence"][1]["snippet"]
    assert conversion["metabolites"][1]["term"] == {"id": "CHEBI:16918", "label": "gallate"}
    assert all("interaction_type" not in n for n in [coupling, conversion, substrates])


def test_lignin_retains_only_the_qualified_existing_causal_direction():
    _, _, docs = records()
    coupling, conversion, substrates = docs[2]["ecological_interactions"]
    (edge,) = coupling["downstream"]
    assert edge["target"] == conversion["name"]
    assert edge["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert not conversion.get("downstream") and not substrates.get("downstream")
    assert "substrate-range evidence" in substrates["description"]


def test_manure_comparators_and_member_transcripts_stay_separate():
    _, _, docs = records()
    doc = docs[3]
    broth, plant, transcripts = doc["ecological_interactions"]
    assert "monoculture, simultaneous co-culture" in broth["description"]
    assert "41.4% versus the water control" in plant["description"]
    assert all(e["evidence_source"] == "IN_VIVO" for e in plant["evidence"])
    assert transcripts["participating_taxa"] == [
        {k: doc["taxonomy"][0]["taxon_term"][k] for k in ["preferred_term", "term"]}
    ]
    assert "not demonstrated protein activity" in transcripts["description"]
    assert all(not n.get("downstream") for n in doc["ecological_interactions"])


def test_all_original_nodes_and_directions_have_dispositions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 9
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 0
    assert sum(len(r["renamed_nodes"]) for r in rows) == 3
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 1
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["status"] == "reviewed"
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"]
    assert ledger["primary_graph_snippet_count"] == len(ledger["snippet_checks"]) == 17
    assert len(ledger["discussion_snippet_checks"]) == 5
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )


def test_followups_and_provider_scope_are_not_silently_resolved():
    ledger, _, _ = records()
    assert ledger["issues"] == [1823, 1824, 1825, 1826]
    assert ledger["unresolved_non_graph_issues"] == [1827]
    assert ledger["unresolved_research_issues"] == []
    assert not ledger["independent_approval"]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["issue_deduplication"]["matching_issues"] == [771, 847, 848]
