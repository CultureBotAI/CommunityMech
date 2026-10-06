"""Separate genomic potential, modeled transfer and measured host endpoints."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-lakes-mars-batch62.yaml"
P = "Lac_Pavin_Stratified_Lake_Community"
W = "Lake_Washington_Methane_Oxygen_Methylotroph_Community"
M = "Legume_Rhizobia_Mars_Simulant_Symbiosis"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / r["path"]).read_text()) for name, r in rows.items()}
    return ledger, rows, docs


def test_pavin_depth_potential_is_not_flux_or_common_driver_causality():
    _, rows, docs = records()
    carbon, methane, rubisco = docs[P]["ecological_interactions"]
    assert "genetic potential, not measured carbon-fixation flux" in carbon["description"]
    assert "not strictly exclusive compartments" in methane["description"]
    assert "nondetection is not proof of absence" in methane["description"]
    assert "free-nucleotide pathway" in rubisco["description"]
    assert "weak depth differentiation" in rubisco["description"]
    assert len(rows[P]["removed_edge_decisions"]) == 2
    for node in [carbon, methane, rubisco]:
        assert "downstream" not in node and "interaction_type" not in node
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
        assert all(e["supports"] == "PARTIAL" for e in node["evidence"])


def test_pavin_participants_remain_partial_canonical_components():
    _, _, docs = records()
    carbon, methane, rubisco = docs[P]["ecological_interactions"]
    assert [t["term"]["id"] for t in carbon["participating_taxa"]] == ["NCBITaxon:2157"]
    assert methane["participating_taxa"] == carbon["participating_taxa"]
    assert [t["term"]["id"] for t in rubisco["participating_taxa"]] == [
        "NCBITaxon:1783273",
        "NCBITaxon:1783276",
    ]
    assert "absent from the record roster" in carbon["description"]
    assert "missing bacterial methane oxidizers" in methane["description"]


def test_washington_guild_coupling_does_not_identify_methanol():
    _, _, docs = records()
    guild = docs[W]["ecological_interactions"][0]
    assert guild["interaction_type"] == "CROSS_FEEDING"
    assert [m["term"]["id"] for m in guild["metabolites"]] == ["CHEBI:16183"]
    assert "not established as the directly transferred" in guild["metabolites"][0]["notes"]
    assert "prior stable-isotope studies" in guild["description"]
    assert "does not identify the transferred compound" in guild["description"]
    assert all(e["supports"] == "PARTIAL" for e in guild["evidence"])


def test_washington_oxygen_selection_survives_without_cross_study_bridge():
    _, rows, docs = records()
    guild, oxygen, model = docs[W]["ecological_interactions"]
    assert len(oxygen["downstream"]) == 1
    assert oxygen["downstream"][0]["target"] == guild["name"]
    assert oxygen["downstream"][0]["description"].startswith("PARTIAL -")
    assert "not constant dissolved-oxygen" in oxygen["description"]
    assert "intermediate mixtures and replicate exceptions" in oxygen["description"]
    assert all(t["term"]["id"] != "NCBITaxon:105972" for t in oxygen["participating_taxa"])
    assert "downstream" not in model
    assert len(rows[W]["retained_edge_decisions"]) == 1
    assert len(rows[W]["removed_edge_decisions"]) == 1


def test_washington_conditional_model_transfer_has_correct_direction_and_limits():
    ledger, _, docs = records()
    model = docs[W]["ecological_interactions"][2]
    assert model["source_taxon"]["term"]["id"] == "NCBITaxon:416"
    assert model["target_taxon"]["term"]["id"] == "NCBITaxon:429"
    assert "interaction_type" not in model
    assert "synthetic 0.05:1 scenario but not the sediment 9.3:1" in model["description"]
    assert "constraints, not predicted abundances" in model["description"]
    assert "no transfer was experimentally validated here" in model["description"]
    assert "#1554" in model["description"]
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in model["evidence"])
    assert all(e["supports"] == "PARTIAL" for e in model["evidence"])
    assert "not partner-directed exchange" in model["metabolites"][1]["notes"]
    assert ledger["unresolved_research_issues"] == [1554]


def test_mars_living_host_reporter_is_not_nitrogen_fixation_flux():
    _, rows, docs = records()
    nodules, reporter, phenotype = docs[M]["ecological_interactions"]
    assert "alternative inoculants, not a coculture" in nodules["description"]
    assert "MMS-1 Unsorted" in nodules["description"] and "MMS-1 Fine" in nodules["description"]
    assert [t["term"]["id"] for t in reporter["participating_taxa"]] == ["NCBITaxon:382"]
    assert "metabolites" not in reporter
    assert "not direct N2-fixation flux" in reporter["description"]
    for node in [nodules, reporter, phenotype]:
        assert "interaction_type" not in node and "downstream" not in node
        assert all(e["evidence_source"] == "IN_VIVO" for e in node["evidence"])
    assert len(rows[M]["removed_edge_decisions"]) == 2


def test_mars_plant_endpoints_do_not_assert_chemical_or_reporter_mediation():
    _, _, docs = records()
    phenotype = docs[M]["ecological_interactions"][2]
    assert "Lateral-root numbers were reduced on every simulant" in phenotype["description"]
    assert "HYPOTHESIZED" in phenotype["description"]
    assert "individual chemical mediation was not selectively tested" in phenotype["description"]
    assert "Martian atmosphere or perchlorate exposure" in phenotype["description"]
    assert phenotype["biological_processes"][0]["term"]["id"] == "GO:0044419"


def test_batch62_caches_and_canonical_participants_are_not_silently_rewritten():
    ledger, _, docs = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for doc in docs.values():
        canonical = {
            t["taxon_term"]["preferred_term"]: t["taxon_term"]["term"] for t in doc["taxonomy"]
        }
        for node in doc["ecological_interactions"]:
            taxa = node.get("participating_taxa", []) + [
                node[k] for k in ["source_taxon", "target_taxon"] if k in node
            ]
            for taxon in taxa:
                assert canonical[taxon["preferred_term"]] == taxon["term"]
        assert "#1553" in doc["discussions"][-1]["rationale"]
    assert ledger["unresolved_non_graph_issues"] == [1553]
    assert ledger["edison"]["provider_submissions"] == 0
    assert ledger["primary_graph_snippet_count"] == 16


def test_batch62_all_nodes_arrows_anchors_and_histories_are_recorded():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1550, 1551, 1552]
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 9
    assert sum(len(r["edges_before"]) for r in rows.values()) == 6
    assert sum(len(r["edges_after"]) for r in rows.values()) == 1
    assert sum(len(r["removed_edge_decisions"]) for r in rows.values()) == 5
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1 and row["status"] == "reviewed"
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {d["node"] for d in row["node_decisions"]} == names
        assert {a.split("#", 1)[1] for a in doc["discussions"][-1]["attaches_to"]} == names
        assert doc["discussions"][-1]["status"] == "OPEN"
