"""Stage the first ambiguity-preserving native status canary, #2848, 2026-11-15.

Inputs: exact 000546, primary study, immutable historical ledger, native code and
761 crosswalk. Outputs: exclusive private same-basename candidate and receipts.
No canonical apply mode, source acquisition, species selection or review rewrite.
"""

import argparse
import contextlib
import copy
import difflib
import hashlib
import importlib.util
import json
import socket
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-ambiguity-20261115"
RECORD = "data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml"
BEFORE = "b6dc768bf6f705611933fc50882d91957225ef1e32c61330e1adb717fe175790"
TABLE = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
ARTICLE = STATE / "faecalibacterium-source-001/article.xml"
ARTICLE_SHA = "c5b4d94fcd98543be47d7eb623a69180ae15cc98dbe1a3b1ad772818f65d421e"
NATIVE = ROOT / "scripts/gtdb_ground.py"
NATIVE_SHA = "0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175"
LEDGER = "reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch146.yaml"
OPTIONS = [
    "GTDB:s__Faecalibacterium_longum",
    "GTDB:s__Faecalibacterium_prausnitzii",
    "GTDB:s__Faecalibacterium_prausnitzii_D",
]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def verify_semantics(before, after):
    """Only the complete native ambiguity result and one event may differ."""
    if before.get("id") != "CommunityMech:000546" or len(before.get("taxonomy", [])) != 1:
        raise ValueError("exact single-stock record required")
    expected = copy.deepcopy(before)
    term = expected["taxonomy"][0]["taxon_term"]
    if term["gtdb_grounding_status"] != "UNRESOLVED" or "gtdb_classification" in term:
        raise ValueError("unexpected baseline grounding")
    term["gtdb_grounding_status"] = "AMBIGUOUS"
    term["gtdb_candidates"] = OPTIONS
    old_history = before.get("curation_history", [])
    history = after.get("curation_history", [])
    if len(history) != len(old_history) + 1 or history[:-1] != old_history:
        raise ValueError("one append-only native event required")
    event = history[-1]
    if event.get("action") != "GTDB_SET_STATUS":
        raise ValueError("native status event required")
    expected["curation_history"] = history
    if expected != after:
        raise ValueError("candidate changes science, identity or the complete ambiguity result")


def deny_network(*_args, **_kwargs):
    raise RuntimeError("network acquisition prohibited during native status staging")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.attempt.isdigit() or head() != args.expected_revision:
        raise ValueError("numeric attempt and exact execution revision required")
    output = STATE / f"ambiguity-candidate-{args.attempt}"
    if output.exists() or output.is_symlink():
        raise ValueError("preserve existing or partial candidate")
    paths = [
        ROOT / RECORD,
        TABLE,
        ARTICLE,
        ARTICLE.parent / "receipt.json",
        ARTICLE.parent / "stock-identity.json",
        STATE / "residual-groups-001.json",
        ROOT / "references_cache/PMID_42655156.txt",
        ROOT / LEDGER,
        ROOT / "tests/test_causal_review_batch146.py",
        ROOT / "src/communitymech/schema/communitymech.yaml",
        ROOT / "src/communitymech/curate/curation_event.py",
        ROOT / "src/communitymech/validators/ncbi_domain.py",
        ROOT / "src/communitymech/ontology_adapters.py",
        ROOT / "uv.lock",
        ROOT / "scripts/adhoc/capture_faecalibacterium_ambiguity_source_20261115.py",
        NATIVE,
        Path(__file__),
    ]
    captures = {path: path.read_bytes() for path in paths}
    for path, digest in (
        (ROOT / RECORD, BEFORE),
        (TABLE, TABLE_SHA),
        (ARTICLE, ARTICLE_SHA),
        (NATIVE, NATIVE_SHA),
    ):
        if sha(captures[path]) != digest:
            raise ValueError(f"fixed source changed: {path.name}")
    source_receipt = json.loads(captures[ARTICLE.parent / "receipt.json"])
    if source_receipt.get("status") != "verified" or source_receipt["sha256"] != ARTICLE_SHA:
        raise ValueError("verified primary source required")
    if any(
        sha(captures[ROOT / name]) != digest for name, digest in source_receipt["inputs"].items()
    ):
        raise ValueError("primary capture provenance changed")
    candidate = output / Path(RECORD).name
    argv = [
        "--community",
        str(candidate),
        "--kg-microbe-dir",
        str(TABLE.parents[2]),
        "--apply-status",
    ]
    plan = {
        "execution_revision": args.expected_revision,
        "record": RECORD,
        "record_id": "CommunityMech:000546",
        "native_argv": argv,
        "canonical_apply": False,
        "inputs": {str(path.relative_to(ROOT)): sha(raw) for path, raw in captures.items()},
        "scope": "Existing NCBI species descriptor only; retain all three GTDB alternatives without assigning any to A2-165/JCM31915. No full scientific reassessment or historical-ledger rewrite.",
    }
    if args.plan:
        print(json.dumps(plan, indent=2))
        return
    output.mkdir()
    candidate.write_bytes(captures[ROOT / RECORD])
    spec = importlib.util.spec_from_file_location("native_gtdb_ambiguity", NATIVE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    started = datetime.now(timezone.utc).isoformat()
    with (output / "native.log").open("x") as log:
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            # This exact species lookup resolves before ontology fallback. Any
            # unexpected acquisition must fail instead of changing the evidence.
            with patch.object(socket.socket, "connect", deny_network):
                code = module.main(argv)
    (output / "native.exit").write_text(f"{code}\n")
    if code != 0:
        raise ValueError("native status writer failed; preserve failed attempt")
    if not (output / "native.log").stat().st_size:
        raise ValueError("native command persisted no log")
    after_raw = candidate.read_bytes()
    before = yaml.safe_load(captures[ROOT / RECORD])
    after = yaml.safe_load(after_raw)
    verify_semantics(before, after)
    if (
        any(path.read_bytes() != raw for path, raw in captures.items())
        or head() != args.expected_revision
    ):
        raise ValueError("reviewed source changed during native staging")
    diff = "".join(
        difflib.unified_diff(
            captures[ROOT / RECORD].decode().splitlines(True),
            after_raw.decode().splitlines(True),
            fromfile=RECORD,
            tofile="staged/" + candidate.name,
        )
    )
    (output / "candidate.diff").write_text(diff)
    receipt = {
        **plan,
        "started_at": started,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "native_exit_code": code,
        "candidate_sha256": sha(after_raw),
        "native_log_sha256": sha((output / "native.log").read_bytes()),
        "native_exit_sha256": sha((output / "native.exit").read_bytes()),
        "diff_sha256": sha(diff.encode()),
        "source_inputs_unchanged": True,
        "appended_native_inline_history": after["curation_history"][-1],
        "sidecar": "NOT RUN; candidate has not been applied.",
    }
    with (output / "receipt.json").open("x") as stream:
        json.dump(receipt, stream, indent=2)
        stream.write("\n")
    print(
        json.dumps(
            {
                "candidate_sha256": receipt["candidate_sha256"],
                "receipt_sha256": sha((output / "receipt.json").read_bytes()),
                "output": str(output.relative_to(ROOT)),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
