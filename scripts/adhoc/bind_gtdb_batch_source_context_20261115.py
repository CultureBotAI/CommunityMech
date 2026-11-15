"""Bind reviewed source context to a complete native route report, 2026-11-15.

Inputs: exact authored max10 config, completed reporter triplet and all its
retained inputs, primary caches, local readonly NCBI SQLite. JSON stdout for
#2848; no acquisition, file writes, native application or scientific clearance.
Executed inspectors and staging helpers remain unchanged.
"""

import argparse
import hashlib
import json
import re
import sqlite3
import subprocess
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
HELPER = "scripts/adhoc/bind_gtdb_batch_source_context_20261115.py"
REPORTER = "scripts/adhoc/report_gtdb_batch_routes_20261115.py"
REPORTER_SHA = "2d4732edafccba24741b728b9e672ca7fada5e50d8220162a9ccf3c5d8d875ef"
NATIVE_SHA = "0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def head():
    return git("rev-parse", "HEAD").decode().strip()


def local(name):
    if not isinstance(name, str) or Path(name).is_absolute() or ".." in Path(name).parts:
        raise ValueError("relative input required")
    path = ROOT / name
    if path.resolve() != path.absolute() or not path.is_file():
        raise ValueError("missing or symlinked input")
    path.resolve().relative_to(ROOT.resolve())
    return path


def db_stat(database):
    result = {}
    for suffix in ("", "-wal", "-shm", "-journal"):
        path = database.with_name(database.name + suffix)
        stat = path.stat() if path.exists() else None
        result[suffix or "database"] = (
            [stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns]
            if stat
            else None
        )
    if result["database"] is None or result["database"][2] == 0:
        raise ValueError("existing nonempty NCBI database required")
    return result


def identity(connection, term, rank):
    rows = [
        dict(row)
        for row in connection.execute(
            "SELECT subject,predicate,value,object FROM statements WHERE subject=? "
            "AND (predicate='rdfs:label' OR predicate LIKE '%Synonym%' "
            "OR predicate LIKE '%rank%' OR predicate='rdfs:subClassOf') "
            "ORDER BY predicate,value,object",
            (term["id"],),
        )
    ]
    labels = {row["value"] for row in rows if row["predicate"] == "rdfs:label"}
    ranks = {row["object"] for row in rows if row["predicate"].endswith("rank")}
    if labels != {term["label"]} or ranks != {rank}:
        raise ValueError("local NCBI label/rank differs")
    return rows


def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("explicit authored " + label + " required")
    return value


def bind(config_path, config_sha, expected_revision, database):
    if not re.fullmatch(r"[a-f0-9]{40}", expected_revision) or head() != expected_revision:
        raise ValueError("exact current revision required")
    captures = {}

    def read(name, expected=None):
        path = local(name)
        if path not in captures:
            captures[path] = path.read_bytes()
        raw = captures[path]
        if expected is not None and sha(raw) != expected:
            raise ValueError("bound input differs: " + name)
        return raw

    def artifact(item):
        if set(item) != {"path", "sha256"}:
            raise ValueError("exact artifact path/hash required")
        return read(item["path"], item["sha256"])

    config = json.loads(read(config_path, config_sha))
    raw_report = artifact(config["route_report"])
    routes = json.loads(raw_report)
    receipt = json.loads(artifact(config["route_receipt"]))
    started = datetime.fromisoformat(receipt["started_at"])
    finished = datetime.fromisoformat(receipt["finished_at"])
    if (
        artifact(config["route_exit"]) != b"0\n"
        or started.utcoffset() is None
        or finished.utcoffset() is None
        or finished < started
        or type(receipt["exit_code"]) is not int
        or receipt["exit_code"] != 0
        or receipt["status"] != "PASSED"
        or receipt["log_sha256"] != sha(raw_report)
        or receipt["log_bytes"] != len(raw_report)
        or receipt["head"] != routes["execution_revision"]
        or routes["kind"] != "read_only_native_route_report"
        or routes["inputs_unchanged"] is not True
        or routes["canonical_writes"] is not False
        or routes["scientific_review"] is not False
        or routes["ncbi_database"]["stat_unchanged"] is not True
    ):
        raise ValueError("completed native reporter triplet required")
    command = receipt["command"]
    if command[:2] != [".venv/bin/python", REPORTER]:
        raise ValueError("exact native reporter invocation required")
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--mapping", required=True)
    parser.add_argument("--record-id")
    parser.add_argument("--ncbi-db")
    args = parser.parse_args(command[2:])
    inputs = routes["inputs"]
    if (
        args.expected_revision != routes["execution_revision"]
        or args.record_id != routes["record_id_filter"]
        or args.plan_sha256 != routes["plan_sha256"]
        or inputs[args.plan] != args.plan_sha256
        or inputs[args.mapping] != TABLE_SHA
        or inputs[REPORTER] != REPORTER_SHA
        or inputs["scripts/gtdb_ground.py"] != NATIVE_SHA
        or sha(git("show", f"{args.expected_revision}:{REPORTER}")) != REPORTER_SHA
    ):
        raise ValueError("reporter invocation or published source binding differs")
    for name, expected in inputs.items():
        read(name, expected)
    read(HELPER)
    requested = config["records"]
    if not 1 <= len(requested) <= 10:
        raise ValueError("one to ten authored whole records required")
    if len({r["record_id"] for r in requested}) != len(requested):
        raise ValueError("duplicate authored record")
    route_rows = {r["record_id"]: r for r in routes["records"]}
    if (
        len(route_rows) != len(routes["records"])
        or len(route_rows) != routes["selected_record_count"]
        or len({r["record"] for r in routes["records"]}) != len(route_rows)
    ):
        raise ValueError("native record inventory differs")
    canonical_paths = {r["record"] for r in routes["records"]}
    common = set(inputs) - canonical_paths
    common.update([config_path, HELPER])
    common.update(config[key]["path"] for key in ("route_report", "route_receipt", "route_exit"))
    result = []
    database = database.expanduser().resolve(strict=True)
    before_stat = db_stat(database)
    with sqlite3.connect(database.as_uri() + "?mode=ro", uri=True) as connection:
        connection.row_factory = sqlite3.Row
        for selected in requested:
            route = route_rows[selected["record_id"]]
            if any(selected[k] != route[k] for k in ("record", "before_sha256")):
                raise ValueError("authored predecessor differs from native report")
            raw = read(route["record"], route["before_sha256"])
            doc = yaml.safe_load(raw)
            unit_inputs = common | {route["record"]}
            for name, expected in selected["additional_inputs"].items():
                read(name, expected)
                unit_inputs.add(name)
            sources, contexts = [], []
            if not selected["primary_sources"]:
                raise ValueError("explicit primary source context required")
            for source in selected["primary_sources"]:
                text = read(source["path"], source["sha256"]).decode()
                unit_inputs.add(source["path"])
                for key in ("reference", "locator", "coverage"):
                    nonempty(source.get(key), key)
                for key in ("identity_tokens", "anchors"):
                    if not isinstance(source[key], list) or not source[key]:
                        raise ValueError("source identity and anchors required")
                    if any(nonempty(token, key) not in text for token in source[key]):
                        raise ValueError("primary source identity or anchor absent")
                sources.append(source)
                for anchor in source["anchors"]:
                    offset = text.index(anchor)
                    contexts.append(
                        {
                            "reference": source["reference"],
                            "path": source["path"],
                            "anchor": anchor,
                            "character_offset": offset,
                            "line": text.count("\n", 0, offset) + 1,
                        }
                    )
            seen, occurrences = set(), []
            if not selected["occurrences"]:
                raise ValueError("explicit selected occurrence required")
            for authored in selected["occurrences"]:
                index = authored["taxonomy_index"]
                if type(index) is not int or index < 0 or index in seen:
                    raise ValueError("unique explicit occurrence required")
                seen.add(index)
                matches = [r for r in route["occurrences"] if r["taxonomy_index"] == index]
                if len(matches) != 1:
                    raise ValueError("selected occurrence absent or repeated")
                observed = matches[0]
                for key in ("term", "strain_name", "native_result", "classify_status"):
                    if authored[key] != observed[key]:
                        raise ValueError("authored occurrence differs from actual native result")
                member = doc["taxonomy"][index]
                if (
                    member["taxon_term"] != observed["existing_descriptor"]
                    or member.get("strain_designation", {}).get("strain_name")
                    != observed["strain_name"]
                    or doc["id"] != selected["record_id"]
                ):
                    raise ValueError("native occurrence differs from captured canonical bytes")
                judgments = {
                    key: nonempty(authored.get(key), key)
                    for key in ("source_assessment", "population_scope", "name_scope")
                }
                occurrences.append(
                    {
                        **observed,
                        **judgments,
                        "ncbi_identity_rows": identity(
                            connection, observed["term"], authored["expected_ncbi_rank"]
                        ),
                    }
                )
            result.append(
                {
                    "record": route["record"],
                    "record_id": route["record_id"],
                    "before_sha256": route["before_sha256"],
                    "input_paths": sorted(unit_inputs),
                    "occurrences": occurrences,
                    "primary_sources": sources,
                    "primary_contexts": contexts,
                    "historical_guard_assessment": nonempty(
                        selected["historical_guard_assessment"], "historical guard assessment"
                    ),
                }
            )
    if db_stat(database) != before_stat:
        raise ValueError("local authority database stat changed")
    if (
        any(path.read_bytes() != raw for path, raw in captures.items())
        or head() != expected_revision
    ):
        raise ValueError("captured source or revision changed")
    return {
        "revision": expected_revision,
        "records": result,
        "route_report": config["route_report"],
        "route_execution_revision": routes["execution_revision"],
        "inputs": {str(path.relative_to(ROOT)): sha(raw) for path, raw in captures.items()},
        "inputs_unchanged": True,
        "canonical_writes": False,
        "scientific_review": False,
        "database_observation": {
            "stat": before_stat,
            "stat_unchanged": True,
            "content_sha256": None,
        },
        "scope": (
            "Authored source context bound to retained native routes and current local label/rank. "
            "No reclassification of study stocks, application approval or scientific clearance. "
            "Per-unit inputs exclude unrelated canonical records merely reported alongside this unit; "
            "explicit additional cross-record dependencies remain included. Null routes and manual "
            "holds are retained and do not imply support by the current staging engine."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--expected-config-sha256", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--ncbi-db", type=Path, default=Path.home() / ".data/oaklib/ncbitaxon.db")
    args = parser.parse_args()
    print(
        json.dumps(
            bind(args.config, args.expected_config_sha256, args.expected_revision, args.ncbi_db),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
