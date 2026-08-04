"""Tests for CommunityMech cross-repo linking schema (RelatedMedia, RelatedIngredient).

Validates:
- YAML test data loads correctly
- RelatedMedia with CultureMech ID pattern validation
- RelatedIngredient with MediaIngredientMech ID pattern validation
- All MediaRelationshipEnum values
- Backward compatibility (communities without new fields)
- Invalid cross-repo ID formats are detected
- Dataclass instantiation from YAML data
"""

import re
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.datamodel.communitymech import (
    GrowthMedia,
    MediaRelationshipEnum,
    MicrobialCommunity,
    RelatedIngredient,
    RelatedMedia,
    Term,
)

TEST_DATA_DIR = Path(__file__).parent / "data" / "test_cross_repo_linking"

CULTUREMECH_ID_PATTERN = re.compile(r"^CultureMech:\d{6}$")
# The MediaIngredientMech:NNNNNN scheme is retired (vestigial per
# MediaIngredientMech#119); ingredient linking joins on chebi_term.


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------


def load_yaml(filename: str) -> dict:
    path = TEST_DATA_DIR / filename
    assert path.exists(), f"Test data file not found: {path}"
    with open(path) as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
# SPRUCE community with full cross-repo links
# ---------------------------------------------------------------------------


class TestSPRUCEWithLinks:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.data = load_yaml("spruce_with_links.yaml")

    def test_basic_fields(self):
        assert self.data["id"] == "CommunityMech:000319"
        assert self.data["name"] == "SPRUCE Peatland Warming Microbial Community"
        assert self.data["ecological_state"] == "STABLE"

    def test_related_media_present(self):
        assert "related_media" in self.data
        assert len(self.data["related_media"]) == 3

    def test_related_media_culturemech_ids(self):
        for rm in self.data["related_media"]:
            cid = rm.get("culturemech_id")
            if cid is not None:
                assert CULTUREMECH_ID_PATTERN.match(cid), f"Invalid CultureMech ID: {cid}"

    def test_related_media_relationship_types(self):
        types = [rm.get("relationship_type") for rm in self.data["related_media"]]
        assert "ENVIRONMENT_ANALOG" in types
        assert "SELECTIVE_ENRICHMENT" in types

    def test_related_media_shared_environment_term(self):
        analog = [
            rm
            for rm in self.data["related_media"]
            if rm.get("relationship_type") == "ENVIRONMENT_ANALOG"
        ]
        assert len(analog) == 2
        for rm in analog:
            assert rm["shared_environment_term"]["id"] == "ENVO:00000044"

    def test_related_media_evidence(self):
        first = self.data["related_media"][0]
        assert "evidence" in first
        ev = first["evidence"][0]
        assert ev["reference"].startswith("PMID:")
        assert ev["supports"] == "SUPPORT"

    def test_related_ingredients_present(self):
        assert "related_ingredients" in self.data
        assert len(self.data["related_ingredients"]) == 2

    def test_related_ingredients_chebi_term(self):
        humic = self.data["related_ingredients"][0]
        assert humic["chebi_term"]["id"] == "CHEBI:34818"
        assert humic["chebi_term"]["label"] == "humic acid"

    def test_related_ingredients_relevance(self):
        for ri in self.data["related_ingredients"]:
            assert "relevance" in ri
            assert len(ri["relevance"]) > 10

    def test_growth_media_coexists(self):
        """Verify growth_media and related_media are independent."""
        assert "growth_media" in self.data
        assert len(self.data["growth_media"]) == 1
        assert self.data["growth_media"][0]["name"] == "Anaerobic Basal Medium"

    def test_dataclass_instantiation(self):
        rm = RelatedMedia(
            preferred_term=self.data["related_media"][0]["preferred_term"],
            culturemech_id=self.data["related_media"][0]["culturemech_id"],
            relevance_notes=self.data["related_media"][0].get("relevance_notes"),
        )
        assert rm.preferred_term == "Acidic Peatland Medium"
        assert rm.culturemech_id == "CultureMech:010001"

        ri = RelatedIngredient(
            preferred_term=self.data["related_ingredients"][0]["preferred_term"],
            mediaingredientmech_id=self.data["related_ingredients"][0]["mediaingredientmech_id"],
            relevance=self.data["related_ingredients"][0].get("relevance"),
        )
        assert ri.preferred_term == "Humic acid"
        assert ri.mediaingredientmech_id == "MediaIngredientMech:000523"


# ---------------------------------------------------------------------------
# Backward compatibility: community without cross-repo fields
# ---------------------------------------------------------------------------


class TestBackwardCompatibility:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.data = load_yaml("community_no_links.yaml")

    def test_loads_without_related_fields(self):
        assert "related_media" not in self.data
        assert "related_ingredients" not in self.data

    def test_basic_fields_intact(self):
        assert self.data["id"] == "CommunityMech:000001"
        assert self.data["name"] == "Test Community Without Cross-Repo Links"
        assert self.data["ecological_state"] == "STABLE"

    def test_dataclass_defaults_empty(self):
        mc = MicrobialCommunity(
            id=self.data["id"],
            name=self.data["name"],
        )
        assert mc.related_media == []
        assert mc.related_ingredients == []


# ---------------------------------------------------------------------------
# All MediaRelationshipEnum values
# ---------------------------------------------------------------------------


class TestAllRelationshipTypes:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.data = load_yaml("community_all_relationship_types.yaml")

    def test_all_five_types_present(self):
        types = [rm["relationship_type"] for rm in self.data["related_media"]]
        expected = {
            "CULTIVATION_MEDIUM",
            "ISOLATION_MEDIUM",
            "ENVIRONMENT_ANALOG",
            "REFERENCED_IN_STUDY",
            "SELECTIVE_ENRICHMENT",
        }
        assert set(types) == expected

    def test_five_related_media(self):
        assert len(self.data["related_media"]) == 5

    def test_two_related_ingredients(self):
        assert len(self.data["related_ingredients"]) == 2

    def test_all_culturemech_ids_valid(self):
        for rm in self.data["related_media"]:
            assert CULTUREMECH_ID_PATTERN.match(rm["culturemech_id"])


# ---------------------------------------------------------------------------
# Cross-repo ID pattern validation
# ---------------------------------------------------------------------------


class TestIDPatternValidation:
    def test_valid_culturemech_ids(self):
        valid = ["CultureMech:000001", "CultureMech:010001", "CultureMech:999999"]
        for cid in valid:
            assert CULTUREMECH_ID_PATTERN.match(cid), f"Should be valid: {cid}"

    def test_invalid_culturemech_ids(self):
        invalid = [
            "CultureMech:12345",  # too few digits
            "CultureMech:1234567",  # too many digits
            "culturemech:000001",  # wrong case
            "MediaIngredientMech:000001",  # wrong prefix
            "CultureMech:abcdef",  # non-numeric
            "CultureMech000001",  # missing colon
            "",  # empty
        ]
        for cid in invalid:
            assert not CULTUREMECH_ID_PATTERN.match(cid), f"Should be invalid: {cid}"


# ---------------------------------------------------------------------------
# Dataclass edge cases
# ---------------------------------------------------------------------------


class TestDataclassEdgeCases:
    def test_related_media_minimal(self):
        """RelatedMedia with only required field (preferred_term)."""
        rm = RelatedMedia(preferred_term="Some Medium")
        assert rm.preferred_term == "Some Medium"
        assert rm.culturemech_id is None
        assert rm.relationship_type is None
        assert rm.shared_environment_term is None
        assert rm.relevance_notes is None

    def test_related_ingredient_minimal(self):
        """RelatedIngredient with only required field (preferred_term)."""
        ri = RelatedIngredient(preferred_term="Some Ingredient")
        assert ri.preferred_term == "Some Ingredient"
        assert ri.mediaingredientmech_id is None
        assert ri.chebi_term is None
        assert ri.relevance is None

    def test_related_media_with_shared_environment_term(self):
        rm = RelatedMedia(
            preferred_term="Test",
            shared_environment_term=Term(id="ENVO:00000044", label="peatland"),
        )
        assert rm.shared_environment_term.id == "ENVO:00000044"

    def test_related_ingredient_with_chebi(self):
        ri = RelatedIngredient(
            preferred_term="Humic acid",
            chebi_term=Term(id="CHEBI:34818", label="humic acid"),
        )
        assert ri.chebi_term.id == "CHEBI:34818"

    def test_related_ingredient_with_shared_environment_term(self):
        """RelatedIngredient carries an ENVO shared_environment_term (issue #30,
        constraint A) — the env join key, mirroring RelatedMedia."""
        ri = RelatedIngredient(
            preferred_term="Humic acid",
            chebi_term=Term(id="CHEBI:34818", label="humic acid"),
            shared_environment_term=Term(id="ENVO:00000044", label="peatland"),
        )
        assert ri.shared_environment_term.id == "ENVO:00000044"

    def test_community_with_both_growth_and_related(self):
        """MicrobialCommunity can have both growth_media and related_media."""
        mc = MicrobialCommunity(
            id="CommunityMech:000050",
            name="Test",
            growth_media=[GrowthMedia(name="Actual Medium")],
            related_media=[RelatedMedia(preferred_term="Related Medium")],
            related_ingredients=[RelatedIngredient(preferred_term="Related Ingredient")],
        )
        assert len(mc.growth_media) == 1
        assert len(mc.related_media) == 1
        assert len(mc.related_ingredients) == 1

    def test_enum_values_accessible(self):
        assert MediaRelationshipEnum.CULTIVATION_MEDIUM is not None
        assert MediaRelationshipEnum.ISOLATION_MEDIUM is not None
        assert MediaRelationshipEnum.ENVIRONMENT_ANALOG is not None
        assert MediaRelationshipEnum.REFERENCED_IN_STUDY is not None
        assert MediaRelationshipEnum.SELECTIVE_ENRICHMENT is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
