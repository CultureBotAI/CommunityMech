"""Retain one-record native history/check receipts for #2848, 2026-11-15.

Inputs: exact reviewed/applied ambiguity bytes, frozen code and raw receipt.
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
STATE = ROOT / ".temp/gtdb-ambiguity-20261115"
REVISION = "4a5999d5f9299a26e1aff0ffc1262bfff03a035f"
TARGET = "data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml"
BEFORE = "b6dc768bf6f705611933fc50882d91957225ef1e32c61330e1adb717fe175790"
AFTER = "d1843b01c495ca1a2c44820435e3a60b76e65089eff627590c26b5d0e003bcb6"
APPLIED = STATE / "ambiguity-apply-001/receipt.json"
APPLIED_SHA = "9aae41ac2845de3d650de74e2913d0b469c30fc8fddd332eb70eb9fa8293e785"
CLAW = Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw")
CLAW_REVISION = "23899092a4a2aedf53ff4435c0bdc03ebd79e6be"
HISTORY = "history/records/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline"
RECIPES = {
    "schema": "validate",
    "strict": "validate-strict",
    "gtdb": "validate-gtdb",
    "domain": "validate-gtdb-domain",
    "scalars": "validate-scalars",
    "terms": "validate-terms",
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
    output = STATE / f"ambiguity-canary-{'plan' if args.plan else 'run'}-{args.gate}-{args.attempt}"
    if output.exists() or output.is_symlink():
        raise ValueError("refusing to overwrite prior command artifacts")
    applied_raw = APPLIED.read_bytes()
    if (
        head() != REVISION
        or sha(ROOT / TARGET) != AFTER
        or hashlib.sha256(applied_raw).hexdigest() != APPLIED_SHA
    ):
        raise ValueError("actual reviewed application/revision required")
    receipt = json.loads(applied_raw)
    if (
        receipt["applied"] is not True
        or receipt["execution_revision"] != REVISION
        or receipt["before_sha256"] != BEFORE
        or receipt["after_sha256"] != AFTER
    ):
        raise ValueError("actual M5 application required")
    paths = [
        ROOT / TARGET,
        APPLIED,
        APPLIED.with_name("before.yaml"),
        ROOT / "uv.lock",
        ROOT / "justfile",
        ROOT / "src/communitymech/schema/communitymech.yaml",
        ROOT / "src/communitymech/schema/history.yaml",
        Path(__file__),
        *(ROOT / name for name in receipt["inputs"]),
    ]
    history_before = {
        str(path.relative_to(ROOT)): sha(path) for path in (ROOT / HISTORY).glob("*.yaml")
    }
    if args.gate in {"history", "new-history"}:
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
                "Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline",
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
                "--pr",
                "https://github.com/CultureBotAI/CommunityMech/pull/2804",
                "--summary",
                "Retain all native GTDB alternatives for the existing species descriptor",
                "--details",
                f"Applied the independently reviewed status-only M5 candidate SHA256 {AFTER}. "
                "PMID:42655156 Methods2.1 identifies A2-165 as JCM31915, using the source name "
                "Faecalibacterium prausnitzii. The exact "
                "NCBI2GTDB snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd "
                "returns three alternatives for the existing NCBITaxon:853 species descriptor: "
                "Faecalibacterium longum, Faecalibacterium prausnitzii and Faecalibacterium prausnitzii_D. "
                "Persist AMBIGUOUS and the complete native list without selecting a species, "
                "reidentifying A2-165, changing its stock designation, or modifying any biology, graph, "
                "source quotation or historical batch146 ledger. The cited literature also uses "
                "Faecalibacterium duncaniae for A2-165; stock-specific nomenclature/genome identity "
                "remains outside this computability correction. Actual raw application receipt "
                f".temp/gtdb-ambiguity-20261115/ambiguity-apply-001/receipt.json SHA256 {APPLIED_SHA}. "
                "A scoped diagnostic assessment and actual native focused gates follow.",
            ]
        )
    else:
        command.append(HISTORY if args.gate == "history" else TARGET)
    if args.gate == "strict":
        command.extend(["--out", str((output / "strict.tsv").relative_to(ROOT))])
    captures = {APPLIED: applied_raw}
    for path in paths:
        if path not in captures:
            captures[path] = path.read_bytes()
    bound = {str(path): hashlib.sha256(raw).hexdigest() for path, raw in captures.items()}
    if bound[str(ROOT / TARGET)] != AFTER:
        raise ValueError("captured canonical bytes differ from accepted application (#2865)")
    if bound[str(APPLIED.with_name("before.yaml"))] != BEFORE:
        raise ValueError("persisted actual predecessor bytes changed")
    for name, expected in receipt["inputs"].items():
        if name == TARGET:
            if expected != BEFORE:
                raise ValueError("actual application predecessor binding changed")
            continue
        if bound[str(ROOT / name)] != expected:
            raise ValueError("reviewed application input changed: " + name)
    if any(path.read_bytes() != raw for path, raw in captures.items()):
        raise ValueError("reviewed source changed before native command")
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
        "history_before": history_before,
    }
    (output / "start.json").write_text(json.dumps(data, indent=2) + "\n")
    with (output / "native.log").open("xb") as stream:
        result = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT)
    (output / "native.exit").write_text(str(result.returncode) + "\n")
    if bound != {str(path): sha(path) for path in paths} or head() != REVISION:
        raise ValueError("execution inputs changed during native command")
    if args.gate == "new-history" and head(CLAW) != CLAW_REVISION:
        raise ValueError("history scaffolder changed during native command")
    history_after = {
        str(path.relative_to(ROOT)): sha(path) for path in (ROOT / HISTORY).glob("*.yaml")
    }
    if any(history_after.get(path) != expected for path, expected in history_before.items()):
        raise ValueError("existing history changed")
    new_history = {
        path: value for path, value in history_after.items() if path not in history_before
    }
    expected_new = int(args.gate == "new-history" and not args.plan and result.returncode == 0)
    if len(new_history) != expected_new:
        raise ValueError("unexpected native sidecar count")
    if not (output / "native.log").stat().st_size:
        raise ValueError("native command produced no retained output")
    data.update(
        finished_at=now(),
        exit_code=result.returncode,
        log_sha256=sha(output / "native.log"),
        log_bytes=(output / "native.log").stat().st_size,
        history_created=new_history,
    )
    with (output / "receipt.json").open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")
    print(json.dumps(data, indent=2))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
