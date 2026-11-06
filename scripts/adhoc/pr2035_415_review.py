"""Build the PR2035/415 successor from current inspection and fresh source receipts.

Writes a JSON candidate; the repository's native helper owns immutable YAML saving.
Never changes canonical records, source caches, history or historical reviews.
"""

from __future__ import annotations

import copy
import json

import yaml
from pr2035_415_audit import OLD, ROOT, SCRATCH, TARGET, now, run, sha, write

ID = "CommunityMech:000415"
HISTORY = "history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-21T190000Z-claude-2048.yaml"
STAGE5 = "reviews/structured/20261021T193000Z-stage5-remediation-verification/review.yaml"


def main():
    initial = json.loads((SCRATCH / "inspection.json").read_text())
    # Recheck immutable scientific inputs before freezing the authored successor.
    for item in initial["source"]["inputs"]:
        if item["path"] != "scripts/adhoc/pr2035_415_audit.py":
            assert sha((ROOT / item["path"]).read_bytes()) == item["sha256"], item["path"]
    search = run(
        "local-search-v2",
        [
            "rg",
            "--no-ignore",
            "--hidden",
            "-n",
            "41745484|1369521|Algal_Methanotroph_Biogas_Valorization_Coculture",
            "references_cache",
            "history/records",
            "reports/causal_graph_review/decisions",
            "kb/taxa",
        ],
    )
    assert search.returncode == 0
    paths = {x["path"] for x in initial["source"]["inputs"] if x["role"] != "target"}
    paths.update(
        str(p.relative_to(ROOT))
        for p in SCRATCH.iterdir()
        if p.is_file()
        and not p.name.startswith(
            ("candidate", "native-validate", "inspect-final", "inspection-final")
        )
    )
    paths.add("scripts/adhoc/pr2035_415_review.py")
    args = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(SCRATCH / "targets.json"),
    ]
    for path in sorted(paths):
        args += ["--input", path]
    result = run("inspect-final-v2", args)
    assert result.returncode == 0, result.stderr.decode()
    inspected = json.loads(result.stdout)
    write("inspection-final-v2.json", inspected)
    timestamp = now()
    old = yaml.safe_load((ROOT / OLD).read_text())
    doc = copy.deepcopy(old)
    rid = timestamp[:19].replace("-", "").replace(":", "") + "Z-pr2035-algal-methanotroph-successor"
    doc.update(
        review_id=rid,
        title="Algal–methanotroph biogas coculture: current-main review successor",
        started_at=json.loads((SCRATCH / "inspect.json").read_text())["started_at"],
        finished_at=timestamp,
        source=inspected["source"],
        targets=inspected["targets"],
    )
    doc["reviewer"] = {
        "identity": "codex",
        "kind": "agent",
        "independence": "unknown",
        "independence_basis": "Author refresh of the stale PR2035 bundle; independent adversarial approval is a separate pass. Historical Codex curation prevents person-level independence claims.",
    }
    doc["summary"] = (
        "Current record adds Leptolyngbya to the qualified community-level oxygen-support node, resolving the predecessor's disconnected-member observation. Four prior curation findings remain. New findings identify an incorrect append-only history event and explicitly track omitted source-supported assay conditions. Two major, three minor and one informational findings remain open. Eight focused/preflight gates pass; corpus network warnings retain their actual nonzero exits."
    )
    doc["scope"][
        "selection"
    ] = "PR2035 staleness refresh: current origin/main target differs from the predecessor only by Leptolyngbya participation and embedded history. All six taxa, both nodes, no arrows, source claims and five history files were reassessed."
    doc["checks"] = []
    evidence = [
        copy.deepcopy(e) for e in old["evidence"] if not e["evidence_id"].startswith("check-")
    ]
    evidence_by_id = {e["evidence_id"]: e for e in evidence}

    def ev(eid, kind, reference, locator, summary, path=None, support="supports"):
        item = {
            "evidence_id": eid,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "summary": summary,
            "support": support,
            "accessed_at": timestamp,
        }
        if path:
            item["snapshot_sha256"] = sha((ROOT / path).read_bytes())
        evidence.append(item)
        return item

    for e in evidence:
        e["accessed_at"] = timestamp
        e.pop("snapshot_sha256", None)
    for eid in ["primary", "gas", "exchange", "methods", "composition", "cultivation"]:
        evidence_by_id[eid]["snapshot_sha256"] = sha((SCRATCH / "primary.xml").read_bytes())
        evidence_by_id[eid]["accessed_at"] = json.loads((SCRATCH / "sources.json").read_text())[0][
            "accessed_at"
        ]
    evidence_by_id["primary"][
        "locator"
    ] = "Fresh Europe PMC XML: PMID41745484/PMC12941554/doi10.3390/md24020081; Results2.1–2.3 and Methods3.1–3.4, Table1 read in full; public XML retrieval receipt and bytes frozen."
    evidence_by_id["record"]["snapshot_sha256"] = sha((ROOT / TARGET).read_bytes())
    for eid, name in [
        ("publication", "publication.xml"),
        ("dataset", "bioproject.json"),
        ("ontology", "ontology-authorities.json"),
        ("snippets", "snippet-replay.json"),
        ("local-search", "local-search-v2.stdout.txt"),
    ]:
        evidence_by_id[eid]["snapshot_sha256"] = sha((SCRATCH / name).read_bytes())
    evidence_by_id["schema"]["snapshot_sha256"] = sha(
        (ROOT / "src/communitymech/schema/communitymech.yaml").read_bytes()
    )
    evidence_by_id["history"].update(
        locator="Five append-only history files plus embedded history and the prior graph decision",
        summary="The four older entries describe creation and gas/light, dangling-edge and uncertainty repairs. The October21 external event is misattributed: it names record000446, Methylocystis/Desmodesmus and a lipid node, while the actual current target change adds Leptolyngbya to 000415's oxygen-support node. Embedded history matches the actual change. Do not use the erroneous external prose to certify the target.",
    )
    evidence_by_id["adapter"].update(
        kind="record_content",
        reference=TARGET,
        locator="All taxon and interaction assertions; applicability assessment only",
        summary="No strain-specific regulatory assertion or expression-module claim is curated. An expression-source lookup is not required for the actual community gas, metagenomic abundance and inferred exchange assertions; no current catalog search or dataset absence is claimed.",
        support="context_only",
    )
    evidence_by_id["cultivation"][
        "summary"
    ] += " Final assays used25 degrees C and200rpm magnetic stirring; Table1 reports56days; the prepared MSM was adjusted to initialpH9. These are distinct from150rpm orbital inoculum growth."
    ev(
        "predecessor",
        "prior_review",
        OLD,
        "All five prior findings, four actions, whole-record assessments and frozen target",
        "Every predecessor finding is rechecked. Stable issue keys and exact finding occurrence references are retained; only the single-target disconnected-member observation is resolved.",
        OLD,
    )
    ev(
        "target-diff",
        "record_content",
        ".temp/pr2035/415/target-diff.stdout.txt",
        "Exact target diff from predecessor base to current HEAD",
        "Only Leptolyngbya47251 participation in node0 and the embedded October21 event changed. The previously flagged role, wording, evidence-locator and media-linkage fields are unchanged.",
        ".temp/pr2035/415/target-diff.stdout.txt",
    )
    ev(
        "target-network",
        "validation",
        ".temp/pr2035/415/target-network.json",
        "NetworkIntegrityAuditor.audit_community on the current entire target",
        "No target network issues. Every curated member occurs in a community-level participant list; this structural result does not demonstrate partner-specific exchange.",
        ".temp/pr2035/415/target-network.json",
    )
    ev(
        "history-mismatch",
        "record_content",
        HISTORY,
        "events[0].summary and events[0].details versus target path, current diff and embedded history",
        "The external event claims two different taxa, CommunityMech000446 and a different node, while the exact diff shows Leptolyngbya in record000415. It needs an append-only correction, not rewriting the old event.",
        HISTORY,
    )
    ev(
        "stage5-context",
        "prior_review",
        STAGE5,
        "finding stage4-disconnected-syncom-participants description; context only",
        "The preexisting multi-target finding describes000415 using Parachlorella kessleri NIES-2152/3074, inconsistent with both current target and primary source Leptolyngbya47251. Its terminal status is not used as scientific proof. This one-target successor does not retire or adjudicate that multi-target issue key.",
        STAGE5,
        "context_only",
    )
    for prior in old["checks"]:
        cid = prior["check_id"]
        if cid == "optional-adapter":
            doc["checks"].append(
                {
                    "check_id": cid,
                    "name": "Structured expression-source applicability",
                    "status": "not_applicable",
                    "required": False,
                    "summary": "No strain-specific regulatory assertion is curated; no adapter execution or current catalog absence is claimed.",
                    "target_ids": [ID],
                    "evidence_ids": ["adapter"],
                }
            )
            continue
        receipt = json.loads((SCRATCH / f"{cid}.json").read_text())
        output = (SCRATCH / f"{cid}.stdout.txt").read_text() + (
            SCRATCH / f"{cid}.stderr.txt"
        ).read_text()
        network = cid in {"audit-network", "check-network-quality"}
        summary = (
            "Actual fresh corpus run:503 records,44 warnings in16 records,0 errors; exit1 retained. This target has no warnings. No corpus remediation is authorized by this review."
            if network
            else output.strip() or "Command completed without reported issues."
        )
        env = receipt["environment"]
        command = " ".join(f"{k}={v}" for k, v in sorted(env.items())) + " " + receipt["command"]
        doc["checks"].append(
            {
                "check_id": cid,
                "name": cid,
                "status": "failed" if receipt["exit_code"] else "passed",
                "required": True,
                "summary": summary,
                "target_ids": [ID],
                "command": command,
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + cid],
                "scope_note": "Corpus-level existing warnings retained; focused target gates have no failures. Reference validation followed clean cache-name preflight and all inspected canonical input bytes remain unchanged.",
            }
        )
        ev(
            "check-" + cid,
            "validation",
            command,
            f"Actual execution {receipt['started_at']} to {receipt['finished_at']}; receipt .temp/pr2035/415/{cid}.json",
            summary,
            f".temp/pr2035/415/{cid}.json",
        )
    for f in doc["findings"]:
        f["previous_occurrences"] = [
            {
                "repository": doc["repository"],
                "review_id": old["review_id"],
                "finding_id": f["finding_id"],
            }
        ]
    resolved = doc["findings"][-1]
    resolved.update(
        status="resolved",
        description="The predecessor observed Leptolyngbya missing from both participant lists. Current main explicitly includes Leptolyngbya47251 in the PARTIAL community-level oxygen-support node. Source sections2.3/2.3.1 report its detection and phototrophic community context. This supports bounded participation without a taxon-resolved transfer or new edge.",
        disposition_reason="Direct current-record inspection, exact target diff, source sections2.3/2.3.1 and a fresh empty target-network audit resolve this specific single-target omission. Neither the erroneous October21 external history prose nor the unrelated taxa in stage5 review prose are used as proof.",
        evidence_ids=["record", "target-diff", "composition", "gas", "target-network"],
    )
    owner = copy.deepcopy(doc["targets"][0]["owner_paths"])
    history_owner = [{"repository": doc["repository"], "path": HISTORY, "role": "curation_history"}]
    additions = [
        {
            "finding_id": "history-provenance",
            "issue_key": "cm-000415-history-provenance",
            "category": "provenance",
            "severity": "major",
            "native_severity": "P2",
            "normalization_reason": "P2: materially misidentifies the record, taxa and interaction whose curation it claims to document.",
            "rule_id": "AGENTS.append-only-history",
            "status": "open",
            "certainty": "confirmed",
            "title": "October21 history event describes different taxa and record",
            "description": "The history file targets the000415slug but its event names000446, Methylocystis hirsuta, Desmodesmus abundans and a lipid-valorization node. The actual change adds Leptolyngbya47251 to000415's oxygen-support node. Schema validation does not establish history accuracy.",
            "target_ids": [ID],
            "field_paths": ["events[0].summary", "events[0].details"],
            "evidence_ids": ["history-mismatch", "target-diff", "record"],
            "owner_paths": history_owner,
        },
        {
            "finding_id": "assay-conditions",
            "issue_key": "cm-000415-assay-conditions",
            "category": "completeness",
            "severity": "informational",
            "native_severity": "P4",
            "normalization_reason": "P4: optional source-supported cultivation enrichment; the existing assay is not invalidated.",
            "rule_id": "review-yaml-record.completeness",
            "status": "open",
            "certainty": "confirmed",
            "title": "Track omitted final-assay cultivation conditions",
            "description": "The predecessor requested later cultivation enrichment without a tracked action. Methods3.2 give25degreesC and200rpm magnetic stirring; Table1 gives56days for the co-culture; Methods3.1 gives initial prepared-medium pH9. These conditions are absent from the entire current target. Later curation must distinguish initialpH from maintainedpH and final-assay magnetic stirring from150rpm orbital inoculum growth.",
            "target_ids": [ID],
            "field_paths": ["growth_media[0]", "cultivation_setup[0]"],
            "evidence_ids": ["cultivation", "record", "predecessor"],
            "owner_paths": owner,
        },
    ]
    doc["findings"].extend(additions)
    doc["actions"].extend(
        [
            {
                "action_id": "correct-history-append-only",
                "description": "Create a new append-only history correction that identifies the erroneous prior event and documents the actual Leptolyngbya addition to000415; preserve the old entry unchanged.",
                "finding_ids": ["history-provenance"],
                "target_ids": [ID],
                "owner_paths": history_owner,
                "acceptance_checks": [
                    "Correction matches the actual Git diff, source scope and embedded history.",
                    "No historical event is rewritten.",
                    "Run history and strict validators.",
                ],
            },
            {
                "action_id": "curate-assay-conditions",
                "description": "Represent supported final-assay temperature, stirring and duration, and initial medium pH with exact source evidence and experimental-stage qualifiers.",
                "finding_ids": ["assay-conditions"],
                "target_ids": [ID],
                "owner_paths": owner,
                "acceptance_checks": [
                    "25degreesC/200rpm magnetic stirring/56days are scoped to final co-culture assay.",
                    "pH9 is initial prepared-medium pH, not a claimed controlled trajectory.",
                    "Do not import150rpm orbital inoculum conditions; run strict/reference validation and append history.",
                ],
            },
        ]
    )
    assessments = {a["assessment_id"]: a for a in doc["assessments"]}
    assessments["node-0"][
        "details"
    ] = "Participants are Chlorella vulgaris, Dunaliella viridis, Leptolyngbya and Methylotuvimicrobium. Source sections2.3/2.3.1 support detected phototrophic membership; the PARTIAL node retains community-scale inferred oxygen support. No donor-resolved oxygen flux, reciprocal fitness or new causal arrow is established."
    assessments["resources"].update(
        outcome="concern",
        summary="Publication and BioProject identities resolve;35of36 snippets match normalized primaryXML and the DOI-labelled36th is in the bibliographic cache header. Five history files validate structurally, but the October21event's scientific identity is incorrect. Historical graph decisions and stage5 terminal status do not certify that event or this whole record.",
    )
    assessments["resources"]["evidence_ids"].extend(
        ["history-mismatch", "stage5-context", "target-diff"]
    )
    doc["assessments"].append(
        {
            "assessment_id": "stage5-identity-correction",
            "area": "provenance",
            "topic": "Bounded correction to Stage 5's CommunityMech:000415 identity clause",
            "outcome": "concern",
            "summary": "The description of finding stage4-disconnected-syncom-participants in review 20261021T193000Z-stage5-remediation-verification incorrectly identifies the missing member of CommunityMech:000415 as Parachlorella kessleri NIES-2152, NCBITaxon:3074. The current record, original Stage 4 descriptions and primary source sections 2.3/2.3.1 instead identify Leptolyngbya, NCBITaxon:47251. This append-only correction applies only to that 000415 identity clause. The other four targets and all grouped resolved dispositions are NOT reassessed; the multi-target issue key and occurrence lineage are not superseded.",
            "target_ids": [ID],
            "evidence_ids": ["stage5-context", "record", "composition", "target-diff"],
        }
    )
    assessments["validation"].update(
        summary="Eight focused/preflight gates pass and inspected canonical bytes remain unchanged. Both required corpus commands return1 for44warnings/16of503records,0errors. This target has no network issues after the Leptolyngbya participation addition; this is structural completeness, not proof of exchange."
    )
    assessments["validation"]["evidence_ids"].append("target-network")
    assessments["metrics"][
        "summary"
    ] = "Completeness90 and capped validation quality100 are rubric values, not scientific approval. Two major, three minor and one informational findings remain open; the original informational disconnected-member finding is resolved."
    for metric in assessments["metrics"]["metrics"]:
        if metric["name"] == "P2":
            metric["value"] = 2
        if metric["name"] in {"P1", "P2", "P3", "P4"}:
            metric["definition"] = (
                "Open native-severity finding count; resolved predecessor omission excluded."
            )
        if metric["name"] == "validation_quality":
            metric["definition"] = (
                "clamp(100-50*P1-10*P2-2*P3+20*min(mean node evidence/2,1)+15 if native COMPLETE,0,100). Open P1=0,P2=2,P3=3,P4=1;5evidence/2nodes; target network empty. clamp(100-20-6+20+15)=100."
            )
    doc["evidence"] = evidence
    doc["limitations"] = [
        "Primary Results/Discussion and Methods were freshly read from XML; separate supplements and raw metagenomic data were not reanalyzed.",
        "Shotgun taxonomic/gene attribution is not a direct measurement of taxon-resolved transfer, pathway activity or reciprocal fitness.",
        "BioProject metadata verifies project identity, not every sample accession or sequencing result.",
        "Bacterial GTDB assignments remain explicitly unresolved; coherence gates do not establish new mappings.",
        "Current reference validator coverage does not certify every assertion's source scope; direct36snippet replay complements it.",
        "Corpus network warning failures are retained explicitly. No out-of-scope canonical remediation was performed.",
        "The preexisting stage5 multi-target review misidentifies000415's member; this one-target successor explicitly excludes that prose from its scientific proof and does not adjudicate its multi-target lineage.",
    ]
    doc["notes"] = [
        "Immutable successor to the stale PR2035review; original review bytes retained.",
        "Current record changed only in participant membership and embedded history; frozen input hashes and new receipts reflect current main.",
        "Scientific source scope and all five original findings were independently reconsidered by the author; independent adversarial approval remains a separate pass.",
        "No canonical records, source caches, history entries or generated products were changed by this refresh.",
        "Three brief source quotes inherited after fresh verification total fewer than25words; new claims are paraphrased with section locators.",
    ]
    doc["tags"] += ["pr-2035", "staleness-refresh", "successor"]
    # Explicitly locate external-history fields rather than implying target YAML slots.
    history_finding = next(f for f in doc["findings"] if f["finding_id"] == "history-provenance")
    history_finding["field_paths"] = [
        HISTORY + ":events[0].summary",
        HISTORY + ":events[0].details",
    ]
    candidate = write("candidate-v2.json", doc)
    result = run(
        "native-validate-v2",
        ["uv", "run", "python", "scripts/record_review.py", "validate", str(candidate)],
    )
    assert result.returncode == 0, result.stderr.decode() + result.stdout.decode()
    print(
        json.dumps(
            {
                "candidate": str(candidate),
                "review_id": rid,
                "target_sha256": sha((ROOT / TARGET).read_bytes()),
            }
        )
    )


if __name__ == "__main__":
    main()
