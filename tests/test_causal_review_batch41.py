"""Keep hypothesis strength, assay scope and research completeness explicit."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch41.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_ferroplasma_retains_hypothesis_not_demonstrated_detoxification():
    _, docs = records()
    supply, consumption, _, response = docs[0]["ecological_interactions"]
    for node in [supply, consumption]:
        assert node["description"].startswith("HYPOTHESIZED:")
        assert node["evidence"][0]["supports"] == "PARTIAL"
        assert node["evidence"][0]["snippet"].startswith("The hypothesis of this work")
    assert supply["downstream"][0]["target"] == consumption["name"]
    assert supply["downstream"][0]["description"].startswith("HYPOTHESIZED:")
    assert "downstream" not in consumption
    assert "not independent measurement" in response["description"]
    assert "interaction_type" not in response and "metabolites" not in response


def test_ferroplasma_intrinsic_context_has_no_false_niche_or_transport():
    _, docs = records()
    supply, consumption, iron, _ = docs[0]["ecological_interactions"]
    for node in [supply, iron]:
        assert node["scope"] == "PAIRWISE"
        assert "source_taxon" in node
        assert all(
            key not in node
            for key in [
                "target_taxon",
                "participating_taxa",
                "interaction_type",
                "biological_processes",
            ]
        )
    assert "Y(T)" in iron["description"] and "not BRL-115" in iron["description"]
    assert "slower electron transfer" in iron["description"]
    assert "do not establish lower-oxygen complementarity" in iron["description"]
    assert [t["term"]["id"] for t in consumption["metabolites"]] == ["CHEBI:50860"]


def test_fomitopsis_liquid_observation_is_not_selective_mediation():
    _, docs = records()
    liquid = docs[1]["ecological_interactions"][0]
    assert "Associated" in liquid["name"]
    assert liquid["description"].startswith("PARTIAL:")
    assert liquid["interaction_type"] == "COMPETITION"
    assert "34 mg (reported as 44% lower)" in liquid["description"]
    assert "do not describe selective glucose rescue" in liquid["description"]
    assert "not production or identification" in liquid["description"]
    assert "Endpoint bacterial counts were not reduced" in liquid["description"]
    assert all("downstream" not in n for n in docs[1]["ecological_interactions"])


def test_fomitopsis_agar_identity_and_acid_mediation_remain_qualified():
    _, docs = records()
    agar = docs[1]["ecological_interactions"][1]
    assert "interaction_type" not in agar
    assert "putatively identified" in agar["description"]
    assert "HYPOTHESIZED:" in agar["description"]
    assert "not shown to be universally absent" in agar["description"]
    assert "distinct from liquid-culture stress" in agar["description"]
    assert agar["evidence"][-1]["supports"] == "PARTIAL"
    assert (
        "not a claim of universal experimental absence" in docs[1]["discussions"][-1]["rationale"]
    )


def test_lung_missing_graph_is_not_certified_complete():
    ledger, docs = records()
    row = ledger["records"][2]
    assert row["status"] == "needs_research"
    assert "ecological_interactions" not in docs[2]
    assert row["node_decisions"] == row["edges_after"] == []
    assert ledger["open_graph_research"] == [1461]
    assert len(docs[2]["taxonomy"]) == 4
    gap = docs[2]["discussions"][-1]
    assert gap["kind"] == "KNOWLEDGE_GAP" and gap["status"] == "OPEN"
    assert "attaches_to" not in gap
    for boundary in [
        "total CFU does not resolve member-specific compositional resilience",
        "hypothesis-qualified treatment",
        "not physiological healthy-airway conditions",
        "Challenge organisms are not members",
    ]:
        assert boundary in gap["rationale"]


def test_batch41_edison_dryrun_and_source_limits_are_auditable():
    ledger, _ = records()
    edison = ledger["edison"]
    assert edison["community"] == "CommunityMech:000432"
    assert edison["provider_job_submitted"] is edison["provider_credits_spent"] is False
    meta = edison["dryrun_meta"]
    assert meta["status"] == "dry-run" and meta["query_chars"] == 7671
    assert hashlib.sha256(meta["query"].encode()).hexdigest() == edison["query_sha256"]
    ferro, fomitopsis, lung = [r["source_review"] for r in ledger["records"]]
    assert "abstract" in ferro["PMID:27535541"]["scope"]
    assert "HTTP 429" in next(iter(fomitopsis.values()))["scope"]
    assert "preprint" in next(iter(fomitopsis.values()))["scope"]
    primary = lung["PMID:42545019"]
    assert (
        primary["receipt"]["source_sha256"]
        == "d26528baa780d0c4344ae24938862ad9d52a0d6143e490e9bcd10f9b03d73c5d"
    )
    assert "No figure images" in primary["scope"]
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected


def test_batch41_dispositions_participants_and_append_only_history():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1459, 1460]
    assert ledger["open_nongraph_followups"] == [1462, 1463]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 6
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 1
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 1
    assert sum(len(r["renamed_nodes"]) for r in ledger["records"]) == 5
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        canonical = {t["taxon_term"]["term"]["id"]: t["taxon_term"] for t in doc["taxonomy"]}
        names = {n["name"] for n in doc.get("ecological_interactions", [])}
        for node in doc.get("ecological_interactions", []):
            participants = node.get("participating_taxa", [])
            participants += [node[k] for k in ["source_taxon", "target_taxon"] if k in node]
            for term in participants:
                assert term["term"] == canonical[term["term"]["id"]]["term"]
            assert all(
                e["target"] in names and e["target"] != node["name"]
                for e in node.get("downstream", [])
            )
        assert all(
            a.split("#", 1)[1] in names for a in doc["discussions"][-1].get("attaches_to", [])
        )


def test_batch41_preserves_pre_paper_baseline_across_ancestry_change():
    ledger, _ = records()
    ancestry = ledger["baseline_ancestry_change"]
    assert ledger["baseline_commit"] == ancestry["old_head"]
    assert ledger["base_commit"] == ancestry["new_head"]
    assert ledger["base_commit"] != ledger["baseline_commit"]
    assert ledger["base_tree"] == ancestry["tree"]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
