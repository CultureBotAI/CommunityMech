"""Separate ecological observations from mediation and genomic candidates."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch95.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_fsqn_unchanged_predictions_are_not_mediation():
    _, rows, docs = records()
    row = rows[0]
    assert row["outcome"] == "unchanged"
    assert row["original_sha256"] == row["record_sha256"]
    assert row["allowed_changed_fields"] == row["history_files"] == []
    observed, predicted = docs[0]["ecological_interactions"]
    assert not any(n.get("downstream") or n.get("interaction_type") for n in [observed, predicted])
    assert predicted["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert "prediction" in predicted["description"]


def test_rice_pot_benefit_and_partial_mediation():
    _, _, docs = records()
    soil, acquisition, outcome = docs[1]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [soil, acquisition, outcome])
    assert all(
        n["downstream"][0]["description"].startswith("PARTIAL:") for n in [soil, acquisition]
    )
    assert acquisition["evidence"][0]["supports"] == "PARTIAL"
    assert outcome["evidence"][0]["supports"] == "SUPPORT"
    assert outcome["evidence"][0]["evidence_source"] == "IN_VIVO"
    assert "field rice/soybean" in outcome["description"]
    assert "decreased" in outcome["description"]
    assert "CHEBI:28659" not in str(outcome)


def test_richmond_real_cycle_is_not_pairwise_mutualism():
    _, _, docs = records()
    lepto, ferro, pyrite, _, _ = docs[2]["ecological_interactions"]
    assert lepto["downstream"][0]["target"] == pyrite["name"]
    assert ferro["downstream"][0]["target"] == pyrite["name"]
    assert pyrite["downstream"][0]["target"] == lepto["name"]
    assert "external oxygen and mineral supply" in pyrite["description"]
    assert "not the rate of this particular biofilm" in pyrite["description"]
    for node in [lepto, ferro, pyrite]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert node["participating_taxa"]
        assert all(set(t) == {"preferred_term", "term"} for t in node["participating_taxa"])
        assert not any(k in node for k in ["source_taxon", "target_taxon", "interaction_type"])
        assert "GO:0006826" not in str(node)
    assert "biological_processes" not in ferro


def test_richmond_capacity_and_contact_identity_are_bounded():
    _, rows, docs = records()
    doc = docs[2]
    contact = doc["ecological_interactions"][3]
    assert contact["name"] == "Thermoplasmatales-ARMAN Cell Contact"
    assert not any(
        k in contact
        for k in ["source_taxon", "target_taxon", "participating_taxa", "interaction_type"]
    )
    assert "small subset" in contact["description"]
    removed = {r["node"] for r in rows[2]["removed_node_decisions"]}
    assert removed == {
        "Nitrogen Fixation by Leptospirillum Group III",
        "Thermoplasmatales-Parvarchaeota Cell Contact",
    }
    nitrogen_gap, contact_gap = doc["discussions"]
    assert "positive diazotrophic capacity" in nitrogen_gap["evidence"][0]["explanation"]
    assert "not identified by proteomics" in nitrogen_gap["evidence"][1]["snippet"]
    assert "does not require obligacy" in contact_gap["rationale"]
    assert (
        "must not be read as an observation for every canonical member" in contact_gap["rationale"]
    )


def test_richmond_refuge_is_a_distribution_observation():
    _, rows, docs = records()
    node = docs[2]["ecological_interactions"][-1]
    assert node["name"] == "Higher-pH Acidithiobacillus Distribution"
    assert rows[2]["renamed_nodes"] == {
        "Iron and Sulfur Oxidation at Higher pH Refugia": node["name"]
    }
    assert node["participating_taxa"][0]["term"]["id"] == "NCBITaxon:920"
    assert set(node["participating_taxa"][0]) == {"preferred_term", "term"}
    assert "interaction_type" not in node and "biological_processes" not in node
    assert "competitive exclusion" in node["description"]
    assert all(e["reference"] == "doi:10.1186/1467-4866-5-13" for e in node["evidence"])


def test_rifle_enrichment_not_inventory_or_competition():
    _, rows, docs = records()
    selection, dominance = docs[3]["ecological_interactions"]
    assert selection["downstream"][0]["target"] == dominance["name"]
    assert selection["downstream"][0]["description"].startswith("PARTIAL:")
    assert "downstream" not in dominance
    assert all("interaction_type" not in n for n in [selection, dominance])
    assert "not proof that every member" in selection["description"]
    assert "72 putative" in dominance["description"]
    assert len(rows[3]["removed_node_decisions"]) == 4
    assert len(rows[3]["removed_edge_decisions"]) == 3
    gap = docs[3]["discussions"][0]
    assert gap["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert "does not exclude EET potential in all other" in gap["rationale"]
    assert "inconsistent near-complete-genome denominators" in gap["rationale"]


def test_all_original_nodes_and_directions_have_dispositions():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 12
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 6
    assert sum(len(r["edges_before"]) for r in rows) == 9
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 3
    for row, doc in zip(rows, docs, strict=True):
        assert {r["node"] for r in row["node_decisions"]} == {
            n["name"] for n in doc["ecological_interactions"]
        }
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        for decision in row["retained_edge_decisions"]:
            assert all(decision["before"][k] == decision["after"][k] for k in ["source", "target"])


def test_source_proof_history_and_unresolved_scope():
    ledger, rows, docs = records()
    assert len(ledger["snippet_checks"]) == ledger["primary_graph_snippet_count"] == 16
    assert len(ledger["discussion_snippet_checks"]) == 5
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )
    assert ledger["cache_changes"] == []
    assert ledger["issues"] == [1761, 1762, 1763]
    assert ledger["unresolved_non_graph_issues"] == [1764]
    assert not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"] == []
    for row, doc in zip(rows[1:], docs[1:], strict=True):
        assert row["curation_events_added"] == len(row["history_files"])
        assert row["curation_events_added"] == (2 if doc["id"] == "CommunityMech:000059" else 1)
        assert doc["curation_history"][-1]["llm_assisted"]
        assert (ROOT / row["history_files"][0]).is_file()
