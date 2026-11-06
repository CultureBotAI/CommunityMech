"""Author a current-main 347 successor as JSON for the immutable native saver."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import yaml
from pr2039_347_audit import OLD, ROOT, SCRATCH, TARGET, now, run, sha, write

ID = "CommunityMech:000347"
HISTORY = (
    "history/records/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom/"
    "2026-10-21T190000Z-claude-2049.yaml"
)


def main():
    initial = json.loads((SCRATCH / "inspection.json").read_text())
    # The audit helper gained source-retrieval/replay phases after its initial inspection.
    # All original scientific/context inputs must still match; freeze the read final helper below.
    for item in initial["source"]["inputs"]:
        if item["path"] != "scripts/adhoc/pr2039_347_audit.py":
            assert sha((ROOT / item["path"]).read_bytes()) == item["sha256"], item["path"]
    old = yaml.safe_load((ROOT / OLD).read_text())
    record = yaml.safe_load((ROOT / TARGET).read_text())
    target_network = json.loads((SCRATCH / "target-network.json").read_text())
    terms = json.loads((SCRATCH / "ontology-authorities.json").read_text())
    snippets = json.loads((SCRATCH / "snippet-replay.json").read_text())
    assert target_network == []
    assert len(terms) == 4 and all(t["matches"] for t in terms)
    assert len(snippets) == 10 and sum(s["article_or_abstract"] for s in snippets) == 5
    assert len(record["ecological_interactions"]) == 3
    assert sum(len(n.get("evidence", [])) for n in record["ecological_interactions"]) == 4
    assert not any(n.get("downstream") for n in record["ecological_interactions"])
    assert all(
        (SCRATCH / f"PS-82-8758-s00{i}.docx").read_bytes().lstrip().startswith(b"<html>")
        for i in [1, 2, 3]
    )
    run(
        "reusable-isolate-search",
        [
            "rg",
            "--no-ignore",
            "--hidden",
            "-n",
            "RW5|RW8|OQ996945|OQ996934",
            "kb/taxa",
            "data/isolates",
        ],
    )
    write(
        "author-source-assessment.json",
        {
            "assessed_at": now(),
            "main": "Entire scientific main article, all figure captions, supplement inventory and data statement read; Figs. 4-7 pixels inspected. Shared public HTML retrieval was completed no later than 2026-11-06T02:42:17.671292Z; this author independently read the bytes and claims no independent-review approval.",
            "main_sha256": sha((SCRATCH / "primary.html").read_bytes()),
            "source_limits": "Own initial PMC route and all three DOCX routes returned HTML challenges. EPMC full XML failed; NCBI PMC XML is explicitly abstract-only; BioC response has no article. No supplementary contents, raw reads or archive sample inventory certified.",
            "snippets": "Five of ten occurrences match normalized main/abstract text. Two source figure-accession labels were verified visually in Fig. 4b. Three HT = RW5, RW8 equations are curator shorthand, not verbatim source text. All ten are present in the committed cache; that does not resolve source-exactness or treatment attribution.",
            "figures": "Fig.4 verifies RW5/OQ996945 and RW8/OQ996934 labels and inhibition; Fig.5 separates CK and FO, preventing an inferred height denominator; Fig.6 supports HT host physiology; Fig.7c/d has C2/FO axes only. No bar-derived exact percentages or gene-isoform direction inferred.",
            "new_history_defect": "The target's newest sidecar names 000448, Bursaphelenchus and pine wilt, contradicting its 347 target path and actual Fusarium/Pinus endpoint-removal delta. New append-only clarification is needed, not editing this sidecar.",
            "catalog": "Public iModulonDB datasets JSON contains no Pinus, B. siamensis or B. vallismortis dataset. No strain/module query applies; Bacillus subtilis cannot substitute. Optional runner absent only from checked PATH and two conventional local locations.",
            "lineage": "All five original single-target findings retained open. Stage4 grouped external-endpoint lineage already has stage5 resolution; only the 347 portion was reassessed here, without superseding grouped findings or dropping their other targets.",
            "metrics": {
                "completeness": 65,
                "P1": 0,
                "P2": 2,
                "P3": 4,
                "P4": 0,
                "node_evidence": 4,
                "nodes": 3,
                "native_network": "COMPLETE",
                "quality": 100,
            },
        },
    )
    paths = {x["path"] for x in initial["source"]["inputs"] if x["role"] != "target"}
    paths.update(str(p.relative_to(ROOT)) for p in SCRATCH.iterdir() if p.is_file())
    paths.update(
        [
            "scripts/adhoc/pr2039_347_review.py",
            ".temp/pr2039/adversarial/fresh-html-receipts.json",
        ]
    )
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
    timestamp = now()
    doc = copy.deepcopy(old)
    doc.update(
        review_id=timestamp[:19].replace("-", "").replace(":", "")
        + "Z-pr2039-masson-pine-ht-successor",
        title="Masson pine HT Bacillus SynCom: current-main review successor",
        started_at=json.loads((SCRATCH / "inspect.json").read_text())["started_at"],
        finished_at=timestamp,
        source=inspected["source"],
        targets=inspected["targets"],
    )
    doc["reviewer"] = {
        "identity": "codex",
        "kind": "agent",
        "independence": "unknown",
        "independence_basis": "Author refresh of stale PR 2039 review; historical Codex curation exists. Public main-source bytes were shared by a separate reviewer and independently read by this author. This author pass claims no independent adversarial approval.",
    }
    doc["summary"] = (
        "Current main removes three external pathogen/host target_taxon slots and records that change. All five original scientific findings remain open: two major treatment/comparator conflicts and three minor cultivation, alias/resource and local-evidence gaps. A new minor finding identifies unrelated organism/record claims in the newest history sidecar. Eight focused checks pass and the target network has no issues. Two corpus network commands retain exit 1 for 44 warnings across 16 of 503 records. No canonical record or historical review was changed."
    )
    doc["scope"].update(
        description="Entire current target, both taxa, all three community-level nodes, zero arrows, ten evidence occurrences, one discussion and three history sidecars. Fresh main scientific text, all captions, Figs.4-7 pixels and bounded accession metadata reviewed. Supplement contents and raw data are not certified.",
        selection="Refresh stale CommunityMech:000347 in PR 2039 against merged main. Parsed comparison finds six changed paths: three removed external targets, two host-specific description additions and one inline history entry. Every original finding is reassessed with its exact predecessor; related grouped reviews are considered only for the current 347 representation.",
    )
    evidence = [
        copy.deepcopy(e)
        for e in old["evidence"]
        if not e["evidence_id"].startswith("check-")
        and e["evidence_id"] not in ["epmc", "independent-source"]
    ]
    by_id = {e["evidence_id"]: e for e in evidence}
    for e in evidence:
        e["accessed_at"] = timestamp
        e.pop("snapshot_sha256", None)
        e.pop("quote", None)
    primary_ids = [
        "pmc-main",
        "membership",
        "isolate-activity",
        "outcomes",
        "genes",
        "cultivation",
        "transcriptome",
    ]
    for eid in primary_ids:
        by_id[eid]["snapshot_sha256"] = sha((SCRATCH / "primary.html").read_bytes())
    for eid, filename in [
        ("pubmed", "publication.xml"),
        ("crossref", "crossref.json"),
        ("figure4", "figure-4.jpg"),
        ("figure5", "figure-5.jpg"),
        ("figure7", "figure-7.jpg"),
        ("physiology", "figure-6.jpg"),
        ("ontology", "ontology-authorities.json"),
        ("snippets", "snippet-replay.json"),
        ("native-target", "target-network.json"),
        ("source-scope", "author-source-assessment.json"),
        ("adapter", "imodulon-catalog.json"),
    ]:
        by_id[eid]["snapshot_sha256"] = sha((SCRATCH / filename).read_bytes())
    by_id["record"]["snapshot_sha256"] = sha((ROOT / TARGET).read_bytes())
    by_id["pmc-main"][
        "summary"
    ] = "Complete main scientific article, captions, supplement inventory and data statement inspected from shared fresh public PMC HTML. Retrieval was completed no later than 2026-11-06T02:42:17.671292Z; the author independently assessed the source and claims no separate approval."
    by_id["ontology"].update(
        locator="Four current unique canonical pairs, verified by local OAK adapters",
        summary="Both Bacillus species, ENVO rhizosphere and GO defense response to fungus labels match. Removed external host/pathogen slots are no longer among the current encoded ontology values.",
    )
    by_id["schema"][
        "summary"
    ] = "PATHOGEN_ANTAGONIST fits both source-assayed strains; DOMINANT permits coequal ordinal prominence within the defined formulation. COMMUNITY_LEVEL descriptions retain the external host/pathogen context; no removed nonmember target_taxon is restored."
    by_id["snippets"].update(
        locator=".temp/pr2039/347/snippet-replay.json plus Fig.4b image inspection",
        summary="Five occurrences match normalized fresh main/abstract text; two accession labels are visually exact Fig.4b transcriptions; three repeated composition equations remain nonverbatim shorthand. All ten exist in the committed cache, whose validator pass cannot certify original source precision.",
    )
    by_id["datasets"].update(
        locator="Fresh OQ996945.embl, OQ996934.embl and bioproject.xml frozen in source.inputs",
        snapshot_sha256=sha((SCRATCH / "bioproject.xml").read_bytes()),
    )
    by_id["history"].update(
        reference=HISTORY,
        locator="Three sidecars, inline curation_history[1], six-path semantic diff and historical decision row",
        summary="The current inline history accurately records removal of external Fusarium/Pinus targets. The matching sidecar incorrectly describes record 000448 and nematode CounterSelection; append-only clarification is required. Earlier causal arrows remain absent and the historical decision row retains its narrower source scope.",
        snapshot_sha256=sha((ROOT / HISTORY).read_bytes()),
    )
    by_id["search"].update(
        reference="references_cache, history, reports/causal_graph_review/decisions, kb/taxa and data/isolates",
        locator="Ignored-inclusive exact identifier/slug search and RW5/RW8/OQ accession search",
        summary="The bounded local lookup resolves current cache, history and decision context; no RW5/RW8/OQ996945/OQ996934 match was found in kb/taxa or data/isolates. This is not a machine-wide alias absence claim.",
        search_scope="rg --no-ignore --hidden covered the named local roots; exact-name/accession lookup cannot exclude unrecognized aliases.",
    )
    by_id["adapter"].update(
        reference="https://imodulondb.org/api/datasets",
        locator="Fresh full public catalog and adapter-discovery.json",
        summary="No Pinus, B. siamensis or B. vallismortis dataset is listed; B. subtilis is not a valid substitute. No covered strain/module search applies and absence supplies no negative biological evidence. The optional runner is unavailable in the bounded checked environment.",
        search_scope="Console PATH and two conventional claw checkout paths; full public dataset catalog inspected, not a machine-wide runner search.",
    )
    by_id["native-target"].update(
        locator=".temp/pr2039/347/target-network.json and author-source-assessment.json",
        summary="Target network audit returns an empty issue list after main removed external target slots. The metric's native network condition is COMPLETE; there are four evidence items across three nodes and no arrows.",
    )
    by_id["source-scope"].update(
        locator="author-source-assessment.json and exact fresh retrieval receipts",
        summary="Entire main text and Figs.4-7 inspected. Own EPMC XML retrieval failed, own initial PMC route and three DOCX routes yielded HTML challenges, NCBI XML exposes only an abstract, and BioC gives no article. Shared complete public HTML supplies main text; supplement contents remain unread.",
    )
    evidence.append(
        {
            "evidence_id": "main-delta",
            "kind": "record_content",
            "reference": ".temp/pr2039/347/semantic-diff.json",
            "locator": "Six differences against the original frozen input; exact grouped review lineage in lineage.json",
            "summary": "Only the endpoint representation and inline history changed. Stage4 grouped endpoint findings already have a stage5 resolution; this single-target successor observes 347's repaired representation without superseding those multi-target findings.",
            "support": "supports",
            "accessed_at": timestamp,
            "snapshot_sha256": sha((SCRATCH / "semantic-diff.json").read_bytes()),
        }
    )
    checks = []
    for check in old["checks"]:
        c = copy.deepcopy(check)
        cid = c["check_id"]
        if (SCRATCH / f"{cid}.json").exists():
            receipt = json.loads((SCRATCH / f"{cid}.json").read_text())
            c.update(
                command=receipt["command"],
                exit_code=receipt["exit_code"],
                expected_exit_code=0,
                status="passed" if receipt["exit_code"] == 0 else "failed",
            )
            c["scope_note"] = (
                "Actual current-worktree execution; exact safe runtime environment and times retained in the frozen receipt."
            )
            if cid in ["audit-network", "check-network-quality"]:
                c["summary"] = (
                    "Actual corpus command exits 1: 44 warnings, zero errors across 16 of 503 records. The current target has zero native network issues; this preserves the existing corpus warning baseline."
                )
            evidence.append(
                {
                    "evidence_id": "check-" + cid,
                    "kind": "validation",
                    "reference": receipt["command"],
                    "locator": f".temp/pr2039/347/{cid}.json; execution {receipt['started_at']} to {receipt['finished_at']}",
                    "summary": c["summary"],
                    "support": "supports",
                    "accessed_at": receipt["finished_at"],
                    "snapshot_sha256": sha((SCRATCH / f"{cid}.json").read_bytes()),
                }
            )
        if cid == "publication-identity":
            c["evidence_ids"] = ["pubmed", "crossref", "pmc-main", "figure4"]
        if cid == "full-primary-source":
            c["evidence_ids"] = [
                "pmc-main",
                "figure4",
                "figure5",
                "figure7",
                "physiology",
                "source-scope",
            ]
        if cid == "structured-adapter":
            c["summary"] = (
                "Optional runner unavailable within checked PATH/checkout scope. Public catalog fallback inspected; no covered target dataset, so no strain/module query applies."
            )
        checks.append(c)
    doc["checks"] = checks
    doc["evidence"] = evidence
    assessments = {a["assessment_id"]: a for a in doc["assessments"]}
    for a in doc["assessments"]:
        a["evidence_ids"] = [e for e in a["evidence_ids"] if e != "independent-source"]
    for dimension in assessments["identity"]["dimensions"]:
        if dimension["name"] == "grounding_status":
            dimension["value"] = (
                "Four current matched ontology pairs; strain-level archive aliases unresolved"
            )
    assessments["node-0"][
        "details"
    ] += " The external pathogen is retained in prose, not as a restored nonmember target_taxon slot."
    assessments["node-1"][
        "details"
    ] += " Pinus context remains in prose after main's endpoint-slot repair."
    assessments["validation"].update(
        summary="Eight focused checks pass and this target has zero network issues; cache validation does not resolve the scientific attribution/provenance findings.",
        details="Do not add Fusarium or Pinus to HT membership or restore removed target_taxon slots. Preserve COMMUNITY_LEVEL scope and use only legitimate community participants. Required corpus commands retain baseline warning exits, not a false green.",
    )
    assessments["provenance"][
        "details"
    ] += " The new sidecar's unrelated 000448/nematode narrative requires append-only correction; do not rewrite it or the historical source-access discussion."
    assessments["metrics"][
        "summary"
    ] = "Completeness remains 65. Quality is capped at 100 after the network repair: two P2 and four P3 findings, four evidence items across three nodes, and the COMPLETE bonus. This score is not a scientific pass."
    for metric in assessments["metrics"]["metrics"]:
        if metric["name"] == "P3":
            metric["value"] = 4
        if metric["name"] == "validation_quality":
            metric["value"] = 100
            metric["definition"] = (
                "clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1) + 15 if native COMPLETE, 0, 100). P1=0, P2=2, P3=4, P4=0; 4 items / 3 nodes. Current target has zero network issues. clamp(100 - 20 - 8 + 13.3333333 + 15) = 100."
            )
    doc["assessments"].append(
        {
            "assessment_id": "main-refresh",
            "area": "provenance",
            "topic": "Current endpoint repair and bounded grouped-review lineage",
            "outcome": "concern",
            "summary": "The record's three external-target removals are preserved; the associated sidecar describes a different record and biological system.",
            "target_ids": [ID],
            "evidence_ids": ["main-delta", "history", "record", "native-target"],
            "details": "The stage4 grouped external-host/pathogen finding also covers 364 and 373 and has a stage5 resolution. This review reassesses only 347 and creates no terminal disposition or successor for that grouped key. All five original single-target scientific findings remain open; the unrelated sidecar narrative is a new bounded provenance finding.",
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
        if finding["finding_id"] == "strain-alias-and-resource":
            finding["description"] = finding["description"].replace(
                "current records name H4/TK2", "current sequence-archive records name H4/TK2"
            )
    history_owner = [
        {
            "repository": doc["repository"],
            "path": str(Path(HISTORY).parent),
            "role": "append_only_history",
        }
    ]
    doc["findings"].append(
        {
            "finding_id": "history-identity",
            "issue_key": "cm-000347-history-identity",
            "category": "provenance",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "P3 minor: a misleading history narrative impairs traceability but does not change the current record identity or supported HT composition.",
            "rule_id": "AGENTS.append-only-history",
            "status": "open",
            "certainty": "confirmed",
            "title": "Clarify the unrelated organism and record claims in the endpoint-repair history",
            "description": "The 2026-10-21T190000Z-claude-2049 sidecar targets this 347 path but its event names CommunityMech:000448 and Bursaphelenchus xylophilus pine-wilt CounterSelection. The actual current record and six-path delta remove external Fusarium/Pinus target_taxon slots and contain no such nematode interaction. The inline history accurately describes that removal. Append a correction identifying the erroneous sidecar; never rewrite its historical bytes.",
            "target_ids": [ID],
            "field_paths": [HISTORY + "#events[0].summary", HISTORY + "#events[0].details"],
            "evidence_ids": ["history", "main-delta", "record"],
            "owner_paths": history_owner,
        }
    )
    for action in doc["actions"]:
        if action["action_id"] == "validate-curation":
            action["acceptance_checks"] = [
                "Keep HT distinct from C2 and the conditioning fungus; retain zero causal arrows unless new source-specific mediation evidence justifies them.",
                "Append a current source-scope assessment and remaining supplement/alias uncertainties without rewriting old history or silently changing the historical discussion's original scope.",
                "Run schema, strict, term, reference, history and network checks. Preserve host/pathogen prose context and the repaired COMMUNITY_LEVEL representation; never restore removed nonmember target_taxon slots or add them to the HT roster.",
                "No canonical record, cache, history event or prior review bundle is changed by this review-only successor.",
            ]
    doc["actions"].append(
        {
            "action_id": "clarify-history-identity",
            "description": "Append a correction of the endpoint-repair sidecar's record/organism narrative.",
            "finding_ids": ["history-identity"],
            "target_ids": [ID],
            "owner_paths": history_owner,
            "acceptance_checks": [
                "Add a new history event naming CommunityMech:000347 and the exact erroneous sidecar, explaining that the actual repair removed external Fusarium/Pinus endpoint slots.",
                "Do not rewrite old history bytes, invent nematode interactions or alter correct current endpoint scope.",
                "Validate the new history entry and verify that its narrative matches the actual recorded diff.",
            ],
        }
    )
    doc["limitations"] = [
        "Full main text and all captions were read; Figs.4-7 pixels were inspected. Other figure pixels and raw data were not reanalyzed. Public primary HTML was shared by a separate reviewer; authorship here remains distinct from independent approval.",
        "Three supplementary DOCX routes returned HTML challenges. Main HTML lists Methods S1-S3 and Tables S1-S6, but their contents remain unread. Table S1 cannot resolve RW5/H4 or RW8/TK2 aliases here. No access control was bypassed.",
        "The source conflicts on HT disease reduction, outcome timing, named-gene treatment scope and CAT1 direction. No exact effects were recalculated from bars and no convenient source version was silently selected.",
        "The abstract associates 153 isolates with Trichoderma treatment; main Results describes isolation across four treatments. HT membership is explicit, but exact original isolate-treatment provenance remains unresolved without the supplementary table.",
        "Both OQ accessions are partial 16S records, not strain genomes. PRJNA1166410 resolves as a host transcriptome project; twelve samples and treatment assignments are source statements, not independently audited repository counts.",
        "Host physiology, transcript enrichment, gene direction and pathway necessity are distinct. No metabolite exchange, selective pathway intervention or protection-to-expression edge is inferred. Existing mediation discussion remains an evidence-watch outcome, not a demand for new experiments.",
        "Historical GTDB metrics were not recomputed. Optional structured adapter availability was checked only in PATH and two conventional checkout paths; the full public iModulonDB dataset catalog has no matching target dataset.",
        "Both required corpus network commands completed with their existing exit 1: 44 warnings, zero errors across 16/503 records. The target itself has no network findings. The quality-score cap does not erase six open curation findings.",
    ]
    doc["notes"] = [
        "Initial native inspect preceded assessment; all immutable scientific inputs were rechecked. The audit helper was extended for fresh retrieval/replay and formatted before final inspection; both final helper files and all source/receipt bytes are frozen.",
        "Original single-target issue keys and exact previous occurrences are preserved. No terminal disposition is created for any grouped review, and no other grouped target is silently dropped.",
        "Canonical records, caches, histories and generated products remain unchanged. JSON candidates are passed to the native validate/save workflow; saved YAML and Markdown are never hand-edited.",
    ]
    doc["related_reviews"] = [
        {
            "repository": doc["repository"],
            "review_id": item["review_id"],
            "relationship": "Original single-target review or bounded context for the previously resolved grouped external-endpoint lineage; no grouped supersession.",
        }
        for item in json.loads((SCRATCH / "lineage.json").read_text())
    ]
    candidate = write("candidate.json", doc)
    for name, args in [
        (
            "validate-candidate",
            ["uv", "run", "python", "scripts/record_review.py", "validate", str(candidate)],
        ),
        (
            "save-candidate",
            [
                "uv",
                "run",
                "python",
                "scripts/record_review.py",
                "save",
                "--content",
                str(candidate),
            ],
        ),
    ]:
        result = run(name, args)
        assert result.returncode == 0, result.stderr.decode() + result.stdout.decode()
    print(doc["review_id"])


if __name__ == "__main__":
    main()
