"""Export verified 000088 lineage/QC metadata for #1548/#2816, 2026-11-15.

Inputs: actual apply receipt, saved native full review, persistence audit and
completed focused logs. Outputs: immutable sanitized public derivatives and a
checkpoint. Raw primary bodies stay private; no M5 replication is claimed.
"""

import argparse
import json
from collections import Counter
from pathlib import Path

import yaml
from check_phase2_brachypodium_20261115 import GATES, ROOT, STATE, TARGET
from export_m5_technical_evidence_20261114 import digest, immutable, sanitize

OUT = ROOT / "reports/phase2-completion-20261115/brachypodium-000088"


def public_bytes(raw):
    counts = Counter()
    return sanitize(raw.decode(), counts).encode(), {
        key: value for key, value in counts.items() if value
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply-receipt", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    receipt_raw = args.apply_receipt.read_bytes()
    applied = json.loads(receipt_raw)
    record_raw = (ROOT / TARGET).read_bytes()
    if (
        applied["applied"] is not True
        or applied["target"] != TARGET
        or applied["after_sha256"] != digest(record_raw)
    ):
        raise ValueError("lineage requires actual applied current-record receipt")
    for name, expected in applied["inputs"].items():
        if digest((ROOT / name).read_bytes()) != expected:
            raise ValueError("actual correction input changed: " + name)
    review_raw = args.review.read_bytes()
    review = yaml.safe_load(review_raw)
    audit = json.loads(args.audit.read_bytes())
    if (
        review["completion"] != "completed"
        or not review["scientific_review"]
        or audit["review_sha256"] != digest(review_raw)
        or audit["markdown_sha256"] != digest(args.review.with_suffix(".md").read_bytes())
        or not audit["all_inputs_match"]
        or not audit["markdown_matches_native_render"]
    ):
        raise ValueError("saved full scientific assessment/persistence proof missing")
    if review["scope"]["coverage"] != "full" or review["scope"]["reviewed_target_ids"] != [
        "CommunityMech:000088"
    ]:
        raise ValueError("review scope does not cover current whole target")
    for item in review["source"]["inputs"]:
        if digest((ROOT / item["path"]).read_bytes()) != item["sha256"]:
            raise ValueError("saved immutable input no longer matches: " + item["path"])
    reviewed_inputs = {item["path"]: item["sha256"] for item in review["source"]["inputs"]}
    raw_apply_path = str(args.apply_receipt.resolve().relative_to(ROOT))
    if reviewed_inputs.get(raw_apply_path) != digest(receipt_raw):
        raise ValueError("actual apply receipt is not bound to the saved scientific review")
    if reviewed_inputs.get(TARGET) != digest(record_raw):
        raise ValueError("saved review does not bind the current canonical record")
    publications = []
    for gate in (*GATES, "references", "network"):
        name = f"brachypodium-{gate}-{args.run}"
        raw = (STATE / (name + ".json")).read_bytes()
        result = json.loads(raw)
        log = (ROOT / result["log"]).read_bytes()
        exit_raw = (STATE / (name + ".exit")).read_bytes()
        if (
            result["name"] != name
            or result["status"] != "PASSED"
            or result["exit_code"] != 0
            or exit_raw.strip() != b"0"
            or not result["finished_at"]
            or result["record_worktree_sha256"] != digest(record_raw)
            or digest(log) != result["log_sha256"]
            or len(log) != result["log_bytes"]
        ):
            raise ValueError("native gate differs from completed current-record evidence")
        log_public, redactions = public_bytes(log)
        receipt_public, receipt_redactions = public_bytes(raw)
        document = json.loads(receipt_public)
        document["log"] = str((OUT / (name + ".log.txt")).relative_to(ROOT))
        document["public_evidence"] = {
            "raw_receipt_sha256": digest(raw),
            "raw_log_sha256": digest(log),
            "raw_exit_sha256": digest(exit_raw),
            "public_log_sha256": digest(log_public),
            "public_log_bytes": len(log_public),
            "redactions": {"log": redactions, "receipt": receipt_redactions},
            "location": "Retained in this local isolated checkout under repository .temp; replication elsewhere is not asserted.",
            "scope": "Native single-record diagnostic, not full QC or scientific approval.",
        }
        publications.extend(
            [
                (OUT / (name + ".log.txt"), log_public),
                (OUT / (name + ".exit.txt"), exit_raw),
                (OUT / (name + ".receipt.json"), (json.dumps(document, indent=2) + "\n").encode()),
            ]
        )
    public_apply, redactions = public_bytes(receipt_raw)
    if redactions or public_apply != receipt_raw:
        raise ValueError(
            "raw lineage receipt needs privacy review before byte-identical publication"
        )
    publications.append((OUT / "actual-curation.raw-receipt.json", receipt_raw))
    document = json.loads(public_apply)
    document["public_evidence"] = {
        "raw_sha256": digest(receipt_raw),
        "raw_path": str(args.apply_receipt.resolve().relative_to(ROOT)),
        "redactions": redactions,
        "scope": "Actual applied transition; staged candidate receipts are not counted as curation.",
    }
    publications.append(
        (OUT / "actual-curation.receipt.json", (json.dumps(document, indent=2) + "\n").encode())
    )
    public_audit, _ = public_bytes(args.audit.read_bytes())
    publications.append((OUT / "saved-review-audit.json", public_audit))
    identities = json.loads((STATE / "study-accessions-003.json").read_bytes())
    rows = [
        "| Paper stock | Verified sequence taxon | BioSample | Current assembly |",
        "|---|---|---|---|",
    ]
    for row in identities["roster"]:
        rows.append(
            f"| {row['paper_name']} | {row['taxon_id']} | [{row['biosample']}](https://www.ncbi.nlm.nih.gov/biosample/{row['biosample']}) | [{row['assembly']}]({row['assembly_url']}) |"
        )
    review_relative = str(args.review.resolve().relative_to(ROOT))
    md = f"""# Brachypodium SynCom15 scientific checkpoint

Record [CommunityMech:000088](../../../{TARGET}) now names the fifteen administered stocks and preserves distinct isolation, inoculum, liquid-culture and host-assay contexts. Actual curation changed SHA-256 `{applied['before_sha256']}` to `{applied['after_sha256']}`; the [applied receipt](actual-curation.receipt.json) retains the raw receipt hash and source bindings. The [byte-identical metadata-only raw receipt](actual-curation.raw-receipt.json) is bound directly in the scientific review input inventory. No staged receipt is counted as application.

The native full scientific assessment is saved as [YAML](../../../{review_relative}) and [Markdown](../../../{review_relative.removesuffix('.yaml')}.md). Its verdict is **needs_curation**, with biological classification/original-analysis-version uncertainty and the native SupportingReference coverage limitation at the reviewed base retained. This does not close the multi-record [issue1548](https://github.com/CultureBotAI/CommunityMech/issues/1548) or claim Phase2/full-corpus scientific completion.

Nine fresh local focused native gates passed: schema, strict cross-field rules, GTDB coherence, NCBI/GTDB domain, scalar hygiene, ontology terms, reference snippets, sidecar history and single-record network. Raw logs and private sources remain in this isolated local checkout; M5 replication is not asserted here. Full integrated QC, generated docs and current shared-schema coverage are root integration gates.

The [paper](https://doi.org/10.3389/fmicb.2025.1649750), all six original figures, separate TablesS1/S3 and supplemental captions were inspected. [BioProjectPRJNA1127609](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1127609) and fifteen BioSamples independently establish the following study-stock links through sample-name genus, strain, host and project. The current project also contains PantoeaRCC30.1/SAMN57447891, which is absent from the paper roster and excluded.

{chr(10).join(rows)}

These are current project-linked assemblies, not a claim that those exact versions were analyzed in2025; Leifsonia's linked assembly is newer. RCC150 has sequence-record identity `NCBITaxon:3239231` (bacteriumRCC_150) while its biological genus/species remain unresolved. Source SILVA Micrococcaceae and GTDB-tk MA-N2 classifications are attributed separately. All fifteen exact sequence taxa remain unresolved in the unchanged native named-species GTDB mapping; genus aggregates were not substituted. Figure2 closest-reference genomes were not copied to study stocks.

All host arms use `NOT_REPORTED` membership because the observed root profiles include other bacteria; the known fifteen-stock inoculum is described explicitly. Buffer-only controls are not asserted microbe-free. Equal input cell counts are distinct from16S read fractions and plant preparation counts. Genome-predicted osmoprotectants are not promoted to demonstrated host mediation. Five qualified biological nodes and zero causal arrows remain.

Original history and the October causal decision are preserved. The staged plant-Bosea homonym failure was caught by the existing [domain guard365](https://github.com/CultureBotAI/CommunityMech/issues/365), and the corrected source ancestry was rechecked. The apply helper rechecks source hashes after native validation; a source-change fault control preserves canonical bytes, with a separate positive application control. Retained failed attempts are diagnostic provenance, not passes.

[Saved-review audit](saved-review-audit.json) confirms every input hash and exact native Markdown rendering. Source article/supplement bodies and database captures are private; this checkpoint publishes metadata and sanitized native logs only. No issue closure, merge or scientific release authorization is implied.
"""
    publications.append((OUT / "README.md", md.encode()))
    OUT.mkdir(parents=True, exist_ok=True)
    for path, raw in publications:
        if path.exists() and path.read_bytes() != raw:
            raise ValueError("different public evidence exists: " + path.name)
    for path, raw in publications:
        immutable(path, raw)
        if path.read_bytes() != raw or not raw:
            raise ValueError("public artifact did not persist")
    print(
        json.dumps(
            {
                "review_id": review["review_id"],
                "public_artifacts": len(publications),
                "canonical_sha256": digest(record_raw),
                "actual_raw_apply_receipt_sha256": digest(receipt_raw),
            }
        )
    )


if __name__ == "__main__":
    main()
