"""Trace every native excerpt call and prove fabricated evidence is rejected."""

import json
import tempfile
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

import yaml
from linkml_reference_validator.cli.validate import validate_app
from linkml_reference_validator.plugins.reference_validation_plugin import ReferenceValidationPlugin
from typer.testing import CliRunner

ROOT = Path(__file__).resolve().parents[3]
RECORD = "kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml"
SENTINEL = "Fabricated Transwell claim for isolated negative-control testing."


def excerpts(node, path=""):
    if isinstance(node, dict):
        if "snippet" in node and "reference" in node:
            yield path + ".snippet"
        for key, value in node.items():
            yield from excerpts(value, f"{path}.{key}" if path else key)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from excerpts(value, f"{path}[{index}]")


def main():
    doc = yaml.safe_load((ROOT / RECORD).read_text())
    expected = sorted(excerpts(doc))
    assert len(expected) == 16
    called = []
    native = ReferenceValidationPlugin._validate_excerpt

    def traced(self, excerpt, reference_id, expected_title, path):
        called.append(path)
        yield from native(self, excerpt, reference_id, expected_title, path)

    outcomes = []
    with tempfile.TemporaryDirectory(prefix="transwell-excerpts-") as directory:
        scratch = Path(directory)
        for name in ["PMID_29152587.txt", "PMID_33159606.txt"]:
            (scratch / name).write_bytes((ROOT / "references_cache" / name).read_bytes())
        target = scratch / "record.yaml"
        with (
            patch(
                "linkml_reference_validator.etl.reference_fetcher.ReferenceSourceRegistry.get_source",
                side_effect=AssertionError("Unexpected source network lookup"),
            ),
            patch.object(ReferenceValidationPlugin, "_validate_excerpt", traced),
        ):
            for case in ["control", "mutation", "restoration"]:
                candidate = deepcopy(doc)
                if case == "mutation":
                    candidate["taxonomy"][0]["evidence"][0]["snippet"] = SENTINEL
                    assert candidate != doc
                target.write_text(yaml.safe_dump(candidate, sort_keys=False))
                called.clear()
                result = CliRunner().invoke(
                    validate_app,
                    [
                        "data",
                        str(target),
                        "--schema",
                        str(ROOT / "src/communitymech/schema/communitymech.yaml"),
                        "--config",
                        str(ROOT / "conf/reference_validator.yaml"),
                        "--cache-dir",
                        str(scratch),
                    ],
                )
                assert result.exit_code == (1 if case == "mutation" else 0), result.output
                assert sorted(called) == expected, (called, expected)
                if case == "mutation":
                    assert (
                        "taxonomy[0].evidence[0].snippet" in result.output
                        and SENTINEL in result.output
                    )
                outcomes.append(
                    {"case": case, "exit_code": result.exit_code, "excerpt_count": len(called)}
                )
    print(
        json.dumps(
            {"cases": outcomes, "excerpt_fields": expected, "network_lookup_forbidden": True},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
