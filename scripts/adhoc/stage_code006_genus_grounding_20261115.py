"""Stage one source-backed Mycobacterium genus correspondence, #2848.

2026-11-15. Inputs: actual status-canary chain, exact761 table and native
grounder; outputs: exclusive private original-basename candidate, logs, diff
and receipt. No canonical application, species identity or scientific review.
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
TARGET = "kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml"
BASELINE = "d58669e049476d801fa68cdb50184e6ac9c21c07cdbc2517ef32579f75acb7f8"
REVISION = "956d00c6143020810ef7a60a6298e67fb0ee0caf"
TABLE = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def deny_network(*_args, **_kwargs):
    raise RuntimeError("network acquisition prohibited")


def verify_semantics(before, after, native, expected_block):
    expected = copy.deepcopy(before)
    term = expected["taxonomy"][1]["taxon_term"]
    if (
        expected["id"] != "CommunityMech:000434"
        or term["term"] != {"id": "NCBITaxon:1763", "label": "Mycobacterium"}
        or term.get("gtdb_grounding_status") != "NOT_ATTEMPTED"
        or "gtdb_classification" in term
    ):
        raise ValueError("wrong bounded current genus baseline")
    term["gtdb_classification"] = expected_block
    term["gtdb_grounding_status"] = "GROUNDED"
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
        if event != actual:
            raise ValueError("native history event differs")
    if after != expected:
        raise ValueError("candidate exceeds one native genus block/status/history scope")
    return events


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric exclusive attempt required")
    output = STATE / f"genus-candidate-{args.attempt}"
    if (
        output.exists()
        or head() != REVISION
        or sha(ROOT / TARGET) != BASELINE
        or sha(TABLE) != TABLE_SHA
    ):
        raise ValueError("exact current source and fresh private namespace required")
    source = ROOT / "scripts/gtdb_ground.py"
    paths = [
        ROOT / TARGET,
        TABLE,
        source,
        Path(__file__),
        ROOT / "references_cache/PMID_42762737.txt",
        ROOT
        / "reviews/structured/20261105T223042Z-pr2035-acidic-nitrification-successor/review.yaml",
        ROOT / "reviews/structured/20261115T050137Z-gtdb-status-000434-canary/review.yaml",
        STATE / "assessment-saved-audit-004.json",
        STATE / "applied-001/receipt.json",
        ROOT
        / "history/records/Acidic_Nitrification_Minimal_Consortium/2026-11-15T045124Z-codex-aa564b.yaml",
    ]
    inputs = {p: sha(p) for p in paths}
    if (
        inputs[STATE / "applied-001/receipt.json"]
        != "39bac49ad4dc868eb2423d94ce1eaac64cef0bdd23595f233d81a75ac1fe853b"
    ):
        raise ValueError("actual prior application receipt differs")
    candidate = output / Path(TARGET).name
    argv = [
        ["--community", str(candidate), "--kg-microbe-dir", str(TABLE.parents[2]), flag]
        for flag in ("--apply", "--apply-status")
    ]
    plan = {
        "code_revision": REVISION,
        "native_argv": argv,
        "inputs": {str(p.relative_to(ROOT)): value for p, value in inputs.items()},
        "canonical_apply": False,
        "scope": "One same-genus database correspondence; no inferred source species/genome, renamed organism, biological assertion or old review change.",
        "prior_review_disposition": "November5 species/genome and mechanism uncertainty remains unchanged; this new mapping describes NCBI genus1763 correspondence to the identical GTDB genus in exact761 crosswalk.",
    }
    if args.plan:
        print(json.dumps(plan, indent=2))
        return
    output.mkdir()
    candidate.write_bytes((ROOT / TARGET).read_bytes())
    before = yaml.safe_load(candidate.read_bytes())
    spec = importlib.util.spec_from_file_location("native_genus_grounding", source)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    database = Path.home() / ".data/oaklib/ncbitaxon.db"
    stat = database.stat()
    with (output / "native.log").open("x") as log:
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            with patch.dict(os.environ, {"PYSTOW_HOME": str(database.parents[1])}):
                with patch.object(socket.socket, "connect", deny_network):
                    from communitymech import ontology_adapters

                    local = ontology_adapters._local_build("ncbitaxon")
                    if local is None:
                        raise ValueError("existing local NCBI adapter required")
                    with patch.object(ontology_adapters, "_local_build", return_value=local):
                        rows = native.collect_rows(
                            TABLE, set(), set(), set(native.lookup_keys("Mycobacterium"))
                        )
                        result = native.resolve_target("1763", "Mycobacterium", *rows)
                        if (
                            not result
                            or result.get("gtdb_id") != "GTDB:g__Mycobacterium"
                            or result.get("majority_fraction") != 1.0
                            or result.get("support_genomes") != 18589
                            or result.get("total_genomes") != 18589
                            or result.get("is_reclassified") is not False
                        ):
                            raise ValueError("exact same-genus source correspondence differs")
                        block = native._block(result, native.describe_mapping(TABLE))
                        codes = [native.main(command) for command in argv]
    (output / "native.exit").write_text(json.dumps(codes) + "\n")
    if codes != [0, 0]:
        raise ValueError("native grounding/status command failed")
    events = verify_semantics(before, yaml.safe_load(candidate.read_bytes()), native, block)
    if inputs != {p: sha(p) for p in inputs} or head() != REVISION:
        raise ValueError("source inputs changed during staging")
    end = database.stat()
    if (stat.st_size, stat.st_mtime_ns) != (end.st_size, end.st_mtime_ns):
        raise ValueError("local NCBI adapter changed")
    diff = "".join(
        difflib.unified_diff(
            (ROOT / TARGET).read_text().splitlines(keepends=True),
            candidate.read_text().splitlines(keepends=True),
            fromfile=TARGET,
            tofile="staged/" + candidate.name,
        )
    )
    (output / "candidate.diff").write_text(diff)
    receipt = {
        **plan,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "exit_codes": codes,
        "candidate_sha256": sha(candidate),
        "native_log_sha256": sha(output / "native.log"),
        "candidate_diff_sha256": sha(output / "candidate.diff"),
        "source_inputs_unchanged": True,
        "local_database_stat_unchanged": True,
        "native_block": block,
        "appended_native_inline_history": events,
    }
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {"candidate_sha256": sha(candidate), "receipt_sha256": sha(output / "receipt.json")},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
