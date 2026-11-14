"""Publish durable technical receipts for the M5 completion review (2026-11-14).

Inputs: retained native logs, exact exit files, and JSON checkpoints in .temp/.
Outputs: immutable public log/exit/receipt files under reports/.../technical-evidence/.
Preserves original hashes; removes home paths, addresses and credential-shaped
values from public derivatives. Raw evidence remains untouched in both clones.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
OUT = ROOT / "reports/m5-completion-20261114/technical-evidence"
PATTERNS = {
    "email_address": r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+",
    "github_token": r"\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b",
    "api_token": r"\bsk-(?:proj-|ant-api\d+-)?[A-Za-z0-9_-]{20,}\b",
    "aws_access_id": r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "authorization_value": r"(?i)\bBearer\s+[A-Za-z0-9._~+/-]{16,}=*",
    "private_key": r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----[\s\S]*?-----END (?:[A-Z]+ )?PRIVATE KEY-----",
    "credential_assignment": r"(?i)\b(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+~=-]{16,}['\"]?",
    "private_home_path": r"/Users/[^/\s'\"<>]+",
    "private_hostname": r"\b[A-Za-z0-9_-]*(?:MacBook|Mac-mini|Mac-Studio)[A-Za-z0-9_.-]*\b",
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sanitize(text, counts):
    occurrences = text.count(str(ROOT))
    if occurrences:
        counts["repository_absolute_path"] += occurrences
        text = text.replace(str(ROOT), "<REPO>")
    for label, pattern in PATTERNS.items():
        text, count = re.subn(pattern, f"<REDACTED:{label}>", text)
        counts[label] += count
    return text


def immutable(path, data):
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f"refusing to overwrite different public evidence: {path.name}")
    else:
        path.write_bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--name", action="append", help="export only this completed run; repeatable"
    )
    args = parser.parse_args()
    completed = []
    for checkpoint in sorted(STATE.glob("*.json")):
        result = json.loads(checkpoint.read_text(encoding="utf-8"))
        if "command" not in result or "exit_code" not in result:
            continue
        completed.append(result)
    if args.name:
        unknown = set(args.name) - {result["name"] for result in completed}
        if unknown:
            parser.error("unknown or incomplete run names: " + ", ".join(sorted(unknown)))
    OUT.mkdir(parents=True, exist_ok=True)
    for result in completed:
        name = result["name"]
        if args.name and name not in args.name:
            continue
        raw = (ROOT / result["log"]).read_bytes()
        raw_exit = (STATE / f"{name}.exit").read_bytes()
        if not raw or digest(raw) != result["log_sha256"]:
            raise ValueError(f"native log is empty or changed after completion: {name}")
        if int(raw_exit.strip()) != result["exit_code"]:
            raise ValueError(f"exit file disagrees with retained result: {name}")
        counts = Counter()
        public_log = sanitize(raw.decode("utf-8"), counts).encode("utf-8")
        public_result = json.loads(sanitize(json.dumps(result), counts))
        public_result.pop("cwd", None)
        public_result["log"] = f"reports/m5-completion-20261114/technical-evidence/{name}.log.txt"
        if name == "qc-references" and (STATE / "invalid-launcher-interruption.json").exists():
            public_result["attempt_disposition"] = "INVALID LAUNCHER; INTERRUPTED"
        if (
            name == "diagnostic-validate-terms-all"
            and (STATE / "baseline-diagnostic-interruption.json").exists()
        ):
            public_result["attempt_disposition"] = "SUPERSEDED BASELINE; INTERRUPTED"
        public_result["public_evidence"] = {
            "original_log_sha256": digest(raw),
            "public_log_sha256": digest(public_log),
            "original_log_bytes": len(raw),
            "public_log_bytes": len(public_log),
            "redactions": {key: value for key, value in sorted(counts.items()) if value},
            "note": "Only path/privacy/credential-shaped text is replaced; raw logs remain in .temp in both checkouts.",
        }
        immutable(OUT / f"{name}.log.txt", public_log)
        immutable(OUT / f"{name}.exit.txt", raw_exit)
        immutable(
            OUT / f"{name}.receipt.json",
            (json.dumps(public_result, indent=2) + "\n").encode("utf-8"),
        )
    for name in (
        ()
        if args.name
        else (
            "historical-bases-verified",
            "invalid-launcher-interruption",
            "baseline-diagnostic-interruption",
            "baseline-diagnostic-termination",
            "final-sync-plan",
            "final-sync-receipt",
            "final-orchestration-inputs",
        )
    ):
        source = STATE / f"{name}.json"
        if source.exists():
            counts = Counter()
            original = source.read_bytes()
            receipt = {
                "source_sha256": digest(original),
                "receipt": json.loads(sanitize(original.decode("utf-8"), counts)),
                "redactions": {key: value for key, value in sorted(counts.items()) if value},
            }
            immutable(OUT / f"{name}.json", (json.dumps(receipt, indent=2) + "\n").encode())
    # Selection limits new exports, never the index of already published evidence.
    index = [
        json.loads(path.read_text(encoding="utf-8")) for path in sorted(OUT.glob("*.receipt.json"))
    ]
    lines = [
        "# Durable technical evidence",
        "",
        "Each receipt preserves the original native-log SHA-256 and the published derivative SHA-256.",
        "Absolute home paths, email addresses and credential-shaped values are replaced where present.",
        "Raw logs remain in both review checkouts. Failed/interrupted attempts are retained.",
        "Separate diagnostics do not change an aggregate failure or its NOT RUN stages.",
        "",
        "| Run | Status | Exit | Log | Receipt |",
        "|---|---|---:|---|---|",
    ]
    for result in index:
        name = result["name"]
        status = result.get("attempt_disposition", result["status"])
        lines.append(
            f"| {name} | {status} | {result['exit_code']} | [{name}.log.txt]({name}.log.txt) | [JSON]({name}.receipt.json) |"
        )
    (OUT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if not args.name:
        report_lines = [
            "# M5 technical checks",
            "",
            "All logs, exact exits and hash receipts are retained in [technical-evidence](technical-evidence/README.md).",
            "Separate diagnostics do not repair failed aggregates; skipped checks are not passes.",
            "The original baseline is 76aa644cd6803ea2c9545d4c704276ede219d354; each receipt records its actual revision and source status.",
            "",
            "| Run | Status | Exit | Native stage counts |",
            "|---|---|---:|---|",
        ]
        for result in index:
            log = (ROOT / result["log"]).read_text(encoding="utf-8")
            summaries = [
                line
                for line in log.splitlines()
                if re.search(r"\b\d+ (?:passed|failed|skipped).*\bin [0-9.]+s", line)
            ]
            result["pytest_summaries"] = summaries
            result["pytest_counts"] = {
                key: int(value)
                for value, key in re.findall(
                    r"\b(\d+) (passed|failed|skipped|deselected|xfailed|xpassed|errors?)\b",
                    summaries[-1] if summaries else "",
                )
            }
            result["native_stage_counts"] = dict(
                Counter(stage["status"] for stage in result.get("stages", []))
            )
            status = result.get("attempt_disposition", result["status"])
            stage_text = "; ".join(
                f"{key}: {value}" for key, value in result["native_stage_counts"].items()
            )
            report_lines.append(
                f"| [{result['name']}](technical-evidence/{result['name']}.receipt.json) | {status} | {result['exit_code']} | {stage_text} |"
            )
        for result in index:
            report_lines.extend(
                [
                    "",
                    "## " + result["name"],
                    "",
                    f"[Native output](technical-evidence/{result['name']}.log.txt) · [Exact exit](technical-evidence/{result['name']}.exit.txt)",
                    "",
                    "Command: `" + " ".join(result["command"]) + "`",
                    "",
                    *result["pytest_summaries"],
                ]
            )
            if result.get("attempt_disposition") == "INVALID LAUNCHER; INTERRUPTED":
                report_lines.append(
                    "Invalid launcher environment; deliberately interrupted. This is not a repository-failure conclusion."
                )
            elif result.get("attempt_disposition") == "SUPERSEDED BASELINE; INTERRUPTED":
                report_lines.append(
                    "Superseded baseline; deliberately interrupted before final-revision validation. This is not a repository-failure conclusion."
                )
            if result.get("skip_markers"):
                report_lines.extend(["", "```text", *result["skip_markers"], "```"])
            if result.get("stages"):
                report_lines.extend(["", "| Native recipe | Status |", "|---|---|"])
                report_lines.extend(
                    f"| {stage['recipe']} | {stage['status']} |" for stage in result["stages"]
                )
        (OUT.parent / "technical-checks.json").write_text(
            json.dumps({"checks": index}, indent=2) + "\n", encoding="utf-8"
        )
        (OUT.parent / "technical-checks.md").write_text(
            "\n".join(report_lines) + "\n", encoding="utf-8"
        )
    print(
        json.dumps({"public_check_receipts": len(index), "directory": str(OUT.relative_to(ROOT))})
    )


if __name__ == "__main__":
    main()
