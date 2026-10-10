"""Keep observed phenotypes distinct from inferred community mechanisms."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-soil-mucin-batch65.yaml"
A = "MSC1_Dominant_Core"
B = "MSC2_Model_Soil_Consortium"
C = "MUC2_Human_Gut_Commensal_Defined_Consortium"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / r["path"]).read_text()) for name, r in rows.items()}
    return ledger, rows, docs


def test_msc1_persistence_is_not_dependency_and_roster_is_partial():
    _, rows, docs = records()
    node = docs[A]["ecological_interactions"][0]
    for phrase in ["residual drift", "31", "approximately 35", "incomplete roster", "HYPOTHESIZED"]:
        assert phrase in node["description"]
    assert len(node["participating_taxa"]) == 9
    assert node["evidence"][1]["supports"] == "PARTIAL"
    assert rows[A]["edges_before"] == rows[A]["edges_after"] == []
    assert docs[A]["taxonomy"][4]["taxon_term"]["term"]["id"] == "NCBITaxon:85413"


def test_msc1_early_total_od_is_not_late_or_partner_resolved_benefit():
    _, _, docs = records()
    node = docs[A]["ecological_interactions"][1]
    for phrase in [
        "10 mM soluble",
        "expected average",
        "not significant in late",
        "does not resolve each partner",
        "partial set",
    ]:
        assert phrase in node["description"]
    assert len(node["participating_taxa"]) == 4
    assert "biological_processes" not in node


def test_msc1_hubs_are_computational_not_keystone_perturbations():
    _, _, docs = records()
    node = docs[A]["ecological_interactions"][2]
    for phrase in [
        "pooled normalized relative",
        "Rhizobiales is an order",
        "common environmental",
        "keystone necessity",
        "distinct contexts",
    ]:
        assert phrase in node["description"]
    assert len(node["participating_taxa"]) == 2
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])


def test_msc2_retains_biological_arrows_as_hypotheses_not_deleted_science():
    _, rows, docs = records()
    nodes = docs[B]["ecological_interactions"]
    assert len(rows[B]["edges_before"]) == len(rows[B]["edges_after"]) == 2
    assert len(rows[B]["retained_edge_decisions"]) == 2
    assert rows[B]["removed_edge_decisions"] == []
    for node in nodes[:2]:
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert "exclusive" in nodes[0]["downstream"][0]["description"]
    assert "No selective product rescue" in nodes[1]["downstream"][0]["description"]
    assert [len(n["participating_taxa"]) for n in nodes] == [5, 8, 1]


def test_msc2_pellet_metabolites_and_temporal_transcripts_are_not_transfer():
    _, _, docs = records()
    primary, sharing, phenotype = docs[B]["ecological_interactions"]
    for phrase in ["100 ppm", "500 ppm", "preconditioning", "18 mM ammonium"]:
        assert phrase in primary["description"]
    assert "cell-pellet extracts after supernatant removal" in sharing["description"]
    assert "without species boundaries" in sharing["description"]
    assert "not matched monoculture-versus-community expression" in phenotype["description"]
    assert "biological_processes" not in phenotype and "source_taxon" not in phenotype
    assert phenotype["evidence"][0]["supports"] == "PARTIAL"


def test_muc2_preserves_outcomes_without_common_treatment_arrow():
    _, rows, docs = records()
    profile, acids = docs[C]["ecological_interactions"]
    assert "calculated CFU equivalents" in profile["description"]
    assert "not direct viable counts" in profile["description"]
    assert "species-level genome sets" in profile["description"]
    for phrase in [
        "lower acetate",
        "higher propionate, butyrate and formate",
        "net extracellular concentration",
        "neither controlled nor measured",
        "daily 10%",
        "HYPOTHESIZED",
    ]:
        assert phrase in acids["description"]
    assert len(rows[C]["removed_edge_decisions"]) == 1
    assert rows[C]["edges_after"] == []
    old_gap = docs[C]["discussions"][0]
    assert old_gap["discussion_id"] == "kg-muc2-group-level-qpcr-resolution"
    assert old_gap["status"] == "OPEN"
    assert set(old_gap["attaches_to"]) == {
        "ecological_interactions#" + n["name"] for n in [profile, acids]
    }


def test_batch65_caches_and_canonical_participants_are_not_rewritten():
    ledger, _, docs = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for doc in docs.values():
        canonical = {
            t["taxon_term"]["preferred_term"]: t["taxon_term"]["term"] for t in doc["taxonomy"]
        }
        for node in doc["ecological_interactions"]:
            assert "interaction_type" not in node
            for taxon in node["participating_taxa"]:
                assert canonical[taxon["preferred_term"]] == taxon["term"]
        assert "#1569" in doc["discussions"][-1]["rationale"]
    assert ledger["unresolved_non_graph_issues"] == [1569]
    assert ledger["primary_graph_snippet_count"] == 12


def test_batch65_complete_ledger_history_and_source_limits():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1566, 1567, 1568]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 8
    assert sum(len(r["removed_node_decisions"]) for r in rows.values()) == 0
    assert sum(len(r["edges_before"]) for r in rows.values()) == 3
    assert sum(len(r["edges_after"]) for r in rows.values()) == 2
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1 and row["status"] == "reviewed"
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {d["node"] for d in row["node_decisions"]} == names
        assert {a.split("#", 1)[1] for a in doc["discussions"][-1]["attaches_to"]} == names
