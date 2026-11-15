"""Reproduce two observed code006 GTDB failures locally, 2026-11-15.

Inputs: exact c9e151eb checkout, its frozen installed environment, preserved
761d5537 crosswalk and existing local NCBI adapter. Outputs: private prerequisite
receipt plus unchanged native runner's pytest log/exit/receipt. No canonical,
classifier, baseline, ontology-cache or M5 writes; no network acquisition.
"""

import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

import m5_completion_checks as native

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"
REVISION = "c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a"
CROSSWALK = Path(
    "/Users/marcin/agent-work/CommunityMech/completion-20261114/.temp/m5-completion-20261114/yolo-sources/NCBI2GTDB.tsv.gz"
)
CROSSWALK_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
TESTS = [
    "tests/test_gtdb_coherence_validator.py::test_the_stored_statuses_reproduce_from_the_classifier",
    "tests/test_gtdb_uncurated_blocks_match_the_tool.py::test_a_block_the_tool_would_not_produce_is_curated",
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        != REVISION
    ):
        raise ValueError("wrong source revision")
    if (STATE / "install-001.exit").read_text().strip() != "0":
        raise ValueError("frozen installation did not pass")
    if sha(CROSSWALK) != CROSSWALK_SHA:
        raise ValueError("preserved crosswalk differs")
    ncbi = Path.home() / ".data/oaklib/ncbitaxon.db"
    stat = ncbi.stat()
    if stat.st_size == 0:
        raise ValueError("local NCBI prerequisite is empty")
    destination = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
    destination.parent.mkdir(parents=True)
    shutil.copyfile(CROSSWALK, destination)
    if sha(destination) != CROSSWALK_SHA:
        raise ValueError("private mapping copy differs")
    shutil.copyfile(STATE / "install-001.exit", STATE / "install.exit")
    with (STATE / "prerequisites-001.json").open("x") as stream:
        json.dump(
            {
                "revision": REVISION,
                "helper_sha256": sha(Path(__file__)),
                "mapping_source": str(CROSSWALK),
                "mapping_sha256": CROSSWALK_SHA,
                "ncbi_adapter": {
                    "path": str(ncbi),
                    "size": stat.st_size,
                    "mtime_ns": stat.st_mtime_ns,
                },
                "install_log_sha256": sha(STATE / "install-001.log"),
                "install_exit_sha256": sha(STATE / "install-001.exit"),
                "tests": TESTS,
            },
            stream,
            indent=2,
        )
        stream.write("\n")
    native.STATE = STATE
    original_environment = native.environment

    def environment():
        env = original_environment()
        env.update(
            KG_MICROBE_DIR=str(STATE / "kg-microbe"),
            PYSTOW_HOME=str(ncbi.parent.parent),
            UV_NO_SYNC="true",
        )
        return env

    native.environment = environment
    result = native.run_check(
        "two-tests-001",
        [],
        expected_revision=REVISION,
        native_command=[
            str(ROOT / ".venv/bin/python"),
            "-m",
            "pytest",
            *TESTS,
            "-vv",
            "--tb=long",
            "-rs",
        ],
    )
    after = ncbi.stat()
    if sha(CROSSWALK) != CROSSWALK_SHA or sha(destination) != CROSSWALK_SHA:
        raise ValueError("crosswalk changed during diagnostic")
    if (after.st_size, after.st_mtime_ns) != (stat.st_size, stat.st_mtime_ns):
        raise ValueError("NCBI adapter metadata changed during diagnostic")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
