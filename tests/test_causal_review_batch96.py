"""Keep field outcomes, ecological effects and model predictions distinct."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch96.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_rifle_removal_is_initial_not_sulfide_extension():
    _, rows, docs = records()
    early, removal, sulfate, succession = docs[0]["ecological_interactions"]
    assert early["downstream"][0]["target"] == removal["name"]
    assert succession["downstream"][0]["target"] == sulfate["name"]
    assert all(
        n["downstream"][0]["description"].startswith("PARTIAL:") for n in [early, succession]
    )
    assert "downstream" not in sulfate
    assert "uranium increased" in sulfate["description"]
    assert "increase in uranium" in sulfate["evidence"][1]["snippet"]
    assert "HYPOTHESIZED:" in succession["description"]
    assert len(rows[0]["removed_node_decisions"]) == len(rows[0]["removed_edge_decisions"]) == 2


def test_rifle_wrong_systems_do_not_certify_membership():
    _, _, docs = records()
    for node in docs[0]["ecological_interactions"]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert not any(
            k in node
            for k in ["interaction_type", "source_taxon", "target_taxon", "participating_taxa"]
        )
        assert all(e["reference"] == "PMID:14532040" for e in node["evidence"])
    rationale = docs[0]["discussions"][0]["rationale"]
    assert "G. uraniireducens" in rationale and "Oak Ridge" in rationale
    assert "not be interpreted as evidence for every canonical member" in rationale


def test_rumen_selection_not_demonstrated_niche_partitioning():
    _, _, docs = records()
    doc = docs[1]
    first, _, last = doc["ecological_interactions"]
    assert all("interaction_type" not in n for n in doc["ecological_interactions"])
    assert first["downstream"][0]["target"] == last["name"]
    assert first["downstream"][0]["description"].startswith("PARTIAL:")
    assert "6.33 mM" in last["evidence"][0]["snippet"]
    assert [d["discussion_id"] for d in doc["discussions"][:2]] == [
        "hydrogen-flux-not-measured",
        "amplicon-bacterial-scope",
    ]


def test_sf356_positive_cycle_and_negative_effect_survive():
    _, _, docs = records()
    hydrolysis, oxygen, fg4, suppression = docs[2]["ecological_interactions"]
    assert hydrolysis["interaction_type"] == "CROSS_FEEDING"
    assert oxygen["interaction_type"] == "MUTUALISM"
    assert hydrolysis["downstream"][0]["target"] == oxygen["name"]
    assert oxygen["downstream"][0]["target"] == hydrolysis["name"]
    assert fg4["downstream"][0]["target"] == hydrolysis["name"]
    assert (
        "not assert an absolute zero-oxygen requirement" in oxygen["downstream"][0]["description"]
    )
    assert all("interaction_type" not in n for n in [fg4, suppression])
    assert "reciprocal harm" in fg4["description"]
    assert fg4["scope"] == "COMMUNITY_LEVEL"
    assert "target_taxon" not in fg4
    assert fg4["source_taxon"]["term"]["id"] == "NCBITaxon:319464"
    assert "suppresses growth" in suppression["description"]


def test_sihumix_neighbors_are_not_bp5_perturbation():
    _, rows, docs = records()
    output, expression, model = docs[3]["ecological_interactions"]
    assert all("downstream" not in n for n in [output, expression, model])
    assert all("interaction_type" not in n for n in [output, expression])
    assert model["interaction_type"] == "CROSS_FEEDING"
    assert model["description"].startswith("COMPUTATIONAL:")
    assert "not a BP5 knockout" in model["description"]
    assert model["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert model["evidence"][0]["supports"] == "PARTIAL"
    assert len(rows[3]["removed_edge_decisions"]) == 2


def test_sihumix_positive_assay_and_cultivation_confounder():
    _, _, docs = records()
    gap = docs[3]["discussions"][0]
    assert "conditions differ" in gap["evidence"][0]["snippet"]
    assert "BP5 may" in gap["evidence"][1]["snippet"]
    assert "reduction in cell size" in gap["evidence"][2]["snippet"]
    assert "inconsistent BCFA direction" in gap["rationale"]
    expression = docs[3]["ecological_interactions"][1]
    assert expression["evidence"][1]["evidence_source"] == "COMPUTATIONAL"
    assert "colonization facilitation" in expression["description"]


def test_every_original_node_and_direction_has_a_disposition():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 14
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 2
    assert sum(len(r["edges_before"]) for r in rows) == 10
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 4
    for row, doc in zip(rows, docs, strict=True):
        assert {d["node"] for d in row["node_decisions"]} == {
            n["name"] for n in doc["ecological_interactions"]
        }
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        for decision in row["retained_edge_decisions"]:
            assert all(
                row["renamed_nodes"].get(decision["before"][k], decision["before"][k])
                == decision["after"][k]
                for k in ["source", "target"]
            )


def test_source_proof_history_and_unresolved_scope():
    ledger, rows, docs = records()
    assert len(ledger["snippet_checks"]) == ledger["primary_graph_snippet_count"] == 20
    assert len(ledger["discussion_snippet_checks"]) == 8
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )
    assert ledger["cache_changes"] == []
    assert ledger["issues"] == [1766, 1767, 1768, 1769]
    assert ledger["unresolved_non_graph_issues"] == [1770]
    assert not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    for row, doc in zip(rows, docs, strict=True):
        assert row["allowed_changed_fields"] == [
            "curation_history",
            "discussions",
            "ecological_interactions",
        ]
        assert row["curation_events_added"] == len(row["history_files"])
        assert row["curation_events_added"] == (2 if doc["id"] == "CommunityMech:000061" else 1)
        assert doc["curation_history"][-1]["llm_assisted"]
        assert (ROOT / row["history_files"][0]).is_file()
