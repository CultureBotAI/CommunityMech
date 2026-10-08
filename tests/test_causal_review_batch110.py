"""Preserve production evidence without polymer, recipient or mediation overclaims."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-three-records-batch110.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_halomonas_preserves_outcomes_without_certifying_medium_or_mediation():
    _, rows, docs = records()
    carbon, product, partition = docs[0]["ecological_interactions"]
    assert rows[0]["status"] == "needs_research" and 1860 in rows[0]["issues"]
    assert carbon["interaction_type"] == "CROSS_FEEDING"
    assert "strain-specific attribution" in carbon["description"]
    assert "Complete medium inputs remain unverified" in carbon["description"]
    assert "31%" in product["description"] and "five months" in product["description"]
    assert product["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in product
    assert "biological_processes" not in product
    assert "interaction_type" not in partition
    assert partition["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")


def test_pha_is_not_phb_or_a_rate_comparison():
    _, _, docs = records()
    product = docs[1]["ecological_interactions"][1]
    assert "interaction_type" not in product and "source_taxon" not in product
    assert product["metabolites"][1]["term"] == {
        "id": "CHEBI:78037",
        "label": "polyhydroxyalkanoate",
    }
    assert "not a measured rate increase" in product["description"]
    assert "most abundant monomer" in product["evidence"][0]["snippet"]
    assert "snapshot at the end" in product["evidence"][1]["snippet"]


def test_dnt_removal_does_not_prove_complete_mineralization():
    _, _, docs = records()
    dnt = docs[1]["ecological_interactions"][2]
    assert "interaction_type" not in dnt and "source_taxon" not in dnt
    assert "adsorption and reductive" in dnt["description"]
    assert "Complete mineralization was not directly established" in dnt["description"]
    assert any("could not precisely quantitate" in e["snippet"] for e in dnt["evidence"])


def test_growth_feedback_preserves_positive_context_without_reverse_sucrose():
    _, _, docs = records()
    feedback = docs[1]["ecological_interactions"][3]
    assert feedback["interaction_type"] == "MUTUALISM"
    assert "conditional carbon-supported partnership" in feedback["description"]
    assert "matched external-sucrose controls" in feedback["description"]
    assert "metabolites" not in feedback
    assert feedback["evidence"][1]["supports"] == "PARTIAL"
    assert "PARTIAL" in feedback["description"]


def test_anode_is_not_a_cyanobacterial_recipient_and_carbon_return_is_hypothetical():
    _, _, docs = records()
    carbon, anode, separation = docs[2]["ecological_interactions"]
    assert carbon["metabolites"][0]["term"] == {
        "id": "CHEBI:16004",
        "label": "(R)-lactate",
    }
    assert "not the exclusive organic input" in carbon["description"]
    assert "source_taxon" not in anode and "target_taxon" not in anode
    assert anode["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in anode
    assert len(anode["participating_taxa"]) == 1
    assert anode["participating_taxa"][0]["term"]["id"] == "NCBITaxon:211586"
    assert anode["downstream"][0]["target"] == carbon["name"]
    assert anode["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert "CO2" in anode["downstream"][0]["description"]
    assert anode["evidence"][1]["supports"] == "PARTIAL"
    assert "enhanced the growth" in anode["evidence"][2]["snippet"]
    assert "interaction_type" not in separation
    assert "continuous medium replenishment" in separation["description"]
    assert "LB supplementation" in separation["description"]


def test_all_existing_topology_and_source_access_limits_are_recorded():
    ledger, rows, docs = records()
    assert ledger["reviewed_counts"] == {
        "retained_nodes": 10,
        "removed_nodes": 0,
        "retained_arrows": 6,
        "removed_arrows": 0,
        "renamed_nodes": 0,
        "graph_quotations": 24,
        "discussion_quotations": 3,
    }
    assert [r["status"] for r in rows] == ["needs_research", "reviewed", "reviewed"]
    assert ledger["unresolved_research_issues"] == [1860]
    assert ledger["unresolved_non_graph_issues"] == [1861, 1862]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    for r, d in zip(rows, docs, strict=True):
        assert [(e["source"], e["target"]) for e in r["edges_before"]] == [
            (e["source"], e["target"]) for e in r["edges_after"]
        ]
        assert len(r["node_decisions"]) == len(d["ecological_interactions"])


def test_hashes_history_and_identity_only_participants_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    for row, doc in zip(rows, docs, strict=True):
        latest = row
        if row["id"] == "CommunityMech:000198":
            successor = (
                ROOT
                / "reports/causal_graph_review/decisions/20261008-halomonas-identity-batch126.yaml"
            )
            latest = yaml.safe_load(successor.read_text())["records"][0]
            assert latest["supersedes_review"] == {
                "review_file": str(LEDGER.relative_to(ROOT)),
                "record_sha256": row["record_sha256"],
            }
            assert latest["original_sha256"] == row["record_sha256"]
        assert (
            hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == latest["record_sha256"]
        )
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        expected_events = 2 if row["id"] == "CommunityMech:000167" else 1
        assert row["curation_events_added"] == len(row["history_files"]) == expected_events
        assert all((ROOT / p).exists() for p in row["history_files"])
        assert doc["curation_history"][-1]["llm_assisted"] is True
        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        for n in doc["ecological_interactions"]:
            assert all(
                t in canonical and set(t) == {"preferred_term", "term"}
                for t in n.get("participating_taxa", [])
            )
