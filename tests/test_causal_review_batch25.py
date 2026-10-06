"""Keep measured assays distinct from field association and proposed resource flux."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-two-records-batch25.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_copper_intrinsic_capacity_and_field_subset_have_correct_scope():
    _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    for index, taxon in [(0, "NCBITaxon:920"), (2, "NCBITaxon:930"), (4, "NCBITaxon:28034")]:
        assert nodes[index]["scope"] == "PAIRWISE"
        assert nodes[index]["source_taxon"]["term"]["id"] == taxon
        assert not {"target_taxon", "participating_taxa", "interaction_type"} & nodes[index].keys()
    assert nodes[1]["scope"] == nodes[3]["scope"] == "COMMUNITY_LEVEL"
    assert len(nodes[1]["participating_taxa"]) == 2
    assert len(nodes[3]["participating_taxa"]) == 5
    assert all("interaction_type" not in n for n in nodes)
    assert all(
        p["term"]["id"] != "GO:0006826" for n in nodes for p in n.get("biological_processes", [])
    )


def test_copper_preserves_positive_assays_and_nonmonotonic_leaching():
    _, docs = records()
    early, aged, sulfur, output, sulfo = docs[0]["ecological_interactions"]
    assert "15% to the approximately 5% abiotic level" in early["description"]
    assert "Ferroplasma was around 10^3 copies/mL" in aged["description"]
    assert "L. ferrooxidans, not this canonical species" in aged["description"]
    assert "rRNA measurements support activity" in sulfur["description"]
    assert "not constant sulfur flux" in sulfur["description"]
    assert "400-day leaching cycle" in output["description"]
    assert "triple culture did not outperform the binaries" in output["description"]
    assert "38 +/- 2 C" in sulfo["description"] and "45 C" in sulfo["description"]
    assert "approximately 30% copper extraction" in sulfo["description"]
    assert "Genus-level Sulfobacillus RNA" in sulfo["description"]
    assert all(e["evidence_source"] == "OTHER" for e in output["evidence"])
    assert sulfur["evidence"][1]["evidence_source"] == "OTHER"


def test_copper_retains_bounded_bidirectional_substrate_feedback():
    _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    output = nodes[3]
    others = [n for n in nodes if n is not output]
    assert {e["target"] for e in output["downstream"]} == {n["name"] for n in others}
    assert all(n["downstream"][0]["target"] == output["name"] for n in others)
    assert all(
        e["description"].startswith("PARTIAL -") for n in nodes for e in n.get("downstream", [])
    )


def test_coscinodiscus_dmsp_is_potential_not_measured_transfer():
    _, docs = records()
    production, dmsp, *_ = docs[1]["ecological_interactions"]
    assert production["scope"] == "PAIRWISE"
    assert production["source_taxon"]["term"]["id"] == "NCBITaxon:33642"
    assert "participating_taxa" not in production and "target_taxon" not in production
    assert len(dmsp["participating_taxa"]) == 2 and "source_taxon" not in dmsp
    assert dmsp["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    provenance = dmsp["evidence"][0]["computational_provenance"]
    assert provenance["prediction_type"] == "SEQUENCE_HOMOLOGY"
    assert provenance["tools"] == [{"tool_name": "BLASTP"}]
    assert "negative growth result does not itself prove absence" in dmsp["description"]
    assert production["downstream"][0]["target"] == dmsp["name"]
    assert production["downstream"][0]["description"].startswith("HYPOTHESIZED -")


def test_coscinodiscus_keeps_pooled_assay_and_nonresponding_control():
    _, docs = records()
    nutrient = docs[1]["ecological_interactions"][3]
    assert len(nutrient["participating_taxa"]) == 3
    assert nutrient["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert nutrient["evidence"][0]["supports"] == "SUPPORT"
    for phrase in [
        "pooled 13-amino-acid mixture plus vitamins",
        "CS4 did not respond",
        "not merely genomic predictions",
        "does not establish which individual nutrient was limiting",
    ]:
        assert phrase in nutrient["description"]
    assert {m["term"]["id"] for m in nutrient["metabolites"]} == {"CHEBI:33709", "CHEBI:33229"}


def test_coscinodiscus_signs_and_model_are_partner_phase_and_condition_specific():
    _, docs = records()
    nodes = docs[1]["ecological_interactions"]
    phases, output = nodes[2], nodes[4]
    assert all("interaction_type" not in n for n in nodes)
    assert "recovery to control-like density after day 9" in phases["description"]
    assert "CS1 was inhibited significantly on days 11-21" in phases["description"]
    assert "CS4/Rose1 showed no significant diatom effect" in phases["description"]
    assert "distinct days 1-17 and 17-41 parameter sets" in output["description"]
    assert "very-late survival benefit" in output["description"]
    assert "not proven universally absent" in output["description"]
    assert phases["downstream"][0]["target"] == output["name"]
    assert phases["downstream"][0]["description"].startswith("PARTIAL -")


def test_batch25_sources_and_cache_limit_are_explicit():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["open_nongraph_followups"] == [1358, 1359]
    assert len(ledger["records"][0]["source_review"]) == 6
    source = ledger["records"][1]["source_review"]["PMID:36300970"]
    assert "Complete primary main body" in source["reviewed_scope"]
    assert "No figure images or supplementary files inspected" in source["reviewed_scope"]
    assert source["new_body_quotes_words"] == 15
    quotes = [docs[1]["ecological_interactions"][i]["evidence"][0]["snippet"] for i in [0, 1, 3]]
    assert sum(len(q.split()) for q in quotes) == 15
    cache = (ROOT / "references_cache/PMID_36300970.md").read_text()
    assert "content_type: abstract_only" in cache
    assert all(q not in cache for q in quotes)
    assert "#1358" in docs[0]["discussions"][0]["rationale"]
    assert "#1359" in docs[1]["discussions"][0]["rationale"]


def test_batch25_accounts_for_every_node_arrow_history_and_unchanged_cache():
    ledger, docs = records()
    rows = ledger["records"]
    assert len(rows) == 2
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 10
    assert sum(len(r["renamed_nodes"]) for r in rows) == 7
    assert not any(r["removed_edge_decisions"] for r in rows)
    assert sum(len(r["history_files"]) for r in rows) == 2
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        edges = [
            {"source": n["name"], **e}
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        ]
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
    assert len(ledger["reference_cache_original_hashes"]) == 8
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
