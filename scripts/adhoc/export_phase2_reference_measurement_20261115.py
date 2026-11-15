"""Verify/publicize native assertion measurements for Phase2/#476, 2026-11-15.

Inputs: one completed maintained measurement directory and its source checkout.
Output: metadata-only JSON/Markdown on stdout; caller chooses an exclusive file.
No network, matching rerun, cache access through fetch(), or filesystem writes.
Host/Python declarations are explicitly separate from facts in the native receipt.
"""

import argparse
import hashlib
import inspect
import json
import re
import subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_runtime.utils.schemaview import SchemaView
from ruamel.yaml import YAML

ROOTS = {"kb/communities", "data/isolates"}
SCRIPT = "scripts/reference_assertion_coverage.py"
CONFIG = "conf/reference_validator.yaml"
SCHEMA = "src/communitymech/schema/communitymech.yaml"
OMISSIONS = {
    "invalid_excerpt_type",
    "empty_excerpt",
    "not_visited_by_native_schema",
    "unannotated_excerpt",
    "no_extractable_reference",
}
EVENT_STATUSES = {
    "matched",
    "mismatched",
    "skipped_prefix",
    "unparseable_cache",
    "missing_cache",
    "no_content",
    "empty_query",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def path_in(root, name):
    path = root / name
    require(
        not Path(name).is_absolute() and ".." not in Path(name).parts and not path.is_symlink(),
        "Unsafe input path",
    )
    require(path.resolve().is_relative_to(root), "Input path escapes source checkout")
    return path


def integer(value):
    require(type(value) is int and value >= 0, "Invalid nonnegative counter")
    return value


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def surfaces(value, path=""):
    if isinstance(value, dict):
        for key, child in value.items():
            here = f"{path}.{key}" if path else key
            if key in {"snippet", "supporting_text"}:
                reference = None
                for key_name in ("reference", "reference_id"):
                    candidate = value.get(key_name)
                    if isinstance(candidate, dict):
                        candidate = candidate.get("id") or candidate.get("reference_id")
                    if isinstance(candidate, str) and candidate:
                        reference = candidate
                        break
                yield here, child, reference
            yield from surfaces(child, here)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from surfaces(child, f"{path}[{index}]")


def verify_cache_identity(root, manifest, cache):
    """#2829: resolve only native case aliases proved to be one physical file."""
    requested = cache["requested_path"]
    require(requested.startswith("references_cache/"), "Loaded path is outside the cache")
    actual = requested
    if requested not in manifest:
        candidates = [name for name in manifest if name.casefold() == requested.casefold()]
        require(len(candidates) == 1, "Cache spelling alias is absent or ambiguous")
        actual = candidates[0]
        requested_path, actual_path = path_in(root, requested), path_in(root, actual)
        require(
            requested_path.is_file() and requested_path.samefile(actual_path),
            "Cache spelling alias is not the same physical file",
        )
        require(
            sha(actual_path.read_bytes()) == manifest[actual],
            "Current aliased cache differs from the verified input",
        )
    require(manifest.get(actual) == cache["sha256"], "Loaded cache does not match retained input")


def verify_event(item, manifest, normalizer, skip_prefixes, root, title=False):
    require(integer(item["validator_calls"]) == 1, "Incomplete validator invocation")
    matcher = integer(item["matcher_calls"])
    substring = integer(item["substring_calls"])
    parts = integer(item["substring_parts_compared"])
    require(
        matcher <= 1 and substring <= matcher and (not parts or substring == 1),
        "Inconsistent matching counters",
    )
    require(type(item["is_valid"]) is bool, "Invalid native validation outcome")
    cache = item.get("cache", {})
    if cache.get("sha256"):
        verify_cache_identity(root, manifest, cache)
    prefix = item["validated_reference"].split(":")[0].upper()
    if prefix in skip_prefixes:
        expected = "skipped_prefix"
    elif not cache.get("loaded"):
        expected = "unparseable_cache" if cache.get("sha256") else "missing_cache"
    elif title:
        expected = "title_match" if item["is_valid"] else "title_mismatch_or_missing"
    elif not cache.get("has_content"):
        expected = "no_content"
    elif not parts:
        expected = "empty_query"
    else:
        expected = "matched" if item["is_valid"] or item.get("title_mismatch") else "mismatched"
    require(item["status"] == expected, "Status contradicts actual comparison/access outcome")
    if expected in {"skipped_prefix", "missing_cache", "unparseable_cache", "no_content"}:
        require(parts == 0, "Uncompared status includes substring comparison")
    if not title:
        expected_reference = item["expected_reference"]
        normalized = normalizer(expected_reference) if expected_reference else None
        require(
            normalized
            and normalized
            == item["normalized_expected_reference"]
            == item["normalized_reference"]
            == item["normalized_validated_reference"],
            "Reference routing is inconsistent",
        )
        require(
            normalizer(item["reference"]) == normalized == normalizer(item["validated_reference"]),
            "Raw reference dispatch differs",
        )
        require(item["reference_binding_consistent"] is True, "Reference binding did not pass")
        require(
            item["path"] == item["validated_path"]
            and item["text_sha256"] == item["validated_text_sha256"],
            "Dispatched path/text changed",
        )
    return bool(parts)


def class_at(view, root_class, assertion_path):
    """Bind native-class counts to the actual schema path, including imports."""
    parent = assertion_path.rsplit(".", 1)[0] if "." in assertion_path else ""
    current = root_class
    for field in parent.split(".") if parent else []:
        field = re.sub(r"\[\d+\]", "", field)
        slots = {slot.name: slot for slot in view.class_induced_slots(current)}
        if field not in slots or slots[field].range not in view.all_classes():
            return None
        current = slots[field].range
    return current


def checked_summary(
    source_root, run_directory, execution_host, python_version=None, exit_file=None
):
    root = source_root.resolve(strict=True)
    run = run_directory.resolve(strict=True)
    require(
        run.is_relative_to(root / ".temp"), "Run directory must belong to the source checkout .temp"
    )
    artifacts = {}

    def read(name):
        path = path_in(run, name)
        raw = path.read_bytes()
        require(bool(raw), "Required artifact is empty")
        artifacts[name] = sha(raw)
        return raw

    receipt = json.loads(read("receipt.json"))
    started = json.loads(read("started.json"))
    require(
        receipt.get("inputs_unchanged") is True and receipt.get("changed_input_paths") == [],
        "Native inputs changed during measurement",
    )
    require(
        len(receipt.get("cases", [])) == 1 and receipt["cases"][0].get("case") == "measurement",
        "Only final measurement runs are supported; native canary attempts remain separate",
    )
    base = {
        key: value
        for key, value in receipt.items()
        if key not in {"finished_at", "exit_code", "inputs_unchanged", "changed_input_paths"}
    }
    base["cases"] = []
    require(base == started, "Started and finalized metadata differ")
    begin, end = (datetime.fromisoformat(receipt[key]) for key in ("started_at", "finished_at"))
    require(
        begin.tzinfo is not None and end.tzinfo is not None and end >= begin,
        "Invalid completion timestamps",
    )
    revision = receipt["revision"]
    require(re.fullmatch(r"[0-9a-f]{40}", revision), "Invalid revision")
    inventory = sorted(
        name
        for name in git(root, "ls-tree", "-r", "--name-only", revision).decode().splitlines()
        if Path(name).parent.as_posix() in ROOTS and name.endswith(".yaml")
    )
    require(
        inventory and inventory == receipt["declared_records"],
        "Declared inventory differs from exact Git tree",
    )
    selected = receipt["selected_records"]
    require(
        selected
        and len(selected) == len(set(selected))
        and all(name in inventory for name in selected),
        "Invalid selected inventory",
    )
    producer = git(root, "show", f"{revision}:{SCRIPT}")
    require(
        sha(producer) == receipt["script_sha256"] == sha(path_in(root, SCRIPT).read_bytes()),
        "Measured producer source differs",
    )
    manifest = receipt["input_sha256"]
    require(
        set(inventory + [CONFIG, "uv.lock", "pyproject.toml", SCHEMA]) <= manifest.keys(),
        "Input manifest omits required sources",
    )
    retained_files = {
        name
        for name in manifest
        if name.startswith(("references_cache/", "src/communitymech/schema/"))
    }
    current_files = {
        str(path.relative_to(root))
        for directory in (root / "references_cache", root / "src/communitymech/schema")
        for path in directory.rglob("*")
        if path.is_file()
    }
    require(retained_files == current_files, "Current schema/cache inventory differs")
    required = retained_files | set(selected) | {CONFIG, "uv.lock", "pyproject.toml"}
    for name in required:
        require(
            sha(path_in(root, name).read_bytes()) == manifest[name],
            "Current selected/schema/config/cache input differs",
        )
    for name in selected:
        require(
            sha(git(root, "show", f"{revision}:{name}")) == manifest[name],
            "Selected input differs from recorded Git revision",
        )
    require(
        sha(Path(inspect.getfile(ReferenceFetcher)).read_bytes())
        == receipt["native_source_sha256"]["reference_fetcher"],
        "Native reference normalization source differs",
    )
    config = YAML(typ="safe").load(path_in(root, CONFIG).read_text()) or {}
    view = SchemaView(str(root / SCHEMA))
    roots = [name for name, definition in view.all_classes().items() if definition.tree_root]
    require(len(roots) == 1, "Ambiguous native root class")
    # __new__ avoids acquisition-client construction; only pure native identifier
    # normalization is used. No fetch/cache parser/matcher is invoked here.
    normalizer = ReferenceFetcher.__new__(ReferenceFetcher)
    normalizer.config = SimpleNamespace(reference_prefix_map=config.get("reference_prefix_map", {}))
    skip_prefixes = {prefix.upper() for prefix in config.get("skip_prefixes", [])}
    case = json.loads(read("measurement.json"))
    require(case == receipt["cases"][0], "Case differs from aggregate receipt")
    require(
        case.get("measurement_valid") is True and case.get("errors") == [],
        "Native measurement was incomplete or inconsistent",
    )
    require(
        case["input_sha256"] == {name: manifest[name] for name in selected},
        "Case inputs differ from selected inputs",
    )
    argv = case["invocation"]["argv"]
    # Mirror directories may be on a different host: compare source-relative
    # suffixes and require every recorded absolute argument share one prefix.
    require(
        case["invocation"]["dispatcher"] == "native Typer validate_app"
        and len(argv) == len(selected) + 8
        and argv[0] == "data",
        "Unexpected native CLI dispatch",
    )
    prefix = str(argv[1])[: -len(selected[0])]
    require(prefix.startswith("/") and prefix.endswith("/"), "Native source root is not absolute")
    expected_argv = [
        "data",
        *[prefix + name for name in selected],
        "--schema",
        prefix + SCHEMA,
        "--config",
        prefix + CONFIG,
        "--cache-dir",
        prefix + "references_cache",
        "--no-full-text",
    ]
    require(argv == expected_argv, "Native command scope/options differ")
    rows = case["records"]
    require(
        [row["record"] for row in rows] == selected
        and all(row["completed"] is True for row in rows),
        "Selected records were not processed completely",
    )
    assertions, events, titles, public_rows = [], [], [], []
    for row in rows:
        document = YAML(typ="safe").load(path_in(root, row["record"]).read_text())
        raw = list(surfaces(document))
        items = row["assertions"]
        require(
            [item["path"] for item in items] == [path for path, _, _ in raw],
            "Occurrence inventory differs from record",
        )
        for item, (path, text, reference) in zip(items, raw, strict=True):
            require(
                item["text_sha256"] == sha(str(text).encode())
                and item["expected_reference"] == reference,
                "Raw occurrence/reference identity differs",
            )
            require(
                item["native_class"] == class_at(view, roots[0], path),
                "Native class differs from schema path",
            )
            if "validator_calls" in item:
                compared = verify_event(
                    item, manifest, normalizer.normalize_reference_id, skip_prefixes, root
                )
                events.append(item)
            else:
                require(
                    item["status"] in OMISSIONS
                    and all(
                        item.get(key, 0) == 0
                        for key in ("matcher_calls", "substring_calls", "substring_parts_compared")
                    ),
                    "Invalid unexamined occurrence",
                )
                compared = False
            require(
                type(item["actually_compared"]) is bool and item["actually_compared"] == compared,
                "Compared-occurrence flag differs from actual calls",
            )
        for item in row["title_only"]:
            verify_event(
                item, manifest, normalizer.normalize_reference_id, skip_prefixes, root, title=True
            )
        row_events = [item for item in items if "validator_calls" in item] + row["title_only"]
        require(
            integer(row["native_issue_count"])
            == sum(not event["is_valid"] for event in row_events),
            "Per-record issue count differs from native outcomes",
        )
        require(
            row["record_kind"] == ("has_snippet_surfaces" if items else "no_snippet_surfaces"),
            "Zero-assertion record type differs",
        )
        assertions.extend(items)
        titles.extend(row["title_only"])
        classes = {}
        for name in sorted(
            {item.get("native_class") or "outside_native_traversal" for item in items}
        ):
            group = [
                item
                for item in items
                if (item.get("native_class") or "outside_native_traversal") == name
            ]
            classes[name] = {
                "surfaces": len(group),
                "compared": sum(item["actually_compared"] for item in group),
                "status_counts": dict(sorted(Counter(item["status"] for item in group).items())),
            }
        public_rows.append(
            {
                "record": row["record"],
                "completed": True,
                "record_kind": row["record_kind"],
                "surfaces": len(items),
                "compared": sum(item["actually_compared"] for item in items),
                "native_issues": row["native_issue_count"],
                "status_counts": dict(sorted(Counter(item["status"] for item in items).items())),
                "native_classes": classes,
            }
        )
    counts = {
        "records_selected": len(selected),
        "records_completed": len(rows),
        "snippet_surfaces": len(assertions),
        "snippet_occurrences_compared": sum(item["actually_compared"] for item in assertions),
        "excerpt_validator_invocations": len(events),
        "matcher_calls": sum(integer(item.get("matcher_calls", 0)) for item in assertions),
        "substring_calls": sum(integer(item.get("substring_calls", 0)) for item in assertions),
        "substring_parts_compared": sum(
            integer(item.get("substring_parts_compared", 0)) for item in assertions
        ),
        "title_only_invocations": len(titles),
        "native_issues": sum(row["native_issue_count"] for row in rows),
    }
    require(counts["snippet_occurrences_compared"] > 0, "Zero actual snippet comparisons")
    statuses = dict(sorted(Counter(item["status"] for item in assertions).items()))
    require(
        counts == case["counts"] and statuses == case["assertion_status_counts"],
        "Aggregate counters do not reconcile",
    )
    coverage = counts["snippet_occurrences_compared"] == len(assertions)
    native_exit = 1 if counts["native_issues"] else 0
    passed = coverage and native_exit == 0
    require(
        case["record_processing_complete"] is True
        and case["assertion_coverage_complete"] == coverage
        and case["native_validation_passed"] == (native_exit == 0)
        and case["validation_passed"] == passed
        and type(case["native_exit_code"]) is int
        and case["native_exit_code"] == native_exit,
        "Coverage/validation/exit flags contradict outcomes",
    )
    require(
        type(receipt["exit_code"]) is int and receipt["exit_code"] == (0 if passed else 1),
        "Wrapper exit contradicts measurement",
    )
    log = read("measurement.log").decode()
    require(
        re.findall(r"^  Total checks: (\d+)$", log, re.MULTILINE) == [str(counts["native_issues"])],
        "Native logged issue counter differs",
    )
    require(
        re.findall(r"^  Files validated: (\d+)$", log, re.MULTILINE) == [str(len(rows))],
        "Native logged file count differs",
    )
    if exit_file:
        exit_raw = exit_file.read_bytes()
        require(
            exit_raw.strip() == str(receipt["exit_code"]).encode(), "Retained process exit differs"
        )
        artifacts["process.exit"] = sha(exit_raw)
    require(execution_host in {"local", "M5"}, "Unsupported execution host declaration")
    require(
        python_version is None or re.fullmatch(r"3\.\d+\.\d+", python_version),
        "Invalid Python declaration",
    )
    return {
        "attempt": run.name,
        "measurement_revision": revision,
        "verification_revision": git(root, "rev-parse", "HEAD").decode().strip(),
        "execution_declaration": {
            "host": execution_host,
            "python_version": python_version,
            "authority": "Caller declaration; native receipt records package/source hashes but not execution host or Python runtime",
        },
        "started_at": receipt["started_at"],
        "finished_at": receipt["finished_at"],
        "dependencies": receipt["dependencies"],
        "producer_sha256": receipt["script_sha256"],
        "native_source_sha256": receipt["native_source_sha256"],
        "declared_records": len(inventory),
        "selected_records": len(selected),
        "current_input_scope": "Selected records and all schema/config/lock/cache files; unselected historical records may have changed",
        "current_input_files_verified": len(required),
        "record_processing_complete": True,
        "full_inventory_processed": selected == inventory,
        "assertion_coverage_complete": coverage,
        "native_validation_passed": native_exit == 0,
        "validation_passed": passed,
        "native_exit_code": native_exit,
        "wrapper_exit_code": receipt["exit_code"],
        "process_exit_independently_retained": exit_file is not None,
        "counts": counts,
        "status_counts": statuses,
        "records": public_rows,
        "raw_artifact_sha256": artifacts,
        "limit": "Measured lexical comparisons are not scientific support; retained issue counts are not examined assertion counts. No source/quote/reference values are published.",
    }


def markdown(report):
    lines = [
        "# Measured native reference assertions",
        "",
        f"Attempt `{report['attempt']}`; measured revision `{report['measurement_revision']}`.",
        f"Execution host: {report['execution_declaration']['host']} (caller-declared); Python: {report['execution_declaration']['python_version'] or 'not recorded'}. Native dependency/source hashes are retained in JSON.",
        "",
        "| Record | Surfaces | Compared | SupportingReference compared | Native issues |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in report["records"]:
        name = row["record"].replace("|", "&#124;").replace("\n", " ")
        lines.append(
            f"| {name} | {row['surfaces']} | {row['compared']} | {row['native_classes'].get('SupportingReference', {}).get('compared', 0)} | {row['native_issues']} |"
        )
    lines.extend(
        [
            "",
            f"Records processed: {report['counts']['records_completed']}/{report['selected_records']} selected from {report['declared_records']} declared. Assertion coverage complete: {report['assertion_coverage_complete']}; native validation passed: {report['native_validation_passed']}. Native exit {report['native_exit_code']}; wrapper exit {report['wrapper_exit_code']}.",
            "",
            report["limit"],
        ]
    )
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--execution-host", choices=("local", "M5"), required=True)
    parser.add_argument("--python-version")
    parser.add_argument("--exit-file", type=Path)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args()
    try:
        report = checked_summary(
            args.source_root, args.run, args.execution_host, args.python_version, args.exit_file
        )
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        # Error messages deliberately omit raw values and private absolute paths.
        print(
            f"Measurement export refused: {type(error).__name__}: consistency or input verification failed",
            file=__import__("sys").stderr,
        )
        return 2
    print(
        json.dumps(report, indent=2) if args.format == "json" else markdown(report),
        end="\n" if args.format == "json" else "",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
