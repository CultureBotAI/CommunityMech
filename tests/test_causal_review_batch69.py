"""Preserve positive observations without workflow or unisolated mediation claims."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-four-records-batch69.yaml"
A = "Medicago_Nodule_Biofertilizer_SynCom"
B = "Mediterranean_AM_Fungal_SixSpecies_SynCom"
C = "Mediterranean_Grassland_qSIP_Rainfall_Community"
D = "Meghalaya_Bacillus_Consortia_A22ED9"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {stem: yaml.safe_load((ROOT / row["path"]).read_text()) for stem, row in rows.items()}
    return ledger, rows, docs


def test_medicago_preserves_strain_traits_with_real_exceptions():
    _, _, docs = records()
    doc = docs[A]
    node = doc["ecological_interactions"][0]
    assert len(node["participating_taxa"]) == 4
    assert len({t["preferred_term"] for t in node["participating_taxa"]}) == 4
    assert len({t["term"]["id"] for t in node["participating_taxa"]}) == 2
    for phrase in ["individually", "N10/N12", "nitrogen-free", "biofilm signal decreased"]:
        assert phrase in node["description"]
    assert "biological_processes" not in node
    assert doc["engineering_design"]["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert (
        doc["environmental_factors"][0]["evidence"][0] == doc["engineering_design"]["evidence"][0]
    )


def test_medicago_retains_host_benefits_without_fixation_or_mediation_proof():
    _, _, docs = records()
    trait, antioxidant, plant = docs[A]["ecological_interactions"]
    assert trait["downstream"][0]["target"] == antioxidant["name"]
    assert antioxidant["downstream"][0]["target"] == plant["name"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED -") for n in [trait, antioxidant]
    )
    assert "external host" in antioxidant["description"]
    assert "shorter but thicker roots" in plant["description"]
    assert {p["term"]["id"] for p in plant["biological_processes"]} == {"GO:0009877"}
    assert {p["term"]["id"] for p in antioxidant["biological_processes"]} == {"GO:0006979"}
    assert plant["evidence"][0]["evidence_source"] == "IN_VIVO"
    assert "enhanced plant growth" in plant["evidence"][0]["snippet"]


def test_fungal_compartments_and_external_evidence_aliases_are_preserved():
    _, rows, docs = records()
    doc = docs[B]
    (node,) = doc["ecological_interactions"]
    assert len(node["participating_taxa"]) == 6
    assert node["biological_processes"][0]["term"]["id"] == "GO:0044403"
    for phrase in [
        "initially six-species",
        "qualitative occurrence",
        "extinction",
        "limited plant-cover",
    ]:
        assert phrase in node["description"]
    raw = (ROOT / rows[B]["path"]).read_text()
    for label in ["id004", "id005"]:
        assert "&" + label in raw and "*" + label in raw
    assert doc["environmental_factors"][1]["evidence"] == node["evidence"][:2]
    assert all(ev["evidence_source"] == "IN_VIVO" for ev in node["evidence"])
    assert all(d["status"] == "OPEN" for d in doc["discussions"][:2])


def test_qsip_keeps_growth_but_not_redundant_workflow_or_selection_proof():
    _, rows, docs = records()
    growth, rainfall, motility, carbon = docs[C]["ecological_interactions"]
    assert len(rows[C]["removed_node_decisions"]) == 1
    assert (
        rows[C]["removed_node_decisions"][0]["node"] == "qSIP-Informed Active Community Resolution"
    )
    assert len(growth["evidence"]) == 3
    assert "eight-day laboratory" in growth["description"]
    assert "overlapping aggregate guild" in growth["description"]
    assert "site-history confounding" in rainfall["description"]
    assert "predicted from genes" in motility["description"]
    assert "not substrate-specific flux" in carbon["description"]
    assert all("downstream" not in n for n in docs[C]["ecological_interactions"])
    assert all("biological_processes" not in n for n in [growth, rainfall, carbon])
    assert motility["biological_processes"][0]["term"]["id"] == "GO:0071973"


def test_bacillus_preserves_single_metal_depletion_and_control_limits():
    _, _, docs = records()
    (node,) = docs[D]["ecological_interactions"]
    assert "single-metal" in node["name"]
    assert "single-metal" in docs[D]["growth_media"][0]["name"]
    for phrase in ["92.08%", "74.15%", "97.587%", "ICP-OES", "Final pH varied", "Cell-free medium"]:
        assert phrase in node["description"]
    assert len(node["participating_taxa"]) == 2
    assert {t["preferred_term"] for t in node["participating_taxa"]} == {
        "Bacillus sp. SK22",
        "Bacillus sp. KHED9",
    }
    assert "potassium dichromate" in node["metabolites"][1]["notes"]
    assert "not chromium metal" in node["metabolites"][1]["notes"]
    assert "cell-free controls" in docs[D]["discussions"][-1]["rationale"]


def test_batch69_research_gaps_are_not_counted_as_completed():
    ledger, rows, docs = records()
    assert ledger["unresolved_research_issues"] == [1592, 1593]
    assert ledger["unresolved_non_graph_issues"] == [1594]
    assert [rows[x]["status"] for x in [A, B, C, D]] == [
        "reviewed",
        "reviewed",
        "needs_research",
        "needs_research",
    ]
    for stem, issue in [(C, 1592), (D, 1593)]:
        assert f"#{issue}" in docs[stem]["discussions"][-1]["rationale"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert [r["query_chars"] for r in ledger["edison"]["dry_runs"]] == [9469, 9544]
    assert ledger["edison"]["required_for_deferred_extensions"] is True


def test_batch69_caches_and_history_are_bound_to_reviewed_content():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["primary_graph_snippet_count"] == 19
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for stem, row in rows.items():
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1
        assert docs[stem]["curation_history"][-1]["llm_assisted"] is True
        assert all("interaction_type" not in n for n in docs[stem]["ecological_interactions"])


def test_batch69_accounts_for_every_original_node_and_arrow():
    _, rows, docs = records()
    assert (
        sum(len(r["node_decisions"]) + len(r["removed_node_decisions"]) for r in rows.values())
        == 10
    )
    assert sum(len(r["retained_edge_decisions"]) for r in rows.values()) == 2
    assert sum(len(r["removed_edge_decisions"]) for r in rows.values()) == 0
    for stem, row in rows.items():
        names = {n["name"] for n in docs[stem]["ecological_interactions"]}
        assert {n["node"] for n in row["node_decisions"]} == names
        renames = row["renamed_nodes"]
        original_edges = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        assert {(e["source"], e["target"]) for e in row["edges_after"]} == original_edges
        for discussion in docs[stem]["discussions"]:
            assert {
                a.split("#", 1)[1]
                for a in discussion["attaches_to"]
                if a.startswith("ecological_interactions#")
            } <= names
