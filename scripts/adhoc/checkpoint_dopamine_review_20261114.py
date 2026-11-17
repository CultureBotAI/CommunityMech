"""Verify and checkpoint the saved dopamine review, 2026-11-14.

Inputs: native review candidate/checkpoint and published YAML/Markdown.
Outputs: reports/m5-completion-20261114/dopamine-syncom-review.{json,md}.
Serves #2710/#2708/#2773/#2774; never modifies the immutable review or KB.
"""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
receipt = json.loads((STATE / "dopamine-syncom-review-checkpoint.json").read_text())
folder = ROOT / "reviews/structured" / receipt["review_id"]
files = []
for name in ("review.yaml", "review.md"):
    path = folder / name
    data = path.read_bytes()
    if not data:
        raise ValueError("empty saved artifact")
    files.append(
        {
            "path": str(path.relative_to(ROOT)),
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        }
    )
saved = yaml.safe_load((folder / "review.yaml").read_text())
if saved["review_id"] != receipt["review_id"] or saved["verdict"] != "needs_curation":
    raise ValueError("saved content mismatch")
target_hash = hashlib.sha256((ROOT / receipt["target"]).read_bytes()).hexdigest()
if target_hash != receipt["target_sha256"]:
    raise ValueError("canonical record changed before checkpoint")
receipt.update(
    status="saved_verified",
    completion=saved["completion"],
    verdict=saved["verdict"],
    artifacts=files,
    scientific_review=saved["scientific_review"],
)
output = ROOT / "reports/m5-completion-20261114/dopamine-syncom-review.json"
output.write_text(json.dumps(receipt, indent=2) + "\n")
lines = [
    "# Dopamine SynCom16 scientific review checkpoint",
    "",
    "The native immutable review is saved and both nonempty artifacts were verified. "
    "Verdict: needs_curation; assessment completed; canonical record unchanged.",
    "",
    f"Reviewed sixteen members, {receipt['nodes']} interaction nodes and "
    f"{receipt['downstream_edges']} downstream edges. Seven focused fresh M5 checks passed.",
    "",
    "| Artifact | Bytes | SHA256 |",
    "| --- | ---: | --- |",
]
lines.extend(
    f"| [{item['path']}](../../{item['path']}) | {item['bytes']} | {item['sha256']} |"
    for item in files
)
lines.extend(
    [
        "",
        "Open findings: retained #2710 and #2708; newly filed #2773 and #2774. "
        "The shared cache finding also affects 000515, which this review does not clear.",
        "",
        f"Native completeness {receipt['completeness']}/100; validation quality "
        f"{receipt['quality']}/100 (raw {receipt['quality_raw']}). These formulas and "
        "counts are in the native assessment and do not override scientific findings.",
        "",
        "Minimal supported curation: remove unsupported host-target assertion on node4; "
        "remove causal host/direction tags from correlation-only nodes0/1 and correct the "
        "guidance example; correct shared cache metadata while preserving source boundaries. "
        "Retain the two direct isolate-growth effects and all measured associations. "
        "Taxonomy provenance and species uncertainty require the separately recorded work. "
        "No canonical edits were made in this review.",
        "",
    ]
)
output.with_suffix(".md").write_text("\n".join(lines))
print(json.dumps(receipt, indent=2))
