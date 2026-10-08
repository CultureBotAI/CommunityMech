"""Keep measured phototrophic outcomes separate from untested mediation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-three-records-batch111.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_acetate_attribution_remains_partial_and_existing_gap_is_reused():
    _, _, docs = records()
    carbon = docs[0]["ecological_interactions"][0]
    assert carbon["interaction_type"] == "CROSS_FEEDING"
    assert carbon["evidence"][1]["supports"] == "PARTIAL"
    assert "do not isotope-resolve" in carbon["description"]
    assert "only source of carbon" in carbon["evidence"][2]["snippet"]
    assert carbon["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert len(docs[0]["discussions"]) == 1
    assert (
        docs[0]["discussions"][0]["discussion_id"]
        == "pseudomonas_butanol_coculture_carbon_specificity"
    )


def test_butanol_output_is_not_duplicate_exchange_or_growth_adaptation_gain():
    _, _, docs = records()
    product = docs[0]["ecological_interactions"][1]
    assert product["scope"] == "COMMUNITY_LEVEL"
    assert "interaction_type" not in product and "source_taxon" not in product
    assert len(product["participating_taxa"]) == 2
    assert "fluctuated and reached a plateau" in product["description"]
    assert "without increasing 1-butanol production" in product["description"]
    assert "did not exceed" in product["evidence"][2]["snippet"]


def test_lichen_ros_protection_remains_positive_and_context_dependent():
    _, _, docs = records()
    protection = docs[1]["ecological_interactions"][1]
    assert protection["interaction_type"] == "MUTUALISM"
    assert "High-density axenic growth remains possible" in protection["description"]
    assert protection["evidence"][1]["supports"] == "SUPPORT"
    assert "progressively reduced" in protection["evidence"][1]["snippet"]
    assert "grew better" in protection["evidence"][2]["snippet"]
    assert protection["evidence"][4]["supports"] == "PARTIAL"
    assert "beyond HOOH reduction" in protection["evidence"][4]["snippet"]


def test_lichen_lipid_endpoint_does_not_prove_ros_mediation():
    _, _, docs = records()
    protection, product = docs[1]["ecological_interactions"][1:]
    assert protection["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert "interaction_type" not in product
    assert (
        "54%" in product["description"] and "whole-culture" in product["evidence"][0]["explanation"]
    )
    assert "not equivalent to final biomass alone" in product["description"]
    assert len(docs[1]["discussions"]) == 1


def test_periphyton_grouping_is_removed_but_eps_role_is_preserved():
    _, rows, docs = records()
    nodes = docs[2]["ecological_interactions"]
    assert len(nodes) == 5
    assert all(n["name"] != "Growth-Balanced Phototroph Grouping" for n in nodes)
    assert rows[2]["removed_node_decisions"][0]["node"] == "Growth-Balanced Phototroph Grouping"
    assert len(rows[2]["renamed_nodes"]) == 3
    assert nodes[0]["interaction_type"] == "COLONIZATION_FACILITATION"
    assert nodes[0]["evidence"][1]["supports"] == "PARTIAL"
    assert "not an added canonical member" in nodes[0]["description"]
    assert all("downstream" not in n for n in nodes)


def test_early_periphyton_outcomes_are_diatom_scoped_not_facilitation_edges():
    _, _, docs = records()
    nodes = docs[2]["ecological_interactions"]
    for node in nodes[1:3]:
        assert node["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in node
        assert len(node["participating_taxa"]) == 1
        assert node["participating_taxa"][0]["preferred_term"] == "diatoms"
    assert "6 to 7 times" in nodes[1]["evidence"][0]["snippet"]
    assert "Longer incubation" in nodes[2]["evidence"][1]["snippet"]


def test_mature_membership_and_psii_exception_do_not_prove_redundancy():
    _, _, docs = records()
    mature, stressor = docs[2]["ecological_interactions"][3:]
    assert "interaction_type" not in mature and "interaction_type" not in stressor
    assert "at least 22 detected" in mature["description"]
    assert "three species were no longer detected" in mature["evidence"][2]["snippet"]
    assert "highest-herbicide exception" in stressor["description"]
    assert "100 nM terbuthylazine at 18 days" in stressor["evidence"][2]["snippet"]
    assert stressor["evidence"][3]["supports"] == "PARTIAL"


def test_all_original_nodes_and_arrows_have_bounded_dispositions():
    ledger, rows, _ = records()
    assert ledger["reviewed_counts"] == {
        "original_nodes": 11,
        "retained_nodes": 10,
        "removed_nodes": 1,
        "retained_arrows": 3,
        "removed_arrows": 0,
        "renamed_nodes": 3,
        "graph_quotations": 27,
        "discussion_quotations": 3,
        "new_discussions": 2,
        "preserved_discussions": 1,
    }
    assert ledger["unresolved_non_graph_issues"] == [1868, 1869]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert all(row["status"] == "reviewed" for row in rows)
    for row in rows:
        assert [(e["source"], e["target"]) for e in row["edges_before"]] == [
            (e["source"], e["target"]) for e in row["edges_after"]
        ]


def test_hashes_histories_and_identity_only_participants_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        expected = {"ecological_interactions", "curation_history"}
        if row["id"] != "CommunityMech:000363":
            expected.add("discussions")
        assert set(row["allowed_changed_fields"]) == expected
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).exists()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        for node in doc["ecological_interactions"]:
            assert all(
                p in canonical and set(p) == {"preferred_term", "term"}
                for p in node.get("participating_taxa", [])
            )
