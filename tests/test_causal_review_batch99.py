"""Keep resource loops, production endpoints and compositional evidence distinct."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch99.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_resource_loop_retains_two_directions_without_oxygen_benefit():
    _, _, docs = records()
    carbon, nitrogen = docs[0]["ecological_interactions"]
    assert [n["name"] for n in [carbon, nitrogen]] == [
        "Yeast Carbon Dioxide Provisioning",
        "Algal Reduced Nitrogen Provisioning",
    ]
    assert carbon["downstream"][0]["target"] == nitrogen["name"]
    assert nitrogen["downstream"][0]["target"] == carbon["name"]
    assert all(n["downstream"][0]["description"].startswith("PARTIAL:") for n in [carbon, nitrogen])
    assert all(n["interaction_type"] == "CROSS_FEEDING" for n in [carbon, nitrogen])
    assert "(14)" in nitrogen["evidence"][0]["snippet"]
    assert all(p["term"]["id"] != "GO:0006113" for p in carbon["biological_processes"])


def test_resveratrol_titer_is_not_mutualistic_fitness_or_isolated_transfer():
    _, _, docs = records()
    mutualism, pathway, outcome = docs[1]["ecological_interactions"]
    assert mutualism["interaction_type"] == "MUTUALISM"
    assert pathway["interaction_type"] == "CROSS_FEEDING"
    assert "downstream" not in mutualism
    assert pathway["downstream"][0]["description"].startswith("PARTIAL:")
    assert "interaction_type" not in outcome
    assert "precursor accumulation and lower biomass" in outcome["description"]
    assert "not by itself a mutualistic fitness measurement" in outcome["description"]


def test_brine_profile_does_not_assert_a_metabolic_chain():
    _, _, docs = records()
    nodes = docs[2]["ecological_interactions"]
    assert len(nodes) == 1
    node = nodes[0]
    assert node["scope"] == "COMMUNITY_LEVEL"
    assert node["name"] == "Community Composition Across Natural and Concentrated Brines"
    assert not any(
        k in node
        for k in [
            "source_taxon",
            "target_taxon",
            "interaction_type",
            "downstream",
            "metabolites",
            "biological_processes",
        ]
    )
    assert "not a controlled lithium-only effect" in node["description"]
    assert "not the concentrated sample" in node["description"]


def test_sclerotia_dropout_effect_is_not_essentiality_or_niche_partitioning():
    _, _, docs = records()
    full, mc, spatial = docs[3]["ecological_interactions"]
    assert all(
        "interaction_type" not in n and "biological_processes" not in n for n in [full, mc, spatial]
    )
    assert mc["scope"] == "COMMUNITY_LEVEL" and "source_taxon" not in mc
    assert len(mc["participating_taxa"]) == 1
    assert mc["participating_taxa"][0]["preferred_term"] == "Trinickia sclerotiorum sp. nov. MC"
    assert mc["target_taxon"]["term"]["id"] == "NCBITaxon:5180"
    assert mc["downstream"][0]["target"] == full["name"]
    assert "not an additive decomposition" in mc["downstream"][0]["description"]
    assert "not demonstrated competition-reducing niche partitioning" in spatial["description"]
    assert "downstream" not in spatial


def test_participant_lists_are_scoped_canonical_identities():
    _, _, docs = records()
    for doc, index, members in [
        (docs[2], 0, range(6)),
        (docs[3], 0, range(12)),
        (docs[3], 2, [3, 2, 10, 11]),
    ]:
        expected = [
            {k: doc["taxonomy"][i]["taxon_term"][k] for k in ["preferred_term", "term"]}
            for i in members
        ]
        assert doc["ecological_interactions"][index]["participating_taxa"] == expected
    assert all(t["taxon_term"]["term"]["id"] != "NCBITaxon:5180" for t in docs[3]["taxonomy"])


def test_dispositions_and_append_only_histories_cover_every_original_node():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 9
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 5
    assert sum(len(r["renamed_nodes"]) for r in rows) == 1
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 4
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 2
    assert len(ledger["snippet_checks"]) == ledger["primary_graph_snippet_count"] == 12
    assert len(ledger["discussion_snippet_checks"]) == 4
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"])
        assert row["curation_events_added"] == (2 if doc["id"] == "CommunityMech:000364" else 1)
        assert doc["curation_history"][-1]["llm_assisted"]
        assert (ROOT / row["history_files"][0]).is_file()
        for e in row["retained_edge_decisions"]:
            assert all(
                row["renamed_nodes"].get(e["before"][k], e["before"][k]) == e["after"][k]
                for k in ["source", "target"]
            )


def test_manuscript_version_differences_are_explicit_not_claimed_literal():
    ledger, _, _ = records()
    checks = ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    assert all(c["cache_matched"] for c in checks)
    variants = [c for c in checks if not c["independent_primary_match"]]
    assert len(variants) == 2
    assert {c["evidence_index"] for c in variants} == {0, 2}
    assert all(
        c["final_version_equivalent"]
        and c["reference"] == "PMID:42523014"
        and c["node"] == "Spatial Invasion of Sclerotia by SynCom Members"
        for c in variants
    )
    assert "exceeded that of all other" in variants[1]["final_version_snippet"]


def test_open_scope_and_provider_boundaries_are_preserved():
    ledger, _, _ = records()
    assert ledger["issues"] == [1784, 1785, 1786, 1787]
    assert ledger["unresolved_non_graph_issues"] == [1788, 1789]
    assert ledger["cache_changes"] == [] and not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert any("403" in s for s in ledger["limitations"])
    assert any("HTTP500" in s for s in ledger["limitations"])
