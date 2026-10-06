"""Keep measured community outcomes distinct from unresolved causal mechanisms."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-hambi-hanford-c6-batch50.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_canonical_input_rosters_and_scopes_remain_explicit():
    _, docs = records()
    for doc, count in zip(docs, [16, 4, 6], strict=True):
        expected = [
            {"preferred_term": t["taxon_term"]["preferred_term"], "term": t["taxon_term"]["term"]}
            for t in doc["taxonomy"]
        ]
        assert len(expected) == count
        for node in doc["ecological_interactions"]:
            assert node["scope"] == "COMMUNITY_LEVEL"
            assert node["participating_taxa"] == expected
            assert (
                not {"interaction_type", "source_taxon", "target_taxon", "downstream"} & node.keys()
            )


def test_hambi_preserves_controlled_carbon_evidence_and_author_interpretation():
    _, (doc, _, _) = records()
    (node,) = doc["ecological_interactions"]
    text = node["description"]
    assert "A. caviae dominated low carbon" in text
    assert "P. chlororaphis co-dominated" in text and "C. koseri dominated high carbon" in text
    assert "OD-scaled abundance" in text and "competitive sorting" in text
    assert "do not selectively establish" in text and "alternative stable states" in text
    assert all(e["supports"] == "SUPPORT" for e in node["evidence"])
    assert all(e["evidence_source"] == "IN_VITRO" for e in node["evidence"])
    assert "not proven persistence" in doc["discussions"][0]["rationale"]


def test_hanford_field_observations_do_not_become_measured_flux():
    ledger, (_, doc, _) = records()
    turnover, flux, depth = doc["ecological_interactions"]
    assert all(e["supports"] == "SUPPORT" for e in turnover["evidence"])
    assert "curated subset" in turnover["description"]
    assert flux["name"] == "Putative Guild Patterns and Inferred Redox Resource Dynamics"
    assert flux["description"].startswith("PARTIAL -")
    assert flux["evidence"][0]["supports"] == "PARTIAL"
    assert flux["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert depth["name"] == "Putative Redox Guilds in Depth-Stratified Sampling"
    assert "does not preserve its precise depth comparison" in depth["description"]
    assert "Separate Methods excerpts" in depth["description"]
    assert [e["supports"] for e in depth["evidence"]] == ["SUPPORT", "PARTIAL"]
    assert "Putative guild annotation only" in depth["biological_processes"][0]["notes"]
    assert "not a demonstrated partner-to-partner transfer" in depth["metabolites"][1]["notes"]
    assert "not full body" in ledger["limitations"][0]
    source = ledger["records"][1]["source_review"]["PMID:22456444"]
    assert "selected-snippet cache only" in source["scope"]
    assert "CAPTCHA" in source["scope"]


def test_c6_shared_taxon_ids_do_not_collapse_distinct_strains():
    _, (_, _, doc) = records()
    members = doc["ecological_interactions"][0]["participating_taxa"]
    assert len(members) == 6 and len({p["preferred_term"] for p in members}) == 6
    assert [p["term"]["id"] for p in members].count("NCBITaxon:293") == 2
    assert [p["term"]["id"] for p in members].count("NCBITaxon:370111") == 2
    removal, recovery = doc["ecological_interactions"]
    assert "94.41% hexamine" in removal["description"]
    assert "ammonia production, not consortium ammonia removal" in removal["description"]
    assert "not a formal equivalence test" in recovery["description"]
    assert "fresh-medium renewal" in recovery["description"]
    assert "does not establish survival of every original strain" in recovery["description"]
    assert all(e["supports"] == "SUPPORT" for n in [removal, recovery] for e in n["evidence"])


def test_c6_existing_gap_is_extended_without_erasing_its_evidence():
    _, (_, _, doc) = records()
    (gap,) = doc["discussions"]
    assert gap["discussion_id"] == "c6-molecular-division-of-labor"
    assert gap["posed_by"] == "claude" and gap["evidence"][0]["reference"] == "PMID:41743136"
    assert len(gap["attaches_to"]) == 2
    assert "main-text 50 mg/L" in gap["rationale"] and "100 mg/L caption" in gap["rationale"]
    assert "preserved, not recertified" in gap["rationale"]


def test_every_node_and_removed_arrow_has_a_hash_bound_decision():
    ledger, docs = records()
    assert ledger["review_mode"] == "source_based_self_adversarial_review"
    assert ledger["independent_approval"] is False and ledger["issues"] == [1493, 1494, 1495]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for row, doc in zip(ledger["records"], docs, strict=True):
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {n["node"] for n in row["node_decisions"]} == names
        assert row["status"] == "reviewed" and row["removed_node_decisions"] == []
        assert len(row["edges_before"]) == len(row["removed_edge_decisions"])
        assert row["edges_after"] == row["retained_edge_decisions"] == []
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        for gap in doc["discussions"]:
            assert gap["status"] == "OPEN"
            assert all(a.split("#", 1)[1] in names for a in gap["attaches_to"])
    assert sum(len(r["edges_before"]) for r in ledger["records"]) == 2
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
