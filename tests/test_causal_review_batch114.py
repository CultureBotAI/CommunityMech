"""Keep thermophilic syntrophy distinct from proposed mechanisms and assay contrasts."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-two-records-batch114.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_acetate_syntrophy_does_not_assert_all_substrate_obligacy():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][0]
    assert node["interaction_type"] == "SYNTROPHY"
    assert "grows acetogenically in pure culture" in node["description"]
    assert "not a claim that intracellular cofactors" in node["description"]
    assert (
        "not direct acetate utilization by the methanogen" in node["downstream"][0]["description"]
    )
    assert node["evidence"][2]["supports"] == "PARTIAL"


def test_tm_expression_is_not_all_genes_or_the_deltah_system():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][1]
    assert "20 to 80 Pa" in node["description"]
    assert "mcr/MRI rather than mrt/MRII" in node["description"]
    assert "other assayed methanogenesis genes" in node["description"]
    assert "separate DeltaH/butyrate" in node["description"]
    assert "does not exclude formate-supported electron transfer" in node["description"]


def test_formate_support_survives_without_proving_the_energy_coupling_model():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][2]
    assert node["name"] == "Formate-Linked Syntrophic Electron Transfer"
    assert node["interaction_type"] == "CROSS_FEEDING"
    assert node["description"].startswith("PARTIAL:")
    assert "not dismissed as a genomic conjecture" in node["description"]
    assert "HYPOTHESIZED:" in node["description"]
    assert (
        "Proton-gradient coupling and physiological acetate reduction were not demonstrated"
        in node["description"]
    )
    assert node["evidence"][0]["supports"] == "PARTIAL"
    assert node["evidence"][1]["supports"] == "SUPPORT"
    assert node["downstream"][0]["description"].startswith("PARTIAL:")


def test_hydrogen_transfer_retains_separate_study_effect_sizes():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][0]
    assert node["interaction_type"] == "SYNTROPHY"
    assert "tenfold bacterial density increase at 85 C" in node["description"]
    assert "separate 2006 study" in node["description"]
    assert "three- to fivefold" in node["description"]
    assert "also grew in monoculture" in node["description"]


def test_proximity_is_not_colonization_or_obligatory_direct_contact():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][1]
    assert node["scope"] == "COMMUNITY_LEVEL"
    assert "interaction_type" not in node
    assert "source_taxon" not in node and "target_taxon" not in node
    assert "do not demonstrate direct cell contact as obligatory" in node["description"]
    assert node["evidence"][1]["supports"] == "PARTIAL"
    assert node["downstream"][0]["description"].startswith("PARTIAL:")


def test_292_is_a_within_culture_growth_phase_contrast():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][2]
    assert node["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in node
    assert "within coculture, versus 24" in node["description"]
    assert "not 292 genes in a direct coculture-versus-monoculture contrast" in node["description"]
    assert "diminished during stationary phase" in node["description"]
    assert "not demonstrated regulatory necessity" in node["description"]


def test_hydrogen_to_phenotype_mediation_is_partial():
    _, _, docs = records()
    edge = docs[1]["ecological_interactions"][0]["downstream"][0]
    assert edge["description"].startswith("PARTIAL:")
    assert (
        "do not selectively demonstrate mediation of every EPS or transcript response"
        in edge["description"]
    )
    assert "culture/gas-handling conditions" in edge["description"]


def test_original_topology_and_evidence_dispositions_are_accounted_for():
    ledger, rows, _ = records()
    counts = ledger["reviewed_counts"]
    assert counts["original_nodes"] == counts["retained_nodes"] == 6
    assert counts["original_arrows"] == counts["retained_arrows"] == 4
    assert counts["removed_arrows"] == counts["removed_nodes"] == 0
    assert counts["renamed_nodes"] == 1
    assert counts["graph_quotations"] == 16 and counts["discussion_quotations"] == 2
    assert [r["status"] for r in rows] == ["reviewed", "reviewed"]
    assert ledger["issues"] == [1888, 1889]
    assert ledger["unresolved_non_graph_issues"] == [1890, 1891]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert all(p["independent_primary_match"] for p in ledger["snippet_checks"])


def test_hashes_history_and_canonical_participants_are_guarded():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).exists()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        names = {n["name"] for n in doc["ecological_interactions"]}
        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        for node in doc["ecological_interactions"]:
            assert all(e["target"] in names for e in node.get("downstream", []))
            if node["scope"] == "COMMUNITY_LEVEL":
                assert node["participating_taxa"] == canonical
        for d in doc["discussions"]:
            assert all(a.split("#", 1)[1] in names for a in d["attaches_to"])
