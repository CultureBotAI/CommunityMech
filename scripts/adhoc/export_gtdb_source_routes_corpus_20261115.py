"""Export retained native whole-corpus check evidence, #2849, 2026-11-15.

Inputs: exact mirrored M5 plan/run artifacts and unchanged source checksums.
Outputs: immutable sanitized log/exit/metadata derivatives only. No validation,
source acquisition, record edits, scientific approval or issue-status changes.
"""

import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

from export_m5_technical_evidence_20261114 import immutable, sanitize

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-source-routes-2849-20261115"
OUT = ROOT / "reports/gtdb-source-routes-2849-20261115"
REVISION = "f39c0fe400740a754f2d006d17ffa8c8e82fae63"
TEST = "tests/test_gtdb_uncurated_blocks_match_the_tool.py"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    captured = {}

    def read(path):
        if not path.resolve().is_relative_to(ROOT):
            raise ValueError("input escapes checkout")
        if path not in captured:
            captured[path] = path.read_bytes()
        return captured[path]

    payloads = {}
    for mode in ("plan", "run"):
        directory = STATE / f"corpus-{mode}-001"
        raw = {path.name: read(path) for path in directory.iterdir() if path.is_file()}
        command = f".venv/bin/python -m pytest -q {TEST} -rs"
        if mode == "plan":
            command += " --collect-only"
        if raw["command.txt"].decode().strip() != command:
            raise ValueError("native command differs")
        if raw["revision.txt"].decode().strip() != REVISION or int(raw["native.exit"]) != 0:
            raise ValueError("wrong native revision or unsuccessful exit")
        if raw["python.txt"].decode().strip() != "Python 3.13.2":
            raise ValueError("native runtime differs")
        if raw["records.nul"] != raw["records-after.nul"]:
            raise ValueError("native record inventory changed")
        hashes = {}
        for line in raw["inputs.sha256"].decode().splitlines():
            expected, relative = line.split("  ", 1)
            if not re.fullmatch(r"[0-9a-f]{64}", expected) or relative in hashes:
                raise ValueError("malformed or duplicated native input")
            if sha(read(ROOT / relative)) != expected:
                raise ValueError("native source input changed: " + relative)
            hashes[relative] = expected
        if raw["inputs-verified.log"].decode() != "".join(f"{path}: OK\n" for path in hashes):
            raise ValueError("native after-check evidence differs")
        if hashes[TEST] != "102ee759b9cd43c34d65d1b169affe6f0823400d40fa4571cdf59fa462306df0":
            raise ValueError("the maintained corpus test changed")
        table = ".temp/gtdb-source-routes-2849-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
        if hashes[table] != "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd":
            raise ValueError("the retained crosswalk changed")
        log = raw["native.log"].decode()
        required = r"3 tests collected" if mode == "plan" else r"3 passed in ([0-9.]+)s"
        if not re.search(required, log) or re.search(r"\d+ skipped|SKIPPED", log):
            raise ValueError("native result is incomplete or skipped")
        started = raw["started-at.txt"].decode().strip()
        finished = raw["finished-at.txt"].decode().strip()
        if datetime.fromisoformat(finished) < datetime.fromisoformat(started):
            raise ValueError("native completion precedes its start")
        redactions = Counter()
        public_log = sanitize(log, redactions).encode()
        metadata = {
            "execution_revision": REVISION,
            "runtime": "M5, Python 3.13.2",
            "command": command,
            "mode": "COLLECTION ONLY" if mode == "plan" else "EXECUTED",
            "exit_code": 0,
            "started_at": started,
            "finished_at": finished,
            "raw_artifacts": {name: sha(value) for name, value in sorted(raw.items())},
            "public_log_sha256": sha(public_log),
            "redactions": dict(redactions),
            "record_inventory_preserved": True,
            "all_captured_source_hashes_preserved": True,
            "runner_sha256": hashes["scripts/adhoc/check_gtdb_source_routes_corpus_20261115.sh"],
            "exporter_sha256": sha(read(Path(__file__))),
            "scope": "The unchanged maintained uncurated-block test module only. Curated correspondence evidence is assessed by the separate saved canaries. This is not full QC, a whole-record scientific review or resolution of the separate status backlog2848.",
            "raw_persistence": "Original isolated M5 checkout and verified private local mirror.",
        }
        prefix = OUT / f"corpus-{mode}-001"
        payloads[prefix.with_suffix(".log.txt")] = public_log
        payloads[prefix.with_suffix(".exit.txt")] = raw["native.exit"]
        payloads[prefix.with_suffix(".receipt.json")] = (
            json.dumps(metadata, indent=2) + "\n"
        ).encode()
    for path, raw in captured.items():
        if path.read_bytes() != raw:
            raise ValueError("captured input changed before publication")
    for path, raw in payloads.items():
        immutable(path, raw)
    print(
        json.dumps({"public_artifacts": len(payloads), "snapshot_inputs_verified": len(captured)})
    )


if __name__ == "__main__":
    main()
