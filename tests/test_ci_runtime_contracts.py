"""CI and research-runtime contracts must be explicit and reproducible (#667)."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
WORKFLOWS = REPO / ".github" / "workflows"
JUSTFILE = REPO / "justfile"

SETUP_UV_ACTION = "astral-sh/setup-uv@c771a70e6277c0a99b617c7a806ffedaca235ff9"
UV_VERSION = "0.12.5"


# A workflow vendored byte-identical from culturebotai-claw carries this banner
# on its first line. Its action pins and uv version are claw's decision, and
# check_vendored_sync.sh fails on any local edit, so a repository-local pin
# contract cannot bind it -- it can only report a drift nobody here may fix
# (culturebotai-claw#391; same shape as CultureMech#437).
GOVERNED_BANNER = "# Governed by culturebotai-claw"


def _workflow_documents() -> list[tuple[Path, dict]]:
    paths = sorted([*WORKFLOWS.glob("*.yaml"), *WORKFLOWS.glob("*.yml")])
    documents = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        if text.startswith(GOVERNED_BANNER):
            continue
        documents.append((path, yaml.safe_load(text)))
    return documents


def _steps(document: dict):
    for job in document.get("jobs", {}).values():
        yield from job.get("steps", [])


def test_every_setup_uv_step_pins_the_same_action_and_binary_version():
    found = []
    for path, document in _workflow_documents():
        for step in _steps(document):
            uses = str(step.get("uses", ""))
            if not uses.startswith("astral-sh/setup-uv@"):
                continue
            found.append(path.name)
            assert uses == SETUP_UV_ACTION, f"{path.name} uses an unpinned/different setup-uv"
            assert (
                step.get("with", {}).get("version") == UV_VERSION
            ), f"{path.name} does not pin uv {UV_VERSION}"

    assert found, "no workflow installs uv; this test checked nothing"


def test_every_workflow_sync_is_frozen():
    sync_commands = []
    for path, document in _workflow_documents():
        for step in _steps(document):
            for line in str(step.get("run", "")).splitlines():
                command = line.strip()
                if not command.startswith("uv sync"):
                    continue
                sync_commands.append((path.name, command))
                assert "--frozen" in command, f"{path.name} re-resolves dependencies: {command}"

    assert sync_commands, "no workflow runs uv sync; this test checked nothing"


def test_provider_profile_alone_triggers_its_test_workflow():
    workflow = (WORKFLOWS / "validate-strict.yaml").read_text(encoding="utf-8")
    assert '"conf/deep_research_provider.yaml"' in workflow


def test_ci_exercises_minimum_and_modern_supported_python():
    document = yaml.safe_load((WORKFLOWS / "validate-strict.yaml").read_text())

    def python_version(job: str) -> str | None:
        for step in document["jobs"][job]["steps"]:
            if str(step.get("uses", "")).startswith("actions/setup-python@"):
                return step.get("with", {}).get("python-version")
        return None

    assert python_version("validate-strict") == "3.10"
    assert python_version("python-compatibility") == "3.13"


def test_modern_python_lane_installs_just_for_repository_contract_tests():
    document = yaml.safe_load((WORKFLOWS / "validate-strict.yaml").read_text())
    uses = {str(step.get("uses", "")) for step in document["jobs"]["python-compatibility"]["steps"]}

    assert "extractions/setup-just@v3" in uses


def test_commands_that_invoke_research_dependencies_have_a_python_preflight():
    text = JUSTFILE.read_text(encoding="utf-8")
    guard = re.search(r"^_require-research-python:\n(?P<body>(?:[ \t]+.*\n)+)", text, re.MULTILINE)
    assert guard, "the research Python preflight recipe is missing"
    assert "sys.version_info < (3, 12)" in guard.group("body")

    guarded = {
        "research-community",
        "research-community-edison",
        "research-community-causal",
        "research-community-edison-batch",
        "enrich-edison-response",
        "research-providers",
        "research-provider",
    }
    for recipe in guarded:
        header = re.search(rf"^{re.escape(recipe)}(?: [^:]*)?:[^\n]*$", text, re.MULTILINE)
        assert header, f"missing recipe: {recipe}"
        assert (
            "_require-research-python" in header.group()
        ), f"{recipe} can reach a Python 3.12-only dependency without the preflight"
