"""Stage one native status-only diagnostic candidate, 2026-11-15, #2848.

Inputs: frozen000434, exact761 crosswalk, historical scientific review and local
NCBI SQLite. Outputs: exclusive private candidate/log/exit/diff/receipt. This has
no canonical-apply mode; it never edits the target record or historical review.
"""

import argparse
import contextlib
import copy
import difflib
import importlib.util
import json
import os
import socket
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import yaml
from inspect_code006_gtdb_route_20261115 import PIN, ROOT, TABLE, TABLE_SHA, git, sha

RECORD = ROOT / "kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml"
REVIEW = (
    ROOT / "reviews/structured/20261105T223042Z-pr2035-acidic-nitrification-successor/review.yaml"
)
DATABASE = Path.home() / ".data/oaklib/ncbitaxon.db"
STATE = ROOT / ".temp/gtdb-code006-20261115"


def deny_network(*_args, **_kwargs):
    raise RuntimeError("network acquisition prohibited during status-only staging")


def semantic_payload(doc):
    value = copy.deepcopy(doc)
    value.pop("curation_history", None)
    for entry in value["taxonomy"]:
        entry["taxon_term"].pop("gtdb_grounding_status", None)
        entry["taxon_term"].pop("gtdb_candidates", None)
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric exclusive attempt required")
    output = STATE / f"status-candidate-{args.attempt}"
    if output.exists():
        raise ValueError("candidate namespace already exists")
    if git("rev-parse", "HEAD") != PIN or sha(TABLE) != TABLE_SHA:
        raise ValueError("exact frozen code/table required")
    database_stat = DATABASE.stat()
    if database_stat.st_size < 1:
        raise ValueError("nonempty local NCBI database required")
    native_source = ROOT / "scripts/gtdb_ground.py"
    # The imported module supplies source paths, revision and hashing/Git logic;
    # its bytes are part of the actual implementation too (#2851).
    imported_source = Path(__file__).with_name("inspect_code006_gtdb_route_20261115.py")
    inputs = {
        p: sha(p) for p in (RECORD, REVIEW, TABLE, native_source, Path(__file__), imported_source)
    }
    candidate = output / RECORD.name
    argv = [
        "--community",
        str(candidate),
        "--kg-microbe-dir",
        str(TABLE.parents[2]),
        "--apply-status",
    ]
    plan = {
        "code_revision": PIN,
        "native_argv": argv,
        "inputs": {str(p.relative_to(ROOT)): h for p, h in inputs.items()},
        "canonical_apply": False,
        "scope": "Current classifier computability on existing term IDs/labels only; no new GTDB block, species/genome identity, scientific re-review, or historical review rewrite.",
        "historical_review_disposition": "Preserve immutable Nov5 review. Its genus/species uncertainty remains valid; this candidate reports current crosswalk computability at the already-declared genus only.",
    }
    if args.plan:
        print(json.dumps(plan, indent=2))
        return
    output.mkdir()
    candidate.write_bytes(RECORD.read_bytes())
    before = yaml.safe_load(RECORD.read_bytes())
    spec = importlib.util.spec_from_file_location("gtdb_ground", native_source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    start = datetime.now(timezone.utc).isoformat()
    with (output / "native.log").open("x") as log:
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            with patch.dict(os.environ, {"PYSTOW_HOME": str(DATABASE.parents[1])}):
                with patch.object(socket.socket, "connect", deny_network):
                    # Populate the maintained shared accessor from the actual
                    # local SQL path; refuse if absent, never fall through.
                    from communitymech import ontology_adapters

                    local = ontology_adapters._local_build("ncbitaxon")
                    if local is None:
                        raise ValueError("native local NCBI adapter failed")
                    with patch.object(ontology_adapters, "_local_build", return_value=local):
                        code = module.main(argv)
    (output / "native.exit").write_text(f"{code}\n")
    after = yaml.safe_load(candidate.read_bytes())
    before_history = before.get("curation_history", [])
    after_history = after.get("curation_history", [])
    if code != 0 or semantic_payload(before) != semantic_payload(after):
        raise ValueError("native status-only semantic gate failed")
    if after_history[:-1] != before_history or after_history[-1]["action"] != "GTDB_SET_STATUS":
        raise ValueError("exactly one append-only native history event required")
    if any(p.stat().st_size == 0 for p in (candidate, output / "native.log")):
        raise ValueError("nonempty native artifacts required")
    if inputs != {p: sha(p) for p in inputs} or git("rev-parse", "HEAD") != PIN:
        raise ValueError("source inputs changed during staging")
    final_stat = DATABASE.stat()
    if (database_stat.st_size, database_stat.st_mtime_ns) != (
        final_stat.st_size,
        final_stat.st_mtime_ns,
    ):
        raise ValueError("local NCBI database changed")
    diff = "".join(
        difflib.unified_diff(
            RECORD.read_text().splitlines(keepends=True),
            candidate.read_text().splitlines(keepends=True),
            fromfile=str(RECORD.relative_to(ROOT)),
            tofile="staged/" + RECORD.name,
        )
    )
    (output / "candidate.diff").write_text(diff)
    receipt = {
        **plan,
        "started_at": start,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "exit_code": code,
        "candidate_sha256": sha(candidate),
        "native_log_sha256": sha(output / "native.log"),
        "candidate_diff_sha256": sha(output / "candidate.diff"),
        "source_inputs_unchanged": True,
        "local_database_stat_unchanged": True,
        "appended_native_inline_history": after_history[-1],
        "sidecar": "Not created: this is an unapplied diagnostic candidate.",
    }
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {
                "output": str(output.relative_to(ROOT)),
                "candidate_sha256": sha(candidate),
                "receipt_sha256": sha(output / "receipt.json"),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
