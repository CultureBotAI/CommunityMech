"""Exercise real binding traversal with a small deterministic ontology adapter."""

from linkml.validator import Validator
from linkml.validator.report import Severity
from linkml_term_validator.plugins import BindingValidationPlugin

from communitymech.paths import REPO_ROOT


class OntologyControl:
    """Only the ontology service is substituted; native binding/range code runs."""

    LABELS = {
        "PATO:0000146": "temperature",
        "PATO:0000001": "quality",
        "CHEBI:18243": "dopamine",
        "CHEBI:24431": "chemical entity",
        "GO:0008150": "biological_process",
        "UO:0000032": "hour",
        "UO:0000003": "time unit",
        "UO:0000009": "kilogram",
    }
    PARENTS = {
        "PATO:0000146": ["PATO:0000001"],
        "CHEBI:18243": ["CHEBI:24431"],
        "UO:0000032": ["UO:0000003"],
    }

    def label(self, curie):
        return self.LABELS.get(curie)

    def ancestors(self, curie, predicates):
        assert predicates == ["rdfs:subClassOf"]
        return iter([curie, *self.PARENTS.get(curie, [])])


def validate(doc, monkeypatch, tmp_path):
    plugin = BindingValidationPlugin(cache_dir=tmp_path, cache_labels=False, strict=True)
    monkeypatch.setattr(plugin, "_get_adapter", lambda prefix: OntologyControl())
    validator = Validator(
        schema=str(REPO_ROOT / "src/communitymech/schema/communitymech.yaml"),
        validation_plugins=[plugin],
    )
    return [
        r
        for r in validator.validate(doc, "MicrobialCommunity").results
        if r.severity in {Severity.ERROR, Severity.WARN}
    ]


def test_factor_binding_is_optional_but_rejects_wrong_ontology_and_label(monkeypatch, tmp_path):
    factor = {"name": "temperature"}
    doc = {
        "id": "CommunityMech:999998",
        "name": "binding control",
        "environmental_factors": [factor],
    }
    assert validate(doc, monkeypatch, tmp_path) == []
    factor["term"] = {"id": "PATO:0000146", "label": "temperature"}
    assert validate(doc, monkeypatch, tmp_path) == []
    factor["term"] = {"id": "GO:0008150", "label": "biological_process"}
    assert any("EnvironmentalFactorTerm" in r.message for r in validate(doc, monkeypatch, tmp_path))
    factor["term"] = {"id": "PATO:0000146", "label": "incorrect label"}
    assert validate(doc, monkeypatch, tmp_path)


def test_nested_arm_factor_and_time_dimension_bindings_run(monkeypatch, tmp_path):
    factor = {"name": "dopamine", "term": {"id": "CHEBI:18243", "label": "dopamine"}}
    elapsed = {"value": 24, "unit": {"id": "UO:0000032", "label": "hour"}}
    doc = {
        "id": "CommunityMech:999998",
        "name": "nested binding control",
        "treatment_arms": [
            {
                "id": "arm",
                "name": "arm",
                "context": "assay",
                "membership_status": "NOT_REPORTED",
                "conditions": [factor],
                "timepoints": [
                    {
                        "id": "time",
                        "name": "time",
                        "elapsed": elapsed,
                        "reference_event": "inoculation",
                    }
                ],
            }
        ],
    }
    assert validate(doc, monkeypatch, tmp_path) == []
    elapsed["unit"] = {"id": "UO:0000009", "label": "kilogram"}
    assert any("TimeUnitTerm" in r.message for r in validate(doc, monkeypatch, tmp_path))
    elapsed["unit"] = {"id": "UO:0000032", "label": "hour"}
    factor["term"] = {"id": "GO:0008150", "label": "biological_process"}
    assert any("EnvironmentalFactorTerm" in r.message for r in validate(doc, monkeypatch, tmp_path))
