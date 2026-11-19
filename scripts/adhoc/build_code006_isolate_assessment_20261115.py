"""Build a scoped isolate correspondence assessment from actual receipts.

#2848, 2026-11-15. Inputs: exact original-basename stage/application, native
gate artifacts, primary source, immutable historical review and recomputation.
Outputs: exclusive private inspect/draft; native save remains a separate step.
No canonical writes, network, historical edits or full scientific approval.
"""

import argparse
import hashlib
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"
sys.path.insert(0, str(ROOT / "tests"))
from batch147_genus_successor import TARGETS, unchanged_science  # noqa: E402

PREVIOUS = "20261111T121000Z-c15s4-record-deep-audit"
SUFFIXES = (".command.txt", ".log", ".exit", ".start.txt", ".finished.txt", ".log.sha256")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


class CapturedInputs:
    """Assess/hash one snapshot and reject drift or a different native inspection (#2864)."""

    def __init__(self):
        self.raw = {}

    def read(self, path):
        path = Path(path).resolve()
        if path not in self.raw:
            self.raw[path] = path.read_bytes()
        return self.raw[path]

    def text(self, path):
        return self.read(path).decode()

    def sha(self, path):
        return hashlib.sha256(self.read(path)).hexdigest()

    def verify(self, inspection=None):
        if any(path.read_bytes() != raw for path, raw in self.raw.items()):
            raise ValueError("input changed after assessment snapshot")
        if inspection is not None:
            native = {row["path"]: row["sha256"] for row in inspection["source"]["inputs"]}
            for path in self.raw:
                if native.get(str(path.relative_to(ROOT))) != self.sha(path):
                    raise ValueError("native inspection differs from assessed snapshot")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", choices=["000552", "000553"], required=True)
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--application-sha256", required=True)
    args = parser.parse_args()
    output = STATE / f"isolate-{args.record}-assessment-{args.attempt}"
    if not args.attempt.isdigit() or output.exists() or head() != args.expected_revision:
        raise ValueError("exact revision and exclusive numeric namespace required")
    captured = CapturedInputs()
    read, text, digest = captured.read, captured.text, captured.sha
    read(Path(__file__))
    read(ROOT / "tests/batch147_genus_successor.py")
    path, values = next(
        (path, values) for path, values in TARGETS.items() if values[0].endswith(args.record)
    )
    identity, ncbi, label, count = values
    applied_path = STATE / f"isolate-{args.record}-applied-001/receipt.json"
    raw = read(applied_path)
    if hashlib.sha256(raw).hexdigest() != args.application_sha256:
        raise ValueError("external actual application hash differs")
    applied = json.loads(raw)
    before = applied_path.with_name("before.yaml")
    if (
        applied["applied"] is not True
        or applied["target"] != path
        or applied["execution_revision"] != args.expected_revision
        or digest(ROOT / path) != applied["after_sha256"]
        or digest(before) != applied["before_sha256"]
    ):
        raise ValueError("exact actual application chain differs")
    unchanged_science(yaml.safe_load(read(before)), yaml.safe_load(read(ROOT / path)), path)
    stage = STATE / f"isolate-{args.record}-candidate-001/receipt.json"
    staged = json.loads(read(stage))
    if (
        digest(stage) != applied["reviewed_receipt_sha256"]
        or digest(stage.with_name(Path(path).name)) != applied["after_sha256"]
        or digest(stage.with_name("native.log")) != staged["native_log_sha256"]
        or staged["exit_codes"] != [0, 0]
    ):
        raise ValueError("original reviewed native candidate differs")
    paths = {
        ROOT / path,
        applied_path,
        before,
        stage,
        stage.with_name(Path(path).name),
        stage.with_name("native.log"),
        stage.with_name("native.exit"),
        Path(__file__),
        ROOT / "tests/batch147_genus_successor.py",
        ROOT / "scripts/adhoc/check_code006_isolate_genus_20261115.sh",
        ROOT / "scripts/adhoc/recompute_code006_isolate_genus_20261115.py",
        ROOT / "src/communitymech/schema/communitymech.yaml",
        ROOT / "uv.lock",
        ROOT / f"reviews/structured/{PREVIOUS}/review.yaml",
        ROOT / f"reviews/structured/{PREVIOUS}/review.md",
        STATE / f"isolate-{args.record}-strict-001.tsv",
    }
    for name, expected in {**applied["inputs"], **applied["implementation"]}.items():
        if name == path:
            continue
        if digest(ROOT / name) != expected:
            raise ValueError("reviewed source/implementation changed")
        paths.add(ROOT / name)
    history = ROOT / "history/records" / Path(path).stem
    paths.update(history.glob("*.yaml"))
    accessed = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    evidence, checks = [], []

    def add_evidence(key, kind, source, summary, support="supports"):
        evidence.append(
            {
                "evidence_id": key,
                "kind": kind,
                "reference": str(source.relative_to(ROOT)),
                "accessed_at": accessed,
                "support": support,
                "summary": summary,
            }
        )

    recipes = {
        "schema": "validate",
        "strict": "validate-strict",
        "gtdb": "validate-gtdb",
        "domain": "validate-gtdb-domain",
        "scalars": "validate-scalars",
        "history": "validate-history",
    }
    for gate in [*recipes, "completion", "new-history"]:
        prefix = STATE / f"isolate-{args.record}-run-{gate}-001"
        command, log, exit_path, start, finished, log_sha = [
            Path(str(prefix) + suffix) for suffix in SUFFIXES
        ]
        argv = shlex.split(text(command))
        if (
            text(exit_path).strip() != "0"
            or not read(log)
            or digest(log) != text(log_sha).split()[0]
            or text(start).splitlines()[:2] != [args.expected_revision, "Python 3.13.2"]
            or not text(finished).strip()
        ):
            raise ValueError("native gate receipt is incomplete or inconsistent")
        if gate == "completion":
            expected = [
                "uv",
                "run",
                "pytest",
                "tests/test_gtdb_coherence_validator.py::test_the_status_distribution_is_what_was_measured",
                "tests/test_gtdb_not_attempted.py::test_no_taxon_is_silently_outstanding",
                "-q",
            ]
            if "2 passed" not in text(log):
                raise ValueError("both native completion tests must pass")
        elif gate == "new-history":
            if (
                argv[:6] != ["just", "--verbose", "--no-dotenv", "--color", "never", "new-history"]
                or Path(path).stem not in argv
                or "data/isolates" not in argv
            ):
                raise ValueError("native sidecar command differs")
            sidecars = [
                item for item in history.glob("*.yaml") if str(item.relative_to(ROOT)) in text(log)
            ]
            if len(sidecars) != 1:
                raise ValueError("one actual persisted native sidecar required")
            sidecar = sidecars[0]
            doc = yaml.safe_load(read(sidecar))
            if doc["target"]["path"] != path or applied["after_sha256"] not in text(sidecar):
                raise ValueError("sidecar target/application binding differs")
            paths.update((command, log, exit_path, start, finished, log_sha))
            continue
        else:
            expected = [
                "just",
                "--verbose",
                "--no-dotenv",
                "--color",
                "never",
                recipes[gate],
                str(history.relative_to(ROOT)) if gate == "history" else path,
            ]
            if gate == "strict":
                expected += [
                    "--out",
                    f".temp/gtdb-code006-20261115/isolate-{args.record}-strict-001.tsv",
                ]
        if argv != expected:
            raise ValueError("actual gate command differs")
        paths.update((command, log, exit_path, start, finished, log_sha))
        summary = (
            "Both unchanged native outstanding-grounding tests passed; not full QC."
            if gate == "completion"
            else "Actual scoped native gate passed with a nonempty hash-verified log."
        )
        add_evidence(gate, "validation", log, summary)
        checks.append(
            {
                "check_id": gate,
                "name": gate,
                "status": "passed",
                "required": True,
                "summary": summary,
                "target_ids": [identity],
                "command": text(command).strip(),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": [gate],
            }
        )
    route_path = STATE / f"isolate-{args.record}-native-recomputation-001.json"
    route = json.loads(read(route_path))
    if (
        route["target"] != path
        or route["record_sha256"] != applied["after_sha256"]
        or route["revision"] != args.expected_revision
        or route["matches_corrected_block"] is not True
        or route["inputs_unchanged"] is not True
        or route["block"] != staged["native_block"]
    ):
        raise ValueError("native post-apply recomputation differs")
    paths.add(route_path)
    terms_dir = STATE / f"isolate-{args.record}-terms-001"
    terms = json.loads(read(terms_dir / "receipt.json"))
    if (
        terms["target"] != path
        or terms["revision"] != args.expected_revision
        or terms["record_sha256"] != applied["after_sha256"]
        or terms["exit_code"] != 0
        or text(terms_dir / "native.exit").strip() != "0"
        or digest(terms_dir / "native.log") != terms["log_sha256"]
        or terms["inputs_unchanged"] is not True
        or digest(terms_dir / "oak.yaml") != terms["config_sha256"]
    ):
        raise ValueError("actual explicit-local-adapter term check differs")
    for name, expected in terms["inputs"].items():
        if digest(ROOT / name) != expected:
            raise ValueError("term input differs")
        paths.add(ROOT / name)
    paths.update(
        terms_dir / name for name in ("receipt.json", "native.log", "native.exit", "oak.yaml")
    )
    add_evidence(
        "terms",
        "validation",
        terms_dir / "native.log",
        "Native LTV binding/label check used explicit existing SQLite adapters and blocked network; database stat identities stayed unchanged, byte hashes were not measured.",
    )
    checks.append(
        {
            "check_id": "terms",
            "name": "Native LTV with explicit local adapters",
            "status": "passed",
            "required": True,
            "summary": evidence[-1]["summary"],
            "target_ids": [identity],
            "command": shlex.join(terms["native_argv"]),
            "exit_code": 0,
            "expected_exit_code": 0,
            "evidence_ids": ["terms"],
        }
    )
    add_evidence(
        "application",
        "record_content",
        applied_path,
        "Exact actual guarded application, retained original bytes and append-only history; biology outside the mapping/status is unchanged.",
    )
    add_evidence(
        "mapping",
        "database",
        route_path,
        f"Native same-genus {ncbi} correspondence to GTDB:g__{label}: {count}/{count} named reference genomes. This does not identify the study stock species or genome.",
    )
    add_evidence(
        "primary",
        "primary_source",
        ROOT / "references_cache/PMID_42666409.txt",
        "Existing primary Section3.1 supports the named genus of this study stock. This bounded check preserves all other source and biological assertions.",
    )
    add_evidence(
        "previous",
        "prior_review",
        ROOT / f"reviews/structured/{PREVIOUS}/review.yaml",
        "Immutable earlier full scientific review and all unresolved findings retained; this is not its replacement.",
        "context_only",
    )
    targets = [
        {
            "target_id": identity,
            "path": path,
            "label": f"{label} study-stock genus correspondence",
            "selector": "taxonomy[0].taxon_term",
            "kind": "maintained",
            "ownership_note": "CommunityMech owns this canonical isolate and its native source-grounding/history tooling.",
        }
    ]
    for item in paths:
        read(item)
    captured.verify()
    output.mkdir()
    (output / "targets.json").write_text(json.dumps({"targets": targets}, indent=2) + "\n")
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(output / "targets.json"),
    ]
    for item in sorted(paths):
        command += ["--input", str(item.relative_to(ROOT))]
    native_raw = subprocess.check_output(command, cwd=ROOT)
    inspection = json.loads(native_raw)
    captured.verify(inspection)
    (output / "inspection.json").write_bytes(native_raw)
    finished = datetime.now(timezone.utc)
    doc = {
        "schema_version": "1.0.0",
        "review_id": finished.strftime("%Y%m%dT%H%M%SZ") + f"-gtdb-genus-{args.record}-canary",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": f"Scoped technical correspondence: {label} isolate {args.record}",
        "started_at": applied["created_at"].replace("+00:00", "Z"),
        "finished_at": finished.isoformat().replace("+00:00", "Z"),
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored application and assessment; parent independently reviewed exact candidate, source limits and guard before application.",
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": False,
        "summary": f"One source-backed same-genus reference correspondence for {label} is now GROUNDED, with seven scoped gates and both unchanged completion tests passing. All biological payload, original stock identity and historical scientific findings remain unchanged; no full scientific review or corpus-QC pass is asserted.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "Only the database correspondence, guarded application/history chain and technical checks were assessed.",
            "selection": "Independently accepted pure same-name higher-rank isolate candidate; original basename and source identity retained.",
            "population_size": 1,
            "reviewed_target_ids": [identity],
            "coverage": "partial",
            "exclusions": [
                {
                    "target": "Other assigned records and unchanged biological claims",
                    "reason": "No wider or full scientific assessment was performed.",
                }
            ],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "genus-correspondence",
                "area": "grounding",
                "topic": "Same-genus database correspondence",
                "outcome": "supported",
                "target_ids": [identity],
                "evidence_ids": ["mapping", "primary", "application", "gtdb", "terms"],
                "summary": f"The existing declared {label} genus maps to GTDB:g__{label} at {count}/{count} named-binomial reference genomes, not reclassified. This database correspondence does not establish the exact study-stock species, genome or mechanisms.",
            },
            {
                "assessment_id": "historical-boundary",
                "area": "provenance",
                "topic": "Preserved biological bytes and earlier assessment",
                "outcome": "supported",
                "target_ids": [identity],
                "evidence_ids": ["previous", "application", "history", "completion"],
                "summary": "The exact old full record remains retained; only the genus block, GROUNDED status and two native inline events changed. Native sidecar and actual application evidence are bound. Earlier UNRESOLVED reflects the prior database result and is not overwritten in its immutable review. Historical scientific needs-curation findings remain open.",
            },
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Partial technical assessment only: no new full-paper/supplement review, reference sweep, stock genome/species inference, mechanism approval or scientific status promotion.",
            "The term check is the installed native CLI with explicit local NCBI/ENVO/CHEBI adapters, not literally the just validate-terms recipe. Adapter stat identities were checked; database byte hashes were not measured.",
            "Seven scoped gates and two outstanding-grounding tests passed; full corpus status reproducibility, historical successor acceptance and full QC are separate gates.",
            "Exact M5 native execution revision is recorded, with additional hashed orchestration helpers. No record or issue outside this target is declared completed.",
        ],
        "related_reviews": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "review_id": PREVIOUS,
                "relationship": "Additive technical correspondence preserves all original scientific findings and source/stock limitations; does not supersede the multi-record scientific assessment.",
            }
        ],
    }
    if (
        inspection["source"]["git_revision"] != args.expected_revision
        or head() != args.expected_revision
    ):
        raise ValueError("revision changed during assessment")
    captured.verify(inspection)
    (output / "review.json").write_text(json.dumps(doc, indent=2) + "\n")
    print(
        json.dumps(
            {
                "review": str((output / "review.json").relative_to(ROOT)),
                "sha256": sha(output / "review.json"),
            }
        )
    )


if __name__ == "__main__":
    main()
