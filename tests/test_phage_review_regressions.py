"""Keep phage hypotheses, sequence observations and assay contexts distinct."""

from copy import deepcopy
from pathlib import Path

import pytest
import yaml
from genus_gtdb_successors import admit_genus_successor

ROOT = Path(__file__).resolve().parents[1]
PHA = ROOT / "kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml"
ALSETH = ROOT / "kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml"
PHAGE_BEFORE = {
    "kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml": (
        "cef1f3c47035ef336cb809456b25a185e0397bb9f0a16c492becdb5b371529f5"
    ),
    "kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml": (
        "aebd6497b6d5a6f49e9e9ef956d4ec0847960acc0fd2413dce5e0960ed748488"
    ),
}


def _record(path=PHA):
    return yaml.safe_load(path.read_text())


def _review_contract(record):
    nodes = record["ecological_interactions"]
    assert len(nodes) == 5
    hypothesis = nodes[0]
    assert hypothesis["interaction_type"] == "KILL_THE_WINNER"
    assert "HYPOTHESIZED" in hypothesis["description"]
    assert not hypothesis.get("downstream")
    assert all(e["supports"] == "PARTIAL" for e in hypothesis["evidence"])
    assert "Structural equation modeling" in hypothesis["evidence"][0]["snippet"]
    for node in nodes[1:]:
        assert "interaction_type" not in node
    for index in (0, 1, 2, 4):
        for evidence in nodes[index]["evidence"]:
            assert evidence["evidence_source"] == "COMPUTATIONAL"
            assert evidence["computational_provenance"]["prediction_type"]
    amg = nodes[3]["evidence"]
    assert amg[0]["evidence_source"] == "COMPUTATIONAL"
    assert amg[0]["computational_provenance"]["tools"][0]["tool_name"] == "DRAM-V"
    assert amg[1]["evidence_source"] == "IN_VITRO"
    assert "transcribed" in amg[1]["snippet"]
    defense = nodes[4]["evidence"][0]["computational_provenance"]
    assert defense["tools"][0]["tool_name"] == "DefenseFinder"
    assert defense["tools"][0]["tool_version"] == "1.2.2"
    viral_member = record["taxonomy"][-1]
    assert viral_member["taxon_term"]["term"]["id"] == "NCBITaxon:10239"
    assert not viral_member.get("functional_role")
    assert not viral_member.get("abundance_level")
    setup = record["cultivation_setup"][0]
    assert setup["working_volume"] == 2.0
    assert setup["working_volume_unit"] == "L"
    assert setup["cultivation_mode"] == "SEQUENCING_BATCH"
    assert "do_controlled" not in setup
    assert "controls_notes" not in setup
    assert "separate 400 mL" in setup["notes"]


def test_pha_observations_preserve_modality_and_assay_scope():
    _review_contract(_record())


@pytest.mark.parametrize(
    "mutation",
    [
        "infection",
        "wet_lab_prediction",
        "missing_provenance",
        "causal_support",
        "causal_arrow",
        "uniform_lytic_role",
        "oxygen_flag",
        "wrong_vessel",
    ],
)
def test_review_contract_rejects_regressions_and_accepts_restoration(mutation):
    original = _record()
    _review_contract(original)
    changed = deepcopy(original)
    nodes = changed["ecological_interactions"]
    if mutation == "infection":
        nodes[4]["interaction_type"] = "LYTIC_INFECTION"
    elif mutation == "wet_lab_prediction":
        nodes[4]["evidence"][0]["evidence_source"] = "IN_VITRO"
    elif mutation == "missing_provenance":
        nodes[4]["evidence"][0]["computational_provenance"]["prediction_type"] = ""
    elif mutation == "causal_support":
        nodes[0]["evidence"][0]["supports"] = "SUPPORT"
    elif mutation == "causal_arrow":
        nodes[0]["downstream"] = [{"target": nodes[2]["name"], "description": "Causes"}]
    elif mutation == "uniform_lytic_role":
        changed["taxonomy"][-1]["functional_role"] = ["LYTIC_PHAGE"]
    elif mutation == "oxygen_flag":
        changed["cultivation_setup"][0]["do_controlled"] = True
    else:
        changed["cultivation_setup"][0]["working_volume"] = 0.4
    with pytest.raises(AssertionError):
        _review_contract(changed)
    _review_contract(original)


def test_phage_corpus_addition_explains_the_grounding_baseline_delta():
    """The introduction census is historical; current mappings require full proof (#2947)."""
    for path, bacterial_count in ((ALSETH, 4), (PHA, 5)):
        members = _historical_members(path)
        unresolved = [
            m for m in members if m["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"
        ]
        assert len(unresolved) == bacterial_count
        assert all("could not locate" in m["taxon_term"]["notes"] for m in unresolved)
        assert len(members) == bacterial_count + 1
        assert members[-1]["taxon_term"]["gtdb_grounding_status"] == "NO_GTDB_EQUIVALENT"


def _historical_members(path):
    relative = path.relative_to(ROOT).as_posix()
    assert relative in PHAGE_BEFORE, "no historical phage census allowance"
    admission = admit_genus_successor(
        ROOT, relative, PHAGE_BEFORE[relative], current=path.read_bytes()
    )
    assert admission.changed, "current phage mapping proof is required"
    return yaml.safe_load(admission.historical_bytes)["taxonomy"]


def test_pha_supporting_snippets_are_contiguous_in_the_primary_cache():
    cache = " ".join((ROOT / "references_cache/PMID_40152616.txt").read_text().split())

    def walk(node):
        if isinstance(node, dict):
            if node.get("reference") == "PMID:40152616" and "snippet" in node:
                assert " ".join(node["snippet"].split()) in cache
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(_record())


def test_lytic_definition_does_not_claim_unique_density_dependence():
    schema = _record(ROOT / "src/communitymech/schema/communitymech.yaml")
    definition = schema["enums"]["InteractionTypeEnum"]["permissible_values"]["LYTIC_INFECTION"][
        "description"
    ]
    guide = (ROOT / "docs/PHAGE_BACTERIA_GUIDE.md").read_text()
    for text in (definition, guide):
        normalized = " ".join(text.split())
        assert "replicates within the host" in normalized
        assert "dependence alone does not distinguish" in normalized
        assert "in a way a grazer's is not" not in normalized
