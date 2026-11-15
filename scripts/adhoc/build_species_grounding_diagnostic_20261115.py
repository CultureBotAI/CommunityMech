"""Build the actual species-route canary diagnostic for #2848, 2026-11-15.

Inputs: reviewed source proof, exact applied JMP134, actual native gates and
history. Outputs: exclusive private native inspection/review candidate and a
metadata-only source proof. No canonical/cache writes or scientific approval.
"""

import argparse
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import check_jmp134_grounding_20261115 as check
import stage_jmp134_grounding_20261115 as staging
import yaml

ROOT, STATE, TARGET = check.ROOT, check.STATE, check.TARGET
IDENTITY = "CommunityMech:000555"
LEDGER = "reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml"
PRIOR = "reviews/structured/20261111T121000Z-c15s4-record-deep-audit/review.yaml"
REPORT = ROOT / "reports/gtdb-species-status-20261115/jmp134-source-evidence-001.json"
digest = staging.evidence.digest


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(path, data):
    with path.open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--gate-attempt", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--applied-receipt", type=Path, required=True)
    parser.add_argument("--expected-receipt-sha256", required=True)
    args = parser.parse_args()
    if not args.attempt.isdigit() or not args.gate_attempt.isdigit():
        raise ValueError("numeric exclusive attempts required")
    output = STATE / ("diagnostic-" + args.attempt)
    if output.exists() or REPORT.exists() or check.head() != args.expected_revision:
        raise ValueError("exclusive evidence outputs and exact execution revision required")
    captured = {}

    def read(path, expected=None):
        path = Path(path).resolve()
        if path not in captured:
            captured[path] = path.read_bytes()
        raw = captured[path]
        if expected is not None and digest(raw) != expected:
            raise ValueError("input hash differs: " + str(path))
        return raw

    applied_path = args.applied_receipt.resolve()
    if not applied_path.is_relative_to(STATE):
        raise ValueError("actual private application required")
    applied = json.loads(read(applied_path, args.expected_receipt_sha256))
    read(ROOT / "scripts/adhoc/apply_jmp134_grounding_20261115.py", applied["helper_sha256"])
    current = yaml.safe_load(read(ROOT / TARGET, check.AFTER))
    before = yaml.safe_load(read(applied_path.with_name("before.yaml"), check.BEFORE))
    stage = STATE / "jmp134-candidate-001"
    stage_receipt = json.loads(read(stage / "receipt.json", applied["reviewed_receipt_sha256"]))
    read(stage / Path(TARGET).name, check.AFTER)
    if (
        applied["applied"] is not True
        or applied["execution_revision"] != args.expected_revision
        or applied["target"] != TARGET
        or applied["before_sha256"] != check.BEFORE
        or applied["after_sha256"] != check.AFTER
        or stage_receipt["exit_codes"] != [0, 0]
        or applied["inputs"] != stage_receipt["inputs"]
    ):
        raise ValueError("actual reviewed application chain differs")
    for name, expected in applied["inputs"].items():
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError("application input outside repository")
        read(path, check.AFTER if name == TARGET else expected)
    for path in (Path(__file__), ROOT / LEDGER, ROOT / PRIOR, ROOT / "scripts/record_review.py"):
        read(path)
    source = json.loads(read(staging.PROOF, staging.PROOF_SHA))
    native = staging.native_module()
    measured = staging.expected_result(native)
    if measured != source["native_result"] or measured != stage_receipt["native_result"]:
        raise ValueError("actual exact-strain correspondence changed")
    staging.verify_semantics(before, current, native, stage_receipt["native_block"])
    if current["taxonomy"][0]["taxon_term"]["gtdb_classification"] != stage_receipt["native_block"]:
        raise ValueError("current block differs from accepted native result")
    started = now()
    checks, evidence, sidecars = [], [], {}
    for gate, recipe in check.RECIPES.items():
        directory = STATE / f"canary-run-{gate}-{args.gate_attempt}"
        receipt = json.loads(read(directory / "receipt.json"))
        log = directory / "native.log"
        log_raw = read(log, receipt["log_sha256"])
        if (
            receipt["revision"] != args.expected_revision
            or receipt["plan"] is not False
            or receipt["exit_code"] != 0
            or read(directory / "native.exit").strip() != b"0"
            or len(log_raw) != receipt["log_bytes"]
            or not log_raw
            or receipt["execution_inputs_unchanged"] is not True
            or receipt["inputs"].get(str(ROOT / TARGET)) != check.AFTER
        ):
            raise ValueError("actual required native gate did not pass: " + gate)
        command = ["just", "--verbose", "--no-dotenv", "--color", "never", recipe]
        if gate == "new-history":
            if receipt["command"][:6] != command or len(receipt["new_history_sidecars"]) != 1:
                raise ValueError("native history generation differs")
            sidecars = receipt["new_history_sidecars"]
        else:
            command.append(check.HISTORY if gate == "history" else TARGET)
            if gate == "strict":
                command.extend(["--out", str((directory / "strict.tsv").relative_to(ROOT))])
            if receipt["command"] != command:
                raise ValueError("gate command scope differs")
        for path, expected in receipt["inputs"].items():
            read(Path(path), expected)
        for path in directory.iterdir():
            if path.is_file():
                read(path)
        evidence.append(
            {
                "evidence_id": gate,
                "kind": "validation",
                "reference": str(log.relative_to(ROOT)),
                "accessed_at": started,
                "support": "supports",
                "summary": "Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs.",
            }
        )
        checks.append(
            {
                "check_id": gate,
                "name": recipe,
                "status": "passed",
                "required": True,
                "summary": evidence[-1]["summary"],
                "target_ids": [IDENTITY],
                "command": shlex.join(receipt["command"]),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": [gate],
                "scope_note": "One exact record; no corpus or whole-record scientific approval.",
            }
        )
    for path, expected in sidecars.items():
        if not path.startswith(check.HISTORY + "/"):
            raise ValueError("sidecar belongs to another record")
        read(ROOT / path, expected)
    read(ROOT / "scripts/adhoc/check_jmp134_grounding_20261115.py")
    metadata = {
        "record": TARGET,
        "record_id": IDENTITY,
        "source_inspection_sha256": staging.PROOF_SHA,
        "source_inputs": source["inputs"],
        "primary_reference": source["primary_reference"],
        "primary_locators": [
            {key: row[key] for key in ("character_offset", "line")}
            for row in source["primary_contexts"]
        ],
        "ncbi_identity_rows": source["ncbi_identity_rows"],
        "ncbi_query_limitation": source["ncbi_query_limitation"],
        "crosswalk_exact_rows": source["crosswalk_exact_rows"],
        "native_result": measured,
        "population_scope": source["population_scope"],
        "name_scope": source["name_scope"],
        "preserved_scientific_limit": source["preserved_scientific_limit"],
        "scientific_review": False,
    }
    staging.unchanged(captured)
    output.mkdir()
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    write_json(REPORT, metadata)
    read(REPORT)
    targets = [
        {
            "target_id": IDENTITY,
            "path": TARGET,
            "selector": "taxonomy[0].taxon_term.gtdb_classification; gtdb_grounding_status",
            "label": "JMP134 exact-strain native GTDB correspondence and status",
            "kind": "maintained",
            "ownership_note": "CommunityMech owns the record; this review assesses one database correspondence and actual provenance, preserving prior biological claims.",
        }
    ]
    write_json(output / "targets.json", {"targets": targets})
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(output / "targets.json"),
    ]
    for path in sorted(captured):
        if path.is_relative_to(ROOT):
            command.extend(["--input", str(path.relative_to(ROOT))])
    raw = subprocess.check_output(command, cwd=ROOT)
    inspection = json.loads(raw)
    if inspection["source"]["git_revision"] != args.expected_revision:
        raise ValueError("native inspection has wrong revision")
    for item in inspection["source"]["inputs"]:
        path = ROOT / item["path"]
        if path in captured and item["sha256"] != digest(captured[path]):
            raise ValueError("native inspection differs from actually assessed bytes")
    (output / "inspection.json").write_bytes(raw)
    sources = [
        (
            "paper",
            "primary_source",
            "https://pubmed.ncbi.nlm.nih.gov/42364169/",
            "Methods/Results; retained cache offsets16009 and28959",
            "The inspected study identifies C.necator JMP134. Its stock name remains unchanged in preferred_term and scientific prose; the paper is not used as a GTDB database assignment.",
        ),
        (
            "stock",
            "database",
            str(REPORT.relative_to(ROOT)),
            "ncbi_identity_rows",
            "Local NCBITaxon264198 query identifies canonical C.pinatubonensis JMP134 and the related synonym C.necator JMP134. This exact-stock connection does not equate other C.necator strains.",
        ),
        (
            "mapping",
            "database",
            str(REPORT.relative_to(ROOT)),
            "crosswalk_exact_rows[0] line71828; native_result",
            "Exact761 crosswalk contains one row for NCBITaxon264198/strainJMP134: one genome, fraction1.0 and GTDB:s__Cupriavidus_pinatubonensis. Fresh native ncbi_id resolution reproduces the same current block; no additional population is inferred.",
        ),
        (
            "application",
            "record_content",
            str(applied_path.relative_to(ROOT)),
            "applied/before_sha256/after_sha256/inputs",
            "Actual M5 guarded replacement persisted only the accepted block, GROUNDED status and two native inline events. All source and raw application inputs, native sidecar and current bytes are bound.",
        ),
        (
            "prior",
            "prior_review",
            LEDGER,
            "records[id=CommunityMech:000555]",
            "Original batch147 evidence and deep audit remain historical. The open relative in-vivo expression/flux contribution of tfdBI versus tfdBII remains unchanged; no new graph or full scientific review is claimed.",
        ),
    ]
    for ident, kind, reference, locator, summary in sources:
        evidence.append(
            {
                "evidence_id": ident,
                "kind": kind,
                "reference": reference,
                "locator": locator,
                "accessed_at": started,
                "support": "context_only" if ident == "prior" else "supports",
                "summary": summary,
            }
        )
    authored = [
        (
            "identity",
            "grounding",
            "Exact source stock and database name scope",
            ["paper", "stock", "terms"],
            "Preserve NCBITaxon264198 and both recorded names. The inspected NCBI synonym connects the paper's C.necator JMP134 to canonical C.pinatubonensis JMP134. No formal nomenclatural change or identity of other stocks is asserted.",
        ),
        (
            "correspondence",
            "grounding",
            "Exact-ID native result and one-genome population",
            ["mapping", "gtdb", "domain"],
            "Add the independently reviewed native species block for the exact strain-ID row and mark its presence GROUNDED. Fraction1.0 and total_genomes1 describe this pinned table row; is_reclassified:false is the native cleaned-name comparison, not a formal nomenclatural claim.",
        ),
        (
            "provenance",
            "provenance",
            "Bounded actual application and retained scientific limits",
            ["application", "schema", "strict", "scalars", "new-history", "history", "prior"],
            "Actual guarded application, eight native commands and append-only sidecar are retained. Entire remaining record semantics, earlier inline events and scientific reviews are preserved, including the open paralog-expression/flux question. The historical hash guard requires its separate strict successor integration.",
        ),
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-jmp134-gtdb-diagnostic",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "JMP134 exact-strain GTDB correspondence: scoped M5 diagnostic",
        "started_at": started,
        "finished_at": now(),
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored source proof and correction; parent independently inspected primary contexts, NCBI query, exact crosswalk row, candidate semantics and guarded writer before actual application.",
        },
        "skill": "curate-yaml-record",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": False,
        "summary": "Scoped native database correspondence and actual provenance only. Exact JMP134 stock identity and pinned one-genome crosswalk row support this species block; existing biological claims and their scientific uncertainty remain unchanged.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "One native GTDB species block, grounding status, exact stock/source identity and actual bounded application.",
            "selection": "Representative exact-ID canary from the29 whole-record same-name species/strain planning group under issue2848; no group fanout preceded this canary.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [IDENTITY],
            "exclusions": [
                {
                    "target": "All other experimental claims/graph/discussions and other records",
                    "reason": "Preserved original science is not newly reassessed by this database diagnostic; no whole-record or corpus scientific approval.",
                }
            ],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": ident,
                "area": area,
                "topic": topic,
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ids,
                "summary": summary,
            }
            for ident, area, topic, ids, summary in authored
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Scoped technical/provenance assessment with scientific_review:false. It neither completes the entire scientific record nor closes broader issue2848.",
            "The NCBI query output is retained but the whole local SQLite database/release was not hash-certified by that query. Exact crosswalk bytes, row, native resolver and source context are separately bound.",
            "One genome in this exact strain-ID row is a thin database population. No species-wide count, other stock identity, genome assembly accession or ANI measurement is inferred.",
            "Seven native scoped validation commands and one history scaffolder passed. Corpus QC, source-snippet matching and generated documentation are separate, unclaimed work.",
            "Original historical hash/biology assertions and immutable scientific reviews remain; a separately reviewed batch147 successor must integrate this actual diagnostic before historical-current tests can accept changed bytes.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CommunityMech/issues/2848",
            "https://github.com/CultureBotAI/CommunityMech/pull/2862",
        ],
    }
    staging.unchanged(captured)
    if check.head() != args.expected_revision:
        raise ValueError("revision changed before publishing candidate")
    write_json(output / "review.json", review)
    print(
        json.dumps(
            {
                "review": str((output / "review.json").relative_to(ROOT)),
                "sha256": digest((output / "review.json").read_bytes()),
                "inputs": len(review["source"]["inputs"]),
            }
        )
    )


if __name__ == "__main__":
    main()
