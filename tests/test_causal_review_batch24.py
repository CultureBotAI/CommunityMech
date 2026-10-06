"""Preserve measured treatments, bounded mediation and a genuine no-change review."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-three-records-batch24.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_cordyceps_is_an_unchanged_bounded_endpoint_graph():
    ledger, docs = records()
    row, doc = ledger["records"][0], docs[0]
    assert row["outcome"] == "unchanged"
    assert row["original_sha256"] == row["record_sha256"]
    assert row["history_files"] == row["allowed_changed_fields"] == row["issues"] == []
    assert row["curation_events_added"] == 0
    assert len(doc["ecological_interactions"]) == 2
    assert not any(n.get("downstream") for n in doc["ecological_interactions"])
    assert all("interaction_type" not in n for n in doc["ecological_interactions"])
    assert "weak to moderate selective" in doc["ecological_interactions"][1]["description"]


def test_succinate_additive_is_external_and_transcript_response_is_source_only():
    _, docs = records()
    doc = docs[1]
    redox, transcript, output = doc["ecological_interactions"]
    assert redox["scope"] == output["scope"] == "COMMUNITY_LEVEL"
    assert redox["participating_taxa"] == output["participating_taxa"]
    assert not {"source_taxon", "target_taxon", "interaction_type"} & redox.keys()
    assert "externally supplied riboflavin" in redox["description"]
    assert "not resolve every additive/transcript assay to K1" in redox["description"]
    assert transcript["scope"] == "PAIRWISE"
    assert transcript["source_taxon"]["term"]["id"] == "NCBITaxon:1718"
    assert not {"target_taxon", "participating_taxa", "interaction_type"} & transcript.keys()
    assert "not directly traced carbon or electron flux" in transcript["description"]
    assert transcript["evidence"][0]["supports"] == "PARTIAL"
    assert redox["downstream"][0]["target"] == transcript["name"]
    assert redox["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert transcript["downstream"][0]["target"] == output["name"]
    assert transcript["downstream"][0]["description"].startswith("PARTIAL")


def test_succinate_parent_and_k1_outcomes_are_separate_and_positive():
    _, docs = records()
    output = docs[1]["ecological_interactions"][2]
    for phrase in [
        "parent-strain coculture yield of 0.169 g/g, 45.65%",
        "ldhA deletion abolished lactate formation in K1",
        "0.686 g/g",
        "up to 23.4% higher yield during extended fermentation",
        "do not establish thermodynamic syntrophy",
    ]:
        assert phrase in output["description"]
    assert output["evidence"][0]["supports"] == "SUPPORT"
    assert all("interaction_type" not in n for n in docs[1]["ecological_interactions"])


def test_fish_immune_and_barrier_measurements_do_not_prove_mediation():
    _, docs = records()
    immune, barrier, output = docs[2]["ecological_interactions"]
    for node in [immune, barrier, output]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert not {"source_taxon", "target_taxon", "interaction_type"} & node.keys()
        assert {p["term"]["id"] for p in node["participating_taxa"]} == {
            "NCBITaxon:180162",
            "NCBITaxon:1849822",
            "NCBITaxon:286",
        }
    assert "increased intestinal SOD, CAT, ACP and lysozyme" in immune["description"]
    assert "KEGG pathway annotation, not a direct IgA production assay" in immune["description"]
    assert "zo-1, occludin and claudin12 transcript levels" in barrier["description"]
    assert "DAO activity also increased" in barrier["description"]
    assert "not an unambiguous improvement in permeability" in barrier["description"]
    assert "not direct barrier-protein abundance" in barrier["description"]
    for node in [immune, barrier]:
        assert node["downstream"][0]["target"] == output["name"]
        assert node["downstream"][0]["description"].startswith("PARTIAL")


def test_fish_protection_keeps_qpcr_and_syncom_versus_fmt_boundaries():
    _, docs = records()
    output = docs[2]["ecological_interactions"][2]
    for phrase in [
        "60% survival versus 32.5%",
        "calibrated qPCR Aeromonas DNA loads",
        "not merely relative 16S profiles or viable-pathogen counts",
        "FMT survival comparison (66.7% versus 36.7%) is not the SynCom result",
    ]:
        assert phrase in output["description"]
    assert output["evidence"][0]["supports"] == "SUPPORT"


def test_batch24_source_access_and_metadata_followups_are_explicit():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["open_nongraph_followups"] == [1353, 1354]
    for row in ledger["records"][:2]:
        source = next(iter(row["source_review"].values()))
        assert "Complete primary abstract only" in source["reviewed_scope"]
    source = ledger["records"][2]["source_review"]["PMID:41280275"]
    assert "Complete primary main body" in source["reviewed_scope"]
    assert "No figure images or supplementary files inspected" in source["reviewed_scope"]
    assert "#1354" in docs[1]["discussions"][0]["rationale"]
    assert "#1353" in docs[2]["discussions"][0]["rationale"]


def test_batch24_accounts_for_every_node_arrow_history_and_cache():
    ledger, docs = records()
    rows = ledger["records"]
    assert len(rows) == 3
    assert sum(len(r["node_decisions"]) for r in rows) == 8
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 4
    assert sum(len(r["renamed_nodes"]) for r in rows) == 4
    assert not any(r["removed_edge_decisions"] for r in rows)
    assert sum(len(r["history_files"]) for r in rows) == 2
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        nodes = doc["ecological_interactions"]
        names = {n["name"] for n in nodes}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        edges = [{"source": n["name"], **e} for n in nodes for e in n.get("downstream", [])]
        assert edges == row["edges_after"]
        rename = row["renamed_nodes"]
        assert {(e["source"], e["target"]) for e in edges} == {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        assert all(
            a.split("#", 1)[1] in names
            for d in doc.get("discussions", [])
            for a in d.get("attaches_to", [])
            if a.startswith("ecological_interactions#")
        )
    assert len(ledger["reference_cache_original_hashes"]) == 3
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
