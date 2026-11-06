"""Build a JSON candidate and invoke native immutable review persistence for PR 2044."""

from __future__ import annotations

import argparse
import copy
import json
import shlex
from datetime import datetime, timezone

import yaml
from pr2044_447_audit import ID, OLD, ROOT, SCRATCH, TARGET, now, run, sha, write

REPOSITORY = "CultureBotAI/CommunityMech"
CHECKS = [
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


def load(name):
    return json.loads((SCRATCH / name).read_text())


def local_evidence(eid, kind, path, locator, summary, support="supports"):
    evidence = {
        "evidence_id": eid,
        "kind": kind,
        "reference": path,
        "locator": locator,
        "summary": summary,
        "support": support,
        "accessed_at": now(),
        "snapshot_sha256": sha((ROOT / path).read_bytes()),
    }
    if kind == "search":
        evidence["search_scope"] = summary
    if eid == "search-leads":
        evidence["support"] = "context_only"
    return evidence


def source_evidence(eid, name, summary, locator="Inspected source body and retrieval receipt"):
    receipt = load(name + ".receipt.json")
    return {
        "evidence_id": eid,
        "kind": "database",
        "reference": receipt["url"],
        "locator": locator,
        "summary": summary,
        "support": "supports",
        "accessed_at": receipt["accessed_at"],
        "snapshot_sha256": receipt["sha256"],
    }


def build():
    old = yaml.safe_load((ROOT / OLD).read_text())
    initial = load("inspection.json")
    for item in initial["source"]["inputs"]:
        assert sha((ROOT / item["path"]).read_bytes()) == item["sha256"], item["path"]
    paths = {x["path"] for x in initial["source"]["inputs"] if x["role"] != "target"}
    paths.add("reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml")
    paths.update(str(p.relative_to(ROOT)) for p in (ROOT / "scripts/adhoc").glob("pr2044_447_*.py"))
    scratch_names = [
        "inspection.json",
        "inspect.json",
        "targets.json",
        "lineage.json",
        "target-diff.stdout.txt",
        "frozen-target.stdout.txt",
        "local-search.json",
        "local-search.stdout.txt",
        "adapter-discovery.json",
        "support-final.json",
        "source-qualification-final.json",
        "legacy-finding-search-final.json",
        "legacy-finding-search-final.stdout.txt",
        "strict.tsv",
    ]
    for name in CHECKS:
        scratch_names.extend([name + ".json", name + ".stdout.txt", name + ".stderr.txt"])
    for name in [
        "pubmed.xml",
        "epmc.json",
        "crossref.json",
        "doi.html",
        "publisher.html",
        "article-api.xml",
        "openalex.json",
        "ncbi-taxonomy.xml",
        "imodulon-catalog.json",
    ]:
        scratch_names.extend([name, name + ".receipt.json"])
    paths.update(str((SCRATCH / name).relative_to(ROOT)) for name in scratch_names)
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
    inspection = run("final-inspect-v3", args)
    assert inspection.returncode == 0, inspection.stderr.decode()
    final = json.loads(inspection.stdout)
    write("final-inspection-v3.json", final)
    review = copy.deepcopy(old)
    review_id = (
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-pr2044-brocadia-current-input-refresh"
    )
    review.update(
        {
            "review_id": review_id,
            "title": "Brocadia low-nitrogen consortium: current-input and participant-scope refresh",
            "started_at": load("inspect.json")["started_at"],
            "finished_at": now(),
            "reviewer": {
                "identity": "codex",
                "kind": "agent",
                "independence": "self_review",
                "independence_basis": "Author refresh of the stale PR 2044 review. This saved observation makes no independent approval claim; the separate adversarial pass is outside this bundle.",
            },
            "completion": "partial",
            "verdict": "needs_curation",
            "scientific_review": False,
            "summary": "The current record retains supported temporal biofilter identity and abstract-level quantities. The original P3 outcome-placement finding remains open. A new P2 finding distinguishes Kuenenia succession membership from participation in the model-inferred Brocadia cross-feeding node. Full Methods/Results, figures and SI remain unavailable; the review is partial.",
            "source": final["source"],
            "targets": final["targets"],
            "scope": {
                "description": "Entire current record and its sole interaction/no downstream arrows reassessed at direct abstract scope, with explicit analysis of the changed participant list, description, evidence and history. Unread full-source material is excluded from certification.",
                "selection": "The sole stale record CommunityMech:000447 identified for PR 2044 after merging main.",
                "coverage": "full",
                "population_size": 1,
                "reviewed_target_ids": [ID],
            },
        }
    )
    evidence = []
    evidence.append(
        local_evidence(
            "record",
            "record_content",
            TARGET,
            "Entire current record; especially ecological_interactions[0] and curation_history[2]",
            "The temporal low-nitrogen biofilter contains two genus descriptors. The current node newly lists Kuenenia alongside Brocadia, adds a succession quote and expands its description; all other scientific fields remain unchanged.",
        )
    )
    for eid, name, summary in [
        (
            "pubmed",
            "pubmed.xml",
            "Fresh exact PMID, DOI, title and complete primary abstract identify the focal study. No full article is supplied by this response.",
        ),
        (
            "epmc",
            "epmc.json",
            "Fresh complete abstract agrees. No PMCID is supplied and the full-text URL requires subscription.",
        ),
        (
            "crossref",
            "crossref.json",
            "Fresh DOI and title agree with PubMed. Bibliographic metadata is not independent mechanistic evidence.",
        ),
        (
            "ncbi",
            "ncbi-taxonomy.xml",
            "Fresh NCBI records identify Candidatus Brocadia 380240 and Candidatus Kuenenia 380738 at genus rank.",
        ),
    ]:
        evidence.append(source_evidence(eid, name, summary))
    for eid, locator, summary, quote in [
        (
            "succession",
            "Abstract: early-acclimation and final succession sentences",
            "Kuenenia reduces costly biosynthesis during early acclimation, including aromatic amino-acid synthesis by 25.6%–38.8%; Brocadia later replaces it as dominant functional lineage. This establishes temporal presence and replacement, not metabolite exchange between the genera.",
            "dominant functional lineage",
        ),
        (
            "model",
            "Abstract: long-term operation sentence",
            "The long-term community shifts to a multispecies Brocadia assemblage with complementary model-inferred auxotrophies. Associations and SMETANA predictions do not demonstrate direct exchange, flux or obligatory dependence; the inspected sentence does not assign Kuenenia to that complementary assemblage.",
            "complementary model-inferred auxotrophies",
        ),
        (
            "quantities",
            "Abstract: transcription, overlap and abundance sentences",
            "Approximately 18-fold gene upregulation, overlap 0.66 ± 0.12 versus 0.77 ± 0.10, abundance rising from 1.0% to 44.7%, 71.5% transcriptional contribution and 68.0% positive associations have distinct measurement denominators.",
            None,
        ),
        (
            "operation",
            "Abstract: operated biofilter and analysis design sentences",
            "An operated anammox biofilter under sustained low-nitrogen stress was examined using metagenomics, metatranscriptomics, co-occurrence networks and SMETANA. Exact reactor configuration and nutrient loading remain unverified at this source scope.",
            None,
        ),
    ]:
        item = source_evidence(eid, "pubmed.xml", summary, locator)
        item.update(kind="primary_source", reference="PMID:42323145")
        if quote:
            item["quote"] = quote
        evidence.append(item)
    evidence.append(
        local_evidence(
            "schema",
            "authority",
            "src/communitymech/schema/communitymech.yaml",
            "EnvironmentalFactor; EcologicalInteraction.participating_taxa; InteractionTypeEnum.CROSS_FEEDING; MicrobialCommunity.ecological_state; abundance and functional-role enums",
            "Environmental factors are conditions or parameters; CROSS_FEEDING denotes metabolite exchange and participating_taxa identifies actual members of that interaction. Ecological state is optional (no required:true), and ENGINEERED is valid here. DOMINANT is ordinal; autotrophic and predicted-recipient roles must not be presented as directly measured carbon fixation or exchange.",
        )
    )
    for eid, name, summary, kind in [
        (
            "ontology",
            "support-final.json",
            "Four unique ontology pairs across six occurrences match local OAK labels. Fresh NCBI taxonomy confirms both taxa are genera; no species or genome mapping is inferred.",
            "authority",
        ),
        (
            "semantics",
            "support-final.json",
            "Temporal taxonomic membership and distinct measurement denominators are retained. Kuenenia's presence does not establish participation in the explicitly Brocadia-specific model complementarity.",
            "validation",
        ),
        (
            "snippets",
            "support-final.json",
            "All 13 snippet occurrences were replayed: 10 strict NFKC/whitespace abstract matches, one hyphen-glyph-only equivalent and two directly corroborated bibliographic identifiers. No full-text match is claimed.",
            "validation",
        ),
        (
            "native-target",
            "support-final.json",
            "The native target network returns zero issues (COMPLETE), one node and two node-evidence items. This structural pass does not establish scientific participant scope.",
            "validation",
        ),
        (
            "resources",
            "source-qualification-final.json",
            "PMID and DOI identify the focal publication. No exact MAG/species identity, SMETANA model source or reproducible medium/feed is established by the inspected abstract; they are unresolved rather than proven absent.",
            "database",
        ),
        (
            "source-scope",
            "source-qualification-final.json",
            "Inspected public routes provide the complete abstract and metadata but not full main Methods/Results, figures or supplements; completion remains partial.",
            "validation",
        ),
        (
            "search-leads",
            "source-qualification-final.json",
            "A fresh exact DOI/title web search exposes indexed publisher Methods fragments. The direct publisher web open returns 403; fragments remain leads and no reactor quantities are curated or certified from them.",
            "search",
        ),
        (
            "adapter",
            "source-qualification-final.json",
            "The public iModulonDB organism catalogue has no Brocadia or Kuenenia dataset. No module lookup is applicable to these unresolved genera; this is not negative biological evidence.",
            "search",
        ),
        (
            "local-search",
            "local-search.stdout.txt",
            "Ignored-inclusive bounded searches covered reference cache, record histories, causal-review decisions and reusable taxa; no machine-wide absence claim is made.",
            "search",
        ),
        (
            "history",
            "lineage.json",
            "The original single-target outcome-placement finding remains open. Three current sidecars and both relevant graph decisions were read. Stage 4/5 grouped findings are context only, not superseded by this one-target review.",
            "record_content",
        ),
        (
            "delta",
            "target-diff.stdout.txt",
            "Frozen-to-current content adds Kuenenia participation, the succession quotation, quantified early-acclimation wording and one curation-history entry. The original outcome placement is unchanged.",
            "record_content",
        ),
    ]:
        evidence.append(
            local_evidence(
                eid, kind, str((SCRATCH / name).relative_to(ROOT)), "Whole bounded receipt", summary
            )
        )
    for eid, name, summary in [
        ("access-doi", "doi.html", "HTTP 200 redirect shell only; no full article."),
        ("access-publisher", "publisher.html", "HTTP 403 access-error page; no full article."),
        (
            "access-article-api",
            "article-api.xml",
            "HTTP 200 bibliographic coredata only; no article body.",
        ),
        (
            "access-openalex",
            "openalex.json",
            "Closed-access metadata supplies no open PDF in its listed locations; not proof of global absence.",
        ),
    ]:
        item = source_evidence(eid, name, summary)
        item["support"] = "context_only"
        evidence.append(item)
    checks = []
    for name in CHECKS:
        receipt = load(name + ".json")
        network = name in {"audit-network", "check-network-quality"}
        summary = (
            "Current corpus diagnostics report 44 warnings, zero errors, across 16 of 508 records; exit 1 is retained. The focal network separately returns zero issues, which does not establish participant evidence."
            if network
            else "Focused native check passed; mechanical validity does not certify scientific support."
        )
        command = (
            " ".join(f"{k}={shlex.quote(v)}" for k, v in receipt["environment"].items())
            + " "
            + receipt["command"]
        )
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "failed" if network else "passed",
                "required": True,
                "summary": summary,
                "target_ids": [ID],
                "command": command,
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + name] + (["native-target"] if network else []),
                "scope_note": (
                    "Full-corpus diagnostic, not a focused pass."
                    if network
                    else "Exact focused target, except the documented corpus cache-filename preflight."
                ),
            }
        )
        evidence.append(
            local_evidence(
                "check-" + name,
                "validation",
                str((SCRATCH / (name + ".json")).relative_to(ROOT)),
                f"Command, environment and stdout/stderr hashes; {receipt['started_at']} through {receipt['finished_at']}",
                summary,
            )
        )
    checks += [
        {
            "check_id": "source-identity",
            "name": "Primary bibliographic identity",
            "status": "passed",
            "required": True,
            "summary": "Fresh PMID, DOI, title and complete abstract agree.",
            "target_ids": [ID],
            "evidence_ids": ["pubmed", "epmc", "crossref"],
        },
        {
            "check_id": "scientific-source",
            "name": "Full primary source and critical supplements",
            "status": "unavailable",
            "required": True,
            "summary": "Critical full Methods/Results, figures, SI and model inputs remain inaccessible through inspected routes; only direct abstract support is certified.",
            "target_ids": [ID],
            "evidence_ids": [
                "source-scope",
                "access-publisher",
                "access-article-api",
                "access-openalex",
            ],
        },
        {
            "check_id": "cross-mech",
            "name": "Medium and archive correspondence",
            "status": "not_applicable",
            "required": False,
            "summary": "No exact recipe or accession can be established from inspected source scope; no guessed cross-repository link.",
            "target_ids": [ID],
            "evidence_ids": ["resources"],
        },
        {
            "check_id": "structured-adapter",
            "name": "Structured expression dataset coverage",
            "status": "not_applicable",
            "required": False,
            "summary": "Public iModulonDB catalogue has no exact Brocadia or Kuenenia dataset; no component lookup or inference is warranted.",
            "target_ids": [ID],
            "evidence_ids": ["adapter"],
        },
    ]
    review["checks"], review["evidence"] = checks, evidence
    assessments = {x["assessment_id"]: x for x in review["assessments"]}
    assessments["node-0"].update(
        outcome="concern",
        summary="The Brocadia model-complementarity claim remains appropriately qualified, but the new Kuenenia participant is supported only for temporal succession.",
        details="The COMMUNITY_LEVEL CROSS_FEEDING participant list now credits both genera. The exact new quotation establishes replacement, while the model sentence explicitly identifies a multispecies Brocadia assemblage. Retain the supported model node but narrow its participant scope or obtain direct primary/model evidence for Kuenenia. This is an evidence-scope gap, not a claim that the inaccessible full article disproves Kuenenia exchange. No downstream arrows are encoded or requested.",
        evidence_ids=["model", "succession", "record", "schema", "delta"],
    )
    assessments["history"].update(
        summary="The original outcome-placement finding persists; the new participant history is descriptive provenance and does not independently prove exchange.",
        details="Three append-only sidecars and the changed inline history were read. The Stage 5 structural network resolution remains context, not source evidence. Snippet replay finds 10 exact-normalized abstract occurrences, one co-occurrence hyphen variant and two metadata identifiers. The hyphen variant is typographical and no full-text verification is claimed.",
        evidence_ids=["history", "delta", "snippets"],
    )
    assessments["validation"][
        "summary"
    ] = "Eight focused native checks and all four unique ontology pairs pass. Current corpus diagnostics retain 44 warnings across 16 of 508 records; target structural completeness cannot validate the new cross-feeding participant."
    metrics = assessments["metrics"]["metrics"]
    for metric in metrics:
        if metric["name"] == "P2":
            metric["value"] = 1
        if metric["name"] == "validation_quality":
            metric["definition"] = (
                "clamp(100 − 50P1 − 10P2 − 2P3 + 20 min(mean node evidence/2, 1) + 15 if COMPLETE, 0, 100). P1=0, P2=1, P3=1, P4=0; two evidence items / one node gives 20, native COMPLETE gives 15; raw 123, capped 100. This does not certify scientific scope."
            )
    review["assessments"].extend(
        [
            {
                "assessment_id": "current-delta",
                "area": "provenance",
                "topic": "Frozen-input refresh",
                "outcome": "concern",
                "summary": "Changed participant scope is reassessed against current record bytes and freshly retrieved primary abstract; unchanged original findings retain exact lineage.",
                "target_ids": [ID],
                "evidence_ids": ["delta", "record", "succession", "model"],
                "details": "The prior target hash 227362963f3008129281c29d08829d1bf49aa57230b126cc7986e592c6cd9a96 differs from current 0ea86ed4c4587ff6d6fcc424c9bf2a27163154962b8430576b2a6fd4bfb1b36c. The early 25.6%–38.8% expression response and succession quotation are supported; using that temporal evidence to credit Kuenenia as a cross-feeding participant is not established at accessible source scope.",
            },
            {
                "assessment_id": "grouped-context-correction",
                "area": "provenance",
                "topic": "Bounded 447-only correction of grouped review identifier/context",
                "outcome": "supported",
                "summary": "The Stage 4 grouped descriptions name 447's Kuenenia as NCBITaxon:174636; the original and current target actually encode genus NCBITaxon:380738, confirmed by fresh NCBI authority.",
                "target_ids": [ID],
                "evidence_ids": ["history", "ncbi", "record", "delta", "native-target"],
                "details": "Exact locators: reviews/structured/20261021T101000Z-stage4-record-deep-audit/review.yaml and reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml, finding_id stage4-disconnected-syncom-participants, issue_key communitymech-stage4-disconnected-syncom-participants, description's 447 clause. This corrects only that identifier/context. The corresponding 20261021T193000Z-stage5-remediation-verification resolved disposition is retained for structural connectivity. The other four targets (000339, 000399, 000415, 000433) and their dispositions are NOT reassessed. No grouped issue key or previous_occurrences is reused to retire the five-target finding; the new participant-evidence finding is distinct.",
            },
        ]
    )
    finding = review["findings"][0]
    finding["previous_occurrences"] = [
        {"repository": REPOSITORY, "review_id": old["review_id"], "finding_id": "outcome-placement"}
    ]
    finding["normalization_reason"] = (
        "P3: unchanged bounded field placement; numerical outcomes remain supported at abstract scope. The new participant-scope issue is tracked separately."
    )
    owner = [{"repository": REPOSITORY, "path": TARGET, "role": "canonical_record"}]
    review["findings"].append(
        {
            "finding_id": "kuenenia-cross-feeding-scope",
            "issue_key": "cm-000447-kuenenia-cross-feeding-scope",
            "category": "evidence",
            "severity": "major",
            "native_severity": "P2",
            "normalization_reason": "P2: adding a taxon to CROSS_FEEDING participants materially broadens the mechanistic claim beyond the attached temporal-succession evidence.",
            "rule_id": "review-checklist.interaction-participants-and-evidence",
            "status": "open",
            "certainty": "confirmed",
            "title": "Keep Kuenenia succession distinct from Brocadia model-inferred cross-feeding",
            "description": "ecological_interactions[0].participating_taxa[1] newly credits early-acclimation Kuenenia as part of a CROSS_FEEDING interaction. The new evidence[0] quotation supports temporal replacement by Brocadia, while evidence[1] and the freshly inspected abstract place model-inferred complementary auxotrophies within a multispecies Brocadia assemblage. Succession and downregulated biosynthesis do not establish Kuenenia metabolite exchange. This is a confirmed support/scope gap in the encoded assertion at inspected abstract scope, not a demonstration that unread full-source evidence excludes Kuenenia exchange.",
            "target_ids": [ID],
            "field_paths": [
                "ecological_interactions[0].participating_taxa[1]",
                "ecological_interactions[0].description",
                "ecological_interactions[0].evidence[0]",
            ],
            "evidence_ids": ["record", "schema", "succession", "model", "delta"],
            "owner_paths": owner,
        }
    )
    review["actions"].extend(
        [
            {
                "action_id": "repair-participant-scope",
                "description": "Separate the temporal succession claim from participation in Brocadia model-inferred complementarity.",
                "finding_ids": ["kuenenia-cross-feeding-scope"],
                "target_ids": [ID],
                "owner_paths": owner,
                "acceptance_checks": [
                    "Retain Kuenenia in the temporal community taxonomy and preserve the supported early-acclimation and succession narrative.",
                    "Restrict CROSS_FEEDING participants to the directly supported multispecies Brocadia assemblage unless directly inspected primary/model evidence explicitly establishes Kuenenia participation; attach that evidence to the precise assertion if recovered.",
                    "Place temporal replacement context separately from the exchange claim, retaining source qualifiers and the distinct 25.6%–38.8% early response. Do not fabricate an interaction or leave participating_taxa empty merely to make network connectivity pass (empty means all members).",
                    "Preserve COMPUTATIONAL evidence and SMETANA provenance. Do not assert measured transfer, obligatory dependence, species/MAG identity or a model source not verified from the primary material.",
                    "After separately authorized curation, add append-only history, run focused schema/strict/term/reference/history checks, and explain any remaining temporal-membership network warning without weakening the gate.",
                ],
            },
            {
                "action_id": "follow-up-primary-methods-and-model-identities",
                "description": "Track the existing brocadia_low_nitrogen_species_resolution discussion as an access-limited curation follow-up, distinct from the two graded record findings.",
                "finding_ids": [],
                "target_ids": [ID],
                "owner_paths": owner,
                "acceptance_checks": [
                    "When accessible, directly inspect the focal Methods, figures, supplements and model/data availability for exact Brocadia species/MAG identifiers, reactor geometry, feed nitrogen/loading and SMETANA genome/model sources; retain precise source locators and versions.",
                    "Curate only verified focal-system values and identities with claim-local evidence. Do not promote indexed publisher snippets, generic influent ranges or other-study species examples into this record.",
                    "If critical sources remain inaccessible, keep the discussion open with a bounded access-status update; do not invent values or require new experiments.",
                    "Do not change partial scientific status until the actual critical source material has been inspected and any newly supported corrections pass native checks.",
                ],
            },
        ]
    )
    review["limitations"] = [
        "Critical full main Methods/Results, figures, SI, species/MAG identities, model construction and exact reactor settings remain unavailable through the inspected public routes. This is an abstract-scope partial review, not whole-source scientific certification.",
        "The abstract supports temporal succession, distinct transcriptional/abundance outcomes and SMETANA-predicted Brocadia complementarity. It does not directly measure inter-genus metabolite exchange, donor-recipient flux, obligate dependence or carbon fixation. The new participant finding is bounded to support currently inspected, not a claim about unread source content.",
        "Indexed publisher Methods fragments are access leads only. Direct page requests returned 403; no reactor scale, volume, configuration, feed concentration or species identity is accepted from those snippets.",
        "No figure inspection, raw omics inspection, simulation or isotope/flux reanalysis was performed. No guessed genome accession, model source, strain or medium link is supplied.",
        "Both documented corpus network diagnostics exit 1 with 44 warnings and zero errors across 16 of 508 records. The focal target is structurally COMPLETE; that mechanical result does not validate scientific participation.",
        "The grouped Stage 4/5 lineage is context only. Only the 447 identifier and current scientific scope are assessed; the other four targets and grouped resolved dispositions are not reassessed or superseded.",
        "Bounded unsuccessful access or catalogue discovery does not establish global absence. No paid provider, contact, authentication bypass or GitHub mutation was used. The author pass does not claim independent approval.",
    ]
    review["notes"] = [
        "Canonical, cache, history, schema, generated products and existing review bundles remain unchanged. The final native inspection verifies all earlier pinned inputs before adding fresh source, receipt and frozen helper pins.",
        "13 snippet occurrences: 10 strict NFKC/whitespace abstract matches, one hyphen-only equivalent and two metadata identifiers. Four unique ontology pairs occur six times; both taxa are genera.",
        "Completeness 70 and quality 100 (raw 123) are mechanical metrics, not scientific certification. One P2 and one P3 remain open; completion is partial and scientific_review is false.",
        "The original single-target outcome-placement finding has exact previous_occurrences. The five-target group key is not superseded by this narrower record observation.",
    ]
    review["related_reviews"] = [
        {
            "repository": REPOSITORY,
            "review_id": row["review_id"],
            "relationship": (
                "Immutable current-input successor retaining the original open outcome-placement finding."
                if row["review_id"] == old["review_id"]
                else "447-only grouped context and identifier clarification; no multi-target disposition supersession."
            ),
        }
        for row in load("lineage.json")
    ]
    review["finished_at"] = now()
    candidate = write("candidate-v3.json", review)
    result = run(
        "candidate-validate-v3",
        ["uv", "run", "python", "scripts/record_review.py", "validate", str(candidate)],
    )
    assert result.returncode == 0, result.stderr.decode()
    print(json.dumps({"candidate": str(candidate), "review_id": review_id}))


def save():
    result = run(
        "native-save",
        [
            "uv",
            "run",
            "python",
            "scripts/record_review.py",
            "save",
            "--content",
            str(SCRATCH / "candidate-v3.json"),
        ],
    )
    assert result.returncode == 0, result.stderr.decode()
    print(result.stdout.decode())
    for name in ["check-record-reviews", "test-record-reviews"]:
        result = run(name, ["just", "--no-dotenv", name])
        assert result.returncode == 0, result.stderr.decode()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["build", "save"])
    args = parser.parse_args()
    {"build": build, "save": save}[args.mode]()
