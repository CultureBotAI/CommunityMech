"""The actual just boundary must preserve quoted adapter/staging arguments."""

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.mark.skipif(shutil.which("just") is None, reason="actual recipe boundary requires just")
@pytest.mark.parametrize(
    "recipe,script,option",
    [
        ("text-map-inputs", "text_map_inputs.py", "--output"),
        ("stage-text-map", "stage_text_map.py", "--root"),
    ],
)
def test_recipes_preserve_quoted_paths(tmp_path, monkeypatch, recipe, script, option):
    capture = tmp_path / "arguments.json"
    executable = tmp_path / "uv"
    executable.write_text(
        "#!/usr/bin/env python3\nimport json,os,sys\nfrom pathlib import Path\n"
        'Path(os.environ["TEXT_MAP_ARGV_CAPTURE"]).write_text(json.dumps(sys.argv[1:]))\n'
    )
    executable.chmod(0o755)
    monkeypatch.setenv("PATH", str(tmp_path) + os.pathsep + os.environ["PATH"])
    monkeypatch.setenv("TEXT_MAP_ARGV_CAPTURE", str(capture))
    value = str(tmp_path / "path with spaces" / "inputs.jsonl")
    root = Path(__file__).resolve().parents[1]
    subprocess.run(["just", recipe, option, value], cwd=root, check=True, capture_output=True)
    assert json.loads(capture.read_text()) == ["run", "python", "scripts/" + script, option, value]
