"""Claim assessments are typed, backward-compatible and never defaulted."""

import json
from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.dumpers import json_dumper
from linkml_runtime.utils.schemaview import SchemaView

from communitymech.datamodel.communitymech import (
    EvidenceItem,
    EvidenceItemSupportEnum,
    EvidenceSourceEnum,
    SupportingReference,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "src/communitymech/schema/communitymech.yaml"
CLASSES = ["EvidenceItem"]
SUPPORT = {"SUPPORT", "REFUTE", "PARTIAL", "NO_EVIDENCE", "WRONG_STATEMENT"}
SOURCES = {
    "FIELD_STUDY",
    "MESOCOSM",
    "LABORATORY",
    "IN_VITRO",
    "IN_VIVO",
    "COMPUTATIONAL",
    "META_ANALYSIS",
    "REVIEW",
    "REMOTE_SENSING",
    "LONG_TERM_MONITORING",
    "EXPERT_OPINION",
    "DATABASE",
    "OTHER",
}
REQUIRED = {"EvidenceItem": {"supports": True, "evidence_source": True}}


@pytest.fixture(scope="module")
def assessment_view():
    return SchemaView(str(SCHEMA))


@pytest.fixture(scope="module")
def assessment_validator():
    return Validator(str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)])


def baseline(view, cls):
    values = {
        "reference": "PMID:12345678",
        "snippet": "A verbatim test fixture passage.",
        "explanation": "Fixture assessment, not a curated scientific assertion.",
        "source": "fixture",
        "supports": "SUPPORT",
        "evidence_source": "IN_VITRO",
    }
    required = {slot.name for slot in view.class_induced_slots(cls) if slot.required}
    assert required == {"reference", "snippet", "supports", "evidence_source"}
    return {name: values[name] for name in required}


@pytest.mark.parametrize("cls", CLASSES)
def test_assessments_preserve_legacy_requiredness_and_have_no_default(
    assessment_view, assessment_validator, cls
):
    for name in ("supports", "evidence_source"):
        slot = assessment_view.induced_slot(name, cls)
        assert bool(slot.required) == REQUIRED[cls][name]
        assert slot.ifabsent is None
        expected = SUPPORT if name == "supports" else SOURCES
        assert set(assessment_view.get_enum(slot.range).permissible_values) == expected
    old = baseline(assessment_view, cls)
    assert not list(assessment_validator.iter_results(old, target_class=cls))


@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize("support", sorted(SUPPORT))
def test_all_support_assessments_validate(assessment_view, assessment_validator, cls, support):
    data = {**baseline(assessment_view, cls), "supports": support, "evidence_source": "DATABASE"}
    assert not list(assessment_validator.iter_results(data, target_class=cls))


@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize("source", sorted(SOURCES))
def test_study_types_validate_without_changing_support(
    assessment_view, assessment_validator, cls, source
):
    data = {**baseline(assessment_view, cls), "supports": "REFUTE", "evidence_source": source}
    assert not list(assessment_validator.iter_results(data, target_class=cls))
    assert data["supports"] == "REFUTE"


@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize(
    "field,value",
    [
        ("supports", "HIGH_CONFIDENCE"),
        ("supports", "support"),
        ("evidence_source", "abstract"),
        ("evidence_source", "LLM_ASSISTED"),
        ("evidence_source", "PMID:123"),
    ],
)
def test_rejects_conflating_assessment_source_and_curation(
    assessment_view, assessment_validator, cls, field, value
):
    valid = {
        **baseline(assessment_view, cls),
        "supports": "PARTIAL",
        "evidence_source": "LABORATORY",
    }
    assert not list(assessment_validator.iter_results(valid, target_class=cls))  # positive control
    invalid = {**valid, field: value}
    assert list(assessment_validator.iter_results(invalid, target_class=cls))


@pytest.mark.parametrize("cls", CLASSES)
def test_unknown_fields_still_fail_closed_validation(assessment_view, assessment_validator, cls):
    data = {**baseline(assessment_view, cls), "invented_evidence_field": "not allowed"}
    assert list(assessment_validator.iter_results(data, target_class=cls))


def test_shared_reference_location_keeps_its_legacy_meaning(assessment_validator):
    data = {"reference": "PMID:12345678", "supports": "PARTIAL", "evidence_source": "abstract"}
    assert not list(assessment_validator.iter_results(data, target_class="SupportingReference"))


@pytest.mark.parametrize("source", sorted(SOURCES))
@pytest.mark.parametrize("support", sorted(SUPPORT))
def test_generated_dataclass_preserves_assessment(assessment_view, source, support):
    payload = {
        **baseline(assessment_view, "EvidenceItem"),
        "supports": support,
        "evidence_source": source,
    }
    result = json.loads(json_dumper.dumps(EvidenceItem(**payload)))
    assert result["supports"] == support
    assert result["evidence_source"] == source


@pytest.mark.parametrize("field", ["reference", "snippet", "supports", "evidence_source"])
def test_required_fields_cannot_be_omitted(assessment_view, assessment_validator, field):
    data = baseline(assessment_view, "EvidenceItem")
    del data[field]
    assert list(assessment_validator.iter_results(data, target_class="EvidenceItem"))
    with pytest.raises(ValueError, match=field):
        EvidenceItem(**data)


@pytest.mark.parametrize("field", ["reference", "snippet", "supports", "evidence_source"])
def test_generated_model_rejects_null_required_fields(assessment_view, field):
    data = {**baseline(assessment_view, "EvidenceItem"), field: None}
    with pytest.raises(ValueError, match=field):
        EvidenceItem(**data)


@pytest.mark.parametrize("field", ["supports", "evidence_source"])
@pytest.mark.parametrize("value", [None, ""])
def test_empty_assessments_are_not_defaulted(assessment_view, assessment_validator, field, value):
    data = {**baseline(assessment_view, "EvidenceItem"), field: value}
    assert list(assessment_validator.iter_results(data, target_class="EvidenceItem"))
    with pytest.raises(ValueError):
        EvidenceItem(**data)


@pytest.mark.parametrize(
    "reference",
    [
        "PMID:12345678",
        "doi:10.1234/fixture",
        "bioproject:PRJNA123456",
        "GITHUB:Example/Fixture/tree/" + "a" * 40,
        "GITHUB:Example/Fixture/blob/" + "b" * 40 + "/evidence.tsv",
        "GITHUB:Example/Fixture/commit/" + "c" * 40,
    ],
)
def test_existing_reference_forms_still_validate(assessment_view, assessment_validator, reference):
    data = {**baseline(assessment_view, "EvidenceItem"), "reference": reference}
    assert not list(assessment_validator.iter_results(data, target_class="EvidenceItem"))
    assert json.loads(json_dumper.dumps(EvidenceItem(**data)))["reference"] == reference


@pytest.mark.parametrize("location", ["abstract", "full_text", "figure", "supplement", "database"])
def test_shared_quotation_locations_round_trip_without_support_default(
    assessment_validator, location
):
    data = {"reference": "https://example.org/fixture", "evidence_source": location}
    assert not list(assessment_validator.iter_results(data, target_class="SupportingReference"))
    result = json.loads(json_dumper.dumps(SupportingReference(**data)))
    assert result["evidence_source"] == location
    assert "supports" not in result


@pytest.mark.parametrize("enum", [EvidenceItemSupportEnum, EvidenceSourceEnum])
def test_generated_enum_descriptions_match_canonical_schema(assessment_view, enum):
    expected = assessment_view.get_enum(enum.__name__).permissible_values
    assert {name for name in vars(enum) if name.isupper()} == set(expected)
    for name, value in expected.items():
        assert getattr(enum, name).description == value.description
