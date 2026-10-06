"""Guard source-specific assay, sampling and participant boundaries."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch35.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_dental_coaggregation_does_not_mediate_acidification_by_assay_order():
    _, docs = records()
    mitis, sanguinis, acid = docs[0]["ecological_interactions"]
    assert all(
        "downstream" not in n and "interaction_type" not in n for n in [mitis, sanguinis, acid]
    )
    for node in [mitis, sanguinis]:
        assert node["scope"] == "PAIRWISE" and "biological_processes" not in node
        assert node["source_taxon"]["preferred_term"] == "Actinomyces naeslundii"
        assert "separate planktonic assay" in node["description"]
    assert mitis["target_taxon"]["preferred_term"] == "Streptococcus mitis"
    assert sanguinis["target_taxon"]["preferred_term"] == "Streptococcus sanguinis"
    assert "15 min" in mitis["description"] and "2 h" in sanguinis["description"]
    assert acid["scope"] == "COMMUNITY_LEVEL" and len(acid["participating_taxa"]) == 5
    assert "no-glucose control remained above pH 7" in acid["description"]
    assert "not demonstrated niche partitioning" in acid["description"]
    assert "distinct stages" in acid["description"]


def test_floodplain_core_does_not_credit_noncore_or_wrong_rank_members():
    _, docs = records()
    doc = docs[1]
    reservoir, capacity, transcript = doc["ecological_interactions"]
    assert all("downstream" not in n for n in [reservoir, capacity, transcript])
    expected = [doc["taxonomy"][i]["taxon_term"]["preferred_term"] for i in [0, 3]]
    for node in [reservoir, capacity]:
        assert [p["preferred_term"] for p in node["participating_taxa"]] == expected
    assert "42 representative genomes" in reservoir["description"]
    assert "89 of 94" in reservoir["description"]
    assert "did not predict" in reservoir["description"]
    assert [p["term"]["id"] for p in transcript["participating_taxa"]] == ["NCBITaxon:28216"]
    assert doc["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] == "WITHHELD"
    assert "Nitrospira genus ID" in doc["discussions"][0]["rationale"]
    assert "disconnected warnings" in doc["discussions"][0]["rationale"]


def test_floodplain_transcription_is_a_bounded_snapshot_not_flux():
    _, docs = records()
    transcript = docs[1]["ecological_interactions"][2]
    assert "Floodplain L" in transcript["name"]
    assert "September 2016 floodplain L RNA snapshot" in transcript["description"]
    assert "not a carbon manipulation, measured flux" in transcript["description"]
    assert "overall transcription favored higher organic carbon" in transcript["description"]
    assert transcript["evidence"][0]["supports"] == "PARTIAL"
    assert "abstract" in transcript["evidence"][0]["explanation"]
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in transcript["evidence"])


def test_hillslope_retains_only_hypothesized_environmental_arrows():
    _, docs = records()
    filtering, function, lineages, selenium = docs[2]["ecological_interactions"]
    assert {e["target"] for e in filtering["downstream"]} == {
        function["name"],
        lineages["name"],
        selenium["name"],
    }
    assert all(e["description"].startswith("HYPOTHESIZED -") for e in filtering["downstream"])
    assert all(e["supports"] == "PARTIAL" for e in filtering["evidence"])
    assert "DNA abundances" in function["description"]
    assert "RNA was extracted for another study" in function["description"]
    assert "two Yanofskybacteria" in lineages["description"]
    assert "unknown hosts" in lineages["description"]
    assert "biological_processes" not in lineages
    assert "selenate-reduction potential" in selenium["description"]
    assert "lacks chemistry" in selenium["description"]
    assert "water-quality improvement were not measured" in selenium["description"]


def test_hillslope_compartments_are_not_collapsed_to_shared_id():
    _, docs = records()
    filtering = docs[2]["ecological_interactions"][0]
    assert len(filtering["participating_taxa"]) == 3
    assert len({p["term"]["id"] for p in filtering["participating_taxa"]}) == 1
    assert len({p["preferred_term"] for p in filtering["participating_taxa"]}) == 3
    for node in docs[2]["ecological_interactions"]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert not {"source_taxon", "target_taxon", "interaction_type"} & node.keys()


def test_batch35_canonical_participants_anchors_history_and_record_hashes():
    ledger, docs = records()
    for row, doc in zip(ledger["records"], docs, strict=True):
        canonical = {
            (t["taxon_term"]["term"]["id"], t["taxon_term"]["preferred_term"]): t["taxon_term"]
            for t in doc["taxonomy"]
        }
        names = {n["name"] for n in doc["ecological_interactions"]}
        for node in doc["ecological_interactions"]:
            terms = node.get("participating_taxa", []) + [
                node[k] for k in ["source_taxon", "target_taxon"] if k in node
            ]
            for term in terms:
                assert (
                    term["term"] == canonical[(term["term"]["id"], term["preferred_term"])]["term"]
                )
            assert all(
                e["target"] in names and e["target"] != node["name"]
                for e in node.get("downstream", [])
            )
        (gap,) = doc["discussions"]
        assert gap["kind"] == "KNOWLEDGE_GAP" and gap["status"] == "OPEN"
        assert set(gap["attaches_to"]) == {"ecological_interactions#" + n for n in names}
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_batch35_complete_original_arrow_accounting():
    ledger, docs = records()
    assert ledger["independent_approval"] is False and ledger["issues"] == [1417, 1418, 1419]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 10
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 3
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 4
    for row, doc in zip(ledger["records"], docs, strict=True):
        rename = row["renamed_nodes"]

        def remap(edge, rename=rename):
            return (
                rename.get(edge["source"], edge["source"]),
                rename.get(edge["target"], edge["target"]),
            )

        assert not row["removed_node_decisions"]
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        assert {remap(e) for e in row["edges_before"]} == {
            (e["source"], e["target"]) for e in row["edges_after"]
        } | {remap(e) for e in row["removed_edge_decisions"]}
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest


def test_batch35_non_graph_metadata_and_source_access_are_not_certified():
    ledger, docs = records()
    assert ledger["open_nongraph_followups"] == [1420, 1421, 1422]
    assert ledger["open_graph_research"] == []
    assert docs[2]["taxonomy"][2]["functional_role"] == ["CROSS_FEEDER", "SYNTROPHIC_PARTNER"]
    assert "fed with sterile saliva" in docs[0]["growth_media"][0]["name"]
    assert "no_provider_job_or_charge" in ledger["edison"]["status"]
    assert ledger["issue_deduplication"]["ignored_hidden_local_files_included"] is True
    assert ledger["issue_deduplication"]["comments_exhaustive"] is False
