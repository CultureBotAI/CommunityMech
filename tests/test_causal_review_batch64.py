"""Separate measured outcomes from procedures and proposed causal mediators."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-assay-boundaries-batch64.yaml"
N = "Lunar_Simulant_Phosphate_Solubilizing_Bacteria_Nicotiana"
L = "Lupinus_SC7_Rhizosphere_SynCom"
M = "MAMC_M48_Lignocellulose"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / r["path"]).read_text()) for name, r in rows.items()}
    return ledger, rows, docs


def test_nicotiana_attachment_and_acids_remain_hypotheses():
    _, _, docs = records()
    attachment, phosphorus, _ = docs[N]["ecological_interactions"]
    assert "not direct biofilm imaging" in attachment["description"]
    assert "separate individual-strain" in attachment["description"]
    assert "HYPOTHESIZED" in attachment["description"]
    assert "specific secreted oxalate or citrate" in phosphorus["description"]
    assert "were not measured" in phosphorus["description"]
    assert len(phosphorus["metabolites"]) == 1
    for node in [attachment, phosphorus]:
        assert len(node["participating_taxa"]) == 5
        assert "biological_processes" not in node
        assert all(e["evidence_source"] == "IN_VITRO" for e in node["evidence"])


def test_nicotiana_plant_response_preserves_time_controls_and_supplementation():
    _, rows, docs = records()
    plant = docs[N]["ecological_interactions"][2]
    text = plant["description"]
    for phrase in [
        "315.92%",
        "204.08%",
        "percentages of control",
        "53.28%",
        "not pre-cultured",
        "MS nutrient supplementation",
        "missing canonical plant host",
    ]:
        assert phrase in text
    assert len(plant["participating_taxa"]) == 3
    assert all(e["evidence_source"] == "IN_VIVO" for e in plant["evidence"])
    assert len(rows[N]["removed_edge_decisions"]) == 2
    assert "PMID:42304108" in docs[N]["discussions"][-1]["rationale"]


def test_lupin_input_roster_keeps_two_distinct_streptomyces_strains():
    _, _, docs = records()
    for node in docs[L]["ecological_interactions"]:
        taxa = node["participating_taxa"]
        assert len(taxa) == 12
        strains = [t for t in taxa if t["term"]["id"] == "NCBITaxon:1883"]
        assert len(strains) == 2
        assert len({t["preferred_term"] for t in strains}) == 2
    assert "does not establish dominance" in docs[L]["ecological_interactions"][0]["description"]


def test_lupin_expression_and_composition_are_not_functional_flux():
    _, _, docs = records()
    _, expression, assembly = docs[L]["ecological_interactions"]
    assert "FlowPot experiment" in expression["description"]
    assert "not direct hormone production, nitrogen-fixation rate" in expression["description"]
    assert "non-sterile CAS soil" in assembly["description"]
    assert "not absolute exclusion" in assembly["description"]
    assert "conflicts with its reported PERMANOVA p=0.001" in assembly["description"]
    assert docs[L]["discussions"][0]["discussion_id"] == "sc7_richness_vs_membership"
    assert docs[L]["discussions"][0]["status"] == "OPEN"


def test_mamc_procedures_are_not_ecological_nodes():
    _, rows, docs = records()
    assert len(docs[M]["ecological_interactions"]) == 1
    assert {n["node"] for n in rows[M]["removed_node_decisions"]} == {
        "Sugarcane Lignocellulose Enrichment",
        "Functional-Group Reductive MAMC Screening",
    }
    assert rows[M]["edges_before"] == rows[M]["edges_after"] == []


def test_mamc_fraction_mean_is_not_each_fraction_or_gravimetric_loss():
    _, _, docs = records()
    output = docs[M]["ecological_interactions"][0]
    for phrase in [
        "43.01%",
        "39.65%",
        "69.18%",
        "averaging 50.6%",
        "rather than 50.6% for each",
        "not direct gravimetric mass loss",
        "16S identification labels",
        "HYPOTHESIZED",
    ]:
        assert phrase in output["description"]
    assert len(output["participating_taxa"]) == 5
    assert "biological_processes" not in output


def test_batch64_caches_and_canonical_participants_are_not_rewritten():
    ledger, _, docs = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for doc in docs.values():
        canonical = {
            t["taxon_term"]["preferred_term"]: t["taxon_term"]["term"] for t in doc["taxonomy"]
        }
        for node in doc["ecological_interactions"]:
            assert "interaction_type" not in node and "downstream" not in node
            for taxon in node["participating_taxa"]:
                assert canonical[taxon["preferred_term"]] == taxon["term"]
        assert "#1564" in doc["discussions"][-1]["rationale"]
    assert ledger["unresolved_non_graph_issues"] == [1564]
    assert ledger["primary_graph_snippet_count"] == 9


def test_batch64_all_nodes_arrows_histories_and_source_limits_recorded():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1561, 1562, 1563]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 7
    assert sum(len(r["removed_node_decisions"]) for r in rows.values()) == 2
    assert sum(len(r["edges_before"]) for r in rows.values()) == 2
    assert sum(len(r["edges_after"]) for r in rows.values()) == 0
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1 and row["status"] == "reviewed"
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {d["node"] for d in row["node_decisions"]} == names
        assert {a.split("#", 1)[1] for a in doc["discussions"][-1]["attaches_to"]} == names
        assert doc["discussions"][-1]["status"] == "OPEN"
