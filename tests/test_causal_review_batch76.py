"""Keep measured outcomes separate from inferred physiology and context arrows."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch76.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_mat_transcripts_remain_measured_but_polymer_flux_is_proposed():
    _, _, docs = records()
    expression, storage, _, _ = docs[0]["ecological_interactions"]
    assert "measured diel expression" in expression["description"]
    assert expression["name"] == "Putative Diel Phototrophic Carbon Fixation"
    assert [e["supports"] for e in expression["evidence"]] == ["PARTIAL", "SUPPORT"]
    assert all(e["supports"] == "PARTIAL" for e in storage["evidence"])
    assert storage["downstream"][0]["target"] == expression["name"]
    assert storage["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert "not a demonstrated effect" in storage["downstream"][0]["description"]
    assert "not directly measured" in storage["description"]


def test_mat_spatial_potential_is_not_directional_nitrogen_transfer():
    _, _, docs = records()
    _, _, nitrogen, structure = docs[0]["ecological_interactions"]
    assert "source_taxon" not in nitrogen and "target_taxon" not in nitrogen
    assert [t["term"]["id"] for t in nitrogen["participating_taxa"]] == [
        "NCBITaxon:1129",
        "NCBITaxon:28261",
    ]
    assert "not demonstrated" in nitrogen["description"]
    assert "partial genomes does not establish pathway absence" in nitrogen["description"]
    assert "not exclusive occupancy" in structure["description"]
    assert "downstream" not in structure


def test_floc_assembly_retains_positive_outcome_and_actual_conditions():
    _, _, docs = records()
    colonies, clusters, model = docs[1]["ecological_interactions"]
    assert "stable nitrifier microcolonies" in colonies["description"]
    assert colonies["downstream"][0]["target"] == clusters["name"]
    for term in ["3000 g", "10 min", "calcium-rich", "10 days", "real positive result"]:
        assert term in clusters["description"]
    assert "not fully decoupled" in clusters["description"]
    assert "Release alone did not" in clusters["description"]
    assert "FISH preparation caused separate artefactual" in clusters["description"]
    assert "downstream" not in clusters and "downstream" not in model
    assert "not a separate downstream biological event" in model["description"]


def test_ndc_sparse_aggregate_graph_preserves_prior_assay_fixes():
    _, rows, docs = records()
    row, doc = rows[2], docs[2]
    assert row["outcome"] == "unchanged" and row["status"] == "reviewed"
    assert row["original_sha256"] == row["record_sha256"]
    assert row["curation_events_added"] == 0 and row["history_files"] == []
    (node,) = doc["ecological_interactions"]
    assert "interaction_type" not in node and "downstream" not in node
    assert len(node["participating_taxa"]) == 6
    assert "89.3%, 88.1%, 85.5%, and 95.3%" in node["evidence"][0]["snippet"]


def test_naica_oxidation_term_and_inferred_activity_are_distinct_from_assimilation():
    _, _, docs = records()
    thermo, ammonia, _ = docs[3]["ecological_interactions"]
    assert "not a measured growth-temperature response" in thermo["description"]
    assert ammonia["name"].startswith("Putative")
    assert ammonia["biological_processes"][0]["term"] == {
        "id": "GO:0019329",
        "label": "ammonia oxidation",
    }
    assert all("concentration" not in m for m in ammonia["metabolites"])
    assert all(e["supports"] == "PARTIAL" for e in ammonia["evidence"])
    assert ammonia["evidence"][0]["snippet"].startswith("genes encoding")
    assert ammonia["evidence"][1]["snippet"].startswith("These organisms")


def test_naica_negative_pcr_is_not_absence_competition_or_causation():
    _, _, docs = records()
    nodes = docs[3]["ecological_interactions"]
    sulfate = nodes[2]
    assert "Negative PCR is not pathway absence" in sulfate["description"]
    assert "not a donor-rescue experiment" in sulfate["description"]
    assert all("interaction_type" not in n and "downstream" not in n for n in nodes)
    assert [e["supports"] for e in sulfate["evidence"]] == ["SUPPORT", "PARTIAL"]
    assert sulfate["evidence"][0]["snippet"].endswith("dissimilatory sulfite reductase")


def test_every_original_node_and_arrow_has_a_decision_without_new_topology():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 11
    assert sum(len(r["edges_before"]) for r in rows) == 6
    assert sum(len(r["edges_after"]) for r in rows) == 2
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 4
    assert ledger["primary_graph_snippet_count"] == 18
    assert ledger["cache_matched_graph_snippet_count"] == 18
    assert all(c["independent_primary_match"] for c in ledger["snippet_checks"])
    for row, doc in zip(rows, docs, strict=True):
        rename = row["renamed_nodes"]
        original = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        remaining = {(e["source"], e["target"]) for e in row["edges_after"]}
        removed = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        assert remaining.isdisjoint(removed) and remaining | removed == original
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            a.split("#", 1)[1] in names
            for d in doc.get("discussions", [])
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_scoped_history_hashes_and_unresolved_metadata_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1632, 1633, 1634]
    assert ledger["unresolved_non_graph_issues"] == [1635]
    assert ledger["unresolved_research_issues"] == []
    assert ledger["edison"]["provider_submissions"] == 0
    assert sum(r["curation_events_added"] for r in rows) == 3
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        changed = row["outcome"] == "changed"
        assert row["curation_events_added"] == len(row["history_files"]) == int(changed)
        assert row["allowed_changed_fields"] == (
            ["curation_history", "discussions", "ecological_interactions"] if changed else []
        )
        if changed:
            assert doc["curation_history"][-1]["llm_assisted"] is True
        assert all((ROOT / p).exists() for p in row["history_files"])
