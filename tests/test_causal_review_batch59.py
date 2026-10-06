"""Pin kefir assay limits and the unresolved empty dairy-panel graph."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-kefir-dairy-batch59.yaml"
KEFIR = "Kefir_Flavor_Lentilactobacillus_Kluyveromyces_Coculture"
DAIRY = "Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / r["path"]).read_text()) for name, r in rows.items()}
    return ledger, rows, docs


def test_kefir_removes_only_procedure_nodes_without_restoring_workflow_arrows():
    _, rows, docs = records()
    row, doc = rows[KEFIR], docs[KEFIR]
    assert len(doc["ecological_interactions"]) == 4
    assert {n["node"] for n in row["removed_node_decisions"]} == {
        "Dominant Kefir Genera Prioritization",
        "SLAM023B-SLAM005Y Coculture Genome Sequencing",
    }
    assert not row["edges_before"] and not row["edges_after"]
    assert all("downstream" not in n for n in doc["ecological_interactions"])
    assert "Removed five downstream edges" in doc["curation_history"][0]["changes"]


def test_kefir_canonical_strains_are_explicit_on_each_retained_node():
    _, _, docs = records()
    doc = docs[KEFIR]
    assert [t["taxon_term"]["term"]["id"] for t in doc["taxonomy"]] == [
        "NCBITaxon:33962",
        "NCBITaxon:4911",
    ]
    for node in doc["ecological_interactions"]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert "source_taxon" not in node and "interaction_type" not in node
        assert [t["preferred_term"] for t in node["participating_taxa"]] == [
            "Lentilactobacillus kefiri SLAM023B",
            "Kluyveromyces marxianus SLAM005Y",
        ]


def test_kefir_preserves_capacity_and_profiles_without_asserting_transfer():
    _, _, docs = records()
    potential, profiles, _, exchange = docs[KEFIR]["ecological_interactions"]
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in potential["evidence"])
    assert "not measured expression" in potential["description"]
    assert "do not establish transfer" in profiles["description"]
    assert exchange["description"].startswith("HYPOTHESIZED - ")
    assert exchange["evidence"][0]["supports"] == "PARTIAL"
    assert "necessary mediation" in exchange["description"]


def test_kefir_compound_specific_null_effect_does_not_erase_positive_responses():
    _, _, docs = records()
    doc = docs[KEFIR]
    response = doc["ecological_interactions"][2]
    text = response["description"]
    assert "increased viable counts" in text
    assert "interactions for selected fatty-acid/aldehyde endpoints" in text
    assert "but not for five yeast-associated volatiles" in text
    assert "normalized GC-MS peak areas" in text
    assert "Discussion comparator conflict" in text
    assert "not sensory-panel scores" in text
    assert "modest acidification" in text
    gap = doc["discussions"][-1]["rationale"]
    for compound in [
        "ethyl acetate",
        "isobutanol",
        "isoamyl alcohol",
        "isoamyl acetate",
        "ethyl octanoate",
    ]:
        assert compound in gap
    assert "#1536" in gap


def test_dairy_empty_graph_is_research_work_not_certified_absence():
    ledger, rows, docs = records()
    row, doc = rows[DAIRY], docs[DAIRY]
    assert row["status"] == "needs_research"
    assert doc["ecological_interactions"] == []
    assert not row["node_decisions"] and not row["edges_before"] and not row["edges_after"]
    assert ledger["unresolved_research_issues"] == [1537]
    gap = doc["discussions"][-1]
    assert gap["status"] == "OPEN"
    assert gap["attaches_to"] == ["ecological_interactions", "taxonomy"]
    assert "not all four phototrophs in one bottle" in gap["rationale"]
    assert "FAPROTAX-predicted" in gap["rationale"]
    assert "not evidence that interactions are absent" in gap["rationale"]
    assert "only its abstract/highlights were reviewed" in gap["rationale"]


def test_dairy_edison_artifact_is_only_an_unpaid_single_community_dry_run():
    ledger, _, _ = records()
    receipt = ledger["edison_dry_run"]
    path = ROOT / receipt["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == receipt["sha256"]
    meta = yaml.safe_load(path.read_text())
    assert meta["community_id"] == "CommunityMech:000384"
    assert meta["status"] == "dry-run" and meta["job"] == "LITERATURE"
    assert meta["query_chars"] == len(meta["query"]) == 10945
    assert hashlib.sha256(meta["query"].encode()).hexdigest() == receipt["query_sha256"]
    assert receipt["provider_submissions"] == receipt["credits_spent"] == 0


def test_kefir_cache_preserves_original_prefix_and_labels_indexed_excerpt_scope():
    ledger, _, _ = records()
    update = ledger["reference_cache_update"]
    raw = (ROOT / update["path"]).read_bytes()
    prefix, appendix = raw.split(b"\n\n## Verified primary body excerpts", 1)
    assert hashlib.sha256(prefix).hexdigest() == update["original_sha256"]
    assert hashlib.sha256(raw).hexdigest() == update["updated_sha256"]
    assert sum(len(q.split()) for q in update["verified_excerpts"]) == 21
    assert all(q.encode() in appendix for q in update["verified_excerpts"])
    assert b"not a complete full-text cache" in appendix
    assert b"direct publisher access returned403" in appendix
    assert b"No access-control bypass" in appendix


def test_batch59_records_have_complete_decisions_and_exact_open_anchors():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1535]
    assert ledger["unresolved_non_graph_issues"] == [1536]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    assert rows[KEFIR]["status"] == "reviewed"
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1
        assert row["source_review"]["cache_provenance_certified"] is False
    names = {n["name"] for n in docs[KEFIR]["ecological_interactions"]}
    assert {r["node"] for r in rows[KEFIR]["node_decisions"]} == names
    assert {a.split("#", 1)[1] for a in docs[KEFIR]["discussions"][-1]["attaches_to"]} == names
    assert docs[KEFIR]["discussions"][-1]["status"] == "OPEN"
