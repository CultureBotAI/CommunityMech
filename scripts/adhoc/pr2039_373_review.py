"""Build the immutable PR 2039 record 373 successor as JSON for the native saver."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import yaml
from pr2039_373_audit import OLD, ROOT, SCRATCH, TARGET, now, run, sha, write

ID = "CommunityMech:000373"
HISTORY = "history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-10-21T190000Z-claude-2049.yaml"


def main():
    initial = json.loads((SCRATCH / "inspection.json").read_text())
    for item in initial["source"]["inputs"]:
        assert sha((ROOT / item["path"]).read_bytes()) == item["sha256"], item["path"]
    paths = {item["path"] for item in initial["source"]["inputs"] if item["role"] != "target"}
    paths.update(
        str(p.relative_to(ROOT))
        for p in SCRATCH.iterdir()
        if p.is_file()
        and not p.name.startswith(
            ("inspect-final", "inspection-final", "candidate", "native-validate")
        )
    )
    paths.update(str(p.relative_to(ROOT)) for p in (ROOT / "scripts/adhoc").glob("pr2039_373_*.py"))
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
    result = run("inspect-final-v3", args)
    assert result.returncode == 0, result.stderr.decode()
    inspected = json.loads(result.stdout)
    write("inspection-final-v3.json", inspected)
    old = yaml.safe_load((ROOT / OLD).read_text())
    doc = copy.deepcopy(old)
    stamp = now()
    rid = stamp[:19].replace("-", "").replace(":", "") + "Z-pr2039-bacillus-tobacco-successor"
    doc.update(
        review_id=rid,
        title="Bacillus G12-Y4-X25 tobacco SynCom: current-main partial successor",
        started_at=json.loads((SCRATCH / "inspect.json").read_text())["started_at"],
        finished_at=stamp,
        source=inspected["source"],
        targets=inspected["targets"],
        completion="partial",
        scientific_review=False,
        verdict="needs_curation",
    )
    doc["reviewer"] = {
        "identity": "codex",
        "kind": "agent",
        "independence": "unknown",
        "independence_basis": "Author refresh of a stale PR 2039 review; prior Codex record creation and graph curation exist. This pass does not claim independent adversarial approval.",
    }
    doc["summary"] = (
        "Current main removes the two external tobacco target_taxon blocks while preserving host context in node descriptions. Fresh full main article and all 11 main figures support the five bounded nodes and all 18 exact snippets. Both original P3 findings remain open: local antagonist-role evidence and experiment-specific cultivation context. A new P3 finding identifies an incorrect October 21 history narrative. Supplementary figure pixels remain unavailable, so this successor is partial. Eight focused checks pass; corpus network commands retain 44 warnings across 16 of 503 records, with no issues for this target."
    )
    doc["scope"].update(
        description="Entire current three-strain target, all five community-level nodes and no arrows, 18 evidence occurrences, three history sidecars, complete primary main HTML and main Figures 1–11. Supplementary captions S1–S5 were read, but the DOCX download returned HTML and its figure pixels were not inspected. No raw sequence or statistical reanalysis.",
        selection="Refresh only stale CommunityMech:000373 in PR 2039. The parsed delta has five changed leaves: two tobacco target_taxon blocks removed, two descriptions given explicit tobacco names, and one embedded curation entry added. Every original finding was reassessed and retains its stable key and exact predecessor.",
    )
    sources = {Path(x["path"]).name: x for x in json.loads((SCRATCH / "sources.json").read_text())}
    evidence = [
        copy.deepcopy(e) for e in old["evidence"] if not e["evidence_id"].startswith("check-")
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
    ev["epmc"][
        "summary"
    ] = "Fresh Europe PMC metadata links PMID 42388034, DOI 10.1002/ps.71069 and PMC13569317. Its XML route did not yield the body; the separately retrieved public PMC HTML did."
    ev["record"].update(
        locator="Entire current record: three members, five nodes, no arrows and 18 snippets",
        snapshot_sha256=sha((ROOT / TARGET).read_bytes()),
    )
    ev["cache"].update(
        summary="The committed cache remains selected primary passages, not the complete article. All 18 snippets match both this cache and the independently retrieved complete PMC main HTML.",
        snapshot_sha256=sha((ROOT / "references_cache/PMID_42388034.txt").read_bytes()),
    )
    ev["access"].update(
        locator=".temp/pr2039/373/sources.json and media-sources.json with per-request receipts",
        summary="Fresh EPMC XML and publisher requests returned curl exit 56. PubMed, Crossref, EPMC metadata, PMC efetch, PMC HTML, BioC and catalog requests returned exit 0. Successful transport alone is not source sufficiency: the complete main HTML and 11 figure images were inspected, whereas the supplement response is a Preparing to download HTML page, not DOCX. No bypass or paid retrieval was used.",
        snapshot_sha256=sha((SCRATCH / "media-sources.json").read_bytes()),
    )
    ev["root-access"].update(
        reference="https://pmc.ncbi.nlm.nih.gov/articles/PMC13569317/",
        locator="Fresh author retrieval: complete Methods 2.1–2.8, Results 3.1–3.7, Discussion, main Figures 1–11 and supplementary captions S1–S5",
        summary="The original main-text access limitation is overcome. Supplementary captions are available in HTML; their DOCX and underlying supplementary pixels remain unverified. The author's own retrieval and source assessment are used here, not another agent's approval.",
        snapshot_sha256=sources["pmc.html"]["sha256"],
    )
    primary = {
        "members": (
            "Abstract and Methods 2.1",
            "G12 is the rhizosphere B. amyloliquefaciens isolate; Y4 and X25 are tobacco endophytes assigned to B. pumilus and B. velezensis. The source attributes prior F. oxysporum antagonism to G12 and P. nicotianae inhibition to Y4/X25. Identity/habitat snippets alone do not directly support the local role annotations.",
        ),
        "compatibility": (
            "Methods 2.2; Results 3.1; Figure 1 A–C; supplementary S1 caption",
            "All six directional plate-inhibition values are below 25%. Figure 1 confirms mild inhibition and aggregate co-culture growth without resolving each strain's survival or persistent coexistence. The record does not claim a specific resource-depletion mechanism.",
        ),
        "iaa": (
            "Methods 2.2; Results 3.1; Figure 1 D–E; Discussion",
            "Per-volume Salkowski colorimetry reports 11.57 +/- 0.24 mg/L in the SynCom, above each monoculture. This supports the qualified IAA-output node; it does not establish member-resolved exchange or IAA-mediated plant protection. The separate co-cultivation growth protocol is not automatically an IAA incubation protocol.",
        ),
        "glasshouse": (
            "Methods 2.4; Results 3.3; Figures 3–5; supplementary S2–S3 captions",
            "He Luo No. 1 tobacco receives preventive or curative treatment around a combined FO/PN challenge. Figure 4 shows disease indices 54.07 for pathogen control, 9.26 for preventive SynCom and 26.67 for curative SynCom. The record's preventive reduction and separate curative benefit are supported without assigning a specific hormonal mechanism.",
        ),
        "root-activity": (
            "Methods 2.5; Results 3.4; Figure 6",
            "The TTC/dehydrogenase assay and Figure 6 support higher root metabolic activity, with the text reporting 20.27–45.38% above preventive single-strain treatments. This is not direct biomass production or reciprocal microbial fitness. Root morphometry is a distinct endpoint.",
        ),
        "field": (
            "Methods 2.7–2.8; Results 3.6–3.7; Figures 9–11; Discussion",
            "The two yellow-soil Luoyang sites show natural-disease control and middle-leaf-based estimated yield, not whole-plot harvested yield. Figure 9 supports the bounded site outcomes. Figure 11 shows nonsignificant genus-level Bacillus and Fusarium shifts; these do not establish strain colonization or durable community stability.",
        ),
        "cultivation": (
            "Methods 2.1, 2.2, 2.4 and 2.7",
            "Fresh complete Methods verify 30 C/180 rpm preparation, distinct 25 C/180 rpm/48 h co-cultivation growth measurement, glasshouse 25 +/- 2 C with 12 h:12 h light/dark and 70–80% RH for 21 days, and 10 mL per-plant field irrigation twice seven days apart. These contexts must remain separate; a precise LB recipe is not specified.",
        ),
        "limits": (
            "Methods 2.6, 2.8; Results 3.5, 3.7; Figures 7–8, 10–11; Discussion",
            "Pooled root/stem/leaf transcriptomic and co-expression associations do not prove tissue-specific hormonal mechanisms. A single-site endpoint and nonsignificant genus changes do not establish inoculant persistence, niche differentiation or resilience. Figure 10(F) depicts lower bacterial richness in SC than LB despite prose saying higher; no directional richness claim is adopted and the target encodes none.",
        ),
    }
    for eid, (locator, summary) in primary.items():
        ev[eid].update(
            locator=locator, summary=summary, snapshot_sha256=sources["pmc.html"]["sha256"]
        )
    ev["ontology"].update(
        locator="Ten unique current NCBITaxon, ENVO, CHEBI and GO pairs",
        summary="All 10 canonical labels match local OAK authority values. Species terms preserve isolate context; broad defense/growth terms are bounded to observed plant endpoints. The removed tobacco target objects are not current ontology placements.",
        snapshot_sha256=sha((SCRATCH / "ontology-authorities.json").read_bytes()),
    )
    ev["schema"][
        "summary"
    ] = "COMPETITION permits reciprocal negative effects without requiring resource depletion. DOMINANT is ordinal prominence of the co-equal formulation members, not a measured field population fraction. Tobacco remains external host context in descriptions; it is not a microbial member."
    ev["snippets"].update(
        locator="primary-html-replay.json and snippet-replay.json: all 18 evidence occurrences",
        summary="All 18 snippets match the fresh main HTML and the selected committed cache after NFKC and whitespace normalization. None is an exact match to the differently worded fresh PubMed abstract; main-text matching now independently verifies the lexical spans.",
        snapshot_sha256=sha((SCRATCH / "primary-html-replay.json").read_bytes()),
    )
    ev["datasets"].update(
        reference="PMID:42388034",
        locator="Fresh PMC main article Data Availability Statement and Methods 2.6/2.8",
        summary="The current public article still states temporary sequencing-release restrictions and future deposition without a study accession. GCF_000715135.1 is a tobacco reference genome, not this study's deposited reads. No arbitrary accession or dataset-omission defect is inferred; no author contact or raw-data analysis was performed.",
        snapshot_sha256=sources["pmc.html"]["sha256"],
    )
    ev["history"].update(
        reference=HISTORY,
        locator="All three sidecars; exact 000373 row in 20261005-eleven-records-batch5.yaml; fresh issues 1248, 880 and 2049",
        summary="The historical graph decision's record hash matches the original review input and its non-graph exclusion remains explicit. Issues 1248 and 880 are CLOSED. The new October 21 sidecar is schema-valid but falsely describes 000449 and counter_selection/Ralstonia changes. The actual delta is tobacco-target removal. Closed issue 2049 also misidentifies the 000373 record/source and is context only, not scientific proof.",
        snapshot_sha256=sha((ROOT / HISTORY).read_bytes()),
    )
    ev["search"].update(
        locator="Fresh rg --no-ignore --hidden exact record ID, PMID, G12, Y4 and X25 query",
        summary="The ignored-inclusive bounded search located this target's cache, three history sidecars and graph decision material. It produced no exact isolate-authenticating kb/taxa hit; shared Bacillus species do not establish equivalent isolates. The query also contains an irrelevant prior-target alternative, which does not narrow its exact current-target alternatives.",
        search_scope="references_cache, history, reports/causal_graph_review/decisions and kb/taxa, including hidden and ignored files; no machine-wide absence claim.",
        snapshot_sha256=sha((SCRATCH / "local-search.stdout.txt").read_bytes()),
    )
    ev["adapter"].update(
        reference="Optional kg-microbe-sources and public iModulonDB catalog",
        locator="adapter-discovery.json and fresh imodulon-catalog.json",
        summary="No runner was found in PATH or either exact probed sibling checkout. The inspected public catalog includes B. subtilis but no exact G12/Y4/X25 target dataset; a different Bacillus species is not a substitute. No expression-module query was performed.",
        search_scope="PATH and two exact sibling paths including ignored files, then the public organism/dataset catalog; absence is not negative biological evidence.",
        snapshot_sha256=sources["imodulon-catalog.json"]["sha256"],
    )
    ev["native-target"].update(
        locator="Fresh NetworkIntegrityAuditor().audit_community(current target)",
        summary="The target audit returned an empty issue list after host-target removal. All five nodes use COMMUNITY_LEVEL scope for the three-member SynCom and contain one evidence item each; no explicit participating_taxa lists or downstream edges are encoded. Native structural completeness does not prove missing scientific mechanisms.",
        snapshot_sha256=sha((SCRATCH / "target-network.json").read_bytes()),
    )
    evidence.append(
        {
            "evidence_id": "current-delta",
            "kind": "record_content",
            "reference": TARGET,
            "locator": "semantic-diff.json; original frozen input versus current merged-main target",
            "summary": "Exactly five semantic leaves changed: curation_history[2] added, tobacco target_taxon removed from nodes 3 and 4, and explicit tobacco names added to those descriptions. The source scopes and two original finding surfaces remain unchanged.",
            "support": "supports",
            "accessed_at": stamp,
            "snapshot_sha256": sha((SCRATCH / "semantic-diff.json").read_bytes()),
        }
    )
    evidence.append(
        {
            "evidence_id": "host-lineage",
            "kind": "record_content",
            "reference": "reviews/structured/20261021T193000Z-stage5-remediation-verification/review.yaml",
            "locator": "stage4-external-host-pathogen-targets and exact Stage 4 predecessor rows; lineage.json",
            "summary": "The later grouped finding explicitly resolves the host-target outcome for 000347/000364/000373. This successor independently confirms only the 000373 tobacco-target cleanup. It neither reassesses the other targets nor supersedes the grouped disposition; the contradictory issue/history identity text is separately flagged.",
            "support": "context_only",
            "accessed_at": stamp,
            "snapshot_sha256": sha((SCRATCH / "lineage.json").read_bytes()),
        }
    )
    checks = []
    old_checks = {c["check_id"]: c for c in old["checks"]}
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
    for name in names:
        receipt = json.loads((SCRATCH / f"{name}.json").read_text())
        network = name in {"audit-network", "check-network-quality"}
        summary = (
            "Fresh corpus check retains exit 1: 44 warnings across 16 of 503 records, with zero target-specific issues."
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
                    "Corpus warning exit preserved, not relabeled as passed."
                    if network
                    else "Fresh focused target/history check, except read-only corpus cache-name preflight. Exact environment is in the pinned receipt; history syntax does not validate narrative truth."
                ),
            }
        )
        evidence.append(
            {
                "evidence_id": "check-" + name,
                "kind": "validation",
                "reference": receipt["command"],
                "locator": f".temp/pr2039/373/{name}.json; {receipt['started_at']} to {receipt['finished_at']}",
                "summary": summary,
                "support": "supports",
                "accessed_at": receipt["finished_at"],
                "snapshot_sha256": sha((SCRATCH / f"{name}.json").read_bytes()),
            }
        )
    for name in [
        "publication-identity",
        "full-primary-source",
        "source-data",
        "cross-mech",
        "structured-adapter",
    ]:
        check = copy.deepcopy(old_checks[name])
        if name == "publication-identity":
            check["summary"] = (
                "Fresh metadata, complete primary main HTML and all 18 snippets independently verify; all 11 main figures were visually reviewed."
            )
        elif name == "full-primary-source":
            check.update(
                name="Remaining supplementary figure assessment",
                summary="Complete main Methods, Results, Discussion and Figures 1–11 are now inspected. Supplementary S1–S5 captions are accessible, but the DOCX route returns HTML and its figure pixels remain unavailable.",
                scope_note="Required supplemental scope remains incomplete; main-text access is no longer the limitation.",
            )
        elif name == "structured-adapter":
            check["summary"] = (
                "Optional runner unavailable; fresh public catalog provides a bounded fallback without exact target dataset or strain-module coverage."
            )
        checks.append(check)
    doc.update(checks=checks, evidence=evidence)
    assessments = {a["assessment_id"]: a for a in doc["assessments"]}
    for d in assessments["identity"]["dimensions"]:
        if d["name"] == "grounding_status":
            d["value"] = "Ten canonical term pairs; historical GTDB blocks/statuses"
    assessments["node-0"][
        "details"
    ] = "Participants are G12, Y4 and X25, with each pair tested in both directions. Fresh Methods 2.2, Results 3.1 and Figure 1 corroborate mild reciprocal plate inhibition. This supports COMPETITION at assay scope, not resource depletion, reciprocal benefit or durable coexistence; supplementary plate photographs S1 remain uninspected."
    assessments["node-3"][
        "details"
    ] = "Direction is SynCom treatment under FO/PN stress to tobacco root TTC activity versus single-strain treatments. Tobacco is now explicitly named in the description and absent from target_taxon. This preserves external host scope without treating it as a missing microbial member or turning TTC activity into biomass growth."
    assessments["node-4"][
        "details"
    ] = "G12/Y4/X25 is applied twice to tobacco under natural co-occurring root-rot/black-shank pressure. Fresh Methods 2.7, Results 3.6 and Figure 9 preserve two-site disease and middle-leaf estimated-yield comparisons. Neither whole-plot harvested yield nor durable microbiome change is established. Tobacco remains host context in the description."
    assessments["cultivation"].update(
        summary="The correctly scoped 30 C preparation block omits separate co-cultivation growth, glasshouse and field conditions now independently verified in complete Methods.",
        details="Keep preparation, 25 C/48 h co-cultivation measurement, 21-day controlled plant experiment and repeated field root irrigation separate. The environmental factor duplicates assembly strategy. The source does not provide a unique LB formulation; supplement unavailability no longer prevents checking these main-text conditions.",
    )
    assessments["provenance"].update(
        outcome="concern",
        summary="Fresh complete main HTML supports every snippet, but the October 21 history narrative misidentifies the record and edit.",
        details="The committed cache is still selected text and is not overwritten. An append-only correction must reconcile the incorrect 000449/Ralstonia/counter_selection narrative with the actual 000373 tobacco-target cleanup. Closed issue 2049 also has unrelated record/source identities; its closure is not evidence of scientific correctness. Current public data restrictions remain explicit, with no invented study accession.",
    )
    assessments["validation"].update(
        topic="Native checks and remaining supplementary scope",
        summary="Eight focused/native checks pass; all 10 current term pairs and all 18 snippets verify. The target audit is clean. The corpus commands retain their 44-warning exits, and unavailable supplementary pixels keep completion partial.",
    )
    metrics = assessments["metrics"]
    metrics.update(
        summary="Completeness is 85 and capped validation quality is 100; source scope and open findings remain explicit.",
        topic="Native completeness and quality within partial supplementary coverage",
    )
    for metric in metrics["metrics"]:
        if metric["name"] == "validation_quality":
            metric["definition"] = (
                "clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1) + 15 if native COMPLETE, 0, 100). P1 = 0, P2 = 0, P3 = 3, P4 = 0; 5 items / 5 nodes = 1; native audit has no issues. 100 - 6 + 10 + 15 = 119 before capping. A clean structural score does not complete supplementary source assessment."
            )
        elif metric["name"] == "P3":
            metric["value"] = 3
    doc["assessments"].append(
        {
            "assessment_id": "staleness-and-host-lineage",
            "area": "provenance",
            "topic": "Current-main host cleanup and grouped-review boundary",
            "outcome": "supported",
            "summary": "Fresh inspection replaces the stale input and confirms only the bounded 000373 host-target cleanup.",
            "details": "Nodes 3 and 4 retain tobacco host context and source-backed outcomes without host membership. The Stage 5 grouped resolved finding is context; no same-key supersession or disposition is emitted for its other targets. Incorrect history/issue identities remain a separate provenance concern. Both original single-record findings remain open.",
            "target_ids": [ID],
            "evidence_ids": [
                "current-delta",
                "host-lineage",
                "native-target",
                "history",
                "root-activity",
                "field",
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
        if finding["finding_id"] == "cultivation-context":
            finding["description"] = (
                "The LB block captures 30 C preparation but omits the separate 25 C/48 h co-cultivation growth assay and controlled glasshouse/field settings. Fresh complete Methods independently verify these contexts; environmental_factors[0] repeats assembly design."
            )
    doc["findings"].append(
        {
            "finding_id": "history-edit-misattribution",
            "issue_key": "cm-000373-history-2049-edit-misattribution",
            "category": "provenance",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "P3 minor: a non-blocking history narrative falsely attributes identity and edits; current scientific record identity remains correct.",
            "rule_id": "review-checklist.provenance",
            "status": "open",
            "certainty": "confirmed",
            "title": "October 21 history misidentifies the record and the actual host-target edit",
            "description": "The 2026-10-21T190000Z-claude-2049 sidecar names CommunityMech:000449 and claims added Ralstonia/Phytophthora counter_selection entries. Current 000373 instead removes tobacco target_taxon from nodes 3 and 4 and retains host text. Issue 2049's body separately assigns 000373 to an unrelated Ralstonia-phage/Pseudomonas record and PMID. Neither historical narrative is reliable proof of this change.",
            "target_ids": [ID],
            "field_paths": [HISTORY + "#events[0].summary", HISTORY + "#events[0].details"],
            "evidence_ids": ["history", "current-delta", "host-lineage", "members"],
            "owner_paths": [
                {"repository": doc["repository"], "path": HISTORY, "role": "append_only_history"}
            ],
        }
    )
    for action in doc["actions"]:
        if action["action_id"] == "fix-cultivation-context":
            action["description"] = (
                "Use freshly verified complete Methods to represent the distinct cultivation and plant-assay settings without conflating preparation and outcome protocols."
            )
            action["acceptance_checks"][
                0
            ] = "Preserve the correctly scoped 30 C preparation block; the main-text numerical contexts have now been independently verified."
            action["acceptance_checks"][
                -1
            ] = "Attach exact main-article Methods evidence at each added context and run strict, term, reference and history checks plus regenerated-document checks after separately authorized curation."
        elif action["action_id"] == "complete-source-assessment":
            action["description"] = (
                "Complete the remaining supplementary S1–S5 figure assessment when publicly accessible, then save a new immutable review; full main Methods, Results and Figures 1–11 are already assessed here."
            )
            action["acceptance_checks"][
                0
            ] = "Inspect the actual supplementary plate photographs, disease/field images and pathway figure; captions alone are not the images. Retain this successor's bounded main-text and numeric verification."
    doc["actions"].append(
        {
            "action_id": "append-history-correction",
            "description": "In separately authorized provenance curation, append a correction identifying the erroneous sidecar and actual 000373 edit; record the linked issue-body mismatch without rewriting old history.",
            "finding_ids": ["history-edit-misattribution"],
            "target_ids": [ID],
            "owner_paths": [
                {
                    "repository": doc["repository"],
                    "path": "history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom",
                    "role": "append_only_history",
                }
            ],
            "acceptance_checks": [
                "Name the exact October 21 sidecar and its incorrect 000449/Ralstonia/counter_selection claims; establish 000373 identity using target content and PMID 42388034.",
                "Document removal of tobacco target_taxon from nodes 3 and 4 plus retained host descriptions; do not fabricate absent counter_selection or pathogen changes.",
                "Preserve all original history bytes and verify the new corrective history with native validation.",
                "Link a correction to the erroneous issue-body identity without treating issue closure as scientific evidence or changing grouped findings for unrelated targets.",
            ],
        }
    )
    doc["limitations"] = [
        "Supplementary S1–S5 captions are inspected, but the DOCX download returned an HTML preparation/verification page; supplementary images remain unavailable. Main article and all 11 main figures were retrieved and assessed. No access-control bypass or paid retrieval was used.",
        "The selected committed cache remains incomplete despite its full-text separator. All 18 current snippets now independently match the complete primary HTML; no cache content was changed.",
        "No raw RNA-seq, amplicon data, figure digitization or statistical reanalysis was performed. Sequencing release restrictions and future deposition remain in the current article; the tobacco reference genome is not a study accession.",
        "Equal formulation membership is not persistent field dominance. Salkowski output, pooled-tissue expression associations and nonsignificant genus shifts do not establish metabolite mediation, member fitness, persistence or resilience. The existing colonization/mechanism discussion remains an evidence boundary, not a request to conduct experiments.",
        "The source's Figure 10(F) richness direction conflicts with its prose. This refresh does not adopt a directional richness claim, and none is encoded in the target; no correction to source raw data is inferred.",
        "Historical GTDB mapping counts/release were not recomputed. Optional adapter discovery is bounded to PATH and two exact sibling locations; the public catalog has no exact target dataset and no strain-module query was performed.",
        "The corpus network commands retain 44 warnings across 16 of 503 records, recorded as failed checks. The current target has no native network issues; grouped dispositions for other records were not reassessed.",
    ]
    doc["notes"] = [
        "This is an author refresh, not independent approval. No canonical record, cache, history, schema or generated product was edited.",
        "Both original P3 issue keys and exact previous_occurrences remain open; the new history concern requires append-only follow-up outside this review-bundle PR.",
        "Direct excerpts retained from the original review total 15 words. Source snapshots and actual command receipts are pinned, and the initial repository input hashes were rechecked before final inspection.",
        "The original complete-source-assessment action is narrowed to still-uninspected supplementary material. The bounded host-target repair does not supersede the three-target Stage 4/5 finding lineage.",
    ]
    doc["tags"].append("pr-2039-refresh")
    update_field_scope(doc)
    candidate = write("candidate-v3.json", doc)
    result = run(
        "native-validate-v3",
        ["uv", "run", "python", "scripts/record_review.py", "validate", str(candidate)],
    )
    assert result.returncode == 0, result.stdout.decode() + result.stderr.decode()
    print(
        json.dumps(
            {"review_id": rid, "candidate": str(candidate), "findings": len(doc["findings"])}
        )
    )


def update_field_scope(doc):
    """Retain the newly visible distinction between field endpoint comparators."""
    doc["summary"] = (
        "Current main removes two external tobacco target_taxon blocks while preserving host descriptions. Fresh main text and all 11 main figures verify all 18 snippets but expose a P2 field-yield comparator overstatement. Both original P3 findings remain open: local role evidence and cultivation context. A new P3 finding identifies incorrect October 21 history. Supplementary pixels remain unavailable, so completion is partial. Eight focused checks pass; corpus network commands retain 44 warnings across 16 of 503 records, with no target issues."
    )
    ev = {e["evidence_id"]: e for e in doc["evidence"]}
    ev["field"][
        "summary"
    ] = "The two yellow-soil sites show natural-disease control and middle-leaf-based estimated yield. Results 3.6 gives yield increases against the control. Figure 9D shows only G12/Y4/X25/SC/LB yield arms, with SC versus X25 fresh-yield comparisons nonsignificant; commercial B. subtilis appears in disease-efficacy panel E. The Discussion makes a broader commercial-product yield claim, but the displayed yield evidence does not establish that comparator. Figure 11 genus shifts are nonsignificant and do not establish strain persistence."
    assessments = {a["assessment_id"]: a for a in doc["assessments"]}
    assessments["node-4"].update(
        outcome="concern",
        summary="Natural-disease and estimated-yield outcomes are supported, but the combined sentence overextends demonstrated yield comparators.",
        details="Results 3.6 gives numeric yield increases versus the control, and Figure 9D has no commercial-product yield arm. Figure 9E supports superior disease efficacy versus B. subtilis. Although the Discussion asserts broader yield superiority, the record should separate these endpoint/comparator scopes or explicitly attribute that unresolved assertion. Not every single-strain yield comparison is significant. Neither whole-plot harvested yield nor durable microbiome change is established.",
    )
    for metric in assessments["metrics"]["metrics"]:
        if metric["name"] == "P2":
            metric["value"] = 1
        elif metric["name"] == "validation_quality":
            metric["definition"] = (
                "clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1) + 15 if native COMPLETE, 0, 100). P1 = 0, P2 = 1, P3 = 3, P4 = 0; 5 items / 5 nodes = 1; native target audit is empty. 100 - 10 - 6 + 10 + 15 = 109 before capping. A clean structural score does not complete supplementary source assessment."
            )
    doc["findings"].append(
        {
            "finding_id": "field-yield-comparator",
            "issue_key": "cm-000373-field-yield-comparator",
            "category": "scope",
            "severity": "major",
            "native_severity": "P2",
            "normalization_reason": "P2 major: a combined endpoint sentence presents commercial-product estimated-yield superiority beyond displayed comparator evidence, conflating disease and yield scopes.",
            "rule_id": "review-checklist.claim_evidence",
            "status": "open",
            "certainty": "confirmed",
            "title": "Separate field disease-control and estimated-yield comparator scopes",
            "description": "Node 4 says estimated yield increased relative to both single-strain and commercial microbial treatments. Figure 9D presents only G12/Y4/X25/SC/LB yield arms, while Figure 9E supports the commercial B. subtilis disease-efficacy comparison. Results 3.6 assigns the 41.33% and 37.54% dry-yield increases to the control. The Discussion does assert broader commercial-product yield superiority, but the presented yield evidence does not establish it; SC versus X25 fresh-yield comparisons are also nonsignificant. The record should preserve demonstrated comparators or explicitly qualify the broader author assertion.",
            "target_ids": [ID],
            "field_paths": [
                "ecological_interactions[4].description",
                "ecological_interactions[4].evidence[0].explanation",
            ],
            "evidence_ids": ["field", "record", "root-access"],
            "owner_paths": [
                {"repository": doc["repository"], "path": TARGET, "role": "canonical_record"}
            ],
        }
    )
    doc["actions"].append(
        {
            "action_id": "bound-field-yield-comparators",
            "description": "Separate field disease-control comparators from middle-leaf estimated-yield comparisons in the node and its evidence explanation.",
            "finding_ids": ["field-yield-comparator"],
            "target_ids": [ID],
            "owner_paths": [
                {"repository": doc["repository"], "path": TARGET, "role": "canonical_record"}
            ],
            "acceptance_checks": [
                "Preserve two-site natural-disease scope and commercial-product disease-efficacy comparison supported by Figure 9E.",
                "State 41.33% and 37.54% dry-yield increases against the source control, preserving middle-leaf estimation and Figure 9D treatment arms.",
                "Do not assert significant superiority over every single-strain yield arm. Distinguish any broader Discussion assertion from demonstrated commercial-product yield data unless additional directly supporting primary evidence is verified.",
                "Attach endpoint-specific evidence, append history, and run reference, strict and generated-document checks after separately authorized curation.",
            ],
        }
    )


if __name__ == "__main__":
    main()
