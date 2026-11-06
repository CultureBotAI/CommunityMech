"""Build a bounded NCBI authority correction as JSON for the native saver.

No canonical record or historical review is written. The source response was
retrieved by the independent reviewer and read directly by this observation's
author; the roles and the narrow taxonomic scope remain explicit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

OUT = Path(".temp/pr2058/020-author")
SELF = Path("scripts/adhoc/pr2058_020_authority_observation.py")
OLD = Path("reviews/structured/20261022T012643Z-coscinodiscus-record-review/review.yaml")
TARGET = "CommunityMech:000020"
RECORD = Path("kb/communities/Coscinodiscus_Synthetic_Community.yaml")
AUTHORITY = Path(".temp/pr2058/independent-secondary/sources/ncbi-taxonomy.xml")
RETRIEVAL = Path(".temp/pr2058/independent-secondary/sources/fresh-authority-receipt.json")
SECONDARY = Path(".temp/pr2058/independent-secondary/independent-science-three-records.json")
ISSUE = Path(".temp/pr2058/020-author/issue2572-current.json")


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def prepare():
    paths = {
        SELF,
        OLD,
        RECORD,
        AUTHORITY,
        RETRIEVAL,
        SECONDARY,
        ISSUE,
        Path(".temp/pr2058/independent-third/issue2572.json"),
        Path("AGENTS.md"),
        Path(".claude/skills/review-yaml-record/SKILL.md"),
        Path(".claude/skills/curate-yaml-record/references/review-checklist.md"),
        Path(".claude/skills/review-communities/reference/metrics-and-reports.md"),
        Path("docs/record-reviews.md"),
        Path("docs/record-review-profile.md"),
        Path("conf/record_review.yaml"),
        Path("conf/reference_validator.yaml"),
        Path("schema/record_review.yaml"),
        Path("src/communitymech/schema/communitymech.yaml"),
        Path("src/communitymech/schema/history.yaml"),
        Path("src/communitymech/schema/mech_shared.yaml"),
        Path("src/communitymech/ontology_adapters.py"),
        Path("references_cache/PMID_36300970.md"),
        Path("scripts/record_review.py"),
        Path("scripts/adhoc/pr2058_294_refresh.py"),
        Path("justfile"),
        Path(".temp/pr2058/294-author/focused-checks.json"),
        Path(
            "reviews/structured/20261106T154646Z-corynebacterium-shewanella-current-main/review.yaml"
        ),
        Path(
            "reviews/structured/20261106T062035Z-pr2043-kefir-state-action-correction/review.yaml"
        ),
    }
    paths.update(Path("history/records/Coscinodiscus_Synthetic_Community").glob("*.yaml"))
    excluded = {
        "input-paths.json",
        "input-manifest.json",
        "final-inspection.json",
        "candidate.json",
        "native-save.stdout",
        "native-save.stderr",
    }
    paths.update(
        p
        for p in OUT.iterdir()
        if p.is_file() and p.name not in excluded and not p.name.startswith("post-save-")
    )
    paths.add(OUT / "input-paths.json")
    manifest = {
        "targets": [TARGET],
        "paths": sorted(str(p) for p in paths),
        "boundaries": [
            "Every concrete source, context, earlier inspection and check input used for this bounded author observation is pinned.",
            "The final native inspection defines the input hashes and cannot hash itself; candidate and post-save outputs are later outputs.",
            "The shared secondary science receipt is attributed context, not fresh author certification of its full-paper or SI work.",
            "Prior GTDB counts are retained as historical assertions from the old review; this observation performs no new crosswalk replay or reassignment.",
        ],
    }
    (OUT / "input-paths.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"inputs": len(paths), "manifest": str(OUT / "input-paths.json")}))


def build(inspection_path):
    old = yaml.safe_load(OLD.read_text())
    inspection = read(inspection_path)
    assert {i["path"] for i in inspection["source"]["inputs"]} == set(
        read(OUT / "input-paths.json")["paths"]
    )
    for item in inspection["source"]["inputs"]:
        assert digest(item["path"]) == item["sha256"], item["path"]
    assert len(old["findings"]) == 4 and len(old["actions"]) == 5
    assert all(f["status"] == "open" for f in old["findings"])
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    owner = inspection["targets"][0]["owner_paths"]
    evidence = []

    def ev(eid, kind, path, locator, summary):
        evidence.append(
            {
                "evidence_id": eid,
                "kind": kind,
                "reference": str(path),
                "locator": locator,
                "summary": summary,
                "support": "supports",
                "accessed_at": now,
                "snapshot_sha256": digest(path),
            }
        )

    ev(
        "authority",
        "authority",
        AUTHORITY,
        "TaxaSet/Taxon[TaxId=74032]: ScientificName, Rank, OtherNames/Synonym, AkaTaxIds",
        "The fresh NCBI response to a request including 1434019 returns genus 74032 Antarctobacter, Mameliella as a synonym, and AkaTaxIds 1434019. UpdateDate is not a merge-event date.",
    )
    ev(
        "retrieval",
        "validation",
        RETRIEVAL,
        "Entry for ncbi-taxonomy.xml, retrieved 2026-11-06T15:40:47.759488+00:00",
        "Independent reviewer retrieved the public NCBI bytes; this author directly read the relevant returned genus entry. Shared retrieval does not make this an independent author approval.",
    )
    ev(
        "record",
        "record_content",
        RECORD,
        "taxonomy[1].taxon_term and ecological_interactions[1,2,4].participating_taxa",
        "Four descriptors use NCBITaxon:1434019 / Mameliella. The source isolate alias CS4 remains distinct from current genus authority. No canonical bytes are changed.",
    )
    ev(
        "prior",
        "prior_review",
        OLD,
        "assessments[identity].details; assessments[grounding].summary; assessments[taxonomy].summary; findings and actions",
        "The original unqualified current-grounding approval needs this narrow correction. Its four open scientific finding heads and five actions are not superseded or reissued.",
    )
    ev(
        "checks",
        "validation",
        OUT / "focused-checks.json",
        "Eight fresh focused commands and their separately pinned stdout/stderr",
        "Seven checks pass. Explained-reference checking fails with the same three interaction snippet cache misses; a local term pass does not establish current live NCBI authority.",
    )
    ev(
        "secondary-context",
        "prior_review",
        SECONDARY,
        "scientific_assessments.000020; focused_checks; inspection_limits",
        "The separate independent reviewer reports main-text corroboration of the three cache-missed snippets and original scientific findings. This author observation does not repeat or certify that whole-paper/SI pass.",
    )
    ev(
        "issue",
        "record_content",
        ISSUE,
        "Issue #2572 body: stable key and five acceptance checks",
        "Current canonical follow-up acceptance preserves source alias, historical GTDB provenance and all existing scientific scopes. Its corrected single-ID URL/hash pair is separate from the author's independently paired combined-response XML/retrieval input; the earlier issue snapshot is retained only as historical context.",
    )
    checks = []
    for row in read(OUT / "focused-checks.json"):
        checks.append(
            {
                "check_id": row["label"],
                "name": row["label"],
                "status": "passed" if row["exit_code"] == 0 else "failed",
                "required": True,
                "summary": (
                    "Fresh exit 0."
                    if row["exit_code"] == 0
                    else "Fresh exit 1: three pre-existing article-cache snippet misses; no validator was weakened."
                ),
                "target_ids": [TARGET],
                "command": " ".join(row["command"]),
                "exit_code": row["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["checks"],
                "scope_note": "Current author run; these checks do not certify full source coverage or live authority labels.",
            }
        )
    checks.append(
        {
            "check_id": "fresh-authority-read",
            "name": "Direct read of fresh public NCBI genus response",
            "status": "passed",
            "required": True,
            "summary": "Returned TaxId 74032 is genus Antarctobacter, synonym Mameliella, with AkaTaxIds 1434019; all four exact record descriptor paths were enumerated.",
            "target_ids": [TARGET],
            "evidence_ids": ["authority", "retrieval", "record"],
        }
    )
    assessments = [
        {
            "assessment_id": "bounded-authority-correction",
            "area": "grounding",
            "topic": "Current accepted genus versus source alias and local historical snapshots",
            "outcome": "concern",
            "summary": "Current NCBI authority resolves the old Mameliella taxid to Antarctobacter 74032.",
            "target_ids": [TARGET],
            "evidence_ids": ["authority", "retrieval", "record", "prior", "checks"],
            "details": "Correct only the current-authority implication in 20261022T012643Z-coscinodiscus-record-review assessments identity, grounding and taxonomy: a local ontology-cache match is not a current NCBI accepted-name certificate. Retain the source designation Mameliella sp. CS4 explicitly. This genus-level relationship does not identify a species, a collection strain, a biological reassignment of the isolate, or the date of a taxonomic merge. The old g__Mameliella 3/3 result remains a historical crosswalk snapshot, not a mapping automatically transferable to 74032.",
            "dimensions": [
                {
                    "name": "authority_rank",
                    "value": "genus",
                    "definition": "Resolution supported by the returned NCBI entry; no species or strain inferred",
                    "evidence_ids": ["authority"],
                },
                {
                    "name": "source_alias",
                    "value": "Mameliella sp. CS4",
                    "definition": "Source designation to retain separately from current accepted genus",
                    "evidence_ids": ["record", "prior"],
                },
                {
                    "name": "review_scope",
                    "value": "authority/provenance only",
                    "definition": "No new full-paper, SI, mechanism, graph, abundance or cultivation reassessment",
                    "evidence_ids": ["prior", "secondary-context"],
                },
            ],
        },
        {
            "assessment_id": "unmodified-scientific-lineage",
            "area": "provenance",
            "topic": "Existing scientific findings and native metrics",
            "outcome": "unknown",
            "summary": "All four original finding heads and all five actions remain untouched.",
            "target_ids": [TARGET],
            "evidence_ids": ["prior", "secondary-context"],
            "details": "No previous_occurrences is emitted for cm-000020-cultivation, cm-000020-non-graph-scope, cm-000020-gtdb-provenance or cm-000020-resources. Their action acceptance, source-access limits, five-node/two-arrow qualifiers and historical completeness/validation-quality metrics remain in the original. Those whole-record scores are not recomputed or promoted by this bounded authority observation; literature and supplementary support are outside its scope.",
        },
        {
            "assessment_id": "current-validation-limits",
            "area": "provenance",
            "topic": "Actual checks and complete local input pins",
            "outcome": "concern",
            "summary": "Native deterministic checks retain the known reference-cache failure and current input attestation.",
            "target_ids": [TARGET],
            "evidence_ids": ["checks", "secondary-context", "authority"],
            "details": "Schema, strict, terms, GTDB shape/domain, history and original-review validation pass. Explained-reference checking fails for interaction indices 0, 1 and 3 against the selected abstract cache. The independent reviewer separately reports these as genuine main-text excerpts; this observation does not certify their primary-source reading. The actual failure is retained, completion is partial, and scientific_review is false. Source/check artifacts, earlier inspect and author helper are frozen; the final inspection and later save checks are outputs, avoiding recursive input hashes.",
        },
    ]
    finding = {
        "finding_id": "current-genus-authority",
        "issue_key": "cm-000020-current-genus-authority",
        "category": "grounding",
        "severity": "minor",
        "native_severity": "P3",
        "normalization_reason": "Bounded authority/provenance reconciliation preserves the same source isolate and does not invalidate the community or infer a different species.",
        "rule_id": "review-checklist.current-authority-and-source-alias",
        "status": "open",
        "certainty": "confirmed",
        "title": "Reconcile the Mameliella source alias with current NCBI genus authority",
        "description": "The four maintained descriptors still pair NCBITaxon:1434019 with Mameliella, while fresh NCBI resolves that alias to accepted genus Antarctobacter 74032. Reconcile the maintained identifier/label consistently, preserve the paper's Mameliella sp. CS4 designation, and keep any new GTDB route separate from the old 3/3 snapshot. Canonical follow-up is #2572; no record curation is performed here.",
        "target_ids": [TARGET],
        "field_paths": [row["path"] for row in read(OUT / "descriptor-locations.json")],
        "evidence_ids": ["authority", "retrieval", "record", "prior", "issue"],
        "owner_paths": owner,
    }
    action = {
        "action_id": "reconcile-current-genus-authority",
        "description": "Apply the separately tracked #2572 authority correction without changing source identity or retiring unrelated curation.",
        "finding_ids": [finding["finding_id"]],
        "target_ids": [TARGET],
        "owner_paths": owner,
        "acceptance_checks": [
            "Inspect the current authoritative alias/accepted-genus relationship, then reconcile the canonical NCBITaxon identifier and label consistently across taxonomy and repeated interaction participants. Preserve the source designation Mameliella sp. CS4 explicitly.",
            "Do not infer an exact species, collection strain or biological reassignment from the genus relationship. UpdateDate alone is not the date of a merge event.",
            "Re-evaluate GTDB for the chosen maintained ID using the pinned crosswalk and actual route. Preserve the prior Mameliella 3/3 result as a historical snapshot; do not silently carry it to a changed ID or force a replacement.",
            "Keep existing biological findings, graph directions and evidence tiers. Run native schema, strict, term, reference, GTDB, domain and history checks after separately authorized curation, append history and regenerate the affected page.",
            "Keep #1359 and other 000020 curation scopes open until their own acceptance checks are met. No kb record is edited by PR #2058.",
        ],
    }
    result = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-coscinodiscus-current-genus-authority",
        "kind": "record",
        "repository": old["repository"],
        "title": "Coscinodiscus CS4 review correction: current NCBI genus authority",
        "started_at": "2026-11-06T15:52:26.966553Z",
        "finished_at": now,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of this bounded authority correction. Separate agents perform independent re-review; shared source retrieval is explicitly attributed.",
        },
        "skill": "review-yaml-record",
        "completion": "partial",
        "verdict": "needs_curation",
        "scientific_review": False,
        "summary": "Withdraw the original unqualified current-genus approval: fresh NCBI resolves taxid 1434019 to genus 74032 Antarctobacter, with Mameliella as synonym. Preserve the source alias Mameliella sp. CS4, historical GTDB snapshot and all four original scientific finding heads/five actions. Add only the minor authority follow-up #2572. The known three reference-cache misses remain; no full-paper or SI reassessment is claimed.",
        "source": inspection["source"],
        "targets": inspection["targets"],
        "scope": {
            "description": "Current NCBI alias/accepted-genus relationship, four exact maintained descriptor locations, prior review assertion and focused deterministic checks only.",
            "selection": "Exactly CommunityMech:000020 in PR #2058; bounded correction for #2571 and canonical action #2572.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [TARGET],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": [finding],
        "actions": [action],
        "limitations": [
            "Literature, supplementary sources, biological mechanisms, graph support, cultivation and resource conclusions are not scientifically reassessed by this authority-only author pass.",
            "Seven focused checks pass and explained-reference checking retains three existing cache misses. Passing local term checks do not override fresh NCBI accepted-name evidence.",
            "The old four finding heads/five actions remain independent and open; no prior occurrence or grouped review is superseded. Whole-record scores are not recomputed for this bounded observation.",
            "No new GTDB replay, exact species/strain assignment or merge-event dating is performed. The historical Mameliella 3/3 mapping cannot be silently transferred to a changed ID.",
        ],
        "related_reviews": [
            {
                "repository": old["repository"],
                "review_id": old["review_id"],
                "relationship": "Append-only correction of current-authority implications in identity, grounding and taxonomy assessments only; all four scientific finding heads and five actions remain untouched.",
            }
        ],
        "notes": [
            "Remediates review-bundle issue #2571 through an immutable observation. Canonical authority issue #2572 remains open; no kb, cache, history or generated product was edited.",
            "All actual local author inputs are captured via native inspection. The new inspection manifest cannot hash itself; candidate and post-save checks are later outputs. The JSON helper introduces no YAML writer.",
        ],
        "tags": [
            "pr2058",
            "authority-correction",
            "bounded-observation",
            "no-scientific-supersession",
        ],
    }
    (OUT / "candidate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "review_id": result["review_id"],
                "candidate": str(OUT / "candidate.json"),
                "inputs": len(result["source"]["inputs"]),
            }
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["prepare", "build"])
    parser.add_argument("inspection", type=Path, nargs="?")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    else:
        build(args.inspection)
