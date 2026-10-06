"""Preserve assay boundaries, strain direction and measured-versus-modeled evidence."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch34.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_drought_genomic_capacity_and_separate_assay_boundaries():
    _, docs = records()
    genomic, mutant, iron = docs[0]["ecological_interactions"]
    assert all("downstream" not in n for n in [genomic, mutant, iron])
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in genomic["evidence"])
    assert "Ten of fifteen" in genomic["description"]
    assert "not microbial expression" in genomic["description"]
    assert "maize" in mutant["description"] and "watered controls" in mutant["description"]
    assert "not significant under drought" in mutant["description"]
    assert "not their coculture or the field microbiome" in iron["description"]
    assert "Fe3+-EDTA" in iron["description"]
    assert iron["evidence"][0]["supports"] == "PARTIAL"


def test_dual_bacillus_exclusion_direction_preserves_distinct_strains():
    _, docs = records()
    detox, succession, _ = docs[1]["ecological_interactions"]
    assert detox["source_taxon"]["preferred_term"].startswith("Bacillus coagulans DSM1")
    assert succession["source_taxon"]["preferred_term"] == "Bacillus coagulans CC17B-1"
    assert succession["target_taxon"]["preferred_term"].startswith("Bacillus coagulans DSM1")
    assert succession["source_taxon"]["term"] == succession["target_taxon"]["term"]
    assert "interaction_type" not in succession and "biological_processes" not in succession
    assert "CFU measures culturability" in succession["description"]
    assert "product inhibition" in succession["description"]
    assert detox["downstream"][0]["target"] == succession["name"]
    assert detox["downstream"][0]["description"].startswith("HYPOTHESIZED -")


def test_dual_staging_is_not_simultaneous_growth_or_direct_pad_catalysis():
    _, docs = records()
    detox, _, scavenger = docs[1]["ecological_interactions"]
    assert "not demonstrated direct PAD catalysis" in detox["description"]
    assert "donor neutrality is not established" in detox["description"]
    assert scavenger["scope"] == "COMMUNITY_LEVEL"
    assert not {"source_taxon", "target_taxon", "interaction_type"} & scavenger.keys()
    assert len(scavenger["participating_taxa"]) == 3
    assert len({p["preferred_term"] for p in scavenger["participating_taxa"]}) == 3
    assert len({p["term"]["id"] for p in scavenger["participating_taxa"]}) == 2
    assert "30 C for 12 h" in scavenger["description"]
    assert "50 C anaerobic" in scavenger["description"]
    assert "after another 12 h" in scavenger["description"]
    assert scavenger["downstream"][0]["target"] == detox["name"]
    assert scavenger["downstream"][0]["description"].startswith("PARTIAL -")


def test_enigma_exchange_preserves_both_directions_and_inference_limits():
    _, docs = records()
    cooperation, _, _ = docs[2]["ecological_interactions"]
    assert "3H11 supplies nitrite to R12" in cooperation["description"]
    assert "transfer from R12 to 3H11 is a kinetic-model inference" in cooperation["description"]
    assert "not directly measured NO flux" in cooperation["description"]
    assert "not obligate partner dependence" in cooperation["description"]
    assert "not a direct N2 measurement" in cooperation["description"]
    assert cooperation["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert cooperation["evidence"][0]["supports"] == "PARTIAL"
    assert cooperation["evidence"][1]["evidence_source"] == "IN_VITRO"
    assert cooperation["evidence"][1]["supports"] == "SUPPORT"


def test_enigma_negative_link_is_nitrite_not_n2o_toxicity():
    _, docs = records()
    cooperation, imbalance, toxicity = docs[2]["ecological_interactions"]
    for node in [cooperation, imbalance, toxicity]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert not {"source_taxon", "target_taxon", "interaction_type"} & node.keys()
        assert len(node["participating_taxa"]) == 2
    assert imbalance["downstream"][0]["target"] == toxicity["name"]
    assert toxicity["downstream"][0]["target"] == cooperation["name"]
    assert all(
        n["downstream"][0]["description"].startswith("PARTIAL -") for n in [imbalance, toxicity]
    )
    assert "nutritional complementarity" in imbalance["description"]
    assert "predicted nitrite exposure" in toxicity["description"]
    assert "N2O accumulation was measured" in toxicity["description"]
    assert "N2O is the inhibitory agent" in toxicity["downstream"][0]["description"]


def test_batch34_canonical_strain_terms_exact_anchors_histories_and_hashes():
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
                original = canonical[(term["term"]["id"], term["preferred_term"])]
                assert term["term"] == original["term"]
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


def test_batch34_every_original_arrow_accounted_for_after_renames():
    ledger, docs = records()
    assert ledger["independent_approval"] is False and ledger["issues"] == [1410, 1411, 1412]
    assert all(r["status"] == "reviewed" for r in ledger["records"])
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 9
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 4
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 2
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


def test_batch34_preserved_metadata_and_access_limits_are_not_certified():
    ledger, docs = records()
    assert ledger["open_nongraph_followups"] == [647, 1413, 1414, 1415]
    assert ledger["open_graph_research"] == []
    assert docs[0]["growth_media"] == []
    assert docs[0]["taxonomy"][0]["functional_role"] == ["PRIMARY_DEGRADER"]
    assert "no_provider_job_or_charge" in ledger["edison"]["status"]
    assert ledger["issue_deduplication"]["ignored_hidden_local_files_included"] is True
    assert ledger["issue_deduplication"]["comments_exhaustive"] is False
