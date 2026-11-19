"""Build one scoped GTDB diagnostic from actual M5 evidence, #2849, 2026-11-15.

Inputs: exact applied000035, native mapping/table, receipts and native sidecar.
Outputs: exclusive private target/inspection/recomputed-route/review JSON; native
validate/save is separate. No canonical write, source acquisition or full science.
"""

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-source-routes-2849-20261115"
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
from check_sulfobacillus_canary_20261115 import (  # noqa: E402
    AFTER,
    APPLIED,
    APPLIED_SHA,
    HISTORY,
    RECIPES,
    REVISION,
    TARGET,
)
from curate_sulfobacillus_mapping_20261115 import BEFORE, assert_scope  # noqa: E402

IDENTITY = "CommunityMech:000035"
SIDECAR = HISTORY + "/2026-11-15T050250Z-codex-3f8936.yaml"
SIDECAR_SHA = "2e50ea4c26f5f9286b35577eaeecb1a3a8c0f08c8685453901619747ed1016e1"
LEDGER = "reports/causal_graph_review/decisions/20261006-pitlakes-bioleach-biofilm-batch53.yaml"
OLD_REVIEW = "reports/causal_graph_review/adversarial-review-20261006-batch53.yaml"
TABLE = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
ROUTE = STATE / "sulfobacillus-route-001.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def exclusive_json(path, value):
    with path.open("x") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempt", required=True)
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric exclusive attempt required")
    output = STATE / f"diagnostic-{args.attempt}"
    if output.exists() or output.is_symlink():
        raise ValueError("prior diagnostic must remain immutable")
    started = now()
    if (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        != REVISION
    ):
        raise ValueError("exact actual M5 execution revision required")
    if sha(ROOT / TARGET) != AFTER or sha(APPLIED) != APPLIED_SHA:
        raise ValueError("actual reviewed application differs")
    applied = json.loads(APPLIED.read_bytes())
    if applied["applied"] is not True or applied["execution_revision"] != REVISION:
        raise ValueError("actual applied receipt required")
    staged = STATE / "sulfobacillus-candidate-m5-001/receipt.json"
    if sha(staged) != applied["reviewed_staging_receipt_sha256"]:
        raise ValueError("reviewed staging receipt changed")
    before_path = APPLIED.with_name("before.yaml")
    if sha(before_path) != BEFORE or sha(ROOT / SIDECAR) != SIDECAR_SHA:
        raise ValueError("actual predecessor/sidecar changed")
    before, after = yaml.safe_load(before_path.read_bytes()), yaml.safe_load(
        (ROOT / TARGET).read_bytes()
    )
    assert_scope(before, after)
    for name, expected in applied["inputs"].items():
        if sha(ROOT / name) != expected:
            raise ValueError("reviewed application source changed: " + name)
    paths = {
        ROOT / TARGET,
        APPLIED,
        before_path,
        staged,
        staged.with_name("candidate.yaml"),
        ROOT / SIDECAR,
        ROOT / LEDGER,
        ROOT / OLD_REVIEW,
        Path(__file__),
        ROOT / "scripts/adhoc/check_sulfobacillus_canary_20261115.py",
        *(ROOT / name for name in applied["inputs"]),
    }
    gate_receipts, checks, evidence = {}, [], []
    for gate in ("schema", "strict", "gtdb", "domain", "scalars", "history", "new-history"):
        prefix = STATE / f"canary-run-{gate}-001"
        receipt = json.loads((prefix / "receipt.json").read_bytes())
        log = prefix / "native.log"
        if (
            receipt["revision"] != REVISION
            or receipt["plan"] is not False
            or receipt["exit_code"] != 0
            or (prefix / "native.exit").read_text().strip() != "0"
            or receipt["log_sha256"] != sha(log)
            or receipt["log_bytes"] != log.stat().st_size
            or not log.stat().st_size
        ):
            raise ValueError("required actual native gate did not pass: " + gate)
        expected = ["just", "--verbose", "--no-dotenv", "--color", "never", RECIPES[gate]]
        if gate == "new-history":
            if receipt["command"][:6] != expected or SIDECAR not in log.read_text():
                raise ValueError("actual native sidecar generation differs")
        else:
            expected.append(HISTORY if gate == "history" else TARGET)
            if gate == "strict":
                expected.extend(["--out", str((prefix / "strict.tsv").relative_to(ROOT))])
            if receipt["command"] != expected:
                raise ValueError("native command scope differs")
        if receipt["inputs"].get(str(ROOT / TARGET)) != AFTER:
            raise ValueError("gate did not bind corrected record")
        for name, expected_hash in receipt["inputs"].items():
            path = Path(name)
            if sha(path) != expected_hash:
                raise ValueError("gate input changed: " + name)
            if path.is_relative_to(ROOT):
                paths.add(path)
        paths.update(prefix.iterdir())
        gate_receipts[gate] = receipt
        evidence.append(
            {
                "evidence_id": gate,
                "kind": "validation",
                "reference": str(log.relative_to(ROOT)),
                "accessed_at": started,
                "support": "supports",
                "summary": "Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log.",
            }
        )
        checks.append(
            {
                "check_id": gate,
                "name": RECIPES[gate],
                "status": "passed",
                "required": True,
                "summary": evidence[-1]["summary"],
                "target_ids": [IDENTITY],
                "command": __import__("shlex").join(receipt["command"]),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": [gate],
                "scope_note": "One corrected record; new-history creates its sidecar and history validates its complete history directory. This is not corpus QC or literature validation.",
            }
        )
    output.mkdir()
    native_path = ROOT / "scripts/gtdb_ground.py"
    spec = importlib.util.spec_from_file_location("sulfobacillus_native_gtdb", native_path)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    rows = native.collect_rows(
        TABLE, {"53633"}, set(native.lookup_keys("Sulfobacillus acidophilus")), set()
    )
    measured = native.resolve_target("53633", "Sulfobacillus acidophilus", *rows)
    prior = json.loads(ROUTE.read_bytes())["native_lookup"]["result"]
    current_block = after["taxonomy"][6]["taxon_term"]["gtdb_classification"]
    if measured != prior or {k: current_block[k] for k in measured if k != "via"} != {
        k: v for k, v in measured.items() if k != "via"
    }:
        raise ValueError("actual native recomputation does not reproduce corrected mapping")
    exclusive_json(
        output / "native-route.json",
        {
            "revision": REVISION,
            "target": TARGET,
            "record_sha256": AFTER,
            "classifier_sha256": sha(native_path),
            "crosswalk_sha256": sha(TABLE),
            "result": measured,
            "matches_corrected_block": True,
            "scope": "Database correspondence at the declared reference species; not exact study-strain identity.",
        },
    )
    paths.add(output / "native-route.json")
    targets = [
        {
            "target_id": IDENTITY,
            "path": TARGET,
            "selector": "taxonomy[6].taxon_term.gtdb_classification",
            "label": "Sulfobacillus acidophilus reference-taxon GTDB correspondence",
            "kind": "maintained",
            "ownership_note": "CommunityMech owns the canonical mapping; native gtdb_ground.py computes the database correspondence from the retained kg-microbe table. Broader composite-community scope remains issue1509.",
        }
    ]
    exclusive_json(output / "targets.json", {"targets": targets})
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(output / "targets.json"),
    ]
    for path in sorted(paths):
        command.extend(["--input", str(path.relative_to(ROOT))])
    captured = subprocess.check_output(command, cwd=ROOT)
    inspection = json.loads(captured)
    if inspection["source"]["git_revision"] != REVISION:
        raise ValueError("native inspection revision differs")
    (output / "inspection.json").write_bytes(captured)
    for identifier, kind, reference, locator, summary in (
        (
            "mapping",
            "database",
            str(ROUTE.relative_to(ROOT)),
            "native_lookup.exact_species_name_rows.sulfobacillus acidophilus; taxonID NCBI679936/1051632; total genomes/majority fraction/species(GTDB)",
            "Two exact-name rows each report2 genomes and fraction1.0 for Sulfobacillus_A acidophilus; no53633 row exists in this exact table. The native name route produces total4, fraction1.0, and GTDB suffix_A, independently recomputed after M5 apply.",
        ),
        (
            "recomputed",
            "validation",
            str((output / "native-route.json").relative_to(ROOT)),
            "result",
            "Actual unchanged native classifier and exact761 table reproduce every stored numerical/classification field after application; mapping_source explicitly records the route and its study-strain limit.",
        ),
        (
            "application",
            "record_content",
            str(APPLIED.relative_to(ROOT)),
            "applied/before_sha256/after_sha256/inputs",
            "Actual M5 guarded apply changed only the reviewed GTDB block and appended native inline history; exact reviewed staging receipt and all source hashes were rechecked before replacement.",
        ),
        (
            "prior",
            "prior_review",
            OLD_REVIEW,
            "findings.issue1509; adversarial_checks; limitations",
            "The preserved batch53 review explicitly left canonical roster and non-graph claims uncertified, with composite community identity unresolved under1509. Its nine current nodes and zero arrows are unchanged by this mapping correction.",
        ),
        (
            "abstract",
            "primary_source",
            "https://pubmed.ncbi.nlm.nih.gov/24242252/",
            "Abstract; committed PMID_24242252.md content",
            "The inspected primary abstract names Sulfobacillus acidophilus in the mixed culture. It supplies no study-strain genome identity or GTDB mapping. This assessment read the abstract, not the inaccessible main paper or supplements.",
        ),
    ):
        evidence.append(
            {
                "evidence_id": identifier,
                "kind": kind,
                "reference": reference,
                "locator": locator,
                "accessed_at": started,
                "support": (
                    "supports"
                    if identifier in {"mapping", "recomputed", "application"}
                    else "context_only"
                ),
                "summary": summary,
            }
        )
    finished = now()
    doc = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-sulfobacillus-gtdb-diagnostic",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "Sulfobacillus reference mapping: one-record M5 diagnostic canary",
        "started_at": started,
        "finished_at": finished,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored the source diagnosis and correction; root independently accepted source rows, guarded helper, local candidate and timestamp-only M5 candidate before the one actual M5 apply.",
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": False,
        "summary": "Only the reference-taxon GTDB correspondence and its actual M5 application/provenance are assessed. The corrected block reproduces native computation on exact761 crosswalk bytes, with six passing native gates and one native sidecar. No whole-record scientific approval, exact strain identity or issue1509 resolution is claimed.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "One taxonomy mapping, before/after scope, database evidence and deterministic gate/provenance chain only.",
            "selection": "First of the three stored-block discrepancies in2849, chosen as the required single end-to-end canary before further record changes.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [IDENTITY],
            "exclusions": [
                {
                    "target": "All other taxonomy mappings and all ecological/cultivation/community claims of000035",
                    "reason": "Existing biological content preserved; source support and composite community identity were not reassessed.",
                },
                {
                    "target": "Other two issue2849 records and remaining corpus",
                    "reason": "No batch application or scientific review is represented by this one-record canary.",
                },
            ],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "reference-mapping",
                "area": "grounding",
                "topic": "Exact retained crosswalk route and denominator",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["mapping", "recomputed", "gtdb"],
                "summary": "Exact species-name rows679936/1051632 agree on Sulfobacillus_A acidophilus; native computation gives total4/fraction1.0/name difference true. Preserve NCBITaxon53633 and source species name, remove unsupported latest/build wording, add no curated exemption.",
            },
            {
                "assessment_id": "bounded-application",
                "area": "provenance",
                "topic": "One actual M5 guarded write and append-only history",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["application", "new-history", "history", "strict", "prior"],
                "summary": "Native validated writer persisted the exact reviewed candidate; every field outside the one GTDB block and appended inline event remains semantically unchanged. The external sidecar records actual application and limitations; old history and batch53 review remain immutable.",
            },
            {
                "assessment_id": "identity-boundary",
                "area": "scope",
                "topic": "Reference species versus study strain and composite community",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["abstract", "mapping", "prior"],
                "summary": "The source abstract's species name is retained. A database name correspondence does not identify the paper's exact strain, resolve the composite roster or establish biological mechanism. The record remains subject to1509; the existing nine nodes/zero arrows are preserved rather than newly certified.",
            },
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Diagnostic-only partial assessment; no full scientific review, new primary full-text/supplement acquisition, exact study-strain genome grounding or issue closure.",
            "The mapping is bound to SHA761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. File modification time does not establish a GTDB release/build; no such release assertion is made.",
            "Full-record native completeness/quality metrics were not recomputed because this assessment covers only one database mapping; passing deterministic gates do not supply scientific approval.",
            "Six native scoped gates plus new-history ran on M5 Python3.13.2 atcb642708 with explicitly hashed additive check/builder source. References, term labels, corpus QC and generated docs are not claimed passed by this diagnostic; no source quotation or NCBITaxon label changed.",
            "Existing source/roster/functional concerns under1509 and other2849 records remain unresolved. An empty finding list is only the result for this corrected mapping scope.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CommunityMech/issues/2849",
            "https://github.com/CultureBotAI/CommunityMech/issues/1509",
            "https://github.com/CultureBotAI/CommunityMech/pull/2804",
        ],
    }
    exclusive_json(output / "review.json", doc)
    print(
        json.dumps(
            {
                "review": str((output / "review.json").relative_to(ROOT)),
                "sha256": sha(output / "review.json"),
                "source_inputs": len(doc["source"]["inputs"]),
            }
        )
    )


if __name__ == "__main__":
    main()
