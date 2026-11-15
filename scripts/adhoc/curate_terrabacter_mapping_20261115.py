"""Stage/apply a verified Terrabacter reference-genus mapping, #2849, 2026-11-15.

Inputs: exact 000532, primary stock/NCBI identity and inspected 761 genus route.
Output: exclusive private candidate/receipt; opt-in exact-hash apply changes only
taxonomy[0].taxon_term.gtdb_classification plus one native inline history event.
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
TARGET = "data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml"
BEFORE = "81c8fd983bc57050595d7a4d51b64acdf2617ce9fea0f03f7ec9db4fa617c05e"
ROUTE = STATE / "terrabacter-grounding-001.json"
ROUTE_SHA = "c018c3a3c7cf0570b45cb3ad53480d30fd73a62104b13a43615c0adc5a0c1762"
SUMMARY = (
    "Correct only the manually curated Terrabacter reference-genus mapping. "
    "PMID:42598292 Methods names DSMZ 28514; primary DSMZ BacDive 157986 identifies this stock as 2APm3. "
    "NCBI Taxonomy 1472881 verifies genus ancestor 53355 Terrabacter, replacing the incorrect 37948 "
    "provenance. The retained crosswalk genus mapping yields Actinomycetales/Dermatophilaceae, "
    "support 12 / total 12 / fraction 1 from the native named-species-filtered reference population. "
    "Preserve outer stock NCBITaxon:1472881 and all biological/graph claims. No exact stock-genome "
    "or GTDB species identity is asserted; these counts do not describe 12 strains of 2APm3. "
    "Remove unsupported latest/build wording and document the manual ancestor route. Issue #2849."
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
    if before["id"] != "CommunityMech:000532" or after["id"] != before["id"]:
        raise ValueError("wrong canonical target")
    before_term = before["taxonomy"][0]["taxon_term"]
    after_term = after["taxonomy"][0]["taxon_term"]
    if before_term["term"] != {"id": "NCBITaxon:1472881", "label": "Terrabacter sp. 2APm3"}:
        raise ValueError("exact source stock required")
    if after.get("curation_history", [])[:-1] != before["curation_history"]:
        raise ValueError("append-only history required")
    old = copy.deepcopy(before)
    new = copy.deepcopy(after)
    for document in (old, new):
        document.pop("curation_history")
        document["taxonomy"][0]["taxon_term"].pop("gtdb_classification")
    block = after_term["gtdb_classification"]
    if (
        old != new
        or block.get("curated") is not True
        or block.get("ncbi_source_id") != "NCBITaxon:53355"
        or not block.get("curation_note")
    ):
        raise ValueError("only the documented manual genus correspondence may change")


def stage(original):
    route_bytes = ROUTE.read_bytes()
    if sha(route_bytes) != ROUTE_SHA:
        raise ValueError("independently inspected source proof changed")
    route = json.loads(route_bytes)
    if route["record"] != TARGET or route["inputs"][TARGET] != BEFORE:
        raise ValueError("route does not bind exact baseline")
    verify_inputs(route["inputs"])
    authority = route["ncbi_authority"]
    if (
        authority["id"] != "1472881"
        or {"id": "53355", "name": "Terrabacter", "rank": "genus"} not in authority["lineage"]
    ):
        raise ValueError("verified stock-to-genus ancestry required")
    if route["native_exact_stock_result"] is not None or route["exact_stock_rows"]:
        raise ValueError("source route has changed; reassess exact stock evidence")
    result = route["reference_genus_result"]
    expected = {
        "gtdb_id": "GTDB:g__Terrabacter",
        "gtdb_taxon": "Terrabacter",
        "gtdb_lineage": "d__Bacteria;p__Actinomycetota;c__Actinomycetes;o__Actinomycetales;f__Dermatophilaceae;g__Terrabacter",
        "ncbi_source_id": "NCBITaxon:53355",
        "majority_fraction": 1.0,
        "support_genomes": 12,
        "total_genomes": 12,
        "is_reclassified": False,
        "via": "ncbi_rank_g",
        "n_alt": 1,
    }
    if result != expected:
        raise ValueError("reviewed native mapping changed")
    before = load(original)
    after = copy.deepcopy(before)
    block = {k: v for k, v in expected.items() if k not in {"via", "n_alt"}}
    block["mapping_source"] = (
        "kg-microbe NCBI2GTDB.tsv.gz sha256:761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd "
        "[manual verified genus-ancestor route NCBITaxon:53355 Terrabacter; native named-species-filtered aggregate support 12 / total 12, "
        "fraction 1.0; reference-genus population, not 12 genomes or strains of 2APm3; no GTDB release inferred from file time]"
    )
    block["curated"] = True
    block["curation_note"] = (
        "Manual reference-genus correspondence for the preserved NCBITaxon:1472881 Terrabacter sp. 2APm3 stock. "
        "PMID:42598292 Methods identifies DSMZ 28514; DSMZ BacDive 157986 links DSM 28514 to 2APm3. "
        "NCBI Taxonomy 1472881 LineageEx verifies genus 53355 Terrabacter; the old 37948 ancestor assertion was incorrect. "
        "The native exact stock ID/name lookup returns no result on the retained crosswalk bytes. A separately inspected "
        "native genus 53355 query gives the stored genus lineage and 12/12 reference-genome counts after named-species filtering "
        "(18 raw genus rows were inspected). This does not establish an exact stock genome, GTDB species assignment, or "
        "12 strains of 2APm3. Preserve this evidenced manual ancestor mapping rather than relabel the stock or invent exact-genome support. Issue #2849."
    )
    after["taxonomy"][0]["taxon_term"]["gtdb_classification"] = block
    text = original.decode()
    pattern = r"(?m)^    gtdb_classification:\n(?:^      .*\n|^        .*\n)+"
    matches = [m for m in re.finditer(pattern, text) if "GTDB:g__Terrabacter" in m[0]]
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
        "references_cache/PMID_42598292.txt",
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
        "scope": "Only the verified Terrabacter reference-genus correspondence changes; exact stock-genome identity and broader biological/source claims are not certified by this correction.",
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
