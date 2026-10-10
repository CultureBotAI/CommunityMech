"""Retain measured outcomes while bounding cross-study and mediator claims."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-six-records-batch124.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_algal_extension_remains_open_and_control_bounded():
    ledger, rows, docs = records()
    assert not docs[0]["ecological_interactions"]
    assert rows[0]["status"] == "needs_research"
    gap = docs[0]["discussions"][-1]
    assert "early nitrogen removal is slower" in gap["rationale"]
    assert "BOD removal is not uniformly better" in gap["rationale"]
    assert "no longer abstract-access gaps" in docs[0]["discussions"][0]["rationale"]
    assert ledger["edison"]["dry_run_completed"]
    assert ledger["edison"]["provider_submissions"] == 0


def test_tcp_reconstruction_is_not_measured_transfer():
    _, _, docs = records()
    a, b = docs[1]["ecological_interactions"]
    e = a["evidence"][0]
    assert e["supports"] == "PARTIAL" and e["evidence_source"] == "COMPUTATIONAL"
    assert e["computational_provenance"]["prediction_type"] == "OTHER"
    assert "not measured intergenus" in a["description"]
    assert not a.get("downstream") and not b.get("downstream")


def test_tcp_keeps_amendment_effects_and_shared_descriptors():
    _, _, docs = records()
    doc = docs[1]
    a, b = doc["ecological_interactions"]
    assert "enhanced TCP degradation" in b["description"]
    assert "19.06" in b["description"] and "3.5 days" in b["description"]
    assert "not separately assigned" in b["description"]
    assert a["metabolites"][1] is b["metabolites"][0]
    assert doc["growth_media"][0]["composition"][0]["chebi_term"] is b["metabolites"][1]


def test_yarrowia_design_is_not_exclusive_niches_or_polymer_catalysis():
    _, _, docs = records()
    a, _, _ = docs[2]["ecological_interactions"]
    assert "interaction_type" not in a and "biological_processes" not in a
    assert "Both can use glucose" in a["description"]
    assert "not an interchangeable YBGL1" in a["description"]
    assert "YBGL3 + YBXT-XR" in a["evidence"][-1]["snippet"]


def test_yarrowia_fraction_does_not_become_titer_advantage():
    _, _, docs = records()
    a, b, c = docs[2]["ecological_interactions"]
    assert "34% versus 26.3%" in c["description"]
    assert "comparable lipid titers" in c["description"]
    assert "1:2 consortium performed worse" in c["description"]
    assert "interaction_type" not in c
    assert "temporal succession" in b["description"]
    assert all(e["description"].startswith("PARTIAL:") for e in a["downstream"])


def test_yogurt_pairs_and_return_flow_remain_distinct():
    _, _, docs = records()
    a, b, _, _ = docs[3]["ecological_interactions"]
    assert (
        "CNRZ1066" in a["description"] and "not one universally beneficial pair" in a["description"]
    )
    assert all(e["supports"] == "PARTIAL" for e in a["evidence"])
    assert "does not satisfy all" in b["description"]
    assert b["downstream"][0]["description"].startswith("HYPOTHESIZED mediation:")


def test_yogurt_urease_recipients_and_scopes_are_explicit():
    _, _, docs = records()
    c, d = docs[3]["ecological_interactions"][2:]
    assert "Ammonia shortage mainly limits S. thermophilus" in c["description"]
    assert "CO2 shortage affects responsive L. bulgaricus" in c["description"]
    for node in [c, d]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert {t["term"]["id"] for t in node["participating_taxa"]} == {
            "NCBITaxon:1308",
            "NCBITaxon:1585",
        }
        assert not any(k in node for k in ["source_taxon", "target_taxon", "interaction_type"])


def test_yogurt_nox_keeps_intervention_early_recipient_and_final_null():
    _, _, docs = records()
    d = docs[3]["ecological_interactions"][3]
    assert "disrupting S. thermophilus nox" in d["description"]
    assert "slowed skim-milk acidification" in d["description"]
    assert "not L. bulgaricus growth" in d["description"]
    assert "final Streptococcus counts converged" in d["description"]
    assert "Pfl is HYPOTHESIZED" in d["downstream"][0]["description"]
    assert "threefold decrease" in docs[3]["discussions"][-1]["evidence"][0]["snippet"]


def test_zymomonas_rescue_is_positive_and_pairs_are_separate():
    _, _, docs = records()
    a, _, c = docs[4]["ecological_interactions"]
    assert "spent medium and individual amino-acid supplementation rescued" in a["description"]
    assert "not describe a four-member consortium" in a["description"]
    assert "three separate pairs" in c["description"]
    assert "species-resolved flow cytometry" in c["description"]
    assert "does not establish long-term community stability" in c["description"]


def test_zymomonas_sulfur_rescue_is_not_exclusive_glutathione():
    _, _, docs = records()
    b = docs[4]["ecological_interactions"][1]
    assert (
        "Cysteine and glutathione supplementation independently supported rescue"
        in b["description"]
    )
    assert "free cysteine below detection was not excluded" in b["description"]
    assert b["evidence"][0]["supports"] == "PARTIAL"
    assert b["evidence"][-1]["supports"] == "SUPPORT"
    assert "exclusive necessity" in b["downstream"][0]["description"]


def test_hcom_outcomes_have_direct_evidence_and_not_facilitation():
    _, _, docs = records()
    a, b, c = docs[5]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [a, b, c])
    assert "increased stability to fecal challenge" in b["evidence"][0]["snippet"]
    assert "colonization resistance" in c["evidence"][0]["snippet"]
    assert b["evidence"][0]["evidence_source"] == c["evidence"][0]["evidence_source"] == "IN_VIVO"


def test_hcom_donor_and_mediator_limits_remain():
    _, _, docs = records()
    a, b, c = docs[5]["ecological_interactions"]
    assert "weaker resilience to unrelated fecal donors" in b["description"]
    assert "not proof that each bacterial member is protective" in c["description"]
    assert "HYPOTHESIZED mediation:" in a["downstream"][1]["description"]
    assert "necessary" in a["downstream"][1]["description"]
    assert "issue 765" in docs[5]["discussions"][-1]["rationale"]


def test_ledger_preserves_topology_history_and_limited_caches():
    ledger, rows, docs = records()
    counts = ledger["reviewed_counts"]
    assert (counts["original_nodes"], counts["retained_nodes"], counts["removed_nodes"]) == (
        15,
        15,
        0,
    )
    assert (counts["original_arrows"], counts["retained_arrows"], counts["removed_arrows"]) == (
        8,
        8,
        0,
    )
    assert counts["renamed_nodes"] == 6 and counts["new_discussions"] == 6
    assert not ledger["independent_approval"]
    assert ledger["unresolved_research_issues"] == [1968]
    assert ledger["unresolved_non_graph_issues"] == [1969, 1970, 1971, 765]
    assert len(ledger["cache_changes"]) == 5
    assert sum(c["before_sha256"] is None for c in ledger["cache_changes"]) == 1
    for cache in ledger["cache_changes"]:
        assert (
            hashlib.sha256((ROOT / cache["path"]).read_bytes()).hexdigest() == cache["after_sha256"]
        )
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and doc["curation_history"][-1]["llm_assisted"]
        names = [n["name"] for n in doc["ecological_interactions"]]
        assert [n["node"] for n in row["node_decisions"]] == names
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
        assert all(
            e["target"] in names
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        )
