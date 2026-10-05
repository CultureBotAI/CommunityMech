"""Preserve assay distinctions and pruning from the fifth causal-graph review."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def nodes(stem):
    return yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())[
        "ecological_interactions"
    ]


def test_coumarin_chemistry_is_not_a_cellular_response_or_physical_dropout():
    release, peroxide, sensitive, shift = nodes("Arabidopsis_Coumarin_Root_SynCom")
    assert all("interaction_type" not in n for n in (release, peroxide, sensitive, shift))
    assert "biological_processes" not in peroxide
    assert all(
        n["metabolites"][0]["term"]["id"] == "CHEBI:23403"
        for n in (release, peroxide, sensitive, shift)
    )
    assert shift["evidence"][1]["evidence_source"] == "COMPUTATIONAL"
    assert sensitive["downstream"][0]["description"].startswith("PARTIAL")


def test_workflow_nodes_and_associative_host_arrow_stay_removed():
    phyllosphere = nodes("Arabidopsis_Phyllosphere_SynCom7")
    assert len(phyllosphere) == 3
    assert not any(n.get("downstream") for n in phyllosphere)
    bsfl = nodes("BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia")
    assert len(bsfl) == 5
    assert not any(n.get("downstream") for n in bsfl)
    assert all("interaction_type" not in n for n in bsfl)


def test_phage_isotope_measurement_is_distinct_from_predicted_hosts():
    carbon, burk, caten, functions = nodes("Avena_Rhizosphere_CrossKingdom_SIP_Community")
    assert carbon["name"] == "Plant-Derived Carbon Incorporation into Phage DNA"
    assert carbon["evidence"][0]["supports"] == "SUPPORT"
    for n in (burk, caten):
        assert n["evidence"][0]["supports"] == "PARTIAL"
        assert n["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
        assert n["downstream"][0]["target"] == carbon["name"]
        assert n["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert functions["evidence"][0]["evidence_source"] == "COMPUTATIONAL"


def test_lignin_proxy_does_not_assert_structural_catabolism():
    signal, dropout, biofilm = nodes("Bacillales_Lignin_Degrading_LDSynCom")
    assert signal["name"] == "LDSynCom lignin-associated phenolic signal"
    assert "biological_processes" not in signal
    assert "biological_processes" not in dropout
    assert biofilm["biological_processes"][0]["term"]["id"] == "GO:0042710"
    assert not any(n.get("downstream") for n in (signal, dropout, biofilm))


def test_supported_exchange_and_reciprocal_plate_interference_are_preserved():
    exchange, enzyme, field = nodes("Bacillus_Bradyrhizobium_Straw_Humification_SynCom")
    assert exchange["interaction_type"] == "CROSS_FEEDING"
    assert "interaction_type" not in enzyme
    assert "interaction_type" not in field
    compatibility, iaa, disease, root, field = nodes(
        "Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom"
    )
    assert compatibility["interaction_type"] == "COMPETITION"
    assert all("interaction_type" not in n for n in (iaa, disease, root, field))
    assert iaa["biological_processes"][0]["term"]["id"] == "GO:0009684"
    assert "biological_processes" not in root


def test_removed_nodes_have_explicit_ledger_decisions():
    ledger = yaml.safe_load(
        (
            ROOT / "reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml"
        ).read_text()
    )
    removed = [n for r in ledger["records"] for n in r.get("removed_nodes", [])]
    assert len(ledger["records"]) == 11
    assert len(removed) == 3
    assert all(n["rationale"].strip() for n in removed)
    assert ledger["deferred_records"][0]["path"].endswith(
        "Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml"
    )
