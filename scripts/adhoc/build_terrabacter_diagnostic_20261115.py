"""Build one scoped GTDB diagnostic from actual M5 evidence, #2849, 2026-11-15.

Inputs: exact applied 000532, primary stock/ancestry, native table and receipts.
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
from check_terrabacter_canary_20261115 import (  # noqa: E402
    AFTER,
    APPLIED,
    APPLIED_SHA,
    HISTORY,
    RECIPES,
    REVISION,
    TARGET,
)
from curate_terrabacter_mapping_20261115 import BEFORE, assert_scope  # noqa: E402

IDENTITY = "CommunityMech:000532"
SIDECAR = HISTORY + "/2026-11-15T052909Z-codex-068f78.yaml"
SIDECAR_SHA = "130afad64f6a3d24ec0ab721758fc13f8f67049380b1eadb737f1b1fd5451c1e"
LEDGER = "reports/causal_graph_review/decisions/20261108-stage2-five-records-batch144.yaml"
OLD_REVIEW = LEDGER
TABLE = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
ROUTE = STATE / "terrabacter-grounding-001.json"


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
    output = STATE / f"terrabacter-diagnostic-{args.attempt}"
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
    staged = STATE / "terrabacter-candidate-m5-001/receipt.json"
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
        ROOT / "scripts/adhoc/check_terrabacter_canary_20261115.py",
        *(ROOT / name for name in applied["inputs"]),
    }
    gate_receipts, checks, evidence = {}, [], []
    for gate in ("schema", "strict", "gtdb", "domain", "scalars", "history", "new-history"):
        prefix = STATE / f"terrabacter-canary-run-{gate}-001"
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
    spec = importlib.util.spec_from_file_location("terrabacter_native_gtdb", native_path)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    rows = native.collect_rows(
        TABLE,
        {"1472881", "53355"},
        set(native.lookup_keys("Terrabacter sp. 2APm3")),
        {"terrabacter"},
    )
    exact_stock = native.resolve_target("1472881", "Terrabacter sp. 2APm3", *rows)
    measured = native.resolve_target("53355", "Terrabacter", *rows)
    prior = json.loads(ROUTE.read_bytes())["reference_genus_result"]
    current_block = after["taxonomy"][0]["taxon_term"]["gtdb_classification"]
    if (
        exact_stock is not None
        or measured != prior
        or {k: current_block[k] for k in measured if k not in {"via", "n_alt"}}
        != {k: v for k, v in measured.items() if k not in {"via", "n_alt"}}
    ):
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
            "exact_stock_result": exact_stock,
            "matches_corrected_block": True,
            "scope": "Verified NCBI stock-to-genus ancestry permits a manual reference-genus correspondence. Counts describe the native named-species-filtered reference population, not an exact stock genome or GTDB species.",
        },
    )
    paths.add(output / "native-route.json")
    targets = [
        {
            "target_id": IDENTITY,
            "path": TARGET,
            "selector": "taxonomy[0].taxon_term.gtdb_classification",
            "label": "Terrabacter 2APm3 manual reference-genus GTDB correspondence",
            "kind": "maintained",
            "ownership_note": "CommunityMech owns this explicitly curated genus mapping. Primary stock/NCBI evidence establishes the ancestor; native gtdb_ground.py computes the reference-genus result. The exact stock has no table result and no GTDB species is assigned.",
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
            "ncbi_authority.lineage; reference_genus_result; reference_genus_rows; native_exact_stock_result",
            "NCBI 1472881 has verified genus ancestor 53355 Terrabacter. The exact stock lookup is empty; the separate native genus query yields GTDB Terrabacter, Actinomycetales/Dermatophilaceae, support 12 / total 12 / fraction 1 after named-species filtering across 18 inspected raw genus rows. This population is not 12 strains of 2APm3.",
        ),
        (
            "recomputed",
            "validation",
            str((output / "native-route.json").relative_to(ROOT)),
            "result",
            "The unchanged native classifier and exact retained table reproduce every stored numerical/classification field for the verified genus after application. The exact stock query remains empty; mapping_source and curation_note explicitly preserve the manual ancestor route and stock-genome limit.",
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
            "records[id=CommunityMech:000532]; node_decisions; source_backed_gaps",
            "The preserved batch144 ledger records the one-node, zero-edge axenic Terrabacter baseline and its unresolved 2-AP ring-cleavage pathway. Those biological claims, evidence quotations and recorded gaps are unchanged and are not newly certified by this mapping diagnostic.",
        ),
        (
            "stock",
            "primary_source",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC13472149/",
            "Methods, Cultures of Microbacterium and Terrabacter, sec2.2 paragraph0; DSMZ BacDive157986; NCBI Taxonomy1472881 LineageEx",
            "The actual primary Methods states 'Preculture of Terrabacter (DSMZ 28514)'. DSMZ BacDive links DSM 28514 to designation 2APm3; NCBI authority links exact stock1472881 to genus53355. These independent sources support stock and ancestor identity, not an exact stock assembly or GTDB species. The generic BacDive NCBI54015 link is not substituted for the exact stock.",
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
        + "-terrabacter-gtdb-diagnostic",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "Terrabacter verified ancestor mapping: one-record M5 diagnostic",
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
        "summary": "Only the manual reference-genus GTDB correspondence and its actual M5 application/provenance are assessed. Verified source stock/NCBI ancestry selects genus53355; the corrected block reproduces its native reference-population computation on exact retained crosswalk bytes, with six passing native gates and one native sidecar. No whole-record scientific approval, exact stock assembly or GTDB species assignment is claimed.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "One taxonomy mapping, before/after scope, database evidence and deterministic gate/provenance chain only.",
            "selection": "One of three stored-block discrepancies in issue2849, addressed only after the Sulfobacillus end-to-end canary persisted successfully. This separately reviewed record has its own actual M5 write and diagnostic chain.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [IDENTITY],
            "exclusions": [
                {
                    "target": "All ecological, cultivation and mechanism claims of000532",
                    "reason": "Existing biological content and quotations are preserved; whole-record scientific support was not reassessed.",
                },
                {
                    "target": "Other issue2849 records and remaining corpus",
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
                "topic": "Verified stock ancestry, retained genus route and denominator",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["stock", "mapping", "recomputed", "gtdb"],
                "summary": "Preserve exact stock1472881 and explicitly curate a genus53355 correspondence supported by primary stock and NCBI ancestry evidence. The native genus result has corrected lineage and support12/total12/fraction1; no exact stock lookup result or stock-genome denominator is asserted. Curated status records the justified manual ancestor route and does not replace independent recomputation.",
            },
            {
                "assessment_id": "bounded-application",
                "area": "provenance",
                "topic": "One actual M5 guarded write and append-only history",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["application", "new-history", "history", "strict", "prior"],
                "summary": "Native validated writer persisted the exact reviewed candidate; every field outside the one GTDB block and appended inline event remains semantically unchanged. The external sidecar records actual application and limitations; old history and batch144 review remain immutable.",
            },
            {
                "assessment_id": "identity-boundary",
                "area": "scope",
                "topic": "Reference-genus population versus exact study-stock assembly",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["stock", "mapping", "prior"],
                "summary": "The primary DSMZ deposit/designation and exact NCBI stock remain intact. A genus correspondence does not identify a stock genome, justify a GTDB species or establish biological mechanism. The existing one node, zero arrows and pathway knowledge gap are preserved rather than newly certified.",
            },
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Diagnostic-only partial assessment. Actual primary full-main Methods, stock catalogue and NCBI authority were inspected for identity; no supplement acquisition, complete scientific review, exact study-stock genome grounding or issue closure is claimed.",
            "The mapping is bound to SHA761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. File modification time does not establish a GTDB release/build; no such release assertion is made.",
            "Full-record native completeness/quality metrics were not recomputed because this assessment covers only one database mapping; passing deterministic gates do not supply scientific approval.",
            "Six native scoped gates plus new-history ran on M5 Python3.13.2 at75c07935 with explicitly hashed additive check/builder source. References, term labels, corpus QC and generated docs are not claimed passed by this diagnostic; no source quotation or NCBITaxon label changed.",
            "The explicitly curated manual genus route is independently recomputed here; the native GTDB gate alone does not establish it. Broader source/functional concerns and work on other2849 records are outside this assessment. An empty finding list is only the result for this corrected mapping scope.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CommunityMech/issues/2849",
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
