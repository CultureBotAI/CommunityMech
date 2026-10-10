"""Guard measured endpoints, alternative routes and unresolved graph expansion."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch37.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_argmet_preserves_distinct_genotypes_and_conditional_reciprocity():
    _, docs = records()
    met, arg, noise = docs[0]["ecological_interactions"]
    assert met["source_taxon"] == arg["target_taxon"]
    assert met["target_taxon"] == arg["source_taxon"]
    assert met["source_taxon"]["term"] == met["target_taxon"]["term"]
    assert met["source_taxon"]["preferred_term"] != met["target_taxon"]["preferred_term"]
    assert [n["interaction_type"] for n in [met, arg, noise]] == [
        "CROSS_FEEDING",
        "CROSS_FEEDING",
        "MUTUALISM",
    ]
    assert "supplemented cultures" in met["description"]
    assert "Supplementation" in arg["description"]
    assert "coefficient of variation" in noise["description"]
    assert "not a direct measurement of intrinsic transcriptional noise" in noise["description"]
    assert "biological_processes" not in noise
    assert all("downstream" not in n for n in [met, arg, noise])


def test_argmet_expansion_is_not_counted_complete():
    ledger, docs = records()
    assert ledger["records"][0]["status"] == "needs_research"
    assert ledger["open_graph_research"] == [1436]
    assert ledger["edison"]["status"] == "dry_run_only_no_provider_job_or_charge"
    assert ledger["edison"]["prompt_characters"] == 11543
    assert ledger["edison"]["receipt"]["exit_code"] == 0
    assert ledger["edison"]["receipt"]["actual_provider_job"] is False
    assert "modeled diffusion/uptake" in docs[0]["discussions"][-1]["rationale"]
    assert "BL21/environmental-isolate" in docs[0]["discussions"][-1]["rationale"]
    assert len(docs[0]["discussions"]) == 3


def test_vfa_has_two_qualified_links_not_a_prediction_to_flux_chain():
    _, docs = records()
    hrt, spatial, prediction, removal, acetate = docs[1]["ecological_interactions"]
    assert [e["target"] for e in hrt["downstream"]] == [spatial["name"]]
    assert hrt["downstream"][0]["description"].startswith("PARTIAL -")
    assert [e["target"] for e in spatial["downstream"]] == [removal["name"]]
    assert spatial["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert all("downstream" not in n for n in [prediction, removal, acetate])
    for node in [hrt, spatial, prediction, removal, acetate]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert len(node["participating_taxa"]) == 3
        assert not {"interaction_type", "biological_processes"} & node.keys()
    assert "sequential HRT phases" in hrt["description"]
    assert "representative genera" in hrt["description"]
    assert "PICRUSt2" in prediction["description"]
    assert "not itself a causal actor" in prediction["description"]
    assert prediction["evidence"][1]["supports"] == "PARTIAL"
    assert removal["evidence"][0]["supports"] == "PARTIAL"
    assert acetate["evidence"][2]["supports"] == "PARTIAL"


def test_toluene_preserves_alternatives_and_distinct_mag_labels():
    _, docs = records()
    control, anode, cathode = docs[2]["ecological_interactions"]
    for node in [control, anode, cathode]:
        assert node["description"].startswith("HYPOTHESIZED -")
        assert not {"downstream", "interaction_type", "biological_processes"} & node.keys()
        assert all(e["supports"] == "PARTIAL" for e in node["evidence"])
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
    assert "Methanosarcina OR Methanothrix" in control["description"]
    assert "e-pili OR acetate" in control["description"]
    assert "(or Methanothrix" in control["evidence"][0]["snippet"]
    assert "MAG10 engaged" in anode["evidence"][0]["snippet"]
    assert "MAG116 and the anode" in anode["evidence"][0]["snippet"]
    assert "does not resolve donor-to-recipient direction" in anode["description"]
    assert cathode["scope"] == "PAIRWISE"
    assert cathode["source_taxon"]["preferred_term"] == "Aminidesulfovibrio sp. MAG60"
    assert control["participating_taxa"][0]["preferred_term"] == "Syntrophobacteraceae MAG116"
    assert control["participating_taxa"][0]["term"] == cathode["source_taxon"]["term"]
    assert cathode["target_taxon"]["preferred_term"] == "Methanobacterium sp. MAG74"


def test_batch37_canonical_participants_history_and_hashes():
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
        assert doc["discussions"][-1]["kind"] == "KNOWLEDGE_GAP"
        assert doc["discussions"][-1]["status"] == "OPEN"
        for gap in doc["discussions"]:
            assert all(
                anchor.split("#", 1)[1] in names
                for anchor in gap.get("attaches_to", [])
                if anchor.startswith("ecological_interactions#")
            )
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_batch37_all_existing_nodes_and_arrows_have_dispositions():
    ledger, docs = records()
    assert ledger["independent_approval"] is False and ledger["issues"] == [1431, 1432, 1433]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 11
    assert all(not r["removed_node_decisions"] for r in ledger["records"])
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 2
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 3
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert not row["renamed_nodes"]
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        assert {(e["source"], e["target"]) for e in row["edges_before"]} == {
            (e["source"], e["target"]) for e in row["edges_after"] + row["removed_edge_decisions"]
        }
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest


def test_batch37_access_limits_and_nongraph_followups_are_explicit():
    ledger, docs = records()
    assert ledger["open_nongraph_followups"] == [373, 1434, 1435]
    assert "abstract only" in ledger["records"][2]["source_review"]["PMID:38865893"]["scope"]
    vfa_source = ledger["records"][1]["source_review"]["doi:10.21203/rs.3.rs-9518331/v1"]
    assert "ResearchGate mirror" in vfa_source["scope"]
    assert "not peer-reviewed" in vfa_source["scope"]
    assert (
        docs[1]["taxonomy"][0]["taxon_term"]["gtdb_classification"]["gtdb_id"]
        == "GTDB:g__Enterococcus_B"
    )
    assert docs[2]["taxonomy"][3]["taxon_term"]["term"] == {
        "id": "NCBITaxon:2629275",
        "label": "unclassified Desulfoprunum",
    }
    assert ledger["issue_deduplication"]["ignored_hidden_local_files_included"] is True
    assert ledger["issue_deduplication"]["comments_exhaustive"] is False
