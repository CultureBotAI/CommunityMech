"""Verify the complete #1994 repair against its preserved historical inputs."""

import argparse
import importlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
migration = importlib.import_module("separate_legacy_supplements")

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path)
args = parser.parse_args()
receipt = Path(__file__).resolve().parent
manifest = json.loads((receipt / "manifest.json").read_text())
inspection = json.loads((receipt / "before-inputs.json").read_text())
base = inspection["source"]["git_revision"]
assert len(manifest["entries"]) == 11
assert {entry["article"] for entry in manifest["entries"]} == {
    target["path"] for target in inspection["targets"]
}


def historical(path):
    return subprocess.check_output(["git", "show", f"{base}:{path}"], cwd=ROOT)


for entry in manifest["entries"]:
    original = historical(entry["article"])
    assert migration.digest(original) == entry["article_before_sha256"]
    head, tail = migration.split_article(original)
    assert (ROOT / entry["article"]).read_bytes() == head
    assert migration.digest(head) == entry["article_after_sha256"]
    assert migration.digest(tail) == entry["appended_sha256"]
    assert migration.digest(head + b"\n") == entry["article_prefix_sha256"]
    assert entry["removed_separator_hex"] == "0a"
    saved = (ROOT / entry["supplement"]).read_bytes()
    assert migration.digest(saved) == entry["supplement_after_sha256"]
    if entry["supplement_before_sha256"] is None:
        assert saved == tail
    else:
        assert saved == historical(entry["supplement"])
        assert migration.digest(saved) == entry["supplement_before_sha256"]
        assert tail[entry["preserved_payload_offset"] :] in saved

records = [
    item["path"] for item in inspection["source"]["inputs"] if item["path"].startswith("kb/")
]
for path in records:
    assert (ROOT / path).read_bytes() == historical(path)
offenders = [
    str(path.relative_to(ROOT))
    for path in (ROOT / "references_cache").rglob("*")
    if path.is_file()
    and path.suffix in {".md", ".txt"}
    and not path.name.endswith(".supplement.md")
    and migration.MARKER in path.read_bytes()
]
assert not offenders, offenders
result = {
    "base": base,
    "verified_articles": len(manifest["entries"]),
    "unchanged_records": len(records),
    "mixed_article_caches": offenders,
    "separator_bytes_removed_per_article": 1,
    "existing_sidecars_unchanged": sum(
        e["supplement_before_sha256"] is not None for e in manifest["entries"]
    ),
    "extracted_sidecars": sum(e["supplement_before_sha256"] is None for e in manifest["entries"]),
}
content = json.dumps(result, indent=2) + "\n"
if args.output:
    args.output.write_text(content)
print(content, end="")
