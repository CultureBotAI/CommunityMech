"""Persist the one-record JMP134 native canary for #2848, 2026-11-15.

Inputs: fixed accepted record, hash-bound actual application and exact code HEAD.
Outputs: exclusive private gate log/exit/receipt and native append-only history.
No source acquisition or claim-level reference approval is performed.
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-species-status-20261115"
TARGET = "data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml"
AFTER = "fede5211f0911d1a0543f1e19f8c53bf4c6dfc4ee306a6a3b8ee5d184ed7e786"
BEFORE = "429964cbf945c41b2e89b57a072718158cf674e03786ef34b1ef96fe9247995e"
CLAW = Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw")
CLAW_REVISION = "23899092a4a2aedf53ff4435c0bdc03ebd79e6be"
SLUG = "Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline"
HISTORY = "history/records/" + SLUG
RECIPES = {
    "schema": "validate",
    "strict": "validate-strict",
    "gtdb": "validate-gtdb",
    "domain": "validate-gtdb-domain",
    "scalars": "validate-scalars",
    "history": "validate-history",
    "new-history": "new-history",
    "terms": "validate-terms",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def head(root=ROOT):
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gate", choices=RECIPES)
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--applied-receipt", type=Path, required=True)
    parser.add_argument("--expected-receipt-sha256", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric exclusive attempt required")
    output = STATE / f"canary-{'plan' if args.plan else 'run'}-{args.gate}-{args.attempt}"
    applied = args.applied_receipt.resolve()
    if output.exists() or not applied.is_relative_to(STATE):
        raise ValueError("exclusive private output and retained application required")
    raw_applied = applied.read_bytes()
    if (
        head() != args.expected_revision
        or sha(ROOT / TARGET) != AFTER
        or hashlib.sha256(raw_applied).hexdigest() != args.expected_receipt_sha256
    ):
        raise ValueError("actual accepted application/revision required")
    receipt = json.loads(raw_applied)
    if (
        receipt["applied"] is not True
        or receipt["execution_revision"] != args.expected_revision
        or receipt["target"] != TARGET
        or receipt["before_sha256"] != BEFORE
        or receipt["after_sha256"] != AFTER
    ):
        raise ValueError("actual bounded application receipt required")
    paths = [
        ROOT / TARGET,
        applied,
        applied.parent / "before.yaml",
        Path(__file__),
        ROOT / "uv.lock",
        ROOT / "justfile",
        ROOT / "src/communitymech/schema/communitymech.yaml",
        ROOT / "src/communitymech/schema/history.yaml",
        *(ROOT / name for name in receipt["inputs"]),
    ]
    if sha(applied.parent / "before.yaml") != BEFORE:
        raise ValueError("actual preserved pre-application record differs")
    for name, expected in receipt["inputs"].items():
        source = (ROOT / name).resolve()
        expected_now = AFTER if name == TARGET else expected
        if not source.is_relative_to(ROOT) or sha(source) != expected_now:
            raise ValueError("reviewed application input changed: " + name)
    if args.gate in RECIPES:
        command = ["just", "--verbose", "--no-dotenv", "--color", "never"]
        if args.plan:
            command.append("--dry-run")
        command.append(RECIPES[args.gate])
        if args.gate == "new-history":
            if head(CLAW) != CLAW_REVISION:
                raise ValueError("native history scaffolder changed")
            paths.extend(sorted((CLAW / "src/kg_microbe_history").glob("*.py")))
            paths.append(CLAW / "src/kg_microbe_governance/artifacts/schema/history.yaml")
            command.extend(
                [
                    "--kind",
                    "record",
                    "--slug",
                    SLUG,
                    "--target-root",
                    "data/isolates",
                    "--event",
                    "EDIT",
                    "--outcome",
                    "changed",
                    "--sections",
                    "taxonomy,curation_history",
                    "--actor-name",
                    "codex",
                    "--model",
                    "gpt-6",
                    "--agent-tool",
                    "codex",
                    "--issue",
                    "https://github.com/CultureBotAI/CommunityMech/issues/2848",
                    "--summary",
                    "Ground exact JMP134 stock through its native NCBI crosswalk row",
                    "--details",
                    "Applied only the reviewed native GTDB block, GROUNDED status and two "
                    "native inline events. Exact crosswalk SHA256761d5537a7edb4b0133e88e7bbc85570"
                    "cf3cb6f2555b9f9ce6cca3e1056a0ddd row71828 maps unchanged NCBITaxon264198 "
                    "strain JMP134 to GTDB:s__Cupriavidus_pinatubonensis, one genome and fraction1. "
                    "The primary C.necator JMP134 name is a retained NCBI synonym of canonical "
                    "C.pinatubonensis JMP134. No formal nomenclatural event, other stock identity "
                    "or additional genome population is inferred. All experimental claims, "
                    "source quotations, graph, open paralog-expression discussion and prior "
                    "history remain unchanged. This is a scoped database correction, not a "
                    "full-record scientific review. Actual application receipt "
                    + str(applied.relative_to(ROOT))
                    + " sha256:"
                    + args.expected_receipt_sha256
                    + ".",
                ]
            )
        else:
            command.append(HISTORY if args.gate == "history" else TARGET)
        if args.gate == "strict":
            command.extend(["--out", str((output / "strict.tsv").relative_to(ROOT))])
    before_sidecars = {
        str(path.relative_to(ROOT)): sha(path) for path in (ROOT / HISTORY).glob("*.yaml")
    }
    paths.extend(ROOT / path for path in before_sidecars)
    bound = {str(path): sha(path) for path in paths}
    if applied.read_bytes() != raw_applied:
        raise ValueError("actual application receipt changed while binding")
    env = dict(os.environ)
    env.update(
        PATH="/Users/marcin/.local/bin:/opt/homebrew/bin:/usr/bin:/bin",
        UV_NO_SYNC="true",
        UV_OFFLINE="true",
        JUST_NO_DOTENV="true",
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONUNBUFFERED="1",
        PYSTOW_HOME="/Users/marcin/.data",
        CLAW_SRC=str(CLAW / "src"),
        KG_MICROBE_DIR=str(STATE / "kg-microbe"),
    )
    output.mkdir()
    data = {
        "started_at": now(),
        "revision": args.expected_revision,
        "python": sys.version,
        "python_executable": sys.executable,
        "command": command,
        "plan": args.plan,
        "inputs": bound,
        "history_scaffolder_revision": CLAW_REVISION if args.gate == "new-history" else None,
    }
    (output / "start.json").write_text(json.dumps(data, indent=2) + "\n")
    with (output / "native.log").open("xb") as stream:
        result = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT)
    (output / "native.exit").write_text(str(result.returncode) + "\n")
    if bound != {str(path): sha(path) for path in paths} or head() != args.expected_revision:
        raise ValueError("execution inputs changed during native command")
    if args.gate == "new-history" and head(CLAW) != CLAW_REVISION:
        raise ValueError("native scaffolder changed during command")
    after_sidecars = {
        str(path.relative_to(ROOT)): sha(path) for path in (ROOT / HISTORY).glob("*.yaml")
    }
    new_sidecars = {
        path: digest for path, digest in after_sidecars.items() if path not in before_sidecars
    }
    if (
        args.gate == "new-history"
        and not args.plan
        and result.returncode == 0
        and len(new_sidecars) != 1
    ):
        raise ValueError("successful history command must persist one new sidecar")
    if not (output / "native.log").stat().st_size:
        raise ValueError("native command produced no retained output")
    data.update(
        finished_at=now(),
        exit_code=result.returncode,
        log_sha256=sha(output / "native.log"),
        log_bytes=(output / "native.log").stat().st_size,
        new_history_sidecars=new_sidecars,
        execution_inputs_unchanged=True,
    )
    with (output / "receipt.json").open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")
    print(json.dumps(data, indent=2))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
