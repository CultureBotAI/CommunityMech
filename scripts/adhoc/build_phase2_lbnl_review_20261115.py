"""Author the full 000087 Phase2 canary reassessment, 2026-11-15.

Inputs: exact post-curation record, pinned primary sources/grounding, append-only
history, predecessor findings and fresh focused native receipts. Output: exclusive
staging review YAML plus native inspection; use native validate/save afterwards.
Serves #1548/#2776/#476. Scientific judgments are authored here, not inferred from
scores or matcher output. No canonical, cache, old-review or provider writes.
"""

import argparse
import copy
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
from check_phase2_lbnl_canary_20261115 import BASE, CACHES, GATES, TARGET  # noqa: E402
from curate_phase2_lbnl_canary_20261115 import INPUTS, STATE, load_document  # noqa: E402

TARGET_ID = "CommunityMech:000087"
REPOSITORY = "CultureBotAI/CommunityMech"
PRIOR_IDS = [
    "20261114T213343Z-m5-lbnl-switchgrass-completion",
    "20261114T213834Z-m5-lbnl-environment-addendum",
]
PAPER = "https://pmc.ncbi.nlm.nih.gov/articles/PMC9765266/"
RUN = "003"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--curation-receipt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="new private directory")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or not output.is_relative_to(ROOT / ".temp"):
        raise ValueError("output must be a new private directory")
    correction = json.loads(args.curation_receipt.read_bytes())
    if not correction["applied"] or correction["after_sha256"] != sha(ROOT / TARGET):
        raise ValueError("correction not applied to the assessed current bytes")
    for relative, expected in INPUTS.items():
        if sha(STATE / relative) != expected:
            raise ValueError("assessed primary/grounding input changed")
    record = load_document((ROOT / TARGET).read_bytes())
    grounding = json.loads((STATE / "lbnl-grounding-final16.json").read_bytes())
    if (
        len(record["taxonomy"]) != 16
        or record.get("ecological_interactions")
        or len(record["discussions"]) != 5
    ):
        raise ValueError("scientifically assessed target shape changed")
    # Bind every terminal receipt to exact commands, revision, current file hashes,
    # a completed exit file, and original log bytes. No prior checks are reused.
    receipts = {}
    for gate in (*GATES, "references", "network"):
        name = "canary-" + gate + "-" + RUN
        receipt_path = STATE / (name + ".json")
        receipt = json.loads(receipt_path.read_bytes())
        log = ROOT / receipt["log"]
        if (
            receipt["head"] != BASE
            or receipt["gate"] != gate
            or receipt["status"] != "PASSED"
            or receipt["exit_code"] != 0
        ):
            raise ValueError("required current native gate did not pass: " + gate)
        if (
            (STATE / (name + ".exit")).read_text().strip() != "0"
            or sha(log) != receipt["log_sha256"]
            or not log.stat().st_size
        ):
            raise ValueError("native receipt/log completion differs: " + gate)
        if not receipt["inputs_unchanged"] or any(
            sha(ROOT / name) != digest for name, digest in receipt["inputs"].items()
        ):
            raise ValueError("current input differs from native gate: " + gate)
        expected_command = GATES.get(gate)
        if gate == "strict":
            expected_command = expected_command + [
                "--out",
                str((STATE / (name + ".tsv")).relative_to(ROOT)),
            ]
        if gate == "terms":
            expected_command = [
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
            expected_command = [
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
                raise ValueError("reference cache changed")
        if gate == "network":
            expected_command = [
                "uv",
                "run",
                "--no-sync",
                "communitymech",
                "audit-network",
                "--communities-dir",
                str((STATE / (name + "-records")).relative_to(ROOT)),
                "--json",
            ]
            network = json.loads(log.read_text())
            if (
                receipt["private_record_sha256"] != sha(ROOT / TARGET)
                or network != {}
                or sorted(path.name for path in (STATE / (name + "-records")).glob("*.yaml"))
                != [Path(TARGET).name]
            ):
                raise ValueError(
                    "network audit input/finding list differs from the assessed single target"
                )
        if receipt["command"] != expected_command:
            raise ValueError("gate command changed: " + gate)
        receipts[gate] = receipt
    prior_paths = [f"reviews/structured/{ident}/review.yaml" for ident in PRIOR_IDS]
    inputs = {
        TARGET,
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "docs/record-review-profile.md",
        "docs/record-reviews.md",
        "conf/record_review.yaml",
        "conf/reference_validator.yaml",
        "uv.lock",
        "justfile",
        ".claude/skills/curate-yaml-record/SKILL.md",
        ".claude/skills/curate-yaml-record/references/review-checklist.md",
        ".claude/skills/review-communities/reference/metrics-and-reports.md",
        *prior_paths,
        *CACHES.values(),
        str(args.curation_receipt.resolve().relative_to(ROOT)),
    }
    inputs.update(str((STATE / name).relative_to(ROOT)) for name in INPUTS)
    for pattern in ("canary-*.json", "canary-*.log", "canary-*.exit", "canary-*-oak.yaml"):
        inputs.update(str(path.relative_to(ROOT)) for path in STATE.glob(pattern))
    inputs.update(
        str(path.relative_to(ROOT))
        for path in (ROOT / "history/records/LBNL_Switchgrass_Soil_SynCom16").glob("*.yaml")
    )
    for name in (
        "lbnl-supplements/retrieval.json",
        "lbnl-supplement-tables.json",
        "lbnl-retained/ecofab-relations/PMC13522444.xml",
        "lbnl-retained/ecofab-independent/ring-s2.xlsx",
        "lbnl-retained/ecofab-independent/ring-s2.txt",
        "lbnl-retained/lbnl-sources/fig2.png",
        "lbnl-retained/lbnl-sources/fig3.png",
        "lbnl-retained/lbnl-sources/fig5.png",
    ):
        inputs.add(str((STATE / name).relative_to(ROOT)))
    inputs.update(
        str(path.relative_to(ROOT))
        for path in (ROOT / "scripts/adhoc").glob("*phase2_lbnl*20261115.py")
    )
    inputs.update(
        {
            ".temp/phase2-science-20261115/curation-applied-001/receipt.json",
            "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml",
            "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml",
        }
    )
    output.mkdir()
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(STATE / "canary-target.yaml"),
    ]
    for name in sorted(inputs):
        command.extend(["--input", name])
    inspected_raw = subprocess.check_output(command, cwd=ROOT, text=True)
    (output / "inspection.json").write_text(inspected_raw)
    inspected = json.loads(inspected_raw)
    finished = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    evidence, assessments, checks = [], [], []
    owner = {"repository": REPOSITORY, "path": TARGET, "role": "canonical_record"}

    def ev(key, kind, reference, locator, summary, *, path=None, quote=None, support="supports"):
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

    def assess(key, area, topic, summary, evidence_ids, outcome="supported", fields=None):
        row = {
            "assessment_id": key,
            "target_ids": [TARGET_ID],
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "evidence_ids": evidence_ids,
        }
        if fields:
            row["details"] = "Exact current field selectors: " + ", ".join(fields)
        assessments.append(row)
        return row

    xml = str((STATE / "lbnl-retained/ecofab-relations/PMC9765266.xml").relative_to(ROOT))
    ev(
        "record",
        "record_content",
        TARGET,
        "Entire post-curation record:16 taxonomy rows,2 stock relations,0 graph nodes/arrows,2 culture contexts,5 discussions and preserved history",
        "All current assertions were read; the record now declares the Methods-defined final16 collection and does not assign earlier18/17-member effects to that complete roster.",
        path=TARGET,
    )
    ev(
        "curation",
        "record_content",
        str(args.curation_receipt.resolve().relative_to(ROOT)),
        "Bounded before/after bytes and native inline event; corresponding new sidecar",
        "Original history remains unchanged. One guarded correction adds16 source stocks, removes the domain placeholder and unsupported final16 graph interpretation, preserves all three measured observations as discussions, and separates physical/model environment and protocols.",
        path=str(args.curation_receipt.resolve().relative_to(ROOT)),
    )
    ev(
        "primary-methods",
        "primary_source",
        PAPER,
        "Methods/Isolate selection(s4-1); growth(s4-2/s4-3); plant colonization(s4-6); cryopreservation(s4-7)",
        "Exact final16 deposits and unknown-species statement; isolate preculture5–7days in1xR2A at30°C differs from200μL community assays with assay-dependent dilution/time and live-plant24°C regime. No general72h culture duration remains.",
        path=xml,
        quote="These isolates are novel strains from unknown species",
    )
    ev(
        "supplement-conflict",
        "primary_source",
        PAPER + "#supplementary-material",
        "Supplemental Table1 DOCX msystems.00951-22-s0006.docx, table1 rows2–19 and footnote",
        "Separately retrieved ZIP/DOCX is source evidence, never appended to the article cache. Row12 says MethylobacteriumOAE516, not MethodsOAE515. TableS1 lists BacillusOAE603 but omits MarmoricolaOAE513; it also includes SphingomonasOAE905 and PseudomonassimiaeWCS417. Genus-level plant-literature footnote supplies no stock-specific functional role. The mismatch remains explicit, not reconciled by guessing.",
        path=str((STATE / "lbnl-supplements/msystems.00951-22-s0006.docx").relative_to(ROOT)),
        quote="OAE516",
        support="context_only",
    )
    ev(
        "grounding",
        "database",
        str((STATE / "lbnl-grounding-final16.json").relative_to(ROOT)),
        "Readonly NCBI labels/ranks/synonyms, ENVO labels, exact crosswalk SHA and native per-genus output",
        "All16 NCBI terms are current genus labels, not verified species/genomes. OAP107 uses Arthrobacter genus1663, not generic species1667. Allobosea85413 retains source Bosea name and the database synonym. Native aggregate named-species crosswalk has13 grounded genera,2 ambiguous(Arthrobacter/Paenibacillus),1 unresolved renamed Allobosea. Crosswalk hash is pinned without a guessed release/build date; genus majority votes are not study-stock placement.",
        path=str((STATE / "lbnl-grounding-final16.json").relative_to(ROOT)),
        support="context_only",
    )
    ev(
        "ring",
        "primary_source",
        "https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003358",
        "Methods/Bacterial genome sequencing; S2 stock list",
        "Ring17 contains all Methods-defined Coker16 stocks plus OAE603. The same-stock rename Burkholderia→Paraburkholderia OAS925 is explicit. DSM113627 is the Coker individual-stock assertion; no consortium deposit is substituted. This relation supplies stock overlap, not transferred plant phenotypes or assay equivalence.",
        path=str((STATE / "lbnl-retained/ecofab-independent/ring-main-plos.xml").relative_to(ROOT)),
        quote="formerly known as Burkholderia sp. OAS925",
    )
    ev(
        "dopamine",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/",
        "Methods/Bacterial culture and SynCom inoculation(Sec9), paragraph0; canonical relation evidence",
        "The dopamine study lists16 stocks including OAE603 and no BradyrhizobiumOAE829, so the canonical15-shared-strain overlap is supported against Coker's final Methods list. It is a different host-genotype/culture design; no dopamine mechanism is imported into000087.",
        path=str((STATE / "lbnl-retained/ecofab-relations/PMC13522444.xml").relative_to(ROOT)),
    )
    observations = [
        (
            "nutrient",
            "s2-3; original Fig2C–E",
            "Initial equal18-strain experiment:1x/0.2x/0.1xR2A after3days, lowerOD600 but higher Shannon/evenness with dilution. Pseudomonas remains relatively dominant. This is a community response, not viable-cell growth enhancement, partner-specific benefit, or a final16 assertion.",
            "all 18 strains",
            "fig2",
        ),
        (
            "ratios",
            "s2-4; Discussion; original Fig3A–C",
            "17/18-strain panels with/without Pseudomonas compare equal and altered starting ratios at2/6days.2x/3xcutoff conditions give high diversity in the tested comparisons. RelativeDNA and spike-in checks do not establish viable counts or a universal optimum. The later dropout experiment has separate membership constraints.",
            "2× cutoff",
            "fig3",
        ),
        (
            "plant",
            "s2-7; Methods s4-6; original Fig5A–B",
            "Equal17/18-isolate inocula colonize12-day-old Brachypodium Bd21-3 and are profiled7days later; source soil is not the assay substrate. Community composition differs from inoculum, not proof of plant growth benefit or reciprocal microbial facilitation. One inoculum batch limits before/after taxon significance tests.",
            "an equally mixed community of 17 or 18 bacterial isolates",
            "fig5",
        ),
    ]
    for key, locator, summary, quote, figure in observations:
        ev(key, "primary_source", PAPER, locator, summary, path=xml, quote=quote)
        ev(
            figure,
            "primary_source",
            PAPER,
            "Original " + figure + " inspected at panel level",
            "Visual inspection agrees with the bounded text/caption interpretation; no raw-data reanalysis or undisclosed statistical replication is claimed.",
            path=str((STATE / "lbnl-retained/lbnl-sources" / (figure + ".png")).relative_to(ROOT)),
        )
    for gate, receipt in receipts.items():
        ev(
            "check-" + gate,
            "validation",
            receipt["log"],
            "Fresh native command and completed bound receipt",
            "Current record/hash-bound scoped diagnostic passed; it is not source truth or full repository QC.",
            path=receipt["log"],
            support="context_only",
        )
        checks.append(
            {
                "check_id": gate,
                "name": "Native " + gate,
                "status": "passed",
                "required": True,
                "summary": "Fresh scoped gate passed on exact current record and retained inputs.",
                "target_ids": [TARGET_ID],
                "command": shlex.join(receipt["command"]),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + gate],
            }
        )
    # This required manual source check has a claim-level evidence trail above;
    # it is distinct from the machine validator's known unannotated surfaces.
    checks.append(
        {
            "check_id": "manual-scientific",
            "name": "Full record source/context assessment",
            "status": "passed",
            "required": True,
            "summary": "Read all current claims and source scopes;16 individual stock/DSM assertions and all three preserved observations have explicit assessments. Uncertainty is retained; pass means assessment performed.",
            "target_ids": [TARGET_ID],
            "evidence_ids": [
                "record",
                "primary-methods",
                "supplement-conflict",
                "grounding",
                "ring",
                "dopamine",
                "nutrient",
                "ratios",
                "plant",
            ],
        }
    )
    assess(
        "identity",
        "scope",
        "Represented collection and physical setting",
        "The record is explicitly the final16 deposited collection in Methods, not every assay inoculum from the study. Laboratory environment is the physical setting; soil is retained as modeled/source environment. ENGINEERED/SYNTHETIC/RHIZOSPHERE classifications are compatible with this bounded model.",
        ["record", "primary-methods", "grounding"],
        fields=[
            "description",
            "ecological_state",
            "community_origin",
            "community_category",
            "environment_term",
            "modeled_environment",
        ],
    )
    for index, row in enumerate(grounding["rows"]):
        key = "stock-" + row["strain"].lower()
        ev(
            key,
            "primary_source",
            PAPER,
            "Methods/Isolate selection(s4-1), final deposited roster",
            "Exact Methods stock/deposit assertion; species remains unspecified and current collection catalog identity was not independently confirmed.",
            path=xml,
            quote=row["source_quote"],
        )
        assess(
            key,
            "grounding",
            row["strain"] + " stock and genus grounding",
            f"Current taxonomy[{index}] preserves {row['source_quote']}; verified genus term is {row['verified_genus_term']['id']} {row['verified_genus_term']['label']}. Native genus mapping is recorded with its uncertainty, not treated as a stock genome assignment. No role, accession or species is inferred.",
            [key, "grounding", "supplement-conflict"]
            + (["ring"] if row["strain"] == "OAS925" else []),
            fields=[f"taxonomy[{index}]"],
        )
    assess(
        "relations",
        "consistency",
        "Both cross-record stock relations",
        "Member-subset relation to ring17 and15-stock overlap with dopamine16 agree with exact strain lists. These relations refer to the final Methods stock list; TableS1's earlier roster does not override it or establish assay equivalence.",
        ["ring", "dopamine", "primary-methods"],
        fields=["related_communities"],
    )
    assess(
        "culture",
        "scope",
        "Distinct study protocols",
        "Description/design/factor fields now separate collection identity from panel outcomes. Two culture entries distinguish isolate preculture from community cultivation; no shared72h incubation or plant24°C bacterial condition remains. Cryopreservation and host protocols are identified as separate experiments, without invented treatment-arm membership.",
        ["primary-methods", "nutrient", "ratios", "plant", "record"],
        fields=["engineering_design", "environmental_factors", "growth_media"],
    )
    for index, (key, _, summary, _, figure) in enumerate(observations, 1):
        assess(
            key + "-discussion",
            "scope",
            "Preserved earlier-panel observation: " + key,
            summary
            + " The original observation/evidence survives in a discussion; removing its graph form prevents the schema's COMMUNITY_LEVEL whole-community default from asserting it for final16. Zero graph nodes and arrows remain, so no participant/direction/mediator is silently invented.",
            [key, figure, "supplement-conflict", "curation"],
            fields=[f"discussions[{index}]"],
        )
    assess(
        "remaining-gaps",
        "evidence",
        "Source conflicts and unsupplied mechanisms",
        "Discussion0 retains unresolved ecological mediation and compositional limits. Discussion4 records the actual Methods/TableS1 stock conflict, with separately retained source bytes. Their open status reflects unresolved claims, not rejection of the measured observations. No functional_role is invented to improve rubric completeness.",
        ["supplement-conflict", "primary-methods", "record"],
        outcome="concern",
        fields=["discussions[0]", "discussions[4]"],
    )
    assess(
        "history",
        "provenance",
        "Append-only curation provenance",
        "The guarded native correction and new sidecar describe the exact scientific scope correction. Existing inline/sidecar history and prior immutable reviews are preserved.",
        ["curation", "check-history"],
    )
    ev(
        "native-coverage-gap",
        "record_content",
        "src/communitymech/schema/mech_shared.yaml",
        "SupportingReference.snippet; Discussion.evidence; issue476",
        "SupportingReference has no native source-excerpt annotation, so machine reference success does not cover discussion assertions. All current discussion source claims were manually checked above; the native annotation gap remains owned by canonical Claw shared-schema work.",
        path="src/communitymech/schema/mech_shared.yaml",
        support="context_only",
    )
    assess(
        "machine-coverage",
        "evidence",
        "Manual verification versus native coverage",
        "Native reference validation traverses annotated EvidenceItem surfaces; its Total checks label counts retained results, not all examined assertions. Discussion SupportingReference surfaces remain uncovered under476. Manual scientific assessment and immutable review save do not resolve this blocker.",
        [
            "native-coverage-gap",
            "check-references",
            "nutrient",
            "ratios",
            "plant",
            "supplement-conflict",
        ],
        outcome="concern",
    )
    findings, actions = [], []
    for prior_id, prior_path in zip(PRIOR_IDS, prior_paths, strict=True):
        prior = yaml.safe_load((ROOT / prior_path).read_text())
        prefix = "prior-" + str(PRIOR_IDS.index(prior_id))
        ev(
            prefix,
            "prior_review",
            prior_path,
            "Immutable predecessor finding heads",
            "Historical finding preserved with explicit current reassessment; old technical receipts are not substituted for current gates.",
            path=prior_path,
            support="context_only",
        )
        for historical in prior["findings"]:
            finding = copy.deepcopy(historical)
            finding["previous_occurrences"] = [
                {
                    "repository": REPOSITORY,
                    "review_id": prior_id,
                    "finding_id": historical["finding_id"],
                }
            ]
            finding["evidence_ids"] = [
                prefix,
                "record",
                "curation",
                "primary-methods",
                "supplement-conflict",
                "grounding",
            ]
            key = finding["issue_key"]
            if key == "cm-000087-member-roster":
                finding["status"] = "open"
                finding["description"] = (
                    "The domain placeholder is corrected with all16 exact Methods stock/DSM pairs and transparent genus mappings. However, Main Methods/TableS1 stock correspondence remains unresolved (OAE515/OAE516; Marmoricola/Bacillus), and collection assertions are source-reported rather than independently catalog-confirmed. This remaining identity boundary stays under1548; no cross-panel alias or exact stock genome is inferred."
                )
                finding["field_paths"] = ["taxonomy", "discussions[4]"]
                finding["title"] = (
                    "Methods roster restored; unresolved supplementary stock correspondence remains"
                )
                finding["disposition_reason"] = (
                    "Retain the identity finding as open despite substantial correction; one record cannot close1548's three-record scope."
                )
            elif key == "cm-000087-assay-scope":
                finding["status"] = "resolved"
                finding["description"] = (
                    "Prior pooled metadata corrected by explicit final Methods collection scope, distinct isolate/community protocols, and individually evidenced earlier18/17 assay discussions. All three measured observations survive; their unsupported final16 graph interpretation is removed."
                )
                finding["disposition_reason"] = (
                    "Direct source/context inspection and fresh native gates support this bounded correction. The parent issue remains open for stock uncertainty and the other two records."
                )
            elif key == "cm-000087-source-versus-studied-environment":
                finding["status"] = "resolved"
                finding["field_paths"] = ["environment_term", "modeled_environment"]
                finding["description"] = (
                    "The physical setting is now ENVO01001405 laboratory environment, while ENVO00001998 soil is retained as modeled/source environment, supported by the Methods and readonly ENVO labels."
                )
                finding["disposition_reason"] = (
                    "Current typed fields and primary assay context agree; fresh native gates passed. No GitHub issue is automatically closed."
                )
            else:
                raise ValueError("unexpected predecessor finding")
            findings.append(finding)
    findings.append(
        {
            "finding_id": "native-discussion-coverage",
            "issue_key": "cm-000087-discussion-reference-coverage",
            "category": "evidence",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "Source claims were manually inspected, but the native validator leaves a known surface uncovered; this is a tooling coverage limitation, not a demonstrated scientific falsehood.",
            "rule_id": "review-checklist.claim-specific-support-and-context",
            "status": "open",
            "certainty": "confirmed",
            "title": "Native reference checks do not cover SupportingReference discussion snippets",
            "description": "All five current discussions use SupportingReference; its source snippets lack the native excerpt annotation. Manual source review does not certify automated coverage. Existing issue476 owns the shared contract gap; canonical fix belongs in Claw before downstream vendoring.",
            "target_ids": [TARGET_ID],
            "field_paths": ["discussions"],
            "owner_paths": [owner],
            "evidence_ids": ["native-coverage-gap", "check-references"],
            "external_issues": ["https://github.com/CultureBotAI/CommunityMech/issues/476"],
        }
    )
    ev(
        "linked-stock-metadata",
        "record_content",
        "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml",
        "OAS925 culture collection; OAP107 taxon; reciprocal 000087 description; parallel 000516 fields",
        "Both neighbors retain generic Arthrobacter sp.1667 for OAP107 and the consortium deposit DSM200000SY under individual OAS925. EcoFAB's reciprocal prose still says000087 has no strain list. These current metadata conflicts must be corrected together before integration with the stronger full-roster relation validator. Source stock-designation set relations are scientifically supported, but current cross-record metadata is not yet coherent.",
        path="kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml",
        support="context_only",
    )
    assess(
        "linked-record-blocker",
        "consistency",
        "Current reciprocal metadata remains a dependent correction",
        "This full record assessment does not certify neighboring records. Exact pairwise relation metadata remains blocked by EcoFAB2674, Dopamine2774 and shared deposit/reciprocal issue2806. Do not weaken validation or change the correct Methods-defined new roster to accommodate old metadata. Neighbor full biological reviews remain separate.",
        ["linked-stock-metadata", "ring", "dopamine", "grounding"],
        outcome="concern",
    )
    findings.append(
        {
            "finding_id": "linked-stock-metadata",
            "issue_key": "cm-000087-linked-stock-metadata",
            "category": "consistency",
            "severity": "major",
            "native_severity": "P2",
            "normalization_reason": "Complete cross-record membership compares stock identity metadata, so an individual-versus-consortium deposit conflict is material despite correct source stock names.",
            "rule_id": "review-checklist.claim-specific-support-and-context",
            "status": "open",
            "certainty": "confirmed",
            "title": "Paired stock metadata needs source-backed neighbor correction",
            "description": "Source-supported final16/ring17/dopamine16 set relations are retained, but neighbor OAP107 rank, OAS925 consortium-as-stock deposit and EcoFAB's stale placeholder description remain explicit integration blockers. The stronger relation validator is not yet integrated into this branch; existing native strict success does not clear that dependency.",
            "target_ids": [TARGET_ID],
            "field_paths": ["related_communities"],
            "owner_paths": [
                owner,
                {
                    "repository": REPOSITORY,
                    "path": "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml",
                    "role": "dependent_stock_metadata",
                },
                {
                    "repository": REPOSITORY,
                    "path": "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml",
                    "role": "dependent_stock_metadata",
                },
            ],
            "evidence_ids": ["linked-stock-metadata", "ring", "dopamine", "grounding"],
            "external_issues": [
                "https://github.com/CultureBotAI/CommunityMech/issues/2674",
                "https://github.com/CultureBotAI/CommunityMech/issues/2774",
                "https://github.com/CultureBotAI/CommunityMech/issues/2806",
            ],
        }
    )
    for finding in findings:
        if finding["status"] == "open":
            actions.append(
                {
                    "action_id": "followup-" + finding["finding_id"],
                    "description": "Resolve the retained source identity or native coverage boundary without inferring missing science.",
                    "finding_ids": [finding["finding_id"]],
                    "target_ids": [TARGET_ID],
                    "owner_paths": [owner],
                    "acceptance_checks": [
                        "For1548, obtain independent stock/deposit or primary clarification for the actual Methods/TableS1 conflict; keep000088/000122 distinct.",
                        "For476, repair the canonical shared schema and measure current source-assertion traversal; no vendor-only patch and no inference from Total checks.",
                        "For2674/2774/2806, correct paired stock rank, consortium-versus-individual deposits and stale reciprocal prose from primary evidence; then run the integrated full-roster relation validator without a waiver.",
                    ],
                }
            )
    metric = assess(
        "metrics",
        "completeness",
        "Literal rubric and zero-node denominator",
        "Completeness15/100 is expected after removing unsupported graph scope:5environment+10growth media, no invented member functions or interactions. Native evidence-per-node and validation-quality formulas divide by interaction count; with0nodes they are not calculated, rather than inventing a perfect score.",
        ["record"],
    )
    metric["metrics"] = [
        {
            "name": "completeness",
            "value": 15,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "Literal native rubric: required-member-role block0; environment5; three factors0; three nodes0; resources0; medium10; datasets0; node metabolites0.",
        },
        {
            "name": "graph_nodes",
            "value": 0,
            "unit": "nodes",
            "definition": "No current graph assertion; three earlier-panel observations are preserved in discussions.",
        },
        {
            "name": "source_methods_stocks",
            "value": 16,
            "unit": "stock assertions",
            "denominator": 16,
            "definition": "16 exact Methods stock/DSM claims represented; not independent catalog verification or source-conflict resolution.",
        },
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": stamp + "-phase2-lbnl-canary",
        "kind": "record",
        "repository": REPOSITORY,
        "title": "LBNL Methods-defined final16 source and assay-scope reassessment",
        "started_at": datetime.fromtimestamp(
            (STATE / "canary-initial-inspection.json").stat().st_mtime, timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "finished_at": finished,
        "reviewer": {
            "identity": "codex-community-m5",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored this bounded curation after primary-source inspection; parent conducts separate independent canary review before fanout.",
        },
        "skill": "curate-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Full current record assessed: 16 Methods stock claims restored, all three earlier 18/17 observations preserved outside the final16 graph, and physical environment/protocol scope corrected. Fresh scoped gates passed. Two predecessor findings resolve narrowly; stock correspondence, native discussion coverage and paired neighbor metadata remain open. No whole-corpus or Phase2 completion is claimed.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Entire000087 current record, every16-stock claim and both relations, all5discussions,0graph nodes/arrows, cultivation/environment/history and exact predecessor findings.",
            "selection": "Phase2 issue1548 canary, explicitly reviewed end to end before000088/000122; not all-record campaign fanout.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TARGET_ID],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "Methods/TableS1 stock conflict remains unresolved; no alias or absent species/function/genome field is invented. Source-reported DSM claims were not independently checked against current collection catalog pages.",
            "Source inspection covers the relevant main text, original figures2/3/5, separate TableS1 and Ring/Ding membership sources. Other original supplemental figures, raw sequencing and statistical reanalysis are outside this review.",
            "Genus-level NCBI/GTDB grounding is not exact study-stock genome placement;13grounds/2ambiguous/1unresolved are retained with a hash-identified mapping, no unsupported release date.",
            "Native SupportingReference discussion traversal remains uncovered under476. Manual claim verification and saved bundle validity are not automated assertion-coverage proof.",
            "The reference diagnostic uses an exact private copy of the existing3source caches with --no-full-text and native cache-hit preflight; no enrichment, supplement merging or canonical cache edits. Full QC/current-revision coverage is integrated separately.",
            "Zero graph nodes makes native evidence-per-interaction and validation-quality division undefined; those ratios are not fabricated. Low completeness rewards neither invented interactions nor member roles.",
            "This is author self-review. Independent canary review remains a separate prerequisite to fanout; no issue closure, push or merge is performed by this builder.",
            "The000088/000122 portions of1548 and the broader all-record campaign remain outside this one-record scientific assessment.",
            "Related-record integration remains blocked by2674/2774/2806. New stronger relation checks are not present in this branch, so current native strict success is not evidence that the dependency is fixed. Previously corrected2708–2710 remain pending merge in2775, not newly unresolved.",
            "Initial strict check failed13 note-placement rules; a separate native guarded follow-up moved the unchanged caveats into ordinary notes. Initial term check was interrupted when its default adapter began a download; final term validation uses explicit existing local adapters. Earlier receipts remain unchanged. A mistaken2807 issue link in one new sidecar was corrected by a separate immutable audit pointing to actual2808.",
        ],
        "related_reviews": [
            {
                "repository": REPOSITORY,
                "review_id": ident,
                "relationship": "Reassesses all predecessor findings against new current bytes; preserves immutable earlier bundle",
            }
            for ident in PRIOR_IDS
        ],
        "links": [
            "https://github.com/CultureBotAI/CommunityMech/issues/1548",
            "https://github.com/CultureBotAI/CommunityMech/issues/2776",
            "https://github.com/CultureBotAI/CommunityMech/issues/476",
            "https://github.com/CultureBotAI/CommunityMech/issues/2805",
            "https://github.com/CultureBotAI/CommunityMech/issues/2806",
            "https://github.com/CultureBotAI/CommunityMech/issues/2808",
        ],
    }
    (output / "review.yaml").write_text(
        yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=106)
    )
    print(
        json.dumps(
            {
                "review_id": review["review_id"],
                "output": str((output / "review.yaml").relative_to(ROOT)),
                "assessments": len(assessments),
                "checks": len(checks),
                "open_findings": 3,
                "resolved_findings": 2,
            }
        )
    )


if __name__ == "__main__":
    main()
