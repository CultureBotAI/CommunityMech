"""Tests for the `modeled_environment` slot (issue #30 / lab-env re-grounding).

`modeled_environment` records the natural/applied habitat an (often engineered)
community derives from or represents, distinct from `environment_term` (where it
was studied). It's multivalued, optional, ENVO-grounded, and reuses
`EnvironmentDescriptor`.
"""

from pathlib import Path

import yaml

from communitymech.datamodel.communitymech import (
    EnvironmentDescriptor,
    MicrobialCommunity,
    Term,
)

SCHEMA = Path(__file__).parent.parent / "src" / "communitymech" / "schema" / "communitymech.yaml"


def test_modeled_environment_is_optional_multivalued():
    # a community with no modeled_environment is valid (backward compatible)
    mc = MicrobialCommunity(id="CommunityMech:000999", name="Bare")
    assert mc.modeled_environment == []


def test_modeled_environment_accepts_multiple_env_descriptors():
    mc = MicrobialCommunity(
        id="CommunityMech:000999",
        name="Groundwater enrichment",
        environment_term=EnvironmentDescriptor(
            preferred_term="laboratory environment",
            term=Term(id="ENVO:01001405", label="laboratory environment"),
        ),
        modeled_environment=[
            EnvironmentDescriptor(
                preferred_term="groundwater", term=Term(id="ENVO:01001004", label="groundwater")
            ),
        ],
    )
    assert len(mc.modeled_environment) == 1
    assert mc.modeled_environment[0].term.id == "ENVO:01001004"
    # environment_term stays independent (honest study setting)
    assert mc.environment_term.term.id == "ENVO:01001405"


def test_schema_defines_modeled_environment_on_community():
    schema = yaml.safe_load(SCHEMA.read_text())
    slot = schema["classes"]["MicrobialCommunity"]["attributes"]["modeled_environment"]
    assert slot["range"] == "EnvironmentDescriptor"
    assert slot["multivalued"] is True
    assert slot.get("required") is False
