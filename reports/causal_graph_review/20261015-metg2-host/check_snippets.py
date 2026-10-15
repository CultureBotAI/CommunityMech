"""Trace the real CLI and explicitly check its two omitted Discussion excerpts."""

import importlib.util
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

from linkml_reference_validator.models import ReferenceValidationConfig
from linkml_reference_validator.plugins.reference_validation_plugin import ReferenceValidationPlugin
import yaml

ROOT = Path(__file__).resolve().parents[3]
STEM = "SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience"
CACHE = "doi_10.1016_j.rhisph.2025.101142.md"
spec = importlib.util.spec_from_file_location(
    "native_cli_probe", ROOT / "reports/reference_cli_coverage/probe.py"
)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)
probe.RECORDS[STEM] = (CACHE, 6, 2)
receipt = probe.run_probe(STEM)
doc = yaml.safe_load((ROOT / f"kb/communities/{STEM}.yaml").read_text())
items = dict(probe.excerpts(doc))
with tempfile.TemporaryDirectory(prefix="metg2-explicit-excerpts-") as directory:
    cache = Path(directory)
    (cache / CACHE.replace("doi_", "DOI_", 1)).write_bytes(
        (ROOT / "references_cache" / CACHE).read_bytes()
    )
    plugin = ReferenceValidationPlugin(config=ReferenceValidationConfig(cache_dir=cache))
    with patch(
        "linkml_reference_validator.etl.reference_fetcher.ReferenceSourceRegistry.get_source",
        side_effect=AssertionError("Unexpected network source lookup"),
    ):
        results = {
            field: list(plugin._validate_excerpt(item["snippet"], item["reference"], None, field))
            for field, item in items.items()
        }
        assert not any(results.values()), results
        field = receipt["omitted_discussion_fields"][0]
        item = items[field]
        assert list(plugin._validate_excerpt(probe.SENTINEL, item["reference"], None, field))
        assert not list(plugin._validate_excerpt(item["snippet"], item["reference"], None, field))
receipt["explicit_excerpt_fields"] = list(results)
receipt["explicit_excerpt_count"] = len(results)
receipt["discussion_mutation_rejected_and_restored"] = True
print(json.dumps(receipt, indent=2))
