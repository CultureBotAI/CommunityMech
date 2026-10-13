"""Generate the bounded #1994 source-byte and native-validator receipt."""

import argparse
import importlib
import json
import sys
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import yaml
from linkml_reference_validator.models import ReferenceContent, ReferenceValidationConfig
from linkml_reference_validator.plugins.reference_validation_plugin import ReferenceValidationPlugin

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--repo-root", type=Path, required=True, help="historical baseline worktree")
parser.add_argument("--output-dir", type=Path, required=True)
args = parser.parse_args()
root = args.repo_root.resolve()
sys.path.insert(0, str(root / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
record_review = importlib.import_module("record_review")
migration = importlib.import_module("separate_legacy_supplements")

out = args.output_dir.resolve()
out.mkdir(parents=True, exist_ok=True)
entries = []
source_parts = {}
targets = []
inputs = [
    "references_cache/README.md",
    "src/communitymech/schema/communitymech.yaml",
    "src/communitymech/schema/mech_shared.yaml",
    "conf/reference_validator.yaml",
    "uv.lock",
]
for path in sorted((root / "references_cache").iterdir()):
    if path.suffix not in {".txt", ".md"} or path.name.endswith(".supplement.md"):
        continue
    raw = path.read_bytes()
    if migration.MARKER not in raw:
        continue
    head, tail = migration.split_article(raw)
    sidecar = path.with_name(path.stem + ".supplement.md")
    saved = sidecar.read_bytes() if sidecar.exists() else None
    offset = 0
    disposition = "byte-identical sidecar retained"
    if saved is None:
        disposition = "extract appended bytes to missing sidecar"
    elif path.stem == "PMID_42482240":
        offset = tail.index(b"\n\n") + 2
        assert tail[offset:] == saved[saved.index(b"\n\n") + 2 :]
        disposition = "same source body; retain existing retrieval header"
    elif path.stem == "doi_10.64898_2026.03.16.712028":
        offset = tail.index(b"Table S2.")
        assert tail[offset:] in saved
        disposition = "Table S2 preserved in larger sidecar with Tables S1-S4"
    else:
        assert saved == tail
    reference = (
        path.stem.replace("PMID_", "PMID:", 1)
        if path.stem.startswith("PMID_")
        else "doi:10.64898/2026.03.16.712028"
    )
    entry = {
        "reference": reference,
        "article": path.relative_to(root).as_posix(),
        "supplement": sidecar.relative_to(root).as_posix(),
        "article_before_sha256": migration.digest(raw),
        "article_after_sha256": migration.digest(head),
        "appended_sha256": migration.digest(tail),
        "supplement_before_sha256": migration.digest(saved) if saved is not None else None,
        "supplement_after_sha256": migration.digest(saved if saved is not None else tail),
        "article_bytes_before": len(raw),
        "article_bytes_after": len(head),
        "appended_bytes": len(tail),
        "boundary_line": raw[: raw.index(migration.MARKER)].count(b"\n") + 1,
        "removed_separator_hex": "0a",
        "article_prefix_sha256": migration.digest(raw[: raw.index(migration.MARKER)]),
        "preserved_payload_offset": offset,
        "disposition": disposition,
    }
    entries.append(entry)
    source_parts[reference] = (raw, head, saved if saved is not None else tail)
    targets.append(
        {
            "target_id": reference,
            "path": entry["article"],
            "label": reference + " article/supplement boundary",
            "kind": "source",
            "owner_paths": [
                {
                    "repository": "CultureBotAI/CommunityMech",
                    "path": entry["article"],
                    "role": "article cache",
                },
                {
                    "repository": "CultureBotAI/CommunityMech",
                    "path": entry["supplement"],
                    "role": "separate supplementary source",
                },
            ],
        }
    )
    if saved is not None:
        inputs.append(entry["supplement"])
assert len(entries) == 11
manifest = {"issue": 1994, "entries": entries}
(out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


def walk(node, path=""):
    if isinstance(node, dict):
        if node.get("reference") in source_parts and isinstance(node.get("snippet"), str):
            yield path, node
        for key, value in node.items():
            yield from walk(value, f"{path}.{key}" if path else str(key))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk(value, f"{path}[{index}]")


items = []
for directory in ("kb/communities", "kb/taxa", "data/isolates"):
    for path in sorted((root / directory).rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text())
        selected = list(walk(doc))
        if selected:
            inputs.append(path.relative_to(root).as_posix())
            for field, item in selected:
                items.append((path.relative_to(root).as_posix(), doc["id"], field, item))

# Capture exact targets and context hashes before any evidence mutation.
inspection = record_review.inspect_source(root, targets, inputs)
(out / "before-inputs.json").write_text(json.dumps(inspection, indent=2) + "\n")
(out / "targets.json").write_text(json.dumps({"targets": targets}, indent=2) + "\n")


def locate(snippet, text):
    # Whitespace folding only: no bracket removal, ellipses, or fuzzy matching.
    normalized = " ".join(text.split()).casefold()
    needle = " ".join(snippet.split()).casefold()
    if needle not in normalized:
        return None
    import re

    pattern = r"\s+".join(re.escape(word) for word in snippet.split())
    found = re.search(pattern, text, re.IGNORECASE)
    if found is None:
        return None
    return {
        "line_start": text[: found.start()].count("\n") + 1,
        "line_end": text[: found.end()].count("\n") + 1,
    }


rows = []
with TemporaryDirectory(prefix="cm1994-native-") as temporary:
    before_cache = Path(temporary) / "before"
    after_cache = Path(temporary) / "after"
    before_cache.mkdir()
    after_cache.mkdir()
    before = ReferenceValidationPlugin(config=ReferenceValidationConfig(cache_dir=before_cache))
    after = ReferenceValidationPlugin(config=ReferenceValidationConfig(cache_dir=after_cache))
    for entry in entries:
        raw, head, supplement = source_parts[entry["reference"]]
        for plugin, data in ((before, raw), (after, head)):
            fetcher = plugin.validator.fetcher
            normalized = fetcher.normalize_reference_id(entry["reference"])
            name = fetcher.get_cache_path(normalized)
            if entry["article"].endswith(".txt"):
                name = name.with_suffix(".txt")
            name.write_bytes(data)
    with patch(
        "linkml_reference_validator.etl.reference_fetcher.ReferenceSourceRegistry.get_source",
        side_effect=AssertionError("network lookup forbidden in bounded cache audit"),
    ):
        for path, record_id, field, item in items:
            reference, snippet = item["reference"], item["snippet"]
            old = list(before._validate_excerpt(snippet, reference, None, field + ".snippet"))
            new = list(after._validate_excerpt(snippet, reference, None, field + ".snippet"))
            raw, head, supplement = source_parts[reference]
            supplement_result = after.validator.find_text_in_reference(
                snippet, ReferenceContent(reference_id=reference, content=supplement.decode())
            )
            rows.append(
                {
                    "record": path,
                    "record_id": record_id,
                    "field": field,
                    "reference": reference,
                    "snippet_sha256": migration.digest(snippet.encode()),
                    "article_location": locate(snippet, head.decode()),
                    "supplement_location": locate(snippet, supplement.decode()),
                    "native_article_before": [str(r.message) for r in old],
                    "native_article_after": [str(r.message) for r in new],
                    "native_supplement_match": supplement_result.found,
                }
            )
    for plugin in (before, after):
        assert list(
            plugin._validate_excerpt(
                "ZZQQ invented evidence XKCD", entries[0]["reference"], None, "canary"
            )
        )

counts = {
    "snippets": len(rows),
    "records": len({r["record"] for r in rows}),
    "native_failures_before": sum(bool(r["native_article_before"]) for r in rows),
    "native_failures_after": sum(bool(r["native_article_after"]) for r in rows),
    "new_native_failures": sum(
        not r["native_article_before"] and bool(r["native_article_after"]) for r in rows
    ),
    "article_verbatim": sum(r["article_location"] is not None for r in rows),
    "supplement_only_verbatim": sum(
        r["article_location"] is None and r["supplement_location"] is not None for r in rows
    ),
    "neither_verbatim": sum(
        r["article_location"] is None and r["supplement_location"] is None for r in rows
    ),
}
receipt = {
    "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "validator_version": version("linkml-reference-validator"),
    "counts": counts,
    "method": (
        "Offline native ReferenceValidationPlugin on isolated before/after article caches; "
        "exact original bytes and native normalized filenames. Supplement matching is a "
        "separate diagnostic, never a fallback or CLI pass. Locator uses case/whitespace "
        "folding only. All canonical YAML roots searched recursively, including ignored files."
    ),
    "rows": rows,
}
(out / "snippet-audit.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=True) + "\n")
print(json.dumps(counts, indent=2))
for row in rows:
    if row["article_location"] is None and row["supplement_location"] is None:
        print("UNMATCHED", json.dumps(row))
