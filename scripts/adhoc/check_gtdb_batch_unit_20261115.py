"""Persist one native gate for a reviewed GTDB batch unit, #2848, 2026-11-15.

Inputs: pinned unit/check config and actual apply receipt, exact code revision,
existing local ontology/crosswalk and optional pinned Claw history source.
Outputs: exclusive private command/log/exit/receipt and requested native sidecar.
One identical launcher serves canary and later serial units; no source fetches.
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


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_path(name, *, private=False):
    relative = Path(name)
    resolved = (ROOT / relative).resolve()
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or not resolved.is_relative_to(ROOT / ".temp" if private else ROOT)
        or (ROOT / relative).is_symlink()
    ):
        raise ValueError("safe repository-relative path required")
    return resolved


def head(root=ROOT):
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()


def now():
    return datetime.now(timezone.utc).isoformat()


def capture(captured, location, expected=None):
    if location not in captured:
        captured[location] = location.read_bytes()
    if expected is not None and digest(captured[location]) != expected:
        raise ValueError("accepted input changed: " + location.name)
    return captured[location]


def run(config_name, config_sha, gate, output_name, revision, *, plan=False, claw=None):
    output = safe_path(output_name, private=True)
    if output.exists() or head() != revision:
        raise ValueError("exclusive private output and exact revision required")
    captured = {}
    config = json.loads(capture(captured, safe_path(config_name), config_sha))
    target = safe_path(config["target"])
    if not config["target"].startswith(("kb/communities/", "data/isolates/")):
        raise ValueError("declared community target root required")
    after, before = config["after_sha256"], config["before_sha256"]
    capture(captured, target, after)
    applied_path = safe_path(config["application_receipt"], private=True)
    applied = json.loads(capture(captured, applied_path, config["application_receipt_sha256"]))
    if (
        applied["applied"] is not True
        or applied["execution_revision"] != revision
        or applied["target"] != config["target"]
        or applied["before_sha256"] != before
        or applied["after_sha256"] != after
    ):
        raise ValueError("actual accepted application differs")
    capture(captured, applied_path.with_name("before.yaml"), before)
    for name, expected in applied["inputs"].items():
        capture(captured, safe_path(name), after if name == config["target"] else expected)
    capture(captured, Path(__file__))
    for name in (
        "uv.lock",
        "justfile",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/history.yaml",
    ):
        capture(captured, ROOT / name)
    # This checks the captured target, not merely an earlier/read-later digest.
    if digest(captured[target]) != after:
        raise ValueError("captured target differs from accepted AFTER")
    slug = target.stem
    history = "history/records/" + slug
    before_sidecars = {
        str(location.relative_to(ROOT)): digest(capture(captured, location))
        for location in sorted((ROOT / history).glob("*.yaml"))
    }
    command = ["just", "--verbose", "--no-dotenv", "--color", "never"]
    if plan:
        command.append("--dry-run")
    command.append(RECIPES[gate])
    if gate == "new-history":
        if claw is None or head(claw) != config["history_scaffolder_revision"]:
            raise ValueError("exact native history checkout required")
        for location in sorted((claw / "src/kg_microbe_history").glob("*.py")):
            capture(captured, location)
        capture(captured, claw / "src/kg_microbe_governance/artifacts/schema/history.yaml")
        command.extend(
            [
                "--kind",
                "record",
                "--slug",
                slug,
                "--target-root",
                str(Path(config["target"]).parent),
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
                config["issue"],
                "--summary",
                config["history_summary"],
                "--details",
                config["history_details"]
                + " Actual apply receipt "
                + config["application_receipt"]
                + " sha256:"
                + config["application_receipt_sha256"]
                + ".",
            ]
        )
    else:
        command.append(history if gate == "history" else config["target"])
    if gate == "strict":
        command.extend(["--out", str((output / "strict.tsv").relative_to(ROOT))])
    if head() != revision or any(
        location.read_bytes() != raw for location, raw in captured.items()
    ):
        raise ValueError("captured inputs changed before native launch")
    table = safe_path(config["crosswalk"], private=True)
    if table not in captured or digest(captured[table]) != config["crosswalk_sha256"]:
        raise ValueError("actual reviewed crosswalk must be captured")
    env = dict(os.environ)
    env.update(
        PATH=str(Path.home() / ".local/bin") + ":/opt/homebrew/bin:/usr/bin:/bin",
        UV_NO_SYNC="true",
        UV_OFFLINE="true",
        JUST_NO_DOTENV="true",
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONUNBUFFERED="1",
        PYSTOW_HOME=str(Path.home() / ".data"),
        KG_MICROBE_DIR=str(table.parents[2]),
    )
    if claw is not None:
        env["CLAW_SRC"] = str(claw / "src")
    output.mkdir(parents=True)
    data = {
        "started_at": now(),
        "revision": revision,
        "python": sys.version,
        "python_executable": sys.executable,
        "command": command,
        "plan": plan,
        "inputs": {str(location): digest(raw) for location, raw in captured.items()},
        "history_scaffolder_revision": (
            config.get("history_scaffolder_revision") if gate == "new-history" else None
        ),
    }
    (output / "start.json").write_text(json.dumps(data, indent=2) + "\n")
    with (output / "native.log").open("xb") as stream:
        result = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT)
    (output / "native.exit").write_text(str(result.returncode) + "\n")
    if head() != revision or any(
        location.read_bytes() != raw for location, raw in captured.items()
    ):
        raise ValueError("captured execution inputs changed during native command")
    if gate == "new-history" and head(claw) != config["history_scaffolder_revision"]:
        raise ValueError("native history checkout changed")
    after_sidecars = {
        str(location.relative_to(ROOT)): digest(location.read_bytes())
        for location in sorted((ROOT / history).glob("*.yaml"))
    }
    new_sidecars = {
        name: value for name, value in after_sidecars.items() if name not in before_sidecars
    }
    if gate == "new-history" and not plan and result.returncode == 0 and len(new_sidecars) != 1:
        raise ValueError("successful native scaffold must persist one new sidecar")
    if not (output / "native.log").stat().st_size:
        raise ValueError("native gate produced no persisted log")
    data.update(
        finished_at=now(),
        exit_code=result.returncode,
        log_sha256=digest((output / "native.log").read_bytes()),
        log_bytes=(output / "native.log").stat().st_size,
        new_history_sidecars=new_sidecars,
        execution_inputs_unchanged=True,
    )
    (output / "receipt.json").write_text(json.dumps(data, indent=2) + "\n")
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gate", choices=RECIPES)
    parser.add_argument("--config", required=True)
    parser.add_argument("--config-sha256", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--claw-root", type=Path)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    result = run(
        args.config,
        args.config_sha256,
        args.gate,
        args.output,
        args.expected_revision,
        plan=args.plan,
        claw=args.claw_root,
    )
    print(json.dumps(result, indent=2))
    raise SystemExit(result["exit_code"])
