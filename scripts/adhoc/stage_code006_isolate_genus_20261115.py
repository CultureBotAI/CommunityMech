"""Stage the reviewed batch147 genus subset through the native CLI, #2848.

2026-11-15. Inputs: pinned two-record plan, table, unchanged selected source and
historical reviews. Outputs: exclusive private original-basename candidate,
native logs, exact diff and receipt. No canonical application or acquisition.
"""

import argparse
import contextlib
import copy
import difflib
import hashlib
import importlib.util
import json
import os
import socket
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"
PLAN = STATE / "genus-subset-plan-001.json"
PLAN_SHA = "1501b8ec1b52aaf7936c9da2a48f4ee208b9e22f4b7bac135dcf5856a4363ae2"
REVISION = "fe18c5d2e1d2d151440137270402d895e9f8418d"
TABLE = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def deny_network(*_args, **_kwargs):
    raise RuntimeError("network acquisition prohibited")


def verify_semantics(before, after, native, block, row):
    expected = copy.deepcopy(before)
    if before["id"] != row["record_id"] or len(before["taxonomy"]) != 1:
        raise ValueError("exact selected isolate required")
    term = expected["taxonomy"][0]["taxon_term"]
    if term["gtdb_grounding_status"] != "UNRESOLVED" or "gtdb_classification" in term:
        raise ValueError("exact ungrounded baseline required")
    if term["term"] != {"id": block["ncbi_source_id"], "label": block["gtdb_taxon"]}:
        raise ValueError("same-genus identity required")
    term["gtdb_classification"], term["gtdb_grounding_status"] = block, "GROUNDED"
    events = after.get("curation_history", [])[len(before.get("curation_history", [])) :]
    if len(events) != 2:
        raise ValueError("exactly two native events required")
    for event, action, changes in zip(
        events,
        ("GTDB_GROUND", "GTDB_SET_STATUS"),
        (
            "Added 1 gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395).",
            "Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        ),
        strict=True,
    ):
        actual = native.record_curation_event(
            expected,
            curator="gtdb_ground.py",
            action=action,
            changes=changes,
            timestamp=event.get("timestamp"),
        )
        if actual != event:
            raise ValueError("native event differs")
    if expected != after:
        raise ValueError("candidate exceeds exact genus/status/native-history scope")
    return events


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", choices=["000552", "000553"], required=True)
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.attempt.isdigit() or sha(PLAN) != PLAN_SHA or head() != REVISION:
        raise ValueError("exact approved plan, execution revision and numeric attempt required")
    plan = json.loads(PLAN.read_bytes())
    rows = [r for r in plan["rows"] if r["record_id"] == "CommunityMech:" + args.record]
    if len(rows) != 1:
        raise ValueError("unique planned isolate required")
    row = rows[0]
    target = ROOT / row["record"]
    source = ROOT / "scripts/gtdb_ground.py"
    output = STATE / f"isolate-{args.record}-candidate-{args.attempt}"
    if output.exists():
        raise ValueError("exclusive private candidate namespace required")
    paths = [
        PLAN,
        target,
        source,
        TABLE,
        ROOT / row["primary_source"]["path"],
        Path(__file__),
        ROOT / "src/communitymech/curate/curation_event.py",
        *(ROOT / item["ledger"] for item in row["historical_byte_bindings"]),
        *(ROOT / item["review"] for item in row["saved_review_inputs"]),
    ]
    inputs = {p: sha(p) for p in paths}
    for path, value in inputs.items():
        name = str(path.relative_to(ROOT))
        if name in plan["inputs"] and value != plan["inputs"][name]:
            raise ValueError("selected planned input changed")
    if inputs[target] != row["baseline_sha256"]:
        raise ValueError("exact planned baseline required")
    candidate = output / target.name
    commands = [
        ["--community", str(candidate), "--kg-microbe-dir", str(TABLE.parents[2]), flag]
        for flag in ("--apply", "--apply-status")
    ]
    receipt = {
        "target": row["record"],
        "record_id": row["record_id"],
        "code_revision": REVISION,
        "canonical_apply": False,
        "native_argv": commands,
        "inputs": {str(p.relative_to(ROOT)): value for p, value in inputs.items()},
        "scope": row["compatibility"],
        "historical_guard": row["actual_historical_guard"],
    }
    if args.plan:
        print(json.dumps(receipt, indent=2))
        return
    output.mkdir()
    candidate.write_bytes(target.read_bytes())
    before = yaml.safe_load(candidate.read_bytes())
    spec = importlib.util.spec_from_file_location("native_isolate_grounding", source)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    database = Path.home() / ".data/oaklib/ncbitaxon.db"
    initial_stat = database.stat()
    with (output / "native.log").open("x") as log:
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            with patch.dict(os.environ, {"PYSTOW_HOME": str(database.parents[1])}):
                with patch.object(socket.socket, "connect", deny_network):
                    from communitymech import ontology_adapters

                    local = ontology_adapters._local_build("ncbitaxon")
                    if local is None:
                        raise ValueError("existing local NCBI adapter required")
                    with patch.object(ontology_adapters, "_local_build", return_value=local):
                        label = row["native_result"]["gtdb_taxon"]
                        groups = native.collect_rows(
                            TABLE, set(), set(), set(native.lookup_keys(label))
                        )
                        result = native.resolve_target(
                            row["native_result"]["ncbi_source_id"].split(":")[1], label, *groups
                        )
                        if result != row["native_result"]:
                            raise ValueError("native genus result differs from reviewed plan")
                        block = native._block(result, native.describe_mapping(TABLE))
                        codes = [native.main(command) for command in commands]
    (output / "native.exit").write_text(json.dumps(codes) + "\n")
    if codes != [0, 0]:
        raise ValueError("native candidate commands failed")
    events = verify_semantics(before, yaml.safe_load(candidate.read_bytes()), native, block, row)
    end_stat = database.stat()
    if (initial_stat.st_size, initial_stat.st_mtime_ns) != (end_stat.st_size, end_stat.st_mtime_ns):
        raise ValueError("local NCBI adapter changed")
    if head() != REVISION or inputs != {p: sha(p) for p in inputs}:
        raise ValueError("source inputs changed during staging")
    diff = "".join(
        difflib.unified_diff(
            target.read_text().splitlines(keepends=True),
            candidate.read_text().splitlines(keepends=True),
            fromfile=row["record"],
            tofile="staged/" + target.name,
        )
    )
    (output / "candidate.diff").write_text(diff)
    receipt.update(
        {
            "completed_at": datetime.now(timezone.utc).isoformat(),
            "exit_codes": codes,
            "candidate_sha256": sha(candidate),
            "native_log_sha256": sha(output / "native.log"),
            "native_block": block,
            "appended_native_inline_history": events,
            "source_inputs_unchanged": True,
            "local_database_stat_unchanged": True,
        }
    )
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {"candidate_sha256": sha(candidate), "receipt_sha256": sha(output / "receipt.json")},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
