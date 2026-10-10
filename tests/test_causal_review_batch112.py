"""Keep syntrophic feedback while bounding assay scope and inferred mediation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-seven-records-batch112.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_propionate_feedback_is_retained_without_carrier_or_enzyme_certainty():
    _, _, docs = records()
    for doc in docs[:2]:
        a, b, c = doc["ecological_interactions"]
        assert a["interaction_type"] == b["interaction_type"] == "SYNTROPHY"
        assert a["evidence"][1]["supports"] == a["evidence"][2]["supports"] == "PARTIAL"
        assert "formate concentration" in b["description"]
        assert "not independently quantify" in b["description"]
        assert b["downstream"][0]["target"] == a["name"]
        assert b["downstream"][0]["description"].startswith("DIRECTLY IMPLIED feedback:")
        assert "not bidirectional donation" in b["downstream"][1]["description"]
        assert c["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in c


def test_exact_partner_and_existing_formate_gap_are_preserved():
    _, _, docs = records()
    doc = docs[0]
    a = doc["ecological_interactions"][0]
    assert "Methanobacterium formicicum" in a["evidence"][0]["snippet"]
    assert a["evidence"][0]["reference"] == "PMID:29611893"
    assert len(doc["discussions"]) == 1
    d = doc["discussions"][0]
    assert d["discussion_id"] == "kg-syntrophobacter-methanobacterium-partner-attribution"
    assert "30 mM recovers" in d["rationale"]
    assert "fresh publisher retrieval was unavailable" in d["rationale"]


def test_ratio_convergence_is_not_reverse_metabolic_causality():
    _, _, docs = records()
    a, b, c = docs[2]["ecological_interactions"]
    assert a["interaction_type"] == "SYNTROPHY"
    assert a["downstream"][0]["description"].startswith("DIRECTLY IMPLIED/PARTIAL:")
    assert "downstream" not in b
    assert b["scope"] == c["scope"] == "COMMUNITY_LEVEL"
    assert "interaction_type" not in b and "interaction_type" not in c
    assert "around 1 from day 15" in b["evidence"][0]["snippet"]
    assert "without a detectable change in aggregation" in c["description"]


def test_butyrate_feedback_is_not_an_unverified_pressure_threshold():
    _, _, docs = records()
    a, b, c = docs[3]["ecological_interactions"]
    assert a["interaction_type"] == b["interaction_type"] == "SYNTROPHY"
    assert "substrate- and assay-bounded" in a["description"]
    assert "10^-4" not in b["description"]
    assert b["evidence"][1]["snippet"].endswith("by S. wolfei.")
    assert "does not specify" in b["downstream"][0]["description"]
    assert "interaction_type" not in c
    assert len(b["evidence"]) == 2


def test_benzoate_conversion_preserves_partner_free_alternative():
    _, _, docs = records()
    a, b, c = docs[4]["ecological_interactions"]
    assert c["name"] == "Community Benzoate Conversion to Acetate and Methane"
    assert "not complete mineralization" in c["description"]
    assert "pure cultures ferment benzoate" in b["description"]
    assert "absence of hydrogen-utilizing partners" in b["evidence"][1]["snippet"]
    assert a["downstream"][0]["target"] == b["downstream"][0]["target"] == c["name"]
    assert "interaction_type" not in c


def test_gentianae_energy_is_intrinsic_and_product_inhibition_not_competition():
    _, _, docs = records()
    a, b, c = docs[5]["ecological_interactions"]
    assert a["interaction_type"] == "SYNTROPHY"
    assert b["scope"] == "PAIRWISE" and b["source_taxon"]["term"]["id"] == "NCBITaxon:43775"
    assert "target_taxon" not in b and "interaction_type" not in b
    assert c["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in c
    assert "not a second partner-directed" in b["description"]
    assert "propionate is not identified as a benzoate product" in c["description"]
    assert (
        "not assert that product addition changes a fixed intrinsic threshold"
        in c["downstream"][0]["description"]
    )


def test_es5_lag_is_distinguished_from_rates_and_final_concentration():
    _, _, docs = records()
    a, _, _ = docs[6]["ecological_interactions"]
    assert "marks the methane lag difference significant, not" in a["description"]
    assert "not an exact-triculture increase estimate" in a["description"]
    assert "rates were similar" in a["evidence"][1]["snippet"]
    assert (
        "former abstract-wide 120%/150% increase attribution"
        in docs[6]["discussions"][0]["rationale"]
    )


def test_es5_proteomics_and_aggregation_are_hypotheses_not_enzyme_activation():
    _, _, docs = records()
    for n in docs[6]["ecological_interactions"]:
        assert n["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in n
        assert len(n["participating_taxa"]) == 3
    _, b, c = docs[6]["ecological_interactions"]
    for n in [b, c]:
        assert n["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert c["evidence"][1]["supports"] == "PARTIAL"
    assert "more abundant in the biculture" in c["description"]
    assert "assayed proteomes belong to S. wolfei and M. hungatei" in c["description"]


def test_graph_metabolite_roles_and_benzoate_grounding_are_structured():
    _, _, docs = records()
    benzoates = []
    for doc in docs:
        for node in doc["ecological_interactions"]:
            for m in node.get("metabolites", []):
                assert "concentration" not in m
                if m["preferred_term"] == "benzoate":
                    benzoates.append(m)
                    assert m["term"] == {"id": "CHEBI:16150", "label": "benzoate"}
    assert len(benzoates) == 4


def test_complete_dispositions_and_source_access_limits_are_recorded():
    ledger, rows, _ = records()
    assert ledger["reviewed_counts"] == {
        "original_nodes": 21,
        "retained_nodes": 21,
        "removed_nodes": 0,
        "retained_arrows": 16,
        "removed_arrows": 1,
        "renamed_nodes": 1,
        "graph_quotations": 45,
        "discussion_quotations": 8,
        "new_discussions": 3,
        "updated_discussions": 3,
    }
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    assert len(ledger["issues"]) == 6 and len(ledger["unresolved_non_graph_issues"]) == 2
    assert ledger["primary_graph_snippet_count"] == 43
    assert sum(not c["independent_primary_match"] for c in ledger["snippet_checks"]) == 2
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    for row in rows:
        for edge in row["retained_edge_decisions"]:
            for k in ["source", "target"]:
                assert (
                    row["renamed_nodes"].get(edge["before"][k], edge["before"][k])
                    == edge["after"][k]
                )


def test_histories_hashes_and_canonical_participants_are_guarded():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["status"] == "reviewed"
        expected_events = 2 if row["id"] == "CommunityMech:000071" else 1
        assert row["curation_events_added"] == len(row["history_files"]) == expected_events
        assert (ROOT / row["history_files"][0]).exists()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        names = {n["name"] for n in doc["ecological_interactions"]}
        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        for n in doc["ecological_interactions"]:
            assert all(e["target"] in names for e in n.get("downstream", []))
            assert all(
                p in canonical and set(p) == {"preferred_term", "term"}
                for p in n.get("participating_taxa", [])
            )
        for d in doc.get("discussions", []):
            assert all(
                a.split("#", 1)[1] in names
                for a in d["attaches_to"]
                if a.startswith("ecological_interactions#")
            )
