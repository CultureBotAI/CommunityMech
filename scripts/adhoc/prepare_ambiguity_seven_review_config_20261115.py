"""Assemble authored seven-record diagnostic configuration, 2026-11-15.

Inputs: reviewed check configs, actual M5 stage/application/history receipts.
Output: exclusive native-builder config for #2848/PR2881, no canonical changes.
The unchanged builder separately verifies all actual gates, source pins and bytes.
"""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRIVATE = ".temp/gtdb-ambiguity-eight-20261115"
PUBLIC = "reports/gtdb-ambiguity-eight-20261115"
CHECK_PINS = {
    "400": "97c74e32807789b41975d421b990809a7933f5bd0d45966315434370bd15d8ff",
    "499": "c58caada6849df9cf3e00305265f3a99d27f066eefe9b880467873d6cd1ade1f",
    "500": "f95eef072b0993275cc036c39bb6db87d9806e39404ba03147ec80cab8c7e225",
    "506": "5f3ef1e0b216a970836ff17a2fb709a26dbcc9ccfed4bf48b9a7fb2592dc3ecd",
    "507": "1298951a16e81c98899888461b9c081a2b7050c6d285de007f9f8da86db8fdee",
    "508": "04489724877a34ebaf67f992bbad4c78c85b2554f89974061a7795359f29661f",
    "509": "d8df45052f10c64338f5f865a5581196e8a850508ce59d0f8537dd84f3e5773d",
}
SOURCE = {
    "400": (
        "PMID_42658845.txt",
        "Retained abstract and labeled supplementary Table S1, lines 50-60; original ENA/GBDP attribution remains source-reported.",
    ),
    "499": (
        "PMID_42354927.txt",
        "Retained Methods 2.2/Results 3.1 and Tables 2-3: T2 Bo1/Bo2 codes, MALDI-TOF best matches and six-isolate roster.",
    ),
    "500": (
        "PMID_42354927.txt",
        "Retained Methods 2.2/Results 3.1 and Tables 2-3: T3 Ht3 code, MALDI-TOF best match and six-isolate roster.",
    ),
    "506": (
        "PMID_41743136.txt",
        "Retained main-text line 64, partial-16S identification, Table 1 C2 roster and Table 2 separate bulk endpoints.",
    ),
    "507": (
        "PMID_41743136.txt",
        "Retained main-text line 64, partial-16S identification, Table 1 C3 roster and Table 2 separate bulk endpoints.",
    ),
    "508": (
        "PMID_41743136.txt",
        "Retained main-text line 64, partial-16S identification, Table 1 C4 roster and Table 2 separate bulk endpoints.",
    ),
    "509": (
        "PMID_41743136.txt",
        "Retained main-text line 64, partial-16S identification, Table 1 C5 roster and Table 2 separate bulk endpoints.",
    ),
}
SELECTORS = {
    "400": "taxonomy[3].taxon_term.gtdb_candidates",
    "499": "taxonomy[0:2].taxon_term.gtdb_candidates; taxonomy[0:2].taxon_term.gtdb_grounding_status",
    "500": "taxonomy[2].taxon_term.gtdb_candidates; taxonomy[2].taxon_term.gtdb_grounding_status",
    "506": "taxonomy[1].taxon_term.gtdb_classification; taxonomy[0,2].taxon_term.gtdb_candidates; taxonomy[0:3].taxon_term.gtdb_grounding_status",
    "507": "taxonomy[1].taxon_term.gtdb_classification; taxonomy[0,2].taxon_term.gtdb_candidates; taxonomy[0:3].taxon_term.gtdb_grounding_status",
    "508": "taxonomy[0,2].taxon_term.gtdb_classification; taxonomy[1].taxon_term.gtdb_candidates; taxonomy[0:3].taxon_term.gtdb_grounding_status",
    "509": "taxonomy[2,4].taxon_term.gtdb_classification; taxonomy[0,1,3].taxon_term.gtdb_candidates; taxonomy[0:5].taxon_term.gtdb_grounding_status",
}
PAPER_CLAIMS = {
    "400": "The retained Table S1 and its footnote identify PMSX member X as Stenotrophomonas maltophilia, associate it with ENA project PRJEB18431 and explain the earlier Xanthomonas retroflexus name through the study's GBDP analysis. This is source attribution, not a new assembly or species assignment.",
    "499": "The source distinguishes T2 isolate codes Bo1 and Bo2 from their MALDI-TOF library best matches ZCF25 and UCP1549. The source roster contains six T2 isolates. Library matches are not exact-stock genome identities, and T4 is a separate consortium.",
    "500": "The source describes T3 isolate Ht3 as Bacillus mojavensis with MALDI-TOF best match B1811. Ht3 remains distinct from that library stock and the other five T3 isolates; its source identification does not supply an assembly assignment.",
    "506": "The source identifies C2 as SRCHD03, SRCHD05 and SRCHD06, using partial-16S isolate characterization. The three-member formulation, isolate kinetics and C2 bulk endpoints remain separate from C6 irradiation and immobilization experiments.",
    "507": "The source identifies C3 as SRCHD04, SRCHD05 and SRCHD06. SRCHD04 is distinct from C2's SRCHD03. Partial-16S identities, isolate kinetics and C3 bulk endpoints are distinct observations.",
    "508": "The source identifies C4 as SRCHD05, SRCHD06 and SRCHD07. SRCHD05 and SRCHD07 retain separate stock codes despite sharing a reported species name; SRCHD06 is identified only to Ochrobactrum genus. Formulation and bulk endpoints do not establish interspecies flux.",
    "509": "The source identifies C5 as the five stocks SRCHD03-SRCHD07. The two Brevundimonas stocks and two Brucella stocks remain distinct, and SRCHD06 is genus-only. Partial-16S identification, individual-isolate kinetics, C5 bulk endpoints and separate C6 experiments are not interchangeable evidence.",
}
REVIEW = {
    "slug": "seven-record-reference-alternatives-diagnostic",
    "title": "Seven records: complete native alternatives and bounded reference correspondence",
    "independence_basis": "The parent inspected the complete affected records, retained source contexts and all seven actual M5 candidate diffs. A separate peer independently checked those exact diffs, candidate/receipt pins and frozen M5 source inputs before application. The new check-config adapter and its authored contexts also received a separate read-only review. This is a partial technical/provenance assessment of the resulting corrections.",
    "summary": "Seven records retain all original source stocks and biological claims while recording complete native ambiguity options and six species-reference blocks. Three status-only records and four mixed hexamine records preserve their different source and assay boundaries. Actual guarded applications, append-only native events and eight required commands per record must be verified by the unchanged diagnostic builder before this assessment can be saved.",
    "scope_description": "Eighteen selected descriptors in records400,499,500,506,507,508,509; complete native reference alternatives/correspondence, actual M5 persistence and scoped technical checks. No new whole-paper or stock-genome approval.",
    "selection": "The remaining seven records followed the fully verified505 application canary. C1's saved review/checkpoint is separate and is not counted in this batch. Other concurrent records and all-record scientific review are excluded.",
    "limitations": [
        "Partial diagnostic with scientific_review:false. Native technical success does not complete scientific review, generated products, aggregate QC, source-specific snippet validation or the broader campaign.",
        "The M5 execution revision remains ee9930cb145805101cc87b0a9ba188616cbf7ab8. The original local source binding ran at a5c0e6d; later commits and changed local historical callers are not substituted for captured M5 execution inputs.",
        "Primary coverage is the retained bounded source passages and rosters declared in the accepted source plans. No new figure-pixel, supplement-sequence, spectra, assembly or complete-paper audit is claimed.",
        "PMSX X retains the source's Stenotrophomonas identity and reported earlier Xanthomonas ENA name. All eleven alternatives remain; PRJEB18431/GBDP attribution is not a new GTDB assembly placement. Model-inferred exchange, substrate identity, partial recipients and CV-biomass limits remain. Recorded findings2486-2489 are not resolved. Its combined article/SI cache remains preserved historical evidence, not source-specific reference-validation approval.",
        "T2 Bo1/Bo2 remain distinct isolates. ZCF25, UCP1549 and T3 B1811 are MALDI-TOF library best matches, not demonstrated study-stock synonyms or genomes. Keep six-isolate T2/T3 rosters, unselected Pseudomonas/Bacillus mappings, separate optimization/simulated-water/pesticide assays and residue-loss versus mineralization limits. Predicted enzyme inventories are not measured pathway mediation.",
        "C2-C5 retain separate source rosters and partial-16S identification. SRCHD03 and04 remain different stocks despite a shared Brevundimonas descriptor; SRCHD05 and07 also remain separate. SRCHD06 stays genus-only. C6's six-stock irradiation/immobilization experiments are separate from these suspended formulations and isolate kinetics.",
        "The six 18-genome/fraction1.0 species blocks are repeated descriptor correspondences, not six populations sampled from study stocks. Brucella pseudintermedia retains its NCBI identity while the native GTDB label is Ochrobactrum pseudintermedium; this is not formal renaming. Complete ambiguity options do not supply a genome denominator or membership probabilities.",
        "The full crosswalk hash binds bytes but its upstream GTDB release is unverified. Local NCBI authority observations are stat-bound, not full database checksum or release claims. Unselected legacy mapping provenance is unchanged.",
        "The first400 history plan persisted in a destination mistakenly reused by the first actual invocation. That actual invocation refused before a native write; both are retained. The successful actual history command uses exclusive attempt002. Other dry-run and actual outputs use distinct destinations.",
        "Strict successor admission must preserve batch10's existing cheese and separately prepared338 paths; batch137's parsed-document taxonomy/snippet/ledger mutation controls; and batch139's505 admission and current biology/participant/snippet controls. Saved checkpoint verification precedes any caller adaptation. These later proof/caller/product steps are separate from this native diagnostic.",
    ],
    "links": [
        "https://github.com/CultureBotAI/CommunityMech/issues/2848",
        "https://github.com/CultureBotAI/CommunityMech/issues/2486",
        "https://github.com/CultureBotAI/CommunityMech/issues/2487",
        "https://github.com/CultureBotAI/CommunityMech/issues/2488",
        "https://github.com/CultureBotAI/CommunityMech/issues/2489",
        "https://github.com/CultureBotAI/CommunityMech/pull/2881",
    ],
}


def read(name, expected=None):
    raw = (ROOT / name).read_bytes()
    if expected is not None and hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError("reviewed input differs: " + name)
    return json.loads(raw)


def main():
    units = []
    for short, pin in CHECK_PINS.items():
        check = read(f"{PUBLIC}/{short}-check-config-001.json", pin)
        application = read(check["application_receipt"], check["application_receipt_sha256"])
        identity = f"CommunityMech:{int(short):06d}"
        if (
            application["target_id"] != identity
            or application["after_sha256"] != check["after_sha256"]
        ):
            raise ValueError("actual application identity differs")
        prefix = identity.split(":")[1]
        gates = {
            gate: f"{PRIVATE}/{short}-{gate}-{'002' if short == '400' and gate == 'new-history' else '001'}"
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
        }
        history = read(gates["new-history"] + "/receipt.json")
        if (
            history["plan"] is not False
            or history["exit_code"] != 0
            or len(history["new_history_sidecars"]) != 1
        ):
            raise ValueError("actual persisted native history required")
        sidecar, sidecar_sha = next(iter(history["new_history_sidecars"].items()))
        metadata = f"{PUBLIC}/{short}-source-evidence-001.json"
        source, locator = SOURCE[short]
        context = check["history_details"]
        evidence = [
            {
                "evidence_id": prefix + "-paper",
                "kind": "primary_source",
                "reference": "references_cache/" + source,
                "locator": locator,
                "support": "supports",
                "summary": PAPER_CLAIMS[short],
            },
            {
                "evidence_id": prefix + "-database",
                "kind": "database",
                "reference": metadata,
                "locator": "Selected occurrences: exact descriptor/rank, local authority rows and complete native results; exact source-binding pins",
                "support": "supports",
                "summary": "The selected source descriptors retain their stock and rank boundaries. Complete native options and any18/1 species reference blocks are reproducible from the pinned crosswalk, without stock-genome assignment or inferred nomenclature.",
            },
            {
                "evidence_id": prefix + "-application",
                "kind": "record_content",
                "reference": check["application_receipt"],
                "locator": "Actual execution_revision, before/after hashes, reviewed receipt and unchanged captured inputs",
                "support": "supports",
                "summary": "The actual M5 application persisted the independently accepted candidate. Only declared taxonomy mapping/status/options and native events change; all source stocks, biology, quotes and prior events remain.",
            },
        ]
        assessments = []
        for suffix, area, topic, refs, summary in [
            (
                "source",
                "grounding",
                "Source-stock and experimental boundaries",
                ["paper", "database", "terms"],
                context,
            ),
            (
                "population",
                "grounding",
                "Complete native reference correspondence without stock assignment",
                ["database", "gtdb", "domain"],
                "The selected native reference alternatives/correspondences are retained without choosing an ambiguous species, merging stock identities or assigning a study genome. Source taxonomic rank and all unselected descriptors remain unchanged.",
            ),
            (
                "provenance",
                "provenance",
                "Actual bounded transition with existing science preserved",
                ["application", "schema", "strict", "scalars", "new-history", "history"],
                "Actual guarded persistence, one appended sidecar and eight native scoped commands bind the accepted bytes. Full scientific review, source-snippet coverage, strict historical integration and generated products require separate evidence.",
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
                "selector": SELECTORS[short],
                "label": "Bounded reference diagnostic for " + identity,
                "stage_directory": f"{PRIVATE}/{short}-candidate-001",
                "history_sidecar": sidecar,
                "history_sidecar_sha256": sidecar_sha,
                "source_metadata_output": metadata,
                "gates": gates,
                "evidence": evidence,
                "assessments": assessments,
            }
        )
    output = ROOT / PUBLIC / "seven-review-config-001.json"
    with output.open("x") as handle:
        handle.write(json.dumps({"review": REVIEW, "records": units}, indent=2) + "\n")
    raw = output.read_bytes()
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
