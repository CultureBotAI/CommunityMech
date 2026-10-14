"""Enumerate native and discussion excerpt coverage with negative controls."""

from copy import deepcopy
import json
from pathlib import Path
from unittest.mock import patch

from linkml.validator import Validator
from linkml_reference_validator.models import ReferenceValidationConfig
from linkml_reference_validator.plugins.reference_validation_plugin import ReferenceValidationPlugin
import yaml

ROOT = Path(__file__).resolve().parents[3]
RECORDS = (
    "Alseth_FourSpecies_Pathogen_Phage_Community",
    "PHA_MixedCulture_Phage_Succession_Community",
)


def walk(value, field=""):
    if isinstance(value, dict):
        if "snippet" in value and "reference" in value:
            yield field + ".snippet", value
        for key, child in value.items():
            yield from walk(child, f"{field}.{key}" if field else key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{field}[{index}]")


results = []
with patch(
    "linkml_reference_validator.etl.reference_fetcher.ReferenceSourceRegistry.get_source",
    side_effect=AssertionError("Unexpected network lookup"),
):
    for stem in RECORDS:
        doc = yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())
        items = dict(walk(doc))
        assert items
        plugin = ReferenceValidationPlugin(
            config=ReferenceValidationConfig(cache_dir=ROOT / "references_cache")
        )
        validator = Validator(
            schema=str(ROOT / "src/communitymech/schema/communitymech.yaml"),
            validation_plugins=[plugin],
        )
        with patch.object(plugin, "_validate_excerpt", wraps=plugin._validate_excerpt) as spy:
            control = validator.validate(doc, target_class="MicrobialCommunity")
            called = [call.args[3] for call in spy.call_args_list]
        expected = [field for field in items if not field.startswith("discussions[")]
        assert sorted(called) == sorted(expected)
        assert not control.results, control.results
        for field, item in items.items():
            assert not list(
                plugin._validate_excerpt(item["snippet"], item["reference"], None, field)
            )
        changed = deepcopy(doc)
        changed["ecological_interactions"][0]["evidence"][0][
            "snippet"
        ] = "UNSUPPORTED_BATCH130_GRAPH_XYZ"
        assert changed != doc
        red = validator.validate(changed, target_class="MicrobialCommunity")
        assert any("UNSUPPORTED_BATCH130_GRAPH_XYZ" in str(item.message) for item in red.results)
        assert not validator.validate(doc, target_class="MicrobialCommunity").results
        missing = sorted(set(items) - set(called))
        for field in missing:
            item = items[field]
            assert list(
                plugin._validate_excerpt(
                    "UNSUPPORTED_BATCH130_DISCUSSION_XYZ", item["reference"], None, field
                )
            )
            assert not list(
                plugin._validate_excerpt(item["snippet"], item["reference"], None, field)
            )
        results.append(
            {
                "record": stem,
                "native_fields": called,
                "native_count": len(called),
                "explicit_excerpt_count": len(items),
                "native_omitted_discussions": missing,
                "graph_control_mutation_restoration": "passed",
                "discussion_control_mutation_restoration": (
                    "passed" if missing else "not_applicable"
                ),
            }
        )
print(
    json.dumps(
        {
            "records": results,
            "network_forbidden": True,
            "limit": "Explicit excerpt checks compensate for the known Discussion traversal gap #476; lexical matches do not prove causal support.",
        },
        indent=2,
    )
)
