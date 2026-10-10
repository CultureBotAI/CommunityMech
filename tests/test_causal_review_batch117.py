"""Guard assay boundaries without erasing experimentally supported interactions."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch117.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_tribromophenol_retains_enrichment_and_sequential_cross_feeding():
    _, _, docs = records()
    a, b, c, d = docs[0]["ecological_interactions"]
    assert a["interaction_type"] == b["interaction_type"] == "CROSS_FEEDING"
    assert "highly enriched Dehalobacter FTH1 culture" in a["description"]
    assert "introduced subsequently" in b["description"]
    assert "not a proven exhaustive three-isolate membership" in d["description"]
    assert "sequential introduction" in b["downstream"][0]["description"]
    assert c["scope"] == d["scope"] == "COMMUNITY_LEVEL"


def test_phenol_outcome_does_not_invent_reciprocal_benefit_or_tbp_tracer():
    _, _, docs = records()
    _, _, c, d = docs[0]["ecological_interactions"]
    assert [t["term"]["id"] for t in c["participating_taxa"]] == ["NCBITaxon:1261393"]
    assert len(d["participating_taxa"]) == 3
    assert "interaction_type" not in c and "interaction_type" not in d
    assert "ring-labeled phenol, not labeled tribromophenol" in c["description"]
    assert "not an observed DS-to-FTH1 benefit" in c["description"]


def test_hydrogen_transfer_is_proposed_despite_expressed_pathways():
    _, _, docs = records()
    a, b, _, d = docs[1]["ecological_interactions"]
    for n in [a, b, d]:
        assert n["name"].startswith("Proposed")
        assert n["description"].startswith("HYPOTHESIZED:")
        assert all(e["supports"] == "PARTIAL" for e in n["evidence"])
    assert "complete methanogenesis pathway and expressed Methanoregula mcrA" in b["description"]
    assert "not direct measurement" in b["description"]


def test_host_energetics_arrows_do_not_upgrade_model_to_measured_fitness():
    _, _, docs = records()
    a, b, _, d = docs[1]["ecological_interactions"]
    assert "interaction_type" not in d
    for n in [a, b]:
        edge = n["downstream"][0]
        assert edge["target"] == d["name"] and edge["description"].startswith("PARTIAL:")
        assert "not a measured transfer-to-fitness causal effect" in edge["description"]
    assert "not experimentally established" in d["description"]


def test_observed_magnetotaxis_survives_without_forced_mutualism():
    _, _, docs = records()
    c = docs[1]["ecological_interactions"][2]
    assert "interaction_type" not in c and c["scope"] == "PAIRWISE"
    assert (
        "Observed field-reversal responses establish active host magnetotaxis" in c["description"]
    )
    assert (
        "FISH failed" in c["description"] and "six months of storage in Munich" in c["description"]
    )
    assert c["evidence"][0]["supports"] == "SUPPORT"


def test_urine_reactor_roles_do_not_transfer_salt_challenge_conditions():
    _, _, docs = records()
    a, b, _ = docs[2]["ecological_interactions"]
    assert "equal or individually essential" in a["description"]
    assert b["name"] == "Ammonia and nitrite oxidation by the nitrifier pair"
    assert "separately salt-adapted in reactor 1" in b["description"]
    assert "not a measured salinity or removal rate" in b["description"]
    assert "not transferred to reactor 2" in b["downstream"][0]["description"]
    assert a["downstream"][0]["target"] == b["name"]


def test_urine_outcome_distinguishes_batch_rates_and_application_motivation():
    _, _, docs = records()
    c = docs[2]["ecological_interactions"][2]
    assert len(c["participating_taxa"]) == 5 and "interaction_type" not in c
    assert "15 +/- 6 mg nitrate-N/L/day" in c["description"]
    assert "Separate fresh-real-urine batch activity tests" in c["description"]
    assert "not proof of spaceflight performance or fertilizer readiness" in c["description"]
    assert all("Astronauts" not in e["snippet"] for e in c["evidence"])
    assert c["biological_processes"][0]["preferred_term"] == "ammonia oxidation"


def test_vitamin_recipient_and_production_assay_are_not_network_wide():
    _, _, docs = records()
    a = docs[3]["ecological_interactions"][0]
    assert a["scope"] == "PAIRWISE" and a["target_taxon"]["term"]["id"] == "NCBITaxon:5206"
    assert "Cryptococcus was not included in the correlation network" in a["description"]
    assert "not a measured concentration in the two-member coculture" in a["description"]
    assert "do not validate every correlated auxotroph" in a["description"]


def test_vitamin_mutualism_preserves_evidence_without_exclusive_mediation():
    _, _, docs = records()
    a, b, c = docs[3]["ecological_interactions"]
    assert c["interaction_type"] == "MUTUALISM" and c["evidence"][0]["supports"] == "SUPPORT"
    assert "higher viable cell densities in coculture" in c["description"]
    assert "without proving vitamin-only mediation" in c["description"]
    assert "sole growth-promoting component" in b["description"]
    assert "only cause" in a["downstream"][0]["description"]


def test_source_discrepancies_are_not_silently_reconciled():
    _, _, docs = records()
    c = docs[3]["ecological_interactions"][2]
    gap = docs[3]["discussions"][-1]["rationale"]
    assert "no reconciled fold increase" in c["description"]
    assert "Fig.6 caption gives about 50-fold" in gap
    assert "bacterial Results densities imply a different ratio" in gap
    assert "Methods describe final-passage coculture spent medium" in gap
    assert "No corrected value or uniquely resolved medium source is invented" in gap


def test_every_node_and_arrow_has_an_explicit_disposition():
    ledger, rows, _ = records()
    c = ledger["reviewed_counts"]
    assert (c["original_nodes"], c["retained_nodes"], c["removed_nodes"]) == (14, 14, 0)
    assert (c["original_arrows"], c["retained_arrows"], c["removed_arrows"]) == (9, 9, 0)
    assert c["renamed_nodes"] == 5
    assert c["graph_quotations"] == 24 and c["discussion_quotations"] == 4
    assert all(not r["removed_edge_decisions"] for r in rows)
    assert ledger["issues"] == [1907, 1908, 1909, 1910]
    assert ledger["unresolved_non_graph_issues"] == [1911, 1912]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0


def test_aliases_canonical_participants_histories_and_anchors_are_guarded():
    ledger, rows, docs = records()
    assert not ledger["independent_approval"]
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).exists()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        names = {n["name"] for n in doc["ecological_interactions"]}
        for n in doc["ecological_interactions"]:
            assert all(t in canonical for t in n.get("participating_taxa", []))
            assert all(e["target"] in names for e in n.get("downstream", []))
        for d in doc["discussions"]:
            assert all(a.split("#", 1)[1] in names for a in d["attaches_to"])
    for doc in [docs[0], docs[2]]:
        shared = doc["engineering_design"]["evidence"][0]
        assert doc["taxonomy"][0]["evidence"][0] is shared
        assert all(e is not shared for n in doc["ecological_interactions"] for e in n["evidence"])
