"""Counter-selection had nowhere to live but prose (#307).

A synthetic community is often defined as much by what was screened *out* as by
what shipped. `SynCom_ARC` is exactly that: candidate *Bacillus* isolates that
inhibited *Bradyrhizobium* were excluded, so the community suppresses aflatoxin
without costing nodulation. That constraint is the whole design.

Before this there were two homes for it, and #305 had to pick the least bad:

* an `ecological_interaction` — machine-readable, and **wrong**. The excluded
  and retained isolates are indistinguishable at the genus grounding the source
  supports, so a typed `Bacillus -> Bradyrhizobium COMPETITION` edge asserts to
  anyone reading the graph that an ARC *member* antagonises the mutualist ARC
  was built to spare — the opposite of the finding.
* `engineering_design.notes` prose — accurate, and invisible to any consumer.

`CounterSelection` is the third option. It sits on the design rather than in
`ecological_interactions` because its subjects are outside the community by
construction.

`excluded_taxon` is optional, which is the point rather than laziness: ARC's
source does not say which three isolates were dropped, so `excluded_count`
carries what is known and the taxon slot stays empty rather than asserting an
identity the paper does not support.
"""

from __future__ import annotations

import pathlib

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"
ARC = REPO / "kb/communities/SynCom_ARC_Peanut_Aflatoxin_Nodulation.yaml"


@pytest.fixture(scope="module")
def schema() -> dict:
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


def test_the_class_exists_and_requires_a_criterion(schema):
    """An exclusion without a reason drops the only informative part."""
    attributes = schema["classes"]["CounterSelection"]["attributes"]
    assert attributes["criterion"].get("required") is True
    assert set(attributes) >= {"criterion", "excluded_taxon", "excluded_count", "evidence"}


def test_the_excluded_taxon_is_optional(schema):
    """Required would force ARC to name isolates its source does not name."""
    assert (
        schema["classes"]["CounterSelection"]["attributes"]["excluded_taxon"].get("required")
        is not True
    )


def test_it_hangs_off_the_design_not_the_interactions(schema):
    """The subjects are outside the community, so this is not an interaction."""
    design = schema["classes"]["CommunityEngineeringDesign"]["attributes"]
    assert design["counter_selection"]["range"] == "CounterSelection"
    assert design["counter_selection"].get("multivalued") is True
    interaction = schema["classes"]["EcologicalInteraction"]["attributes"]
    assert "counter_selection" not in interaction


def test_the_motivating_record_now_carries_it_structurally():
    """#305 chose prose because there was no alternative; there is one now."""
    document = yaml.safe_load(ARC.read_text(encoding="utf-8"))
    entries = (document.get("engineering_design") or {}).get("counter_selection") or []
    assert len(entries) == 1, entries

    entry = entries[0]
    assert "Bradyrhizobium" in entry["criterion"]
    assert entry["excluded_count"] == 3
    assert "excluded_taxon" not in entry, (
        "ARC's source does not resolve which three isolates were excluded; naming "
        "one asserts an identity the paper does not support (#305, #307)"
    )
    assert entry.get("evidence"), "an exclusion should be evidence-backed like everything else"


def test_the_prose_that_explains_the_choice_survives():
    """The note says *why* this is not an interaction, which the data cannot.

    Structuring the fact is not a reason to drop the reasoning behind the
    modelling decision — that is what sends the next curator back to the
    misleading edge.
    """
    document = yaml.safe_load(ARC.read_text(encoding="utf-8"))
    notes = (document.get("engineering_design") or {}).get("notes") or ""
    assert "ecological interaction" in notes.lower()


def test_no_record_smuggles_the_exclusion_back_into_the_graph():
    """The edge #305 refused to write must not reappear.

    A `Bacillus -> Bradyrhizobium` antagonism edge inside ARC would say a member
    attacks the mutualist the community was assembled to protect.
    """
    document = yaml.safe_load(ARC.read_text(encoding="utf-8"))
    for interaction in document.get("ecological_interactions") or []:
        if not isinstance(interaction, dict):
            continue
        pair = {
            str((interaction.get(role) or {}).get("preferred_term", ""))
            for role in ("source_taxon", "target_taxon")
        }
        antagonistic = interaction.get("interaction_type") in {"COMPETITION", "AMENSALISM"}
        assert not (
            antagonistic
            and any("Bacillus" in p for p in pair)
            and any("Bradyrhizobium" in p for p in pair)
        ), f"the counter-selection is back as a typed edge: {interaction.get('interaction_type')}"
