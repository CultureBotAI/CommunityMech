"""Author the one-record 000122 scientific reassessment, 2026-11-15.

Inputs: accepted applied candidate, exact primary/supplement/grounding inputs,
nine native receipts and actual assertion counts. Outputs: exclusive private
inspection/review and public metadata-only application proof. Serves #1548,
#2814/#2815 and integration lineage #2816. No canonical/cache/history writes.
Scientific judgments below are authored, not inferred from technical scores.
"""

import argparse
import hashlib
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
from check_gut_record_20261115 import BASE, GATES, HISTORY, STATE, TARGET  # noqa: E402
from curate_gut_record_20261115 import BEFORE, load  # noqa: E402

IDENTIFIER = "CommunityMech:000122"
REPO = "CultureBotAI/CommunityMech"
PAPER = "https://pmc.ncbi.nlm.nih.gov/articles/PMC6011841/"
AFTER = "d0beaaa1d74383d9b6c81fafe5a70cae23eae00ae706f38fa10d78f874504dce"
PREVIOUS = "20261115T025108Z-phase2-gut-completion"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or not output.is_relative_to(STATE):
        raise ValueError("exclusive private output required")
    applied_path = STATE / "applied-001/receipt.json"
    applied = json.loads(applied_path.read_bytes())
    record = load((ROOT / TARGET).read_bytes())
    if (
        not applied["applied"]
        or applied["before_sha256"] != BEFORE
        or applied["after_sha256"] != AFTER
        or sha(ROOT / TARGET) != AFTER
    ):
        raise ValueError("actual reviewed application chain differs")
    for path, expected in applied["inputs"].items():
        if sha(ROOT / path) != expected:
            raise ValueError("applied source changed: " + path)
    if (
        record["id"] != IDENTIFIER
        or len(record["taxonomy"]) != 12
        or len(record["treatment_arms"]) != 13
    ):
        raise ValueError("assessed roster/arms changed")
    receipts = {}
    for gate in (*GATES, "references", "network"):
        name = "canary-" + gate + "-applied-001"
        receipt = json.loads((STATE / (name + ".json")).read_bytes())
        if (
            receipt["head"] != BASE
            or receipt["gate"] != gate
            or receipt["status"] != "PASSED"
            or receipt["exit_code"] != 0
            or not receipt["inputs_unchanged"]
        ):
            raise ValueError("required gate not complete: " + gate)
        if (
            (STATE / (name + ".exit")).read_text().strip() != "0"
            or sha(ROOT / receipt["log"]) != receipt["log_sha256"]
            or not receipt["log_bytes"]
        ):
            raise ValueError("gate log/exit changed: " + gate)
        if any(sha(ROOT / path) != digest for path, digest in receipt["inputs"].items()):
            raise ValueError("gate input changed: " + gate)
        if receipt["record"] != TARGET or receipt["record_worktree_sha256"] != AFTER:
            raise ValueError("gate target differs")
        expected = GATES.get(gate)
        if gate == "strict":
            expected = expected + ["--out", str((STATE / (name + ".tsv")).relative_to(ROOT))]
        if gate == "terms":
            expected = [
                "uv",
                "run",
                "--no-sync",
                "linkml-term-validator",
                "validate-data",
                TARGET,
                "-s",
                "src/communitymech/schema/communitymech.yaml",
                "--labels",
                "--config",
                str((STATE / (name + "-oak.yaml")).relative_to(ROOT)),
                "--cache-dir",
                str((STATE / (name + "-labels")).relative_to(ROOT)),
            ]
        if gate == "references":
            expected = [
                "uv",
                "run",
                "--no-sync",
                "linkml-reference-validator",
                "validate",
                "data",
                TARGET,
                "-s",
                "src/communitymech/schema/communitymech.yaml",
                "--config",
                "conf/reference_validator.yaml",
                "--cache-dir",
                str((STATE / (name + "-cache")).relative_to(ROOT)),
                "--no-full-text",
            ]
            if not receipt["private_cache_unchanged"]:
                raise ValueError("private source copy changed")
        if gate == "network":
            expected = [
                "uv",
                "run",
                "--no-sync",
                "communitymech",
                "audit-network",
                "--communities-dir",
                str((STATE / (name + "-records")).relative_to(ROOT)),
                "--json",
            ]
            if (
                json.loads((ROOT / receipt["log"]).read_text()) != {}
                or receipt["private_record_sha256"] != AFTER
            ):
                raise ValueError("scoped network output differs")
        if receipt["command"] != expected:
            raise ValueError("native invocation differs: " + gate)
        receipts[gate] = receipt
    measurement_path = STATE / "measured-applied-001/receipt.json"
    measurement = json.loads(measurement_path.read_bytes())
    if (
        not measurement["measurement_valid"]
        or not measurement["inputs_unchanged"]
        or measurement["record_sha256"] != AFTER
        or measurement["assertion_status_counts"] != {"matched": 43, "unannotated_excerpt": 1}
    ):
        raise ValueError("actual assertion measurement differs")
    inputs = {
        TARGET,
        "uv.lock",
        "justfile",
        "docs/record-review-profile.md",
        "docs/record-reviews.md",
        "conf/record_review.yaml",
        "conf/reference_validator.yaml",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "src/communitymech/schema/history.yaml",
        ".claude/skills/curate-yaml-record/SKILL.md",
        ".claude/skills/curate-yaml-record/references/review-checklist.md",
        ".claude/skills/review-communities/reference/metrics-and-reports.md",
        "references_cache/PMID_29930200.txt",
        "references_cache/pmc_full_pmid_29930200.txt",
        "reports/causal_graph_review/decisions/20261006-lbnl-batch61.yaml",
    }
    inputs.update(applied["inputs"])
    inputs.update(str(path.relative_to(ROOT)) for path in (ROOT / HISTORY).glob("*.yaml"))
    inputs.update(
        str(path.relative_to(ROOT)) for path in (ROOT / "scripts/adhoc").glob("*gut*20261115.py")
    )
    for pattern in (
        "canary-*-applied-001.json",
        "canary-*-applied-001.log",
        "canary-*-applied-001.exit",
        "canary-*-applied-001.tsv",
        "canary-*-applied-001-oak.yaml",
        "supplement-*-cells.json",
    ):
        inputs.update(str(path.relative_to(ROOT)) for path in STATE.glob(pattern))
    for folder in ("applied-001", "candidate-002", "measured-applied-001"):
        inputs.update(
            str(path.relative_to(ROOT)) for path in (STATE / folder).iterdir() if path.is_file()
        )
    inputs.add(f"reviews/structured/{PREVIOUS}/review.yaml")
    inputs.add(".temp/phase2-gut-20261115/review-005-builder.py")
    output.mkdir()
    target_manifest = yaml.safe_load((STATE / "targets.yaml").read_text())
    target_manifest["targets"][0]["kind"] = "maintained"
    targets_path = output / "targets.yaml"
    targets_path.write_text(yaml.safe_dump(target_manifest, sort_keys=False))
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(targets_path),
    ]
    for path in sorted(inputs):
        command.extend(["--input", path])
    inspected_raw = subprocess.check_output(command, cwd=ROOT, text=True)
    (output / "inspection.json").write_text(inspected_raw)
    inspected = json.loads(inspected_raw)
    finished = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    evidence, assessments, checks = [], [], []

    def ev(key, kind, reference, locator, summary, path=None, quote=None, support="supports"):
        row = {
            "evidence_id": key,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "accessed_at": finished,
            "support": support,
            "summary": summary,
        }
        if path:
            row["snapshot_sha256"] = sha(ROOT / path)
        if quote:
            row["quote"] = quote
        evidence.append(row)

    def assess(key, area, topic, summary, refs, fields=None, outcome="supported"):
        row = {
            "assessment_id": key,
            "target_ids": [IDENTIFIER],
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "evidence_ids": refs,
        }
        if fields:
            row["details"] = "Exact current fields: " + ", ".join(fields)
        assessments.append(row)
        return row

    xml = str((STATE / "primary-001/article.xml").relative_to(ROOT))
    ev(
        "record",
        "record_content",
        TARGET,
        "Entire current record",
        "Twelve stocks, thirteen intended arms, three model-bounded graph nodes, one directed downstream model link, two discussions and append-only history were assessed.",
        path=TARGET,
    )
    ev(
        "primary",
        "primary_source",
        PAPER,
        "Complete main text: Methods, Results, Discussion and all figure captions",
        "Primary study distinguishes inferred effective ecological coefficients from molecular mechanism; source protocols and exact stock roster were read.",
        path=xml,
    )
    ev(
        "methods",
        "primary_source",
        PAPER,
        "Methods: strains/media, time-series measurements, 16S and metabolomics protocols",
        "Twelve deposited stocks; slow six 41h starters versus fast six 16h; static deep-well37°C community culture; 24h1:20 transfers; shaken384-well optical-density aliquot; ER/FP33mM acetate metabolomics is a separate protocol.",
        path=xml,
        quote="Serial transfers were performed at 24‐h intervals into fresh media using a 1:20 dilution.",
    )
    ev(
        "grounding",
        "database",
        str((STATE / "grounding-roster-002.json").relative_to(ROOT)),
        "Readonly NCBI species labels/ranks/synonyms and native retained crosswalk",
        "All12 current species labels checked;10 GTDB grounds, CA unresolved and PC ambiguous. Species-level mapping is not this stock's genome placement.",
        path=str((STATE / "grounding-roster-002.json").relative_to(ROOT)),
        support="context_only",
    )
    ev(
        "environment",
        "database",
        str((STATE / "environment-authority-001.json").relative_to(ROOT)),
        "Exact readonly ENVO label assertions",
        "ENVO01001405 laboratory environment is physical; ENVO2100002 intestine environment is modeled, not a collected host sample.",
        path=str((STATE / "environment-authority-001.json").relative_to(ROOT)),
        support="context_only",
    )
    ev(
        "fp-catalog",
        "database",
        "https://www.dsmz.de/collection/catalogue/details/culture/DSM-17677",
        "DSM17677/A2-165 catalogue nomenclatural note",
        "Catalogue explicitly records former F.prausnitzii reassignment to F.duncaniae in May2022. Historical source abbreviation FP is retained.",
        path=str((STATE / "dsm17677-catalog-001/catalog.html").relative_to(ROOT)),
    )
    for number, key, description in [
        (
            1,
            "appendix",
            "All Appendix captions and relevant panels S21/S24/S25-S26 inspected; pairwise/conditioned-medium/metabolomic limitations retained.",
        ),
        (
            2,
            "ev1",
            "All workbook cell/formula text retained and Description inspected: time-series mean relative species abundance for PW1 (Fig2A); not optical density.",
        ),
        (
            3,
            "ev2",
            "All workbook cell/formula text retained and Description inspected: time-series mean relative species abundance for PW2 (Fig2B).",
        ),
        (
            4,
            "ev3",
            "All workbook cell/formula text retained: source species order and full NONE plus12 named dropout arms, with abundance timepoints kept separate.",
        ),
        (
            5,
            "ev4",
            "All workbook cell/formula text retained and97 metabolite names inspected; no direct stock-to-stock transfer demonstrated by extracellular changes.",
        ),
        (
            6,
            "code",
            "All four SBML filenames inspected; T3 CH/ER coefficients inspected, aCHER=-0.5077 and aERCH=1.1905 with recipient-first convention. Model was not executed.",
        ),
        (
            7,
            "review-process",
            "Relevant reviewer/author clarifications about CFU calibration and acetate protocol inspected; not every page of the29-page review process was read.",
        ),
    ]:
        folder = STATE / f"publisher-supplement-{number:02d}"
        source = next(path for path in folder.iterdir() if path.name.startswith("44320_"))
        ev(
            key,
            "primary_source",
            "https://link.springer.com/article/10.15252/msb.20178157#Sec24",
            source.name,
            description,
            path=str(source.relative_to(ROOT)),
            support="context_only",
        )
    ev(
        "figure4",
        "primary_source",
        PAPER,
        "Figure4B/C image, caption and Results network-motif analysis",
        "Actual pixels show positive CH-to-ER limb and reverse inhibitory ER-to-CH limb; a two-member gLV motif, not all12 members or a molecular mediator.",
        path=str((STATE / "primary-001/figure4.png").relative_to(ROOT)),
    )
    ev(
        "applied",
        "record_content",
        str(applied_path.relative_to(ROOT)),
        "Actual applied=true receipt, externally reviewed candidate and receipt hashes",
        "Exact baseline aa025332 to d0beaaa1 application; native closed-schema roundtrip and post-validation source/concurrency rechecks. Original history preserved.",
        path=str(applied_path.relative_to(ROOT)),
    )
    ev(
        "measured",
        "validation",
        str(measurement_path.relative_to(ROOT)),
        "Actual native CLI traversal/matcher counters with no acquisition adapter",
        "44 surfaces:43 actual comparisons/matches and1 unannotated SupportingReference. Zero native issues is not44 checks or complete assertion coverage; all inputs unchanged.",
        path=str(measurement_path.relative_to(ROOT)),
        support="context_only",
    )
    for gate, receipt in receipts.items():
        ev(
            "check-" + gate,
            "validation",
            receipt["log"],
            "Fresh completed native command, exit and immutable input binding",
            "Scoped technical check passed; this does not prove source truth or full repository QC.",
            path=receipt["log"],
            support="context_only",
        )
        checks.append(
            {
                "check_id": gate,
                "name": "Native " + gate,
                "status": "passed",
                "required": True,
                "summary": "Fresh exact applied-record native check passed.",
                "target_ids": [IDENTIFIER],
                "command": shlex.join(receipt["command"]),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + gate],
            }
        )
    checks.append(
        {
            "check_id": "manual-science",
            "name": "Full current-record source and scope assessment",
            "status": "passed",
            "required": True,
            "summary": "Each current stock, arm, graph node/link and protocol claim assessed; pass means assessment performed, not all mechanisms known.",
            "target_ids": [IDENTIFIER],
            "evidence_ids": ["primary", "methods", "figure4", "grounding", "ev3", "ev4"],
        }
    )
    assess(
        "identity",
        "scope",
        "Represented community and habitats",
        "Defined12-stock laboratory human-gut model, not an in-vivo host consortium. Physical laboratory and modeled intestine terms are separately grounded; no source habitat or host phenotype is invented.",
        ["record", "primary", "environment"],
        [
            "description",
            "ecological_state",
            "community_origin",
            "community_category",
            "environment_term",
            "modeled_environment",
            "engineering_design",
        ],
    )
    grounding = json.loads((STATE / "grounding-roster-002.json").read_bytes())
    for index, item in enumerate(grounding["rows"]):
        assess(
            "stock-" + item["member_id"].lower(),
            "grounding",
            item["member_id"] + " stock and current species identity",
            f"Methods source {item['source_name']}, {item['collection']} {item['accession']}; current term {item['term']['id']} {item['term']['label']}. Exact source designation retained. Starter duration {item['starter_incubation_hours']}h is not community duration. GTDB uses aggregate named-species genomes, not a verified individual-stock genome; no unsupported function/type status assigned.",
            ["methods", "grounding"] + (["fp-catalog"] if item["member_id"] == "FP" else []),
            [f"taxonomy[{index}]"],
        )
    assess(
        "arms",
        "scope",
        "All13 intended full/single-dropout assemblages",
        "Source full plus all12 single-species dropout designs map to explicit member IDs. Every dropout contains the other11 intended stocks and names full as comparator. BU late contamination at47.5h0.4% and72h2% is explicitly qualified; intended membership is not immutable realized composition. No values from different times, replicates or assay bases are pooled into scalar abundance.",
        ["primary", "ev3", "appendix", "record"],
        ["treatment_arms"],
    )
    assess(
        "protocols",
        "scope",
        "Separate starter, community, OD assay and metabolomics protocols",
        "41/16h15mL starters are not deep-well working volume. Static37°C deep-well cultures undergo daily1:20 transfers for72h; vocabulary OTHER states serial transfer precisely without inventing continuous/draw-fill operation. Parallel384-well shaken OD and 16S×OD proxy differ from viable counts. ER/FP33mM acetate metabolomics and separate CFU calibration are not the standard whole-community medium.",
        ["methods", "appendix", "review-process"],
        ["growth_media", "cultivation_setup", "engineering_design", "environmental_factors"],
    )
    assess(
        "node-0",
        "scope",
        "Pairwise-trained model prediction of community dynamics",
        "Three training tiers distinguish mono/pairwise inputs from later full-community information. Prediction supports important pairwise effective effects for tested11/12-member assemblages, not perfect generalization, absence of higher-order interactions or acetate transfer. The12 explicit participating stocks denote the represented network population; no directed molecular source/target is assigned.",
        ["primary", "record", "ev1", "ev2"],
        ["ecological_interactions[0]"],
    )
    assess(
        "node-1",
        "scope",
        "Signed effective network topology",
        "Frequent positive/negative gLV coefficients inferred from abundance dynamics describe effective signs over the12-stock network. They do not uniquely establish competition, cross-feeding, niche partitioning or named molecular mediators; conditioned-medium/metabolomics concordance is incomplete.",
        ["primary", "appendix", "ev4", "record"],
        ["ecological_interactions[1]"],
    )
    assess(
        "node-2-edge",
        "scope",
        "CH/ER pair feedback and sole downstream link",
        "Figure4B/C and T3 coefficients support positive CH(Peptacetobacterhiranonis DSM13275)→ER(Agathobacterrectalis ATCC33656) and reverse inhibition. Source/target fields encode positive limb and prose states coupled reverse limb. Sole topology→coexistence edge is a model-bounded pairwise mechanism across tested growth-rate regimes; it is not12-member feedback or observed molecular transfer. Exact organism attribution was narrowed after independent finding2815.",
        ["figure4", "code", "primary", "record"],
        ["ecological_interactions[2]", "ecological_interactions[1].downstream[0]"],
    )
    assess(
        "mediators",
        "evidence",
        "Molecular mechanism and acetate separation",
        "Prior-literature acetate example, supplied acetate in ER/FP metabolomics, extracellular depletion/secretion and conditioned-medium responses do not demonstrate a direct stock-to-stock transfer. Unsupported acetate ingredient/CROSS_FEEDER assertion removed. Both discussions preserve unanswered molecular questions; October wording is a dated historical assessment, not a claim about the new review's inspected sources.",
        ["primary", "ev4", "methods", "review-process", "record"],
        ["discussions", "related_ingredients"],
        outcome="concern",
    )
    assess(
        "history",
        "provenance",
        "Append-only actual curation lineage",
        "Externally reviewed dual hashes bound the actual application and post-native source rechecks. Original inline history remains; a new sidecar accidentally inherited actor-name claude-code while model/tool werecodex, and a separate immutable GENERAL entry corrects that toCodex without altering the original.",
        ["applied", "check-history"],
        ["curation_history"],
    )
    assess(
        "coverage",
        "evidence",
        "Actual comparisons versus yielded issue count",
        "Applied current record has43 matching EvidenceItem comparisons plus1 unannotated discussion SupportingReference. Manual source assessment covers its claim; automated coverage remains incomplete under476 until canonical Claw change is governed downstream. No historical measurement is relabeled44/44.",
        ["measured", "primary", "check-references"],
        ["discussions[1].evidence[0]"],
        outcome="concern",
    )
    owner = {"repository": REPO, "path": TARGET, "role": "canonical_record"}
    ev(
        "prior-metadata",
        "prior_review",
        f"reviews/structured/{PREVIOUS}/review.yaml",
        "Immutable predecessor evidence item ev1 and source.inputs",
        "Issue2819: predecessor mislabeled EV1 as OD data and omitted three derived cell extracts from its inputs. The four original workbooks and canonical record were correctly bound. This successor corrects report metadata, retains all source boundaries and changes no scientific record.",
        path=f"reviews/structured/{PREVIOUS}/review.yaml",
        support="context_only",
    )
    assess(
        "metadata-correction",
        "provenance",
        "Corrected supplement description and complete retained-extract inventory",
        "EV1 is PW1 relative species abundance; EV2 is PW2 relative species abundance; EV3 is multi-species relative abundance; EV4 is monospecies metabolite log2 fold change. All four original workbooks and derived extracts are bound here. Prior saved bundle and exact authoring helper snapshot are preserved; its canonical application and nine native gate results are unchanged.",
        ["prior-metadata", "ev1", "ev2", "ev3", "ev4"],
    )
    findings = []

    def finding(key, title, description, refs, fields, status="open", priority="P3", issue=1548):
        if status == "resolved":
            # These corrections predate this first record-specific saved bundle.
            # Never invent a predecessor finding to manufacture a closed lineage.
            assess("correction-" + key, "evidence", title, description, refs, fields)
            return
        findings.append(
            {
                "finding_id": key,
                "issue_key": "cm-000122-" + key,
                "category": "evidence",
                "severity": "major" if priority == "P2" else "minor",
                "native_severity": priority,
                "normalization_reason": "Material assertion-scope defects areP2; explicit remaining source/tool uncertainty isP3 and is not evidence of a false current assertion.",
                "rule_id": "review-checklist.claim-specific-support-and-context",
                "status": status,
                "certainty": "confirmed",
                "title": title,
                "description": description,
                "target_ids": [IDENTIFIER],
                "field_paths": fields,
                "owner_paths": [owner],
                "evidence_ids": refs,
                "external_issues": [
                    f"https://github.com/CultureBotAI/CommunityMech/issues/{issue}"
                ],
                **(
                    {
                        "disposition_reason": "Independent source/guard review accepted candidate002; its exact reviewed bytes were applied with native validation and fresh scoped gates. Broader parent issues remain open."
                    }
                    if status == "resolved"
                    else {}
                ),
            }
        )

    finding(
        "roster-protocol",
        "Twelve-stock roster and serial-transfer scope corrected",
        "Aggregate domain/CROSS_FEEDER placeholder replaced by exact Methods stocks. Static deep-well versus shakenOD,41/16h starters and daily1:20 transfer protocols separated; acetate is no longer claimed as the community mediator. This resolves only the000122 portion of broader1548, not the whole issue.",
        ["methods", "grounding", "fp-catalog", "applied"],
        ["taxonomy", "cultivation_setup", "growth_media"],
        "resolved",
        "P2",
    )
    finding(
        "pairwise-feedback",
        "Pairwise feedback participant expansion corrected before application",
        "Rejected staged candidate001 attributed all12 stocks to the CH/ER motif; accepted/applied candidate002 instead restricts the modeled pair with explicit sign/direction and source evidence.",
        ["figure4", "code", "applied"],
        ["ecological_interactions[2]"],
        "resolved",
        "P2",
        2815,
    )
    finding(
        "molecular-mechanism",
        "Direct stock-specific metabolite transfer remains unproven",
        "Main paper/supplements nominate possible mechanisms but do not resolve direct molecular transfers for inferred signed effects. Keep the graph model-bounded and the discussion open; no fabricated acetate-mediated interaction.",
        ["primary", "ev4", "methods"],
        ["discussions", "ecological_interactions"],
    )
    finding(
        "stock-genome",
        "Two GTDB mappings and individual-stock genomes remain unresolved",
        "CA has no retained crosswalk mapping; PC has two candidate GTDB species. Other10 species-level mappings do not identify the exact study-stock genome. No speculative lineage or accession is filled.",
        ["grounding", "methods"],
        ["taxonomy"],
    )
    finding(
        "discussion-coverage",
        "One SupportingReference is not automatically compared under old schema",
        "Actual native measurement is43 matched/1 unannotated, not44 passed. Canonical Claw annotation repair and governed downstream pin are pending integration; this source claim was manually inspected.",
        ["measured", "primary"],
        ["discussions[1].evidence[0]"],
        issue=476,
    )
    actions = [
        {
            "action_id": "followup-" + item["finding_id"],
            "description": item["description"],
            "finding_ids": [item["finding_id"]],
            "target_ids": [IDENTIFIER],
            "owner_paths": [owner],
            "acceptance_checks": [
                "Resolve the named uncertainty using inspected primary evidence or governed annotation integration; retain explicit uncertainty if unsupported."
            ],
        }
        for item in findings
        if item["status"] == "open"
    ]
    for item in findings:
        item["previous_occurrences"] = [
            {"repository": REPO, "review_id": PREVIOUS, "finding_id": item["finding_id"]}
        ]
    nodes = record["ecological_interactions"]
    evidence_count = sum(len(node.get("evidence", [])) for node in nodes)
    completeness = (
        5
        + (10 if len(record.get("environmental_factors", [])) >= 3 else 0)
        + (10 if len(nodes) >= 3 else 0)
        + (5 if record.get("external_resources") else 0)
        + (10 if record.get("growth_media") else 0)
        + (5 if record.get("associated_datasets") else 0)
        + (5 if any("metabolites" in node for node in nodes) else 0)
    )
    counts = {
        level: sum(
            item["status"] == "open" and item["native_severity"] == level for item in findings
        )
        for level in ("P1", "P2", "P3", "P4")
    }
    average = evidence_count / len(nodes)
    quality = max(
        0,
        min(
            100,
            100
            - 50 * counts["P1"]
            - 10 * counts["P2"]
            - 2 * counts["P3"]
            + min(average / 2, 1) * 20
            + 15,
        ),
    )
    metrics = assess(
        "metrics",
        "completeness",
        "Literal native completeness and validation-quality scores",
        "Missing functional roles are not invented to raise completeness. Formula bonuses can saturate quality despite open scientific/tool gaps; the score is not scientific approval or a release verdict.",
        ["record", "check-network", "measured"],
    )
    metrics["metrics"] = [
        {
            "name": "completeness",
            "value": completeness,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "Native rubric: required-member-role block0; environment5; at least3factors10 ifpresent; at least3nodes10; externalresources5 ifpresent; growthmedia10; datasets5 ifpresent; node-metabolites5 ifpresent.",
        },
        {
            "name": "validation_quality",
            "value": quality,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": f"Native clip(100-50P1-10P2-2P3+min((evidence/nodes)/2,1)*20+15 network) with {counts}, evidence={evidence_count}, nodes={len(nodes)}, average={average}; scoped network complete. Saturation does not clear3open findings.",
        },
        {
            "name": "actual_compared_snippets",
            "value": 43,
            "unit": "assertions",
            "denominator": 44,
            "definition": "Actual native matching occurred for43 unique occurrences;1 unannotated occurrence excluded.",
        },
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-phase2-gut-completion",
        "kind": "record",
        "repository": REPO,
        "title": "Twelve-stock human gut SynCom source, protocol and pairwise-model reassessment",
        "started_at": "2026-11-15T02:20:27Z",
        "finished_at": finished,
        "reviewer": {
            "identity": "codex-inventory-audit",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored this curation after source inspection; parent independently accepted exact staged candidate and applied-writer guards before application.",
        },
        "skill": "curate-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Entire current000122 assessed:12stock identities,13intended arms,3model-bounded nodes/1edge and separate protocols. Nine native gates passed;43snippets actually matched and1remains unannotated. Roster/protocol and staged pairwise-scope defects corrected; molecular, stock-genome and automatic-discussion-coverage uncertainties remain explicit.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Entire one-record scientific content, every stock, arm, interaction/downstream link, medium/protocol/environment, discussion and provenance.",
            "selection": "Explicit Phase2 issue1548 target000122 following verified000087 saved-review canary; no other canonical record changed.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [IDENTIFIER],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "Full means every current record assertion assessed; it does not mean all underlying raw data, all supplemental pixels or all29peer-review pages were inspected/reanalyzed. Main paper complete text, all supplement cell/formula extracts and relevant Appendix panels were inspected; T3 coefficients were read without model execution.",
            "No individual stock genome/type status or unreported function is inferred. Only the changed DSM17677 nomenclature was independently checked in its current culture catalogue; other exact deposits are primary-source assertions plus current species authority, not independent catalog confirmation.",
            "Native lexical matching is43of44 under the unchanged old shared schema; SupportingReference remainsunannotated476. Source-access/acquisition and cache writes were refused by the measurement adapter; native gate used exact private cache copies and --no-full-text.",
            "Nine scoped gates and native review persistence do not establish full repositoryQC. Parent owns integration, new governed shared-schema pin and fresh integrated validation.",
            "The October discussion intentionally remains historical, including its then-aggregate roster and then-uninspected-source statements; the new discussion explicitly supersedes that assessment scope.",
            "Original actor-default history entry is retained; separate immutable Codex correction records the scaffolder omission. No old history/review was rewritten.",
            "The other000087/000088 portions of1548 and the wider all-record campaign remain separate. Three unresolved findings are preserved despite formula-saturated validation quality.",
        ],
        "links": [
            f"https://github.com/CultureBotAI/CommunityMech/issues/{number}"
            for number in (1548, 476, 2814, 2815, 2816, 2819)
        ],
        "related_reviews": [
            {
                "repository": REPO,
                "review_id": PREVIOUS,
                "relationship": "Corrects EV1 report metadata and binds all cell extracts; canonical record, application and native gate outcomes unchanged; preserves three open findings.",
            }
        ],
    }
    (output / "review.yaml").write_text(
        yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=106)
    )
    # Exact source receipt contains metadata/hashes only; never export raw article bodies.
    public = ROOT / "reports/phase2-gut-20261115/application-001.json"
    public.parent.mkdir(parents=True, exist_ok=True)
    proof = {
        "raw_receipt_path": str(applied_path.relative_to(ROOT)),
        "raw_receipt_sha256": sha(applied_path),
        "receipt": applied,
        "scope": "Actual canonical application metadata only; source text remains private.",
    }
    if public.exists():
        if json.loads(public.read_bytes()) != proof:
            raise ValueError("existing public application proof differs")
    else:
        with public.open("x") as stream:
            json.dump(proof, stream, indent=2)
            stream.write("\n")
    print(
        json.dumps(
            {
                "review": str((output / "review.yaml").relative_to(ROOT)),
                "review_id": review["review_id"],
                "assessments": len(assessments),
                "checks": len(checks),
                "findings": len(findings),
                "metrics": metrics["metrics"],
            }
        )
    )


if __name__ == "__main__":
    main()
