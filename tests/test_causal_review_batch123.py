"""Preserve observed endpoints and explicit inference limits in four graphs."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch123.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_five_positive_perturbations_do_not_imply_failed_completion():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][0]
    assert "positive composition-perturbation effects" in node["description"]
    assert "All tested consortia completed fermentation" in node["description"]
    assert "produced significant impacts" in node["evidence"][0]["snippet"]
    assert "were not addressed" in node["evidence"][1]["snippet"]


def test_five_competition_remains_a_qualified_inference():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][1]
    assert node["interaction_type"] == "COMPETITION"
    assert node["name"].startswith("Inferred ")
    assert node["evidence"][0]["supports"] == "PARTIAL"
    assert "not absolute viable population size" in node["description"]
    assert "candidate mechanisms" in node["description"]


def test_five_strain_effects_are_panel_specific_and_not_saccharomyces_silence():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][2]
    assert "particular strains tested" in node["description"]
    assert "still had detectable effects" in node["description"]
    assert "Table 1 names the ten strains" in docs[0]["discussions"][0]["rationale"]
    assert not any(n.get("downstream") for n in docs[0]["ecological_interactions"])


def test_three_keeps_growth_and_qualifies_suppression():
    _, _, docs = records()
    a, b, _ = docs[1]["ecological_interactions"]
    assert "established numerical dominance" in a["description"]
    assert "HYPOTHESIZED" in b["description"]
    assert b["evidence"][1]["supports"] == "PARTIAL"
    assert "indirect pairwise confirmation" in b["description"]
    assert "interaction_type" not in b and not b.get("downstream")


def test_three_keeps_amino_acid_early_effect_late_null_and_source_limits():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][2]
    assert "higher in the indirect-contact condition" in node["description"]
    assert "no significant difference after 9 h" in node["description"]
    assert "after 9 h" in node["evidence"][-1]["snippet"]
    assert "does not by itself demonstrate" in node["description"]
    assert "histidine, methionine and tryptophan" in node["description"]
    assert (
        docs[1]["discussions"][0]["discussion_id"]
        == "wine_yeast_indirect_contact_amino_acid_source"
    )


def test_wolffia_compartments_are_not_selectively_demonstrated_filtering():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][0]
    assert "interaction_type" not in node
    assert "operational sterilized-tissue fraction" in node["description"]
    assert "not a strictly epiphytic sample" in node["description"]
    assert node["evidence"][0]["supports"] == "PARTIAL"


def test_wolffia_potential_is_not_exchange_or_strain_matched_validation():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][1]
    assert "interaction_type" not in node and not node.get("downstream")
    assert "HYPOTHESIZED cross-feeding" in node["description"]
    assert "not strain-matched endophytes" in node["description"]
    assert "reconstruction limitations" in node["description"]
    assert len(node["participating_taxa"]) == 7
    assert docs[2]["discussions"][0]["discussion_id"] == "direct_cobamide_exchange_not_measured"


def test_wolffia_provenance_is_gene_content_not_flux_simulation():
    _, _, docs = records()
    evidence = docs[2]["ecological_interactions"][1]["evidence"][2]
    provenance = evidence["computational_provenance"]
    assert evidence["evidence_source"] == "COMPUTATIONAL"
    assert provenance["prediction_type"] == "OTHER"
    assert "At least three compatible" in provenance["parameters"]
    assert "not FBA, direct flux or abundance correlation" in provenance["parameters"]
    assert [t["tool_name"] for t in provenance["tools"]] == ["MetaBat2", "MetaErg", "igraph"]
    assert not any(t.get("tool_version") for t in provenance["tools"])


def test_woll_transfer_is_hypothesized_and_carbohydrate_loss_is_not_tracing():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][0]
    assert node["name"].startswith("Hypothesized ")
    assert "interaction_type" not in node
    assert "Medium sucrose consumption" in node["description"]
    assert "does not trace" in node["description"]
    assert node["evidence"][0]["supports"] == "PARTIAL"


def test_woll_metabolite_changes_are_bulk_and_not_uniform():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][1]
    assert "interaction_type" not in node
    assert "bulk concentrations, not gene-expression measurements" in node["description"]
    assert "mixed-culture oxalic acid was much lower" in node["description"]
    assert node["evidence"][1]["supports"] == "PARTIAL"
    assert "100% CMS-1." in node["evidence"][2]["snippet"]


def test_woll_retains_both_qualified_directions():
    _, _, docs = records()
    a, b, c = docs[3]["ecological_interactions"]
    assert len(a["downstream"]) == len(b["downstream"]) == 1
    assert a["downstream"][0]["target"] == b["name"]
    assert b["downstream"][0]["target"] == c["name"]
    assert a["downstream"][0]["description"].startswith("HYPOTHESIZED:")
    assert b["downstream"][0]["description"].startswith("PARTIAL:")


def test_woll_positive_leaching_is_not_carbon_sequestration():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][2]
    assert "interaction_type" not in node
    assert all(s in node["description"] for s in ["79.95%", "18.59%", "day 12"])
    assert "measure net CO2 sequestration" in node["description"]
    assert node["evidence"][0]["supports"] == "SUPPORT"
    assert node["evidence"][1]["supports"] == "PARTIAL"


def test_ledger_binds_topology_history_and_narrow_cache_append():
    ledger, rows, docs = records()
    counts = ledger["reviewed_counts"]
    assert (counts["original_nodes"], counts["retained_nodes"], counts["removed_nodes"]) == (
        11,
        11,
        0,
    )
    assert (counts["original_arrows"], counts["retained_arrows"], counts["removed_arrows"]) == (
        2,
        2,
        0,
    )
    assert counts["renamed_nodes"] == 3
    assert (counts["graph_quotations"], counts["discussion_quotations"]) == (22, 4)
    assert len(ledger["cache_changes"]) == 1 and not ledger["independent_approval"]
    cache = ledger["cache_changes"][0]
    assert cache["path"] == "references_cache/PMID_42784437.txt"
    assert hashlib.sha256((ROOT / cache["path"]).read_bytes()).hexdigest() == cache["after_sha256"]
    assert ledger["edison"]["provider_submissions"] == 0
    assert ledger["unresolved_non_graph_issues"] == [1958, 1959, 1960, 1961]
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
