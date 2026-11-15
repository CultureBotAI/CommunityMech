"""Stage one exact-strain GTDB correspondence for #2848, 2026-11-15.

Inputs: fixed JMP134 source proof/native code/crosswalk; outputs: exclusive
private candidate, native log and hash-bound receipt. The native editor acts on
an original-basename private copy. No canonical application or scientific review.
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

import inspect_jmp134_grounding_20261115 as evidence
import yaml

ROOT, STATE, TARGET, BASELINE = (
    evidence.ROOT,
    evidence.STATE,
    evidence.TARGET,
    evidence.BASELINE,
)
PROOF = STATE / "jmp134-source-001.json"
PROOF_SHA = "a6294d17526c05649b26e490918a69bacaa62cf524296f77e28b8c11f457c9e7"
REVISION = "99e82a494d02201b72c8b85ed7c5e63f3390cdf0"


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def native_module():
    spec = importlib.util.spec_from_file_location("jmp134_stage_native", evidence.NATIVE)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    return native


def expected_result(native):
    rows = native.collect_rows(evidence.TABLE, {"264198"}, set(), set())
    return native.resolve_target("264198", "Cupriavidus pinatubonensis JMP134", *rows)


def verify_semantics(before, after, native, block):
    expected = copy.deepcopy(before)
    term = expected["taxonomy"][0]["taxon_term"]
    if (
        expected["id"] != "CommunityMech:000555"
        or len(expected["taxonomy"]) != 1
        or term["term"] != {"id": "NCBITaxon:264198", "label": "Cupriavidus pinatubonensis JMP134"}
        or term.get("gtdb_grounding_status") != "UNRESOLVED"
        or "gtdb_classification" in term
    ):
        raise ValueError("wrong exact-strain baseline")
    term["gtdb_classification"] = block
    term["gtdb_grounding_status"] = "GROUNDED"
    events = after.get("curation_history", [])[len(before.get("curation_history", [])) :]
    if len(events) != 2:
        raise ValueError("exactly two native appended events required")
    for event, action, changes in zip(
        events,
        ("GTDB_GROUND", "GTDB_SET_STATUS"),
        (
            "Added 1 gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395).",
            "Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        ),
        strict=True,
    ):
        if event != native.record_curation_event(
            expected,
            curator="gtdb_ground.py",
            action=action,
            changes=changes,
            timestamp=event.get("timestamp"),
        ):
            raise ValueError("native event differs")
    if expected != after:
        raise ValueError("change exceeds one block/status/two-event scope")
    return events


def capture_inputs():
    proof_bytes = PROOF.read_bytes()
    if evidence.digest(proof_bytes) != PROOF_SHA:
        raise ValueError("independently inspectable source proof changed")
    proof = json.loads(proof_bytes)
    captured = {PROOF: proof_bytes}
    for name, expected in proof["inputs"].items():
        path = ROOT / name
        if Path(name).is_absolute() or path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError("unsafe source path")
        raw = path.read_bytes()
        if evidence.digest(raw) != expected:
            raise ValueError("source proof input differs")
        captured[path] = raw
    for name in (
        "src/communitymech/curate/curation_event.py",
        "src/communitymech/validators/ncbi_domain.py",
        "src/communitymech/ontology_adapters.py",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "src/communitymech/validation/write_validated.py",
        "uv.lock",
        "reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml",
        "reviews/structured/20261111T121000Z-c15s4-record-deep-audit/review.yaml",
        "tests/test_causal_review_batch147.py",
    ):
        path = ROOT / name
        captured[path] = path.read_bytes()
    captured[Path(__file__)] = Path(__file__).read_bytes()
    return proof, captured


def unchanged(captured):
    if any(path.read_bytes() != raw for path, raw in captured.items()):
        raise ValueError("source inputs changed")


def deny_network(*_args, **_kwargs):
    raise RuntimeError("network acquisition prohibited")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric exclusive attempt required")
    output = STATE / ("jmp134-candidate-" + args.attempt)
    if output.exists() or head() != REVISION:
        raise ValueError("exact staging revision and exclusive output required")
    proof, captured = capture_inputs()
    candidate = output / Path(TARGET).name
    argv = [
        ["--community", str(candidate), "--kg-microbe-dir", str(evidence.TABLE.parents[2]), flag]
        for flag in ("--apply", "--apply-status")
    ]
    plan = {
        "code_revision": REVISION,
        "native_argv": argv,
        "inputs": {
            str(path.relative_to(ROOT)): evidence.digest(raw) for path, raw in captured.items()
        },
        "canonical_apply": False,
        "scope": "One exact NCBI strain-ID to GTDB species correspondence; preserved stock, preferred source name, biological claims, quotes, discussions and historical reviews.",
    }
    if args.plan:
        unchanged(captured)
        print(json.dumps(plan, indent=2))
        return
    output.mkdir()
    candidate.write_bytes(captured[ROOT / TARGET])
    before = yaml.safe_load(captured[ROOT / TARGET])
    native = native_module()
    database = Path.home() / ".data/oaklib/ncbitaxon.db"
    before_stat = database.stat()
    with (output / "native.log").open("x") as log:
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            with patch.dict(os.environ, {"PYSTOW_HOME": str(database.parents[1])}):
                with patch.object(socket.socket, "connect", deny_network):
                    from communitymech import ontology_adapters

                    local = ontology_adapters._local_build("ncbitaxon")
                    if local is None:
                        raise ValueError("existing local NCBI adapter required")
                    with patch.object(ontology_adapters, "_local_build", return_value=local):
                        result = expected_result(native)
                        if result != proof["native_result"]:
                            raise ValueError("fresh native result differs from source proof")
                        block = native._block(result, native.describe_mapping(evidence.TABLE))
                        codes = [native.main(command) for command in argv]
    (output / "native.exit").write_text(json.dumps(codes) + "\n")
    if codes != [0, 0]:
        raise ValueError("native private candidate execution failed")
    candidate_raw = candidate.read_bytes()
    events = verify_semantics(before, yaml.safe_load(candidate_raw), native, block)
    after_stat = database.stat()
    if (before_stat.st_size, before_stat.st_mtime_ns) != (
        after_stat.st_size,
        after_stat.st_mtime_ns,
    ):
        raise ValueError("existing NCBI adapter changed")
    unchanged(captured)
    if head() != REVISION:
        raise ValueError("staging revision changed")
    diff = "".join(
        difflib.unified_diff(
            captured[ROOT / TARGET].decode().splitlines(keepends=True),
            candidate_raw.decode().splitlines(keepends=True),
            fromfile=TARGET,
            tofile="staged/" + candidate.name,
        )
    )
    (output / "candidate.diff").write_text(diff)
    receipt = {
        **plan,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "exit_codes": codes,
        "candidate_sha256": evidence.digest(candidate_raw),
        "native_log_sha256": evidence.digest((output / "native.log").read_bytes()),
        "candidate_diff_sha256": evidence.digest(diff.encode()),
        "source_inputs_unchanged": True,
        "local_database_stat_unchanged": True,
        "native_result": result,
        "native_block": block,
        "appended_native_inline_history": events,
        "remaining_limit": proof["preserved_scientific_limit"],
        "scientific_review": False,
    }
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {
                "candidate_sha256": receipt["candidate_sha256"],
                "receipt_sha256": evidence.digest((output / "receipt.json").read_bytes()),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
