"""Prepare the full 000122 successor after historical-scope repair, #2831.

Inputs: unchanged primary sources and immutable prior full assessment, exact
actual application chain, three native sidecars, nine current gates and measured
44/44 comparisons. Outputs: exclusive private native inspection/review draft;
2026-11-15. No canonical, cache, history or previously saved review writes.
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

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
from check_gut_successor_20261115 import BASE, GATES, HISTORY, STATE, TARGET  # noqa: E402
from curate_gut_historical_scope_20261115 import BASELINE, PREVIOUS, load, revised  # noqa: E402

AFTER = "c8c508709645f7a90090f0e3e69a5bcd5757f89b624343abcef8ad9e412be34e"
PRIOR_SHA = "ec301661050a11d2968e36efb03d39f97dbdf9158fa3e4db7b8c3b35a09c9366"
APPLICATION = "7752c6f3470f9d8312cc8406313158b04500472eaf6b1a9b50973185400eefe6"
OLD_APPLICATION = "69e86f16f78d6c4c3106002bfa14dac64844399e71bb52940656f2d0bfeae21a"
IDENTIFIER = "CommunityMech:000122"
REPO = "CultureBotAI/CommunityMech"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def retained_plan():
    prior_path = ROOT / PREVIOUS / "review.yaml"
    if sha(prior_path) != PRIOR_SHA:
        raise ValueError("immutable full predecessor changed")
    prior = yaml.safe_load(prior_path.read_bytes())
    changes = []
    for item in prior["source"]["inputs"]:
        path = ROOT / item["path"]
        actual = sha(path) if path.is_file() else None
        if actual != item["sha256"]:
            changes.append({"path": item["path"], "before": item["sha256"], "current": actual})
    return prior, changes


def checked_receipts():
    result = {}
    for gate in (*GATES, "references", "network"):
        name = f"canary-{gate}-historical-001"
        receipt = json.loads((STATE / (name + ".json")).read_bytes())
        if any(
            (
                receipt["head"] != BASE,
                receipt["gate"] != gate,
                receipt["record"] != TARGET,
                receipt["record_worktree_sha256"] != AFTER,
                receipt["status"] != "PASSED",
                receipt["exit_code"] != 0,
                not receipt["inputs_unchanged"],
                (STATE / (name + ".exit")).read_text().strip() != "0",
                sha(ROOT / receipt["log"]) != receipt["log_sha256"],
                not receipt["log_bytes"],
                receipt["runner_sha256"]
                != sha(ROOT / "scripts/adhoc/check_gut_successor_20261115.py"),
            )
        ):
            raise ValueError("native gate receipt is incomplete or stale")
        if any(sha(ROOT / path) != expected for path, expected in receipt["inputs"].items()):
            raise ValueError("native gate input changed")
        expected = GATES.get(gate)
        if gate == "strict":
            expected = expected + ["--out", str((STATE / (name + ".tsv")).relative_to(ROOT))]
        elif gate == "terms":
            expected = [
                "uv",
                "run",
                "--no-sync",
                "linkml-term-validator",
                "validate-data",
                TARGET,
                "-s",
                "src/communitymech/schema/communitymech.yaml",
                "--labels",
                "--config",
                str((STATE / (name + "-oak.yaml")).relative_to(ROOT)),
                "--cache-dir",
                str((STATE / (name + "-labels")).relative_to(ROOT)),
            ]
        elif gate == "references":
            expected = [
                "uv",
                "run",
                "--no-sync",
                "linkml-reference-validator",
                "validate",
                "data",
                TARGET,
                "-s",
                "src/communitymech/schema/communitymech.yaml",
                "--config",
                "conf/reference_validator.yaml",
                "--cache-dir",
                str((STATE / (name + "-cache")).relative_to(ROOT)),
                "--no-full-text",
            ]
            if not receipt["private_cache_unchanged"]:
                raise ValueError("reference source copy changed")
        elif gate == "network":
            expected = [
                "uv",
                "run",
                "--no-sync",
                "communitymech",
                "audit-network",
                "--communities-dir",
                str((STATE / (name + "-records")).relative_to(ROOT)),
                "--json",
            ]
            if (
                receipt["private_record_sha256"] != AFTER
                or json.loads((ROOT / receipt["log"]).read_text()) != {}
            ):
                raise ValueError("network target/output differs")
        if receipt["command"] != expected:
            raise ValueError("native command differs")
        result[gate] = receipt
    return result


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    prior, changes = retained_plan()
    if args.plan:
        print(json.dumps({"prior_input_changes": changes}, indent=2))
        return
    allowed = {
        TARGET: (BASELINE, AFTER),
        "src/communitymech/schema/mech_shared.yaml": (
            "c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895",
            "cf32864df1626201128e9311054b075bfc4ad3d8345491ac144122a5d5e67d11",
        ),
        "docs/record-reviews.md": (
            "452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b",
            "eaedec5783b40925a3f0e159dfd1202c315a12e98c8859526378ceea5c547822",
        ),
    }
    if {item["path"]: (item["before"], item["current"]) for item in changes} != allowed:
        raise ValueError("predecessor input changes exceed the explicitly reassessed scope")
    if not args.output:
        raise ValueError("exclusive output required")
    output = args.output.resolve()
    if output.exists() or not output.is_relative_to(STATE):
        raise ValueError("exclusive private output required")
    old_application = STATE / "applied-001/receipt.json"
    application = STATE / "historical-scope-applied-001/receipt.json"
    if sha(old_application) != OLD_APPLICATION or sha(application) != APPLICATION:
        raise ValueError("actual application receipts changed")
    old_applied, applied = (
        json.loads(path.read_bytes()) for path in (old_application, application)
    )
    if (
        not old_applied["applied"]
        or not applied["applied"]
        or (
            old_applied["after_sha256"] != BASELINE
            or applied["before_sha256"] != BASELINE
            or applied["after_sha256"] != AFTER
            or sha(ROOT / TARGET) != AFTER
        )
    ):
        raise ValueError("application chain is not contiguous")
    before = load((STATE / "historical-scope-applied-001/before.yaml").read_bytes())
    record = load((ROOT / TARGET).read_bytes())
    expected = revised(before)
    expected["curation_history"].append(applied["event"])
    if expected != record:
        raise ValueError("scientific record changed beyond the accepted scope")
    receipts = checked_receipts()
    measurement_path = STATE / "measured-historical-001/receipt.json"
    measurement = json.loads(measurement_path.read_bytes())
    if any(
        (
            measurement["head"] != BASE,
            measurement["record_sha256"] != AFTER,
            not measurement["measurement_valid"],
            not measurement["inputs_unchanged"],
            not measurement["assertion_coverage_complete"],
            measurement["native_exit_code"] != 0,
            measurement["counts"]["snippet_surfaces"] != 44,
            measurement["counts"]["snippet_occurrences_compared"] != 44,
            measurement["assertion_status_counts"] != {"matched": 44},
            (measurement_path.parent / "exit").read_text().strip() != "0",
        )
    ):
        raise ValueError("actual assertion measurement differs")
    if any(sha(ROOT / path) != value for path, value in measurement["inputs"].items()):
        raise ValueError("measured input changed")
    paths = {item["path"] for item in prior["source"]["inputs"]}
    paths.update(
        (PREVIOUS + "/review.yaml", PREVIOUS + "/review.md", str(Path(__file__).relative_to(ROOT)))
    )
    paths.update(str(path.relative_to(ROOT)) for path in (ROOT / HISTORY).glob("*.yaml"))
    if {path.name for path in (ROOT / HISTORY).glob("*.yaml")} != {
        "2026-10-06T204405Z-codex-60df62.yaml",
        "2026-11-15T024332Z-claude-code-aee684.yaml",
        "2026-11-15T024401Z-codex-6c2ac7.yaml",
        "2026-11-15T033049Z-codex-fa718a.yaml",
    }:
        raise ValueError("expected October predecessor and three November native gut sidecars")
    for pattern in (
        "canary-*-historical-001.json",
        "canary-*-historical-001.log",
        "canary-*-historical-001.exit",
        "canary-*-historical-001.tsv",
        "canary-*-historical-001-oak.yaml",
    ):
        paths.update(str(path.relative_to(ROOT)) for path in STATE.glob(pattern))
    for folder in (
        "historical-scope-candidate-001",
        "historical-scope-applied-001",
        "measured-historical-001",
    ):
        paths.update(
            str(path.relative_to(ROOT)) for path in (STATE / folder).iterdir() if path.is_file()
        )
    paths.update(
        str(path.relative_to(ROOT)) for path in (ROOT / "scripts/adhoc").glob("*gut*20261115.*")
    )
    paths.add("tests/test_gut_historical_scope_guard.py")
    output.mkdir()
    targets = {"targets": prior["targets"]}
    (output / "targets.yaml").write_text(yaml.safe_dump(targets, sort_keys=False))
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(output / "targets.yaml"),
    ]
    for path in sorted(paths):
        command.extend(["--input", path])
    inspected_raw = subprocess.check_output(command, cwd=ROOT, text=True)
    (output / "inspection.json").write_text(inspected_raw)
    inspected = json.loads(inspected_raw)
    finished = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    review = copy.deepcopy(prior)
    review.update(
        review_id=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-phase2-gut-historical-successor",
        title="Full current gut assessment after historical discussion-scope correction",
        started_at=applied["created_at"].replace("+00:00", "Z"),
        finished_at=finished,
        source=inspected["source"],
        targets=inspected["targets"],
        summary="Full current 000122 reassessment preserves the twelve-stock, protocol, arm and model-bounded scientific judgments after an exact two-rationale correction. All primary/supplement/grounding sources remain byte-identical to the preceding full review. Nine fresh native gates passed; current annotated schema compares all44 snippets, including the SupportingReference, with44 matches. Molecular mechanisms and individual-stock genome grounding remain unresolved. No global issue or repository-QC pass is claimed.",
    )
    review["reviewer"][
        "independence_basis"
    ] = "Same author carries the full unchanged-assertion assessment forward after source-hash and semantic checks; parent independently accepted the exact two-rationale candidate and guarded writer before application. A separate final review is required."
    evidence = {item["evidence_id"]: item for item in review["evidence"]}
    evidence["record"].update(snapshot_sha256=AFTER, accessed_at=finished)
    evidence["measured"].update(
        reference=str(measurement_path.relative_to(ROOT)),
        snapshot_sha256=sha(measurement_path),
        accessed_at=finished,
        summary="Actual no-acquisition native measurement:44 unique snippets compared and matched, including43 EvidenceItem and1 SupportingReference; zero yielded issues. Historical43+1 measurement remains unchanged.",
    )
    for gate, receipt in receipts.items():
        evidence["check-" + gate].update(
            reference=receipt["log"], snapshot_sha256=receipt["log_sha256"], accessed_at=finished
        )
        check = next(item for item in review["checks"] if item["check_id"] == gate)
        check["command"] = shlex.join(receipt["command"])
        check["summary"] = (
            "Fresh exact-record native gate passed with unchanged bound inputs; does not establish scientific support or repository QC."
        )
    for identifier, path, kind, summary in (
        (
            "historical-application",
            application,
            "validation",
            "Actual reviewed d0be-to-c8c application with post-native-validation input rechecks, external dual hashes and append-only history.",
        ),
        (
            "prior-full",
            ROOT / PREVIOUS / "review.yaml",
            "prior_review",
            "Immutable full predecessor; its scientific assertions are retained after byte/semantic checks, and its historical43+1 automatic coverage claim is not rewritten.",
        ),
    ):
        review["evidence"].append(
            {
                "evidence_id": identifier,
                "kind": kind,
                "reference": str(path.relative_to(ROOT)),
                "locator": "Complete retained artifact",
                "accessed_at": finished,
                "support": "context_only",
                "summary": summary,
                "snapshot_sha256": sha(path),
            }
        )
    assessments = {item["assessment_id"]: item for item in review["assessments"]}
    assessments["history"][
        "summary"
    ] = "Both actual application receipts bind the contiguous original-to-d0be-to-c8c chain. Original inline history and the two earlier sidecars remain unchanged; a third native Codex sidecar records the historical-scope correction."
    assessments["history"]["evidence_ids"] += ["historical-application", "prior-full"]
    assessments["coverage"].update(
        outcome="supported",
        summary="Current c8c record under the governed annotated shared schema has44 actual comparisons and44 matches, including1 SupportingReference. The earlier full review remains an honest43-matched/1-unannotated observation. Resolves only this record's automated-coverage finding; lexical matching is not source-truth proof.",
    )
    review["assessments"].append(
        {
            "assessment_id": "historical-scope",
            "target_ids": [IDENTIFIER],
            "area": "provenance",
            "topic": "Historical versus current roster and inspection scope",
            "outcome": "supported",
            "summary": "The October checkpoint's aggregate roster and uninspected source surfaces are explicitly historical. Current12-stock taxonomy, complete article text/captions, Figure4B/C pixels and Appendix/EV inspections are distinguished from unperformed raw-data, all-supplement-pixel and model work. Only the two discussion tails plus one inline history event changed; quoted evidence, protocols and graph assertions are unchanged.",
            "evidence_ids": [
                "record",
                "primary",
                "figure4",
                "prior-full",
                "historical-application",
            ],
            "details": "Corrects#2831; exact current fields discussions[0].rationale and discussions[1].rationale.",
        }
    )
    for finding in review["findings"]:
        finding["previous_occurrences"] = [
            {
                "repository": REPO,
                "review_id": prior["review_id"],
                "finding_id": finding["finding_id"],
            }
        ]
        if finding["finding_id"] == "discussion-coverage":
            finding.update(
                status="resolved",
                disposition_reason="Current exact-record native measurement compares44/44 and matches44/44 under the governed SupportingReference annotations; previous43+1 observation is preserved.",
                title="Current SupportingReference is automatically compared",
                description="The prior record-scoped automatic-coverage gap is resolved in this measured revision; no global closure of#476 or source-truth certification follows.",
            )
    review["actions"] = [
        item for item in review["actions"] if "discussion-coverage" not in item["finding_ids"]
    ]
    metrics = assessments["metrics"]["metrics"]
    for metric in metrics:
        if metric["name"] == "actual_compared_snippets":
            metric.update(
                value=44,
                definition="Actual native matching occurred for all44 unique snippet occurrences; no skipped/unannotated occurrences.",
            )
        elif metric["name"] == "validation_quality":
            metric["definition"] = (
                metric["definition"]
                .replace("'P3': 3", "'P3': 2")
                .replace("clear3open", "clear2open")
            )
    review["limitations"] = [
        item
        for item in review["limitations"]
        if not item.startswith(
            (
                "Native lexical matching",
                "The October discussion intentionally",
                "The other000087/000088",
                "Nine scoped gates",
            )
        )
    ]
    review["limitations"] += [
        "This full current assessment carries the earlier primary-source judgments forward only after proving all scientific assertion fields unchanged outside the accepted discussion/history scope and all primary/supplement/grounding inputs byte-identical. It does not claim a new complete reread of all raw experimental data.",
        "Nine current scoped gates and44 matching snippets do not establish full repository QC or resolve the two scientific uncertainties. The separate M5 aggregate remains separately reported.",
        "Current source differences from the prior full input ledger are exactly the accepted record correction, governed SupportingReference annotations and updated review durability documentation; no primary source was silently refreshed.",
    ]
    review["related_reviews"].append(
        {
            "repository": REPO,
            "review_id": prior["review_id"],
            "relationship": "Full current successor after bounded historical-scope correction and governed annotation measurement; preserves prior evidence/limits and two unresolved scientific findings.",
        }
    )
    review["links"].append("https://github.com/CultureBotAI/CommunityMech/issues/2831")
    (output / "review.yaml").write_text(
        yaml.dump(review, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=96)
    )
    (output / "source-change-audit.json").write_text(
        json.dumps(
            {
                "changes": changes,
                "unchanged_prior_inputs": len(prior["source"]["inputs"]) - len(changes),
            },
            indent=2,
        )
        + "\n"
    )
    print(
        json.dumps(
            {
                "review_id": review["review_id"],
                "assessments": len(review["assessments"]),
                "input_count": len(inspected["source"]["inputs"]),
                "checks": len(review["checks"]),
            }
        )
    )


if __name__ == "__main__":
    main()
