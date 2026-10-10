"""Keep Avena and Chlorella causal claims within the measured assay scope."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-two-records-batch12.yaml"


def record(stem):
    return yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())


def test_avena_groups_and_diversity_do_not_prove_substrate_partitioning():
    doc = record("Avena_Rhizosphere_Detritusphere_Niche_Succession")
    succession, guild, transcripts, coexistence, carbon = doc["ecological_interactions"]
    assert len(doc["taxonomy"]) == 1
    assert doc["taxonomy"][0]["taxon_term"]["term"]["id"] == "NCBITaxon:2"
    assert "transcriptional succession, not measured reaction flux" in succession["description"]
    assert "Low Response lacks a clear habitat preference" in guild["description"]
    assert guild["interaction_type"] == coexistence["interaction_type"] == "NICHE_PARTITIONING"
    assert guild["description"].startswith("PARTIAL")
    assert "80-percent-identity" in guild["description"]
    assert "did not significantly increase" in coexistence["description"]
    assert "not measured enzyme activity" in transcripts["description"]
    assert carbon["description"].startswith("HYPOTHESIZED")
    assert not succession.get("downstream") and not coexistence.get("downstream")
    assert guild["downstream"][0]["target"] == coexistence["name"]
    assert transcripts["downstream"][0]["target"] == carbon["name"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED") for n in (guild, transcripts)
    )


def test_chlorella_keeps_real_mutualism_and_partial_resource_use():
    doc = record("Chlorella_Azospirillum_Synthetic_Mutualism")
    mutualism, exchange, _, _ = doc["ecological_interactions"]
    assert mutualism["interaction_type"] == "MUTUALISM"
    assert "illuminated" in mutualism["description"]
    assert "did not differ significantly" in mutualism["description"]
    assert exchange["interaction_type"] == "CROSS_FEEDING"
    assert exchange["description"].startswith("PARTIAL")
    assert "thiamine diphosphate" in exchange["description"]
    assert "undetected" in exchange["description"]
    assert "neither uniquely bacterial nor specific" in exchange["description"]
    assert all(e["supports"] == "PARTIAL" for e in exchange["evidence"])
    assert [t["strain_designation"]["strain_name"] for t in doc["taxonomy"]] == ["UTEX 2714", "Cd"]


def test_chlorella_proximity_is_not_proven_colonization_facilitation():
    mutualism, _, aggregation, _ = record("Chlorella_Azospirillum_Synthetic_Mutualism")[
        "ecological_interactions"
    ]
    assert "interaction_type" not in aggregation
    assert "engineered proximity" in aggregation["description"]
    assert aggregation["downstream"][0]["target"] == mutualism["name"]
    assert aggregation["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert "not selectively disrupted" in aggregation["downstream"][0]["description"]


def test_chlorella_starch_is_not_mutualism_or_a_cd_knockout_result():
    _, exchange, _, starch = record("Chlorella_Azospirillum_Synthetic_Mutualism")[
        "ecological_interactions"
    ]
    assert "interaction_type" not in starch
    assert "dark, aerobic, glucose-fed" in starch["description"]
    assert "Sp6-derived" in starch["description"]
    assert "reduced algal population growth" in starch["description"]
    assert "nonsignificant" in starch["description"]
    assert exchange["downstream"][0]["target"] == starch["name"]
    assert exchange["downstream"][0]["description"].startswith("PARTIAL")
    assert "not a Cd mutant" in exchange["downstream"][0]["description"]


def test_fems_cache_declares_actual_excerpt_scope_without_new_body_text():
    text = (ROOT / "references_cache/doi_10.1093_femsec_fiw077.md").read_text()
    meta = yaml.safe_load(text.split("---", 2)[1])
    assert meta["content_type"] == "abstract_and_methods_excerpts"
    assert meta["source_url"].startswith("https://academic.oup.com/")
    assert "not a complete abstract" in meta["excerpt_scope"]
    assert "ASCII" in meta["text_normalization"]
    assert "No additional article body" in text
    assert "license" not in meta


def test_batch12_decisions_cover_nodes_removed_edges_and_valid_anchors():
    rows = yaml.safe_load(LEDGER.read_text())["records"]
    assert len(rows) == 2
    assert sum(len(r["node_decisions"]) for r in rows) == 9
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 4
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 2
    for row in rows:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        nodes = doc["ecological_interactions"]
        names = {n["name"] for n in nodes}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in nodes
        )
        edges = [{"source": n["name"], **e} for n in nodes for e in n.get("downstream", [])]
        assert row["edges_after"] == edges
        assert all(e["target"] in names for e in edges)
        assert any(
            d["kind"] == "KNOWLEDGE_GAP" and d["status"] == "OPEN" for d in doc["discussions"]
        )
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
        renames = row.get("renamed_nodes", {})
        before = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        assert before == {
            (e["source"], e["target"])
            for e in row["retained_edge_decisions"] + row["removed_edge_decisions"]
        }
