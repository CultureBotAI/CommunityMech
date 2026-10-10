"""Preserve treatment benefits without inventing the mediating mechanism."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch122.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_tb_retains_positive_disease_control_without_competition():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][0]
    assert "interaction_type" not in node
    assert "70.97%" in node["description"]
    assert "70.97%" in node["evidence"][1]["snippet"]
    assert "not a TB member" in node["description"]
    assert len(node["participating_taxa"]) == 3


def test_tb_network_robustness_is_simulated_not_biological_removal():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][1]
    assert "interaction_type" not in node and "biological_processes" not in node
    assert "not biological removal experiments" in node["description"]
    assert "Hub-targeted simulations" in node["evidence"][1]["snippet"]
    assert "absolute viable abundance" in node["description"]


def test_tb_hypotheses_do_not_borrow_other_study_perturbations():
    _, _, docs = records()
    discussion = docs[0]["discussions"][-1]
    assert "working hypotheses" in discussion["evidence"][0]["snippet"]
    assert "not directly collected root exudates" in discussion["rationale"]
    assert "distinct six-strain SMC study" in discussion["rationale"]
    assert not any(n.get("downstream") for n in docs[0]["ecological_interactions"])


def test_dt_protection_is_not_inoculant_superiority_or_drought_validation():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][0]
    assert "43.3%" in node["description"]
    assert "pairwise differences were not significant" in node["description"]
    assert "not a test of whole-plant drought protection" in node["description"]
    assert "50.4%" in node["evidence"][0]["snippet"]


def test_dt_rna_changes_precede_challenge_and_keep_broad_null():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][1]
    assert "Before pathogen challenge" in node["description"]
    assert "no significant treatment shift" in node["description"]
    assert "not PICRUSt predictions" in node["description"]
    assert "not broad community changes" in node["evidence"][1]["snippet"]
    assert "not reference SynCom genomes" in node["evidence"][2]["snippet"]
    assert not node.get("downstream")


def test_dt_pathway_and_strain_identity_limits_remain_explicit():
    _, _, docs = records()
    discussion = docs[1]["discussions"][-1]
    assert "did not allow direct assignment" in discussion["evidence"][0]["snippet"]
    assert "strain-level identity cannot be confirmed" in discussion["evidence"][1]["snippet"]
    assert docs[1]["discussions"][0]["discussion_id"] == "prjna1405459_visibility"


def test_straw_process_outputs_are_not_reciprocal_mutualism():
    _, _, docs = records()
    nodes = docs[2]["ecological_interactions"]
    assert len(nodes) == 3 and all("interaction_type" not in n for n in nodes)
    assert "does not measure reciprocal fitness" in nodes[0]["description"]
    assert "downstream anaerobic-digestion community" in nodes[0]["description"]


def test_straw_retains_both_material_transfer_directions():
    _, _, docs = records()
    a, b, c = docs[2]["ecological_interactions"]
    assert len(a["downstream"]) == len(b["downstream"]) == 1
    assert a["downstream"][0]["target"] == b["name"]
    assert b["downstream"][0]["target"] == c["name"]
    assert "enzyme-mediated material-transfer" in a["downstream"][0]["description"]
    assert "supplies substrate" in b["downstream"][0]["description"]


def test_straw_preserves_positive_polymer_degradation_values():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][1]
    assert all(v in node["description"] for v in ["39.85%", "36.99%", "19.21%"])
    assert "acts through the enzyme preparation" in node["description"]
    assert "39.85" in node["evidence"][1]["snippet"]


def test_straw_total_biogas_is_not_methane_only_or_isolate_methanogenesis():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][2]
    assert "801.16 mL/g TS" in node["description"]
    assert "not a methane-only yield" in node["description"]
    assert "metabolites" not in node
    assert "cumulative biogas" in node["evidence"][0]["snippet"]


def test_sasw_water_outcome_is_combined_biocoating_not_syncom_alone():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][0]
    assert "biocoating-associated" in node["name"]
    assert "coating-only CC and SynCom-only BC" in node["description"]
    assert "does not isolate the microbial or EPS contribution" in node["description"]
    assert "BCC (biochar-consortium coating)" in node["evidence"][1]["snippet"]


def test_sasw_eps_mediation_remains_hypothesized():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][0]
    assert "interaction_type" not in node
    assert "HYPOTHESIZED" in node["description"]
    assert node["evidence"][0]["supports"] == "PARTIAL"
    assert node["evidence"][1]["supports"] == "SUPPORT"


def test_sasw_profiles_do_not_establish_viable_strains_or_causal_cascade():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][1]
    assert "interaction_type" not in node
    assert "do not uniquely identify viable inoculant strains" in node["description"]
    assert "do not prove BCAA transfer" in node["description"]
    assert node["evidence"][0]["supports"] == "PARTIAL"
    assert "En_BCC samples" in node["evidence"][1]["snippet"]


def test_sasw_prior_removals_and_positive_field_context_survive():
    _, _, docs = records()
    assert len(docs[3]["ecological_interactions"]) == 2
    assert not any(n.get("downstream") for n in docs[3]["ecological_interactions"])
    discussion = docs[3]["discussions"][-1]
    assert "Positive BCC field yields" in discussion["rationale"]
    assert "Two treatments were established" in discussion["evidence"][0]["snippet"]
    assert "PICRUSt2" in discussion["evidence"][1]["snippet"]
    assert docs[3]["discussions"][0]["attaches_to"] == ["taxonomy"]


def test_ledger_accounts_for_topology_history_and_unchanged_caches():
    ledger, rows, docs = records()
    counts = ledger["reviewed_counts"]
    assert (counts["original_nodes"], counts["retained_nodes"], counts["removed_nodes"]) == (
        9,
        9,
        0,
    )
    assert (counts["original_arrows"], counts["retained_arrows"], counts["removed_arrows"]) == (
        2,
        2,
        0,
    )
    assert counts["renamed_nodes"] == 1
    assert (counts["graph_quotations"], counts["discussion_quotations"]) == (17, 6)
    assert not ledger["cache_changes"] and not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == 0
    assert ledger["unresolved_non_graph_issues"] == [1951, 1952]
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and doc["curation_history"][-1]["llm_assisted"]
        names = [n["name"] for n in doc["ecological_interactions"]]
        assert [n["node"] for n in row["node_decisions"]] == names
        assert all(
            a.removeprefix("ecological_interactions#") in names
            for a in doc["discussions"][-1]["attaches_to"]
        )
        assert all(
            e["target"] in names
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        )
