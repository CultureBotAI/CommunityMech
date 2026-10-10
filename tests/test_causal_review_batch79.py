"""Preserve positive outcomes without promoting assay/model scope to resolved flux."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch79.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_frc_controlled_tolerance_and_selection_survive():
    _, _, docs = records()
    tolerance, dominance, redox = docs[0]["ecological_interactions"]
    assert "Eight Rhodanobacter" in tolerance["description"]
    assert "186 tested isolates" in tolerance["description"]
    assert "not a whole-groundwater-community perturbation" in tolerance["description"]
    assert "some Pseudomonas isolates tolerate neutral-pH mixtures" in tolerance["description"]
    assert [e["target"] for e in tolerance["downstream"]] == [dominance["name"]]
    assert (
        "experimentally supported selection mechanism" in tolerance["downstream"][0]["description"]
    )
    assert "downstream" not in redox


def test_frc_uranyl_and_genus_scope_do_not_imply_nitrate_selection_or_exchange():
    _, _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert all(
        n["metabolites"][0]["term"] == {"id": "CHEBI:43515", "label": "dioxouranium(2+)"}
        for n in nodes[:2]
    )
    assert all("interaction_type" not in n for n in nodes)
    assert "source_taxon" not in nodes[1]
    assert "not a selectively toxic driver" in nodes[1]["description"]
    assert nodes[1]["evidence"][0]["supports"] == "SUPPORT"
    assert "accessible abstract does not quantify" in nodes[2]["description"]
    assert all(e["supports"] == "PARTIAL" for e in nodes[2]["evidence"])
    assert docs[0]["taxonomy"][0]["taxon_term"]["term"]["id"] == "NCBITaxon:666685"


def test_ogataea_rescue_is_not_measured_directed_exchange():
    _, _, docs = records()
    rescue, sulfur, _ = docs[1]["ecological_interactions"]
    assert rescue["interaction_type"] == "MUTUALISM"
    assert "range 27.3-28.5 spans this pair" in rescue["description"]
    assert "methanol growth remained below FY00" in rescue["description"]
    assert "labeled derivatives used for population tracking" in rescue["description"]
    assert sulfur["description"].startswith("HYPOTHESIZED -")
    assert "not measured interstrain transfer" in sulfur["description"]
    assert "not sodium sulfide" in sulfur["description"]
    assert [e["supports"] for e in sulfur["evidence"]] == ["PARTIAL", "SUPPORT"]
    assert sulfur["source_taxon"]["term"]["id"] == sulfur["target_taxon"]["term"]["id"]
    assert sulfur["source_taxon"]["preferred_term"] != sulfur["target_taxon"]["preferred_term"]


def test_ogataea_ratio_effect_retains_high_and_low_growth_arms():
    _, rows, docs = records()
    ratio = docs[1]["ecological_interactions"][2]
    assert "1:10, 1:5 and 1:1 achieved higher final biomass" in ratio["description"]
    assert "5:1 and 10:1 maintained met10Delta dominance but grew weakly" in ratio["description"]
    assert "not evidence that every culture increased" in ratio["description"]
    assert "interaction_type" not in ratio
    assert rows[1]["status"] == "needs_research"
    assert all("downstream" not in n for n in docs[1]["ecological_interactions"])
    assert len(ratio["participating_taxa"]) == 2


def test_okeke_positive_isolate_activities_and_proposed_contributions_remain():
    _, _, docs = records()
    cellulose, xylan, combined = docs[2]["ecological_interactions"]
    assert "27.83 and 31.22" in cellulose["description"] and "18.07" in cellulose["description"]
    assert "103.05" in xylan["description"] and "7.72" in xylan["description"]
    for node in [cellulose, xylan]:
        assert node["evidence"][0]["supports"] == "SUPPORT"
        assert node["downstream"][0]["target"] == combined["name"]
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert all("interaction_type" not in n for n in [cellulose, xylan, combined])


def test_okeke_access_limit_does_not_establish_absent_experiments():
    _, rows, docs = records()
    node = docs[2]["ecological_interactions"][2]
    assert node["description"].startswith("HYPOTHESIZED -")
    assert "not demonstrated absent" in node["description"]
    assert "lignin breakdown" in node["description"]
    assert [e["supports"] for e in node["evidence"]] == ["SUPPORT", "PARTIAL"]
    assert rows[2]["status"] == "needs_research"
    assert "authorized full text" in docs[2]["discussions"][0]["rationale"]


def test_rumen_lab_result_and_genome_complement_remain_with_limits():
    _, _, docs = records()
    lab, genomes, _ = docs[3]["ecological_interactions"]
    assert "66.84%" in lab["description"] and "20.56%" in lab["description"]
    assert "Dry-matter degradation and gas production were not different" in lab["description"]
    assert "not the initial seven-member" in lab["description"]
    assert "not a justified final 61-mL bottle concentration" in lab["description"]
    assert "47 GH and 19 CBM" in genomes["description"]
    assert "not measured expression" in genomes["description"]
    assert len(genomes["evidence"]) == 3
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in genomes["evidence"])


def test_rumen_cattle_trends_and_bags_are_not_significant_independent_replication():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][2]
    assert "2.61%/7.81%/11.47% were not statistically significant" in node["description"]
    assert "lower at 12 h, higher at 24/48 h" in node["description"]
    assert "not nine independent cattle" in node["description"]
    assert "propionate did not differ" in node["description"]
    assert node["evidence"][0]["supports"] == "SUPPORT"
    assert all("downstream" not in n for n in docs[3]["ecological_interactions"])


def test_every_node_and_arrow_is_decided_without_unapproved_extension():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 12
    assert sum(len(r["edges_before"]) for r in rows) == 4
    assert sum(len(r["edges_after"]) for r in rows) == 3
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    assert (
        ledger["primary_graph_snippet_count"] == ledger["cache_matched_graph_snippet_count"] == 21
    )
    for row, doc in zip(rows, docs, strict=True):
        rename = row["renamed_nodes"]
        before = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        after = {(e["source"], e["target"]) for e in row["edges_after"]}
        removed = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        assert after.isdisjoint(removed) and before == after | removed
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            a.split("#", 1)[1] in names
            for d in doc.get("discussions", [])
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_history_and_research_lifecycle_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1652, 1653, 1654, 1655]
    assert ledger["unresolved_research_issues"] == [1656, 1657]
    assert ledger["unresolved_non_graph_issues"] == [1658]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert len(ledger["edison"]["dry_runs"]) == 1
    assert ledger["edison"]["dry_runs"][0]["query_chars"] == 11815
    for row, doc in zip(rows, docs, strict=True):
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert all((ROOT / p).exists() for p in row["history_files"])
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
