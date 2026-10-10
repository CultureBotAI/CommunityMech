"""Keep observed outcomes distinct from model, protocol and assay overclaims."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch78.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_nitrifier_positive_redox_outcomes_are_not_resolved_guild_flux():
    _, rows, docs = records()
    (node,) = docs[0]["ecological_interactions"]
    assert rows[0]["status"] == "needs_research"
    assert node["description"].startswith("PARTIAL -")
    assert "only after about day 30" in node["description"]
    assert "anoxic cultures accumulated ammonia" in node["description"]
    assert "do not demonstrate nitrification under anoxia" in node["description"]
    assert [(e["supports"], e["evidence_source"]) for e in node["evidence"]] == [
        ("PARTIAL", "OTHER"),
        ("SUPPORT", "IN_VITRO"),
    ]
    assert {t["term"]["id"] for t in node["participating_taxa"]} == {
        "NCBITaxon:35798",
        "NCBITaxon:911",
    }
    assert "45.96%" in str(docs[0]["taxonomy"])


def test_omm12_resistance_is_not_the_expanded_community_outcome():
    _, _, docs = records()
    resistance = docs[1]["ecological_interactions"][1]
    assert "less than a conventional complex microbiota" in resistance["description"]
    assert "three added facultative anaerobic bacteria" in resistance["description"]
    assert "interaction_type" not in resistance
    assert resistance["evidence"][0]["supports"] == "SUPPORT"
    assert "albeit not to the degree" in resistance["evidence"][0]["snippet"]
    assert docs[1]["taxonomy"][0]["taxon_term"]["term"]["id"] == "NCBITaxon:2"


def test_omm12_repeat_dose_effect_survives_without_context_arrow_or_all12_guarantee():
    _, _, docs = records()
    dose, _, colonization = docs[1]["ecological_interactions"]
    assert len(dose["downstream"]) == 1
    assert dose["downstream"][0]["target"] == colonization["name"]
    assert "improved reproducibility" in dose["downstream"][0]["description"]
    assert "not guaranteed detection of every strain" in dose["downstream"][0]["description"]
    assert "not a fully matched randomized comparison" in dose["description"]
    assert "not viable cell counts" in colonization["description"]
    assert "functional equivalence" in colonization["description"]
    assert "downstream" not in colonization
    assert all("interaction_type" not in n for n in docs[1]["ecological_interactions"])


def test_trophic_arrows_and_measured_chemistry_remain_with_flux_limits():
    _, _, docs = records()
    donor, sulfate, fumarate, _ = docs[2]["ecological_interactions"]
    assert [e["target"] for e in donor["downstream"]] == [sulfate["name"], fumarate["name"]]
    assert "sulfate consumption and fumarate reduction" in donor["description"]
    assert "not independently traced interspecies fluxes" in donor["description"]
    assert sulfate["interaction_type"] == "CROSS_FEEDING"
    assert "not proof of reciprocal obligate syntrophy" in sulfate["description"]
    assert "residual acetate and succinate production" in fumarate["description"]
    assert all(
        e["supports"] == "SUPPORT" for n in [donor, sulfate, fumarate] for e in n["evidence"]
    )
    assert donor["source_taxon"]["term"]["id"] == "NCBITaxon:1521"
    assert sulfate["target_taxon"]["term"]["id"] == "NCBITaxon:882"
    assert fumarate["target_taxon"]["term"]["id"] == "NCBITaxon:35554"


def test_trophic_limitation_grounding_and_fulltext_discussion_are_corrected():
    _, _, docs = records()
    nodes = docs[2]["ecological_interactions"]
    limitation = nodes[-1]
    assert "interaction_type" not in limitation
    assert "selective succinate causation was not isolated" in limitation["description"]
    assert all(
        e["evidence_source"] == "COMPUTATIONAL" and e["supports"] == "PARTIAL"
        for e in limitation["evidence"]
    )
    fumarates = [
        m for n in nodes for m in n.get("metabolites", []) if m["preferred_term"] == "fumarate"
    ]
    assert len(fumarates) == 2
    assert all(m["term"] == {"id": "CHEBI:29806", "label": "fumarate(2-)"} for m in fumarates)
    gap = docs[2]["discussions"][0]
    assert "now inspected" in gap["rationale"]
    assert "OptCom" in gap["rationale"] and "not new measured transfer" in gap["rationale"]
    assert "modeled fourth-member extension is not part" in gap["rationale"]


def test_pd10_preserves_medium_selection_without_niche_or_uniform_timing_claims():
    _, _, docs = records()
    selection, _, _, mops, r2a = docs[3]["ecological_interactions"]
    assert [e["target"] for e in selection["downstream"]] == [mops["name"], r2a["name"]]
    assert "passage 4" in mops["description"]
    assert "passage 10" in r2a["description"]
    assert "15 passages" in r2a["description"]
    assert all("interaction_type" not in n for n in [selection, mops, r2a])
    assert "BC15 proteins" in r2a["description"]
    assert "not a direct viable-cell count" in r2a["description"]


def test_pd10_agar_phenotypes_do_not_prove_liquid_selection_mechanisms():
    _, _, docs = records()
    assay = docs[3]["ecological_interactions"][1]
    assert assay["name"] == "Pairwise Growth Phenotypes on R2A Agar"
    assert "inhibition" in assay["description"] and "growth promotion" in assay["description"]
    assert "agar-versus-liquid conditions are alternative explanations" in assay["description"]
    assert "interaction_type" not in assay and "downstream" not in assay
    assert assay["evidence"][0]["supports"] == "SUPPORT"


def test_pd10_r2a_model_retains_proposed_support_with_correct_partner_and_chemical_scope():
    _, rows, docs = records()
    export = docs[3]["ecological_interactions"][2]
    assert rows[3]["status"] == "needs_research"
    assert export["description"].startswith("HYPOTHESIZED -")
    assert "conditioned on endpoint 16S proportions" in export["description"]
    assert "target_taxon" not in export
    assert {t["preferred_term"] for t in export["participating_taxa"]} == {
        "Pantoea sp. YR343",
        "Pseudomonas sp. GM17",
        "Sphingobium sp. AP49",
    }
    assert export["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert (
        "enzyme detection is not exchange-flux validation" in export["downstream"][0]["description"]
    )
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in export["evidence"])
    assert [m["preferred_term"] for m in export["metabolites"]] == ["organic acid"]
    assert export["metabolites"][0]["term"]["id"] == "CHEBI:64709"
    assert "purine derivatives and biogenic amines" in export["description"]


def test_every_node_and_arrow_has_a_decision_without_unapproved_extension():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 13
    assert sum(len(r["edges_before"]) for r in rows) == 7
    assert sum(len(r["edges_after"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    assert (
        ledger["primary_graph_snippet_count"] == ledger["cache_matched_graph_snippet_count"] == 22
    )
    assert all(c["independent_primary_match"] for c in ledger["snippet_checks"])
    for row, doc in zip(rows, docs, strict=True):
        rename = row["renamed_nodes"]
        before = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        after = {(e["source"], e["target"]) for e in row["edges_after"]}
        removed = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        assert after.isdisjoint(removed) and after | removed == before
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            a.split("#", 1)[1] in names
            for d in doc.get("discussions", [])
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_research_authorization_history_and_issue_lifecycle_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1644, 1645, 1646, 1647]
    assert ledger["unresolved_research_issues"] == [1648, 1649]
    assert ledger["unresolved_non_graph_issues"] == [1650]
    assert not ledger["cache_changes"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert [(d["community_id"], d["query_chars"]) for d in ledger["edison"]["dry_runs"]] == [
        ("CommunityMech:000433", 9473),
        ("CommunityMech:000047", 15034),
    ]
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert row["allowed_changed_fields"] == [
            "curation_history",
            "discussions",
            "ecological_interactions",
        ]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert all((ROOT / p).exists() for p in row["history_files"])
