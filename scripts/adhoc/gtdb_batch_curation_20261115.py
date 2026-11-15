"""Stage/apply reviewed GTDB units with shared bounded guards, #2848, 2026-11-15.

Inputs: exact source-plan proof, per-record native correspondence, and externally
approved candidate/receipt hashes. Outputs: exclusive private native candidates
or one atomic canonical replacement plus actual receipt. A batch is at most ten
whole records, executed one unit at a time after a verified route canary.
"""

import argparse
import contextlib
import copy
import difflib
import importlib.util
import json
import os
import socket
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import yaml

from communitymech.validation.write_validated import write_validated_community

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp"
NATIVE = "scripts/gtdb_ground.py"
NATIVE_SHA = "0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
REQUIRED_INPUTS = (
    NATIVE,
    "src/communitymech/curate/curation_event.py",
    "src/communitymech/validators/ncbi_domain.py",
    "src/communitymech/ontology_adapters.py",
    "src/communitymech/schema/communitymech.yaml",
    "src/communitymech/schema/mech_shared.yaml",
    "src/communitymech/validation/write_validated.py",
    "uv.lock",
    "pyproject.toml",
    "justfile",
)


def sha(raw):
    import hashlib

    return hashlib.sha256(raw).hexdigest()


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def path(name, *, private=False):
    relative = Path(name)
    result = (ROOT / relative).resolve()
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or not result.is_relative_to(STATE if private else ROOT)
        or (ROOT / relative).is_symlink()
    ):
        raise ValueError("safe repository-relative path required")
    return result


def capture(captured, name, expected=None):
    location = path(name)
    if location not in captured:
        captured[location] = location.read_bytes()
    raw = captured[location]
    if expected is not None and sha(raw) != expected:
        raise ValueError("accepted input changed: " + name)
    return raw


def unchanged(captured, revision):
    if head() != revision or any(
        location.read_bytes() != raw for location, raw in captured.items()
    ):
        raise ValueError("captured source or revision changed")


def native_module():
    spec = importlib.util.spec_from_file_location("bounded_gtdb_native", ROOT / NATIVE)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    return native


def source_unit(proof, record_id):
    records = proof["records"]
    if not 1 <= len(records) <= 10 or len({row["record"] for row in records}) != len(records):
        raise ValueError("one to ten unique whole records required")
    selected = [row for row in records if row["record_id"] == record_id]
    if len(selected) != 1:
        raise ValueError("one exact whole-record unit required")
    row = selected[0]
    # Multi-record source adapters must declare each unit's complete input set;
    # this prevents an earlier unit's write from silently invalidating a later
    # target capture, and prevents dropping a real cross-record dependency.
    names = row.get("input_paths")
    if names is None:
        if len(records) != 1:
            raise ValueError("batch source proof requires explicit per-record input paths")
        names = list(proof["inputs"])
    if row["record"] not in names or len(names) != len(set(names)):
        raise ValueError("unique complete per-record source input list required")
    inputs = {name: proof["inputs"][name] for name in names}
    return row, inputs


def expected_science(before, row, native, mapping_source):
    if before["id"] != row["record_id"]:
        raise ValueError("target identity differs")
    expected = copy.deepcopy(before)
    seen = set()
    ground_count = status_count = 0
    for occurrence in row["occurrences"]:
        index = occurrence["taxonomy_index"]
        if not isinstance(index, int) or isinstance(index, bool) or index < 0 or index in seen:
            raise ValueError("unique explicit taxonomy occurrence required")
        seen.add(index)
        member = expected["taxonomy"][index]
        descriptor = member["taxon_term"]
        if (
            descriptor != occurrence["existing_descriptor"]
            or descriptor["term"] != occurrence["term"]
        ):
            raise ValueError("reviewed complete source descriptor differs")
        if member.get("strain_designation", {}).get("strain_name") != occurrence["strain_name"]:
            raise ValueError("reviewed stock identity differs")
        result = occurrence["native_result"]
        prior = copy.deepcopy(descriptor)
        if result is None:
            require_unresolved(occurrence)
            descriptor["gtdb_grounding_status"] = "UNRESOLVED"
            descriptor.pop("gtdb_candidates", None)
        elif result.get("ambiguous"):
            if "gtdb_classification" in descriptor or not result.get("gtdb_options"):
                raise ValueError("ambiguous route cannot remove a block or omit options")
            descriptor["gtdb_grounding_status"] = "AMBIGUOUS"
            descriptor["gtdb_candidates"] = list(result["gtdb_options"])
        elif result.get("gtdb_id"):
            if "gtdb_classification" in descriptor:
                raise ValueError("add-only source plan cannot refresh a prior block")
            descriptor["gtdb_classification"] = native._block(result, mapping_source)
            descriptor["gtdb_grounding_status"] = "GROUNDED"
            descriptor.pop("gtdb_candidates", None)
            ground_count += 1
        else:
            raise ValueError("native grounded or complete ambiguous result required")
        status_count += any(
            prior.get(key) != descriptor.get(key)
            for key in ("gtdb_grounding_status", "gtdb_candidates")
        )
    if not seen or not (ground_count or status_count):
        raise ValueError("no substantive declared change")
    actions = []
    if ground_count:
        actions.append(
            (
                "GTDB_GROUND",
                f"Added {ground_count} gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395).",
            )
        )
    if status_count:
        actions.append(
            (
                "GTDB_SET_STATUS",
                f"Wrote gtdb_grounding_status on {status_count} taxonomy entries (#294, #395).",
            )
        )
    return expected, actions


def require_unresolved(occurrence):
    """Admit only an explicit native-null observation, never an inferred absence (#2888)."""
    descriptor = occurrence["existing_descriptor"]
    if (
        occurrence["native_result"] is not None
        or occurrence.get("classify_status") != {"status": "UNRESOLVED", "candidates": []}
        or not occurrence["term"]["id"].startswith("NCBITaxon:")
        or "gtdb_classification" in descriptor
        or descriptor.get("gtdb_grounding_status") in {"WITHHELD", "NO_GTDB_EQUIVALENT"}
        or "manual_curated_reason" not in occurrence
        or "manual_withheld_reason" not in occurrence
        or occurrence["manual_curated_reason"] is not None
        or occurrence["manual_withheld_reason"] is not None
    ):
        raise ValueError("explicit unheld native-null UNRESOLVED observation required")


def verify_operations(row, flags):
    """Null correspondence is status-only; it cannot authorize block replacement."""
    for occurrence in row["occurrences"]:
        result = occurrence["native_result"]
        if result is None:
            require_unresolved(occurrence)
            if flags != ["--apply-status"]:
                raise ValueError("native-null correction requires status-only operation")
        elif flags == ["--apply-status"] and not result.get("ambiguous"):
            raise ValueError("status-only correction requires complete ambiguity or native null")


def verify_fresh_unresolved(native, row, occurrence, rows):
    """Recompute the domain/hold-aware classifier in the same offline native context."""
    require_unresolved(occurrence)
    descriptor, term = occurrence["existing_descriptor"], occurrence["term"]
    status, candidates = native.classify_status(
        Path(row["record"]).name,
        term["id"],
        term["label"],
        "gtdb_classification" in descriptor,
        *rows,
        preferred=descriptor.get("preferred_term"),
    )
    if {"status": status, "candidates": candidates} != occurrence["classify_status"]:
        raise ValueError("fresh native null classification differs from accepted source")


def verify_candidate(original, candidate, row, native, mapping_source):
    before, after = yaml.safe_load(original), yaml.safe_load(candidate)
    expected, actions = expected_science(before, row, native, mapping_source)
    previous = before.get("curation_history", [])
    events = after.get("curation_history", [])[len(previous) :]
    if len(events) != len(actions):
        raise ValueError("exact substantive native events required")
    for event, (action, changes) in zip(events, actions, strict=True):
        if event != native.record_curation_event(
            expected,
            curator="gtdb_ground.py",
            action=action,
            changes=changes,
            timestamp=event.get("timestamp"),
        ):
            raise ValueError("appended event differs from native event")
    if after != expected:
        raise ValueError("candidate changes undeclared taxonomy or scientific content")
    return after, events


def prepare(proof_name, proof_sha, record_id, revision):
    if head() != revision:
        raise ValueError("exact current revision required")
    captured = {}
    proof_raw = capture(captured, proof_name, proof_sha)
    proof = json.loads(proof_raw)
    if proof.get("inputs_unchanged") is not True or proof.get("canonical_writes") is not False:
        raise ValueError("completed read-only source proof required")
    row, source_inputs = source_unit(proof, record_id)
    for name, digest in source_inputs.items():
        capture(captured, name, digest)
    for name in (*REQUIRED_INPUTS, str(Path(__file__).relative_to(ROOT))):
        capture(captured, name)
    capture(captured, NATIVE, NATIVE_SHA)
    original = capture(captured, row["record"], row["before_sha256"])
    if not row["record"].startswith(("data/isolates/", "kb/communities/")):
        raise ValueError("declared community-record root required")
    tables = [location for location in captured if location.name == "NCBI2GTDB.tsv.gz"]
    if len(tables) != 1 or sha(captured[tables[0]]) != TABLE_SHA:
        raise ValueError("exact reviewed crosswalk required")
    return proof, row, original, captured, tables[0]


def stage(proof_name, proof_sha, record_id, output_name, revision, operations, *, plan=False):
    output = path(output_name, private=True)
    if output.exists():
        raise ValueError("exclusive private stage output required")
    proof, row, original, captured, table = prepare(proof_name, proof_sha, record_id, revision)
    candidate = output / Path(row["record"]).name
    flags = {
        "ground-and-status": ("--apply", "--apply-status"),
        "status-only": ("--apply-status",),
    }[operations]
    verify_operations(row, list(flags))
    argv = [
        ["--community", str(candidate), "--kg-microbe-dir", str(table.parents[2]), flag]
        for flag in flags
    ]
    metadata = {
        "code_revision": revision,
        "target": row["record"],
        "target_id": record_id,
        "source_proof": {"path": proof_name, "sha256": proof_sha},
        "before_sha256": sha(original),
        "inputs": {str(location.relative_to(ROOT)): sha(raw) for location, raw in captured.items()},
        "canonical_apply": False,
        "native_operations": list(flags),
        "scope": "Only declared native GTDB blocks/status/options and substantive native inline events; preserve all other claims, stock identities, source quotes and old history.",
    }
    if plan:
        unchanged(captured, revision)
        return {**metadata, "native_argv": argv, "planned": True}
    output.mkdir(parents=True)
    candidate.write_bytes(original)
    native = native_module()
    database = Path.home() / ".data/oaklib/ncbitaxon.db"
    before_stat = database.stat()

    def deny_network(*_args, **_kwargs):
        raise RuntimeError("source acquisition prohibited")

    with (output / "native.log").open("x") as log:
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            with patch.dict(os.environ, {"PYSTOW_HOME": str(database.parents[1])}):
                with patch.object(socket.socket, "connect", deny_network):
                    from communitymech import ontology_adapters

                    local = ontology_adapters._local_build("ncbitaxon")
                    if local is None:
                        raise ValueError("existing local NCBI adapter required")
                    with patch.object(ontology_adapters, "_local_build", return_value=local):
                        identifiers = {
                            item["term"]["id"].split(":", 1)[1] for item in row["occurrences"]
                        }
                        names = {
                            key
                            for item in row["occurrences"]
                            for key in native.lookup_keys(item["term"]["label"])
                        }
                        rows = native.collect_rows(table, identifiers, names, names)
                        for occurrence in row["occurrences"]:
                            term = occurrence["term"]
                            if (
                                native.resolve_target(
                                    term["id"].split(":", 1)[1], term["label"], *rows
                                )
                                != occurrence["native_result"]
                            ):
                                raise ValueError("fresh native route differs from accepted source")
                            if occurrence["native_result"] is None:
                                verify_fresh_unresolved(native, row, occurrence, rows)
                        mapping_source = native.describe_mapping(table)
                        codes = [native.main(command) for command in argv]
    (output / "native.exit").write_text(json.dumps(codes) + "\n")
    if codes != [0] * len(flags):
        raise ValueError("native private staging failed")
    candidate_raw = candidate.read_bytes()
    _, events = verify_candidate(original, candidate_raw, row, native, mapping_source)
    after_stat = database.stat()
    if (before_stat.st_size, before_stat.st_mtime_ns) != (
        after_stat.st_size,
        after_stat.st_mtime_ns,
    ):
        raise ValueError("local NCBI adapter changed")
    unchanged(captured, revision)
    diff = "".join(
        difflib.unified_diff(
            original.decode().splitlines(keepends=True),
            candidate_raw.decode().splitlines(keepends=True),
            fromfile=row["record"],
            tofile="staged/" + candidate.name,
        )
    )
    (output / "candidate.diff").write_text(diff)
    receipt = {
        **metadata,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "native_argv": argv,
        "exit_codes": codes,
        "candidate_sha256": sha(candidate_raw),
        "native_log_sha256": sha((output / "native.log").read_bytes()),
        "candidate_diff_sha256": sha(diff.encode()),
        "source_inputs_unchanged": True,
        "local_database_stat_unchanged": True,
        "mapping_source": mapping_source,
        "appended_native_inline_history": events,
        "scientific_review": False,
    }
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    return {
        "candidate_sha256": sha(candidate_raw),
        "receipt_sha256": sha((output / "receipt.json").read_bytes()),
    }


def apply(stage_name, output_name, candidate_sha, receipt_sha, revision, *, plan=False):
    stage_dir, output = path(stage_name, private=True), path(output_name, private=True)
    if output.exists() or head() != revision:
        raise ValueError("exclusive private output and exact revision required")
    captured = {}
    receipt_name = str((stage_dir / "receipt.json").relative_to(ROOT))
    raw_receipt = capture(captured, receipt_name, receipt_sha)
    receipt = json.loads(raw_receipt)
    if (
        receipt.get("canonical_apply") is not False
        or receipt.get("source_inputs_unchanged") is not True
        or receipt.get("native_operations")
        not in [["--apply", "--apply-status"], ["--apply-status"]]
        or receipt.get("exit_codes") != [0] * len(receipt.get("native_operations", []))
        or receipt.get("candidate_sha256") != candidate_sha
    ):
        raise ValueError("successful native candidate receipt required")
    proof_item = receipt["source_proof"]
    proof, row, original, inputs, _ = prepare(
        proof_item["path"], proof_item["sha256"], receipt["target_id"], revision
    )
    verify_operations(row, receipt["native_operations"])
    # Never overwrite an earlier capture with a second read of the same path.
    for location, raw in inputs.items():
        if location in captured and captured[location] != raw:
            raise ValueError("source changed between receipt and proof capture")
        captured.setdefault(location, raw)
    if receipt["target"] != row["record"] or receipt["before_sha256"] != sha(original):
        raise ValueError("actual target differs from reviewed native baseline")
    staged_inputs = receipt["inputs"]
    expected_names = {str(location.relative_to(ROOT)) for location in inputs}
    if set(staged_inputs) != expected_names:
        raise ValueError("staged input coverage differs")
    for name, digest in staged_inputs.items():
        capture(captured, name, digest)
    candidate_name = str((stage_dir / Path(row["record"]).name).relative_to(ROOT))
    candidate = capture(captured, candidate_name, candidate_sha)
    native = native_module()
    after, events = verify_candidate(original, candidate, row, native, receipt["mapping_source"])
    if events != receipt["appended_native_inline_history"]:
        raise ValueError("native events differ from reviewed receipt")
    unchanged(captured, revision)
    if plan:
        return {"planned": True, "target": row["record"], "candidate_sha256": candidate_sha}
    output.mkdir(parents=True)
    (output / "before.yaml").write_bytes(original)
    write_validated_community(after, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native validated serialization differs")
    unchanged(captured, revision)
    # Cooperative concurrent-change guard, not a guarantee against writers
    # that ignore the final check. No force-recovery or automatic retry.
    (output / "replacement.yaml").write_bytes(candidate)
    (output / "replacement.yaml").replace(ROOT / row["record"])
    if (ROOT / row["record"]).read_bytes() != candidate:
        raise ValueError("actual persisted candidate differs")
    result = {
        "applied": True,
        "target": row["record"],
        "target_id": row["record_id"],
        "execution_revision": revision,
        "before_sha256": sha(original),
        "after_sha256": candidate_sha,
        "reviewed_receipt_sha256": receipt_sha,
        "source_proof": proof_item,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "inputs": staged_inputs,
        "helper_sha256": sha(captured[Path(__file__)]),
        "native_operations": receipt["native_operations"],
        "native_serialization_sha256": sha((output / "validated.yaml").read_bytes()),
        "scope": receipt["scope"],
        "sidecar_status": "PENDING separate native scaffold and validation",
        "scientific_review": False,
    }
    (output / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest="action", required=True)
    staging = actions.add_parser("stage")
    staging.add_argument("--source-proof", required=True)
    staging.add_argument("--source-sha256", required=True)
    staging.add_argument("--record-id", required=True)
    staging.add_argument(
        "--operations", required=True, choices=("ground-and-status", "status-only")
    )
    application = actions.add_parser("apply")
    application.add_argument("--stage", required=True)
    application.add_argument("--candidate-sha256", required=True)
    application.add_argument("--receipt-sha256", required=True)
    for command in (staging, application):
        command.add_argument("--output", required=True)
        command.add_argument("--expected-revision", required=True)
        command.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if args.action == "stage":
        result = stage(
            args.source_proof,
            args.source_sha256,
            args.record_id,
            args.output,
            args.expected_revision,
            args.operations,
            plan=args.plan,
        )
    else:
        result = apply(
            args.stage,
            args.output,
            args.candidate_sha256,
            args.receipt_sha256,
            args.expected_revision,
            plan=args.plan,
        )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
