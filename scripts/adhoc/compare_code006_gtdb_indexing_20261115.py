"""Compare code006 test and native CLI GTDB lookup collection, 2026-11-15.

Inputs: unchanged c9 record/classifier/test bytes, pinned761 table and existing
local NCBI adapter. Output: JSON stdout only for #2848. No acquisition, source
mutation, candidates, or scientific approval. --record supplies the live canary.
"""

import argparse
import hashlib
import importlib.util
import json
import os
import socket
import subprocess
from collections import Counter
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]
BASE = "c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a"
TABLE = ROOT / ".temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT).strip()


def deny_network(*_args, **_kwargs):
    raise RuntimeError("network acquisition prohibited")


def wanted(module, occurrences, native):
    ids, species, higher = set(), set(), set()
    for item in occurrences:
        tid, label = item["id"], item["label"]
        if not tid.startswith("NCBITaxon:"):
            continue
        clean = module._clean_label(label)
        if native:
            if module._is_species(clean):
                ids.add(tid.split(":", 1)[1])
                species.update(module.lookup_keys(label))
            elif clean:
                higher.update(module.lookup_keys(label))
        else:
            ids.add(tid.split(":")[1])
            (species if " " in clean else higher).add(clean.lower())
    return ids, species, higher


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--record")
    args = parser.parse_args()
    head = git("rev-parse", "HEAD").decode()
    source = ROOT / "scripts/gtdb_ground.py"
    test = ROOT / "tests/test_gtdb_coherence_validator.py"
    inventory = (
        git("ls-tree", "-r", "--name-only", BASE, "kb/communities", "data/isolates")
        .decode()
        .splitlines()
    )
    inventory = sorted(p for p in inventory if p.endswith(".yaml"))
    if args.record and args.record not in inventory:
        raise ValueError("record is outside exact baseline inventory")
    selected = [args.record] if args.record else inventory
    inputs = {p: sha(p) for p in (source, test, Path(__file__), TABLE)}
    if inputs[TABLE] != TABLE_SHA:
        raise ValueError("exact pinned mapping required")
    for path in (source, test, *(ROOT / name for name in selected)):
        # Preserve exact Git bytes, including final whitespace.
        baseline = subprocess.check_output(
            ["git", "show", f"{BASE}:{path.relative_to(ROOT)}"], cwd=ROOT
        )
        if path.read_bytes() != baseline:
            raise ValueError("selected input differs from frozen baseline")
        inputs[path] = sha(path)
    spec = importlib.util.spec_from_file_location("native_gtdb_indexing", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    occurrences = []
    for name in selected:
        doc = yaml.safe_load((ROOT / name).read_bytes())
        for index, entry in enumerate(doc.get("taxonomy") or []):
            block = entry.get("taxon_term") or {}
            term = block.get("term") or {}
            occurrences.append(
                {
                    "record": name,
                    "record_id": doc["id"],
                    "selector": f"taxonomy[{index}].taxon_term",
                    "id": str(term.get("id", "")),
                    "label": term.get("label", ""),
                    "block": block,
                }
            )
    wanted_sets = {
        mode: wanted(module, occurrences, native=mode == "native_cli")
        for mode in ("legacy_test", "native_cli")
    }
    # Each native collect_rows index is keyed independently. One union scan,
    # then exact key subsets, produces the same per-mode rows without two reads.
    union = [set().union(*(groups[i] for groups in wanted_sets.values())) for i in range(3)]
    all_rows = module.collect_rows(TABLE, *union)
    rows = {
        mode: tuple(
            {key: values for key, values in all_rows[i].items() if key in groups[i]}
            for i in range(3)
        )
        for mode, groups in wanted_sets.items()
    }
    database = Path.home() / ".data/oaklib/ncbitaxon.db"
    stat = database.stat()
    if not stat.st_size:
        raise ValueError("nonempty local NCBI adapter required")
    differences, discrepancies = [], {mode: [] for mode in rows}
    with patch.dict(os.environ, {"PYSTOW_HOME": str(database.parents[1])}):
        with patch.object(socket.socket, "connect", deny_network):
            from communitymech import ontology_adapters

            local = ontology_adapters._local_build("ncbitaxon")
            if local is None:
                raise ValueError("native local NCBI adapter unavailable")
            with patch.object(ontology_adapters, "_local_build", return_value=local):
                for item in occurrences:
                    block = item["block"]
                    identity = {k: v for k, v in item.items() if k != "block"}
                    outcomes = {}
                    for mode, indexes in rows.items():
                        status, candidates = module.classify_status(
                            Path(item["record"]).name,
                            item["id"],
                            item["label"],
                            "gtdb_classification" in block,
                            *indexes,
                            preferred=block.get("preferred_term"),
                        )
                        outcomes[mode] = {"status": status, "candidates": sorted(candidates)}
                        errors = []
                        if status != block.get("gtdb_grounding_status"):
                            errors.append("status")
                        if sorted(block.get("gtdb_candidates") or []) != sorted(candidates):
                            errors.append("candidates")
                        if errors:
                            discrepancies[mode].append(
                                {
                                    **identity,
                                    "error_kinds": errors,
                                    "stored_status": block.get("gtdb_grounding_status"),
                                    "stored_candidates": sorted(block.get("gtdb_candidates") or []),
                                    **outcomes[mode],
                                }
                            )
                    if outcomes["legacy_test"] != outcomes["native_cli"]:
                        differences.append({**identity, **outcomes})
    end = database.stat()
    if (stat.st_size, stat.st_mtime_ns) != (end.st_size, end.st_mtime_ns):
        raise ValueError("local NCBI adapter changed")
    if inputs != {p: sha(p) for p in inputs} or head != git("rev-parse", "HEAD").decode():
        raise ValueError("inputs changed during read-only comparison")
    summary = {
        mode: {
            "discrepancy_rows": sum(len(row["error_kinds"]) for row in values),
            "taxonomy_occurrences": len(values),
            "record_files": len({row["record"] for row in values}),
            "status_transitions": dict(
                Counter(
                    f'{r["stored_status"]}->{r["status"]}'
                    for r in values
                    if "status" in r["error_kinds"]
                )
            ),
        }
        for mode, values in discrepancies.items()
    }
    print(
        json.dumps(
            {
                "source_revision": BASE,
                "execution_revision": head,
                "helper": str(Path(__file__).relative_to(ROOT)),
                "inputs": {str(p.relative_to(ROOT)): h for p, h in inputs.items()},
                "expected_records": len(inventory),
                "selected_records": len(selected),
                "taxonomy_occurrences": len(occurrences),
                "summary": summary,
                "indexing_differences": differences,
                "discrepancies": discrepancies,
                "inputs_unchanged": True,
                "local_ncbi_stat_unchanged": True,
                "limitation": "Read-only native classification comparison, not a curation plan or scientific review. Existing manual holds and blocks are passed unchanged to classify_status.",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
