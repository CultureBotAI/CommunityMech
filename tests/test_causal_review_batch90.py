"""Keep reported causal findings distinct from reversed transfers and scope drift."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch90.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_chloronitro_downstream_step_does_not_imply_reverse_feeding():
    _, rows, docs = records()
    upstream, downstream, endpoint = docs[0]["ecological_interactions"]
    assert len(rows[0]["edges_after"]) == 2
    assert upstream["interaction_type"] == "CROSS_FEEDING"
    assert downstream["scope"] == "COMMUNITY_LEVEL"
    assert "source_taxon" not in downstream and "target_taxon" not in downstream
    assert "interaction_type" not in downstream and "interaction_type" not in endpoint
    assert "not evidence of Rhodococcus supplying a metabolite back" in downstream["description"]


def test_chloronitro_conditional_mineralization_is_preserved():
    _, _, docs = records()
    endpoint = docs[0]["ecological_interactions"][-1]
    assert "reports coculture mineralization" in endpoint["description"]
    assert "additional carbon source" in endpoint["description"]
    assert len(endpoint["evidence"]) == 2
    assert "not evidence that controls were absent" in docs[0]["discussions"][-1]["rationale"]


def test_tpa_competition_has_metabolic_evidence_not_only_dominance():
    _, _, docs = records()
    exploit, interference, dominance = docs[1]["ecological_interactions"]
    assert all(n["interaction_type"] == "COMPETITION" for n in [exploit, interference, dominance])
    assert len(exploit["evidence"]) == 2
    assert "TPA metabolism was abolished" in exploit["evidence"][1]["snippet"]
    assert "not by itself the mechanism" in exploit["evidence"][0]["explanation"]
    assert "measured population outcome" in dominance["description"]


def test_tpa_positive_contact_inhibition_attribution_survives():
    _, rows, docs = records()
    node = docs[1]["ecological_interactions"][1]
    assert len(rows[1]["edges_after"]) == 2
    assert "authors report assays" in node["description"]
    assert "main contributor to dominance" in node["downstream"][0]["description"]
    assert "relative growth kinetics" in node["description"]
    assert "does not imply absent controls" in docs[1]["discussions"][-1]["rationale"]


def test_naphthalene_model_and_positive_endpoints_are_separate():
    _, _, docs = records()
    transfer, circuit, endpoint = docs[2]["ecological_interactions"]
    assert transfer["interaction_type"] == circuit["interaction_type"] == "SYNTROPHY"
    assert "interaction_type" not in endpoint
    assert transfer["description"].startswith("PARTIAL:")
    assert circuit["description"].startswith("PARTIAL:")
    assert circuit["scope"] == endpoint["scope"] == "COMMUNITY_LEVEL"
    assert "98.3%" in endpoint["description"] and "89.5%" in endpoint["description"]
    assert "complete carbon balance" in endpoint["description"]


def test_syntrophy_review_follows_the_current_schema_not_an_obligacy_requirement():
    ledger, _, docs = records()
    schema = yaml.safe_load((ROOT / "src/communitymech/schema/communitymech.yaml").read_text())
    definition = schema["enums"]["InteractionTypeEnum"]["permissible_values"]["SYNTROPHY"][
        "description"
    ]
    assert "Obligacy is not asserted." in definition
    correction = ledger["precommit_adversarial_correction"]
    assert correction["schema_definition"] == definition
    assert correction["superseded_regressions"].startswith("816 passed")
    assert len(correction["records"]) == 2
    for node in docs[2]["ecological_interactions"][:2]:
        assert node["interaction_type"] == "SYNTROPHY"
        assert "does not assert obligacy" in " ".join(node["description"].split())


def test_diatom_workflow_and_environmental_scope_do_not_become_pair_mechanisms():
    _, rows, docs = records()
    synthesis, response, exchange = docs[3]["ecological_interactions"]
    removed = {n["node"] for n in rows[3]["removed_node_decisions"]}
    assert removed == {
        "Diatom-Associated Bacterial Consortium Resolution",
        "Coastal Sulfitobacter IAA Prevalence",
    }
    assert synthesis["downstream"][0]["target"] == response["name"]
    assert "IAA promotes diatom cell division" in response["description"]
    assert all("interaction_type" not in n for n in [synthesis, response, exchange])
    assert "widespread" in docs[3]["environmental_factors"][0]["value"]
    assert "#1742" in docs[3]["discussions"][-1]["rationale"]


def test_all_original_nodes_edges_and_graph_anchors_have_dispositions():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 12
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 2
    assert sum(len(r["edges_before"]) for r in rows) == 7
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 7
    assert all(
        not r["removed_edge_decisions"] and not r["mechanical_edge_source_corrections"]
        for r in rows
    )
    for row, doc in zip(rows, docs, strict=True):
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert {(e["source"], e["target"]) for e in row["edges_before"]} == {
            (e["source"], e["target"]) for e in row["edges_after"]
        }
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_abstract_matches_are_not_full_text_certification():
    ledger, _, _ = records()
    assert ledger["primary_graph_snippet_count"] == 16
    assert len(ledger["discussion_snippet_checks"]) == 8
    checks = ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    assert len(checks) == 24 and all(c["independent_primary_match"] for c in checks)
    assert len(ledger["source_access"]) == 6
    assert all("abstract" in r["accessed_scope"].lower() for r in ledger["source_access"])


def test_history_no_spend_and_unfinished_followups_are_explicit():
    ledger, rows, docs = records()
    assert not ledger["independent_approval"]
    assert ledger["issues"] == [1738, 1739, 1740, 1741]
    assert ledger["unresolved_non_graph_issues"] == [1742]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"] == []
    assert sum(len(row["history_files"]) for row in rows) == 6
    for index, (row, doc) in enumerate(zip(rows, docs, strict=True)):
        assert (
            row["curation_events_added"]
            == len(row["history_files"])
            == (2 if index in [0, 2] else 1)
        )
        assert row["status"] == "reviewed" and doc["curation_history"][-1]["llm_assisted"]


def test_reviewed_records_canonical_participants_and_caches_are_hash_bound():
    ledger, rows, docs = records()
    assert ledger["cache_changes"] == []
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        for node in doc["ecological_interactions"]:
            if node.get("participating_taxa"):
                assert node["participating_taxa"] == canonical
    for path, digest in ledger["primary_artifacts"].items():
        if path.startswith("references_cache/"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
