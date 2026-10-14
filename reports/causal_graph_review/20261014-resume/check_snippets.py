"""Instrument native validation so a zero-error report cannot conceal zero coverage."""

from copy import deepcopy
import json
from pathlib import Path
from unittest.mock import patch

from linkml.validator import Validator
from linkml_reference_validator.models import ReferenceValidationConfig
from linkml_reference_validator.plugins.reference_validation_plugin import ReferenceValidationPlugin
import yaml

root = Path(__file__).resolve().parents[3]
path = root / "kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml"
doc = yaml.safe_load(path.read_text())
plugin = ReferenceValidationPlugin(
    config=ReferenceValidationConfig(cache_dir=root / "references_cache")
)
validator = Validator(
    schema=str(root / "src/communitymech/schema/communitymech.yaml"), validation_plugins=[plugin]
)


def walk(value, field=""):
    if isinstance(value, dict):
        if "snippet" in value and "reference" in value:
            yield field + ".snippet", value
        for key, child in value.items():
            yield from walk(child, f"{field}.{key}" if field else key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from walk(child, f"{field}[{i}]")


with patch(
    "linkml_reference_validator.etl.reference_fetcher.ReferenceSourceRegistry.get_source",
    side_effect=AssertionError("Unexpected network lookup"),
):
    with patch.object(plugin, "_validate_excerpt", wraps=plugin._validate_excerpt) as spy:
        clean = validator.validate(doc, target_class="MicrobialCommunity")
        called = [call.args[3] for call in spy.call_args_list]
        items = dict(walk(doc))
        missing = sorted(set(items) - set(called))
        assert missing == [
            "discussions[0].evidence[0].snippet",
            "discussions[0].evidence[1].snippet",
        ]
        assert len(called) == 20
        assert not clean.results, clean.results
        supplemental = {
            field: list(plugin._validate_excerpt(item["snippet"], item["reference"], None, field))
            for field, item in items.items()
        }
        assert not any(supplemental.values()), supplemental
    changed = deepcopy(doc)
    changed["taxonomy"][1]["evidence"][-1]["snippet"] = "UNSUPPORTED_MUTATION_20261014_XYZ"
    assert changed != doc
    red = validator.validate(changed, target_class="MicrobialCommunity")
    assert red.results
    assert any("UNSUPPORTED_MUTATION_20261014_XYZ" in str(r.message) for r in red.results)
    restored = validator.validate(doc, target_class="MicrobialCommunity")
    assert not restored.results
    discussion = items[missing[0]]
    discussion_red = list(
        plugin._validate_excerpt(
            "UNSUPPORTED_DISCUSSION_20261014_XYZ", discussion["reference"], None, missing[0]
        )
    )
    assert discussion_red
    assert not list(
        plugin._validate_excerpt(discussion["snippet"], discussion["reference"], None, missing[0])
    )
print(
    json.dumps(
        {
            "native_cli_snippets_examined": len(called),
            "native_field_paths": called,
            "native_unchecked_fields": missing,
            "explicit_native_excerpt_checks": len(items),
            "control_errors": len(clean.results),
            "mutation_errors": [str(r.message) for r in red.results],
            "discussion_mutation_errors": [str(r.message) for r in discussion_red],
            "restored_errors": len(restored.results),
            "note": "Native CLI prints number of results/errors as Total checks. Its traversal checks20 EvidenceItems but omits2 SupportingReference objects under Discussion.evidence (#476); all22 were separately checked by the unchanged native excerpt matcher with network forbidden. This diagnostic does not alter schema or claim the CLI traverses discussions.",
        },
        indent=2,
    )
)
