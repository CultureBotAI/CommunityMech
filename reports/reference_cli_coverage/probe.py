"""Reproduce CLI issue-count semantics without changing records or using the network."""

import json
import tempfile
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path
from unittest.mock import patch

import yaml
from linkml_reference_validator.cli.validate import validate_app
from linkml_reference_validator.plugins.reference_validation_plugin import ReferenceValidationPlugin
from typer.testing import CliRunner

ROOT = Path(__file__).resolve().parents[2]
RECORDS = {
    "Phormidium_Alkaline_Consortium": ("doi_10.3389_fmicb.2022.780346.md", 21, 2),
    "Alseth_FourSpecies_Pathogen_Phage_Community": ("PMID_38648198.txt", 27, 1),
    "PHA_MixedCulture_Phage_Succession_Community": ("PMID_40152616.txt", 24, 0),
}
SCHEMA = "src/communitymech/schema/communitymech.yaml"
SENTINEL = "ZZQQ_UNSUPPORTED_REFERENCE_CLI_COVERAGE_CANARY_XYZ"


def excerpts(value, path=""):
    if isinstance(value, dict):
        if "snippet" in value and "reference" in value:
            yield path + ".snippet", value
        for key, child in value.items():
            yield from excerpts(child, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from excerpts(child, f"{path}[{i}]")


def run_probe(stem="Phormidium_Alkaline_Consortium"):
    started = datetime.now(timezone.utc).isoformat()
    cache_name, native_count, omitted_count = RECORDS[stem]
    record = f"kb/communities/{stem}.yaml"
    cache_path = f"references_cache/{cache_name}"
    original = yaml.safe_load((ROOT / record).read_text())
    items = dict(excerpts(original))
    called = []
    validate_excerpt = ReferenceValidationPlugin._validate_excerpt

    def traced(self, excerpt, reference_id, expected_title, path):
        called.append(path)
        yield from validate_excerpt(self, excerpt, reference_id, expected_title, path)

    results = []
    with tempfile.TemporaryDirectory(prefix="communitymech-cli-probe-") as directory:
        scratch = Path(directory)
        cache = scratch / "cache"
        cache.mkdir()
        # Native DOI filename casing in this isolated fixture only; bytes unchanged.
        native_name = cache_name.replace("doi_", "DOI_", 1)
        (cache / native_name).write_bytes((ROOT / cache_path).read_bytes())
        target = scratch / "record.yaml"
        args = [
            "data",
            str(target),
            "--schema",
            str(ROOT / SCHEMA),
            "--config",
            str(ROOT / "conf/reference_validator.yaml"),
            "--cache-dir",
            str(cache),
        ]
        runner = CliRunner()
        with (
            patch(
                "linkml_reference_validator.etl.reference_fetcher.ReferenceSourceRegistry.get_source",
                side_effect=AssertionError("Network source lookup forbidden in CLI probe"),
            ),
            patch.object(ReferenceValidationPlugin, "_validate_excerpt", traced),
        ):
            cases = ["control", "evidence_mutation", "restoration"]
            if omitted_count:
                cases.append("discussion_mutation")
            for case in cases:
                document = deepcopy(original)
                if case == "evidence_mutation":
                    document["ecological_interactions"][0]["evidence"][0]["snippet"] = SENTINEL
                if case == "discussion_mutation":
                    discussion = next(d for d in document["discussions"] if d.get("evidence"))
                    discussion["evidence"][0]["snippet"] = SENTINEL
                target.write_text(yaml.safe_dump(document, sort_keys=False))
                called.clear()
                result = runner.invoke(validate_app, args)
                expected = 1 if case == "evidence_mutation" else 0
                assert result.exit_code == expected, (case, result.output, result.exception)
                expected_paths = sorted(p for p in items if not p.startswith("discussions["))
                assert sorted(called) == expected_paths, (case, called, expected_paths)
                if case == "evidence_mutation":
                    assert SENTINEL in result.output
                    assert (
                        "Location: ecological_interactions[0].evidence[0].snippet" in result.output
                    )
                    assert "Total checks: 1" in result.output
                else:
                    assert "Total checks: 0" in result.output
                results.append(
                    {
                        "case": case,
                        "exit_code": result.exit_code,
                        "excerpt_fields": list(called),
                        "excerpt_count": len(called),
                        "stdout": result.output.replace(str(scratch), "<temporary-directory>"),
                    }
                )
    assert len(items) == native_count + omitted_count
    assert len(expected_paths) == native_count
    return {
        "started_at": started,
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "invocation": "typer.testing.CliRunner invokes the actual validate data command",
        "network_source_lookup_forbidden": True,
        "dependencies": {name: version(name) for name in ("linkml", "linkml-reference-validator")},
        "inputs": {
            p: sha256((ROOT / p).read_bytes()).hexdigest()
            for p in (
                record,
                cache_path,
                SCHEMA,
                "src/communitymech/schema/mech_shared.yaml",
                "conf/reference_validator.yaml",
                "reports/reference_cli_coverage/probe.py",
            )
        },
        "cases": results,
        "omitted_discussion_fields": sorted(set(items) - set(expected_paths)),
        "limit": "Lexical CLI coverage only, not scientific support. Discussion gap #476 remains.",
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--record", choices=RECORDS, default="Phormidium_Alkaline_Consortium")
    args = parser.parse_args()
    receipt = run_probe(args.record)
    with args.output.open("x") as handle:
        json.dump(receipt, handle, indent=2)
        handle.write("\n")
    print(
        json.dumps(
            {
                "cases": [
                    (r["case"], r["exit_code"], r["excerpt_count"]) for r in receipt["cases"]
                ],
                "receipt": str(args.output),
            }
        )
    )
