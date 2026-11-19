"""Build the one-genus technical successor from real M5 receipts, #2848.

2026-11-15. Inputs: actual two-step application chain, unchanged scientific
predecessor, native gates/completion tests and exact table. Outputs: exclusive
private inspection/draft JSON only; native review save is a separate action.
"""

import argparse
import copy
import hashlib
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"
TARGET = "kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml"
REVISION = "956d00c6143020810ef7a60a6298e67fb0ee0caf"
AFTER = "c2cf66bb2d62e59ac75c16db1aa9598a33719c6461822ae237d44558c6c91ea9"
PREVIOUS = "20261115T050137Z-gtdb-status-000434-canary"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    args = parser.parse_args()
    output = STATE / f"genus-assessment-{args.attempt}"
    if not args.attempt.isdigit() or output.exists():
        raise ValueError("numeric exclusive assessment namespace required")
    applied_path = STATE / "genus-applied-001/receipt.json"
    if (
        sha(ROOT / TARGET) != AFTER
        or sha(applied_path) != "14a946e2082e7203b18b39d3c5862403c56eb47ee2844fb917b35b1b4d00123c"
        or subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        != REVISION
    ):
        raise ValueError("exact actual genus application required")
    applied = json.loads(applied_path.read_bytes())
    if (
        applied["applied"] is not True
        or applied["after_sha256"] != AFTER
        or applied["execution_revision"] != REVISION
    ):
        raise ValueError("actual receipt binding differs")
    if sha(applied_path.with_name("before.yaml")) != applied["before_sha256"]:
        raise ValueError("actual predecessor bytes differ")
    for name, expected in {**applied["inputs"], **applied["implementation"]}.items():
        if name != TARGET and sha(ROOT / name) != expected:
            raise ValueError("reviewed source/implementation changed")
    staged = STATE / "genus-candidate-001/receipt.json"
    if sha(staged) != applied["reviewed_receipt_sha256"]:
        raise ValueError("reviewed stage differs")
    old_draft = STATE / "assessment-draft-004.json"
    if sha(old_draft) != "a8e6a444cd2493a0d532a9b5f30c39a9348cdde81f7d82308b4498de6e69792d":
        raise ValueError("previous diagnostic content differs")
    doc = copy.deepcopy(json.loads(old_draft.read_bytes()))
    paths = {
        ROOT / TARGET,
        applied_path,
        applied_path.with_name("before.yaml"),
        staged,
        staged.with_name(Path(TARGET).name),
        old_draft,
        Path(__file__),
        ROOT / "scripts/adhoc/check_code006_genus_canary_20261115.sh",
        STATE / "genus-strict-001.tsv",
        STATE / "native-source-provenance-001.txt",
        ROOT / f"reviews/structured/{PREVIOUS}/review.yaml",
        ROOT / f"reviews/structured/{PREVIOUS}/review.md",
        ROOT / "src/communitymech/schema/communitymech.yaml",
        ROOT / "uv.lock",
        ROOT / "tests/test_gtdb_coherence_validator.py",
        ROOT / "tests/test_gtdb_not_attempted.py",
    }
    paths.update(
        ROOT / name for name in {**applied["inputs"], **applied["implementation"]} if name != TARGET
    )
    history = ROOT / "history/records/Acidic_Nitrification_Minimal_Consortium"
    paths.update(history.glob("*.yaml"))
    sidecar = history / "2026-11-15T051056Z-codex-79864e.yaml"
    if not sidecar.is_file() or not sidecar.stat().st_size:
        raise ValueError("actual new native sidecar required")
    new_history = STATE / "genus-canary-run-new-history-001"
    history_artifacts = [
        Path(str(new_history) + suffix)
        for suffix in (
            ".command.txt",
            ".log",
            ".exit",
            ".start.txt",
            ".finished.txt",
            ".log.sha256",
        )
    ]
    if (
        history_artifacts[2].read_text().strip() != "0"
        or str(sidecar.relative_to(ROOT)) not in history_artifacts[1].read_text()
        or sha(history_artifacts[1]) != history_artifacts[5].read_text().split()[0]
    ):
        raise ValueError("actual native new-history evidence differs")
    paths.update(history_artifacts)
    accessed = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    checks, evidence = [], []
    recipes = {
        "schema": "validate",
        "strict": "validate-strict",
        "gtdb": "validate-gtdb",
        "domain": "validate-gtdb-domain",
        "scalars": "validate-scalars",
        "history": "validate-history",
    }
    for gate, recipe in recipes.items():
        prefix = STATE / f"genus-canary-run-{gate}-001"
        command, log, exit_path, start, finished, log_sha = [
            Path(str(prefix) + suffix)
            for suffix in (
                ".command.txt",
                ".log",
                ".exit",
                ".start.txt",
                ".finished.txt",
                ".log.sha256",
            )
        ]
        expected = [
            "just",
            "--verbose",
            "--no-dotenv",
            "--color",
            "never",
            recipe,
            str(history.relative_to(ROOT)) if gate == "history" else TARGET,
        ]
        if gate == "strict":
            expected += ["--out", ".temp/gtdb-code006-20261115/genus-strict-001.tsv"]
        if (
            shlex.split(command.read_text()) != expected
            or exit_path.read_text().strip() != "0"
            or not log.stat().st_size
            or sha(log) != log_sha.read_text().split()[0]
            or start.read_text().splitlines()[:2] != [REVISION, "Python 3.13.2"]
        ):
            raise ValueError("actual scoped gate differs")
        paths.update((command, log, exit_path, start, finished, log_sha))
        evidence.append(
            {
                "evidence_id": gate,
                "kind": "validation",
                "reference": str(log.relative_to(ROOT)),
                "accessed_at": accessed,
                "support": "supports",
                "summary": "Actual scoped M5 gate completed with exit0 and a nonempty hash-verified log.",
            }
        )
        checks.append(
            {
                "check_id": gate,
                "name": recipe,
                "status": "passed",
                "required": True,
                "summary": evidence[-1]["summary"],
                "target_ids": ["CommunityMech:000434"],
                "command": command.read_text().strip(),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": [gate],
                "scope_note": "One record and its native history directory; no corpus or scientific validation claim.",
            }
        )
    completion = STATE / "genus-completion-001"
    ccommand, chead, clog, cexit = [
        Path(str(completion) + suffix) for suffix in (".command.txt", ".head.txt", ".log", ".exit")
    ]
    expected_tests = [
        ".venv/bin/python",
        "-m",
        "pytest",
        "tests/test_gtdb_coherence_validator.py::test_the_status_distribution_is_what_was_measured",
        "tests/test_gtdb_not_attempted.py::test_no_taxon_is_silently_outstanding",
        "-q",
        "--tb=short",
    ]
    if (
        shlex.split(ccommand.read_text()) != expected_tests
        or chead.read_text().strip() != REVISION
        or cexit.read_text().strip() != "0"
        or "2 passed" not in clog.read_text()
    ):
        raise ValueError("both unchanged native completion tests must actually pass")
    paths.update((ccommand, chead, clog, cexit))
    evidence.append(
        {
            "evidence_id": "completion",
            "kind": "validation",
            "reference": str(clog.relative_to(ROOT)),
            "accessed_at": accessed,
            "support": "supports",
            "summary": "Both unchanged native outstanding-grounding tests passed on the actual genus application.",
        }
    )
    checks.append(
        {
            "check_id": "completion",
            "name": "Native outstanding-grounding guards",
            "status": "passed",
            "required": True,
            "summary": evidence[-1]["summary"],
            "target_ids": ["CommunityMech:000434"],
            "command": ccommand.read_text().strip(),
            "exit_code": 0,
            "expected_exit_code": 0,
            "evidence_ids": ["completion"],
            "scope_note": "Two actual corpus-level guard tests; not the complete status-reproducibility test or full QC.",
        }
    )
    for identifier, kind, path, summary in (
        (
            "application",
            "record_content",
            applied_path,
            "Actual reviewed genus application connects status-canary d586 to c2cf; original biological payload stays unchanged.",
        ),
        (
            "mapping",
            "database",
            staged,
            "Native same-genus NCBITaxon1763→GTDB:g__Mycobacterium correspondence,18589/18589 named genomes, exact761 crosswalk; no source species/genome identification.",
        ),
        (
            "previous",
            "prior_review",
            ROOT
            / "reviews/structured/20261105T223042Z-pr2035-acidic-nitrification-successor/review.yaml",
            "Preserved November5 full scientific review, source organism/genome uncertainty, literature-access and mechanism limits.",
        ),
        (
            "diagnostic",
            "prior_review",
            ROOT / f"reviews/structured/{PREVIOUS}/review.yaml",
            "Preserved status-only technical diagnostic and its two native completion failures; new actual grounding now addresses that bounded pending action.",
        ),
    ):
        evidence.append(
            {
                "evidence_id": identifier,
                "kind": kind,
                "reference": str(path.relative_to(ROOT)),
                "accessed_at": accessed,
                "support": (
                    "supports" if identifier in {"application", "mapping"} else "context_only"
                ),
                "summary": summary,
            }
        )
    targets = copy.deepcopy(doc["targets"])
    targets[0]["selector"] = "taxonomy[1].taxon_term"
    targets[0]["label"] = "Current Mycobacterium genus correspondence and source limits"
    initial = {path: sha(path) for path in paths}
    output.mkdir()
    target_file = output / "targets.json"
    target_file.write_text(json.dumps({"targets": targets}, indent=2))
    command = [sys.executable, "scripts/record_review.py", "inspect", "--targets", str(target_file)]
    for path in sorted(paths):
        command += ["--input", str(path.relative_to(ROOT))]
    captured = subprocess.check_output(command, cwd=ROOT)
    (output / "inspection.json").write_bytes(captured)
    inspection = json.loads(captured)
    finished = datetime.now(timezone.utc)
    doc.update(
        {
            "review_id": finished.strftime("%Y%m%dT%H%M%SZ") + "-gtdb-genus-000434-canary",
            "title": "One-record technical canary: source-backed Mycobacterium genus correspondence",
            "started_at": applied["created_at"].replace("+00:00", "Z"),
            "finished_at": finished.isoformat().replace("+00:00", "Z"),
            "completion": "completed",
            "verdict": "pass_with_limitations",
            "scientific_review": False,
            "summary": "One actual native genus correspondence and GROUNDED status now pass six scoped gates and both unchanged completion tests. This technical correspondence preserves the paper's unresolved species/genome and mechanism limits; it is not a full scientific review or corpus-QC repair.",
            "source": inspection["source"],
            "targets": targets,
            "checks": checks,
            "evidence": evidence,
            "assessments": [
                {
                    "assessment_id": "genus-correspondence",
                    "area": "grounding",
                    "topic": "Same-genus database correspondence at unchanged source identity",
                    "outcome": "supported",
                    "target_ids": ["CommunityMech:000434"],
                    "evidence_ids": ["mapping", "application", "gtdb", "completion"],
                    "summary": "The retained table supports only the existing declared genus: GTDB:g__Mycobacterium,18589/18589, not reclassified. Exact paper species/genome remains unknown; no primary organism name, quotation or ecological assertion changed.",
                },
                {
                    "assessment_id": "historical-boundary",
                    "area": "provenance",
                    "topic": "Actual application chain and immutable prior assessments",
                    "outcome": "supported",
                    "target_ids": ["CommunityMech:000434"],
                    "evidence_ids": ["previous", "diagnostic", "application", "history"],
                    "summary": "Original13b8→status-only d586→genus c2cf is recorded through two actual application receipts and two append-only sidecars. Both previous reviews remain unchanged. The status-only pending action is addressed for this record; broader2848/2849 and historical scientific findings stay open.",
                },
            ],
            "findings": [],
            "actions": [],
            "limitations": [
                "Technical correspondence only: no new full-paper, supplement, reference/term sweep, exact species/genome identity or scientific approval.",
                "Six scoped gates and two native completion tests pass; the historical native495 discrepancy inventory and three-block work are separate. No full QC pass is asserted.",
                "Execution was isolated M5 Python3.13.2 at956d00c6 plus explicitly hashed orchestration helpers. The prior status-only failed completion proof remains historical, not erased.",
                "Existing scientific findings and source-access/organism/mechanism uncertainty remain; no issue closure or bulk curation is authorized by this assessment.",
            ],
        }
    )
    doc["scope"][
        "description"
    ] = "Only this genus database correspondence, guarded application/history chain and technical completion were assessed."
    doc["related_reviews"][0][
        "relationship"
    ] = "Preserved full scientific assessment; this additive database correspondence does not resolve its species/genome, source-access or mechanism limits."
    doc["related_reviews"].append(
        {
            "repository": "CultureBotAI/CommunityMech",
            "review_id": PREVIOUS,
            "relationship": "Additive technical successor resolves this record's outstanding genus mapping; preserves the actual failed status-only diagnostic and all wider scientific limits.",
        }
    )
    if inspection["source"]["git_revision"] != REVISION or initial != {
        path: sha(path) for path in paths
    }:
        raise ValueError("source changed during assessment inspection")
    (output / "review.json").write_text(json.dumps(doc, indent=2) + "\n")
    print(
        json.dumps(
            {
                "review": str((output / "review.json").relative_to(ROOT)),
                "sha256": sha(output / "review.json"),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
