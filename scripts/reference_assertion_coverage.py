#!/usr/bin/env python3
"""Measure native reference CLI comparisons without acquisition or input writes.

Inputs: Git-declared community/isolate records, schema, config and article cache.
Outputs: an exclusive .temp directory of JSON receipts and native CLI logs.
Purpose: maintained successor to the immutable reference_cli_coverage probe;
distinguish issue counts from comparison coverage (#257, #476, #1996).
Date: 2026-11-15. This measures lexical support, not scientific correctness.
"""

from __future__ import annotations

import argparse
import builtins
import inspect
import io
import json
import os
import socket
import subprocess
import sys
from collections import Counter
from contextlib import ExitStack, contextmanager
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha1, sha256
from importlib.metadata import version
from pathlib import Path
from unittest.mock import patch

import yaml
from linkml.validator import Validator
from linkml_reference_validator.cli.validate import validate_app
from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_reference_validator.plugins.reference_validation_plugin import ReferenceValidationPlugin
from linkml_reference_validator.validation.supporting_text_validator import SupportingTextValidator
from typer.testing import CliRunner

from communitymech.paths import REPO_ROOT, default_record_roots

SCHEMA = "src/communitymech/schema/communitymech.yaml"
CONFIG = "conf/reference_validator.yaml"
ASGARD = "kb/communities/Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml"
CANARY_PATH = "related_ingredients[2].evidence[0].snippet"
SUPPORTED_VERSION = "0.2.1"


def digest(data):
    return sha256(data).hexdigest()


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def declared_records(root=REPO_ROOT):
    """Bind the native recipe's top-level YAML denominator to an exact Git tree."""
    revision = git(root, "rev-parse", "HEAD")
    roots = [p.relative_to(REPO_ROOT) for p in default_record_roots()]
    tree = git(root, "ls-tree", "-r", "-z", revision)
    blobs = {
        entry.split("\t", 1)[1]: entry.split("\t", 1)[0].split()[2]
        for entry in tree.split("\0")
        if entry
    }
    tracked = list(blobs)
    records = sorted(p for p in tracked if Path(p).parent in roots and p.endswith(".yaml"))
    disk = sorted(str(p.relative_to(root)) for r in roots for p in (root / r).glob("*.yaml"))
    if not records or records != disk:
        raise ValueError("Git inventory and native on-disk record globs disagree")
    for name in records:
        data = (root / name).read_bytes()
        blob = sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data, usedforsecurity=False
        ).hexdigest()
        if (root / name).is_symlink() or blob != blobs[name]:
            raise ValueError(f"Record is not the exact declared Git input: {name}")
    return revision, records


def input_manifest(root, records):
    """Hash all cache files, including ignored files, and every declared record."""
    paths = {root / p for p in [*records, CONFIG, "uv.lock", "pyproject.toml"]}
    for directory in (root / "references_cache", root / "src/communitymech/schema"):
        paths.update(p for p in directory.rglob("*") if p.is_file())
    if any(p.is_symlink() for p in paths):
        raise ValueError("Input symlinks are not accepted")
    return {str(p.relative_to(root)): digest(p.read_bytes()) for p in sorted(paths)}


def snippet_surfaces(value, path=""):
    """Independent census includes fields that native schema traversal may omit."""
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else key
            if key in {"snippet", "supporting_text"}:
                yield child_path, child, path, key, value
            yield from snippet_surfaces(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from snippet_surfaces(child, f"{path}[{index}]")


def raw_reference(instance):
    """Independent extraction of CommunityMech's supported reference forms (#2795)."""
    for field in ("reference", "reference_id"):
        value = instance.get(field)
        if isinstance(value, dict):
            value = value.get("id") or value.get("reference_id")
        if isinstance(value, str) and value:
            return value
    return None


@contextmanager
def no_side_effects(violations):
    """Hard refusal guards supplement the cache-only adapter; attempts are retained."""

    def refuse(*_args, **_kwargs):
        violations.append("Native acquisition, filesystem mutation or process launch attempted")
        raise RuntimeError(violations[-1])

    def guarded_open(original):
        def opened(file, mode="r", *args, **kwargs):
            if any(flag in mode for flag in "wax+"):
                return refuse()
            return original(file, mode, *args, **kwargs)

        return opened

    original_os_open = os.open

    def guarded_os_open(path, flags, *args, **kwargs):
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
            return refuse()
        return original_os_open(path, flags, *args, **kwargs)

    with ExitStack() as stack:
        for owner, name in ((builtins, "open"), (io, "open")):
            stack.enter_context(patch.object(owner, name, guarded_open(getattr(owner, name))))
        stack.enter_context(patch.object(os, "open", guarded_os_open))
        for name in ("mkdir", "makedirs", "remove", "unlink", "rename", "replace", "rmdir"):
            stack.enter_context(patch.object(os, name, refuse))
        for name in ("connect", "connect_ex", "sendto"):
            stack.enter_context(patch.object(socket.socket, name, refuse))
        for name in ("create_connection", "getaddrinfo"):
            stack.enter_context(patch.object(socket, name, refuse))
        stack.enter_context(patch.object(subprocess, "Popen", refuse))
        for name in (
            "_maybe_retry_full_text",
            "_enrich_with_full_text",
            "_save_by_access",
            "_save_to_disk",
            "_save_pdf",
        ):
            stack.enter_context(patch.object(ReferenceFetcher, name, refuse))
        stack.enter_context(
            patch(
                "linkml_reference_validator.etl.reference_fetcher.ReferenceSourceRegistry.get_source",
                side_effect=refuse,
            )
        )
        yield


class Trace:
    """Wrappers always call the original native traversal and matching functions."""

    def __init__(self, root, documents):
        self.root = root
        self.documents = documents
        self.rows = []
        self.current = None
        self.event = None
        self.violations = []
        self.normalize_reference = None

    @contextmanager
    def instrument(self):
        native_record = Validator.validate
        native_visit = ReferenceValidationPlugin._validate_instance
        native_excerpt = ReferenceValidationPlugin._validate_excerpt
        native_title = ReferenceValidationPlugin._validate_title
        native_validate = SupportingTextValidator.validate
        native_validate_title = SupportingTextValidator.validate_title
        native_match = SupportingTextValidator.find_text_in_reference
        native_substring = SupportingTextValidator._substring_match

        def record(validator, instance, *args, **kwargs):
            index = len(self.rows)
            if index >= len(self.documents) or instance != self.documents[index][1]:
                raise ValueError("Native CLI record dispatch differs from declared inputs")
            name, _ = self.documents[index]
            self.current = {
                "record": name,
                "visits": {},
                "excerpts": [],
                "titles": [],
                "completed": False,
            }
            self.rows.append(self.current)
            result = native_record(validator, instance, *args, **kwargs)
            self.current["issues"] = [
                {"path": r.instantiates, "severity": str(r.severity.value)} for r in result.results
            ]
            self.current["completed"] = True
            return result

        def visit(plugin, instance, class_name, path):
            self.normalize_reference = plugin.validator.fetcher.normalize_reference_id
            self.current["visits"][path] = {
                "class": class_name,
                "excerpt_fields": plugin._find_excerpt_fields(class_name),
            }
            yield from native_visit(plugin, instance, class_name, path)

        def excerpt(plugin, text, reference_id, expected_title, path):
            event = self.new_event(path, reference_id, text)
            event["normalized_reference"] = self.normalize_reference(reference_id)
            self.current["excerpts"].append(event)
            self.event = event
            yield from native_excerpt(plugin, text, reference_id, expected_title, path)
            self.event = None

        def title(plugin, text, reference_id, path):
            event = self.new_event(path, reference_id, text)
            self.current["titles"].append(event)
            self.event = event
            yield from native_title(plugin, text, reference_id, path)
            self.event = None

        def cache_path(fetcher, reference_id):
            # Same native identifier/filename rules; avoid get_cache_dir's mkdir.
            result = fetcher._cache_path(reference_id, self.root / "references_cache")
            if not result.resolve().is_relative_to((self.root / "references_cache").resolve()):
                raise ValueError("Cache path escapes the declared cache")
            return result

        def fetch(fetcher, reference_id, force_refresh=False):
            if force_refresh:
                raise ValueError("Forced acquisition is forbidden")
            normalized = fetcher.normalize_reference_id(reference_id)
            path = cache_path(fetcher, normalized)
            if not path.exists():
                path = path.with_suffix(".txt")
            reference = fetcher._load_from_disk(normalized)
            self.event["cache"] = {
                "requested_reference": normalized,
                "loaded_reference_id": reference.reference_id if reference else None,
                "requested_path": str(path.relative_to(self.root)),
                "sha256": digest(path.read_bytes()) if path.is_file() else None,
                "content_type": reference.content_type if reference else None,
                "has_content": bool(reference and reference.content),
                "has_title": bool(reference and reference.title),
                "loaded": reference is not None,
            }
            return reference

        def finish(validator, result, title_only=False):
            event = self.event
            event["is_valid"] = result.is_valid
            event["severity"] = result.severity.value
            prefix = event["validated_reference"].split(":")[0].upper()
            if prefix in {p.upper() for p in validator.config.skip_prefixes}:
                event["status"] = "skipped_prefix"
            elif not event.get("cache", {}).get("loaded"):
                event["status"] = (
                    "unparseable_cache" if event.get("cache", {}).get("sha256") else "missing_cache"
                )
            elif title_only:
                event["status"] = "title_match" if result.is_valid else "title_mismatch_or_missing"
            elif not event["cache"]["has_content"]:
                event["status"] = "no_content"
            elif not event["substring_parts_compared"]:
                event["status"] = "empty_query"
            else:
                event["status"] = "matched" if result.match_result.found else "mismatched"
                event["title_mismatch"] = result.match_result.found and not result.is_valid
            return result

        def validate(validator, supporting_text, reference_id, expected_title=None, path=None):
            self.event["validator_calls"] += 1
            self.event["validated_reference"] = reference_id
            self.event["normalized_validated_reference"] = self.normalize_reference(reference_id)
            self.event["validated_text_sha256"] = digest(str(supporting_text).encode())
            self.event["validated_path"] = path
            return finish(
                validator,
                native_validate(
                    validator,
                    supporting_text,
                    reference_id,
                    expected_title=expected_title,
                    path=path,
                ),
            )

        def validate_title(validator, reference_id, expected_title, path=None):
            self.event["validator_calls"] += 1
            self.event["validated_reference"] = reference_id
            return finish(
                validator,
                native_validate_title(
                    validator, reference_id, expected_title=expected_title, path=path
                ),
                True,
            )

        def match(validator, *args, **kwargs):
            self.event["matcher_calls"] += 1
            return native_match(validator, *args, **kwargs)

        def substring(validator, parts, *args, **kwargs):
            event = self.event
            event["substring_calls"] += 1

            class CountedParts(list):
                def __iter__(self):
                    for part in super().__iter__():
                        event["substring_parts_compared"] += 1
                        yield part

            return native_substring(validator, CountedParts(parts), *args, **kwargs)

        with ExitStack() as stack:
            for owner, name, replacement in (
                (Validator, "validate", record),
                (ReferenceValidationPlugin, "_validate_instance", visit),
                (ReferenceValidationPlugin, "_validate_excerpt", excerpt),
                (ReferenceValidationPlugin, "_validate_title", title),
                (SupportingTextValidator, "validate", validate),
                (SupportingTextValidator, "validate_title", validate_title),
                (SupportingTextValidator, "find_text_in_reference", match),
                (SupportingTextValidator, "_substring_match", substring),
                (ReferenceFetcher, "fetch", fetch),
                (ReferenceFetcher, "get_cache_path", cache_path),
            ):
                stack.enter_context(patch.object(owner, name, replacement))
            stack.enter_context(no_side_effects(self.violations))
            yield

    @staticmethod
    def new_event(path, reference, text):
        return {
            "path": path,
            "reference": reference,
            "text_sha256": digest(str(text).encode()),
            "validator_calls": 0,
            "matcher_calls": 0,
            "substring_calls": 0,
            "substring_parts_compared": 0,
        }


def reconcile(trace, native_exit):
    """Accounting failures invalidate a run; uncovered surfaces remain uncovered."""
    errors = list(trace.violations)
    rows = []
    for native in trace.rows:
        document = dict(trace.documents)[native["record"]]
        events = native["excerpts"]
        by_path = {event["path"]: event for event in events}
        if len(by_path) != len(events):
            errors.append(f"Duplicate excerpt invocation: {native['record']}")
        assertions = []
        for path, value, parent, field, instance in snippet_surfaces(document):
            item = {"path": path, "text_sha256": digest(str(value).encode())}
            expected_reference = raw_reference(instance)
            item["expected_reference"] = expected_reference
            item["normalized_expected_reference"] = (
                trace.normalize_reference(expected_reference)
                if expected_reference and trace.normalize_reference
                else None
            )
            visit = native["visits"].get(parent)
            if path in by_path:
                item.update(by_path.pop(path))
                if (
                    item["text_sha256"] != digest(str(value).encode())
                    or item.get("validated_text_sha256") != digest(str(value).encode())
                    or item.get("validated_path") != path
                ):
                    errors.append(f"Changed dispatched excerpt: {native['record']}:{path}")
                item["reference_binding_consistent"] = bool(
                    item["normalized_expected_reference"]
                    and item["normalized_expected_reference"]
                    == item.get("normalized_reference")
                    == item.get("normalized_validated_reference")
                )
                if not item["reference_binding_consistent"]:
                    errors.append(f"Reference identity mismatch: {native['record']}:{path}")
            elif not isinstance(value, str):
                item["status"] = "invalid_excerpt_type"
            elif not value.strip():
                item["status"] = "empty_excerpt"
            elif visit is None:
                item["status"] = "not_visited_by_native_schema"
            elif field not in visit["excerpt_fields"]:
                item["status"] = "unannotated_excerpt"
            else:
                item["status"] = "no_extractable_reference"
            item["native_class"] = visit["class"] if visit else None
            item["actually_compared"] = item.get("substring_parts_compared", 0) > 0 and item.get(
                "reference_binding_consistent", False
            )
            assertions.append(item)
        if by_path:
            errors.append(f"Native excerpt absent from independent inventory: {native['record']}")
        for event in [*events, *native["titles"]]:
            if event["validator_calls"] != 1 or "status" not in event:
                errors.append(
                    f"Incomplete validator invocation: {native['record']}:{event['path']}"
                )
            if event["matcher_calls"] > 1 or event["substring_calls"] > event["matcher_calls"]:
                errors.append(
                    f"Inconsistent matcher accounting: {native['record']}:{event['path']}"
                )
        expected_issues = sum(
            not event.get("is_valid", False) for event in [*events, *native["titles"]]
        )
        if len(native.get("issues", [])) != expected_issues:
            errors.append(f"Native issue/validator-result mismatch: {native['record']}")
        rows.append(
            {
                "record": native["record"],
                "completed": native["completed"],
                "assertions": assertions,
                "title_only": native["titles"],
                "native_issue_count": len(native.get("issues", [])),
                "record_kind": "has_snippet_surfaces" if assertions else "no_snippet_surfaces",
            }
        )
    processed = [row["record"] for row in rows if row["completed"]]
    expected = [name for name, _ in trace.documents]
    if processed != expected:
        errors.append("Record dispatch/completion does not reconcile with selected inventory")
    assertions = [item for row in rows for item in row["assertions"]]
    comparisons = sum(item["actually_compared"] for item in assertions)
    if comparisons == 0:
        errors.append("Zero snippet occurrences actually compared")
    issues = sum(row["native_issue_count"] for row in rows)
    if native_exit != (1 if issues else 0):
        errors.append("Native CLI exit disagrees with retained validation issues")
    counts = {
        "records_selected": len(expected),
        "records_completed": len(processed),
        "snippet_surfaces": len(assertions),
        "snippet_occurrences_compared": comparisons,
        "excerpt_validator_invocations": sum(len(r["excerpts"]) for r in trace.rows),
        "matcher_calls": sum(i.get("matcher_calls", 0) for i in assertions),
        "substring_calls": sum(i.get("substring_calls", 0) for i in assertions),
        "substring_parts_compared": sum(i.get("substring_parts_compared", 0) for i in assertions),
        "title_only_invocations": sum(len(row["title_only"]) for row in rows),
        "native_issues": issues,
    }
    coverage_complete = bool(assertions) and comparisons == len(assertions)
    return {
        "measurement_valid": not errors,
        "errors": errors,
        "counts": counts,
        "record_processing_complete": processed == expected,
        "assertion_coverage_complete": coverage_complete,
        "native_validation_passed": native_exit == 0,
        "validation_passed": not errors and coverage_complete and native_exit == 0,
        "native_exit_code": native_exit,
        "assertion_status_counts": dict(sorted(Counter(i["status"] for i in assertions).items())),
        "records": rows,
    }


def measure(root, documents, paths):
    """One real native CLI dispatch, shared by focused canary and corpus modes."""
    trace = Trace(root, documents)
    argv = [
        "data",
        *map(str, paths),
        "--schema",
        str(root / SCHEMA),
        "--config",
        str(root / CONFIG),
        "--cache-dir",
        str(root / "references_cache"),
        "--no-full-text",
    ]
    with trace.instrument():
        result = CliRunner().invoke(validate_app, argv)
    receipt = reconcile(trace, result.exit_code)
    receipt["invocation"] = {"dispatcher": "native Typer validate_app", "argv": argv}
    if result.exception and not isinstance(result.exception, SystemExit):
        receipt["errors"].append(
            f"Native exception: {type(result.exception).__name__}: {result.exception}"
        )
        receipt["measurement_valid"] = receipt["validation_passed"] = False
    return receipt, result.output


def write_json(path, value):
    with path.open("x") as handle:
        json.dump(value, handle, indent=2)
        handle.write("\n")


def run(root, output, selected, canary=False):
    if version("linkml-reference-validator") != SUPPORTED_VERSION:
        raise ValueError("Instrumentation requires reviewed linkml-reference-validator 0.2.1")
    revision, inventory = declared_records(root)
    selected = selected or inventory
    if len(set(selected)) != len(selected) or any(p not in inventory for p in selected):
        raise ValueError("Selected records must be unique members of the exact Git inventory")
    if canary and selected != [ASGARD]:
        raise ValueError("The literal-bracket canary requires exactly the complete Asgard record")
    output = output.resolve()
    temp_root = (root / ".temp").resolve()
    if not output.is_relative_to(temp_root) or output == temp_root:
        raise ValueError("Output must be a new directory beneath this checkout's .temp")
    before = input_manifest(root, inventory)
    output.mkdir(parents=True, exist_ok=False)
    receipt = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "revision": revision,
        "dependencies": {p: version(p) for p in ("linkml", "linkml-reference-validator")},
        "script_sha256": digest(Path(__file__).read_bytes()),
        "native_source_sha256": {
            name: digest(Path(inspect.getfile(obj)).read_bytes())
            for name, obj in {
                "reference_fetcher": ReferenceFetcher,
                "reference_validation_plugin": ReferenceValidationPlugin,
                "supporting_text_validator": SupportingTextValidator,
                "linkml_validator": Validator,
            }.items()
        },
        "declared_records": inventory,
        "selected_records": selected,
        "scope": "Native top-level community/isolate reference recipe; kb/taxa is excluded",
        "policy": "Native cache parsing/matching; no acquisition, enrichment, saving or supplement fallback",
        "interpretation": "Snippet occurrences and substring comparisons are not scientific assertion truth",
        "input_sha256": before,
        "cases": [],
    }
    write_json(output / "started.json", receipt)
    documents = [(name, yaml.safe_load((root / name).read_text())) for name in selected]
    if any(not isinstance(document, dict) for _, document in documents):
        raise ValueError("Declared records must be YAML mappings")
    cases = ["control", "mutation", "restoration"] if canary else ["measurement"]
    for case in cases:
        case_documents = deepcopy(documents)
        paths = [root / name for name in selected]
        if canary:
            document = case_documents[0][1]
            original = document["related_ingredients"][2]["evidence"][0]["snippet"]
            if original.count("[NiFe]") != 1:
                raise ValueError("Canary target no longer contains exactly one [NiFe]")
            if case == "mutation":
                document["related_ingredients"][2]["evidence"][0]["snippet"] = original.replace(
                    "[NiFe]", "[FeFe]"
                )
            # JSON is valid YAML: scratch input only; never round-trip a canonical record.
            paths = [output / f"{case}-input.json"]
            write_json(paths[0], document)
        result, log = measure(root, case_documents, paths)
        result["case"] = case
        result["input_sha256"] = {str(p.relative_to(root)): digest(p.read_bytes()) for p in paths}
        with (output / f"{case}.log").open("x") as handle:
            handle.write(log)
        write_json(output / f"{case}.json", result)
        receipt["cases"].append(result)
    after = input_manifest(root, inventory)
    receipt["inputs_unchanged"] = before == after
    receipt["changed_input_paths"] = sorted(
        p for p in before.keys() | after.keys() if before.get(p) != after.get(p)
    )
    valid = receipt["inputs_unchanged"] and all(r["measurement_valid"] for r in receipt["cases"])
    if canary:
        control, mutated, restored = receipt["cases"]

        def target(result):
            return next(i for i in result["records"][0]["assertions"] if i["path"] == CANARY_PATH)

        receipt["canary_passed"] = bool(
            valid
            and control["validation_passed"]
            and restored["validation_passed"]
            and control["counts"] == restored["counts"]
            and target(control)["status"] == target(restored)["status"] == "matched"
            and target(mutated)["status"] == "mismatched"
            and mutated["native_exit_code"] == 1
            and mutated["counts"]["native_issues"] == 1
            and mutated["counts"]["snippet_occurrences_compared"]
            == control["counts"]["snippet_occurrences_compared"]
        )
        code = 0 if receipt["canary_passed"] else 2
    else:
        code = 2 if not valid else (0 if receipt["cases"][0]["validation_passed"] else 1)
    receipt["exit_code"] = code
    receipt["finished_at"] = datetime.now(timezone.utc).isoformat()
    write_json(output / "receipt.json", receipt)
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="append", help="Exact repo-relative native record path")
    parser.add_argument("--output", type=Path, help="New exclusive directory beneath .temp")
    parser.add_argument(
        "--canary", action="store_true", help="Whole Asgard positive/mutated/restored CLI cases"
    )
    parser.add_argument(
        "--plan", action="store_true", help="Print Git-bound selection without validation"
    )
    args = parser.parse_args()
    try:
        if args.plan:
            revision, records = declared_records()
            if args.record and any(p not in records for p in args.record):
                raise ValueError("Unknown selected record")
            print(
                json.dumps(
                    {
                        "revision": revision,
                        "declared": len(records),
                        "selected": args.record or records,
                    },
                    indent=2,
                )
            )
            return 0
        if args.output is None:
            parser.error("--output is required unless --plan is used")
        result = run(REPO_ROOT, args.output, args.record, args.canary)
        print(
            json.dumps(
                {
                    "receipt": str(args.output / "receipt.json"),
                    "exit_code": result["exit_code"],
                    "cases": [{"case": c["case"], **c["counts"]} for c in result["cases"]],
                },
                indent=2,
            )
        )
        return result["exit_code"]
    except (OSError, ValueError) as error:
        print(f"Coverage refused: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
