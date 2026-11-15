"""Assemble the authored nine-record native diagnostic configuration, 2026-11-15.

Inputs: pinned accepted source judgments and explicit native-check config pins,
actual M5 application/history receipts. Output: one exclusive builder config
for #2848/PR2884. No canonical writes, check execution or scientific approval.
The unchanged shared builder independently verifies the complete actual proof.
"""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRIVATE = ".temp/gtdb-species-third-batch-20261115"
PUBLIC = "reports/gtdb-species-third-batch-20261115"
REVISION = "dd97489f4475c6cc6127d1fdd375b4a80f3220b1"
SOURCE_CONFIG = PUBLIC + "/ten-authored-source-context-001.json"
SOURCE_SHA = "964e4b51e40ead5807af2fb77349a5d5678871db257f27d53a657c5b1af44369"
IDS = ("339", "491", "414", "391", "358", "502", "503", "504", "550")
GATES = ("schema", "strict", "gtdb", "domain", "scalars", "new-history", "history", "terms")

REVIEW = {
    "slug": "nine-record-species-reference-diagnostic",
    "title": "Nine records: bounded species-reference correspondence with stock context preserved",
    "independence_basis": "The accepted authored source contexts and full native source binding were inspected before staging. Three independent readers divided the exact nine M5 candidates and receipts into disjoint groups; all groups accepted the bounded diffs before actual application. The completed549 canary proved the same native application, check, save and checkpoint path. This assessment reuses those inspected source judgments and binds the actual resulting technical evidence; it is not a new whole-record scientific review.",
    "summary": "Nine whole records receive nineteen selected species-reference GTDB blocks/statuses while retaining their source stocks and biological claims. The distinct space-habitat, two-step PCB, two wheat experiments, PAH consortia and A1 isolate contexts remain explicit. The unchanged builder must verify actual guarded persistence, eighteen native inline events, nine separate history sidecars and seventy-two required native commands before saving this partial diagnostic.",
    "scope_description": "Nineteen selected taxonomy descriptors in records339,491,414,391,358,502,503,504,550; source-stock/reference-population boundaries, actual native correspondence, bounded application and technical provenance. Other scientific claims are preserved but not newly certified.",
    "selection": "The remaining nine records of the accepted third ten-record source plan followed the fully verified549 canary. Its immutable review/checkpoint is separate. No other current records, held source corrections or all-record scientific campaign units are included.",
    "limitations": [
        "Partial technical/provenance assessment with scientific_review:false. Scoped native validation does not complete whole-record science, source-snippet matching, generated products, aggregate QC or the broader campaign.",
        "Source preparation ran locally at7ed0013e; actual M5 staging, application and checks ran at frozen dd97489f4475c6cc6127d1fdd375b4a80f3220b1 with Python3.13.2. Their retained revisions are not relabeled as a later integration revision.",
        "Primary coverage is the bounded retained text declared in the accepted source contexts. No fresh complete-paper, figure-pixel, supplement-sequence, assembly, genotype or pathway audit is claimed. The PCB491 primary read is abstract-only; unread main material is not declared devoid of additional experiments.",
        "339 preserves all seven stocks and assembly/deposit strings, including terrestrial type strains versus ISS/preflight isolates. Species-ID reference populations do not directly classify those assemblies. The unselected Bacillus subtilis block and unresolved Pseudomonas antarctica descriptor remain unchanged. Cultivability, biomass, equal adjusted-OD input and stress-specific interpretations remain qualified.",
        "491 retains the separate acidic copper-leaching and alkaline gold-mobilization stages. WCS361 is not assigned to Acidithiobacillus. Issue2876 remains a scientific attribution/interaction blocker: this correspondence neither resolves nor endorses the broader organism attribution or reciprocal MUTUALISM labels.",
        "414 preserves six distinct stocks/deposits, including PM16 and S32 with a shared species descriptor;391 preserves only its T19/PM16 pair and separate Fusarium challenge. No cross-study deposit is added, and reference populations do not identify experimental genomes, viable persistence or inoculum abundance. Source/version, experimental clock, panel and causal limitations in1945/1951 remain separate.",
        "The PAH records preserve A1/A3 Consortium3, B8-1/A1 Consortium1, B8-1/A3 Consortium2, all-three Consortium4 and the separate A1 isolate baseline. B8-1 remains absent from Consortium3. Unequal inoculum volumes, seven-day HPLC removal, planktonic/static-biofilm conditions, DCPIP screening, biomass and soil/liquid regimes are not conflated. Existing2317-2319 source/assay/marker findings remain unresolved by taxonomy correspondence.",
        "PV848451/PV848453/PV848454 are marker accessions, not assemblies. Bacillus_A and native is_reclassified:true express a GTDB label difference, not a formal nomenclatural act or a reidentified study stock. Rounded majority fractions are not exact numerators, identity probabilities or unanimity.",
        "The complete crosswalk hash binds bytes; an upstream release or chronology is unestablished. Local NCBI authority observations have retained file-stat provenance, not full database checksum or release certification. Unselected legacy mapping provenance and every prior event remain unchanged.",
        "Strict successor admission and generated products are subsequent evidence. Preserve339's existing stage5 chain and362 admission;414's107 remediation chain;391's shared122 caller including409;491's other batch135 records; PAH batch138 biology and negative controls; and batch147's549/552-555 admissions, unmodified551 and unknown-path refusal. Complete saved-input checkpoints precede caller edits.",
    ],
    "links": [
        "https://github.com/CultureBotAI/CommunityMech/issues/2848",
        "https://github.com/CultureBotAI/CommunityMech/issues/2876",
        "https://github.com/CultureBotAI/CommunityMech/issues/1945",
        "https://github.com/CultureBotAI/CommunityMech/issues/1951",
        "https://github.com/CultureBotAI/CommunityMech/issues/2317",
        "https://github.com/CultureBotAI/CommunityMech/issues/2318",
        "https://github.com/CultureBotAI/CommunityMech/issues/2319",
        "https://github.com/CultureBotAI/CommunityMech/pull/2884",
    ],
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def prepare(pins_name, pins_sha):
    captured = {}

    def read(name, expected=None):
        relative = Path(name)
        location = (ROOT / relative).resolve()
        if relative.is_absolute() or ".." in relative.parts or not location.is_relative_to(ROOT):
            raise ValueError("repository-relative input required")
        if location not in captured:
            captured[location] = location.read_bytes()
        raw = captured[location]
        if expected is not None and digest(raw) != expected:
            raise ValueError("pinned input differs: " + name)
        return json.loads(raw)

    source = read(SOURCE_CONFIG, SOURCE_SHA)
    pins = read(pins_name, pins_sha)
    if set(pins) != set(IDS):
        raise ValueError("exact nine-record check-pin set required")
    wanted = {f"CommunityMech:{int(short):06d}" for short in IDS}
    selected = [row for row in source["records"] if row["record_id"] in wanted]
    if len(selected) != len(wanted) or {row["record_id"] for row in selected} != wanted:
        raise ValueError("exactly one authored source row per selected record required")
    contexts = {row["record_id"]: row for row in selected}
    units = []
    for short in IDS:
        identity = f"CommunityMech:{int(short):06d}"
        prefix = identity.split(":")[1]
        source_row = contexts[identity]
        check = read(f"{PUBLIC}/{short}-check-config-001.json", pins[short])
        application = read(check["application_receipt"], check["application_receipt_sha256"])
        if (
            application["applied"] is not True
            or application["execution_revision"] != REVISION
            or application["target_id"] != identity
            or application["target"] != check["target"]
            or application["before_sha256"] != check["before_sha256"]
            or application["after_sha256"] != check["after_sha256"]
            or source_row["record"] != check["target"]
            or source_row["before_sha256"] != check["before_sha256"]
        ):
            raise ValueError("authored context and actual application differ")
        gates = {gate: f"{PRIVATE}/{short}-run-{gate}-001" for gate in GATES}
        history = read(gates["new-history"] + "/receipt.json")
        if (
            history["plan"] is not False
            or history["exit_code"] != 0
            or len(history["new_history_sidecars"]) != 1
        ):
            raise ValueError("one actual persisted native sidecar required")
        sidecar, sidecar_sha = next(iter(history["new_history_sidecars"].items()))
        metadata = f"{PUBLIC}/remaining-nine-{short}-source-evidence-001.json"
        occurrences = source_row["occurrences"]
        indices = [item["taxonomy_index"] for item in occurrences]
        if len(indices) != len(set(indices)):
            raise ValueError("unique selected occurrences required")
        source_judgment = " ".join(
            f"Taxonomy[{item['taxonomy_index']}]: {item['source_assessment']}"
            for item in occurrences
        )
        population_judgment = " ".join(
            f"Taxonomy[{item['taxonomy_index']}]: {item['population_scope']} {item['name_scope']}"
            for item in occurrences
        )
        evidence = [
            {
                "evidence_id": prefix + "-paper-" + str(index),
                "kind": "primary_source",
                "reference": primary["path"],
                "locator": primary["locator"],
                "support": "supports",
                "summary": source_judgment + " Coverage: " + primary["coverage"],
            }
            for index, primary in enumerate(source_row["primary_sources"])
        ]
        paper_ids = [item["evidence_id"] for item in evidence]
        evidence.extend(
            [
                {
                    "evidence_id": prefix + "-database",
                    "kind": "database",
                    "reference": metadata,
                    "locator": "Selected occurrences, exact native results, NCBI authority rows, source contexts and captured crosswalk/input hashes",
                    "support": "supports",
                    "summary": population_judgment,
                },
                {
                    "evidence_id": prefix + "-application",
                    "kind": "record_content",
                    "reference": check["application_receipt"],
                    "locator": "Actual execution revision, before/after hashes, reviewed stage receipt and captured inputs",
                    "support": "supports",
                    "summary": "The actual M5 guarded application persisted the independently accepted mapping/status candidate and two native inline events, preserving all other science and prior history.",
                },
            ]
        )
        assessments = []
        for suffix, area, topic, refs, summary in (
            (
                "source",
                "grounding",
                "Preserved source stocks and experimental context",
                paper_ids + [prefix + "-terms"],
                source_judgment,
            ),
            (
                "population",
                "grounding",
                "Species-reference correspondence without experimental genome assignment",
                [prefix + key for key in ("-database", "-gtdb", "-domain")],
                population_judgment,
            ),
            (
                "provenance",
                "provenance",
                "Actual bounded persistence with prior science retained",
                [
                    prefix + key
                    for key in (
                        "-application",
                        "-schema",
                        "-strict",
                        "-scalars",
                        "-new-history",
                        "-history",
                    )
                ],
                check["history_details"],
            ),
        ):
            assessments.append(
                {
                    "assessment_id": prefix + "-" + suffix,
                    "area": area,
                    "topic": topic,
                    "outcome": "supported",
                    "target_ids": [identity],
                    "evidence_ids": refs,
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
                "selector": "; ".join(
                    f"taxonomy[{index}].taxon_term.gtdb_classification; taxonomy[{index}].taxon_term.gtdb_grounding_status"
                    for index in indices
                ),
                "label": "Bounded species-reference diagnostic for " + identity,
                "stage_directory": f"{PRIVATE}/{short}-m5-candidate-001",
                "history_sidecar": sidecar,
                "history_sidecar_sha256": sidecar_sha,
                "source_metadata_output": metadata,
                "gates": gates,
                "evidence": evidence,
                "assessments": assessments,
            }
        )
    output = ROOT / PUBLIC / "remaining-nine-review-config-001.json"
    if output.exists() or any(location.read_bytes() != raw for location, raw in captured.items()):
        raise ValueError("exclusive output and unchanged captured inputs required")
    raw = (json.dumps({"review": REVIEW, "records": units}, indent=2) + "\n").encode()
    with output.open("xb") as stream:
        stream.write(raw)
    print(
        json.dumps(
            {"path": str(output.relative_to(ROOT)), "sha256": digest(raw), "bytes": len(raw)}
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-pins", required=True)
    parser.add_argument("--check-pins-sha256", required=True)
    args = parser.parse_args()
    prepare(args.check_pins, args.check_pins_sha256)
