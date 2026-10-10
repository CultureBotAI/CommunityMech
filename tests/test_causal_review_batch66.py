"""Preserve observations without promoting association or feasible flux to proof."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-wetland-crossfeeding-batch66.yaml"
A = "MUCC_Freshwater_Wetland_Methane_Network_Community"
B = "MWF001_FourSpecies_CrossFeeding_Consortium"
C = "Magnetite_Sulfate_Stress_Anaerobic_Microbiome"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / r["path"]).read_text()) for name, r in rows.items()}
    return ledger, rows, docs


def test_mucc_occupancy_and_network_are_not_demonstrated_interactions():
    _, rows, docs = records()
    core, network, _, _ = docs[A]["ecological_interactions"]
    for phrase in ["five high-emitting", "at least one sample", "contextual placeholders"]:
        assert phrase in core["description"]
    for phrase in ["12 late-season samples", "JLA is a swamp", "genus level", "environmental"]:
        assert phrase in network["description"]
    assert rows[A]["edges_before"] == rows[A]["edges_after"] == []
    assert all("interaction_type" not in n for n in docs[A]["ecological_interactions"])


def test_mucc_predictor_and_genomic_potential_do_not_prove_flux_or_methanol_use():
    _, _, docs = records()
    predictor, potential = docs[A]["ecological_interactions"][2:]
    for phrase in ["within methanogens", "2018", "2015", "not methane-production flux"]:
        assert phrase in predictor["description"]
    for phrase in ["107", "methylated sulfides", "methoxylated", "not confirmed substrate use"]:
        assert phrase in potential["description"]
    assert {m["term"]["id"] for m in potential["metabolites"]} == {"CHEBI:16183"}
    assert all("biological_processes" not in n for n in docs[A]["ecological_interactions"])


def test_mwf_crossfeeding_has_residual_resource_and_generic_model_limits():
    _, _, docs = records()
    node = docs[B]["ecological_interactions"][0]
    assert node["interaction_type"] == "CROSS_FEEDING"
    assert node["description"].startswith("PARTIAL -")
    for phrase in ["not chemically resolved", "applies to simulations", "Generic", "not universal"]:
        assert phrase in node["description"]
    assert node["evidence"][0]["supports"] == "PARTIAL"
    assert node["evidence"][1]["evidence_source"] == "COMPUTATIONAL"


def test_mwf_finite_coexistence_keeps_exceptions_and_extension_unfinished():
    ledger, rows, docs = records()
    node = docs[B]["ecological_interactions"][1]
    for phrase in ["eight 72-hour", "5X-malate", "without carbon", "1/10", "four-day"]:
        assert phrase in node["description"]
    assert "interaction_type" not in node
    assert rows[B]["status"] == "needs_research"
    assert ledger["unresolved_research_issues"] == [1575]
    assert ledger["edison"]["required_for_pending_extension"] is True
    assert docs[B]["discussions"][0]["discussion_id"] == "mwf001_exact_byproduct_resolution"
    assert "#1575" in docs[B]["discussions"][-1]["rationale"]


def test_magnetite_response_is_partial_and_does_not_prove_diet():
    _, _, docs = records()
    node = docs[C]["ecological_interactions"][0]
    for phrase in [
        "19% relative",
        "not full",
        "1.2 g/L",
        "Separate abiotic",
        "no abiotic hydrogen",
    ]:
        assert phrase in node["description"]
    assert "interaction_type" not in node
    assert docs[C]["discussions"][0]["discussion_id"] == "kg-magnetite-sulfate-diet-validation"


def test_magnetite_retains_model_exchange_with_role_and_replication_limits():
    _, _, docs = records()
    acetate, exchange = docs[C]["ecological_interactions"][1:]
    for node in [acetate, exchange]:
        assert node["interaction_type"] == "CROSS_FEEDING"
        assert node["description"].startswith("HYPOTHESIZED -")
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
        assert len(node["participating_taxa"]) == 4
    for phrase in ["DTU8", "DTU25", "DTU38", "DTU36", "gap-filled", "0.7", "One biological"]:
        assert phrase in acetate["description"]
    assert "0.1 mmol/gDW/hour" in exchange["description"]
    assert "Multiple solutions" in exchange["description"]


def test_batch66_caches_canonical_participants_and_existing_gaps_preserved():
    ledger, _, docs = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for doc in docs.values():
        canonical = {
            t["taxon_term"]["preferred_term"]: t["taxon_term"]["term"] for t in doc["taxonomy"]
        }
        for node in doc["ecological_interactions"]:
            for taxon in node["participating_taxa"]:
                assert canonical[taxon["preferred_term"]] == taxon["term"]
        assert "#1574" in doc["discussions"][-1]["rationale"]
    assert ledger["unresolved_non_graph_issues"] == [1574]
    assert ledger["primary_graph_snippet_count"] == 16


def test_batch66_whole_node_ledger_history_and_no_false_completion():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1571, 1572, 1573]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 9
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1
        assert row["status"] == ("needs_research" if name == B else "reviewed")
        assert row["edges_before"] == row["edges_after"] == []
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {d["node"] for d in row["node_decisions"]} == names
        assert {a.split("#", 1)[1] for a in doc["discussions"][-1]["attaches_to"]} == names
