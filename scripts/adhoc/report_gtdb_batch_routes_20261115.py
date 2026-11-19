"""Report complete native GTDB routes for an explicit bounded plan, 2026-11-15.

Inputs: reviewed JSON/YAML plan (records with record, record_id, before_sha256),
exact execution revision/native code, pinned761 crosswalk, existing local NCBI
SQLite. JSON stdout only for #2848; no writes, acquisition, or apply approval.
Use --record-id for one whole-record canary before the same-path max10 batch.
Database identity is stat-bound, not a content hash or ontology release claim.
"""

import argparse
import hashlib
import io
import json
import os
import platform
import re
import socket
import subprocess
import sys
import types
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]
HELPER = "scripts/adhoc/report_gtdb_batch_routes_20261115.py"
NATIVE = "scripts/gtdb_ground.py"
NATIVE_SHA = "0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
MODULES = {
    "communitymech": "src/communitymech/__init__.py",
    "communitymech.curate": "src/communitymech/curate/__init__.py",
    "communitymech.validators": "src/communitymech/validators/__init__.py",
    "communitymech.ontology_adapters": "src/communitymech/ontology_adapters.py",
    "communitymech.curate.curation_event": "src/communitymech/curate/curation_event.py",
    "communitymech.validators.ncbi_domain": "src/communitymech/validators/ncbi_domain.py",
    "native_gtdb_route_report": NATIVE,
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def revision():
    return git("rev-parse", "HEAD").decode().strip()


def relative_file(name):
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError("repository-relative file required")
    path = ROOT / name
    if ".." in Path(name).parts or path.resolve() != path.absolute():
        raise ValueError("unsafe or symlinked input path")
    path.resolve().relative_to(ROOT.resolve())
    if not path.is_file():
        raise ValueError("input file missing: " + name)
    return path


def database_identity(database):
    """Retain file identity/stat and SQLite companion state without hashing 13GB."""
    if database.name != "ncbitaxon.db" or database.parent.name != "oaklib":
        raise ValueError("explicit local oaklib/ncbitaxon.db required")
    result = {}
    for suffix in ("", "-wal", "-shm", "-journal"):
        path = database.with_name(database.name + suffix)
        if path.exists():
            stat = path.stat()
            result["database" + suffix] = {
                "device": stat.st_dev,
                "inode": stat.st_ino,
                "bytes": stat.st_size,
                "mtime_ns": stat.st_mtime_ns,
                "ctime_ns": stat.st_ctime_ns,
            }
        else:
            result["database" + suffix] = None
    if not result["database"] or not result["database"]["bytes"]:
        raise ValueError("nonempty local NCBI database required")
    return result


def deny_network(*_args, **_kwargs):
    raise RuntimeError("network is prohibited in the route reporter")


@contextmanager
def native_snapshot(captured, database):
    """Execute captured repository code, with one explicit local adapter only."""
    names = {}
    for name, relative in MODULES.items():
        module = types.ModuleType(name)
        module.__file__ = str(ROOT / relative)
        module.__package__ = name if relative.endswith("/__init__.py") else name.rpartition(".")[0]
        if relative.endswith("/__init__.py"):
            module.__path__ = [str((ROOT / relative).parent)]
        names[name] = module
    original_path = sys.path[:]
    try:
        with (
            patch.dict(sys.modules, names),
            patch.dict(os.environ, {"PYSTOW_HOME": str(database.parent.parent)}),
            patch.object(socket.socket, "connect", deny_network),
            patch.object(socket.socket, "connect_ex", deny_network),
            patch.object(socket, "create_connection", deny_network),
            patch.object(socket, "getaddrinfo", deny_network),
        ):
            for name, relative in MODULES.items():
                module = names[name]
                # Only exact Git-bound repository snapshots enter this static module list.
                exec(  # noqa: S102
                    compile(captured[ROOT / relative], module.__file__, "exec"), module.__dict__
                )
                parent, _, attribute = name.rpartition(".")
                if parent in names:
                    setattr(names[parent], attribute, module)
            adapters = names["communitymech.ontology_adapters"]
            local = adapters._local_build("ncbitaxon")
            if local is None:
                raise ValueError("native local NCBI adapter unavailable; no fallback allowed")
            with patch.object(adapters, "_local_build", return_value=local):
                yield names["native_gtdb_route_report"]
    finally:
        sys.path[:] = original_path


def wanted(native, occurrences):
    """Match the native CLI's rank-aware, both-spelling collection exactly."""
    ids, species, higher = set(), set(), set()
    for row in occurrences:
        term = row["existing_descriptor"]["term"]
        if not term["id"].startswith("NCBITaxon:"):
            continue
        label = term["label"]
        clean = native._clean_label(label)
        if native._is_species(clean):
            ids.add(term["id"].split(":", 1)[1])
            species.update(native.lookup_keys(label))
        elif clean:
            higher.update(native.lookup_keys(label))
    return ids, species, higher


def compute(native, table_bytes, records):
    occurrences = [item for row in records for item in row["occurrences"]]
    indexes = native.collect_rows(io.BytesIO(table_bytes), *wanted(native, occurrences))
    source_rows = {}

    def row_hashes(rows):
        hashes = []
        for cells in rows:
            key = digest(json.dumps(cells, separators=(",", ":"), ensure_ascii=False).encode())
            source_rows[key] = cells
            hashes.append(key)
        return hashes

    for row in records:
        for item in row["occurrences"]:
            block = item["existing_descriptor"]
            term = block["term"]
            tid, label = term["id"], term["label"]
            keys = wanted(native, [item])
            item["lookup_indexes"] = {
                kind: {key: row_hashes(index.get(key, [])) for key in sorted(selected)}
                for kind, index, selected in zip(
                    ("exact_ncbi_id", "ncbi_species_name", "ncbi_higher_name"),
                    indexes,
                    keys,
                    strict=True,
                )
            }
            result = (
                native.resolve_target(tid.split(":", 1)[1], label, *indexes)
                if tid.startswith("NCBITaxon:")
                else None
            )
            status, candidates = native.classify_status(
                Path(row["record"]).name,
                tid,
                label,
                "gtdb_classification" in block,
                *indexes,
                preferred=block.get("preferred_term"),
            )
            item.update(
                native_result=result,
                classify_status={"status": status, "candidates": candidates},
                manual_curated_reason=native.CURATED_GROUNDINGS.get(
                    (Path(row["record"]).name, tid)
                ),
                manual_withheld_reason=native.WITHHELD_GROUNDINGS.get(
                    (Path(row["record"]).name, block.get("preferred_term"))
                ),
            )
    return records, source_rows


def report(plan_path, plan_sha, expected_revision, mapping, database, record_id=None):
    if not re.fullmatch(r"[a-f0-9]{40}", expected_revision) or revision() != expected_revision:
        raise ValueError("exact current execution revision required")
    captured = {}

    def capture(relative):
        path = relative_file(relative)
        if path not in captured:
            captured[path] = path.read_bytes()
        return captured[path]

    raw_plan = capture(plan_path)
    if digest(raw_plan) != plan_sha:
        raise ValueError("reviewed plan hash differs")
    plan = yaml.safe_load(raw_plan)
    entries = plan.get("records") if isinstance(plan, dict) else None
    if not isinstance(entries, list) or not 1 <= len(entries) <= 10:
        raise ValueError("explicit plan of one to ten whole records required")
    seen_ids, seen_paths = set(), set()
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {"record", "record_id", "before_sha256"}:
            raise ValueError("route plan entries require only record, record_id, before_sha256")
        if not re.fullmatch(r"CommunityMech:\d{6}", str(entry["record_id"])):
            raise ValueError("canonical record identifier required")
        if not re.fullmatch(r"(?:kb/communities|data/isolates)/[^/]+\.yaml", entry["record"]):
            raise ValueError("canonical record path required")
        if not re.fullmatch(r"[a-f0-9]{64}", str(entry["before_sha256"])):
            raise ValueError("exact before hash required")
        if entry["record_id"] in seen_ids or entry["record"] in seen_paths:
            raise ValueError("duplicate whole record")
        seen_ids.add(entry["record_id"])
        seen_paths.add(entry["record"])
    selected = [r for r in entries if record_id is None or r["record_id"] == record_id]
    if not selected:
        raise ValueError("record-id is absent from explicit plan")
    for relative in (*MODULES.values(), "uv.lock", "pyproject.toml"):
        raw = capture(relative)
        if raw != git("show", f"{expected_revision}:{relative}"):
            raise ValueError("native dependency differs from execution revision: " + relative)
    if digest(captured[ROOT / NATIVE]) != NATIVE_SHA:
        raise ValueError("exact reviewed native classifier required")
    capture(HELPER)
    table_bytes = capture(mapping)
    if digest(table_bytes) != TABLE_SHA:
        raise ValueError("exact pinned761 mapping required")
    records = []
    for entry in selected:
        raw = capture(entry["record"])
        if digest(raw) != entry["before_sha256"]:
            raise ValueError("record before hash differs: " + entry["record"])
        doc = yaml.safe_load(raw)
        if doc["id"] != entry["record_id"]:
            raise ValueError("record identity differs")
        taxonomy = doc.get("taxonomy")
        if not isinstance(taxonomy, list) or not taxonomy:
            raise ValueError("nonempty whole-record taxonomy required")
        occurrences = []
        for index, member in enumerate(taxonomy):
            block = member["taxon_term"]
            term = block["term"]
            if not all(isinstance(term.get(key), str) and term[key] for key in ("id", "label")):
                raise ValueError("explicit stored term identity required")
            occurrences.append(
                {
                    "taxonomy_index": index,
                    "selector": f"taxonomy[{index}].taxon_term",
                    "term": term,
                    "strain_name": (member.get("strain_designation") or {}).get("strain_name"),
                    "existing_descriptor": block,
                }
            )
        records.append({**entry, "occurrences": occurrences})
    database = database.expanduser().resolve(strict=True)
    db_before = database_identity(database)
    with native_snapshot(captured, database) as native:
        results, source_rows = compute(native, table_bytes, records)
    if database_identity(database) != db_before:
        raise ValueError("local NCBI database stat changed")
    if any(path.read_bytes() != raw for path, raw in captured.items()):
        raise ValueError("captured route input changed")
    if revision() != expected_revision:
        raise ValueError("execution revision changed")
    return {
        "kind": "read_only_native_route_report",
        "scientific_review": False,
        "canonical_writes": False,
        "execution_revision": expected_revision,
        "python_version": platform.python_version(),
        "plan_sha256": plan_sha,
        "planned_record_count": len(entries),
        "selected_record_count": len(records),
        "record_id_filter": record_id,
        "records": results,
        "crosswalk_rows": source_rows,
        "crosswalk_row_encoding": (
            "Keys are SHA256 of UTF-8 compact JSON cells (ensure_ascii=false), not raw line "
            "hashes. Values retain every parsed crosswalk column. Per-occurrence indexes "
            "retain duplicate rows and every exact native lookup key. Native defaults are "
            "denominator=aggregate, exclude_unnamed=true; native_result carries its actual "
            "denominator, not a strain count. Index rows precede native rank/name filtering."
        ),
        "inputs": {str(p.relative_to(ROOT)): digest(raw) for p, raw in captured.items()},
        "inputs_unchanged": True,
        "ncbi_database": {"stat": db_before, "stat_unchanged": True, "content_sha256": None},
        "limitation": (
            "Native mapping/status computation only. No source interpretation, stock identity, "
            "candidate approval, application, validation gates or scientific clearance. "
            "All options and null results are retained; existing blocks/manual holds are passed "
            "to the classifier unchanged. NCBI database provenance is file stat only."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--mapping", required=True)
    parser.add_argument("--ncbi-db", type=Path, default=Path.home() / ".data/oaklib/ncbitaxon.db")
    parser.add_argument("--record-id")
    args = parser.parse_args()
    result = report(
        args.plan,
        args.plan_sha256,
        args.expected_revision,
        args.mapping,
        args.ncbi_db,
        args.record_id,
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
