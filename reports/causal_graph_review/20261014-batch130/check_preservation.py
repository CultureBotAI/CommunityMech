"""Verify the complete canonical census and unchanged out-of-scope bytes."""

import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[3]
BASE = "b68d71e702200cd7ce9afdec001705dc8b0890fd"
TARGET = "kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml"
old = list(
    csv.DictReader(
        io.StringIO(
            subprocess.check_output(
                ["git", "show", BASE + ":reports/causal_graph_review/inventory.tsv"],
                cwd=ROOT,
                text=True,
            )
        ),
        delimiter="\t",
    )
)
current = list(
    csv.DictReader((ROOT / "reports/causal_graph_review/inventory.tsv").open(), delimiter="\t")
)
assert {r["path"] for r in old} == {r["path"] for r in current}
changed = [
    r["path"]
    for r in old
    if hashlib.sha256((ROOT / r["path"]).read_bytes()).hexdigest() != r["record_sha256"]
]
assert changed == [TARGET], changed
assert not subprocess.check_output(
    ["git", "diff", "--name-only", BASE, "--", "references_cache"], cwd=ROOT
)
caches = subprocess.check_output(
    ["git", "ls-tree", "-r", "--name-only", BASE, "references_cache"], cwd=ROOT, text=True
).splitlines()


def blocks(text):
    pairs = yaml.compose(text).value
    return {
        k.value: text[
            k.start_mark.index : (
                pairs[i + 1][0].start_mark.index if i + 1 < len(pairs) else len(text)
            )
        ]
        for i, (k, v) in enumerate(pairs)
    }


before = blocks(subprocess.check_output(["git", "show", BASE + ":" + TARGET], cwd=ROOT, text=True))
after = blocks((ROOT / TARGET).read_text())
allowed = {"description", "ecological_interactions", "discussions", "curation_history"}
assert all(after[k] == v for k, v in before.items() if k not in allowed)
print(
    json.dumps(
        {
            "canonical_records": len(old),
            "changed_records": changed,
            "unchanged_records": len(old) - len(changed),
            "unchanged_tracked_cache_files": len(caches),
            "unchanged_non_graph_root_blocks": True,
            "ignored_files_included_in_inventory": True,
        },
        indent=2,
    )
)
