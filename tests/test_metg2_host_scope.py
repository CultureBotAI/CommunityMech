"""Keep the sugarcane host separate from microbial transcription (#1847)."""

from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
RECORD = "kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml"


def current():
    return yaml.safe_load((ROOT / RECORD).read_text())


def assert_host_scope(doc):
    host = doc["taxonomy"][0]["taxon_term"]
    phylum = doc["taxonomy"][1]["taxon_term"]
    colonization, functions, response = doc["ecological_interactions"]
    assert host["term"] == {"id": "NCBITaxon:4546", "label": "Saccharum"}
    assert host["preferred_term"] == "sugarcane (Saccharum; species unresolved)"
    assert "parent-rank anchor" in host["notes"]
    assert "not a genus-wide" in host["notes"]
    assert "cultivar" in host["notes"] and "unverified" in host["notes"]
    assert host["gtdb_grounding_status"] == "NO_GTDB_EQUIVALENT"
    assert response["participating_taxa"] == [{k: host[k] for k in ("preferred_term", "term")}]
    assert colonization["participating_taxa"] == [
        {k: phylum[k] for k in ("preferred_term", "term")}
    ]
    assert "species and cultivar remain unverified" in response["description"]
    assert "not by themselves" in response["description"]
    assert functions["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert "not assigned exclusively" in functions["description"]
    assert doc["discussions"][0]["status"] == "OPEN"
    assert "Chiliseed2" in doc["discussions"][0]["rationale"]
    assert "Chileseed2" in doc["discussions"][0]["rationale"]


def test_host_grounding_and_expression_participants():
    assert_host_scope(current())


@pytest.mark.parametrize("mutation", ["species", "all_host", "bacterial_host", "closed"])
def test_control_mutation_restoration(mutation):
    control = current()
    assert_host_scope(control)
    changed = deepcopy(control)
    if mutation == "species":
        changed["taxonomy"][0]["taxon_term"]["term"] = {
            "id": "NCBITaxon:4547",
            "label": "Saccharum officinarum",
        }
    elif mutation == "all_host":
        del changed["ecological_interactions"][2]["participating_taxa"]
    elif mutation == "bacterial_host":
        changed["ecological_interactions"][2]["participating_taxa"] = deepcopy(
            changed["ecological_interactions"][0]["participating_taxa"]
        )
    else:
        changed["discussions"][0]["status"] = "RESOLVED"
    assert changed != control
    with pytest.raises(AssertionError):
        assert_host_scope(changed)
    assert_host_scope(control)
