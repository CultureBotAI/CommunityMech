"""Verify the one-record boundary and unchanged native warning set."""

from collections import Counter
import json
from pathlib import Path
import subprocess

import yaml

ROOT = Path(__file__).resolve().parents[3]
BASE = "737a95eed17f606b30dd99fbec7dc82c19ad3f40"
RECORD = "kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml"
OUT = ROOT / "reports/causal_graph_review/20261015-metg2-host"
changed = subprocess.check_output(
    ["git", "diff", "--name-only", BASE], cwd=ROOT, text=True
).splitlines()
canonical = [p for p in changed if p.startswith(("kb/", "data/isolates/"))]
assert canonical == [RECORD], canonical
assert not any(p.startswith(("references_cache/", "src/", "conf/", "schema/")) for p in changed)
old = yaml.safe_load(subprocess.check_output(["git", "show", f"{BASE}:{RECORD}"], cwd=ROOT))
doc = yaml.safe_load((ROOT / RECORD).read_text())


def excerpts(value, path=""):
    if isinstance(value, dict):
        if "snippet" in value and "reference" in value:
            yield path, (value["reference"], value["snippet"])
        for key, child in value.items():
            yield from excerpts(child, f"{path}.{key}")
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from excerpts(child, f"{path}[{i}]")


assert dict(excerpts(doc)) == dict(excerpts(old))
before = json.loads((OUT / "baseline-audit.json").read_text())
after = json.loads((OUT / "network.json").read_text())
assert before["exit_code"] == after["exit_code"] == 1
assert json.loads(before["stdout"]) == json.loads(after["stdout"])
summary = json.loads((ROOT / "reports/causal_graph_review/summary.json").read_text())
assert summary["records"] == 462
assert summary["review_status_counts"] == {"needs_research": 54, "reviewed": 408}
assert not summary["structural_defects"]
severities = Counter(item["severity"] for item in summary["network_audit"])
assert not severities["error"]
print(
    json.dumps(
        dict(
            changed_canonical_paths=canonical,
            unchanged_excerpt_occurrences=len(dict(excerpts(doc))),
            old_cache_schema_and_config_unchanged=True,
            native_network_json_identical=True,
            native_network_exit_code=1,
            network_severity_counts=dict(severities),
            records=summary["records"],
            review_status_counts=summary["review_status_counts"],
            structural_defects=summary["structural_defects"],
        ),
        indent=2,
    )
)
