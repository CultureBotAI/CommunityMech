"""Author the PR 2040 record 401 successor as JSON for native immutable saving."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import yaml
from pr2040_401_audit import OLD, ROOT, SCRATCH, TARGET, now, run, sha, write

ID = "CommunityMech:000401"


def main():
    initial = json.loads((SCRATCH / "inspection.json").read_text())
    for item in initial["source"]["inputs"]:
        assert sha((ROOT / item["path"]).read_bytes()) == item["sha256"], item["path"]
    paths = {item["path"] for item in initial["source"]["inputs"] if item["role"] != "target"}
    paths.update(str(p.relative_to(ROOT)) for p in SCRATCH.iterdir() if p.is_file())
    paths.update(str(p.relative_to(ROOT)) for p in (ROOT / "scripts/adhoc").glob("pr2040_401_*.py"))
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
    stamp = now()
    rid = (
        stamp[:19].replace("-", "").replace(":", "")
        + "Z-pr2040-bifidobacterium-faecalibacterium-successor"
    )
    doc.update(
        review_id=rid,
        title="Bifidobacterium–Faecalibacterium 2′-FL/FOS: current-main review successor",
        started_at=json.loads((SCRATCH / "inspect.json").read_text())["started_at"],
        finished_at=stamp,
        source=inspected["source"],
        targets=inspected["targets"],
    )
    doc["reviewer"] = {
        "identity": "codex",
        "kind": "agent",
        "independence": "unknown",
        "independence_basis": "Author refresh of a stale PR 2040 review. Historical Codex record creation and graph review exist. This pass does not claim independent adversarial approval.",
    }
    doc["summary"] = (
        "Current main adds DOMINANT to both members and one source-exact abundance quotation under B. bifidum. Fresh complete primary text, Figures 1–4, Supplementary S1 and culture/taxonomic authorities retain all three original findings: A2-165 species grounding (P2), unsupported DIET category (P2), and B. bifidum consumer role (P3). A new P3 asks for local Faecalibacterium abundance evidence and its FOS-only treatment qualifier. Both members can be prominent across different treatment arms; they are not simultaneously measured at 60% and 95%. Eight focused checks pass; corpus network checks retain 44 warnings across 16 of 503 records, with no target issues."
    )
    doc["scope"].update(
        description="Entire current target, two nodes, no downstream arrows, 32 snippets and four history sidecars. Fresh complete main XML, all four main figures, full one-page S1 PDF and pixels, current JCM/NCBI authority metadata and native checks were assessed. No raw-data, genome or statistical reanalysis.",
        selection="Refresh the only stale target in PR 2040 against current merged main. Exactly four parsed leaves were added: taxonomy[0].abundance_level, taxonomy[0].evidence[2], taxonomy[1].abundance_level and curation_history[3]. All three original findings were reassessed with stable issue keys and exact predecessor links.",
    )
    sources = {Path(x["path"]).name: x for x in json.loads((SCRATCH / "sources.json").read_text())}
    media = {x["name"]: x for x in json.loads((SCRATCH / "media-sources.json").read_text())}
    supplemental = json.loads((SCRATCH / "supplement-fallback.json").read_text())
    assert len(supplemental["extracted"]) == 1
    evidence = [
        copy.deepcopy(e)
        for e in old["evidence"]
        if not e["evidence_id"].startswith("check-") and e["evidence_id"] != "independent-source"
    ]
    ev = {e["evidence_id"]: e for e in evidence}
    for e in evidence:
        e["accessed_at"] = stamp
        e.pop("snapshot_sha256", None)
    for eid, filename in [
        ("pubmed", "publication.xml"),
        ("crossref", "crossref.json"),
        ("epmc", "epmc.json"),
    ]:
        ev[eid].update(
            snapshot_sha256=sources[filename]["sha256"],
            accessed_at=sources[filename]["accessed_at"],
        )
    for eid in ["methods", "peak", "transfer", "mono"]:
        ev[eid].update(
            snapshot_sha256=sources["primary.xml"]["sha256"],
            accessed_at=sources["primary.xml"]["accessed_at"],
        )
    ev["record"].update(
        locator="Whole current record: exact two-strain model, two nodes, no arrows and 32 evidence occurrences",
        snapshot_sha256=sha((ROOT / TARGET).read_bytes()),
    )
    for index in range(1, 5):
        row = media[f"microorganisms-14-01812-f00{index}.webp"]
        ev[f"figure-{index}"].update(
            locator=f"Fresh primary Figure {index}: all panels and caption visually inspected",
            snapshot_sha256=row["sha256"],
            accessed_at=row["accessed_at"],
        )
    ev["figure-4"][
        "summary"
    ] = "Relative qPCR composition changes across 24-hour substrate arms. Faecalibacterium is approximately 60% in FOS-only medium and Bifidobacterium reaches approximately 95% at high 2′-FL. These are different conditions, not simultaneous shares, viable-cell counts or donor-resolved flux."
    ev["supplement"].update(
        locator="Full one-page Supplementary S1 PDF extracted from the public Europe PMC supplementaryFiles package, rendered and inspected",
        summary="S1 shows estimated genome-copy profiles: Faecalibacterium falls at high 2′-FL and Bifidobacterium rises, with distinct absolute and relative trajectories. These estimates do not measure viable cells, acetate transfer or the causal basis of the butyrate peak. Direct PMC returned an HTML shell and the guessed publisher PDF route failed; the authentic public supplementary package supplied the verified PDF.",
        snapshot_sha256=supplemental["extracted"][0]["sha256"],
        accessed_at=supplemental["retrieval"]["accessed_at"],
    )
    ev["catalogues"].update(
        locator="Fresh JCM31915 and JCM1254 HTML and parsed text",
        summary="Current JCM identifies A2-165/JCM31915/DSM17677 as F. duncaniae and links NCBITaxon:411483. JCM1254/DSM20082 remains B. bifidum and links strain NCBITaxon:398514. Catalogue-maintenance recipes and genomes are not the focal experiment's conditions or newly generated datasets.",
        snapshot_sha256=sources["jcm31915.html"]["sha256"],
    )
    ev["strain-authority"].update(
        reference="Fresh NCBI Taxonomy efetch: 411483, 853, 398514 and 1681",
        locator="ncbi-taxonomy.xml and ncbi-authorities.json: names, ranks and parent chains",
        summary="Current NCBI independently resolves species 411483 as F. duncaniae and species 853 as the distinct F. prausnitzii. Strain 398514 is B. bifidum JCM 1254 under species 1681. Correct lexical labels on the target do not fix its A2-165 species mismatch.",
        snapshot_sha256=sources["ncbi-taxonomy.xml"]["sha256"],
    )
    ev["ontology"].update(
        locator="All eight unique current curated term pairs replayed through local OAK authorities",
        snapshot_sha256=sha((SCRATCH / "ontology-authorities.json").read_bytes()),
    )
    ev["schema"][
        "summary"
    ] = "DIET means direct interspecies electron transfer. CROSS_FEEDER denotes consumption of other taxa's metabolites. DOMINANT is ordinal prominence, with no fixed percentage cutoff; it does not mean both members have the same population share across every treatment."
    ev["snippets"].update(
        locator="Fresh snippet-replay.json: all 32 current occurrences",
        summary="All 32 snippets, including the new two-sentence abundance passage, match fresh full primary XML and the committed cache after NFKC/whitespace normalization. Main-text comparison is not an abstract-only check.",
        snapshot_sha256=sha((SCRATCH / "snippet-replay.json").read_bytes()),
    )
    ev["history"].update(
        locator="Four target sidecars, embedded entries, exact 000401 graph-decision row and fresh issue receipts",
        summary="The graph-only decision's frozen record hash matches the original review input. Issues 991–994 and 1254 are CLOSED; 1256 remains OPEN for the separate A2-165 taxonomy follow-up. Issue 2113 is CLOSED and both abundance fields are now present. Its new quotation covers both taxa, but the parsed delta adds it only to taxonomy[0]; this placement fact does not by itself make the history's general coverage wording false.",
        snapshot_sha256=sha((SCRATCH / "semantic-diff.json").read_bytes()),
    )
    ev["resources"].update(
        locator="Fresh primary Data Availability Statement; JCM source-strain catalogues; current resource fields",
        summary="The article's Data Availability points to article/SI and further inquiry without a study archive accession. Existing PMID and DOI resolve. Catalogue genome links are distinct identity resources and were not fetched or reanalyzed; no dataset-omission defect is inferred.",
        snapshot_sha256=sources["primary.xml"]["sha256"],
    )
    ev["native-target"].update(
        locator="Fresh target-network.json and current two-node/evidence inventory",
        summary="Native target audit returns no issues. Two nodes contain six evidence items with no downstream arrows; community-level participants and directed pair endpoints match current taxonomy identifiers. This structural consistency does not establish correct current strain grounding or scientific mechanism.",
        snapshot_sha256=sha((SCRATCH / "target-network.json").read_bytes()),
    )
    ev["source-scope"].update(
        locator="Fresh source/media receipts, complete XML, four main figure images and supplementary fallback receipt",
        summary="The author inspected the entire scientific main text, all four main figures and full Supplementary S1. Current source bytes are preserved separately in scratch; no raw-data or genome reanalysis and no independent-approval claim are made.",
        snapshot_sha256=sha((SCRATCH / "supplement-fallback.json").read_bytes()),
    )
    ev["search"].update(
        locator="Fresh ignored-inclusive exact record ID/slug, PMID and JCM1254/JCM31915/A2-165 query",
        summary="The bounded search found the primary cache, four histories and graph decisions. It produced no exact strain hit in kb/taxa; other source-paper matches are leads rather than automatically equivalent strain evidence.",
        search_scope="rg --no-ignore --hidden over references_cache, history, reports/causal_graph_review/decisions and kb/taxa; includes ignored files, with no machine-wide absence assertion.",
        snapshot_sha256=sha((SCRATCH / "local-search.stdout.txt").read_bytes()),
    )
    ev["adapter"].update(
        locator="Fresh adapter-discovery.json and public iModulonDB catalog",
        summary="No optional runner was found in PATH or either exact probed sibling checkout. The fresh public catalog has no Bifidobacterium or Faecalibacterium dataset entry; no target strain/expression-module query was available. Absence from this catalog is not negative biological evidence.",
        search_scope="PATH plus two explicit sibling paths, including ignored files, followed by the inspected public organism/dataset catalog.",
        snapshot_sha256=sources["imodulon-catalog.json"]["sha256"],
    )
    evidence.extend(
        [
            {
                "evidence_id": "current-delta",
                "kind": "record_content",
                "reference": TARGET,
                "locator": "semantic-diff.json: frozen original target versus current merged main",
                "summary": "Two DOMINANT fields, one abundance quotation under taxonomy[0], and curation_history[3] are new. No original taxonomy-grounding, category or consumer-role finding was repaired by these additions.",
                "support": "supports",
                "accessed_at": stamp,
                "snapshot_sha256": sha((SCRATCH / "semantic-diff.json").read_bytes()),
            },
            {
                "evidence_id": "abundance-scope",
                "kind": "primary_source",
                "reference": "PMID:42655156",
                "locator": "Methods 2.2–2.3, Results 3.4, Figure 4 and Supplementary S1",
                "summary": "Both strains are material contributors to the model and alternate in relative prominence across substrate arms. Approximately 60% Faecalibacterium applies to FOS-only culture; approximately 95% Bifidobacterium applies to 2′-FL-rich culture. Taxonomy[0]'s new quote states both observations; taxonomy[1] still has only identity and failure-to-grow-on-2′-FL snippets, which do not locally substantiate its abundance annotation.",
                "support": "supports",
                "accessed_at": stamp,
                "snapshot_sha256": sources["primary.xml"]["sha256"],
            },
            {
                "evidence_id": "abundance-lineage",
                "kind": "prior_review",
                "reference": "reviews/structured/20261104T203000Z-c6s5-remediation-verification/review.yaml",
                "locator": "c6s4-000401-bifido-faecali-abundance-levels and its two exact Stage 4 predecessor occurrences; fresh issue 2113",
                "summary": "The later review resolves the narrow missing-field finding and both fields are now present. This successor confirms that bounded resolution and records exact evidence placement without superseding the existing disposition. The new local-evidence concern has a distinct issue key; unrelated findings and the other issue-2113 records are not reassessed.",
                "support": "supports",
                "accessed_at": stamp,
                "snapshot_sha256": sha((SCRATCH / "lineage.json").read_bytes()),
            },
        ]
    )
    checks = []
    old_checks = {c["check_id"]: c for c in old["checks"]}
    for name in [
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
    ]:
        receipt = json.loads((SCRATCH / f"{name}.json").read_text())
        network = name in {"audit-network", "check-network-quality"}
        summary = (
            "Fresh corpus command retains baseline exit 1: 44 warnings across 16 of 503 records; target-specific native audit is empty."
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
                    "Full-corpus warning exit preserved, not converted into a target pass."
                    if network
                    else "Fresh focused target/history check, except read-only corpus cache-name preflight; exact runtime environment is recorded in the pinned receipt."
                ),
            }
        )
        evidence.append(
            {
                "evidence_id": "check-" + name,
                "kind": "validation",
                "reference": receipt["command"],
                "locator": f".temp/pr2040/401/{name}.json; {receipt['started_at']} to {receipt['finished_at']}",
                "summary": summary,
                "support": "supports",
                "accessed_at": receipt["finished_at"],
                "snapshot_sha256": sha((SCRATCH / f"{name}.json").read_bytes()),
            }
        )
    for name in ["source-identity", "scientific-source", "cross-mech", "structured-adapter"]:
        check = copy.deepcopy(old_checks[name])
        if name == "scientific-source":
            check["evidence_ids"] = ["source-scope", "supplement", "abundance-scope"]
            check["summary"] = (
                "Fresh complete main text, all four figures and full one-page S1 were inspected; numerical, treatment and mechanism scopes remain distinct."
            )
        elif name == "structured-adapter":
            check["summary"] = (
                "Optional runner unavailable in the bounded discovery; fresh public catalog contains no applicable organism entry."
            )
        checks.append(check)
    doc.update(checks=checks, evidence=evidence)
    assessments = {a["assessment_id"]: a for a in doc["assessments"]}
    assessments["identity"]["dimensions"].append(
        {
            "name": "abundance_interpretation",
            "value": "Ordinal prominence across distinct substrate arms",
            "definition": "The two DOMINANT fields describe important members across this defined pair's treatment series. The approximately 60% and 95% qPCR observations belong to different substrate ratios and do not establish simultaneous dominance, viable counts, equal starting cells or persistent in-vivo prevalence.",
            "evidence_ids": ["abundance-scope", "figure-4", "supplement", "schema"],
        }
    )
    assessments["taxon-faecalibacterium"][
        "details"
    ] += " Its new DOMINANT field is defensible as prominence in this model across treatment conditions, but its own evidence list does not contain the FOS-only relative-abundance support; add that local evidence and condition qualifier without changing the source's literal legacy species name."
    assessments["taxon-faecalibacterium"]["evidence_ids"].append("abundance-scope")
    assessments["provenance"].update(
        summary="All 32 snippets and four sidecars preserve source provenance; current abundance fields resolve the narrow omission while their evidence placement needs one local refinement.",
        details="Issues 991–994 and 1254 are CLOSED and their graph/volume/evidence repairs remain present; 1256 is OPEN for taxonomy. Issue 2113 is CLOSED and both abundance fields now exist. The one new quotation covers both organisms but resides only under taxonomy[0]. This observation does not declare history false or reopen the resolved missing-field finding. Publication resources resolve; catalogue genome links remain separate from focal-study data.",
    )
    assessments["validation"][
        "summary"
    ] = "Eight focused/native checks pass, all eight encoded term labels and all 32 snippets match. Fresh NCBI/JCM checks expose the persistent strain-species mismatch beyond lexical validation. Corpus network commands retain their 44-warning exits, with no target issues."
    for metric in assessments["metrics"]["metrics"]:
        if metric["name"] == "P3":
            metric["value"] = 2
        elif metric["name"] == "validation_quality":
            metric["definition"] = (
                "clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1) + 15 if native COMPLETE, 0, 100). P1 = 0, P2 = 2, P3 = 2, P4 = 0; 6 evidence items / 2 nodes = 3 gives 20 evidence bonus. Native target audit is empty. 100 - 20 - 4 + 20 + 15 = 111 before capping; high mechanical quality does not erase semantic findings."
            )
    doc["assessments"].append(
        {
            "assessment_id": "staleness-and-abundance-lineage",
            "area": "provenance",
            "topic": "Fresh input and bounded prior abundance resolution",
            "outcome": "concern",
            "summary": "Both previously missing abundance fields are present, but Faecalibacterium needs its own condition-scoped evidence.",
            "details": "The exact delta preserves all three original finding surfaces. The source's two-sentence passage covers both taxa but was added only to taxonomy[0]. The prior c6s5 resolution of missing fields remains intact; a distinct new concern addresses local attachment and interpretation, without claiming both organisms dominate every treatment. No other issue-2113 target or grouped disposition is superseded.",
            "target_ids": [ID],
            "evidence_ids": [
                "current-delta",
                "abundance-scope",
                "abundance-lineage",
                "history",
                "schema",
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
    doc["findings"].append(
        {
            "finding_id": "faecalibacterium-abundance-evidence-scope",
            "issue_key": "cm-000401-faecalibacterium-abundance-evidence-scope",
            "category": "evidence",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "P3 minor: the source supports prominence under a specific treatment, but the newly populated taxon annotation lacks its local supporting snippet and condition qualifier; the exact pair and source observation remain resolved.",
            "rule_id": "review-checklist.claim_evidence",
            "status": "open",
            "certainty": "confirmed",
            "title": "Attach treatment-scoped abundance support to the Faecalibacterium member",
            "description": "Taxonomy[1] now has abundance_level DOMINANT, but its own evidence list still contains only exact strain identity and failure to grow on 2′-FL alone. The new quotation under taxonomy[0] supplies the approximately 60% FOS-only Faecalibacterium observation as well as the approximately 95% 2′-FL-rich Bifidobacterium observation. Attach the relevant support locally and distinguish these treatment-dependent relative-qPCR observations from simultaneous dominance or viable abundance.",
            "target_ids": [ID],
            "field_paths": ["taxonomy[1].abundance_level", "taxonomy[1].evidence"],
            "evidence_ids": ["abundance-scope", "figure-4", "methods", "schema", "current-delta"],
            "owner_paths": [
                {"repository": doc["repository"], "path": TARGET, "role": "canonical_record"}
            ],
        }
    )
    doc["actions"].append(
        {
            "action_id": "attach-faecalibacterium-abundance-evidence",
            "description": "Add the local source-exact Faecalibacterium abundance support and treatment explanation during separately authorized record curation.",
            "finding_ids": ["faecalibacterium-abundance-evidence-scope"],
            "target_ids": [ID],
            "owner_paths": [
                {"repository": doc["repository"], "path": TARGET, "role": "canonical_record"}
            ],
            "acceptance_checks": [
                "Attach the exact Results 3.4 FOS-only abundance passage to taxonomy[1] with PMID 42655156 and IN_VITRO provenance, preserving literal legacy source naming.",
                "Explain that approximately 60% refers to the 24-hour FOS-only relative-qPCR result, while approximately 95% Bifidobacterium belongs to 2′-FL-rich arms. Do not imply simultaneous percentages, viable counts or equal starting cell counts.",
                "Retain DOMINANT only with the record-relative and treatment scope made explicit; do not invent a numerical enum cutoff or change other source-supported fields to force consistency.",
                "Keep the separate A2-165 nomenclature, DIET-category and Bifidobacterium consumer-role findings open until independently corrected; preserve the qualified graph and unresolved pH/substrate/flux discussion.",
                "Append normal curation history without rewriting old entries, then run schema, strict, term, reference, history and generated-document checks. No historical correction is requested solely for the shared quotation's placement.",
            ],
        }
    )
    doc["limitations"].extend(
        [
            "Both DOMINANT values are ordinal prominence across the substrate series. Different treatment arms produce the approximately 60% and 95% relative-qPCR observations; neither the percentages nor S1 copy estimates measure viable abundance or persistence.",
            "Direct PMC supplement retrieval returned an HTML preparation page and the guessed publisher PDF route failed. The public Europe PMC supplementaryFiles package supplied the authentic PDF, which was extracted and inspected without access-control bypass or paid retrieval.",
            "The corpus network commands retain baseline exit 1 with 44 warnings across 16 of 503 records, recorded as failed. The target-specific native audit is empty; other records are outside this review.",
        ]
    )
    doc["notes"] = [
        "Author refresh only; no independent approval claim and no canonical record, cache, history, schema or generated-product edits.",
        "Initial repository inputs were hashed before judgment and rechecked before final inspection. All three original unresolved findings retain stable keys and exact previous_occurrences.",
        "The narrow c6s5 missing-field resolution remains intact. One new quotation covers both organisms but appears only in taxonomy[0]; no false-history finding is inferred from that placement.",
        "The existing bifido_faecali_2fl_fos_flux_unresolved discussion remains a source boundary covered by the preserve-qualified-model action. No experiment, paid research or author contact is requested.",
        "Native quality is capped at 100 from 111; completeness remains 75. Fifteen quoted words from the focal article are retained from the predecessor, with other source descriptions paraphrased.",
    ]
    doc["tags"].append("pr-2040-refresh")
    candidate = write("candidate.json", doc)
    result = run(
        "native-validate",
        ["uv", "run", "python", "scripts/record_review.py", "validate", str(candidate)],
    )
    assert result.returncode == 0, result.stdout.decode() + result.stderr.decode()
    print(
        json.dumps(
            {"review_id": rid, "candidate": str(candidate), "findings": len(doc["findings"])}
        )
    )


if __name__ == "__main__":
    main()
