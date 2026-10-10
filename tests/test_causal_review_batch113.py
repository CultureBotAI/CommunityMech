"""Preserve marine assay boundaries and distinguish correlation from causation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-three-records-batch113.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_hp15_positive_and_null_aggregation_results_remain_distinct():
    _, _, docs = records()
    aggregation = docs[0]["ecological_interactions"][0]
    assert aggregation["scope"] == "COMMUNITY_LEVEL"
    assert "interaction_type" not in aggregation
    assert "not a universal bacterial requirement" in aggregation["description"]
    assert "much less, not uniformly zero" in aggregation["description"]
    assert aggregation["evidence"][-1]["reference"] == "PMID:25375640"
    assert "independent of the presence" in aggregation["evidence"][-1]["snippet"]


def test_tep_is_not_directed_feeding_or_a_universal_aggregation_driver():
    _, _, docs = records()
    aggregation, tep, _, _ = docs[0]["ecological_interactions"]
    assert tep["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in tep
    assert "warmer treatments generated more TEP but less aggregation" in tep["description"]
    assert tep["evidence"][2]["supports"] == "PARTIAL"
    assert "not the identity of all TEP" in tep["description"]
    assert tep["downstream"][0]["target"] == aggregation["name"]
    assert tep["downstream"][0]["description"].startswith("PARTIAL:")


def test_attachment_perturbation_does_not_demonstrate_aggregation_mediation():
    _, _, docs = records()
    attachment = docs[0]["ecological_interactions"][2]
    assert "interaction_type" not in attachment
    assert (
        "fraction of bacteria attaching to the diatom decreased"
        in attachment["evidence"][1]["snippet"]
    )
    assert "abiotic surfaces" in attachment["description"]
    assert attachment["downstream"][0]["description"].startswith("HYPOTHESIZED:")
    assert "not selective mediation" in attachment["downstream"][0]["description"]


def test_export_interpretation_is_not_niche_partitioning_or_measured_field_flux():
    _, _, docs = records()
    export = docs[0]["ecological_interactions"][3]
    assert "interaction_type" not in export and "downstream" not in export
    assert "not a measured field flux" in export["description"]
    assert all(e["supports"] == "PARTIAL" for e in export["evidence"])


def test_ruegeria_recognition_and_chitin_response_are_not_exchange_or_mediation():
    _, _, docs = records()
    recognition, feeding, response = docs[1]["ecological_interactions"]
    assert all("downstream" not in n for n in [recognition, feeding, response])
    assert "interaction_type" not in recognition and "interaction_type" not in response
    assert feeding["interaction_type"] == "CROSS_FEEDING"
    assert "not selectively demonstrated" in recognition["description"]
    assert "B12-replete axenic controls" in response["description"]
    assert "does not negate the earlier B12-limited benefit" in response["description"]


def test_metabolite_evidence_grades_are_specific_to_the_ruegeria_column():
    _, _, docs = records()
    feeding = docs[1]["ecological_interactions"][1]
    assert feeding["evidence"][0]["supports"] == "PARTIAL"
    assert "three separate bacterial pair cultures" in feeding["description"]
    assert [m["notes"].split(" (")[0] for m in feeding["metabolites"]] == [
        "Gene-expression inference",
        "Gene-expression inference",
        "Net metabolite drawdown",
        "Net metabolite drawdown",
    ]
    assert all(
        "not an individually traced transfer flux" in m["notes"] for m in feeding["metabolites"]
    )


def test_trichodesmium_helpers_remain_hypotheses_with_host_to_epibiont_b12():
    _, _, docs = records()
    colony, helper, diel = docs[2]["ecological_interactions"]
    assert all(
        "interaction_type" not in n and "downstream" not in n for n in [colony, helper, diel]
    )
    assert helper["description"].startswith("HYPOTHESIZED:")
    assert "facultative B12 use" in helper["description"]
    assert "Proposed Trichodesmium-to-Alteromonas provision" in helper["metabolites"][2]["notes"]
    assert all(e["supports"] == "PARTIAL" for e in helper["evidence"])
    assert helper["metabolites"][3]["term"]["id"] == "CHEBI:26523"
    assert helper["biological_processes"][0]["term"]["id"] == "GO:0098869"


def test_field_expression_does_not_credit_the_exact_laboratory_strain():
    _, _, docs = records()
    diel = docs[2]["ecological_interactions"][2]
    assert "source_taxon" not in diel and "target_taxon" not in diel
    assert [p["preferred_term"] for p in diel["participating_taxa"]] == [
        "Trichodesmium-associated heterotrophic microbiome"
    ]
    assert "not demonstrated to be IMS101" in diel["description"]
    assert "not directly demonstrated cross-feeding" in diel["description"]


def test_dispositions_and_unfinished_extension_are_honest():
    ledger, rows, _ = records()
    counts = ledger["reviewed_counts"]
    assert counts["original_nodes"] == counts["retained_nodes"] == 10
    assert counts["original_arrows"] == 6 and counts["retained_arrows"] == 2
    assert counts["removed_arrows"] == 4 and counts["renamed_nodes"] == 6
    assert counts["graph_quotations"] == 21 and counts["discussion_quotations"] == 3
    assert len(ledger["issues"]) == 3 and ledger["unresolved_research_issues"] == [1883]
    assert [r["status"] for r in rows] == ["reviewed", "needs_research", "reviewed"]
    assert ledger["edison"]["authorized_invocations"] == 1
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["task_id"] is None
    assert sum(not p["independent_primary_match"] for p in ledger["snippet_checks"]) == 1


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
            assert all(
                p in canonical and set(p) == {"preferred_term", "term"}
                for p in node.get("participating_taxa", [])
            )
        for d in doc["discussions"]:
            assert all(a.split("#", 1)[1] in names for a in d["attaches_to"])
