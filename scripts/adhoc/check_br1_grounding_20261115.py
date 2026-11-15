"""Persist the one-record BR1 native canary for #2849, 2026-11-15.

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
STATE = ROOT / ".temp/br1-source-review-20261115"
TARGET = "data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml"
AFTER = "acdadd88a7f7e81eced8c1d229709ba94023dde7e7f72f3238f483685b4c2236"
BEFORE = "c0326c5cdaf678c922659c33dbe4fe1b5717be2bf79dab54d672f160574c0fe5"
CLAW = Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw")
CLAW_REVISION = "23899092a4a2aedf53ff4435c0bdc03ebd79e6be"
SLUG = "Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline"
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
    if (
        head() != args.expected_revision
        or sha(ROOT / TARGET) != AFTER
        or sha(applied) != args.expected_receipt_sha256
    ):
        raise ValueError("actual accepted application/revision required")
    receipt = json.loads(applied.read_bytes())
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
        Path(__file__),
        ROOT / "uv.lock",
        ROOT / "justfile",
        ROOT / "src/communitymech/schema/communitymech.yaml",
        ROOT / "src/communitymech/schema/history.yaml",
        *(ROOT / name for name in receipt["inputs"]),
    ]
    for name, expected in receipt["inputs"].items():
        source = (ROOT / name).resolve()
        if not source.is_relative_to(ROOT) or sha(source) != expected:
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
                    "taxonomy,description,curation_history",
                    "--actor-name",
                    "codex",
                    "--model",
                    "gpt-6",
                    "--agent-tool",
                    "codex",
                    "--issue",
                    "https://github.com/CultureBotAI/CommunityMech/issues/2849",
                    "--pr",
                    "https://github.com/CultureBotAI/CommunityMech/pull/2856",
                    "--summary",
                    "Ground BR1 through its exact assembly and explicit GTDB R220 history",
                    "--details",
                    "Applied only the reviewed GTDB block and one description identifier "
                    "plus native inline history. NCBI assembly GCF_002812725.1 / GCA_002812725.1 "
                    "links exact strain BR1, NCBITaxon:1070896 and SAMN07351343; explicit GTDB "
                    "R220 history assigns Microbacterium sp002812725. The native crosswalk has no "
                    "BR1 row; this independently curated genome mapping asserts no crosswalk "
                    "population counts. Preserve all experimental claims, source quotations, "
                    "graph, discussions and prior history. This is a scoped grounding correction, "
                    "not a full-record scientific review. Actual application receipt "
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
