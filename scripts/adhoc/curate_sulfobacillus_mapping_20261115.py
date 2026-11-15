"""Stage/apply one source-grounded GTDB correction, #2849, 2026-11-15.

Inputs: exact000035, independently inspected761crosswalk route and source cache.
Output: exclusive private candidate/receipt; opt-in exact-hash apply changes only
taxonomy[6].taxon_term.gtdb_classification plus one native inline history event.
No ontology, cache, source acquisition or broader scientific approval.
"""

import argparse
import copy
import difflib
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from communitymech.curate.curation_event import (  # noqa: E402
    append_curation_event_text,
    record_curation_event,
)
from communitymech.validation.write_validated import write_validated_community  # noqa: E402

STATE = ROOT / ".temp/gtdb-source-routes-2849-20261115"
TARGET = "kb/communities/Industrial_Bioreactor_Consortium.yaml"
BEFORE = "71160959bae2c8e3f0caf63d57452a597e29967f70faea6bec59016752b9aad4"
ROUTE = STATE / "sulfobacillus-route-001.json"
SUMMARY = (
    "Reconcile only the Sulfobacillus acidophilus GTDB mapping against the retained "
    "NCBI2GTDB snapshot sha256:761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd: "
    "two exact species-name rows, NCBI679936 and 1051632, each report two genomes with "
    "majority fraction 1.0 and the same Sulfobacillus_A acidophilus lineage. "
    "Use the native species-name result, total_genomes 4 and name-difference true; "
    "remove unsupported latest/build wording. Preserve NCBITaxon:53633 and the source "
    "species name. This database correspondence does not identify the study's exact "
    "strain or validate its composite community, functional claims or graph; #1509 remains open."
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(raw):
    return yaml.safe_load(raw)


def current_head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def verify_inputs(inputs):
    for relative, expected in inputs.items():
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT) or sha(path.read_bytes()) != expected:
            raise ValueError("reviewed input changed: " + relative)


def assert_scope(before, after):
    if before["id"] != "CommunityMech:000035" or after["id"] != before["id"]:
        raise ValueError("wrong canonical target")
    before_term = before["taxonomy"][6]["taxon_term"]
    after_term = after["taxonomy"][6]["taxon_term"]
    if before_term["term"] != {"id": "NCBITaxon:53633", "label": "Sulfobacillus acidophilus"}:
        raise ValueError("exact source species required")
    if after.get("curation_history", [])[:-1] != before["curation_history"]:
        raise ValueError("append-only history required")
    old = copy.deepcopy(before)
    new = copy.deepcopy(after)
    for document in (old, new):
        document.pop("curation_history")
        document["taxonomy"][6]["taxon_term"].pop("gtdb_classification")
    if old != new or after_term["gtdb_classification"].get("curated"):
        raise ValueError("only the source-supported native mapping may change")


def stage(original):
    route_bytes = ROUTE.read_bytes()
    route = json.loads(route_bytes)
    if route["record"] != TARGET or route["inputs"][TARGET] != BEFORE:
        raise ValueError("route does not bind exact baseline")
    verify_inputs(route["inputs"])
    measured = route["native_lookup"]
    rows = measured["exact_species_name_rows"]["sulfobacillus acidophilus"]
    if measured["exact_id_rows"] or len(rows) != 2:
        raise ValueError("reviewed source route changed")
    if {r["taxonID NCBI"] for r in rows} != {"679936", "1051632"} or any(
        r["species (GTDB)"] != "Sulfobacillus_A acidophilus"
        or r["total genomes"] != "2"
        or r["majority fraction"] != "1.0"
        for r in rows
    ):
        raise ValueError("reviewed primary table rows changed")
    result = measured["result"]
    expected = {
        "gtdb_id": "GTDB:s__Sulfobacillus_A_acidophilus",
        "gtdb_taxon": "Sulfobacillus_A acidophilus",
        "gtdb_lineage": "d__Bacteria;p__Bacillota_E;c__Sulfobacillia;o__Sulfobacillales;f__Sulfobacillaceae;g__Sulfobacillus_A;s__Sulfobacillus_A acidophilus",
        "ncbi_source_id": "NCBITaxon:53633",
        "majority_fraction": 1.0,
        "total_genomes": 4,
        "is_reclassified": True,
        "via": "ncbi_name",
    }
    if result != expected:
        raise ValueError("reviewed native mapping changed")
    before = load(original)
    after = copy.deepcopy(before)
    block = {k: v for k, v in expected.items() if k != "via"}
    block["mapping_source"] = (
        "kg-microbe NCBI2GTDB.tsv.gz sha256:761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd "
        "[native exact NCBI species-name mapping; no row for NCBITaxon:53633; rows 679936/1051632 each have 2 genomes, "
        "both Sulfobacillus_A acidophilus; reference-taxon correspondence, not study-strain genome identification]"
    )
    after["taxonomy"][6]["taxon_term"]["gtdb_classification"] = block
    text = original.decode()
    pattern = r"(?m)^    gtdb_classification:\n(?:^      .*\n|^        .*\n)+"
    matches = [m for m in re.finditer(pattern, text) if "GTDB:s__Sulfobacillus_acidophilus" in m[0]]
    if len(matches) != 1:
        raise ValueError("one exact text-preserving mapping anchor required")
    replacement = yaml.safe_dump({"gtdb_classification": block}, sort_keys=False, width=120)
    replacement = "".join("    " + line + "\n" for line in replacement.splitlines())
    match = matches[0]
    text = text[: match.start()] + replacement + text[match.end() :]
    if load(text) != after:
        raise ValueError("bounded mapping text changed other semantics")
    event = record_curation_event(
        after, curator="codex", action="EDIT", changes=SUMMARY, llm_assisted=True
    )
    text = append_curation_event_text(
        text,
        curator="codex",
        action="EDIT",
        changes=SUMMARY,
        timestamp=event["timestamp"],
        width=120,
    )
    without_flag = {k: v for k, v in event.items() if k != "llm_assisted"}
    anchor = yaml.safe_dump([without_flag], sort_keys=False, allow_unicode=True, width=120).rstrip()
    if text.count(anchor) != 1:
        raise ValueError("native event anchor changed")
    text = text.replace(
        anchor, yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=120).rstrip(), 1
    )
    if load(text) != after:
        raise ValueError("native event persistence differs")
    inputs = {k: v for k, v in route["inputs"].items() if k != TARGET}
    inputs[str(ROUTE.relative_to(ROOT))] = sha(route_bytes)
    for name in (
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/validation/write_validated.py",
        "src/communitymech/curate/curation_event.py",
        "references_cache/PMID_24242252.md",
        "reports/causal_graph_review/adversarial-review-20261006-batch53.yaml",
        str(Path(__file__).relative_to(ROOT)),
    ):
        inputs[name] = sha((ROOT / name).read_bytes())
    assert_scope(before, after)
    return text, after, inputs


def execute(output, candidate_path=None, expected_sha=None, receipt_sha=None, *, expected_revision):
    output = Path(output).resolve()
    if not output.is_relative_to(STATE) or output.exists() or output.is_symlink():
        raise ValueError("new exclusive private output required")
    if not re.fullmatch(r"[0-9a-f]{40}", expected_revision) or current_head() != expected_revision:
        raise ValueError("exact execution revision required")
    canonical = ROOT / TARGET
    original = canonical.read_bytes()
    if sha(original) != BEFORE:
        raise ValueError("exact unmodified canonical baseline required")
    if candidate_path:
        candidate_path = Path(candidate_path).resolve()
        if not candidate_path.is_relative_to(STATE) or not expected_sha or not receipt_sha:
            raise ValueError("explicit reviewed private candidate/hash required")
        text = candidate_path.read_text()
        raw_proof = candidate_path.with_name("receipt.json").read_bytes()
        if sha(raw_proof) != receipt_sha:
            raise ValueError("reviewed staging receipt changed")
        proof = json.loads(raw_proof)
        if (
            sha(text.encode()) != expected_sha
            or proof["after_sha256"] != expected_sha
            or proof["before_sha256"] != BEFORE
            or proof["target"] != TARGET
            or proof["applied"] is not False
        ):
            raise ValueError("staging receipt/candidate mismatch")
        inputs = proof["inputs"]
        verify_inputs(inputs)
        after = load(text)
        assert_scope(load(original), after)
    else:
        if expected_sha or receipt_sha:
            raise ValueError("candidate hash requires an apply candidate")
        text, after, inputs = stage(original)
    output.mkdir(parents=True)
    write_validated_community(after, output / "validated.yaml")
    if load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native written form differs")
    verify_inputs(inputs)
    if canonical.read_bytes() != original or current_head() != expected_revision:
        raise ValueError("canonical changed during native validation")
    (output / "candidate.yaml").write_text(text)
    (output / "before.yaml").write_bytes(original)
    (output / "candidate.diff").write_text(
        "".join(
            difflib.unified_diff(
                original.decode().splitlines(keepends=True),
                text.splitlines(keepends=True),
                fromfile=TARGET,
                tofile="staged/" + Path(TARGET).name,
            )
        )
    )
    if candidate_path:
        verify_inputs(inputs)
        if (
            canonical.read_bytes() != original
            or current_head() != expected_revision
            or candidate_path.read_bytes() != text.encode()
            or candidate_path.with_name("receipt.json").read_bytes() != raw_proof
        ):
            raise ValueError("canonical changed before replacement")
        replacement = output / "replacement.yaml"
        replacement.write_text(text)
        replacement.replace(canonical)
        if canonical.read_bytes() != text.encode():
            raise ValueError("canonical persistence differs")
    receipt = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "target": TARGET,
        "before_sha256": BEFORE,
        "after_sha256": sha(text.encode()),
        "inputs": inputs,
        "applied": bool(candidate_path),
        "execution_revision": expected_revision,
        "reviewed_staging_receipt_sha256": receipt_sha,
        "scope": "Only Sulfobacillus reference mapping; exact study strain, composite community and broader scientific claims remain unresolved under #1509.",
    }
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-candidate", type=Path)
    parser.add_argument("--expected-candidate-sha256")
    parser.add_argument("--expected-receipt-sha256")
    parser.add_argument("--expected-revision", required=True)
    args = parser.parse_args()
    execute(
        args.output,
        args.apply_candidate,
        args.expected_candidate_sha256,
        args.expected_receipt_sha256,
        expected_revision=args.expected_revision,
    )


if __name__ == "__main__":
    main()
