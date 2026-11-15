"""Retain one native Wetland471 identity gate; #2898, 2026-11-15.

Inputs: fixed accepted application, source pins, exact revision and native Claw.
Outputs: exclusive raw command/log/exit/receipt and requested native sidecar.
Reuses captured-input utilities; no crosswalk, acquisition or shared-helper edits.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SHARED = "scripts/adhoc/check_gtdb_batch_unit_20261115.py"
SPEC = importlib.util.spec_from_file_location("identity_checks", ROOT / SHARED)
assert SPEC and SPEC.loader
checks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checks)
TARGET = "kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml"
SCOPE = "wetland471-source-identity-only"
SECTIONS = "description,taxonomy,discussions,curation_history"


def run(config_name, config_sha, gate, output_name, revision, *, plan=False, claw=None):
    output = checks.safe_path(output_name, private=True)
    if output.exists() or checks.head() != revision:
        raise ValueError("exclusive private output and exact revision required")
    captured = {}
    config = json.loads(checks.capture(captured, checks.safe_path(config_name), config_sha))
    if config["target"] != TARGET or config["scope"] != SCOPE:
        raise ValueError("fixed identity target and scope required")
    target = checks.safe_path(TARGET)
    before, after = config["before_sha256"], config["after_sha256"]
    checks.capture(captured, target, after)
    applied_path = checks.safe_path(config["application_receipt"], private=True)
    applied = json.loads(
        checks.capture(captured, applied_path, config["application_receipt_sha256"])
    )
    if (
        applied["applied"] is not True
        or applied["execution_revision"] != revision
        or applied["target"] != TARGET
        or applied["target_id"] != "CommunityMech:000471"
        or applied["scope"] != SCOPE
        or applied["scientific_review"] is not False
        or applied["before_sha256"] != before
        or applied["after_sha256"] != after
    ):
        raise ValueError("actual accepted identity application required")
    checks.capture(captured, applied_path.with_name("before.yaml"), before)
    for name, expected in applied["inputs"].items():
        checks.capture(captured, checks.safe_path(name), after if name == TARGET else expected)
    for name in (
        SHARED,
        str(Path(__file__).relative_to(ROOT)),
        "uv.lock",
        "justfile",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/history.yaml",
    ):
        checks.capture(captured, ROOT / name)
    if checks.digest(captured[target]) != after:
        raise ValueError("captured target differs from accepted AFTER")
    history = "history/records/" + Path(TARGET).stem
    old_sidecars = {
        str(p.relative_to(ROOT)): checks.digest(checks.capture(captured, p))
        for p in sorted((ROOT / history).glob("*.yaml"))
    }
    command = ["just", "--verbose", "--no-dotenv", "--color", "never"]
    if plan:
        command.append("--dry-run")
    command.append(checks.RECIPES[gate])
    if gate == "new-history":
        if claw is None or checks.head(claw) != config["history_scaffolder_revision"]:
            raise ValueError("exact native history checkout required")
        for location in sorted((claw / "src/kg_microbe_history").glob("*.py")):
            checks.capture(captured, location)
        checks.capture(captured, claw / "src/kg_microbe_governance/artifacts/schema/history.yaml")
        command.extend(
            [
                "--kind",
                "record",
                "--slug",
                Path(TARGET).stem,
                "--target-root",
                "kb/communities",
                "--event",
                "EDIT",
                "--outcome",
                "changed",
                "--sections",
                SECTIONS,
                "--actor-name",
                "codex",
                "--model",
                "gpt-6",
                "--agent-tool",
                "codex",
                "--issue",
                "https://github.com/CultureBotAI/CommunityMech/issues/2898",
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
        command.append(history if gate == "history" else TARGET)
    if gate == "strict":
        command.extend(["--out", str((output / "strict.tsv").relative_to(ROOT))])

    def unchanged():
        if checks.head() != revision or any(p.read_bytes() != raw for p, raw in captured.items()):
            raise ValueError("captured execution inputs or revision changed")

    unchanged()
    env = dict(os.environ)
    env.update(
        PATH=str(Path.home() / ".local/bin") + ":/opt/homebrew/bin:/usr/bin:/bin",
        UV_NO_SYNC="true",
        UV_OFFLINE="true",
        JUST_NO_DOTENV="true",
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONUNBUFFERED="1",
        PYSTOW_HOME=str(Path.home() / ".data"),
    )
    if claw is not None:
        env["CLAW_SRC"] = str(claw / "src")
    output.mkdir(parents=True)
    data = {
        "started_at": checks.now(),
        "revision": revision,
        "python": sys.version,
        "python_executable": sys.executable,
        "command": command,
        "plan": plan,
        "inputs": {str(p): checks.digest(raw) for p, raw in captured.items()},
        "history_scaffolder_revision": (
            config.get("history_scaffolder_revision") if gate == "new-history" else None
        ),
    }
    (output / "start.json").write_text(json.dumps(data, indent=2) + "\n")
    with (output / "native.log").open("xb") as stream:
        result = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT)
    (output / "native.exit").write_text(str(result.returncode) + "\n")
    unchanged()
    if gate == "new-history" and checks.head(claw) != config["history_scaffolder_revision"]:
        raise ValueError("native history checkout changed")
    sidecar_bytes = {
        str(p.relative_to(ROOT)): p.read_bytes() for p in sorted((ROOT / history).glob("*.yaml"))
    }
    sidecars = {name: checks.digest(raw) for name, raw in sidecar_bytes.items()}
    added = {name: value for name, value in sidecars.items() if name not in old_sidecars}
    if gate == "new-history" and not plan and result.returncode == 0:
        if len(added) != 1:
            raise ValueError("successful scaffold must persist one native sidecar")
        yaml_document = yaml.safe_load(sidecar_bytes[next(iter(added))])
        event = yaml_document["events"]
        if (
            yaml_document["target"]["path"] != TARGET
            or len(event) != 1
            or event[0]["type"] != "EDIT"
            or event[0]["outcome"] != "changed"
            or event[0]["sections"] != SECTIONS.split(",")
            or config["application_receipt"] not in event[0]["details"]
            or config["application_receipt_sha256"] not in event[0]["details"]
        ):
            raise ValueError("native sidecar target, sections or actual receipt link differs")
    elif added:
        raise ValueError("non-scaffold or dry run unexpectedly created a sidecar")
    log = (output / "native.log").read_bytes()
    if not log:
        raise ValueError("native output must persist")
    unchanged()
    if any((ROOT / name).read_bytes() != raw for name, raw in sidecar_bytes.items()):
        raise ValueError("native sidecar changed before receipt publication")
    data.update(
        finished_at=checks.now(),
        exit_code=result.returncode,
        log_sha256=checks.digest(log),
        log_bytes=len(log),
        new_history_sidecars=added,
        execution_inputs_unchanged=True,
    )
    (output / "receipt.json").write_text(json.dumps(data, indent=2) + "\n")
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gate", choices=checks.RECIPES)
    parser.add_argument("--config", required=True)
    parser.add_argument("--config-sha256", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--claw", type=Path)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    result = run(
        args.config,
        args.config_sha256,
        args.gate,
        args.output,
        args.expected_revision,
        plan=args.plan,
        claw=args.claw,
    )
    print(json.dumps(result, indent=2))
    raise SystemExit(result["exit_code"])
