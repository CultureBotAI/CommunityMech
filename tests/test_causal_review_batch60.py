"""Pin KZ assay limits, KMC hypothesis scope and the unresolved empty relay graph."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-kz-kmc-komagataella-batch60.yaml"
KZ = "Klebsiella_Arthrobacter_KZ_Phenanthrene_Cadmium_SynCom"
KMC = "Kombucha_KMC_IMBG1_Fermentation_Community"
KOM = "Komagataella_Ecoli_Coinducible_Biosynthesis_Coculture"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(row["path"]).stem: row for row in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / row["path"]).read_text()) for name, row in rows.items()}
    return ledger, rows, docs


def test_kz_preserves_positive_assays_without_directed_transfer():
    _, rows, docs = records()
    (node,) = docs[KZ]["ecological_interactions"]
    assert rows[KZ]["status"] == "needs_research"
    assert node["scope"] == "COMMUNITY_LEVEL"
    assert not any(
        key in node for key in ["source_taxon", "target_taxon", "interaction_type", "downstream"]
    )
    assert [term["term"]["id"] for term in node["participating_taxa"]] == [
        "NCBITaxon:570",
        "NCBITaxon:1663",
    ]
    assert "better phenanthrene degradation and mineralization" in node["description"]
    assert "Biomass-normalized enzyme assays" in node["description"]
    assert "not a resolved donor-to-recipient transfer" in node["description"]
    assert node["evidence"][0]["supports"] == "PARTIAL"
    assert node["evidence"][1]["supports"] == "SUPPORT"


def test_kz_correction_is_not_assumed_irrelevant_or_resolved():
    _, _, docs = records()
    gaps = docs[KZ]["discussions"]
    assert gaps[0]["discussion_id"] == "kz_cultivation_and_inoculation_details"
    text = gaps[-1]["rationale"]
    assert "PMID:41456976" in text
    assert "metadata only, not its body" in text
    assert "Do not assume the correction is biologically immaterial" in text
    assert "#1541" in text and gaps[-1]["status"] == "OPEN"


def test_kmc_retains_the_source_explicit_spatial_model_as_hypothesized():
    ledger, rows, docs = records()
    cooperation, pellicle, composition = docs[KMC]["ecological_interactions"]
    assert len(rows[KMC]["edges_before"]) == 2 and len(rows[KMC]["edges_after"]) == 1
    assert cooperation["description"].startswith("HYPOTHESIZED - ")
    assert cooperation["evidence"][0]["supports"] == "PARTIAL"
    (edge,) = pellicle["downstream"]
    assert edge["target"] == cooperation["name"]
    assert edge["description"].startswith("HYPOTHESIZED - ")
    assert "not a selective test" in edge["description"]
    assert pellicle["evidence"][-1]["snippet"] == ledger["primary_matched_fragment"]
    assert "downstream" not in composition


def test_kmc_preserves_composition_and_persistence_without_niche_or_mutualism_claim():
    _, _, docs = records()
    cooperation, pellicle, composition = docs[KMC]["ecological_interactions"]
    assert "not an exhaustive identical membership" in cooperation["description"]
    assert "microscopy reports mixed bacterial and yeast morphotypes" in pellicle["description"]
    assert "persisted through passages" in composition["description"]
    assert (
        "relative sequence profiles do not establish absolute growth" in composition["description"]
    )
    for node in [cooperation, pellicle, composition]:
        assert "interaction_type" not in node and "source_taxon" not in node
        assert [term["term"]["id"] for term in node["participating_taxa"]] == [
            "NCBITaxon:1434011",
            "NCBITaxon:441",
            "NCBITaxon:4919",
            "NCBITaxon:13366",
        ]
    assert "#1543" in docs[KMC]["discussions"][-1]["rationale"]


def test_komagataella_empty_structure_remains_an_explicit_research_gap():
    ledger, rows, docs = records()
    doc = docs[KOM]
    assert "ecological_interactions" not in doc
    assert rows[KOM]["status"] == "needs_research"
    assert rows[KOM]["node_decisions"] == rows[KOM]["edges_after"] == []
    assert ledger["unresolved_research_issues"] == [1541, 1542]
    assert doc["discussions"][0]["discussion_id"] == "kphaffii_ecoli_relayed_intermediate"
    gap = doc["discussions"][-1]
    assert gap["attaches_to"] == ["ecological_interactions", "engineering_design"]
    assert "does not prove biological neutralism" in gap["rationale"]
    assert "sharing an induction signal is not metabolite cross-feeding" in gap["rationale"]
    assert "needs_research, not absent biology" in gap["rationale"]


def test_komagataella_edison_provenance_is_an_unpaid_single_community_dry_run():
    ledger, _, _ = records()
    receipt = ledger["edison_dry_run"]
    path = ROOT / receipt["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == receipt["sha256"]
    meta = yaml.safe_load(path.read_text())
    assert meta["community_id"] == "CommunityMech:000343"
    assert meta["status"] == "dry-run" and meta["job"] == "LITERATURE"
    assert len(meta["query"]) == meta["query_chars"] == 7457
    assert hashlib.sha256(meta["query"].encode()).hexdigest() == receipt["query_sha256"]
    assert receipt["provider_submissions"] == receipt["credits_spent"] == 0


def test_batch60_selected_cache_bytes_remain_unchanged():
    ledger, _, _ = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    raw = (ROOT / "references_cache/PMID_26061774.md").read_text()
    assert "".join(ledger["primary_matched_fragment"].split()) in "".join(raw.split())


def test_batch60_every_node_arrow_and_new_anchor_is_accounted_for():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1539, 1540]
    assert ledger["unresolved_non_graph_issues"] == [1543]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    assert (
        len(rows[KMC]["retained_edge_decisions"]) == len(rows[KMC]["removed_edge_decisions"]) == 1
    )
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1
        assert row["source_review"]["cache_provenance_certified"] is False
        names = {node["name"] for node in doc.get("ecological_interactions", [])}
        assert {decision["node"] for decision in row["node_decisions"]} == names
        if name != KOM:
            assert {
                anchor.split("#", 1)[1] for anchor in doc["discussions"][-1]["attaches_to"]
            } == names
        assert doc["discussions"][-1]["status"] == "OPEN"
