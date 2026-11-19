"""Prepare one private Switchgrass locator canary for CommunityMech #1996.

Inputs: explicit CommunityMech root and retained Table S1 asset/retrieval record.
Outputs: exclusive .temp records, exact schema copies, catalog and input hashes.
Only local copies are written; no acquisition, canonical changes or validation.
Reuses validator prepare_switchgrass_source_canary_20261115.py at SHA256
1bcde6de0f2302de5a7d3c5ba1d333a15dc61144904270bd6e6f505d4ecb2963.
Consumer difference: existing reviewed schema bytes are never augmented.
Date: 2026-11-15.
"""

import argparse
import json
import subprocess
from copy import deepcopy
from hashlib import sha256
from pathlib import Path

from linkml_reference_validator.etl.source_locator import extract_docx_tables
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[2]
PINS = {
    "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml": "bb31b1df4a9be2241453528101fc5d55657c23eccf1d58ce1cc9639e5912b368",
    "src/communitymech/schema/communitymech.yaml": "a8db0b22ee6fb930fa9e603d881fd4b67cd1f1433e8fd716db13ca7db116febb",
    "src/communitymech/schema/mech_shared.yaml": "01d09b7d91a21235b97cc37d8482518a7b2c36ab63d8898796fede3877061ed9",
    "conf/reference_validator.yaml": "297b1fbd8a77ba2f89ca7126339deabc0f61ee91013d054d0fa64caef59a630d",
    "references_cache/PMID_36472419.txt": "af090796fe581c590b97b09d340412fef5bc735f0b4c94e8cef3f92a31f4c1a6",
    "references_cache/PMID_40920748.md": "e941bcf804a045b43ed4cede7eddc57cc7bf3fe078d5915d1d1d8a89660b217f",
    "references_cache/PMID_42660928.md": "4b0186047599fd515aebc524d5e008ffbdf72ade572fc308443b60af2298bcdf",
}
ASSET = "msystems.00951-22-s0006.docx"
ASSET_SHA = "5bfa02fdb94538e9405fb0ec7d7b0dad338791a5ca0b4b651589f33148c8e0e7"
DISCUSSION = "methods_final16_vs_supplement_table_s1"
CELLS = {2: (12, 2, "OAE516"), 3: (18, 1, "Bacillus"), 4: (18, 2, "OAE603")}


def digest(raw):
    """Hash the exact bytes also used for parsing and publication."""
    return sha256(raw).hexdigest()


def encoded(value):
    """Serialize deterministic private JSON artifacts."""
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def native_schema_artifacts(schema_raw, shared_raw):
    """Require existing consumer slots and return the exact captured bytes."""
    yaml = YAML(typ="safe")
    schema, shared = yaml.load(schema_raw), yaml.load(shared_raw)
    for document, classname in ((schema, "EvidenceItem"), (shared, "SupportingReference")):
        slot = document["classes"][classname]["attributes"].get("source_locator")
        if (
            not isinstance(slot, dict)
            or slot.get("range") != "SourceLocator"
            or slot.get("inlined") is not True
            or slot.get("required", False)
        ):
            raise ValueError("Consumer schema lacks the reviewed optional inlined locator")
    if "SourceLocator" not in shared["classes"]:
        raise ValueError("Consumer schema lacks its shared SourceLocator class")
    return {"schema/communitymech.yaml": schema_raw, "schema/mech_shared.yaml": shared_raw}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--community-root", type=Path, required=True)
    parser.add_argument("--asset", type=Path, required=True)
    parser.add_argument("--retrieval", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if args.community_root.resolve() != ROOT:
        raise ValueError("Use this isolated CommunityMech consumer checkout")
    output = args.output.resolve()
    if output.exists() or not output.is_relative_to(ROOT / ".temp"):
        raise ValueError("A new private output under this repository is required")
    paths = [args.community_root / name for name in PINS] + [
        args.asset,
        args.retrieval,
        Path(__file__),
    ]
    if any(p.is_symlink() or not p.is_file() for p in paths):
        raise ValueError("Every input must be an existing regular file")
    captured = {p.absolute(): p.read_bytes() for p in paths}
    before_head = subprocess.check_output(
        ["git", "-C", str(args.community_root), "rev-parse", "HEAD"], text=True
    ).strip()
    for name, expected in PINS.items():
        if digest(captured[(args.community_root / name).absolute()]) != expected:
            raise ValueError(f"Reviewed input differs: {name}")
    asset_raw = captured[args.asset.absolute()]
    if digest(asset_raw) != ASSET_SHA or args.asset.name != ASSET:
        raise ValueError("Wrong retained Table S1 asset")
    retrieval = json.loads(captured[args.retrieval.absolute()])
    if (
        retrieval["url"]
        != "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9765266/supplementaryFiles"
    ):
        raise ValueError("Wrong source acquisition identity")
    matches = [item for item in retrieval["retained_members"] if item["filename"] == ASSET]
    if (
        len(matches) != 1
        or matches[0]["sha256"] != ASSET_SHA
        or matches[0]["bytes"] != len(asset_raw)
    ):
        raise ValueError("Retained acquisition receipt does not bind the asset")
    projection = extract_docx_tables(asset_raw)
    if len(projection["tables"]) != 1 or len(projection["tables"][0]) != 19:
        raise ValueError("Unexpected Table S1 shape")
    yaml = YAML(typ="safe")
    original_raw = captured[(args.community_root / next(iter(PINS))).absolute()]
    original = yaml.load(original_raw)
    if original["id"] != "CommunityMech:000087":
        raise ValueError("Wrong record")
    record = deepcopy(original)
    indexes = [
        i for i, item in enumerate(record["discussions"]) if item["discussion_id"] == DISCUSSION
    ]
    if len(indexes) != 1:
        raise ValueError("Ambiguous discussion selector")
    discussion_index = indexes[0]
    selected_paths = []
    for index, (row, cell, quote) in CELLS.items():
        evidence = record["discussions"][discussion_index]["evidence"][index]
        if (
            evidence["reference"] != "PMID:36472419"
            or evidence["snippet"] != quote
            or evidence["evidence_source"] != "supplement_table_S1"
            or "source_locator" in evidence
            or projection["tables"][0][row - 1][cell - 1] != {"status": "supported", "text": quote}
        ):
            raise ValueError("Reviewed evidence/coordinate binding differs")
        evidence["source_locator"] = {
            "kind": "supplement",
            "asset_id": ASSET,
            "version": "published",
            "table": 1,
            "row": row,
            "cell": cell,
        }
        selected_paths.append(f"discussions[{discussion_index}].evidence[{index}].snippet")
    stripped = deepcopy(record)
    for index in CELLS:
        del stripped["discussions"][discussion_index]["evidence"][index]["source_locator"]
    if stripped != original:
        raise ValueError("Non-locator record content changed")
    schemas = native_schema_artifacts(
        captured[(args.community_root / "src/communitymech/schema/communitymech.yaml").absolute()],
        captured[(args.community_root / "src/communitymech/schema/mech_shared.yaml").absolute()],
    )
    projection_raw = encoded(projection)
    catalog = {
        "version": 1,
        "sources": [
            {
                "reference": "PMID:36472419",
                "asset_id": ASSET,
                "version": "published",
                "asset_path": f"assets/{ASSET}",
                "asset_sha256": ASSET_SHA,
                "extraction_path": "extractions/table-s1.json",
                "extraction_sha256": digest(projection_raw),
            }
        ],
    }
    config = yaml.load(captured[(args.community_root / "conf/reference_validator.yaml").absolute()])
    config.update(
        cache_dir=str(output / "references_cache"),
        source_catalog=str(output / "catalog.json"),
        fetch_full_text=False,
    )
    artifacts = {
        "original.yaml": original_raw,
        "selected.json": encoded(record),
        **schemas,
        "config.json": encoded(config),
        "catalog.json": encoded(catalog),
        f"assets/{ASSET}": asset_raw,
        "extractions/table-s1.json": projection_raw,
        "source-retrieval.json": captured[args.retrieval.absolute()],
    }
    for name in PINS:
        if name.startswith("references_cache/"):
            artifacts[name] = captured[(args.community_root / name).absolute()]
    receipt = {
        "scope": "Private consumer canary using exact native schema bytes; no canonical correction",
        "reuse_helper_sha256": "1bcde6de0f2302de5a7d3c5ba1d333a15dc61144904270bd6e6f505d4ecb2963",
        "schema_bytes_unchanged": True,
        "community_revision": before_head,
        "record_content_unchanged_except_three_locators": True,
        "selected_paths": selected_paths,
        "asset_sha256": ASSET_SHA,
        "inputs": {str(path): digest(raw) for path, raw in captured.items()},
        "outputs": {name: digest(raw) for name, raw in artifacts.items()},
        "plan": args.plan,
    }
    if before_head != subprocess.check_output(
        ["git", "-C", str(args.community_root), "rev-parse", "HEAD"], text=True
    ).strip() or any(path.read_bytes() != raw for path, raw in captured.items()):
        raise ValueError("Inputs or source revision changed during preparation")
    if not args.plan:
        output.mkdir(parents=True, exist_ok=False)
        for name, raw in artifacts.items():
            destination = output / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open("xb") as handle:
                handle.write(raw)
        with (output / "preparation.json").open("xb") as handle:
            handle.write(encoded(receipt))
        if any((output / name).read_bytes() != raw for name, raw in artifacts.items()):
            raise ValueError("Persisted scratch artifact differs")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
