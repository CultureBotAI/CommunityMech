"""Check every excerpt offline, with explicit Discussion traversal and negative controls."""

from copy import deepcopy
import json
from pathlib import Path
from unittest.mock import patch

from linkml.validator import Validator
from linkml_reference_validator.models import ReferenceValidationConfig
from linkml_reference_validator.plugins.reference_validation_plugin import ReferenceValidationPlugin
import yaml

ROOT = Path(__file__).resolve().parents[3]


def walk(value, field=""):
    if isinstance(value, dict):
        if "snippet" in value and "reference" in value:
            yield field + ".snippet", value
        for key, child in value.items():
            yield from walk(child, f"{field}.{key}" if field else key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{field}[{index}]")


doc = yaml.safe_load((ROOT / "kb/communities/Phormidium_Alkaline_Consortium.yaml").read_text())
items = dict(walk(doc))
with patch(
    "linkml_reference_validator.etl.reference_fetcher.ReferenceSourceRegistry.get_source",
    side_effect=AssertionError("Unexpected network lookup"),
):
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
    assert sorted(called) == sorted(f for f in items if not f.startswith("discussions["))
    assert not control.results, control.results
    for field, item in items.items():
        assert not list(plugin._validate_excerpt(item["snippet"], item["reference"], None, field))
    changed = deepcopy(doc)
    changed["taxonomy"][0]["evidence"][-1]["snippet"] = "UNSUPPORTED_BATCH132_IDENTITY_XYZ"
    red = validator.validate(changed, target_class="MicrobialCommunity")
    assert any("UNSUPPORTED_BATCH132_IDENTITY_XYZ" in str(r.message) for r in red.results)
    assert not validator.validate(doc, target_class="MicrobialCommunity").results
    omitted = sorted(set(items) - set(called))
    for field in omitted:
        item = items[field]
        assert list(
            plugin._validate_excerpt(
                "UNSUPPORTED_BATCH132_DISCUSSION_XYZ", item["reference"], None, field
            )
        )
print(
    json.dumps(
        {
            "record": doc["id"],
            "native_count": len(called),
            "native_fields": called,
            "explicit_excerpt_count": len(items),
            "native_omitted_discussions": omitted,
            "identity_control_mutation_restoration": "passed",
            "discussion_negative_controls": "passed",
            "network_forbidden": True,
            "limit": "Lexical matches do not establish scientific support; known Discussion traversal gap #476 is compensated, not fixed.",
        },
        indent=2,
    )
)
