#!/usr/bin/env python3
"""Recover the M5 stopped-work scope for the 2026-11-14 completion review.

Inputs: read-only M5 session excerpts, local Git history/reviews, public GitHub
issue/PR metadata via gh. Outputs: reports/m5-completion-20261114/scope.{json,md}.
Serves the resumed PR #2102 QC/scientific-review task. No remote writes, session
input, curation edits, publication, or goal changes. Created 2026-11-14.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path

STOPPED = "61392371875097d7de2efaf34acf59274b361427"
SCHEMA_MERGE = "b0a9df35188b40081a3ba8f354ee3b024f8276ad"
SURVIVOR = "reviews/structured/20261106T211930Z-ecofab-ring-trial-current-main/review.yaml"
PROVENANCE = (
    "reviews/structured/20261106T213141Z-pr2062-complete-current-input-provenance/review.yaml"
)
ISSUE_NUMBERS = [622, 1427, 1548, 2429, 2430, 2674, 2675, 2676, *range(2700, 2711)]
AUDITED_OWNERS = [
    "src/communitymech/validators/related_communities.py",
    "src/communitymech/schema/communitymech.yaml",
    "src/communitymech/templates/_partials/host_soil_related.html",
    "src/communitymech/render.py",
    "references_cache/PMID_42660928.md",
]


def run(argv: list[str], cwd: Path | None = None) -> str:
    return subprocess.run(argv, cwd=cwd, text=True, capture_output=True, check=True).stdout


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def remote(command: str, host: str) -> str:
    return run(
        [
            "ssh",
            "-o",
            "BatchMode=yes",
            "-o",
            "ConnectTimeout=8",
            host,
            "PATH=/opt/homebrew/bin:/usr/local/bin:$PATH; " + command,
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reuse-snapshot", action="store_true")
    parser.add_argument("--refresh-github", action="store_true")
    parser.add_argument("--host", help="Private SSH hostname; required for fresh capture")
    parser.add_argument("--session", help="Private retained session path")
    parser.add_argument("--remote-repo", help="Private original checkout path")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    out = repo / "reports/m5-completion-20261114"
    out.mkdir(parents=True, exist_ok=True)
    snapshot_path = out / "scope.json"
    private_path = repo / ".temp/m5-completion-20261114/scope-private.json"
    private_path.parent.mkdir(parents=True, exist_ok=True)
    previous = (
        json.loads(snapshot_path.read_text())
        if args.reuse_snapshot or args.refresh_github
        else None
    )
    if previous:
        if "user_instructions" in previous["session_evidence"] and not private_path.exists():
            with private_path.open("x") as handle:
                json.dump(previous, handle, indent=2)
                handle.write("\n")
        private = json.loads(private_path.read_text())
        session_evidence = private["session_evidence"]
        issues = previous["github"]["issues"]
        github_checked_at = previous["github"]["checked_at"]
        schema_pr = previous["github"].get("schema_pr")
    else:
        if not all([args.host, args.session, args.remote_repo]):
            parser.error("Fresh capture requires --host, --session and --remote-repo")
        selector = (
            'select(.type=="response_item" and .payload.type=="message" '
            'and .payload.role=="user") | .payload.content[]? | .text // empty | '
            'select(startswith("The canary is verified on GitHub:") '
            'or startswith("The user wants your 16 open batch-review PRs"))'
        )
        prompts = remote(
            "jq -r " + shlex.quote(selector) + " " + shlex.quote(args.session), args.host
        )
        final_selector = (
            'select(.type=="event_msg" and .payload.type=="task_complete") '
            "| .payload.last_agent_message"
        )
        final_handoff = remote(
            "tail -n 100 " + shlex.quote(args.session) + " | jq -r " + shlex.quote(final_selector),
            args.host,
        )
        assert "### Phase 2" in prompts and "skip batches 17–46" in prompts
        assert "Phase 2 stopped" in final_handoff and "#2700–#2710" in final_handoff
        old_handoffs = [
            ".temp/batch-publication-20261105/progress.json",
            ".temp/pr-2102-schema-followups/.temp/pr2102/stopped-handoff.json",
        ]
        absence = remote("ls -la " + shlex.quote(args.remote_repo + "/.temp"), args.host)
        session_evidence = {
            "host": args.host,
            "session_path": args.session,
            "selection": "Two explicit user instructions and final task_complete from last 100 rows",
            "user_instructions": prompts,
            "user_instructions_sha256": digest(prompts.encode()),
            "final_handoff": final_handoff,
            "final_handoff_sha256": digest(final_handoff.encode()),
            "missing_original_handoffs": old_handoffs,
            "absence_scope": "ls -la of original .temp includes ignored and hidden entries; empty",
            "absence_command_output": absence,
        }
    if not previous or args.refresh_github:
        fields = (
            "number title state url body closedAt updatedAt "
            "closedByPullRequestsReferences(first:20,includeClosedPrs:true) "
            "{nodes{number title state url mergedAt mergeCommit{oid}}}"
        )
        query = 'query{repository(owner:"CultureBotAI",name:"CommunityMech") {'
        query += " ".join(f"i{n}:issue(number:{n}){{{fields}}}" for n in ISSUE_NUMBERS)
        query += (
            " schema_pr:pullRequest(number:2102) "
            "{number title state url body mergedAt mergeCommit{oid}}"
        )
        query += "}}"
        github = json.loads(run(["gh", "api", "graphql", "-f", "query=" + query], cwd=repo))
        if github.get("errors"):
            raise RuntimeError(github["errors"])
        issues = [
            value for key, value in github["data"]["repository"].items() if key.startswith("i")
        ]
        schema_pr = github["data"]["repository"]["schema_pr"]
        github_checked_at = datetime.now(timezone.utc).isoformat()

    def git(*argv: str) -> str:
        return run(["git", *argv], cwd=repo).strip()

    current = git("rev-parse", "HEAD")
    paths = git(
        "diff-tree", "--no-commit-id", "--name-only", "-r", SCHEMA_MERGE, "--", "kb/communities"
    ).splitlines()
    records = []
    for path in paths:
        content = (repo / path).read_bytes()
        identifier = re.search(rb"^id: (.+)$", content, re.MULTILINE).group(1).decode()
        label = re.search(rb"^name: (.+)$", content, re.MULTILINE).group(1).decode()
        stopped_bytes = run(["git", "show", f"{STOPPED}:{path}"], cwd=repo).encode()
        records.append(
            {
                "id": identifier,
                "path": path,
                "label": label,
                "current_sha256": digest(content),
                "stopped_sha256": digest(stopped_bytes),
                "changed_since_stopped_checkout": content != stopped_bytes,
                "selection_reason": "Maintained record changed by merged schema PR2102",
            }
        )
    assert len(records) == 4, "Do not silently broaden or narrow the frozen PR2102 scope"
    findings = [
        {
            "key": "cm-000025-causal-role-evidence",
            "severity": "major",
            "issues": [1427],
            "summary": "Treatment outcomes exceed member-specific causal/role evidence",
        },
        {
            "key": "cm-000025-study-stage-scope",
            "severity": "major",
            "issues": [1427],
            "summary": "Ring trial, related nitrogen/light studies and preparation assays conflated",
        },
        {
            "key": "cm-000025-grounding-provenance",
            "severity": "minor",
            "issues": [2674],
            "summary": "OAP107 rank refinement and unsupported mapping build/latest wording",
        },
        {
            "key": "cm-000025-genome-identifiers",
            "severity": "minor",
            "issues": [2675],
            "summary": "Genome pseudo-range omits OAE908 Gp0440934 and is not all17 projects",
        },
        {
            "key": "cm-000025-cache-content-type",
            "severity": "minor",
            "issues": [2676],
            "summary": "Two abstract_only headers contradict appended full-main content",
        },
    ]
    caches = ["references_cache/PMID_40920748.md", "references_cache/doi_10.1126_sciadv.adg7888.md"]
    file_evidence = []
    for path in [SURVIVOR, PROVENANCE, *caches, *AUDITED_OWNERS]:
        content = (repo / path).read_bytes()
        historical = run(["git", "show", f"{STOPPED}:{path}"], cwd=repo).encode()
        file_evidence.append(
            {
                "path": path,
                "sha256": digest(content),
                "changed_since_stopped_checkout": content != historical,
            }
        )
    result = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repository": "CultureBotAI/CommunityMech",
        "current_revision": current,
        "current_branch": git("branch", "--show-current"),
        "stopped_revision": STOPPED,
        "schema_pr": {"number": 2102, "merge_revision": SCHEMA_MERGE},
        "session_evidence": session_evidence,
        "scientific_scope": records,
        "selection_basis": "Original Phase2A and exact four-record PR2102 Git diff",
        "excluded_scope": [
            "Original all-unreviewed-record goal was explicitly superseded",
            "Batches 17–46 skipped at explicit user direction; do not restore deleted tmp clones",
            "Completed Phase 1 review-publication batch 16 is not an unfinished ten-record batch",
            "Full repository technical QC does not imply full-corpus scientific review",
        ],
        "broader_phase2_followups": [
            "Named treatment arms referenced by abundances/interactions",
            "EnvironmentalFactor ontology term slot (existing issue #2429)",
            "KGX support for host/soils/related_communities (existing issue #2430)",
            "Issue #1548 strain roster for CommunityMech:000087",
        ],
        "historical_stop": {
            "validator_issue": 622,
            "record": "CommunityMech:000219",
            "reason": "Reference validator stripped [NiFe] from an unchanged quote",
            "partial_audit_issues": list(range(2700, 2711)),
            "followup_implementation_committed": False,
        },
        "surviving_ecofab_findings": findings,
        "file_evidence": file_evidence,
        "github": {"checked_at": github_checked_at, "issues": issues, "schema_pr": schema_pr},
        "completion_criteria": [
            "Run full required technical QC on current revision and preserve exact commands/results",
            "Canary one current record, then independently assess remaining three with primary sources",
            "Save immutable native scientific reviews with claim/participant/direction/context evidence",
            "Carry exact prior issue keys/occurrences and test each acceptance criterion",
            "Reconcile later changes and existing issues; no duplicate issue creation",
            "Report broader Phase2 schema/export implementation separately; do not claim it complete",
        ],
        "limitations": [
            "This scope reconstruction is not a scientific assessment or QC result",
            "Closed GitHub state alone does not prove remediation; inspect linked code and evidence",
            "Historical scratch evidence is unavailable; retained hashes do not reconstruct missing bytes",
        ],
    }
    if not private_path.exists():
        with private_path.open("x") as handle:
            json.dump(result, handle, indent=2)
            handle.write("\n")
    result["session_evidence"] = {
        "source": "preserved M5 session",
        "selection": session_evidence["selection"],
        "user_instructions_sha256": session_evidence["user_instructions_sha256"],
        "final_handoff_sha256": session_evidence["final_handoff_sha256"],
        "missing_original_handoffs": session_evidence["missing_original_handoffs"],
        "absence_scope": session_evidence["absence_scope"],
        "private_capture": "Retained separately in ignored working evidence; excluded from publication",
    }
    snapshot_path.write_text(json.dumps(result, indent=2) + "\n")
    lines = [
        "# M5 CommunityMech stopped-work scope reconstruction",
        "",
        f"Generated {result['generated_at']}; current revision `{current}`.",
        "",
        "The unfinished scientific scope is the four maintained records changed by PR #2102. "
        "The retained session explicitly superseded its original all-unreviewed-record goal, "
        "skipped batches 17–46, and completed the 15-PR publication phase. The last ten-record "
        "publication batch does not define the remaining scientific work.",
        "",
        f"PR #2102 had already merged as `{SCHEMA_MERGE}`. Its partial audit stopped after "
        "the separate corpus reference check reproduced issue #622 on unchanged record 000219; "
        "the handoff retained #2700–#2710 and #1548. These are historical findings, reconciled "
        "against the current GitHub states below.",
        "",
        "## Frozen scientific target set",
        "",
        "| Record | Maintained path | Changed since stopped checkout |",
        "| --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            f"| {record['id']} | `{record['path']}` | "
            f"{record['changed_since_stopped_checkout']} |"
        )
    lines += [
        "",
        "## Surviving EcoFAB review",
        "",
        f"`{SURVIVOR}` remains the authoritative retained review. It records four old "
        "open curation findings plus a fifth cache-header finding despite eight focused "
        "checks passing. Its original Git base is `31c456d35d214662bf435750b783a762d59a22df`.",
        "",
    ]
    for finding in findings:
        owners = ", ".join(f"#{n}" for n in finding["issues"])
        lines.append(
            f"- `{finding['key']}` ({finding['severity']}; {owners}): {finding['summary']}."
        )
    lines += [
        "",
        "The exact target and two cited cache files were compared byte-for-byte with "
        "the stopped revision; the JSON records hashes and change flags. Technical checks "
        "and provenance-only review bundles do not resolve scientific findings.",
        "",
        "## Current issue and linked PR state",
        "",
        f"Read from GitHub at {github_checked_at}. Closed states require separate "
        "acceptance verification before being treated as resolved.",
        "",
        "| Issue | State | Subject | Linked closing PRs |",
        "| --- | --- | --- | --- |",
    ]
    for issue in issues:
        prs = issue["closedByPullRequestsReferences"]["nodes"]
        links = ", ".join(f"[#{p['number']}]({p['url']}) ({p['state']})" for p in prs)
        title = issue["title"].replace("|", "\\|")
        lines.append(
            f"| [#{issue['number']}]({issue['url']}) | {issue['state']} | {title} | "
            f"{links or 'None returned by GitHub closure linkage'} |"
        )
    owner_changes = [
        row["path"]
        for row in file_evidence
        if row["path"] in AUDITED_OWNERS and row["changed_since_stopped_checkout"]
    ]
    lines += ["", "## Reconciliation against current code", ""]
    if not owner_changes:
        lines += [
            "All five maintained owner files for the eleven PR #2102 findings are unchanged "
            "from the stopped revision: related-community validation, schema, host/soil template, "
            "renderer, and Ding article cache. All four maintained target records are also "
            "unchanged. No remediation is present in these identified owner files across the "
            "compared revision range. This verifies unchanged inputs; the historical synthetic "
            "counterexamples and any dependency-mediated behavior have not been rerun here."
        ]
    else:
        lines += [
            "Changed owner files require fresh acceptance assessment: " + ", ".join(owner_changes)
        ]
    lines += ["", "## Broader Phase2 work retained separately", ""]
    lines += [f"- {item}." for item in result["broader_phase2_followups"]]
    lines += [
        "",
        "These original implementation requirements remain outside a claim that four "
        "scientific assessments and technical QC are complete. Current issue state above "
        "must determine which remain open; neither this report nor a green gate implements them.",
        "",
        "## Completion evidence required",
        "",
    ]
    lines += [f"- {item}." for item in result["completion_criteria"]]
    lines += [
        "",
        "## Recovery provenance and limits",
        "",
        "Source: preserved M5 session. Raw private instructions and the stopped-work handoff "
        "are retained separately in ignored working evidence. Public `scope.json` contains "
        "excerpt digests, reconstructed scope, target hashes, Git selection and public GitHub facts.",
        f"Instruction excerpt SHA256: `{session_evidence['user_instructions_sha256']}`.",
        f"Final handoff excerpt SHA256: `{session_evidence['final_handoff_sha256']}`.",
        "",
        "The original `.temp` directory was inspected with `ls -la`, including hidden "
        "and ignored entries; it was empty. Both referenced handoffs are unavailable. "
        "No old scratch was recreated or treated as current evidence.",
        "",
    ]
    lines += [f"- {item}." for item in result["limitations"]]
    (out / "scope.md").write_text("\n".join(lines) + "\n")
    print(
        json.dumps(
            {
                "records": len(records),
                "issues": len(issues),
                "scope_json": str(snapshot_path),
                "scope_md": str(out / "scope.md"),
            }
        )
    )


if __name__ == "__main__":
    main()
