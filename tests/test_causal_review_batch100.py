"""Keep measured process outcomes distinct from unisolated ecological mechanisms."""

import hashlib
import runpy
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch100.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_retention_outcomes_are_not_additional_niche_partitioning():
    _, _, docs = records()
    niche, retention, depletion = docs[0]["ecological_interactions"]
    assert niche["interaction_type"] == "NICHE_PARTITIONING"
    assert niche["downstream"][0]["description"].startswith("PARTIAL:")
    assert niche["downstream"][0]["target"] == retention["name"]
    assert retention["downstream"][0]["target"] == depletion["name"]
    assert all("interaction_type" not in n for n in [retention, depletion])
    assert "29% shorter" in retention["description"]
    assert "not a separate niche-partitioning" in retention["description"]
    assert "8.1 hours" in depletion["description"]


def test_anammox_pathway_and_competition_attribution_stay_bounded():
    _, _, docs = records()
    supply, dose = docs[1]["ecological_interactions"]
    assert supply["description"].startswith("PARTIAL:")
    assert supply["interaction_type"] == "CROSS_FEEDING"
    assert "not expression or a taxon-resolved flux measurement" in supply["description"]
    assert "interaction_type" not in dose
    assert "HYPOTHESIZED:" in dose["description"]
    assert "culture-volume" in dose["description"] and "97%" in dose["description"]
    assert not any(n.get("downstream") for n in [supply, dose])


def test_richness_workflow_nodes_do_not_survive_as_mechanisms():
    _, _, docs = records()
    nodes = docs[2]["ecological_interactions"]
    assert len(nodes) == 4
    assert not any(n.get("downstream") or n.get("biological_processes") for n in nodes)
    assert "only at days 3 and 30" in nodes[0]["description"]
    assert "not complete denitrification" in nodes[0]["description"]
    assert nodes[1]["name"] == "Larger Functional Increases at Lower Initial Richness"
    assert "does not establish identical final performance" in nodes[1]["description"]
    assert "statistical decomposition" in nodes[2]["description"]
    assert nodes[3]["name"] == "Mixture-Associated Relative Yield Differences"


def test_biofilm_keeps_real_current_advantage_without_syntrophy():
    _, _, docs = records()
    formation, response, current = docs[3]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [formation, response, current])
    assert current["name"] == "Higher Current in the Three-Species Coculture"
    assert "produced more current than each solitary culture" in current["description"]
    assert "without treating it as proof of superadditivity" in current["description"]
    assert formation["downstream"][0]["description"].startswith("PARTIAL:")
    assert response["downstream"][0]["description"].startswith("HYPOTHESIZED:")
    assert all(n["downstream"][0]["target"] == current["name"] for n in [formation, response])


def test_biofilm_transcript_response_uses_scoped_canonical_participants():
    _, _, docs = records()
    doc = docs[3]
    node = doc["ecological_interactions"][1]
    assert node["scope"] == "COMMUNITY_LEVEL"
    assert "source_taxon" not in node and "target_taxon" not in node
    expected = [
        {k: doc["taxonomy"][i]["taxon_term"][k] for k in ["preferred_term", "term"]} for i in [0, 1]
    ]
    assert node["participating_taxa"] == expected
    assert "three-species coculture comparison" in node["description"]


def test_selected_quote_does_not_become_independent_cache_coverage():
    ledger, _, docs = records()
    quote = docs[3]["ecological_interactions"][2]["evidence"][0]["snippet"]
    assert len(quote.split()) == 15
    assert quote in (ROOT / "references_cache/PMID_28087529.md").read_text()
    audit = runpy.run_path(str(ROOT / "scripts/evidence_snippet_audit.py"))
    content, available = audit["cache_text"]("PMID:28087529")
    assert available
    assert audit["alnum"](quote) not in audit["alnum"](content)
    selected = [c for c in ledger["snippet_checks"] if c["selected_cache_excerpt"]]
    assert len(selected) == 1 and not selected[0]["independent_cache_coverage"]


def test_decisions_cover_all_original_nodes_and_preserve_existing_directions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 12
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 2
    assert sum(len(r["renamed_nodes"]) for r in rows) == 5
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 4
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"]
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert all(
            e["target"] in names
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        )
    assert ledger["primary_graph_snippet_count"] == len(ledger["snippet_checks"]) == 23
    assert len(ledger["discussion_snippet_checks"]) == 4
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )


def test_followups_and_provider_authorization_are_not_preempted():
    ledger, _, _ = records()
    assert ledger["issues"] == [1791, 1792, 1793, 1794]
    assert ledger["unresolved_non_graph_issues"] == [1795, 1796]
    assert not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert len(ledger["cache_changes"]) == 1
    assert ledger["cache_changes"][0]["original_bytes_preserved"]
    assert ledger["cache_changes"][0]["selected_excerpt_excluded_from_independent_audit"]
