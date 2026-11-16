"""Community schema/model controls for supplement routing, #1996, 2026-11-15.

Exercises the actual consumer schema with its frozen LinkML dependency versions.
Adapted from the reviewed Claw #1283 shared-contract controls; both evidence
classes must preserve old citations and reject malformed explicit selections.
"""

import importlib
import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml
from jsonschema.validators import validator_for
from linkml.generators.jsonschemagen import JsonSchemaGenerator

from communitymech.datamodel.communitymech import EvidenceItem, SourceLocator, SupportingReference

SCHEMA = Path(__file__).resolve().parents[1] / "src/communitymech/schema/communitymech.yaml"
LOCATOR = {
    "kind": "supplement",
    "asset_id": "table-s1.docx",
    "version": "published",
    "table": 1,
    "row": 12,
    "cell": 2,
}


@pytest.fixture(scope="module", params=["EvidenceItem", "SupportingReference"])
def evidence_contract(request):
    # Follow Claw #263: generate the actual closed schema outside any damaged
    # process-global parent YAML loader, retaining this interpreter/dependencies.
    generated = subprocess.run(
        [
            sys.executable,
            "-c",
            "from linkml.generators.jsonschemagen import JsonSchemaGenerator\n"
            "import sys\n"
            "print(JsonSchemaGenerator(sys.argv[1], top_class=sys.argv[2], "
            "not_closed=False).serialize())\n",
            str(SCHEMA),
            request.param,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    schema = json.loads(generated.stdout)
    validator_type = validator_for(schema)
    validator_type.check_schema(schema)
    citation = {"reference": "PMID:36472419", "snippet": "The exact source cell text."}
    if request.param == "EvidenceItem":
        citation.update(supports="SUPPORT", evidence_source="IN_VITRO")
    return validator_type(schema), citation


def test_actual_consumer_schema_accepts_old_and_selected_citations(evidence_contract):
    validator, citation = evidence_contract
    validator.validate(citation)
    validator.validate({**citation, "source_locator": LOCATOR})


@pytest.mark.parametrize("missing", LOCATOR)
def test_actual_consumer_schema_requires_complete_locator(evidence_contract, missing):
    validator, citation = evidence_contract
    locator = deepcopy(LOCATOR)
    del locator[missing]
    assert list(validator.iter_errors({**citation, "source_locator": locator}))


@pytest.mark.parametrize(
    "field,value",
    [
        ("kind", "article"),
        ("asset_id", ""),
        ("version", " \t"),
        ("table", 0),
        ("row", -1),
        ("cell", True),
        ("table", "1"),
        ("row", 1.5),
        ("cell", None),
        ("unknown_field", "ignored"),
    ],
)
def test_actual_consumer_schema_rejects_malformed_selection(evidence_contract, field, value):
    validator, citation = evidence_contract
    locator = {**LOCATOR, field: value}
    assert list(validator.iter_errors({**citation, "source_locator": locator}))


@pytest.mark.parametrize("model", [EvidenceItem, SupportingReference])
def test_generated_model_preserves_locator_and_original_citation(model):
    citation = {"reference": "PMID:36472419", "snippet": "The exact source cell text."}
    if model is EvidenceItem:
        citation.update(supports="SUPPORT", evidence_source="IN_VITRO")
    original = model(**citation)
    selected = model(**citation, source_locator=deepcopy(LOCATOR))
    assert original.source_locator is None
    assert selected.reference == original.reference
    assert selected.snippet == original.snippet
    assert isinstance(selected.source_locator, SourceLocator)
    assert str(selected.source_locator.kind) == "supplement"
    for field in ("asset_id", "version", "table", "row", "cell"):
        assert getattr(selected.source_locator, field) == LOCATOR[field]


@pytest.mark.parametrize("top_class", ["EvidenceItem", "SupportingReference"])
def test_consumer_schema_survives_damaged_parent_loader_and_restoration(monkeypatch, top_class):
    """Prevent the observed Claw #263 fixture failure at both consumer roots."""

    class NullTagLoader(yaml.SafeLoader):
        def resolve(self, kind, value, implicit):
            return None

    loader = importlib.import_module("linkml_runtime.loaders.yaml_loader")
    original = loader.DupCheckYamlLoader
    request = SimpleNamespace(param=top_class)
    with monkeypatch.context() as changed:
        changed.setattr(loader, "DupCheckYamlLoader", NullTagLoader)
        with pytest.raises(yaml.constructor.ConstructorError, match="tag None"):
            JsonSchemaGenerator(str(SCHEMA), top_class=top_class, not_closed=False).serialize()
        isolated, citation = evidence_contract.__wrapped__(request)
        isolated.validate(citation)
        isolated.validate({**citation, "source_locator": LOCATOR})
        incomplete = {key: value for key, value in LOCATOR.items() if key != "cell"}
        assert not isolated.is_valid({**citation, "source_locator": incomplete})
        assert not isolated.is_valid({**citation, "source_locator": {**LOCATOR, "row": 0}})
        assert loader.DupCheckYamlLoader is NullTagLoader
    assert loader.DupCheckYamlLoader is original
    restored, citation = evidence_contract.__wrapped__(request)
    restored.validate({**citation, "source_locator": LOCATOR})
