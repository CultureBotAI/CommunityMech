"""Run one native focused gate for the #2831 000122 successor, 2026-11-15.

Inputs: current target, pinned native source/config, installed frozen environment.
Outputs: unique private log/receipt/exit and hashes. No provider enrichment or
canonical cache writes: reference validation uses a verified private cache copy
and --no-full-text; preflight requires every referenced source already loaded.
Nine scoped gates do not imply full QC or source truth. Copied from the verified
check_gut_record_20261115 launcher to preserve its historical source bytes.
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_reference_validator.models import ReferenceValidationConfig

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/phase2-gut-20261115"
TARGET = "kb/communities/LBNL_Human_Gut_Interaction_SynCom.yaml"
BASE = "de4c6450dd3e42f205c2f7e8f11b8fe44f03bd6b"
HISTORY = "history/records/LBNL_Human_Gut_Interaction_SynCom"
CACHES = {
    "PMID:29930200": "references_cache/PMID_29930200.txt",
}
EXTRA_CACHES = ["references_cache/pmc_full_pmid_29930200.txt"]
GATES = {
    "schema": ["just", "--no-dotenv", "validate", TARGET],
    "strict": ["just", "--no-dotenv", "validate-strict", TARGET],
    "gtdb": ["just", "--no-dotenv", "validate-gtdb", TARGET],
    "domain": ["just", "--no-dotenv", "validate-gtdb-domain", TARGET],
    "scalars": ["just", "--no-dotenv", "validate-scalars", TARGET],
    "terms": ["just", "--no-dotenv", "validate-terms", TARGET],
    "history": ["just", "--no-dotenv", "validate-history", HISTORY],
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def references(value):
    if isinstance(value, dict):
        if "reference" in value:
            yield value["reference"]
        for item in value.values():
            yield from references(item)
    elif isinstance(value, list):
        for item in value:
            yield from references(item)


def inputs(record):
    names = [
        TARGET,
        record,
        "uv.lock",
        "justfile",
        "conf/reference_validator.yaml",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "src/communitymech/schema/history.yaml",
        *CACHES.values(),
        *EXTRA_CACHES,
    ]
    names.extend(str(path.relative_to(ROOT)) for path in (ROOT / HISTORY).glob("*.yaml"))
    return {name: sha(ROOT / name) for name in sorted(names)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gate", choices=[*GATES, "references", "network"])
    parser.add_argument(
        "--name", required=True, help="new receipt basename, e.g. canary-scalars-001"
    )
    parser.add_argument(
        "--record", default=TARGET, help="canonical target or its exclusive staged candidate"
    )
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    record_path = (ROOT / args.record).resolve()
    if record_path != ROOT / TARGET and not record_path.is_relative_to(STATE):
        raise ValueError("record must be named target or its private candidate")
    record = str(record_path.relative_to(ROOT))
    if yaml.safe_load(record_path.read_bytes()).get("id") != "CommunityMech:000122":
        raise ValueError("wrong record identity")
    if not args.name.replace("-", "").isalnum() or not args.name.startswith("canary-"):
        raise ValueError("unsafe receipt name")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if revision != BASE:
        raise ValueError("unexpected checkout revision; rebind gate run before continuing")
    receipt = STATE / (args.name + ".json")
    log = STATE / (args.name + ".log")
    code_path = STATE / (args.name + ".exit")
    if any(path.exists() for path in (receipt, log, code_path)):
        raise ValueError("refusing to replace a retained native run")
    if args.plan:
        print(
            json.dumps({"gate": args.gate, "record": record, "name": args.name, "head": revision})
        )
        return
    bound = inputs(record)
    command = GATES.get(args.gate)
    if command:
        command = [record if item == TARGET else item for item in command]
    if args.gate == "strict":
        command = command + ["--out", str((STATE / (args.name + ".tsv")).relative_to(ROOT))]
    cache_copy = None
    record_copy = None
    if args.gate == "terms":
        config_path = STATE / (args.name + "-oak.yaml")
        adapters = {
            "NCBITaxon": "/Users/marcin/.data/oaklib/ncbitaxon.db",
            "ENVO": "/Users/marcin/.data/oaklib/envo.db",
            "GO": "/Users/marcin/.data/oaklib/go.db",
        }
        if config_path.exists() or any(not Path(path).is_file() for path in adapters.values()):
            raise ValueError("local adapter prerequisite or exclusive config failed")
        config_path.write_text(
            yaml.safe_dump(
                {"ontology_adapters": {key: "sqlite:" + value for key, value in adapters.items()}}
            )
        )
        command = [
            "uv",
            "run",
            "--no-sync",
            "linkml-term-validator",
            "validate-data",
            record,
            "-s",
            "src/communitymech/schema/communitymech.yaml",
            "--labels",
            "--config",
            str(config_path.relative_to(ROOT)),
            "--cache-dir",
            str((STATE / (args.name + "-labels")).relative_to(ROOT)),
        ]
    if args.gate == "network":
        record_directory = STATE / (args.name + "-records")
        record_directory.mkdir()
        record_copy = record_directory / Path(TARGET).name
        record_copy.write_bytes(record_path.read_bytes())
        command = [
            "uv",
            "run",
            "--no-sync",
            "communitymech",
            "audit-network",
            "--communities-dir",
            str(record_directory.relative_to(ROOT)),
            "--json",
        ]
    if args.gate == "references":
        identifiers = set(references(yaml.safe_load(record_path.read_bytes())))
        if identifiers != set(CACHES):
            raise ValueError("source list changed; inspect sources before native validation")
        cache_copy = STATE / (args.name + "-cache")
        cache_copy.mkdir()
        for relative in [*CACHES.values(), *EXTRA_CACHES]:
            (cache_copy / Path(relative).name).write_bytes((ROOT / relative).read_bytes())
        fetcher = ReferenceFetcher(
            ReferenceValidationConfig(cache_dir=cache_copy, fetch_full_text=False)
        )
        for identifier in identifiers:
            loaded = fetcher._load_from_disk(identifier)
            if loaded is None or not loaded.content:
                raise ValueError("native cache miss; provider calls are not permitted in this gate")
        command = [
            "uv",
            "run",
            "--no-sync",
            "linkml-reference-validator",
            "validate",
            "data",
            record,
            "-s",
            "src/communitymech/schema/communitymech.yaml",
            "--config",
            "conf/reference_validator.yaml",
            "--cache-dir",
            str(cache_copy.relative_to(ROOT)),
            "--no-full-text",
        ]
    env = dict(os.environ)
    env.update(
        UV_NO_SYNC="true",
        JUST_NO_DOTENV="true",
        GIT_TERMINAL_PROMPT="0",
        PYTHONUNBUFFERED="1",
        NO_COLOR="1",
    )
    for name in ("EMAIL", "NCBI_EMAIL", "ENTREZ_EMAIL", "CROSSREF_MAILTO", "OPENALEX_MAILTO"):
        env.pop(name, None)
    result = {
        "name": args.name,
        "gate": args.gate,
        "started_at": now(),
        "head": revision,
        "record": record,
        "record_worktree_sha256": bound[record],
        "inputs": bound,
        "command": command,
        "runner_sha256": sha(Path(__file__)),
        "status": "RUNNING",
        "limitations": [
            "Focused diagnostic only; does not establish scientific claim support or full QC.",
            "Native reference output counts issues; actual assertion coverage is measured separately by the maintained adapter.",
        ],
    }
    receipt.write_text(json.dumps(result, indent=2) + "\n")
    with log.open("x") as stream:
        run = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT)
    after = inputs(record)
    result.update(
        finished_at=now(),
        exit_code=run.returncode,
        status="PASSED" if run.returncode == 0 else "FAILED",
        log=str(log.relative_to(ROOT)),
        log_sha256=sha(log),
        log_bytes=log.stat().st_size,
        inputs_unchanged=after == bound,
    )
    if cache_copy:
        result["private_cache_unchanged"] = all(
            sha(cache_copy / Path(name).name) == bound[name]
            for name in [*CACHES.values(), *EXTRA_CACHES]
        )
    if record_copy:
        result["private_record_sha256"] = sha(record_copy)
        if result["private_record_sha256"] != bound[record]:
            raise ValueError("network diagnostic input changed")
    if after != bound or (cache_copy and not result["private_cache_unchanged"]):
        result["status"] = "INPUTS_CHANGED"
    receipt.write_text(json.dumps(result, indent=2) + "\n")
    code_path.write_text(str(run.returncode) + "\n")
    print(json.dumps({key: result[key] for key in ("name", "exit_code", "status", "log_bytes")}))
    sys.exit(run.returncode if result["status"] != "INPUTS_CHANGED" else 2)


if __name__ == "__main__":
    main()
