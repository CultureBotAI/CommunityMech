"""Keep measured coculture outcomes distinct from inferred causal mechanisms."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-three-records-batch20.yaml"
STEMS = [
    "Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture",
    "Clostridium_Ecoli_Nitratidesulfovibrio_Minority_Mediator_Consortium",
    "Clostridium_Ljungdahlii_Kluyveri_Syngas_Alcohol_Coculture",
]


def record(index):
    return yaml.safe_load((ROOT / "kb/communities" / f"{STEMS[index]}.yaml").read_text())


def test_hydrogen_keeps_ammonium_control_without_inventing_nitrogen_fixation_flux():
    supply, hydrogen, transcript = record(0)["ecological_interactions"]
    assert supply["interaction_type"] == "CROSS_FEEDING"
    assert supply["downstream"][0]["target"] == hydrogen["name"]
    assert "PARTIAL" in supply["downstream"][0]["description"]
    assert "ammonium suppression" in hydrogen["description"]
    assert "not a directly measured partition" in hydrogen["description"]
    assert "argon headspace" in hydrogen["description"]
    assert "interaction_type" not in hydrogen
    for node in (hydrogen, transcript):
        assert "GO:0009399" not in {p["term"]["id"] for p in node["biological_processes"]}
    assert hydrogen["evidence"][1]["supports"] == "PARTIAL"


def test_transcription_is_an_observation_not_a_causal_transfer_arrow():
    transcript = record(0)["ecological_interactions"][2]
    assert transcript["name"] == "Transcriptomic Responses Associated with Cocultivation"
    assert "interaction_type" not in transcript
    assert "downstream" not in transcript
    assert "measured responses" in transcript["description"]


def test_minority_exchange_and_inhibition_are_not_growth_mediation_or_minus_minus():
    exchange, inhibition, lactate, growth = record(1)["ecological_interactions"]
    assert all("downstream" not in n for n in (exchange, inhibition, lactate, growth))
    assert "interaction_type" not in exchange
    assert "does not identify a growth-supporting metabolite" in exchange["description"]
    assert all(e["supports"] == "PARTIAL" for e in exchange["evidence"])
    assert "interaction_type" not in inhibition
    assert "early E. coli phase appears unaffected" in inhibition["description"]
    assert "do not reproduce every live-coculture feature" in inhibition["description"]
    assert lactate["interaction_type"] == "CROSS_FEEDING"
    assert lactate["source_taxon"]["term"]["id"] == "NCBITaxon:316385"
    assert lactate["target_taxon"]["term"]["id"] == "NCBITaxon:272562"
    assert "filtered E. coli supernatant" in lactate["description"]


def test_minority_growth_keeps_soluble_control_and_abundance_assay_limits():
    growth = record(1)["ecological_interactions"][3]
    assert "interaction_type" not in growth
    assert "5.5 h versus 9 h" in growth["description"]
    assert "mixed-culture OD600" in growth["description"]
    assert "copies per ng DNA are not direct live-cell counts" in growth["description"]
    assert "without simultaneous contact" in growth["description"]
    assert "not itself a colonization assay" in growth["description"]
    assert "supernatant" in growth["evidence"][-1]["snippet"]


def test_syngas_retains_links_without_reverse_alcohol_donation():
    supply, elongation, alcohol, ph = record(2)["ecological_interactions"]
    assert supply["downstream"][0]["target"] == elongation["name"]
    assert "calculated from stoichiometry" in supply["description"]
    assert elongation["source_taxon"]["term"]["id"] == "NCBITaxon:1534"
    assert elongation["target_taxon"]["term"]["id"] == "NCBITaxon:1538"
    assert "not ethanol transfer in that direction" in elongation["description"]
    assert elongation["downstream"][0]["target"] == alcohol["name"]
    assert elongation["downstream"][0]["description"].startswith("PARTIAL")
    assert "does not exclude a C. kluyveri contribution" in alcohol["description"]
    for node in (alcohol, ph):
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert "interaction_type" not in node
        assert "source_taxon" not in node and "target_taxon" not in node
        assert {t["term"]["id"] for t in node["participating_taxa"]} == {
            "NCBITaxon:1538",
            "NCBITaxon:1534",
        }


def test_syngas_anion_grounding_and_single_run_ph_scope():
    _, elongation, alcohol, ph = record(2)["ecological_interactions"]
    for node in (elongation, alcohol):
        ids = {m["term"]["id"] for m in node["metabolites"]}
        assert {"CHEBI:17968", "CHEBI:17120"} <= ids
        assert not {"CHEBI:30772", "CHEBI:30776"} & ids
    assert "pH-dependent undissociated acids" in alcohol["description"]
    assert "one continuously operated reactor" in ph["description"]
    assert "not measured reciprocal ecological harm" in ph["description"]


def test_batch20_ledger_accounts_for_every_node_arrow_and_preserved_cache():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    rows = ledger["records"]
    assert len(rows) == 3
    assert sum(len(r["node_decisions"]) for r in rows) == 11
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 3
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 3
    assert sum(len(r["renamed_nodes"]) for r in rows) == 5
    for row in rows:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        nodes = doc["ecological_interactions"]
        names = {n["name"] for n in nodes}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        edges = [{"source": n["name"], **e} for n in nodes for e in n.get("downstream", [])]
        assert row["edges_after"] == edges
        renames = row["renamed_nodes"]
        before = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        removed = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        retained = {(e["source"], e["target"]) for e in row["retained_edge_decisions"]}
        assert before == retained | removed and not retained & removed
        assert all(e["target"] in names for e in edges)
        assert any(d["kind"] == "KNOWLEDGE_GAP" for d in doc["discussions"])
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
