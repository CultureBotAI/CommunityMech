"""Keep positive assay results while bounding causal interpretations."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch74.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    docs = [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]
    return ledger, rows, docs


def test_core_enrichment_is_not_universal_membership_or_proven_symbiosis():
    _, _, docs = records()
    plasmid, function, core = docs[0]["ecological_interactions"]
    assert plasmid["name"].startswith("Putative Plasmid")
    assert "98%" in plasmid["description"]
    assert "HYPOTHESIZED" in plasmid["description"]
    assert "20 of 25" in function["description"]
    assert "18.5%-68.5%" in core["description"]
    assert "cyanobacteria-free controls were absent" in core["description"]
    assert "not absence of host or inoculum effects" in core["evidence"][0]["explanation"]
    assert "independent recruitment" not in core["evidence"][0]["explanation"]
    assert all("interaction_type" not in node for node in [plasmid, function, core])
    assert all("downstream" not in node for node in [plasmid, function, core])


def test_detoxification_retains_positive_effect_and_formaldehyde_free_control():
    _, _, docs = records()
    toxin, mitigation, _, competition = docs[1]["ecological_interactions"]
    assert "0.6-0.8 mM" in toxin["description"]
    assert "0.5 mM" in toxin["description"]
    edge = toxin["downstream"][0]
    assert edge["target"] == mitigation["name"]
    assert "formaldehyde-free PCA control" in edge["description"]
    assert "lowers measurable formaldehyde" in mitigation["description"]
    assert "not completely ameliorate" in mitigation["description"]
    assert "secreted inhibitor" in competition["description"]
    assert "downstream" not in competition


def test_methionine_direction_and_conditional_rescue_are_explicit():
    _, _, docs = records()
    exchange = docs[1]["ecological_interactions"][2]
    assert exchange["interaction_type"] == "CROSS_FEEDING"
    assert exchange["source_taxon"]["term"]["id"] == "NCBITaxon:408"
    assert exchange["target_taxon"]["term"]["id"] == "NCBITaxon:1708"
    for term in ["CM4744", "methanol or succinate", "wild-type", "reverse-direction"]:
        assert term in exchange["description"]
    assert "do not demonstrate autonomous" in exchange["description"]
    assert exchange["metabolites"][0]["term"]["id"] == "CHEBI:16811"


def test_moss_outcomes_are_preserved_without_shared_outcome_direction():
    ledger, _, docs = records()
    colonization, growth, metabolites = docs[2]["ecological_interactions"]
    assert colonization["downstream"][0]["description"].startswith("PARTIAL -")
    assert "significant combined-treatment improvements" in growth["description"]
    assert "downstream" not in growth
    assert "interaction_type" not in growth and "interaction_type" not in metabolites
    assert "D-ribose and D-gluconate" in metabolites["description"]
    assert "parallel reported treatment outcomes" in metabolites["description"]
    assert sum("visually matched" in s["method"] for s in ledger["snippet_checks"]) == 4


def test_mucin_preserves_substrate_response_and_glycan_distinctions():
    _, _, docs = records()
    composition, degradation, fermentation = docs[3]["ecological_interactions"]
    assert composition["downstream"][0]["description"].startswith("PARTIAL -")
    assert "rather than holding substrate fixed" in composition["downstream"][0]["description"]
    assert "N-glycans are completely degraded" in degradation["description"]
    assert "some remain detectable at120 h" in degradation["description"]
    assert "yeast-extract fermentation" in fermentation["description"]
    assert len(docs[3]["discussions"]) == 2
    assert (
        docs[3]["discussions"][0]["discussion_id"] == "mucin-mdsc-pairwise-crossfeeding-resolution"
    )
    assert docs[3]["curation_history"][-2]["action"] == "FIX_MDSC_GTDB_GROUNDINGS"


def test_all_nodes_and_original_arrows_have_decisions_without_extensions():
    ledger, rows, docs = records()
    assert sum(len(row["node_decisions"]) for row in rows) == 13
    assert sum(len(row["edges_before"]) for row in rows) == 7
    assert sum(len(row["edges_after"]) for row in rows) == 3
    assert sum(len(row["removed_edge_decisions"]) for row in rows) == 4
    assert ledger["cache_matched_graph_snippet_count"] == 21
    assert ledger["edison"]["provider_submissions"] == 0
    assert ledger["unresolved_non_graph_issues"] == [1624]
    for row, doc in zip(rows, docs, strict=True):
        renames = row["renamed_nodes"]
        original = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        retained = {(e["source"], e["target"]) for e in row["edges_after"]}
        removed = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        assert original == retained | removed and not retained & removed
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_record_hashes_and_append_only_histories_are_bound_to_review():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    for row, doc in zip(rows, docs, strict=True):
        assert row["status"] == "reviewed" and row["outcome"] == "changed"
        assert row["allowed_changed_fields"] == [
            "curation_history",
            "discussions",
            "ecological_interactions",
        ]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert all((ROOT / path).exists() for path in row["history_files"])
