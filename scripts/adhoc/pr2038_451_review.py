"""Author the PR 2038 record 451 successor as JSON for the native review saver."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import yaml
from pr2038_451_audit import OLD, ROOT, SCRATCH, TARGET, now, run, sha, write

ID = "CommunityMech:000451"


def main():
    initial = json.loads((SCRATCH / "inspection.json").read_text())
    for item in initial["source"]["inputs"]:
        assert sha((ROOT / item["path"]).read_bytes()) == item["sha256"], item["path"]
    paths = {item["path"] for item in initial["source"]["inputs"] if item["role"] != "target"}
    paths.update(str(p.relative_to(ROOT)) for p in SCRATCH.iterdir() if p.is_file())
    paths.add("scripts/adhoc/pr2038_451_review.py")
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
    result = run("inspect-final", args)
    assert result.returncode == 0, result.stderr.decode()
    inspected = json.loads(result.stdout)
    write("inspection-final.json", inspected)
    old = yaml.safe_load((ROOT / OLD).read_text())
    doc = copy.deepcopy(old)
    timestamp = now()
    rid = (
        timestamp[:19].replace("-", "").replace(":", "")
        + "Z-pr2038-auxenochlorella-pseudomonas-successor"
    )
    doc.update(
        review_id=rid,
        title="Auxenochlorella-Pseudomonas: current-main review successor",
        started_at=json.loads((SCRATCH / "inspect.json").read_text())["started_at"],
        finished_at=timestamp,
        source=inspected["source"],
        targets=inspected["targets"],
    )
    doc["reviewer"] = {
        "identity": "codex",
        "kind": "agent",
        "independence": "unknown",
        "independence_basis": "Author refresh of a stale PR 2038 bundle; historical Codex graph curation exists. This author pass does not claim independent adversarial approval.",
    }
    doc["summary"] = (
        "Current main adds bacterial DOMINANT prominence, a source-matching pair-membership snippet and an abundance history entry. The two members can be co-equal prominent partners under the current ordinal enum; no measured composition or precursor-wide dominance is inferred. Fresh primary article and supplement review retains all three original findings: bacterial consumer-role overstatement (P2), recoverable pair cultivation and treatment-arm representation (P3), and optional pyridoxal grounding (P4). Eight focused checks pass. The two corpus network commands retain their baseline exit 1 with 44 warnings across 16 of 503 records; this target has no native network issues."
    )
    doc["scope"].update(
        description="Entire current target: two members, one directed node, no downstream arrows, two factors, one dataset, 14 evidence occurrences and three history sidecars. Fresh main article, Text S9-S14 and Tables S3-S10, publication and BioProject metadata were inspected. No raw sequence, chromatogram, figure-image or population-composition reanalysis.",
        selection="Refresh the sole stale target in PR 2038 against merged current main. Parsed comparison identifies exactly three additions: taxonomy[1].abundance_level, taxonomy[1].evidence[2], and curation_history[2]. Every original finding was reassessed, preserving its issue key and exact predecessor.",
    )
    sources = {Path(x["path"]).name: x for x in json.loads((SCRATCH / "sources.json").read_text())}
    assert all(x["exit_code"] == 0 for x in sources.values())
    evidence = [
        copy.deepcopy(e) for e in old["evidence"] if not e["evidence_id"].startswith("check-")
    ]
    by_id = {e["evidence_id"]: e for e in evidence}
    for e in evidence:
        e["accessed_at"] = timestamp
        e.pop("snapshot_sha256", None)
    primary_ids = [
        "fulltext",
        "identity-source",
        "precursor",
        "pair-benefit",
        "supplementation",
        "consumer-scope",
        "genome-potential",
    ]
    for eid in primary_ids:
        by_id[eid]["snapshot_sha256"] = sources["primary.xml"]["sha256"]
        by_id[eid]["accessed_at"] = sources["primary.xml"]["accessed_at"]
    for eid, filename in [
        ("pubmed", "publication.xml"),
        ("crossref", "crossref.json"),
        ("supplement", "supplement.docx"),
        ("pair-medium", "supplement.docx"),
        ("pair-arms", "supplement.docx"),
        ("bioproject", "bioproject.xml"),
    ]:
        by_id[eid]["snapshot_sha256"] = sources[filename]["sha256"]
        by_id[eid]["accessed_at"] = sources[filename]["accessed_at"]
    by_id["record"].update(
        locator="Entire current record: two members, one directed pairwise node, no arrows, two factors, one dataset and 14 evidence occurrences",
        snapshot_sha256=sha((ROOT / TARGET).read_bytes()),
    )
    by_id["fulltext"].update(
        summary="Fresh complete primary main text, including abstract, Introduction, Methods, Results, Discussion, Conclusion, figure captions and data-availability statement, was inspected. Figure images and raw data were not reanalyzed."
    )
    by_id["supplement"].update(
        summary="Fresh public publisher DOCX was downloaded; Text S9-S14 and Tables S3-S10 were inspected as separate supplementary evidence. Its bytes remain separate from the committed article cache. Embedded figures and chromatogram images were not visually reassessed."
    )
    by_id["genome-potential"][
        "summary"
    ] = "Genome annotation reports vitamin-B6 biosynthetic potential and predicted secondary-metabolite clusters. Table S5 includes low-similarity cluster assignments, so these are not proof of specific chemical production. The target's broad computational-potential wording is supported; no assembly or pathway analysis was repeated."
    by_id["schema"].update(
        summary="CROSS_FEEDER denotes use of another taxon's metabolites. DOMINANT denotes the most prominent or co-equal most prominent members within this record, not a measured fraction or percentage threshold. Dataset and Discussion evidence uses SupportingReference, whose free-form evidence_source permits full_text; those values are not EvidenceItem enum violations."
    )
    by_id["ontology"].update(
        locator="All five unique curated NCBITaxon, ENVO and GO ID-label pairs across seven placements",
        summary="All five canonical labels match local OAK authority values. Generic NCBITaxon:306 plus the local Pseudomonas_sp1 strain designation does not establish a species. Laboratory and modeled freshwater environments remain distinct; GO:0044419 is a broad interaction process.",
        snapshot_sha256=sha((SCRATCH / "ontology-authorities.json").read_bytes()),
    )
    by_id["chemicals"].update(
        locator="Fresh local OAK labels and definitions for CHEBI:17310, CHEBI:87185 and CHEBI:60159",
        summary="CHEBI:17310 is pyridoxal, the measured vitamin-B6 aldehyde form; CHEBI:87185 is florfenicol; CHEBI:60159 is poly(lactic acid) polymer. These identifiers support bounded chemical enrichment, not traced transfer, polymer stereochemistry or particle morphology.",
        snapshot_sha256=sha((SCRATCH / "chemical-authorities.json").read_bytes()),
    )
    by_id["snippets"].update(
        locator="Every current snippet: 14 occurrences, including the new bacterial pair-membership evidence, against fresh XML and committed article cache",
        summary="All 14 current snippets match both sources after NFKC and whitespace normalization. The added selection sentence supports defined-pair membership; it does not quantify bacterial cell fraction or demonstrate metabolite consumption.",
        snapshot_sha256=sha((SCRATCH / "snippet-replay.json").read_bytes()),
    )
    by_id["history"].update(
        locator="Three target history sidecars, current embedded entries, and reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml exact CommunityMech:000451 row",
        summary="The historical graph decision's record hash matches the original review's frozen target and explicitly excludes non-graph certification. November 5 history accurately records the new bacterial abundance field and snippet. This limited curation neither resolves the original three findings nor establishes endogenous pyridoxal necessity or transfer.",
    )
    by_id["issue"].update(
        locator="Fresh read-only gh issue view 1244; issue-1244.json and its timestamped receipt",
        summary="Issue 1244 is CLOSED as of this review; its graph repair does not certify the separate role, medium or chemical-grounding fields.",
        snapshot_sha256=sha((SCRATCH / "issue-1244.json").read_bytes()),
    )
    by_id["search"].update(
        locator="Fresh ignored-inclusive exact ID, PMID, slug, algal ID and Pseudomonas_sp1 lookup",
        summary="The bounded query located the article cache, all three target sidecars and relevant graph decisions, with no exact local-isolate or algal-anchor hit in kb/taxa. No machine-wide or all-Pseudomonas absence is asserted.",
        search_scope="rg --no-ignore --hidden over references_cache, history, reports/causal_graph_review/decisions and kb/taxa in this worktree, including ignored files.",
        snapshot_sha256=sha((SCRATCH / "local-search.stdout.txt").read_bytes()),
    )
    by_id["dataset-audit"].update(
        locator="Fresh BioProject PRJNA1171391 XML and primary article Methods Sec8",
        summary="PRJNA1171391 resolves to genome-sequencing/raw-read metadata for phycospheric bacteria. The public metadata is generic and the article supplies the exact Pseudomonas_sp1 association. No individual read or assembly content was certified.",
        snapshot_sha256=sources["bioproject.xml"]["sha256"],
    )
    by_id["medium-linkage"].update(
        reference=TARGET,
        locator="growth_media and Text S12/S14; no current external recipe registry query",
        summary="The target has no encoded CultureMech or MediaIngredientMech linkage. The supplement names BG-11 without specifying the exact formulation; no unique external recipe equivalence was established in this refresh. The predecessor's historical 29-candidate registry result is not presented as a fresh result.",
        search_scope="Entire target and inspected supplementary Text S12/S14; exact external recipe matching was not performed.",
    )
    by_id["adapter"].update(
        locator="Fresh PATH and two exact sibling-checkout probes; public https://imodulondb.org/api/datasets fallback",
        summary="No installed kg-microbe-sources runner or either probed CLAW checkout was available. The public catalog has 20 organism entries including other Pseudomonas species, but no exact Pseudomonas_sp1 or Auxenochlorella dataset. No species or strain equivalence is inferred from those neighbors; catalog absence is not negative biological evidence.",
        search_scope="PATH plus two explicit sibling paths including ignored files, then the inspected public dataset catalog. No machine-wide absence or expression-module search is claimed.",
        snapshot_sha256=sources["imodulon-catalog.json"]["sha256"],
    )
    by_id["native-target"].update(
        locator="Fresh NetworkIntegrityAuditor().audit_community(current target) and complete node/participant inventory",
        summary="Native target audit returned no issues. One pairwise node has both current members as its directed participants, three evidence items and no downstream arrows, giving mean node evidence 3 and structurally complete participation.",
        snapshot_sha256=sha((SCRATCH / "target-network.json").read_bytes()),
    )
    evidence += [
        {
            "evidence_id": "current-delta",
            "kind": "record_content",
            "reference": TARGET,
            "locator": "Frozen original target versus merged current-main target, parsed semantic-diff.json",
            "summary": "Only taxonomy[1].abundance_level, taxonomy[1].evidence[2] and curation_history[2] were added. All original finding surfaces and the qualified graph remain semantically unchanged; wrapping changes have no semantic effect.",
            "support": "supports",
            "accessed_at": timestamp,
            "snapshot_sha256": sha((SCRATCH / "semantic-diff.json").read_bytes()),
        },
        {
            "evidence_id": "abundance-scope",
            "kind": "primary_source",
            "reference": "PMID:41724996",
            "locator": "Results Sec18; Methods Sec9; supplement Text S12 and Table S3; current AbundanceEnum",
            "summary": "The selected Pseudomonas_sp1 is the sole bacterial partner of axenic A. pyrenoidosa, with a measured bacterial-associated algal benefit. Co-equal DOMINANT annotations are defensible as prominence within this defined binary record. The source's precursor Pseudomonas genus enrichment, MIC resistance, inoculum CFU and algal cell counts are different measurements and are not a measured pair population fraction.",
            "support": "supports",
            "accessed_at": timestamp,
            "snapshot_sha256": sources["primary.xml"]["sha256"],
        },
        {
            "evidence_id": "abundance-lineage",
            "kind": "record_content",
            "reference": "reviews/structured/20261105T171000Z-c7s5-remediation-verification/review.yaml",
            "locator": "finding c7s4-000451-auxenochlorella-pseudomonas-sp1-abundance-level and its two exact c7s4 predecessors; issue-2120.json",
            "summary": "The later c7s5 bundle explicitly resolves the narrow missing-field finding from 20261105T144000Z-c7s4-record-deep-audit and 20261105T144100Z-c7s4-frozen-cohort-review. Fresh issue 2120 state is CLOSED. This refresh confirms the field is present and suitably scoped; it does not supersede any unrelated or grouped finding.",
            "support": "supports",
            "accessed_at": timestamp,
            "snapshot_sha256": sha((SCRATCH / "lineage.json").read_bytes()),
        },
    ]
    checks = []
    names = [
        "validate",
        "validate-strict",
        "validate-terms",
        "validate-gtdb",
        "validate-gtdb-domain",
        "validate-history",
        "normalize-cache-names-check",
        "validate-references-explained",
        "audit-network",
        "check-network-quality",
    ]
    old_checks = {c["check_id"]: c for c in old["checks"]}
    for name in names:
        receipt = json.loads((SCRATCH / f"{name}.json").read_text())
        network = name in {"audit-network", "check-network-quality"}
        summary = (
            "Fresh corpus check returned baseline exit 1: 44 warnings across 16 of 503 records. This target has no native network issues."
            if network
            else old_checks[name]["summary"]
        )
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "passed" if receipt["exit_code"] == 0 else "failed",
                "required": True,
                "summary": summary,
                "target_ids": [ID],
                "command": receipt["command"],
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + name],
                "scope_note": (
                    "Corpus-wide gate; existing warning exit retained and not relabeled as a target pass."
                    if network
                    else "Fresh focused target/history check, except read-only corpus cache-name preflight; exact runtime environment recorded in the pinned receipt."
                ),
            }
        )
        evidence.append(
            {
                "evidence_id": "check-" + name,
                "kind": "validation",
                "reference": receipt["command"],
                "locator": f".temp/pr2038/451/{name}.json; actual execution {receipt['started_at']} to {receipt['finished_at']}",
                "summary": summary,
                "support": "supports",
                "accessed_at": receipt["finished_at"],
                "snapshot_sha256": sha((SCRATCH / f"{name}.json").read_bytes()),
            }
        )
    for name in ["primary-source", "dataset", "cross-mech", "structured-adapter"]:
        check = copy.deepcopy(old_checks[name])
        if name == "structured-adapter":
            check["summary"] = (
                "The optional runner is unavailable; inspected public catalog provides a bounded fallback without exact strain coverage or an expression-module query."
            )
        checks.append(check)
    doc["checks"] = checks
    doc["evidence"] = evidence
    assessments = {a["assessment_id"]: a for a in doc["assessments"]}
    for dimension in assessments["identity"]["dimensions"]:
        if dimension["name"] == "abundance_interpretation":
            dimension.update(
                value="Both partners are co-equal prominent members within the defined pair",
                definition="DOMINANT is ordinal record-relative prominence; source selection and phenotype support this characterization without a measured population fraction or percentage threshold.",
                evidence_ids=["abundance-scope", "schema", "record"],
            )
    assessments["taxonomy"][
        "details"
    ] = "Both DOMINANT labels are defensible as co-equal prominence within the defined pair, not a measured population fraction. The new selection snippet does not establish metabolite consumption and therefore does not repair CROSS_FEEDER. NO_GTDB_EQUIVALENT for the eukaryote and UNRESOLVED for the bacterial anchor preserve taxonomic limits; no new species assignment or GTDB re-grounding is claimed."
    assessments["taxonomy"]["evidence_ids"].append("abundance-scope")
    assessments["history"][
        "summary"
    ] = "Fresh source review confirms the cautious graph, recoverable supplement conditions and limited November 5 abundance history; the three original curation findings remain open."
    assessments["validation"][
        "summary"
    ] = "Eight focused/native checks pass; all five unique curated ID-label pairs and all 14 snippets verify. The two corpus network commands retain their unrelated baseline warning exits."
    doc["assessments"].append(
        {
            "assessment_id": "staleness-and-abundance-lineage",
            "area": "provenance",
            "topic": "Current-main changes and bounded abundance repair",
            "outcome": "supported",
            "summary": "The stale original input is replaced by a freshly inspected current record. The added ordinal abundance field and source-matching membership evidence are supported within the pair's scope; the narrow later abundance finding is already explicitly resolved.",
            "details": "This assessment confirms the bounded abundance resolution without creating a new terminal disposition or superseding grouped reviews. It preserves all three original unresolved findings and the explicit experimental boundary in discussions[1] (auxeno_pyridoxal_mediation). Future published evidence would need to distinguish endogenous necessity from supplementation sufficiency and direct transfer from correlated detection before those qualifications could change. No experiment is requested here.",
            "target_ids": [ID],
            "evidence_ids": [
                "current-delta",
                "abundance-scope",
                "abundance-lineage",
                "history",
                "supplementation",
            ],
        }
    )
    for finding in doc["findings"]:
        finding["previous_occurrences"] = [
            {
                "repository": doc["repository"],
                "review_id": old["review_id"],
                "finding_id": finding["finding_id"],
            }
        ]
    doc["limitations"][
        -1
    ] = "Optional kg-microbe-sources is unavailable in PATH and the two probed sibling checkouts. Public iModulonDB catalog inspection found no exact target strain or alga; other Pseudomonas species are not substitutes. No expression-module query, external recipe-body equivalence check or raw dataset reanalysis was performed."
    doc["limitations"] += [
        "The corpus network commands return the existing 44-warning baseline across 16 of 503 records. This is recorded as failed, not silently converted to a pass; the target-specific native audit returned no issues.",
        "DOMINANT is an ordinal record-relative characterization of the two defined partners, not a quantitative estimate of absolute counts, biomass, relative share or precursor community composition.",
    ]
    doc["notes"] += [
        "This is the author refresh, not independent adversarial approval. No canonical record, cache, history, schema or generated product was edited.",
        "The unresolved auxeno_pyridoxal_mediation discussion remains an explicit evidence boundary covered by the pyridoxal-grounding acceptance checks; no additional finding or experimental action is introduced.",
    ]
    doc["tags"].append("pr-2038-refresh")
    candidate = write("candidate.json", doc)
    result = run(
        "native-validate",
        ["uv", "run", "python", "scripts/record_review.py", "validate", str(candidate)],
    )
    assert result.returncode == 0, result.stdout.decode() + result.stderr.decode()
    print(
        json.dumps(
            {"candidate": str(candidate), "review_id": rid, "findings": len(doc["findings"])}
        )
    )


if __name__ == "__main__":
    main()
