"""Keep biological results distinct from workflow, substrates and assay inference."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch80.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_vitamin_rescue_and_serial_persistence_remain_positive():
    _, _, docs = records()
    bacterial, algal, stable = docs[0]["ecological_interactions"]
    assert all(n["interaction_type"] == "MUTUALISM" for n in [bacterial, algal, stable])
    assert (
        "30%" in bacterial["description"]
        and "physiological complementation" in bacterial["description"]
    )
    assert "niacin, biotin and p-aminobenzoic acid" in algal["description"]
    assert bacterial["downstream"][0]["target"] == stable["name"]
    assert "four consecutive subcultures" in stable["description"]
    assert "Thiamine and biotin were supplied" in stable["description"]


def test_vitamin_reverse_arrow_removed_without_unapproved_reversal():
    _, rows, docs = records()
    _, algal, stable = docs[0]["ecological_interactions"]
    assert "downstream" not in stable and "downstream" not in algal
    assert rows[0]["status"] == "needs_research" and 1664 in rows[0]["issues"]
    assert len(rows[0]["removed_edge_decisions"]) == 1
    assert "other nutrients" in stable["description"]


def test_pet_positive_hydrolysis_consumption_and_five_arrows_survive():
    _, _, docs = records()
    hydro, tpa, eg, competition, film = docs[1]["ecological_interactions"]
    assert "interaction_type" not in hydro
    assert hydro["source_taxon"]["term"]["id"] == hydro["target_taxon"]["term"]["id"]
    assert hydro["source_taxon"]["preferred_term"] != hydro["target_taxon"]["preferred_term"]
    assert len(hydro["downstream"]) == 2
    assert "28 h" in tpa["description"] and "20 h" in eg["description"]
    for node in [tpa, eg, competition]:
        assert node["downstream"][0]["target"] == film["name"]
        assert node["downstream"][0]["description"].startswith("PARTIAL -")
    assert tpa["evidence"][0]["supports"] == eg["evidence"][0]["supports"] == "SUPPORT"


def test_pet_timing_materials_temperature_and_mediation_are_distinct():
    _, _, docs = records()
    _, tpa, eg, competition, film = docs[1]["ecological_interactions"]
    assert "after 7 days in Results, not the 3 days" in tpa["description"]
    assert "not a PET-film mass balance" in eg["description"]
    assert "day 3" in eg["description"]
    assert "durable coexistence" in competition["description"]
    assert "three species, not four" in film["description"]
    assert "37 C" in film["description"] and "23.2%" in film["description"]
    assert "31.2%" in film["description"] and "mineralization" in film["description"]


def test_column_and_synthetic_palladium_are_not_one_cascade():
    _, _, docs = records()
    al, thio, column = docs[2]["ecological_interactions"]
    assert all("downstream" not in n and "interaction_type" not in n for n in [al, thio, column])
    assert al["metabolites"][0]["term"] == {"id": "CHEBI:28984", "label": "aluminium atom"}
    assert "not direct demonstration" in al["description"]
    assert "uncrushed" in column["description"] and "315 h" in column["description"]
    assert "53.6%" in column["description"] and "105 h" in column["description"]
    assert "metabolites" not in column
    assert all(e["reference"] == "PMID:31059950" for n in [al, column] for e in n["evidence"])
    assert len(docs[2]["taxonomy"]) == 1


def test_palladium_solid_loss_is_not_dissolved_recovery_or_pt_rh():
    _, rows, docs = records()
    thio = docs[2]["ecological_interactions"][1]
    assert "93.22%" in thio["description"] and "63.53%" in thio["description"]
    assert "100 C" in thio["description"] and "60 C" in thio["description"]
    assert "alpha-alumina" in thio["description"] and "precipitation" in thio["description"]
    assert {m["term"]["id"] for m in thio["metabolites"]} == {
        "CHEBI:16094",
        "CHEBI:33363",
        "CHEBI:29036",
        "CHEBI:16134",
    }
    assert rows[2]["status"] == "needs_research" and 1665 in rows[2]["issues"]


def test_variovorax_protocol_nodes_removed_but_positive_individual_hits_kept():
    _, rows, docs = records()
    hits, confirmation, live = docs[3]["ecological_interactions"]
    assert len(rows[3]["removed_node_decisions"]) == 3
    assert "each individually improved" in hits["description"]
    assert "not a six-strain consortium" in hits["description"]
    assert "17%" in confirmation["description"] and "20.4%" in confirmation["description"]
    assert (
        "9.3%" in confirmation["description"] and "not independent" in confirmation["description"]
    )
    assert all(
        "downstream" not in n and "interaction_type" not in n for n in [hits, confirmation, live]
    )


def test_variovorax_live_cell_result_does_not_isolate_contact_or_acc():
    _, _, docs = records()
    live = docs[3]["ecological_interactions"][2]
    assert "no physical-separation experiment is described" in live["description"]
    assert "unstable signals" in live["description"]
    assert "not tested as the mediator" in live["description"]
    assert [e["supports"] for e in live["evidence"]] == ["SUPPORT", "PARTIAL"]
    assert len(docs[3]["taxonomy"]) == 6
    hits, confirmation, _ = docs[3]["ecological_interactions"]
    assert {t["preferred_term"] for t in hits["participating_taxa"]} == {
        t["taxon_term"]["preferred_term"] for t in docs[3]["taxonomy"]
    }
    for node in [confirmation, live]:
        assert node["participating_taxa"] == [
            {
                "preferred_term": "Variovorax sp. CF313",
                "term": {"id": "NCBITaxon:34072", "label": "Variovorax"},
            }
        ]


def test_every_original_node_and_arrow_has_a_decision():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 14
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 3
    assert sum(len(r["edges_before"]) for r in rows) == 10
    assert sum(len(r["edges_after"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 4
    assert (
        ledger["primary_graph_snippet_count"] == ledger["cache_matched_graph_snippet_count"] == 25
    )
    assert ledger["independent_fresh_primary_graph_snippet_count"] == 22
    for row, doc in zip(rows, docs, strict=True):
        renames = row["renamed_nodes"]

        def pairs(edges, mapping=renames):
            return {
                (mapping.get(e["source"], e["source"]), mapping.get(e["target"], e["target"]))
                for e in edges
            }

        before, after, removed = [
            pairs(row[k]) for k in ["edges_before", "edges_after", "removed_edge_decisions"]
        ]
        assert after.isdisjoint(removed) and before == after | removed
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_history_research_and_source_scope_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1660, 1661, 1662, 1663]
    assert ledger["unresolved_research_issues"] == [1664, 1665]
    assert ledger["unresolved_non_graph_issues"] == [1666]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"][0]["query_chars"] == 9032
    for row, doc in zip(rows, docs, strict=True):
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert all((ROOT / p).exists() for p in row["history_files"])
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
