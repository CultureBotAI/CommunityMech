"""Assemble four authored partial diagnostics after the105 canary, 2026-11-15.

Inputs: pinned peer-reviewed source contexts, check configs and actual M5 receipts.
Output: exclusive review config for the unchanged native builder, #2848/PR2896.
No canonical edits or new scientific inference; full gate verification is separate.
"""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRIVATE = ".temp/gtdb-ambiguity-five-20261115"
PUBLIC = "reports/gtdb-ambiguity-five-20261115"
REVISION = "b195783da416b4be119edbb442d5b19dabe32ed4"
SOURCE_SHA = "505b806393fc307ddac81904d1452739bd3a13ee0fa70c1ec83ca90dfa226eff"
PROOF_SHA = "c9039d12a2c1b11de05642bfb079a86c0ce654af7e21e472c066868050065114"
CHECKS = {
    "425": "ff680f2b4e9a4c551bc680d7fc8d95f385fcba4892d85426343cc9da700d125b",
    "460": "39c3a25c9faeb3ab333764286a4fe195a612da63700796769b1770b486819ce3",
    "446": "de483ba5e0f905512817ceb4c82c0f7b15ba5afca09f16a9c1f6741171018b5d",
    "412": "a5b97a4163955f098df5b7c973f3fbed248883ff926e9e431944d171b718a68c",
}
REVIEW = {
    "slug": "four-record-complete-reference-alternatives-diagnostic",
    "title": "Probiotic, Panax, diatom and RAMC records: complete reference alternatives",
    "independence_basis": "Complete records, bounded primary passages and current historical callers received independent source reads. Separate peers read every actual M5 candidate diff and all30 stage inputs per record before application. The parent inspected actual persistence, all32 native logs and source/assay boundaries. This is a partial technical and provenance review.",
    "summary": "Four selected descriptors retain their complete unselected native ambiguity sets: four reuteri, eight Serratia, three Aliivibrio and two Rhodococcus alternatives. All source stocks, other taxonomy, biological claims and old history remain intact. Four actual guarded M5 applications, four native inline events, four separate history sidecars and32 required native checks are bound.",
    "scope_description": "The selected status/options fields in425/460/446/412, their source-stock and reference-population limits, actual persistence and eight native checks per record. No full scientific or stock-genome assessment.",
    "selection": "These four records followed the complete independently verified105 canary. The separate105 saved review/checkpoint is excluded from this population of four.",
    "limitations": [
        "Partial coverage with scientific_review:false. Native technical passes do not establish full-record scientific support, exact reference-snippet matching, current generated products or full corpus QC.",
        "Primary coverage is the bounded retained identity, Methods, Results and limitation passages declared in the accepted source contexts. No fresh supplement, figure pixels, raw omics, study-assembly bytes or complete-paper audit is claimed.",
        "425: preserve all three CICC stocks, the existing B.longum ambiguity and C.butyricum block. Live coculture, partner supernatants, mixed-species vesicles, luteolin cargo and animal doses are distinct. Cross-feeding is not traced transfer; MsrA necessity and dosing/timing findings1629/1630 remain.",
        "460: preserve XB-7/PX678127 as source stock/16S marker, XY-6 and its block, and BS versus alternative Hafnia treatments or Fusarium challenge. Monoculture filtrates mixed1:1 are not coculture metabolites. Disease comparators, rootMDA/POD/SOD, source discrepancy and relative fungal/network findings1674 remain separate.",
        "446: preserve MCCC1H00019, diatomCCAP1055/1 and its NO_GTDB_EQUIVALENT, conditions and notes. Keep all three native alternatives including the unexpected Vibrio harveyi label. RNA-seq does not place the bacterial stock genome. Attachment/competition, matched day8 physiology, missing axenic transcriptome, modeled flux and EPS findings1698/1701 remain unresolved.",
        "412: preserve wild-type PET/RPET/SR, ADP1/ATCC33305 and its existing block, versus engineered SR-P/SA-P in RAMC-P and PET polymer feedstock. Complementary aromatic/aliphatic use, chemical deconstruction, total-carbon units, inoculum ratios and engineered products are distinct. The open succinate discussion remains; issue1753 is not its owner.",
        "All ambiguity options remain unselected. No ambiguity-route genome denominator, experimental abundance, stock identity probability, strain equivalence or formal taxonomic rename is inferred.",
        "The crosswalk SHA identifies bytes, not an established upstream release; native mapping_source observes mtime. Local NCBI observations have file-stat provenance, not a full database checksum or certified ontology version.",
        "Actual M5 applications, gates and native builder/save use frozen b195783da416b4be119edbb442d5b19dabe32ed4 with Python3.13.2. Local source preparation and configuration assembly have their own revisions; later local commits are not substituted for actual execution metadata.",
        "Strict historical admission follows complete saved-input checkpoint verification. Preserve batch75 Mulberry435 and274/batch91; batch81 record359/c8s5; batch84 record053 and054/batch132; and batch93 record388 plus412's immutable unchanged-row/zero-event ledger. Current biology must remain current in every caller.",
    ],
    "links": [
        "https://github.com/CultureBotAI/CommunityMech/issues/2848",
        "https://github.com/CultureBotAI/CommunityMech/pull/2896",
    ],
}


def main():
    captured = {}

    def read(name, expected=None):
        path = ROOT / name
        raw = path.read_bytes()
        if expected is not None and hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError("pinned input differs: " + name)
        if path in captured and captured[path] != raw:
            raise ValueError("input changed between captures: " + name)
        captured[path] = raw
        return json.loads(raw)

    source = read(f"{PUBLIC}/five-authored-source-context-002.json", SOURCE_SHA)
    rows = {item["record_id"]: item for item in source["records"]}
    units = []
    for short, pin in CHECKS.items():
        identity = f"CommunityMech:{int(short):06d}"
        prefix = identity.split(":")[1]
        row = rows[identity]
        check = read(f"{PUBLIC}/{short}-check-config-001.json", pin)
        application = read(check["application_receipt"], check["application_receipt_sha256"])
        if (
            application["applied"] is not True
            or application["execution_revision"] != REVISION
            or application["target_id"] != identity
            or application["target"] != row["record"]
            or application["target"] != check["target"]
            or application["before_sha256"] != row["before_sha256"]
            or application["before_sha256"] != check["before_sha256"]
            or application["after_sha256"] != check["after_sha256"]
            or application["source_proof"]["sha256"] != PROOF_SHA
        ):
            raise ValueError("actual source/application differs: " + short)
        history = read(f"{PRIVATE}/{short}-new-history-001/receipt.json")
        if history["revision"] != REVISION or history["plan"] or history["exit_code"] != 0:
            raise ValueError("actual history execution required")
        if len(history["new_history_sidecars"]) != 1:
            raise ValueError("exactly one native sidecar required")
        sidecar, sidecar_sha = next(iter(history["new_history_sidecars"].items()))
        sidecar_bytes = (ROOT / sidecar).read_bytes()
        if hashlib.sha256(sidecar_bytes).hexdigest() != sidecar_sha:
            raise ValueError("persisted sidecar differs")
        captured[ROOT / sidecar] = sidecar_bytes
        occurrence = row["occurrences"][0]
        if len(row["occurrences"]) != 1 or len(row["primary_sources"]) != 1:
            raise ValueError("one selected occurrence and primary source required")
        primary = row["primary_sources"][0]
        metadata = f"{PUBLIC}/{short}-source-evidence-001.json"
        evidence = []
        for suffix, kind, reference, locator, summary in [
            (
                "paper",
                "primary_source",
                primary["path"],
                primary["locator"],
                occurrence["source_assessment"],
            ),
            (
                "database",
                "database",
                metadata,
                "Selected full native result, complete alternatives, NCBI identity rows and exact captured inputs",
                occurrence["population_scope"] + " " + occurrence["name_scope"],
            ),
            (
                "application",
                "record_content",
                check["application_receipt"],
                "Actual applied flag, revision, accepted stage pin and before/after hashes",
                check["history_details"],
            ),
            (
                "prior",
                "prior_review",
                next(iter(row["additional_inputs"])),
                "Accepted historical caller and source-boundary assessment",
                row["historical_guard_assessment"],
            ),
        ]:
            evidence.append(
                {
                    "evidence_id": prefix + "-" + suffix,
                    "kind": kind,
                    "reference": reference,
                    "locator": locator,
                    "support": "context_only" if suffix == "prior" else "supports",
                    "summary": summary,
                }
            )
        assessments = []
        for suffix, area, topic, refs, summary in [
            (
                "source",
                "grounding",
                "Source stock and assay boundaries",
                ["paper", "database", "prior"],
                occurrence["source_assessment"] + " " + occurrence["name_scope"],
            ),
            (
                "alternatives",
                "grounding",
                "Complete unselected reference alternatives",
                ["database", "gtdb", "domain", "terms"],
                occurrence["population_scope"]
                + " The actual candidate preserves all ordered native alternatives without changing other descriptors.",
            ),
            (
                "provenance",
                "provenance",
                "Actual persistence with prior science preserved",
                ["application", "schema", "strict", "scalars", "new-history", "history", "prior"],
                "The guarded application, one native sidecar and eight actual scoped checks bind the corrected bytes. Only one status/options set and one inline event changed semantically. Historical caller admission, complete corpus QC and full scientific assessment remain separate requirements.",
            ),
        ]:
            assessments.append(
                {
                    "assessment_id": prefix + "-" + suffix,
                    "area": area,
                    "topic": topic,
                    "outcome": "supported",
                    "target_ids": [identity],
                    "evidence_ids": [prefix + "-" + ref for ref in refs],
                    "summary": summary,
                }
            )
        units.append(
            {
                key: check[key]
                for key in (
                    "target",
                    "before_sha256",
                    "after_sha256",
                    "application_receipt",
                    "application_receipt_sha256",
                )
            }
            | {
                "target_id": identity,
                "selector": f"taxonomy[{occurrence['taxonomy_index']}].taxon_term.gtdb_candidates; taxonomy[{occurrence['taxonomy_index']}].taxon_term.gtdb_grounding_status",
                "label": "Complete unselected reference alternatives for " + identity,
                "stage_directory": f"{PRIVATE}/{short}-m5-candidate-001",
                "history_sidecar": sidecar,
                "history_sidecar_sha256": sidecar_sha,
                "source_metadata_output": metadata,
                "gates": {
                    gate: f"{PRIVATE}/{short}-{gate}-001"
                    for gate in (
                        "schema",
                        "strict",
                        "gtdb",
                        "domain",
                        "scalars",
                        "new-history",
                        "history",
                        "terms",
                    )
                },
                "evidence": evidence,
                "assessments": assessments,
            }
        )
    for path, raw in captured.items():
        if path.read_bytes() != raw:
            raise ValueError("captured input changed before output")
    output = ROOT / PUBLIC / "four-review-config-001.json"
    raw = (json.dumps({"review": REVIEW, "records": units}, indent=2) + "\n").encode()
    with output.open("xb") as handle:
        handle.write(raw)
    if output.read_bytes() != raw:
        raise ValueError("persisted configuration differs")
    print(
        json.dumps(
            {
                "path": str(output.relative_to(ROOT)),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
            }
        )
    )


if __name__ == "__main__":
    main()
