"""Keep process outcomes and omics responses distinct from proven mediation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch108.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_tobacco_preserves_measured_outcomes_without_reciprocal_fitness():
    _, _, docs = records()
    degradation, succession, outcome = docs[0]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [degradation, succession, outcome])
    assert all(value in degradation["description"] for value in ["52.48%", "56.36%", "68.47%"])
    assert "uninoculated control" in degradation["description"]
    assert "relative abundance" in succession["description"]
    assert "31 differentially" in outcome["evidence"][0]["snippet"]
    assert "reducing irritancy" in outcome["evidence"][1]["snippet"]
    assert "biological_processes" not in outcome


def test_tobacco_path_model_is_bounded_and_directions_stay_hypotheses():
    _, _, docs = records()
    degradation, succession, outcome = docs[0]["ecological_interactions"]
    model = succession["evidence"][1]
    assert model["evidence_source"] == "COMPUTATIONAL" and model["supports"] == "PARTIAL"
    provenance = model["computational_provenance"]
    assert provenance["prediction_type"] == "STATISTICAL_INFERENCE"
    assert "PLS-PM" in provenance["parameters"] and "tools" not in provenance
    for node in [degradation, succession]:
        assert node["downstream"][0]["target"] == outcome["name"]
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert "beta-diversity variable" in succession["downstream"][0]["description"]


def test_chlorella_workflows_are_context_not_graph_nodes_or_arrows():
    _, rows, docs = records()
    nodes = docs[1]["ecological_interactions"]
    assert len(nodes) == 3
    assert all("interaction_type" not in n and not n.get("downstream") for n in nodes)
    assert {r["node"] for r in rows[1]["removed_node_decisions"]} == {
        "Sequential SynCom-Microalga Coupling Construction",
        "Sixty-Day Stable Slurry Operation",
    }
    assert len(rows[1]["removed_edge_decisions"]) == 3
    assert all(
        value in nodes[0]["description"] for value in ["60 days", "94.41%", "81.84%", "6.31%"]
    )
    assert len(docs[1]["curation_history"]) == 2
    assert "construction-to-operation workflow edge" in docs[1]["curation_history"][0]["changes"]


def test_chlorella_comparator_and_algal_scope_are_explicit():
    _, _, docs = records()
    doc = docs[1]
    removal, growth, transcript = doc["ecological_interactions"]
    assert "BG11 comparison" in growth["description"]
    assert "27.15%" in growth["description"] and "488.10%" in growth["description"]
    assert "metabolites" not in growth
    expected = [{k: doc["taxonomy"][0]["taxon_term"][k] for k in ["preferred_term", "term"]}]
    assert growth["participating_taxa"] == transcript["participating_taxa"] == expected
    assert "participating_taxa" not in removal
    assert "does not measure enzyme activity" in transcript["description"]


def test_metg2_omics_and_identity_gaps_are_not_certified_as_mechanisms():
    ledger, rows, docs = records()
    colonization, functions, host = docs[2]["ecological_interactions"]
    assert rows[2]["status"] == "needs_research" and ledger["unresolved_research_issues"] == [1847]
    assert all(
        not any(k in n for k in ["interaction_type", "source_taxon", "target_taxon"])
        for n in [colonization, functions, host]
    )
    assert not colonization.get("downstream")
    assert colonization["evidence"][0]["supports"] == "PARTIAL"
    assert len(functions["evidence"]) == 1
    assert functions["downstream"][0]["target"] == host["name"]
    assert functions["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert "antioxidant-related genes were also induced" in host["evidence"][1]["snippet"]
    assert "Saccharum officinarum grounding" in host["description"]
    assert "four MetG2 strains" in docs[2]["discussions"][-1]["rationale"]


def test_artemisia_preserves_traits_without_inventing_niches_or_assay_setting():
    _, _, docs = records()
    tolerance, complementarity, capacity = docs[3]["ecological_interactions"]
    assert "Cadmium tolerance" in tolerance["name"] and "2 mM" in tolerance["description"]
    assert all(
        "interaction_type" not in n and not n.get("downstream")
        for n in [tolerance, complementarity, capacity]
    )
    assert complementarity["scope"] == "PAIRWISE"
    assert complementarity["evidence"][0]["supports"] == "PARTIAL"
    assert all(
        e["evidence_source"] == "OTHER"
        for n in [tolerance, complementarity, capacity]
        for e in n["evidence"]
    )
    assert "carbon fixation capacity" in capacity["evidence"][0]["snippet"]
    assert "measured sequestration flux" in capacity["description"]
    assert len(docs[3]["curation_history"]) == 2
    assert "Removed two downstream edges" in docs[3]["curation_history"][0]["changes"]


def test_every_original_node_and_direction_has_a_disposition_without_extensions():
    ledger, rows, docs = records()
    assert sum(len(d["ecological_interactions"]) for d in docs) == 12
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 2
    assert sum(len(r["edges_before"]) for r in rows) == 7
    assert sum(len(r["edges_after"]) for r in rows) == 3
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 4
    assert sum(len(r["renamed_nodes"]) for r in rows) == 7
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["unresolved_non_graph_issues"] == [183]


def test_hashes_append_only_histories_and_discussion_schema_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert [r["status"] for r in rows] == ["reviewed", "reviewed", "needs_research", "reviewed"]
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).exists()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert all(
            e["target"] in names
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        )
        assert all(
            "computational_provenance" not in e for d in doc["discussions"] for e in d["evidence"]
        )
