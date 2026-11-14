#!/usr/bin/env python3
"""Freeze predecessor identities and authored delta acceptance, 2026-11-14.

Inputs: three immutable scientific bundles plus unchanged LBNL context.
Output: an ignored acceptance map for the later native batch review. This is
preparation only: it reads no changing canonical input and resolves no finding.
Serves #2676/#2708/#2709/#2710/#2772/#2773 and retained scientific findings.
"""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
REVIEWS = (
    "20261114T212137Z-m5-ecofab-completion-canary",
    "20261114T213322Z-m5-yolo-scientific-completion",
    "20261114T213444Z-m5-dopamine-syncom-primary-review",
)
CONTEXT = (
    "20261114T213343Z-m5-lbnl-switchgrass-completion",
    "20261114T213834Z-m5-lbnl-environment-addendum",
)
ACCEPTANCE = {
    "cm-000025-cache-content-type": [
        "Both ring-trial and nitrogen cache declarations accurately name their already present abstract/full-main payloads.",
        "Apart from the single content_type value in each frontmatter, all source bytes and boundary/identity/provenance markers remain identical to the reviewed baseline.",
        "Post-change reference checks pass for 000025; no supplement text is merged into the main article.",
    ],
    "cm-000025-dopamine-relation-description": [
        "Relation prose states ring17 equals dopamine16 plus OAE829; existing typed relation, all17 ring stocks, related target and source evidence are unchanged.",
        "Primary Coker/Ding stock lists and ring S2 continue to support distinct16-stock comparators; no identity equivalence is inferred.",
        "Native history and all focused post-change gates pass, including generated documentation checks.",
    ],
    "cm-000515-gtdb-copied-mechanism-provenance": [
        "Copied record-specific amoA/ammonia-oxidation attribution is replaced by source-bounded 16S taxonomic evidence and explicit functional uncertainty.",
        "All six stored numerical mapping cores remain unchanged, including curated Nitrososphaeria552/631 and fraction0.875; pin the actually reproduced crosswalk hash/method without claiming a release/build date.",
        "Six measured control abundances, both treatment response nodes, all soil/protocol fields and evidence snippets are unchanged; native history and post-change checks pass.",
    ],
    "cm-pmid42660928-cache-content-type": [
        "Shared Ding cache content_type describes the existing abstract plus full-main text; all remaining source bytes and article/supplement boundaries are unchanged.",
        "Post-change reference checks pass for BOTH 000515 and000516. Retain both predecessor finding heads and target IDs in a single terminal observation.",
    ],
    "cm-000516-exudate-decrease-host-target-scope": [
        "Remove HOST_IS_TARGET from node4 while retaining the measured pooled extracellular dopamine decrease, all source evidence and unresolved microbial consumption versus changed host production/exudation. Separately verify removal of residual effect_direction under issue2778; do not invent a structured predecessor for that issue-only observation.",
        "No host metabolic effect, uptake or catabolic mechanism is asserted; five nodes/zero downstream arrows and intended16-member inoculum remain intact.",
        "Native history and all focused post-change gates pass, including generated documentation checks.",
    ],
    "cm-000516-correlation-direction-scope": [
        "Remove HOST_IS_SOURCE and signed effect_direction from correlation-only nodes0/1 while preserving observed correlation signs and the explicit association/relative16S limits.",
        "The source-supported isolate interventions in nodes2/3 retain their INCREASES/DECREASES effects and no host role; no in-SynCom mechanism is inferred.",
        "Correct docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md to use measured isolate-growth effects for signed examples and explicitly separate correlations from causal direction. Verify both the example and the worked-example host_participation table row (issue2777).",
        "Native history and all focused post-change gates pass, including generated documentation checks.",
    ],
}


def read_review(review_id):
    path = ROOT / "reviews/structured" / review_id / "review.yaml"
    raw = path.read_bytes()
    return yaml.load(raw, Loader=yaml.CSafeLoader), {
        "review_id": review_id,
        "path": str(path.relative_to(ROOT)),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def main():
    findings = {}
    sources = []
    targets = {}
    for review_id in REVIEWS:
        review, provenance = read_review(review_id)
        sources.append(provenance)
        targets.update({row["target_id"]: row for row in review["targets"]})
        for finding in review["findings"]:
            key = finding["issue_key"]
            entry = findings.setdefault(
                key,
                {
                    "issue_key": key,
                    "proposed_disposition": (
                        "resolve_only_after_acceptance" if key in ACCEPTANCE else "retain_open"
                    ),
                    "target_ids": [],
                    "previous_occurrences": [],
                    "prior_findings": [],
                    "acceptance": ACCEPTANCE.get(
                        key,
                        [
                            "No change addressing this finding is in the authorized delta. Re-inspect its selectors for unchanged semantics and retain the current open finding and owner/action scope."
                        ],
                    ),
                },
            )
            entry["target_ids"] = sorted(set(entry["target_ids"] + finding["target_ids"]))
            entry["previous_occurrences"].append(
                {
                    "repository": "CultureBotAI/CommunityMech",
                    "review_id": review_id,
                    "finding_id": finding["finding_id"],
                }
            )
            entry["prior_findings"].append(finding)
    context = []
    for review_id in CONTEXT:
        review, provenance = read_review(review_id)
        context.append(
            {
                **provenance,
                "findings": review["findings"],
                "reason": "Unchanged000087 outside delta; no supersession or closure",
            }
        )
    receipt = {
        "status": "preparation_only_no_canonical_assessment_or_disposition",
        "scope": "Changed fields in exactly three maintained records, related guidance, caches and new history; shared cache2708 includes both consumers",
        "targets": list(targets.values()),
        "prior_review_inputs": sources,
        "finding_acceptance_map": list(findings.values()),
        "excluded_context": context,
        "additional_issue_only_corrections": [
            {
                "issue": "https://github.com/CultureBotAI/CommunityMech/issues/2777",
                "acceptance": "Worked-example host_participation table no longer claims the removed000516tags remain present; no other example changes are inferred.",
                "disposition_policy": "Verify correction and link issue; no invented terminal structured finding predecessor",
            },
            {
                "issue": "https://github.com/CultureBotAI/CommunityMech/issues/2778",
                "acceptance": "Node4 has neither host_participation nor effect_direction; description/evidence retain the observed SynCom-to-extracellular-dopamine endpoint and unresolved mechanism.",
                "disposition_policy": "Verify correction and link issue; no invented terminal structured finding predecessor",
            },
        ],
        "required_after_writes_complete": [
            "Native inspect exact current targets and all actually assessed source/schema/guidance/history/caches before delta assessment",
            "Independently inspect complete changed records and exact baseline diff; reject any unreviewed semantic change",
            "Inspect actual persisted correction receipts and sidecars; preserve prior bytes and model/actor provenance",
            "Hash-verify seven fresh M5 post-curation check logs per target and generated documentation receipts",
            "Only then validate/save one immutable kind:batch review with coverage:partial and exact previous_occurrences; never close GitHub issues automatically",
        ],
    }
    output = STATE / "postcuration-acceptance-map.json"
    output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(output)
    print(
        f"{len(targets)} targets; {len(findings)} unique finding keys; {len(ACCEPTANCE)} candidate resolutions"
    )


if __name__ == "__main__":
    main()
