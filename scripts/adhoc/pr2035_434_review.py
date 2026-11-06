"""Build the source-reassessed, immutable successor for PR 2035 record 434.

Run verify after the audit helper's initial inspection/source captures/checks,
then inspect-final with that helper, then build. This writes scratch candidate
YAML only; the native record_review validator and saver publish the bundle.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shlex
import subprocess
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import yaml
from defusedxml import ElementTree

from communitymech.network.auditor import NetworkIntegrityAuditor

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2035/434"
OLD = "reviews/structured/20261020T035434Z-acidic-nitrification-record/review.yaml"
TARGET = "kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml"
HISTORY = (
    "history/records/Acidic_Nitrification_Minimal_Consortium/2026-10-21T190000Z-claude-2047.yaml"
)
REPO = "CultureBotAI/CommunityMech"
IDS = ["CommunityMech:000434"]


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((OUT / f"{name}.json").read_text())


def normalized(value):
    return " ".join(unicodedata.normalize("NFKC", value).split())


def differences(before, after, path=""):
    if (
        isinstance(before, str)
        and isinstance(after, str)
        and normalized(before) == normalized(after)
    ):
        return []
    if isinstance(before, dict) and isinstance(after, dict):
        return [
            item
            for key in sorted(set(before) | set(after))
            for item in differences(before.get(key), after.get(key), f"{path}.{key}".strip("."))
        ]
    if isinstance(before, list) and isinstance(after, list) and len(before) == len(after):
        return [
            item
            for index, (left, right) in enumerate(zip(before, after, strict=True))
            for item in differences(left, right, f"{path}[{index}]")
        ]
    return [] if before == after else [{"path": path, "before": before, "after": after}]


def evidence_items(value, path=""):
    if isinstance(value, dict):
        if "snippet" in value and "supports" in value and "reference" in value:
            yield path, value
        for key, item in value.items():
            yield from evidence_items(item, f"{path}.{key}".strip("."))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from evidence_items(item, f"{path}[{index}]")


def verify():
    prior = yaml.safe_load((ROOT / OLD).read_text())
    target = yaml.safe_load((ROOT / TARGET).read_text())
    historical_bytes = subprocess.check_output(
        ["git", "show", f"{prior['source']['git_revision']}:{TARGET}"], cwd=ROOT
    )
    frozen = next(item for item in prior["source"]["inputs"] if item["path"] == TARGET)
    assert hashlib.sha256(historical_bytes).hexdigest() == frozen["sha256"]
    document = ElementTree.fromstring((OUT / "source-pubmed.body").read_bytes())
    abstract = " ".join("".join(node.itertext()) for node in document.findall(".//AbstractText"))
    identifiers = {
        node.attrib["IdType"]: "".join(node.itertext()) for node in document.findall(".//ArticleId")
    }
    # These two record snippets are labelled identifier metadata, not article
    # prose. Match the value to the corresponding XML identifier type exactly.
    metadata = f"PMID: {identifiers['pubmed']} DOI: {identifiers['doi']}"
    snippets = [
        {
            "path": path,
            "source_scope": (
                "abstract" if normalized(item["snippet"]) in normalized(abstract) else "metadata"
            ),
            "matches": normalized(item["snippet"]) in normalized(abstract + " " + metadata),
        }
        for path, item in evidence_items(target)
    ]
    assert snippets and all(item["matches"] for item in snippets), snippets
    result = {
        "started_at": now(),
        "historical_sha256": frozen["sha256"],
        "current_sha256": sha(ROOT / TARGET),
        "semantic_changes": differences(yaml.safe_load(historical_bytes), target),
        "snippets": snippets,
        "network_issues": NetworkIntegrityAuditor().audit_community(ROOT / TARGET),
        "finished_at": now(),
    }
    assert not result["network_issues"], result["network_issues"]
    with (OUT / "reassessment.json").open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(result, indent=2))


class NoAliases(yaml.SafeDumper):
    def ignore_aliases(self, _data):
        return True


def build():
    review = yaml.safe_load((ROOT / OLD).read_text())
    prior_id = review["review_id"]
    initial = read("inspect-initial")
    final = json.loads((OUT / "inspect-final.stdout").read_text())
    replay = read("reassessment")
    stamp = now()
    review.update(
        review_id=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-pr2035-acidic-nitrification-successor",
        title="Acidic nitrification consortium: refreshed current-record assessment for PR 2035",
        started_at=initial["started_at"],
        finished_at=stamp,
        source=final["source"],
        reviewer={
            "identity": "codex-pr2035-434-refresh-author",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of this successor bundle; record itself was not edited. Independent adversarial review of this PR is a separate pass.",
        },
        completion="partial",
        verdict="needs_curation",
        summary="The current record retains a source-bounded putative community linkage. The newly added primary-producer role and dominance labels are supported at their stated computational and pH-specific scope. The original role finding is resolved; application-motivation evidence typing remains open. A new external-history provenance finding concerns an incorrect record ID, category and partner. Full Methods remain unavailable and the origin classification requires verification without assuming an assembled two-strain culture.",
        related_reviews=[
            {
                "repository": REPO,
                "review_id": prior_id,
                "relationship": "Current-record successor; explicitly reassesses both predecessor findings and all stale target changes.",
            }
        ],
    )
    review["scope"][
        "selection"
    ] = "Exact stale record in PR 2035; compared current origin/main record bytes with the predecessor's frozen input and reread all scientific assertions."
    review["scope"][
        "description"
    ] = "Whole current record and five history entries read; every present node, absence of arrows, evidence occurrence, newly added field and prior finding reassessed against freshly retrieved primary abstract and identifier metadata."
    review["checks"] = []
    review["evidence"] = []

    def ev(
        eid, kind, ref, locator, summary, support="supports", timestamp=stamp, digest=None, **extra
    ):
        item = {
            "evidence_id": eid,
            "kind": kind,
            "reference": ref,
            "locator": locator,
            "summary": summary,
            "support": support,
            "accessed_at": timestamp,
        }
        if digest:
            item["snapshot_sha256"] = digest
        item.update(extra)
        review["evidence"].append(item)

    ev(
        "record",
        "record_content",
        TARGET,
        "Whole current record",
        "Two taxa; one putative interaction; no downstream arrows; two environmental factors; three chemicals; two publication resources. Changed fields are origin, primary-producer role, dominance metadata and appended history.",
        digest=sha(ROOT / TARGET),
    )
    pubmed = read("source-pubmed")
    ev(
        "abstract",
        "primary_source",
        "PMID:42762737",
        pubmed["url"] + "; complete abstract",
        "Primary abstract describes three aerobic reactors, pH-specific dominance and genome/transcriptional potential. It does not supply exact exchanged compounds, source MAG accessions, assembly methods or demonstrated wastewater-performance improvement.",
        timestamp=pubmed["finished_at"],
        digest=pubmed["sha256"],
    )
    ev(
        "linkage",
        "primary_source",
        "PMID:42762737",
        "Abstract, pH 2 community paragraph",
        "Supports putative carbon/nitrogen cycling, not resolved direction, compounds, reciprocal benefit or partner-specific rescue.",
        timestamp=pubmed["finished_at"],
        quote="suggested potential metabolic linkages related to carbon and nitrogen compound cycling",
    )
    ev(
        "dominance",
        "primary_source",
        "PMID:42762737",
        "Abstract, pH 5 and pH 2 sentences",
        "The ammonia oxidizer reaches up to 56% at pH 5; at pH 2 both named populations dominate. This does not imply constant abundance or exactly two isolates. Carbon-fixation genes support the newly added PRIMARY_PRODUCER annotation at computational evidence scope.",
        timestamp=pubmed["finished_at"],
        quote="dominated by",
    )
    source_summaries = {
        "europepmc": (
            "epmc",
            "Article identity agrees; no PMCID and subscription-required DOI link. This is an access label, not proof of permanent paywall.",
        ),
        "crossref": (
            "crossref",
            "Title and DOI agree. CC-BY version-of-record license starts September 16, 2026; licenses alone do not provide full text.",
        ),
        "publisher": ("publisher", "HTTP 403 response does not establish accessible full Methods."),
        "publisher-xml": (
            "publisher-xml",
            "HTTP 200 returns only coredata metadata, including the matching title, DOI and open-access label; no article body or Methods is present.",
        ),
        "taxonomy": (
            "taxonomy-search",
            "NCBI exact-name search for Nitrosoglobus kelleri returns zero results at this access time. Retain explicit broad fallback and unresolved GTDB status.",
        ),
        "imodulondb": (
            "adapter",
            "Entire public catalog inspected: 20 organisms, 28 datasets. No Nitrosoglobus dataset; M. tuberculosis is not an identity match for this genus-only environmental Mycobacterium population. No exact source strain or module can be assigned.",
        ),
    }
    for name, (eid, summary) in source_summaries.items():
        receipt = read("source-" + name)
        ev(
            eid,
            "database",
            receipt["url"],
            f"Actual HTTP {receipt['status']}; {receipt['size_bytes']} bytes",
            summary,
            support=(
                "context_only"
                if name.startswith("publisher") or name == "imodulondb"
                else "supports"
            ),
            timestamp=receipt["finished_at"],
            digest=receipt["sha256"],
        )
    ev(
        "ontology",
        "authority",
        "src/communitymech/schema/communitymech.yaml; native validate-terms receipt",
        "Six unique terms: two NCBITaxon, one ENVO, three CHEBI",
        "Focused label validation passes without ontology skips. Family Nitrosococcaceae and genus Mycobacterium are explicit fallback scopes; ingredient identity is not proof of exchanged metabolite identity.",
        digest=sha(OUT / "validate-terms.json"),
    )
    ev(
        "schema",
        "authority",
        "src/communitymech/schema/communitymech.yaml",
        "FunctionalRoleEnum.PRIMARY_PRODUCER; EvidenceSourceEnum; CommunityOriginEnum",
        "PRIMARY_PRODUCER denotes carbon fixation/autotrophy; the source reports gene potential. ENGINEERED origin means deliberately engineered or synthetic; reactor operation does not by itself establish a two-isolate assembly. IN_VITRO labels experiments, whereas the application statement is prospective motivation.",
        digest=sha(ROOT / "src/communitymech/schema/communitymech.yaml"),
    )
    ev(
        "snippets",
        "validation",
        TARGET,
        "All 16 EvidenceItem occurrences; independent NFKC/whitespace replay against fresh PubMed XML",
        "Fourteen science snippets match the abstract; two publication identifier snippets match metadata. The native reference validator also passes; matching does not prove appropriate evidence classification.",
        digest=sha(OUT / "reassessment.json"),
    )
    ev(
        "history",
        "record_content",
        "history/records/Acidic_Nitrification_Minimal_Consortium",
        "All five history files plus target rows of the three causal-review decision ledgers",
        "Earlier removal of unsupported cultivation and directed mechanisms remains appropriate. Oct31 role/dominance history matches the current record. Oct21 external history incorrectly says 000359, SYNTHETIC_COMMUNITY and Nitrosoglobus/Nitrobacter; current target and embedded history do not contain those claims.",
    )
    ev(
        "history-mismatch",
        "record_content",
        HISTORY,
        "events[0].details",
        "The target path is correct, but its explanation names the wrong record ID, category and microbial partner, and asserts unsupported constructed-consortium provenance. Correct by a new append-only history entry, preserving the original bytes.",
        support="refutes",
        digest=sha(ROOT / HISTORY),
    )
    ev(
        "local-search",
        "search",
        "Local evidence, history and decisions",
        "Ignored-inclusive identifier, slug and citation search",
        "Search found the committed abstract, five target history files and three decision ledgers; no full article in these searched roots. Installed source runner was not on PATH and three explicitly checked sibling CLAW locations did not exist; this is a bounded runner search.",
        support="context_only",
        search_scope="rg --no-ignore --hidden -l '42762737|Acidic_Nitrification_Minimal_Consortium|watres.2026.126966' references_cache history/records reports/causal_graph_review/decisions kb/taxa. Ignored files included. Runner: command -v kg-microbe-sources; checked /Users/marcin/Documents/VIMSS/{culturebotai-claw,ontology/culturebotai-claw,ontology/Mechs/culturebotai-claw}. Public catalog fallback inspected.",
    )
    ev(
        "staleness",
        "prior_review",
        OLD,
        "source.inputs target hash and both prior findings",
        "Historical frozen target hash verified via git show. Parsed changes are exactly origin, taxon role/dominance metadata and appended history; the single putative node and evidence text are unchanged. All changed fields were reassessed rather than merely rehashed.",
        digest=sha(OUT / "reassessment.json"),
    )

    recipes = [
        "validate",
        "validate-strict",
        "validate-terms",
        "validate-gtdb",
        "validate-gtdb-domain",
        "validate-history",
        "cache-preflight",
        "validate-references-explained",
        "audit-network",
        "check-network-quality",
    ]
    for name in recipes:
        receipt = read(name)
        corpus = name in {"audit-network", "check-network-quality"}
        summary = (
            "Required full-corpus check exits 1: 44 warnings among 16 of 503 records; target has no native network issues. Baseline warnings remain failures, not waived passes."
            if corpus
            else (receipt["stdout"] + receipt["stderr"]).strip()
            or "Command exited 0 with no output; read-only cache-name preflight found no rename work."
        )
        if corpus:
            assert receipt["exit_code"] == 1
        else:
            assert receipt["exit_code"] == 0
        eid = "check-" + name
        ev(
            eid,
            "validation",
            shlex.join(receipt["command"]),
            f"Actual execution {receipt['started_at']} to {receipt['finished_at']}; exit {receipt['exit_code']}",
            summary,
            support="context_only" if corpus else "supports",
            timestamp=receipt["finished_at"],
            digest=sha(OUT / f"{name}.json"),
        )
        review["checks"].append(
            {
                "check_id": name,
                "name": name,
                "status": "failed" if corpus else "passed",
                "required": True,
                "summary": summary,
                "target_ids": IDS,
                "command": "UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src JUST_NO_DOTENV=true "
                + shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [eid],
                "scope_note": (
                    "Full corpus; no warning converted to passing."
                    if corpus
                    else "Focused target/history; cache-name preflight is read-only corpus scope. Shared maintained Python 3.13 environment reused; no dependency sync."
                ),
            }
        )
    review["checks"].extend(
        [
            {
                "check_id": "full-text",
                "name": "Full source Methods retrieval",
                "status": "unavailable",
                "required": True,
                "summary": "Publisher HTML403; publisher XML200 contains coredata only. No Methods or supplements inspected.",
                "target_ids": IDS,
                "evidence_ids": ["publisher", "publisher-xml", "epmc", "crossref"],
            },
            {
                "check_id": "expression-adapter",
                "name": "Structured expression-source cross-check",
                "status": "not_applicable",
                "required": False,
                "summary": "Bounded runner search unavailable; full public catalog has no exact source-strain dataset. No module evidence borrowed from a congeneric species.",
                "target_ids": IDS,
                "evidence_ids": ["adapter", "local-search"],
            },
        ]
    )

    assessments = {item["assessment_id"]: item for item in review["assessments"]}
    assessments["identity"][
        "summary"
    ] = "Description and graph preserve three-reactor and pH-specific boundaries. Minimal is not proof that only two isolates exist. The new ENGINEERED origin is not treated as evidence of defined assembly; exact origin remains unresolved without Methods. Up to 56% is a pH-specific maximum."
    assessments["engineering"][
        "summary"
    ] = "Wastewater relevance remains prospective, but its evidence is still IN_VITRO and can imply measured application performance. Newly populated ENGINEERED origin may describe deliberate reactor cultivation, yet its asserted assembly rationale in external history is incorrect and the abstract does not establish inoculum origin. Verify Methods before treating origin as a constructed SynCom."
    assessments["engineering"]["evidence_ids"].append("history-mismatch")
    assessments["completeness"][
        "summary"
    ] = "PRIMARY_PRODUCER is now present for the ammonia oxidizer and supported at gene-potential scope. Leaving the genus-only partner without an exact functional role is appropriate given only putative linkage evidence; both prior taxon selectors were reassessed. The earlier role finding is resolved without inventing a partner function. Medium, reactor details, source MAGs and abundance matrix remain explicit open Methods questions."
    assessments["completeness"]["outcome"] = "unknown"
    assessments["provenance"].update(
        outcome="concern",
        summary="Fresh PubMed, EPMC, Crossref and publisher metadata agree on article identity; all 16 snippets replay against abstract or metadata. External Oct21 history has a concrete ID/category/partner mismatch despite correct embedded history. Publisher XML200 is metadata only, not full-text access.",
        evidence_ids=[
            "abstract",
            "epmc",
            "crossref",
            "publisher-xml",
            "snippets",
            "history-mismatch",
        ],
    )
    assessments["taxonomy"][
        "summary"
    ] += " New PRIMARY_PRODUCER is supported as genomic carbon-fixation potential, and both DOMINANT labels retain the pH-qualified source context."
    assessments["taxonomy"]["evidence_ids"].extend(["dominance", "schema"])
    assessments["metrics"][
        "summary"
    ] = "Completeness remains 10 because the optional, source-unresolved partner role cannot satisfy the native all-taxa role block. That is a rubric limitation, not permission to invent a role. Quality100 remains capped despite two currently open P3 findings; a resolved predecessor is excluded from active counts."
    assessments["metrics"]["metrics"][1][
        "definition"
    ] = "clamp(100-50*P1-10*P2-2*P3+20*min(mean node evidence/2,1)+15 if native COMPLETE,0,100). Active P1=0,P2=0,P3=2 (motivation evidence and external history); one attached evidence item/one node; native target audit has zero issues. clamp(100-4+10+15)=100. Resolved predecessor excluded; partial source review is not scientific approval."
    assessments["metrics"]["metrics"][0][
        "definition"
    ] += " The unresolved Mycobacterium role leaves the required block at zero; supported Nitrosoglobus role is present."
    review["assessments"].append(
        {
            "assessment_id": "refresh-diff",
            "area": "provenance",
            "topic": "Changed target bytes and predecessor findings",
            "outcome": "supported",
            "summary": "Current target SHA256 is "
            + replay["current_sha256"]
            + "; historical hash "
            + replay["historical_sha256"]
            + ". Parsed change locations: "
            + ", ".join(item["path"] for item in replay["semantic_changes"])
            + ". Initial native inspect preceded this formal assessment; final inspect adds the formatted author helper and newly read decision ledgers. No canonical input changed between these inspections.",
            "target_ids": IDS,
            "evidence_ids": ["record", "staleness", "history", "schema", "dominance"],
        }
    )

    for finding in review["findings"]:
        finding["previous_occurrences"] = [
            {"repository": REPO, "review_id": prior_id, "finding_id": finding["finding_id"]}
        ]
    role, motivation = review["findings"]
    role.update(
        status="resolved",
        title="Supported taxon role is now represented; unsupported partner role remains unknown",
        description="taxonomy[0].functional_role now has PRIMARY_PRODUCER with source evidence for carbon-fixation genes. taxonomy[1] remains unassigned because genus-level co-occurrence and potential linkage do not establish a specific partner function. Both prior field selectors were reviewed, including why absence of the second role is appropriate.",
        disposition_reason="The prior action requested only source-supported roles plus explicit uncertainty. Current primary-producer metadata satisfies the supported part; the whole-record putative linkage and source-gap discussion preserve uncertainty for the partner. Missing unsupported metadata is not a scientific defect merely because it lowers a rubric score.",
        normalization_reason="Historical P3 minor completeness finding, now resolved after scoped source reassessment; no unsupported role added.",
    )
    motivation["normalization_reason"] = (
        "P3 minor evidence-provenance mismatch: prose retains the prospective qualifier, but the IN_VITRO tag overstates what this particular implication snippet demonstrates."
    )
    history_owner = [
        {
            "repository": REPO,
            "path": "history/records/Acidic_Nitrification_Minimal_Consortium",
            "role": "append_only_history",
        }
    ]
    review["findings"].append(
        {
            "finding_id": "origin-history-provenance",
            "issue_key": "cm-000434-origin-history-provenance",
            "category": "provenance",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "P3 minor provenance defect: external history is materially inaccurate while the current scientific record identity, participant and category remain correct.",
            "rule_id": "AGENTS.append-only-history",
            "status": "open",
            "certainty": "confirmed",
            "title": "Origin curation history names the wrong record, category and partner",
            "description": "The Oct21 external history targets this file but describes CommunityMech:000359, SYNTHETIC_COMMUNITY and a constructed Nitrosoglobus/Nitrobacter pair. The actual record is 000434, BIOTECHNOLOGY and Nitrosoglobus/Mycobacterium. The construction rationale is not established by the inspected abstract. Embedded history is correct; changing it alone would not repair the external provenance.",
            "target_ids": IDS,
            "field_paths": [HISTORY + "::events[0].details"],
            "evidence_ids": ["record", "abstract", "history-mismatch", "schema"],
            "owner_paths": history_owner,
        }
    )
    review["actions"] = [copy.deepcopy(review["actions"][1])]
    review["actions"].extend(
        [
            {
                "action_id": "correct-origin-history",
                "description": "Append a corrective history entry that identifies the incorrect Oct21 explanation and states the verified record ID, category and Mycobacterium partner. Check Methods before claiming deliberate community assembly or changing origin; do not rewrite old history.",
                "finding_ids": ["origin-history-provenance"],
                "target_ids": IDS,
                "owner_paths": history_owner,
                "acceptance_checks": [
                    "Old history bytes remain intact; new entry names the exact superseded file and corrections.",
                    "Distinguish engineered reactor operation from verified assembled-community origin.",
                    "Run validate-history and focused record/reference checks for any authorized curation; regenerate affected products if the canonical record changes.",
                ],
            },
            {
                "action_id": "verify-source-methods",
                "description": "Track the existing discussions[0] source-detail request: obtain authorized full Methods/supplements to assess origin, medium/feed, reactor dimensions and schedule, inoculum, MAG/data accessions and pH-specific abundances. This is a pre-existing curation follow-up, not newly invented evidence or a required extra graph.",
                "finding_ids": [],
                "target_ids": IDS,
                "owner_paths": review["targets"][0]["owner_paths"],
                "acceptance_checks": [
                    "Record article versus supplement source boundaries and exact locators.",
                    "Preserve unknown fields when the full source still supplies no evidence; do not infer specific partner role, exchange direction or compounds.",
                    "Validate any later authorized record curation with schema, strict, terms, references, history and generated-products checks.",
                ],
            },
        ]
    )
    review["limitations"] = [
        "Partial full-source verification: complete abstract and metadata were freshly inspected, but publisher HTML403 and metadata-only XML200 did not provide Methods, supplements or raw data.",
        "EPMC subscription label conflicts with Crossref/publisher open-access metadata; no permanent access restriction or source absence is inferred.",
        "Exact candidatus taxonomy search returned zero at access time; genus-only partner and unresolved GTDB mappings cannot be promoted to exact strains or genomes.",
        "ENGINEERED origin is not certified as deliberate two-isolate assembly. Its source-specific interpretation remains a Methods follow-up; inaccurate external history is a separate confirmed finding.",
        "Required whole-corpus network checks failed with the current 44-warning baseline; target-specific native audit has no issues. No validator or threshold was altered.",
        "Optional expression runner search was bounded; public catalog fallback has no exact strain match. No provider invoked and no canonical record, cache, history or product edited.",
    ]
    review["notes"] = [
        "New author helpers and an immutable successor bundle only; original review bytes remain intact.",
        "Whitespace-normalized parsed comparison distinguishes YAML reformatting from changed scientific metadata; raw target hashes are retained separately.",
        "Source quotations total fewer than 25 words; interpretation is separate from the short exact quotations.",
    ]
    with (OUT / "candidate.yaml").open("x") as stream:
        yaml.dump(review, stream, Dumper=NoAliases, sort_keys=False, allow_unicode=True, width=100)
    print(review["review_id"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["verify", "build"])
    args = parser.parse_args()
    (verify if args.mode == "verify" else build)()


if __name__ == "__main__":
    main()
