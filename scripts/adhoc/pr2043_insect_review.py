"""Build one immutable JSON successor per insect; native saver owns YAML writes."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

import yaml
from pr2043_insect_audit import RECORDS, ROOT, SCRATCH, now, run, sha, write


def build(key):
    row = RECORDS[key]
    target = row["target_path"]
    tid = row["target_id"]
    folder, shared = SCRATCH / key, SCRATCH / "shared"
    output = folder / "draft-final"
    old = yaml.safe_load((ROOT / row["review"]).read_text())
    initial = json.loads((folder / "inspection.json").read_text())
    for entry in initial["source"]["inputs"]:
        assert sha((ROOT / entry["path"]).read_bytes()) == entry["sha256"], entry["path"]
    paths = {x["path"] for x in initial["source"]["inputs"] if x["role"] != "target"}
    paths.update(
        str(p.relative_to(ROOT))
        for d in [folder, shared]
        for p in d.iterdir()
        if p.is_file()
        and not p.name.startswith(
            ("candidate", "inspect-final", "inspection-final", "native-validate")
        )
    )
    paths.update(
        str(p.relative_to(ROOT)) for p in (ROOT / "scripts/adhoc").glob("pr2043_insect_*.py")
    )
    paths.add("reports/causal_graph_review/decisions/20261025-c2s5-review-remediation.yaml")
    args = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(folder / "targets.json"),
    ]
    for path in sorted(paths):
        args += ["--input", path]
    result = run(output, "inspect-final", args)
    assert result.returncode == 0, result.stderr.decode()
    inspected = json.loads(result.stdout)
    write(output / "inspection-final.json", inspected)
    stamp = now()
    insect = {"000006": "spittlebug", "000007": "sharpshooter", "000008": "cicada"}[key]
    rid = stamp[:19].replace("-", "").replace(":", "") + f"Z-pr2043-{insect}-successor"
    model = "MODEL180625000" + str(int(key) - 3)
    history = "history/records/" + Path(target).stem + "/2026-10-25T151200Z-antigravity-2072.yaml"
    doc = copy.deepcopy(old)
    doc.update(
        review_id=rid,
        title=f"{insect.capitalize()} BioModels record: current-main review successor",
        started_at=json.loads((folder / "inspect.json").read_text())["started_at"],
        finished_at=stamp,
        source=inspected["source"],
        targets=inspected["targets"],
    )
    doc["reviewer"] = {
        "identity": "codex",
        "kind": "agent",
        "independence": "unknown",
        "independence_basis": "Author refresh of a stale PR 2043 review. Earlier Codex graph curation exists; this pass does not claim independent adversarial approval.",
    }
    doc["summary"] = (
        "Current main adds a supported broad animal-associated environment and matching embedded history. Fresh primary main text, figures, supplementary methods, focal tables and deposited model metadata retain all four original findings: host membership and unsupported ecological STABLE (P2), structured computational provenance and publication-as-dataset organization (P3). A new P3 identifies an unrelated PMID in the external environment-history sidecar. The environment addition itself remains valid. Eight focused checks pass; corpus network checks report 44 warnings across 16 of 508 records, with no target-native issues. No simulation was rerun."
    )
    doc["scope"].update(
        description="Entire current target and its two history sidecars; three qualified interaction nodes, zero downstream arrows and all nine source snippets. Fresh complete primary scientific main, all seven main and three supplementary figures, full Text S1, focal S1e/f/g and S1h/i rows, S5o run bounds, S6 model headers, BioModels metadata/SBML and focal BioProject metadata. Supplement workbook extraction is broader than the human-assessed slices; no exhaustive reaction-list or executable-model audit.",
        selection=f"Refresh stale {tid} in PR 2043 against merged main. Environment and one embedded history event are the only canonical delta; every original finding is reassessed with its stable key and exact predecessor.",
    )

    evidence = [
        copy.deepcopy(e)
        for e in old["evidence"]
        if not e["evidence_id"].startswith("check-")
        and e["evidence_id"] not in {"independent-source", "source-reuse"}
    ]
    ev = {e["evidence_id"]: e for e in evidence}
    for e in evidence:
        e["accessed_at"] = stamp
        e.pop("snapshot_sha256", None)

    def pin(eid, path, receipt=None):
        ev[eid]["snapshot_sha256"] = sha(path.read_bytes())
        if receipt:
            ev[eid]["accessed_at"] = json.loads(receipt.read_text())["accessed_at"]

    for eid, filename in [
        ("pubmed", "pubmed.xml"),
        ("crossref", "crossref.json"),
        ("epmc", "epmc.json"),
    ]:
        pin(eid, shared / filename, shared / (filename + ".receipt.json"))
    for eid in [
        "sulcia",
        "sodalis" if key == "000006" else "baumannia" if key == "000007" else "hodgkinia",
        "reciprocal",
        "methods",
        "inference",
    ]:
        pin(eid, shared / "primary.xml", shared / "primary.xml.receipt.json")
        ev[eid]["locator"] = ev[eid]["locator"].replace("Reused direct XML", "Fresh XML")
    pin("record", ROOT / target)
    pin("schema", ROOT / "src/communitymech/schema/communitymech.yaml")
    pin("supplement", shared / "supplement.zip", shared / "supplement.zip.receipt.json")
    ev["supplement"][
        "locator"
    ] += "; fresh EPMC supplementaryFiles archive, Text S1 and all three SI figures; table-audit.json preserves extraction with focal human-reading scope stated separately"
    for eid in ["ontology", "snippets", "native-target"]:
        pin(eid, folder / "replay-qualified.json")
        ev[eid]["locator"] = str((folder / "replay-qualified.json").relative_to(ROOT))
    ev["ontology"][
        "summary"
    ] = "All seven unique curated term pairs across eleven occurrences match local OAK labels; fresh NCBI independently confirms all focal taxon names and OLS confirms ENVO:01001002. Label validity does not establish microbial membership."
    ev["snippets"][
        "summary"
    ] = "All nine excerpts match fresh primary sources after NFKC/whitespace normalization: eight interaction snippets occur in the full article XML and the resource quotation is the exact punctuated PubMed title. The initial article-only replay correctly misses that PubMed-specific terminal period; the qualified replay preserves source boundaries."
    ev["native-target"][
        "summary"
    ] = "Target-native audit returns no issues for the three-node, zero-arrow graph; eight interaction evidence occurrences are counted separately from one resource-title citation. Structural consistency does not certify equilibrium or membership."
    ev["history"].update(
        reference=history,
        locator="events[0].details, compared with current environment_term.notes and embedded curation_history[1]",
        summary="The new external history sidecar wrongly cites PMID:29944653 for the insect environment addition. That PMID resolves to an unrelated human urinary-symptom questionnaire study. The current record correctly cites insect modeling paper PMID:30254121; the source-backed ENVO addition and grouped missing-field resolution remain valid.",
    )
    pin("history", ROOT / history)
    pin("resources", shared / (model + ".json"), shared / (model + ".json.receipt.json"))
    ev["resources"][
        "locator"
    ] = f"Fresh {model} metadata and file list; verified SBML payload, focal BioProject XML, immutable author tree/payload at bb20c83c112331442b19a7b5f16f6cd6389221b4"
    pin("model-boundary", shared / "model-audit.json")
    ev["model-boundary"]["locator"] = (
        str((shared / "model-audit.json").relative_to(ROOT))
        + ": focal model identity, archive digest, compartments and selected exchange bounds"
    )
    ev["source-scope"].update(
        locator="Fresh shared retrieval receipts and archive-inventory.json; article Sections 1–4, all main/SI figures, Text S1 and focal table/model slices",
        summary="The author read fresh primary main text and the stated asset slices. Supplement bytes and model identity were independently retrieved in this author pass; computational outputs were not recomputed, raw sequences were not inspected, and no independent approval is claimed.",
    )
    pin("source-scope", shared / "archive-inventory.json")
    ev["search"].update(
        locator=str((folder / "local-search.stdout.txt").relative_to(ROOT)),
        summary="Ignored-inclusive exact ID/slug and source-PMID search found source caches, target sidecars and relevant graph-decision files. No focal match was returned from kb/taxa; this bounded result does not establish machine-wide absence.",
        search_scope="rg --no-ignore --hidden over references_cache, history, reports/causal_graph_review/decisions and kb/taxa, including ignored files.",
    )
    pin("search", folder / "local-search.stdout.txt")
    ev["adapter"].update(
        reference="https://imodulondb.org/api/datasets",
        locator="Fresh public organism/dataset catalog",
        summary="The structured iModulonDB catalog has no Sulcia/Karelsulcia, Sodalis, Baumannia/Palibaumannia, Hodgkinia or focal insect entry. E. coli is a reconstruction reference, not the focal symbiosis; its expression modules do not establish insect-host mechanisms. No matching module query is applicable and catalog absence is not negative biological evidence.",
        search_scope="All organism entries in the fresh public structured catalog; no machine-wide adapter-availability assertion.",
    )
    pin("adapter", shared / "imodulon-catalog.json", shared / "imodulon-catalog.json.receipt.json")
    evidence.extend(
        [
            {
                "evidence_id": "current-delta",
                "kind": "record_content",
                "reference": target,
                "locator": str((folder / "target-diff.stdout.txt").relative_to(ROOT)),
                "summary": "Only environment_term and the corresponding embedded history event were added; the four previously flagged fields remain unchanged.",
                "support": "supports",
                "accessed_at": stamp,
                "snapshot_sha256": sha((folder / "target-diff.stdout.txt").read_bytes()),
            },
            {
                "evidence_id": "environment-authority",
                "kind": "authority",
                "reference": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001002",
                "locator": "Fresh ENVO:01001002 label and definition plus primary Introduction/Methods and Figure 1",
                "summary": "ENVO:01001002 is animal-associated environment, an environmental system determined by an animal. The broad term fits the modeled intracellular insect bacteriome; the preferred term supplies host detail without claiming a more specific ENVO identity.",
                "support": "supports",
                "accessed_at": json.loads((shared / "envo.json.receipt.json").read_text())[
                    "accessed_at"
                ],
                "snapshot_sha256": sha((shared / "envo.json").read_bytes()),
            },
            {
                "evidence_id": "history-wrong-source",
                "kind": "database",
                "reference": "PMID:29944653",
                "locator": "Fresh PubMed ArticleTitle and Abstract, compared with external history events[0].details",
                "summary": "This identifier denotes a clinical comparison of nocturia and prostate-symptom questionnaires in men, not insect endosymbiont modeling. PMID:30254121 supplies the supported focal environment context.",
                "support": "refutes",
                "accessed_at": json.loads(
                    (shared / "history-pmid-29944653.xml.receipt.json").read_text()
                )["accessed_at"],
                "snapshot_sha256": sha((shared / "history-pmid-29944653.xml").read_bytes()),
            },
            {
                "evidence_id": "environment-lineage",
                "kind": "prior_review",
                "reference": "reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml",
                "locator": "c2s4-biomodels-missing-environment-term, including its two exact c2s4 grouped predecessors",
                "summary": "The resolved grouped finding covers 000006, 000007, 000008 and 000013. This single-target successor confirms only its own source-supported field addition; it does not supersede the four-target disposition or reassess the other members. A separate history-PMID defect does not undo field presence.",
                "support": "context_only",
                "accessed_at": stamp,
                "snapshot_sha256": sha((folder / "lineage.json").read_bytes()),
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
        network = name in {"audit-network", "check-network-quality"}
        receipt_path = (shared if network else folder) / (name + ".json")
        receipt = json.loads(receipt_path.read_text())
        assert receipt["exit_code"] == (1 if network else 0)
        c = copy.deepcopy(old_checks[name])
        c.update(
            command=receipt["command"],
            exit_code=receipt["exit_code"],
            status="failed" if network else "passed",
            summary=(
                "Fresh corpus check reports 44 baseline warnings across 16 of 508 records; the focal native audit is empty."
                if network
                else c["summary"]
            ),
            evidence_ids=["check-" + name],
        )
        c["scope_note"] = (
            "Actual local execution with pinned canary Python/UV environment; corpus network diagnostics remain failed and are not represented as a target pass."
            if network
            else "Actual focused target/history execution, except corpus cache-name preflight; structural success does not establish scientific support."
        )
        checks.append(c)
        evidence.append(
            {
                "evidence_id": "check-" + name,
                "kind": "validation",
                "reference": receipt["command"],
                "locator": str(receipt_path.relative_to(ROOT)),
                "summary": c["summary"],
                "support": "context_only" if network else "supports",
                "accessed_at": receipt["finished_at"],
                "snapshot_sha256": sha(receipt_path.read_bytes()),
            }
        )
    for name in ["source-identity", "scientific-source", "cross-mech"]:
        c = copy.deepcopy(old_checks[name])
        c.pop("command", None)
        c.pop("exit_code", None)
        c["evidence_ids"] = [
            e for e in c["evidence_ids"] if e not in {"independent-source", "source-reuse"}
        ]
        c["summary"] = (
            "Fresh public source identity, model metadata and declared scientific slices inspected by the author; no executable reproduction."
            if name != "cross-mech"
            else c["summary"]
        )
        checks.append(c)
    checks.append(
        {
            "check_id": "structured-adapter",
            "name": "Structured source catalog applicability",
            "status": "not_applicable",
            "required": False,
            "summary": "Fresh iModulonDB organism catalog has no focal partner or insect dataset; no target-module claim was inferred.",
            "target_ids": [tid],
            "evidence_ids": ["adapter"],
        }
    )
    doc["checks"], doc["evidence"] = checks, evidence
    for a in doc["assessments"]:
        if a["assessment_id"] == "identity":
            for dimension in a["dimensions"]:
                if dimension["name"] == "environment":
                    dimension.update(
                        value="ENVO:01001002 animal-associated environment; modeled intracellular bacteriome and external hemolymph",
                        definition="Fresh primary host/bacteriocyte context supports the broad canonical ENVO term, while the preferred term preserves the focal insect habitat.",
                        evidence_ids=["methods", "environment-authority"],
                    )
        if a["assessment_id"] == "provenance":
            a.update(
                outcome="concern",
                summary="Original graph qualifications and all nine source snippets remain supported, but the new external environment-history event cites an unrelated paper.",
                details="The MD cache remains labeled abstract_only despite appended main text; the TXT is abstract/bibliographic material. Fresh full XML and PubMed were independently matched. The external sidecar requires append-only correction; its historical bytes must not be rewritten. No current GitHub issue status is inferred from the predecessor.",
                evidence_ids=["snippets", "history", "history-wrong-source", "current-delta"],
            )
        if a["assessment_id"] == "metrics":
            for metric in a["metrics"]:
                if metric["name"] == "completeness":
                    metric.update(
                        value=80,
                        definition="min(100, 50 required metadata including roles + 5 environment + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets + 5 node metabolites). Current record: 50 + 5 + 0 + 10 + 5 + 0 + 5 + 5 = 80.",
                    )
                elif metric["name"] == "validation_quality":
                    metric.update(
                        value=100,
                        definition="clamp(100 - 50 P1 - 10 P2 - 2 P3 + 20 min(mean node evidence / 2, 1) + 15 if native COMPLETE, 0, 100). P1 = 0, P2 = 2, P3 = 3, P4 = 0; 8 evidence / 3 nodes gives 20 evidence bonus and 15 network bonus: 109 before capping. Scores are not scientific approval.",
                    )
                elif metric["name"] == "P3":
                    metric["value"] = 3
    doc["assessments"].append(
        {
            "assessment_id": "environment-refresh",
            "area": "grounding",
            "topic": "Current-main habitat addition and bounded prior disposition",
            "outcome": "supported",
            "summary": "The new broad ENVO term and focal insect note match primary host-associated modeling context; the earlier grouped missing-field resolution is preserved.",
            "details": "The environment is natural intracellular symbiosis represented computationally, not a wet-lab medium or evidence of ecological equilibrium. The single-target review does not retire a multi-target predecessor. Correcting the sidecar source attribution is separate from retaining this field.",
            "target_ids": [tid],
            "evidence_ids": [
                "current-delta",
                "environment-authority",
                "methods",
                "environment-lineage",
            ],
        }
    )
    for f in doc["findings"]:
        f["previous_occurrences"] = [
            {
                "repository": doc["repository"],
                "review_id": old["review_id"],
                "finding_id": f["finding_id"],
            }
        ]
    owner = [
        {
            "repository": doc["repository"],
            "path": "history/records/" + Path(target).stem,
            "role": "append_only_provenance",
        }
    ]
    doc["findings"].append(
        {
            "finding_id": "environment-history-source",
            "issue_key": f"cm-{key}-environment-history-source",
            "category": "provenance",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "P3 minor: an external provenance event cites an unrelated source, while record identity, supported environment grounding and the embedded citation remain correct.",
            "rule_id": "review-checklist.audit",
            "status": "open",
            "certainty": "confirmed",
            "title": "Append a correction for the environment-history source PMID",
            "description": f"{history}:events[0].details attributes the environment addition to PMID:29944653, an unrelated human clinical questionnaire study. The target environment_term.notes and actual insect model source use PMID:30254121. Preserve the original event and append a precise corrective provenance entry.",
            "target_ids": [tid],
            "field_paths": [history + ":events[0].details"],
            "evidence_ids": ["history", "history-wrong-source", "methods", "environment-authority"],
            "owner_paths": owner,
        }
    )
    doc["actions"].append(
        {
            "action_id": "correct-environment-history-source",
            "description": "During separately authorized curation, append a correction identifying the erroneous historical source citation.",
            "finding_ids": ["environment-history-source"],
            "target_ids": [tid],
            "owner_paths": owner,
            "acceptance_checks": [
                f"Create a new history entry for {tid} naming {history}:events[0].details, its incorrect PMID:29944653, and the supported replacement PMID:30254121.",
                "Preserve the original historical file byte-for-byte; explain that the canonical environment field and embedded citation were already supported and remain unchanged.",
                "Keep the resolved grouped missing-environment disposition intact and retain the four unrelated original findings until their separate curation is verified.",
                "Validate the new history entry, inspect the append-only diff and verify no unsupported ecological-state or host-membership promotion.",
            ],
        }
    )
    for a in doc["actions"]:
        if a["action_id"] == "preserve-model-graph":
            a["acceptance_checks"].append(
                "Keep insect_model_nitrogen_and_host_control as an explicit source-boundary discussion. Any future evidence update must distinguish measured transfer/regulation from model predictions; no new experiment, paid research or author contact is requested."
            )
    doc["limitations"] = [
        x
        for x in old["limitations"]
        if not any(
            s in x for s in ["new environment ontology", "Frozen 000006", "Failed publisher/bin"]
        )
    ]
    doc["limitations"].extend(
        [
            "Exact culture-collection strains, historical GTDB mapping statistics, replacement ecological-state classification and executable model equivalence were not established; no empirical host-control or dynamic-equilibrium assay is inferred.",
            "Supplementary human reading was limited to focal EAA outputs and exchange scope in S1e/f/g, S1h, nitrogen definitions/summaries in S1i, all S5o medium bounds, S6 component headers, Text S1 and all SI figures. Extracting every workbook cell is not an exhaustive scientific audit of those cells.",
            "Fresh corpus network checks return baseline exit 1 with 44 warnings across 16 of 508 records. The focal native audit is empty; unrelated records were not scientifically reviewed.",
        ]
    )
    if key == "000006":
        doc["limitations"].append(
            "S6a labels the Sodalis component iNA402 while main Methods/Text S1 call it iNA400. Preserve this source naming discrepancy when curating computational provenance; the integrated iNA761 identity remains verified."
        )
    doc["notes"] = [
        "Author refresh only; no canonical record, cache, history, schema or generated-product edit, no executable-model reproduction and no independent-approval claim.",
        "Initial input pins were captured before assessment and rechecked before final inspection. The four original open findings retain exact previous_occurrences; only the separate external-history source finding is new.",
        "The grouped c2s5 missing-environment resolution is contextual only. Its four-target scope is not superseded or narrowed by this one-target observation.",
        "Completeness rises from 75 to 80 because environment_term is present. Quality is capped at 100 from 109 and does not negate two major and three minor findings.",
        "The existing source-boundary discussion is covered by the preserve-model-graph acceptance checks; it is not a demand to perform experiments. Primary quoted excerpts remain the predecessor's short quotations.",
    ]
    doc["tags"].append("pr-2043-refresh")
    candidate = write(output / "candidate.json", doc)
    result = run(
        output,
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
    parser = argparse.ArgumentParser()
    parser.add_argument("record", choices=list(RECORDS))
    build(parser.parse_args().record)
