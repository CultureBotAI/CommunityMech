"""Retain one-record native history/check receipts for #2849, 2026-11-15.

Inputs: exact reviewed/applied Sulfobacillus bytes, frozen code and raw receipt.
Outputs: exclusive private per-command artifacts; only new-history creates a
canonical append-only sidecar. No references acquisition or other record edits.
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
STATE = ROOT / ".temp/gtdb-source-routes-2849-20261115"
REVISION = "cb642708f04b12d3a30ecdb662854dd26816014c"
TARGET = "kb/communities/Industrial_Bioreactor_Consortium.yaml"
AFTER = "24c55ff3c29b21fa5988c4859fdcccfacc52caf62a1902cb28887b68780f551e"
APPLIED = STATE / "sulfobacillus-applied-m5-001/receipt.json"
APPLIED_SHA = "ee8f6aec6f076b02c80539d3d47fc1a694274d6de97ca68145131910add33066"
CLAW = Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw")
CLAW_REVISION = "23899092a4a2aedf53ff4435c0bdc03ebd79e6be"
HISTORY = "history/records/Industrial_Bioreactor_Consortium"
RECIPES = {
    "schema": "validate",
    "strict": "validate-strict",
    "gtdb": "validate-gtdb",
    "domain": "validate-gtdb-domain",
    "scalars": "validate-scalars",
    "history": "validate-history",
    "new-history": "new-history",
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
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric exclusive attempt required")
    output = STATE / f"canary-{'plan' if args.plan else 'run'}-{args.gate}-{args.attempt}"
    if output.exists() or output.is_symlink():
        raise ValueError("refusing to overwrite prior command artifacts")
    if head() != REVISION or sha(ROOT / TARGET) != AFTER or sha(APPLIED) != APPLIED_SHA:
        raise ValueError("actual reviewed application/revision required")
    receipt = json.loads(APPLIED.read_bytes())
    if receipt["applied"] is not True or receipt["execution_revision"] != REVISION:
        raise ValueError("actual M5 application required")
    paths = [
        ROOT / TARGET,
        APPLIED,
        ROOT / "uv.lock",
        ROOT / "justfile",
        ROOT / "src/communitymech/schema/communitymech.yaml",
        ROOT / "src/communitymech/schema/history.yaml",
        Path(__file__),
        *(ROOT / name for name in receipt["inputs"]),
    ]
    if args.gate == "history":
        paths.extend((ROOT / HISTORY).glob("*.yaml"))
    command = ["just", "--verbose", "--no-dotenv", "--color", "never"]
    if args.plan:
        command.append("--dry-run")
    command.append(RECIPES[args.gate])
    if args.gate == "new-history":
        if head(CLAW) != CLAW_REVISION:
            raise ValueError("native history scaffolder revision changed")
        paths.extend(sorted((CLAW / "src/kg_microbe_history").glob("*.py")))
        paths.append(CLAW / "src/kg_microbe_governance/artifacts/schema/history.yaml")
        command.extend(
            [
                "--kind",
                "record",
                "--slug",
                "Industrial_Bioreactor_Consortium",
                "--target-root",
                "kb/communities",
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
                "https://github.com/CultureBotAI/CommunityMech/issues/2849",
                "--pr",
                "https://github.com/CultureBotAI/CommunityMech/pull/2804",
                "--summary",
                "Reconcile the Sulfobacillus reference-taxon GTDB mapping",
                "--details",
                "Applied the independently reviewed one-block M5 candidate24c55ff3. "
                "Retained NCBI2GTDB snapshot SHA256761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd "
                "has no53633 row; exact species-name rows679936 and1051632 each report2 genomes, "
                "fraction1.0, and Sulfobacillus_A acidophilus. Native name mapping yields4 genomes "
                "and changed GTDB name. Preserve NCBITaxon53633, all biological claims, graphs, "
                "source quotations and historical batch53 review. This is reference-taxon "
                "correspondence, not exact study-strain identification or full scientific approval; "
                "composite-community issue1509 remains unresolved. Actual raw application receipt "
                f".temp/gtdb-source-routes-2849-20261115/sulfobacillus-applied-m5-001/receipt.json SHA256{APPLIED_SHA}. "
                "A scoped diagnostic assessment and actual native focused gates follow.",
            ]
        )
    else:
        command.append(HISTORY if args.gate == "history" else TARGET)
    if args.gate == "strict":
        command.extend(["--out", str((output / "strict.tsv").relative_to(ROOT))])
    bound = {str(path): sha(path) for path in paths}
    for name, expected in receipt["inputs"].items():
        if sha(ROOT / name) != expected:
            raise ValueError("reviewed application input changed: " + name)
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
        "revision": REVISION,
        "python": sys.version,
        "command": command,
        "plan": args.plan,
        "inputs": bound,
        "history_scaffolder_revision": CLAW_REVISION if args.gate == "new-history" else None,
    }
    (output / "start.json").write_text(json.dumps(data, indent=2) + "\n")
    with (output / "native.log").open("xb") as stream:
        result = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT)
    (output / "native.exit").write_text(str(result.returncode) + "\n")
    if bound != {str(path): sha(path) for path in paths} or head() != REVISION:
        raise ValueError("execution inputs changed during native command")
    if args.gate == "new-history" and head(CLAW) != CLAW_REVISION:
        raise ValueError("history scaffolder changed during native command")
    if not (output / "native.log").stat().st_size:
        raise ValueError("native command produced no retained output")
    data.update(
        finished_at=now(),
        exit_code=result.returncode,
        log_sha256=sha(output / "native.log"),
        log_bytes=(output / "native.log").stat().st_size,
    )
    with (output / "receipt.json").open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")
    print(json.dumps(data, indent=2))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
