"""Preserve assay boundaries and an explicit unresolved host-response expansion."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch39.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_eucalyptus_prior_traits_are_not_measured_nursery_flux():
    _, docs = records()
    traits, roots, quality = docs[0]["ecological_interactions"]
    assert len(traits["participating_taxa"]) == 5
    assert len(roots["participating_taxa"]) == len(quality["participating_taxa"]) == 6
    assert [m["term"]["id"] for m in traits["metabolites"]] == ["CHEBI:18367"]
    assert "do not demonstrate nitrogen fixation" in traits["description"]
    assert "specific indole-3-acetic acid exchange" in traits["description"]
    assert all("biological_processes" not in n for n in [traits, roots])
    assert docs[0]["taxonomy"][3]["taxon_term"]["gtdb_grounding_status"] == "AMBIGUOUS"
    assert traits["evidence"][-1]["evidence_source"] == "IN_VIVO"
    assert "No genus or phylum showed robust differential abundance" in roots["description"]
    assert "30 A/B-category seedlings" in roots["description"]


def test_eucalyptus_outcomes_do_not_restore_workflow_arrows_or_mutualism():
    _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert all(not {"interaction_type", "downstream"} & n.keys() for n in nodes)
    assert "water control" in nodes[2]["description"]
    assert "not exclusively literal mortality" in nodes[2]["description"]
    assert "greater than 45 degrees" in nodes[2]["description"]
    assert "Seedlings exhibiting severe stem curvature" in nodes[2]["evidence"][-1]["snippet"]
    assert "do not establish reciprocal bacterial fitness" in nodes[2]["description"]
    assert "2026-10-02" in docs[0]["discussions"][-1]["rationale"]


def test_ewaste_keeps_actual_redox_feedback_not_a_transfer_workflow():
    _, docs = records()
    oxidation, metals, adaptation = docs[1]["ecological_interactions"]
    assert [e["target"] for e in oxidation["downstream"]] == [metals["name"]]
    assert [e["target"] for e in metals["downstream"]] == [oxidation["name"]]
    assert [e["target"] for e in adaptation["downstream"]] == [oxidation["name"]]
    assert "oxidant/substrate feedback" in oxidation["downstream"][0]["description"]
    assert "reduces Fe(III) to Fe(II)" in metals["downstream"][0]["description"]
    assert "immediate redox drop" in metals["downstream"][0]["description"]
    assert "biological_processes" not in oxidation
    assert "metabolites" not in adaptation
    assert all("interaction_type" not in n for n in [oxidation, metals, adaptation])


def test_ewaste_shorter_oxidation_lag_is_not_faster_batch_dissolution():
    _, docs = records()
    oxidation, metals, adaptation = docs[1]["ecological_interactions"]
    assert "did not accelerate batch metal dissolution" in oxidation["description"]
    assert "seven days regardless of subculture" in metals["description"]
    assert "whereas leachates of 2% (w/v) PCBs" in metals["evidence"][1]["snippet"]
    assert metals["evidence"][1]["snippet"].endswith("Zn.")
    assert all("1% and 2% solid-PCB STR" in m["concentration"] for m in metals["metabolites"])
    assert "18 to 13 to 7 days" in adaptation["description"]
    assert "ten-day storage pause" in adaptation["description"]
    assert (
        "8% equivalent chemical leachate during the 25-day flask assay" in adaptation["description"]
    )
    assert "not a universal above-8% threshold" in adaptation["description"]
    assert "does not identify genetic resistance" in adaptation["description"]
    assert "omit attached biomass" in adaptation["description"]


def test_fos_distinguishes_dna_enumeration_from_expression_and_flux():
    _, docs = records()
    abundance, expression, metabolites = docs[2]["ecological_interactions"]
    assert len(abundance["participating_taxa"]) == len(metabolites["participating_taxa"]) == 7
    assert len(expression["participating_taxa"]) == 3
    assert "DNA-qPCR estimated" in abundance["description"]
    assert "not CFU viability" in abundance["description"]
    assert "not carbon-mass matched" in abundance["description"]
    assert "biological_processes" not in abundance
    assert "RNA/cDNA-qPCR" in expression["description"]
    assert "partner-resolved cross-feeding" in expression["description"]
    assert expression["evidence"][0]["supports"] == "PARTIAL"
    assert all("downstream" not in n for n in [abundance, expression, metabolites])
    assert all("functional_role" not in t for t in docs[2]["taxonomy"])


def test_fos_figure_specific_assignments_do_not_imply_physiological_absence():
    ledger, docs = records()
    metabolites = docs[2]["ecological_interactions"][2]
    assert [m["term"]["id"] for m in metabolites["metabolites"]] == [
        "CHEBI:30089",
        "CHEBI:28358",
        "CHEBI:17968",
    ]
    assert "does not establish physiological absence" in metabolites["description"]
    assert "glucose-grown profiles were similar" in metabolites["description"]
    assert "not measured ionic speciation" in metabolites["description"]
    assert all("not quantified yield" in m["notes"] for m in metabolites["metabolites"])
    source = ledger["records"][2]["source_review"]["PMID:42781020"]
    assert "visually inspected" in source["scope"]
    assert len(source["figure"]["sha256"]) == 64


def test_batch39_complete_dispositions_canonical_participants_and_history():
    ledger, docs = records()
    assert ledger["independent_approval"] is False and ledger["issues"] == [1445, 1446, 1447]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 9
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 3
    for row, doc in zip(ledger["records"], docs, strict=True):
        canonical = {
            (t["taxon_term"]["term"]["id"], t["taxon_term"]["preferred_term"]): t["taxon_term"]
            for t in doc["taxonomy"]
        }
        names = {n["name"] for n in doc["ecological_interactions"]}
        for node in doc["ecological_interactions"]:
            assert node["scope"] == "COMMUNITY_LEVEL"
            for term in node["participating_taxa"]:
                assert (
                    term["term"] == canonical[(term["term"]["id"], term["preferred_term"])]["term"]
                )
            assert all(
                e["target"] in names and e["target"] != node["name"]
                for e in node.get("downstream", [])
            )
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        assert not row["removed_node_decisions"] and not row["renamed_nodes"]
        assert not row["removed_edge_decisions"]
        assert {(e["source"], e["target"]) for e in row["edges_before"]} == {
            (e["source"], e["target"]) for e in row["edges_after"]
        }
        gap = doc["discussions"][-1]
        assert gap["kind"] == "KNOWLEDGE_GAP" and gap["status"] == "OPEN"
        assert set(gap["attaches_to"]) == {"ecological_interactions#" + n for n in names}
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_fos_expansion_stays_pending_and_nongraph_fields_are_not_certified():
    ledger, docs = records()
    assert [r["status"] for r in ledger["records"]] == ["reviewed", "reviewed", "needs_research"]
    assert ledger["open_nongraph_followups"] == [1448, 1449]
    assert ledger["open_graph_research"] == [1450]
    assert ledger["edison"]["dryrun"]["actual_provider_job"] is False
    assert ledger["edison"]["query_chars"] == 13999
    assert len(docs[2]["discussions"]) == 2
    assert (
        docs[2]["discussions"][0]["discussion_id"]
        == "fos_lactobacillus_hepg2_active_metabolites_unresolved"
    )
    assert docs[2]["discussions"][0]["proposed_experiments"]
    rationale = docs[2]["discussions"][-1]["rationale"]
    assert "0.1 mg/mL" in rationale and "removal, then 0.25 mM palmitate" in rationale
    assert "do not claim graph completeness" in rationale and "#1450" in rationale
    assert (
        "sulfuric acid generation from sulfur oxidation"
        in docs[1]["environmental_factors"][0]["description"]
    )
    assert ledger["issue_deduplication"]["ignored_hidden_local_files_included"] is True
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
