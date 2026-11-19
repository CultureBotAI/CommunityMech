"""Run one native focused gate for the linked Phase2 cohort, 2026-11-15.

Inputs: current target, pinned native source/config, installed frozen environment.
Outputs: unique private log/receipt/exit and hashes. No provider enrichment or
canonical cache writes: reference validation uses a verified private cache copy
and --no-full-text; preflight requires every referenced source already loaded.
Serves #2674/#2774/#2806. Focused gates do not imply full QC or source truth.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_reference_validator.models import ReferenceValidationConfig

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/phase2-science-20261115"
TARGETS = {
    "ecofab": "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml",
    "dopamine": "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml",
    "lbnl": "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml",
}
CACHES = {
    "PMID:36472419": "references_cache/PMID_36472419.txt",
    "PMID:40920748": "references_cache/PMID_40920748.md",
    "PMID:42660928": "references_cache/PMID_42660928.md",
    "doi:10.1126/sciadv.adg7888": "references_cache/doi_10.1126_sciadv.adg7888.md",
}
GATE_RECIPES = {
    "schema": "validate",
    "strict": "validate-strict",
    "gtdb": "validate-gtdb",
    "domain": "validate-gtdb-domain",
    "scalars": "validate-scalars",
    "terms": "validate-terms",
    "history": "validate-history",
}
REQUIRED_ONTOLOGIES = frozenset({"NCBITaxon", "ENVO", "PO", "UBERON", "CHEBI", "GO"})
LOCAL_ONTOLOGIES = {
    prefix: Path("/Users/marcin/.data/oaklib") / (prefix.lower() + ".db")
    for prefix in REQUIRED_ONTOLOGIES
}


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def ontology_manifest(adapters):
    """Bind explicit adapters; a partial map disables native fallback (#2817)."""
    missing = REQUIRED_ONTOLOGIES - set(adapters)
    if missing:
        raise ValueError("missing required ontology prefixes: " + ", ".join(sorted(missing)))
    if any(not Path(path).is_file() for path in adapters.values()):
        raise ValueError("local ontology adapter prerequisite is missing")
    return {
        prefix: {"filename": Path(path).name, "sha256": sha(Path(path))}
        for prefix, path in sorted(adapters.items())
    }


def prepare_ontology_config(path, adapters):
    if path.exists():
        raise ValueError("exclusive ontology config already exists")
    manifest = ontology_manifest(adapters)
    with path.open("x") as stream:
        yaml.safe_dump(
            {"ontology_adapters": {key: "sqlite:" + str(value) for key, value in adapters.items()}},
            stream,
        )
    return manifest


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


def inputs():
    names = [
        *TARGETS.values(),
        "uv.lock",
        "justfile",
        "conf/reference_validator.yaml",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "src/communitymech/schema/history.yaml",
        "src/communitymech/validators/related_communities.py",
        "scripts/validate_strict.py",
        *CACHES.values(),
    ]
    for target in TARGETS.values():
        history = ROOT / "history/records" / Path(target).stem
        names.extend(str(path.relative_to(ROOT)) for path in history.glob("*.yaml"))
    return {name: sha(ROOT / name) for name in sorted(names)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gate", choices=[*GATE_RECIPES, "references", "network"])
    parser.add_argument("--record", choices=TARGETS, required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument(
        "--name", required=True, help="new receipt basename, e.g. linked-ecofab-scalars-001"
    )
    args = parser.parse_args()
    prefix = f"linked-{args.record}-{args.gate}-"
    if not args.name.replace("-", "").isalnum() or not args.name.startswith(prefix):
        raise ValueError("unsafe receipt name")
    if not re.fullmatch(r"[0-9a-f]{40}", args.expected_revision):
        raise ValueError("expected revision must be the full reviewed commit")
    target = TARGETS[args.record]
    history = str(Path("history/records") / Path(target).stem)
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if revision != args.expected_revision:
        raise ValueError("unexpected checkout revision; rebind gate run before continuing")
    receipt = STATE / (args.name + ".json")
    log = STATE / (args.name + ".log")
    code_path = STATE / (args.name + ".exit")
    if any(path.exists() for path in (receipt, log, code_path)):
        raise ValueError("refusing to replace a retained native run")
    bound = inputs()
    command = (
        [
            "just",
            "--no-dotenv",
            GATE_RECIPES[args.gate],
            history if args.gate == "history" else target,
        ]
        if args.gate in GATE_RECIPES
        else None
    )
    if args.gate == "strict":
        command = command + ["--out", str((STATE / (args.name + ".tsv")).relative_to(ROOT))]
    cache_copy = None
    record_copy = None
    ontology_inputs = None
    if args.gate == "terms":
        config_path = STATE / (args.name + "-oak.yaml")
        ontology_inputs = prepare_ontology_config(config_path, LOCAL_ONTOLOGIES)
        command = [
            "uv",
            "run",
            "--no-sync",
            "linkml-term-validator",
            "validate-data",
            target,
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
        record_copy = record_directory / Path(target).name
        record_copy.write_bytes((ROOT / target).read_bytes())
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
        identifiers = set(references(yaml.safe_load((ROOT / target).read_bytes())))
        if not identifiers or not identifiers <= set(CACHES):
            raise ValueError("source list changed; inspect sources before native validation")
        cache_copy = STATE / (args.name + "-cache")
        cache_copy.mkdir()
        for relative in CACHES.values():
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
            target,
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
        UV_NO_SYNC="1",
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
        "record": target,
        "record_worktree_sha256": bound[target],
        "inputs": bound,
        "command": command,
        "runner_sha256": sha(Path(__file__)),
        "status": "RUNNING",
        "limitations": [
            "Focused diagnostic only; does not establish scientific claim support or full QC.",
            "SupportingReference coverage depends on the recorded shared-schema bytes; validator output is not manual source assessment.",
            "The related-community policy is pinned by source hash; final integrated policy validation remains a separate check if this worktree has older code.",
        ],
    }
    if ontology_inputs is not None:
        from linkml_term_validator import validator as term_validator

        result["ontology_inputs"] = ontology_inputs
        result["ontology_config_sha256"] = sha(config_path)
        result["native_term_validator_sha256"] = sha(Path(term_validator.__file__))
    receipt.write_text(json.dumps(result, indent=2) + "\n")
    with log.open("x") as stream:
        run = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT)
    after = inputs()
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
            sha(cache_copy / Path(name).name) == bound[name] for name in CACHES.values()
        )
    if record_copy:
        result["private_record_sha256"] = sha(record_copy)
        if result["private_record_sha256"] != bound[target]:
            raise ValueError("network diagnostic input changed")
    if ontology_inputs is not None:
        result["ontology_inputs_unchanged"] = (
            ontology_manifest(LOCAL_ONTOLOGIES) == ontology_inputs
            and sha(config_path) == result["ontology_config_sha256"]
        )
    if (
        after != bound
        or (cache_copy and not result["private_cache_unchanged"])
        or result.get("ontology_inputs_unchanged") is False
    ):
        result["status"] = "INPUTS_CHANGED"
    receipt.write_text(json.dumps(result, indent=2) + "\n")
    code_path.write_text(str(run.returncode) + "\n")
    print(json.dumps({key: result[key] for key in ("name", "exit_code", "status", "log_bytes")}))
    sys.exit(run.returncode if result["status"] != "INPUTS_CHANGED" else 2)


if __name__ == "__main__":
    main()
