"""Build the append-only PR 2054 S1 qualification as JSON for the native saver.

Reads the immutable predecessor and scratch source/check receipts. It writes no
canonical YAML, historical bundle, cache, history, or generated product. The
native record_review.py validator and saver own the eventual review pair.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shlex
from datetime import datetime, timezone
from pathlib import Path

import yaml

PREDECESSOR = Path("reviews/structured/20261021T231001Z-jn4-gd17-record-review/review.yaml")
TARGET = "CommunityMech:000180"
REPOSITORY = "CultureBotAI/CommunityMech"
SCRATCH = Path(".temp/pr2054/independent-third")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text())


def evidence(key, kind, reference, locator, summary, path, accessed_at, support="supports"):
    return {
        "evidence_id": key,
        "kind": kind,
        "reference": reference,
        "locator": locator,
        "summary": summary,
        "snapshot_sha256": digest(path),
        "accessed_at": accessed_at,
        "support": support,
    }


def assessment(key, area, topic, outcome, summary, ids, details):
    return {
        "assessment_id": key,
        "area": area,
        "topic": topic,
        "outcome": outcome,
        "summary": summary,
        "target_ids": [TARGET],
        "evidence_ids": ids,
        "details": details,
    }


def build(inspection_path: Path, started_at: str, lint_path: Path) -> dict:
    original = yaml.safe_load(PREDECESSOR.read_text())
    inspection = read_json(inspection_path)
    assert inspection["targets"] == original["targets"]
    assert inspection["source"]["state"] == "working_tree"
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    xml = SCRATCH / "PMC6746925.xml"
    source_receipt = next(
        r
        for r in read_json(SCRATCH / "fresh-fulltext-receipts.json")
        if r["name"] == "PMC6746925.xml"
    )
    accessed = source_receipt["observed_at"].replace("+00:00", "Z")
    source = "PMID:31551972; doi:10.3389/fmicb.2019.02035"
    summaries = {
        "identity": (
            "Strains and Chemicals; Enhanced End-Product Formation",
            "Methods identifies JN4 (CGMCC 1.5210) and GD17 (CGMCC 1.5209). "
            "The authors report reconstruction with both strains and present PCR as confirmation. "
            "This is author-reported identity, not independent certification of the S1 controls.",
        ),
        "recipe": (
            "Bacterial Growth",
            "The complete CTFUD formulation and substrate alternatives are available. "
            "Keep salt forms, unspecified resazurin stock strength, seed context, and "
            "0.5% substrate arms separate; do not infer missing gas ratios or culture pH.",
        ),
        "growth": (
            "Bacterial Growth; Enhanced End-Product Formation",
            "Anaerobic tubes/serum bottles at 60 C without agitation, 10% seed addition, "
            "and a separately stated 1:1 reconstruction ratio are reported. "
            "At least five passages is a reconstruction statement, not an endpoint abundance.",
        ),
        "volumes": (
            "Analytical Methods",
            "Cellulose-grown JN4 monoculture and coculture use 80 mL; independent "
            "glucose/cellobiose member-monoculture assays use 50 mL. These are not "
            "demonstrated sugar-coculture arms or interchangeable vessel capacities.",
        ),
        "analytical": (
            "Analytical Methods; Biomass and Bacterial Ratio Determination; Real-Time PCR",
            "Products, protein-based biomass estimates, 16S DNA proportions and "
            "recA-normalized transcription are different measurements. Added-carbon "
            "and sampling-time differences prevent selective flux or viable-growth attribution.",
        ),
        "xylose": (
            "GD17 growth/biomass results; Figure 4C; tentative Figure 6B",
            "Weak GD17 corncob growth and a proposed hemicellulose-to-xylose benefit "
            "do not demonstrate xylose release, transfer or JN4 benefit. The route "
            "should remain an authors' hypothesis, not be declared impossible.",
        ),
        "contexts": (
            "Reference Chimtong et al. 2011; Reference Liu et al. 2008; Figures 1-7",
            "The cited hemicellulose isolate is NOI-1, not GD17. The 2019 bibliography "
            "misattaches PMID 27538932 to the distinct 2008 DOI. Seven fresh main "
            "figures were inspected; their outcomes and conceptual model do not "
            "override these identity or inferential boundaries.",
        ),
    }
    ev = [
        evidence(k, "primary_source", source, loc, summary, xml, accessed)
        for k, (loc, summary) in summaries.items()
    ]
    supplement = read_json(SCRATCH / "supplement-retry-receipt.json")
    ev.append(
        evidence(
            "supplement",
            "primary_source",
            source,
            "Supplementary Figure S1, Image_1.TIF; Table S1; S2-S3",
            "Fresh S1 displays G/J/C lanes in every primer group; the JN-1/JN-2 "
            "bands appear in G and C while J is blank. The caption additionally "
            "names G as T. thermocellum and J as C. thermocellum JN4. The positive "
            "C lanes are compatible with the authors' report but cannot independently "
            "certify the stated strain specificity while these labels conflict. "
            "S2 compares expression and S3 compares stimulant growth. The full "
            "primer table retains duplicated licB rows. No sequence reanalysis was done.",
            SCRATCH / "supplement-180/Image_1.TIF",
            supplement["finished_at"].replace("+00:00", "Z"),
            "context_only",
        )
    )
    authorities = read_json(SCRATCH / "fresh-authority-and-access-receipts.json")
    tax_receipt = next(r for r in authorities if r["path"].endswith("taxonomy.xml"))
    ev.extend(
        [
            evidence(
                "strain",
                "authority",
                "NCBI Taxonomy efetch: 1515 and 1517",
                "Species names/ranks; source-local JN4/GD17 designations",
                "NCBI confirms species-level Acetivibrio thermocellus and "
                "Thermoanaerobacterium thermosaccharolyticum. Source collection "
                "accessions remain author-reported; no direct CGMCC catalogue "
                "certification or invented strain CURIE is asserted.",
                SCRATCH / "taxonomy.xml",
                tax_receipt["observed_at"].replace("+00:00", "Z"),
            ),
            evidence(
                "gtdb",
                "authority",
                "KG-Microbe NCBI2GTDB.tsv.gz; scripts/gtdb_ground.py --community",
                "Exact ncbi_id mappings for 1515 and 1517",
                "Fresh community-mode replay preserves both 1.0/18 mappings. "
                "Crosswalk SHA256 is "
                "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. "
                "July 25 is file metadata, not a verified latest release/build. "
                "The name-comparison flag does not establish biological reclassification.",
                SCRATCH / "000180/gtdb-ground.stdout",
                now,
            ),
            evidence(
                "schema",
                "authority",
                "src/communitymech/schema/communitymech.yaml; AGENTS.md",
                "FunctionalRoleEnum; cultivation and evidence definitions; optional state",
                "Current role, evidence and cultivation semantics support the retained "
                "actions. Ecological state remains optional. Host, soils and community "
                "relations do not create mandatory omissions for this liquid bacterial pair.",
                Path("src/communitymech/schema/communitymech.yaml"),
                now,
            ),
            evidence(
                "predecessor",
                "prior_review",
                str(PREDECESSOR),
                "evidence[evidence_id=supplement].summary; findings and all four actions",
                "The predecessor positively described S1 as supporting primer-specific "
                "membership while mentioning only its caption-name discrepancy. "
                "This successor withdraws that independent proof inference, preserves "
                "the immutable old bytes, and retains all three open record findings.",
                PREDECESSOR,
                now,
                "context_only",
            ),
            evidence(
                "focused-qc",
                "validation",
                str(SCRATCH / "focused-checks.json"),
                "CommunityMech:000180 entries; current unchanged target",
                "Seven focused record gates passed with real exit 0 before this "
                "agent switched from independent reader to correction author. "
                "The record and relevant validator bytes are unchanged; these receipts "
                "are reused explicitly, not claimed as independent approval of this successor.",
                SCRATCH / "focused-checks.json",
                now,
            ),
            evidence(
                "access",
                "primary_source",
                "PMID:27538932; doi:10.1007/s00253-016-7776-1",
                "Fresh Europe PMC abstract and publisher subscription preview",
                "The 2016 hydrogen paper remains abstract/preview only. Its reported "
                "comparative rate does not certify the full assay. The 2008 API "
                "returns bibliographic coredata, not a complete body. Current partial "
                "status is preserved despite complete fresh access to the 2019 SI.",
                SCRATCH / "pmid27538932.json",
                now,
                "context_only",
            ),
            evidence(
                "metrics",
                "validation",
                original["targets"][0]["path"],
                "Current native rubric presence and evidence counts",
                "Unchanged record has three nodes, two qualified arrows and six node "
                "evidence occurrences. The three retained findings are one P2 and "
                "two P3. Presence completeness is 85; quality raw 121, capped 100. "
                "Rubric required-field wording is a scoring rule, not LinkML requiredness.",
                Path(original["targets"][0]["path"]),
                now,
            ),
        ]
    )
    findings = copy.deepcopy(original["findings"])
    for f in findings:
        f["previous_occurrences"] = [
            {
                "repository": REPOSITORY,
                "review_id": original["review_id"],
                "finding_id": f["finding_id"],
            }
        ]
    checks = []
    for q in read_json(SCRATCH / "focused-checks.json"):
        if q["target"] != TARGET or q["label"] in {"inspect", "review-validate"}:
            continue
        assert q["exit_code"] == 0
        checks.append(
            {
                "check_id": q["label"],
                "name": "Focused " + q["label"],
                "status": "passed",
                "required": True,
                "summary": "Exit 0 on the unchanged current target; exact receipt retained.",
                "target_ids": [TARGET],
                "command": shlex.join(q["command"]),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": ["focused-qc"],
                "scope_note": "Run before the author's role switch; no target/validator edit.",
            }
        )
    lint = read_json(lint_path)
    assert lint["exit_code"] == 0
    checks.append(
        {
            "check_id": "full-lint",
            "name": "Full repository lint before helper freeze",
            "status": "passed",
            "required": True,
            "summary": "Black, Ruff and mypy passed before the helper was committed and pinned.",
            "target_ids": [TARGET],
            "command": lint["command"],
            "exit_code": 0,
            "expected_exit_code": 0,
            "evidence_ids": [],
        }
    )
    assessments = [
        assessment(
            "s1-proof-correction",
            "evidence",
            "Bound the predecessor S1 inference",
            "concern",
            "Withdraw independent primer-specific membership proof from S1.",
            ["supplement", "predecessor", "identity"],
            "Issue #2544 concerns this review-metadata sentence only. Attribute the pair "
            "and the authors' PCR-confirmation statement to Methods. Explicitly preserve "
            "the G/J/C band-label conflict and separate caption typo. Do not relabel lanes, "
            "infer another member, assert failed reconstruction or redesign primers. "
            "The independent predecessor audit identified this defect; this document is "
            "the author remediation and requires a separate read-only re-review.",
        ),
        assessment(
            "identity",
            "identity",
            "Exact reconstructed pair",
            "supported",
            "The source-reported JN4/GD17 identity remains appropriate.",
            ["identity", "strain", "supplement"],
            "Historical names, current NCBI species labels and author-reported strain "
            "accessions remain distinct. The ambiguous S1 controls do not independently "
            "certify specificity or justify changing canonical membership.",
        ),
        assessment(
            "culture",
            "scope",
            "CTFUD and assay-specific cultivation",
            "concern",
            "The original cultivation finding and all its acceptance checks remain open.",
            ["recipe", "growth", "volumes", "analytical", "schema"],
            "The full source contradicts the record's no-working-volume/abstract-only "
            "limitations. Preserve exact source forms, separate culture arms and omit "
            "invented static-operation rationale; no canonical change occurs here.",
        ),
        assessment(
            "xylose",
            "evidence",
            "Proposed hemicellulose benefit",
            "concern",
            "The original xylose hypothesis-qualification finding remains open.",
            ["xylose", "contexts"],
            "Weak corncob growth and a tentative model do not establish GD17 xylose "
            "release or JN4 uptake. The different NOI-1 background reference stays scoped.",
        ),
        assessment(
            "taxonomy",
            "grounding",
            "Valid mappings and unsupported provenance shorthand",
            "concern",
            "The original GTDB snapshot finding remains open; core mappings reproduce.",
            ["gtdb", "strain"],
            "Retain exact IDs, lineages, 1.0 fractions and 18-genome counts for both "
            "species. A local file date does not establish a release called latest.",
        ),
        assessment(
            "graph",
            "graph",
            "Measured outcomes versus inferred mechanisms",
            "supported",
            "Three nodes and two qualified arrows remain appropriately bounded.",
            ["analytical", "contexts", "access"],
            "Community products, independent sugar conversion, estimated JN4 biomass, "
            "DNA proportions and transcription are distinct. Preserve confounding from "
            "added carbon and different sampling times; no direct flux, viable-cell "
            "count, reciprocal harm, obligatory dependence or required abundance is inferred.",
        ),
        assessment(
            "coverage",
            "scope",
            "Current access and historical limits",
            "unknown",
            "Partial scientific scope remains necessary because the 2016 full assay is unavailable.",
            ["access", "supplement", "predecessor"],
            "Fresh 2019 body, seven main figures, three SI figures and complete primer "
            "table were read. The first SI transfer timed out and the second completed. "
            "The predecessor's dates and source limits remain historical; no unavailable "
            "/private/tmp artifact is an active input or claimed newly read source.",
        ),
        assessment(
            "validation",
            "schema",
            "Native focused gates and current guidance",
            "supported",
            "Current record validators pass independently of the scientific limitations.",
            ["focused-qc", "schema"],
            "The existing source caches have accurate content-type headers and remain "
            "unchanged. Existing append-only graph history and the open flux/growth "
            "knowledge-gap discussion remain bounded. No new cache/history repair or "
            "request to perform experiments is introduced.",
        ),
    ]
    metric = copy.deepcopy(
        next(a for a in original["assessments"] if a["assessment_id"] == "metrics")
    )
    metric["details"] = (
        "Rechecked against the unchanged current record and three retained curation findings. "
        "Presence scores do not certify scientific completion or make optional state mandatory."
    )
    assessments.append(metric)
    return {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-jn4-gd17-s1-proof-correction",
        "kind": "record",
        "repository": REPOSITORY,
        "title": "JN4/GD17 review successor: qualify ambiguous S1 membership proof",
        "started_at": started_at,
        "finished_at": now,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author remediation after a separate read-only pass identified "
            "the S1 defect. A different agent will re-review this successor; no independent "
            "approval or person-level independence is claimed here.",
        },
        "skill": original["skill"],
        "completion": "partial",
        "verdict": "needs_curation",
        "scientific_review": False,
        "summary": "Append-only qualification for issue #2544: S1 cannot independently "
        "certify primer-specific membership because its G/J/C lane-band assignments and "
        "caption conflict. Preserve author-reported JN4/GD17 identity, all three open "
        "record-curation findings and their full acceptance checks. The 2016 full-source "
        "limit remains unresolved; no canonical records or previous reviews are changed.",
        "source": inspection["source"],
        "targets": inspection["targets"],
        "scope": {
            "description": "Current unchanged 000180 target and all three predecessor "
            "findings/actions; fresh 2019 body/figures/SI and available 2016 abstract; "
            "bounded correction of the predecessor's S1 inference.",
            "selection": "Only CommunityMech:000180 in PR #2054.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TARGET],
            "exclusions": [
                {"target": "Other PR #2054 records", "reason": "Outside this author successor."}
            ],
        },
        "checks": checks,
        "evidence": ev,
        "assessments": assessments,
        "findings": findings,
        "actions": copy.deepcopy(original["actions"]),
        "limitations": [
            "The 2016 hydrogen paper remains abstract/preview only; 2008 body is unavailable. "
            "Do not certify complete hydrogen-assay review or import their missing Methods.",
            "S1 contains unresolved lane/control-label ambiguity and a caption typo. "
            "No lane relabeling, contamination finding, failed reconstruction or new member follows.",
            "No raw sequencing, numerical, viable-cell or flux reanalysis was performed. "
            "Protein-based biomass and comparative metabolism do not establish selective causality.",
            "All prior bundles are immutable. Their old /private/tmp source paths are "
            "historical references only, not recoverable current inputs.",
            "This is an author remediation, not the independent re-review. Native save, "
            "bundle/contract and writer-gate receipts are reported separately after saving.",
        ],
        "notes": [
            "The original 000180 evidence summary is explicitly qualified rather than silently rewritten.",
            "The open jn4_gd17_flux_and_growth_partition discussion remains an evidence-watch "
            "boundary. No action demands experiments.",
            "AGENTS.md is pinned directly; the CLAUDE.md symlink is not a current input.",
        ],
        "related_reviews": [
            {
                "repository": REPOSITORY,
                "review_id": original["review_id"],
                "relationship": "Current-input successor retaining all three open findings; "
                "explicitly qualifies the predecessor evidence_id supplement S1 proof statement.",
            }
        ],
        "links": ["https://github.com/CultureBotAI/CommunityMech/issues/2544"],
        "tags": ["pr-2054", "append-only", "author-remediation", "s1-proof-boundary"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inspection", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--started-at", required=True)
    parser.add_argument("--lint-receipt", required=True, type=Path)
    args = parser.parse_args()
    result = build(args.inspection, args.started_at, args.lint_receipt)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(result["review_id"])


if __name__ == "__main__":
    main()
