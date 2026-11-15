"""Stage/apply the reviewed BR1 genome correction for #2849, 2026-11-15.

Inputs: exact record, frozen NCBI/GTDB/paper snapshots and reviewed source report.
Outputs: exclusive private candidate, native validation, diff and actual receipt.
Only the GTDB block, one description identifier and one inline event may change.
No fetch, source-cache update or whole-record scientific approval.
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

STATE = ROOT / ".temp/br1-source-review-20261115"
TARGET = "data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml"
BEFORE = "c0326c5cdaf678c922659c33dbe4fe1b5717be2bf79dab54d672f160574c0fe5"
REPORT = "reports/br1-source-review-20261115/grounding-evidence-003.json"
REPORT_SHA = "fb9c72121151ab7e4a8c04baad430692dae203a82cec9bfd26c79eb88c3359a5"
OLD_ID = "GTDB:s__Microbacterium_lacus"
NEW_ID = "GTDB:s__Microbacterium_sp002812725"
SUMMARY = (
    "Correct only BR1's GTDB block and the corresponding identifier in the opening "
    "description using the exact NCBITaxon:1070896 / BR1 / SAMN07351343 assembly pair "
    "GCF_002812725.1 and GCA_002812725.1. Official GTDB taxon history explicitly assigns "
    "this genome to Microbacterium sp002812725 in R220; the retained current card agrees. "
    "Record this as an independently curated genome mapping because the retained "
    "NCBI2GTDB crosswalk has no exact BR1 row. Remove unmeasured crosswalk majority/count "
    "fields and unsupported latest/build wording. Preserve the original NCBI stock, "
    "phenotype claims, source quotations, graph, discussions and prior history. "
    "This scoped correction under #2849 is not a new full-record scientific review."
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def current_head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def verify_inputs(inputs):
    for relative, expected in inputs.items():
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT) or sha(path.read_bytes()) != expected:
            raise ValueError("reviewed input changed: " + relative)


def source_block():
    raw = (ROOT / REPORT).read_bytes()
    if sha(raw) != REPORT_SHA:
        raise ValueError("reviewed source report changed")
    report = json.loads(raw)
    if report["record"] != TARGET or report["record_sha256"] != BEFORE:
        raise ValueError("source report target differs")
    inputs = {REPORT: REPORT_SHA}
    for relative, digest in report["source_sha256"].items():
        inputs[str((STATE / relative).relative_to(ROOT))] = digest
    inspector = "scripts/adhoc/inspect_br1_grounding_evidence_20261115.py"
    inputs[inspector] = report["helper_sha256"]
    verify_inputs(inputs)
    block = {
        "gtdb_id": NEW_ID,
        "gtdb_taxon": "Microbacterium sp002812725",
        "gtdb_lineage": report["r220_lineage"],
        "ncbi_source_id": "NCBITaxon:1070896",
        "is_reclassified": True,
        "mapping_source": (
            "GTDB R220 explicit genome taxon history for GCF_002812725.1 "
            "(https://gtdb-api.ecogenomic.org/genome/GCF_002812725.1/taxon-history; "
            "retrieved 2026-11-15; sha256:"
            + report["source_sha256"]["gtdb-history-001/source.json"]
            + "); exact stock identity from NCBI Datasets assembly "
            "https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/"
            "GCF_002812725.1/dataset_report (sha256:"
            + report["source_sha256"]["assembly-001/source.json"]
            + ")."
        ),
        "curated": True,
        "curation_note": (
            "Exact BR1 genome mapping: NCBITaxon:1070896, strain BR1 and BioSample "
            "SAMN07351343 link GCF_002812725.1 to paired GCA_002812725.1. GTDB's "
            "explicit R220 history assigns this assembly to Microbacterium sp002812725; "
            "the retained current genome card agrees. The retained NCBI2GTDB table "
            "sha256:761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd "
            "has no exact BR1 NCBI ID or species-name row. Its CJ77 row, the GTDB "
            "species-cluster size and this single assembly are different populations; "
            "no crosswalk majority fraction or genome count is asserted for BR1. "
            "The primary study distinguishes the separately cited Microbacterium lacus "
            "soil isolate from BR1; no equivalence with that isolate is inferred. "
            "The GTDB placeholder is a genome classification, not a formal species "
            "renaming or an independent ANI calculation. See issue #2849."
        ),
    }
    return block, inputs


def assert_scope(before, after):
    if before["id"] != "CommunityMech:000531" or after["id"] != before["id"]:
        raise ValueError("wrong canonical target")
    if before["taxonomy"][0]["taxon_term"]["term"] != {
        "id": "NCBITaxon:1070896",
        "label": "Microbacterium sp. BR1",
    }:
        raise ValueError("exact BR1 stock required")
    block, _ = source_block()
    if after["taxonomy"][0]["taxon_term"]["gtdb_classification"] != block:
        raise ValueError("exact reviewed genome block required")
    if before["description"].count(OLD_ID) != 1 or after["description"] != before[
        "description"
    ].replace(OLD_ID, NEW_ID, 1):
        raise ValueError("only the exact description identifier may change")
    old_history = before.get("curation_history", [])
    new_history = after.get("curation_history", [])
    if len(new_history) != len(old_history) + 1 or new_history[:-1] != old_history:
        raise ValueError("append-only history required")
    event = new_history[-1]
    if set(event) != {"timestamp", "curator", "action", "changes", "llm_assisted"} or any(
        event[key] != value
        for key, value in {
            "curator": "codex",
            "action": "EDIT",
            "changes": SUMMARY,
            "llm_assisted": True,
        }.items()
    ):
        raise ValueError("exact attributable native history event required")
    old, new = copy.deepcopy(before), copy.deepcopy(after)
    for document in (old, new):
        document.pop("curation_history")
        document.pop("description")
        document["taxonomy"][0]["taxon_term"].pop("gtdb_classification")
    if old != new:
        raise ValueError("unrelated canonical semantics changed")


def stage(original):
    block, inputs = source_block()
    before = yaml.safe_load(original)
    after = copy.deepcopy(before)
    after["taxonomy"][0]["taxon_term"]["gtdb_classification"] = block
    after["description"] = after["description"].replace(OLD_ID, NEW_ID, 1)
    text = original.decode()
    pattern = r"(?m)^    gtdb_classification:\n(?:^      .*\n|^        .*\n)+"
    matches = list(re.finditer(pattern, text))
    if len(matches) != 1 or OLD_ID not in matches[0][0]:
        raise ValueError("one exact mapping text anchor required")
    replacement = yaml.safe_dump({"gtdb_classification": block}, sort_keys=False, width=120)
    replacement = "".join("    " + line + "\n" for line in replacement.splitlines())
    match = matches[0]
    text = text[: match.start()] + replacement + text[match.end() :]
    if text.count(OLD_ID) != 1:
        raise ValueError("one remaining description identifier required")
    text = text.replace(OLD_ID, NEW_ID, 1)
    if yaml.safe_load(text) != after:
        raise ValueError("bounded text differs from intended semantics")
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
    without_flag = {key: value for key, value in event.items() if key != "llm_assisted"}
    anchor = yaml.safe_dump([without_flag], sort_keys=False, allow_unicode=True, width=120).rstrip()
    if text.count(anchor) != 1:
        raise ValueError("native inline event anchor differs")
    text = text.replace(
        anchor, yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=120).rstrip(), 1
    )
    if yaml.safe_load(text) != after:
        raise ValueError("native event persistence differs")
    for name in (
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/validation/write_validated.py",
        "src/communitymech/curate/curation_event.py",
        "references_cache/PMID_42598292.txt",
        "reports/causal_graph_review/decisions/20261108-stage2-five-records-batch144.yaml",
        str(Path(__file__).relative_to(ROOT)),
    ):
        inputs[name] = sha((ROOT / name).read_bytes())
    assert_scope(before, after)
    return text, after, inputs


def execute(output, candidate_path=None, expected_sha=None, receipt_sha=None, *, expected_revision):
    output = Path(output).resolve()
    if not output.is_relative_to(STATE) or output.exists():
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
            raise ValueError("explicit reviewed candidate and receipt hashes required")
        raw_proof = candidate_path.with_name("receipt.json").read_bytes()
        text = candidate_path.read_text()
        proof = json.loads(raw_proof)
        if (
            sha(raw_proof) != receipt_sha
            or sha(text.encode()) != expected_sha
            or proof["after_sha256"] != expected_sha
            or proof["before_sha256"] != BEFORE
            or proof["target"] != TARGET
            or proof["applied"] is not False
        ):
            raise ValueError("reviewed staging receipt/candidate mismatch")
        inputs = proof["inputs"]
        verify_inputs(inputs)
        after = yaml.safe_load(text)
        assert_scope(yaml.safe_load(original), after)
    else:
        if expected_sha or receipt_sha:
            raise ValueError("hash requires an apply candidate")
        text, after, inputs = stage(original)
    output.mkdir(parents=True)
    write_validated_community(after, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native writer semantics differ")
    verify_inputs(inputs)
    if canonical.read_bytes() != original or current_head() != expected_revision:
        raise ValueError("canonical/revision changed during validation")
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
            raise ValueError("reviewed inputs changed before replacement")
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
        "scope": "Exact BR1 genome GTDB block and one description identifier plus native inline history; scientific_review:false.",
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
