"""Repair only native GTDB note placement after the 000087 canary,2026-11-15.

Input: exact first applied record and source receipt. Output: native validated
record plus exclusive before/after proof.13 genus caveats belong in ordinary
taxon notes, not curated-override metadata. No numerical map/source changes;
old history preserved and one native event appended. Serves #1548.
"""

import argparse
import copy
import json
from pathlib import Path

import yaml
from curate_phase2_lbnl_canary_20261115 import (
    ROOT,
    STATE,
    TARGET,
    append_curation_event_text,
    digest,
    load_document,
    record_curation_event,
    replace_section,
    write_validated_community,
)

BEFORE = "2fe1ed016c1662df531daee34c1f2115fe19086677a63904f68180de0547c7f7"
NOTE = "Aggregate genus correspondence, not a sequenced-study-stock placement. Minority mappings and species identity remain uncertain."
SUMMARY = "Moved13 unchanged genus-versus-study-stock caveats from GTDB curated-override metadata to ordinary taxon notes after native strict detected gtdb_note_without_curated. No mapping votes, stock identities, source assertions or prior history changed; no false curated:true override added. First failed strict receipt is retained."


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or not output.is_relative_to(ROOT / ".temp"):
        raise ValueError("new private output required")
    canonical = ROOT / TARGET
    original = canonical.read_bytes()
    first = json.loads((STATE / "curation-applied-001/receipt.json").read_bytes())
    if digest(original) != BEFORE or first["after_sha256"] != BEFORE or not first["applied"]:
        raise ValueError("source changed since failed native check")
    before = load_document(original)
    after = copy.deepcopy(before)
    count = 0
    for member in after["taxonomy"]:
        term = member["taxon_term"]
        mapping = term.get("gtdb_classification")
        if mapping:
            if mapping.pop("curation_note", None) != NOTE or "curated" in mapping:
                raise ValueError("unexpected mapping annotation")
            term["notes"] += " " + NOTE
            count += 1
    if count != 13:
        raise ValueError("expected exactly13 grounded genus caveats")
    text = replace_section(original.decode(), "taxonomy", after["taxonomy"])
    event = record_curation_event(
        after, curator="codex", action="EDIT", changes=SUMMARY, llm_assisted=True
    )
    text = append_curation_event_text(
        text,
        curator="codex",
        action="EDIT",
        changes=SUMMARY,
        timestamp=event["timestamp"],
        width=108,
    )
    unmarked = {key: value for key, value in event.items() if key != "llm_assisted"}
    anchor = yaml.safe_dump([unmarked], sort_keys=False, allow_unicode=True, width=108).rstrip()
    if text.count(anchor) != 1:
        raise ValueError("native event anchor changed")
    text = text.replace(
        anchor, yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=108).rstrip(), 1
    )
    if load_document(text) != after or after["curation_history"][:-1] != before["curation_history"]:
        raise ValueError("unexpected history or semantic change")
    output.mkdir()
    write_validated_community(after, output / "validated.yaml")
    if load_document((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native validation changed semantics")
    (output / "before.yaml").write_bytes(original)
    (output / "candidate.yaml").write_text(text)
    if args.apply:
        if canonical.read_bytes() != original:
            raise ValueError("concurrent source mutation")
        (output / "replacement.yaml").write_text(text)
        (output / "replacement.yaml").replace(canonical)
        if canonical.read_bytes() != text.encode():
            raise ValueError("persisted bytes differ")
    receipt = {
        "target": TARGET,
        "before_sha256": BEFORE,
        "after_sha256": digest(text.encode()),
        "applied": args.apply,
        "event": event,
        "count": count,
        "helper_sha256": digest(Path(__file__).read_bytes()),
        "predecessor_receipt": ".temp/phase2-science-20261115/curation-applied-001/receipt.json",
    }
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
