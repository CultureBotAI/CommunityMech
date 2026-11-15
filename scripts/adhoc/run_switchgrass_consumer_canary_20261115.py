"""Run one installed-runtime CommunityMech consumer canary for issue #1996.

Inputs: exact prepared private namespace, its pinned receipt, installed runtime.
Outputs: exclusive native log, actual comparison receipt and native exit file.
A profile observer records native returns; it does not replace any validator,
fetcher, traversal or matching method. Socket access is refused. 2026-11-15.
Reuses validator run_switchgrass_source_canary_20261115.py at SHA256
41f2a72e151753c27d776afdf3e1f307625146824fa5a8097c28bf4b9e117d7c.
Consumer differences: explicit reviewed source revision, complete Python member
identity, and unchanged consumer schemas captured by the preparation helper.
"""

import argparse
import inspect
import json
import platform
import re
import socket
import subprocess
import sys
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path

from linkml_reference_validator.cli.validate import data_command, validate_app
from linkml_reference_validator.validation.supporting_text_validator import SupportingTextValidator
from ruamel.yaml import YAML
from typer.testing import CliRunner

ROOT = Path(__file__).resolve().parents[2]
MODES = ("article-only", "selected", "wrong-parent", "wrong-cell")


def digest(raw):
    """Hash exact captured bytes."""
    return sha256(raw).hexdigest()


def encoded(value):
    """Serialize receipts with deterministic ordering."""
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def surfaces(value, path=""):
    """Independent snippet census; no schema traversal is reused."""
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else key
            if key in {"snippet", "supporting_text"}:
                yield child_path, child, value.get("reference")
            yield from surfaces(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from surfaces(child, f"{path}[{index}]")


def located_evidence(value, path=""):
    """Index explicit locators independently of the runtime's result identity."""
    if isinstance(value, dict):
        if "source_locator" in value and "snippet" in value:
            yield f"{path}.snippet", value
        for key, child in value.items():
            yield from located_evidence(child, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from located_evidence(child, f"{path}[{index}]")


def comparison_counts(events):
    """Count actual native match results separately from validation returns."""
    return {
        "native_validation_calls": len(events),
        "native_comparisons": sum(item["matched"] is not None for item in events),
        "native_matches": sum(item["matched"] is True for item in events),
        "native_mismatches": sum(item["matched"] is False for item in events),
        "source_selection_failures": sum(
            item["matched"] is None
            and not item["is_valid"]
            and item["message"].startswith("Source selection failed:")
            for item in events
        ),
    }


def capture_runtime_members(source_root, package, captured):
    """Capture exact source/installed Python membership and bytes, no writes."""
    source_package = source_root / "src/linkml_reference_validator"
    source_paths = set(source_package.rglob("*.py"))
    relative = {path.relative_to(source_package) for path in source_paths}
    if not relative or {path.relative_to(package) for path in package.rglob("*.py")} != relative:
        raise ValueError("Installed Python membership differs from reviewed source")
    for path in sorted(source_paths):
        installed = package / path.relative_to(source_package)
        for member in (path, installed):
            if member.is_symlink():
                raise ValueError("Runtime members must not be symlinks")
            if member not in captured:
                captured[member] = member.read_bytes()
        if captured[path] != captured[installed]:
            raise ValueError("Installed runtime bytes differ from reviewed source")
    return source_package, relative


def verify_runtime_membership(source_package, package, relative):
    """Reject added or removed Python members before publishing a result."""
    if {path.relative_to(source_package) for path in source_package.rglob("*.py")} != relative or {
        path.relative_to(package) for path in package.rglob("*.py")
    } != relative:
        raise ValueError("Runtime Python membership changed during validation")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--preparation-sha256", required=True)
    parser.add_argument("--mode", choices=MODES, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--validator-source-root", type=Path, required=True)
    parser.add_argument("--expected-validator-revision", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    validator_root = args.validator_source_root.resolve()
    if not re.fullmatch(r"[0-9a-f]{40}", args.expected_validator_revision):
        raise ValueError("An explicit full reviewed validator revision is required")

    def require_validator_revision():
        revision = subprocess.check_output(
            ["git", "-C", str(validator_root), "rev-parse", "HEAD"], text=True
        ).strip()
        status = subprocess.check_output(
            ["git", "-C", str(validator_root), "status", "--porcelain"], text=True
        ).strip()
        if revision != args.expected_validator_revision or status:
            raise ValueError("Reviewed validator checkout must be clean at the exact revision")

    require_validator_revision()
    output = args.output.resolve()
    prepared = args.prepared.resolve()
    if (
        output.exists()
        or not output.is_relative_to(ROOT / ".temp")
        or not prepared.is_relative_to(ROOT / ".temp")
    ):
        raise ValueError("New private output and prepared namespace required")
    receipt_path = prepared / "preparation.json"
    receipt_raw = receipt_path.read_bytes()
    if digest(receipt_raw) != args.preparation_sha256:
        raise ValueError("Preparation receipt differs")
    preparation = json.loads(receipt_raw)
    captured = {receipt_path: receipt_raw, Path(__file__): Path(__file__).read_bytes()}
    for name, expected in preparation["outputs"].items():
        path = prepared / name
        if path.is_symlink() or not path.resolve().is_relative_to(prepared):
            raise ValueError("Unsafe prepared path")
        raw = path.read_bytes()
        if digest(raw) != expected:
            raise ValueError(f"Prepared artifact differs: {name}")
        captured[path] = raw
    for name, expected in preparation["inputs"].items():
        path = Path(name)
        raw = captured[path] if path in captured else path.read_bytes()
        if path.is_symlink() or digest(raw) != expected:
            raise ValueError(f"Original source differs: {name}")
        captured[path] = raw
    import linkml_reference_validator

    package = Path(linkml_reference_validator.__file__).resolve().parent
    if not package.is_relative_to(Path(sys.prefix).resolve()) or package.is_relative_to(
        validator_root / "src"
    ):
        raise ValueError("Use an explicitly installed noneditable candidate environment")
    source_package, runtime_members = capture_runtime_members(validator_root, package, captured)
    if sys.getprofile() is not None:
        raise ValueError("An existing process profiler cannot be replaced")
    yaml = YAML(typ="safe")
    original = yaml.load(captured[prepared / "original.yaml"])
    selected = json.loads(captured[prepared / "selected.json"])
    record = deepcopy(original if args.mode == "article-only" else selected)
    discussion = next(
        item
        for item in record["discussions"]
        if item["discussion_id"] == "methods_final16_vs_supplement_table_s1"
    )
    if args.mode == "wrong-parent":
        discussion["evidence"][2]["reference"] = "PMID:12345"
    elif args.mode == "wrong-cell":
        # Bacillus occurs in the article; it must still fail this explicit wrong cell.
        discussion["evidence"][3]["source_locator"].update(row=12, cell=1)
    expected = {path: (text, reference) for path, text, reference in surfaces(record)}
    if len(expected) != 37 or len(list(surfaces(record))) != 37:
        raise ValueError("Unexpected independent snippet denominator")
    if args.plan:
        require_validator_revision()
        verify_runtime_membership(source_package, package, runtime_members)
        if any(path.read_bytes() != raw for path, raw in captured.items()):
            raise ValueError("Captured input changed during plan")
        print(
            json.dumps(
                {
                    "plan": True,
                    "mode": args.mode,
                    "installed_package": str(package),
                    "validator_revision": args.expected_validator_revision,
                    "runtime_python_members": len(runtime_members),
                    "independent_snippet_surfaces": len(expected),
                    "output": str(output),
                    "inputs": {str(path): digest(raw) for path, raw in captured.items()},
                },
                indent=2,
            )
        )
        return 0
    output.mkdir(parents=True, exist_ok=False)
    record_path = output / "record.json"
    record_raw = encoded(record)
    with record_path.open("xb") as handle:
        handle.write(record_raw)
    captured[record_path] = record_raw
    events = []
    violations = []
    native_code = SupportingTextValidator.validate.__code__

    def observe(frame, event, result):
        if event == "return" and frame.f_code is native_code:
            if result is None:
                violations.append("Native validator returned no result")
                return
            events.append(
                {
                    "path": frame.f_locals["path"],
                    "reference": frame.f_locals["reference_id"],
                    "text_sha256": digest(frame.f_locals["supporting_text"].encode()),
                    "is_valid": result.is_valid,
                    "severity": result.severity.value,
                    "matched": result.match_result.found if result.match_result else None,
                    "source_identity": deepcopy(result.source_identity),
                    "message": result.message,
                }
            )

    def no_network(*_args, **_kwargs):
        violations.append("Native CLI attempted network access")
        raise RuntimeError(violations[-1])

    socket_functions = [
        (socket, "create_connection"),
        (socket, "getaddrinfo"),
        (socket.socket, "connect"),
        (socket.socket, "connect_ex"),
        (socket.socket, "sendto"),
    ]
    originals = [(owner, name, getattr(owner, name)) for owner, name in socket_functions]
    argv = [
        "data",
        str(record_path),
        "--schema",
        str(prepared / "schema/communitymech.yaml"),
        "--target-class",
        "MicrobialCommunity",
        "--config",
        str(prepared / "config.json"),
        "--no-full-text",
    ]
    try:
        for owner, name, _ in originals:
            setattr(owner, name, no_network)
        sys.setprofile(observe)
        result = CliRunner().invoke(validate_app, argv)
    finally:
        sys.setprofile(None)
        for owner, name, function in originals:
            setattr(owner, name, function)
    errors = list(violations)
    if Counter(item["path"] for item in events) != Counter(expected.keys()):
        errors.append("Actual native comparison paths differ from the independent census")
    for item in events:
        text, reference = expected.get(item["path"], ("", None))
        if item["text_sha256"] != digest(text.encode()) or item["reference"] != reference:
            errors.append("Actual dispatched reference/snippet differs")
    changed = [
        str(path) for path, raw in captured.items() if path.is_symlink() or path.read_bytes() != raw
    ]
    require_validator_revision()
    verify_runtime_membership(source_package, package, runtime_members)
    if changed:
        errors.append("Captured input changed during native CLI validation")
    failed = {item["path"] for item in events if not item["is_valid"]}
    selected_paths = preparation["selected_paths"]
    wanted_failures = {
        "article-only": {selected_paths[0], selected_paths[2]},
        "selected": set(),
        "wrong-parent": {selected_paths[0]},
        "wrong-cell": {selected_paths[1]},
    }[args.mode]
    if failed != wanted_failures or result.exit_code != (1 if wanted_failures else 0):
        errors.append("Native exit or precise failure set differs from the declared control")
    established = [item for item in events if item["source_identity"] is not None]
    expected_established = (
        0 if args.mode == "article-only" else (2 if args.mode == "wrong-parent" else 3)
    )
    if len(established) != expected_established:
        errors.append("Source comparison identity count differs")
    catalog_raw = captured[prepared / "catalog.json"]
    catalog = json.loads(catalog_raw)
    if len(catalog["sources"]) != 1:
        raise ValueError("The canary requires its one exact asset entry")
    source = catalog["sources"][0]
    projection = json.loads(captured[prepared / source["extraction_path"]])
    locator_by_path = {path: owner["source_locator"] for path, owner in located_evidence(record)}
    for item in established:
        identity = item["source_identity"]
        locator = locator_by_path[item["path"]]
        selected_cell = projection["tables"][locator["table"] - 1][locator["row"] - 1][
            locator["cell"] - 1
        ]
        if selected_cell["status"] != "supported":
            raise ValueError("An established identity cannot select an unsupported cell")
        exact_identity = {
            "reference": source["reference"],
            "asset_id": source["asset_id"],
            "version": source["version"],
            "asset_sha256": source["asset_sha256"],
            "extraction_sha256": source["extraction_sha256"],
            "catalog_sha256": digest(catalog_raw),
            "extractor": projection["format"],
            "locator": locator,
            "selected_sha256": digest(selected_cell["text"].encode()),
        }
        if identity != exact_identity or item["path"] not in selected_paths:
            errors.append("Selected native source identity differs")
    counts = comparison_counts(events)
    expected_counts = {
        "article-only": (37, 37, 35, 2, 0),
        "selected": (37, 37, 37, 0, 0),
        "wrong-cell": (37, 37, 36, 1, 0),
        "wrong-parent": (37, 36, 36, 0, 1),
    }[args.mode]
    if tuple(counts.values()) != expected_counts:
        errors.append("Actual calls/comparisons/matches/mismatches/source failures differ")
    if args.mode == "wrong-parent":
        selection_errors = [item for item in events if item["matched"] is None]
        if any(
            item["is_valid"]
            or item["severity"] != "ERROR"
            or not item["message"].startswith("Source selection failed:")
            for item in selection_errors
        ):
            errors.append("Wrong parent did not produce a hard source-selection failure")
    report = {
        "mode": args.mode,
        "native_argv": argv,
        "native_exit_code": result.exit_code,
        "control_passed": not errors,
        "errors": errors,
        "changed_inputs": changed,
        "python": sys.version,
        "executable": sys.executable,
        "platform": platform.platform(),
        "dependencies": {
            name: version(name)
            for name in ("linkml-reference-validator", "linkml", "linkml-runtime")
        },
        "installed_package": str(package),
        "native_cli_source": inspect.getfile(data_command),
        "validator_revision": args.expected_validator_revision,
        "runtime_python_members": len(runtime_members),
        "reuse_helper_sha256": "41f2a72e151753c27d776afdf3e1f307625146824fa5a8097c28bf4b9e117d7c",
        "independent_snippet_surfaces": len(expected),
        **counts,
        "native_failures": len(failed),
        "established_source_identities": len(established),
        "comparisons": events,
        "inputs": {str(path): digest(raw) for path, raw in captured.items()},
        "network_attempts": violations,
        "log_sha256": digest(result.output.encode()),
        "limitations": "One scratch record; lexical routing only, not science or canonical adoption.",
    }
    for name, raw in (
        ("native.log", result.output.encode()),
        ("native.exit", f"{result.exit_code}\n".encode()),
        ("receipt.json", encoded(report)),
    ):
        with (output / name).open("xb") as handle:
            handle.write(raw)
        if (output / name).read_bytes() != raw:
            raise ValueError("Persisted result differs")
    print(
        json.dumps(
            {
                key: report[key]
                for key in (
                    "mode",
                    "native_exit_code",
                    "control_passed",
                    "errors",
                    "native_validation_calls",
                    "native_comparisons",
                    "native_matches",
                    "native_mismatches",
                    "source_selection_failures",
                )
            },
            indent=2,
        )
    )
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
