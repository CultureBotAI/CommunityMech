"""Author the bounded linked-stock scientific successor, 2026-11-15.

Inputs: reviewed three-record correction, primary sources, exact local grounding,
immutable predecessors and 27 current native receipts. Output: exclusive private
review candidate and native input inspection; native validate/save is separate.
Serves #2674/#2774/#2806; does not supersede full-record scientific coverage.
No canonical/cache mutation, provider access, issue closure or status promotion.
"""

import argparse
import copy
import json
import re
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
from check_phase2_linked_records_20261115 import (  # noqa: E402
    CACHES,
    GATE_RECIPES,
    REQUIRED_ONTOLOGIES,
    STATE,
    TARGETS,
    sha,
)
from check_phase2_linked_records_20261115 import (  # noqa: E402
    inputs as current_gate_inputs,
)

REPOSITORY = "CultureBotAI/CommunityMech"
BASE = "9356098cacff705d28eeef526b336f41f33113f5"
IDS = {
    "ecofab": "CommunityMech:000025",
    "dopamine": "CommunityMech:000516",
    "lbnl": "CommunityMech:000087",
}
GENERATION = "002"
DELTA_ID = "20261114T221158Z-m5-postcuration-scientific-delta"
CANARY_ID = "20261115T021628Z-phase2-lbnl-canary"
PLAN = STATE / "linked-stock-plan-003"
PRIMARY = {
    "coker": STATE / "linked-retained/ecofab-relations/PMC9765266.xml",
    "ring": STATE / "linked-retained/ecofab-independent/ring-main-plos.xml",
    "ring-table": STATE / "linked-retained/ecofab-independent/ring-s2.xlsx",
    "ding": STATE / "linked-retained/ecofab-relations/PMC13522444.xml",
    "ding-table": STATE / "linked-retained/dopamine-syncom-sources/stocks.xlsx",
    "coker-supplement": STATE / "lbnl-supplements/msystems.00951-22-s0006.docx",
}
EXPECTED_PRIMARY = {
    "coker": "ad9774e85b789eaa1718f1f06984f59845f20e3108993418c0444f715e869922",
    "ring": "8ab7d3de83f7b92e7dc6443db61d9ed31471d7ccdbdd1c8cf6c3d3b2efc6e947",
    "ring-table": "fd7882e673f62498ce2ac8c1215ece003edb7369fa780c106bfaa6db4b80e147",
    "ding": "9a58e566488461f6bda24554f2ab3c580e53fff58f5413b74e0957220acbe274",
    "ding-table": "185d64e815b7ef418d51b0cea0e2a42136fc92423836497bfe88ecbf6c4abfa3",
    "coker-supplement": "5bfa02fdb94538e9405fb0ec7d7b0dad338791a5ca0b4b651589f33148c8e0e7",
}
# These stock sets were manually read in the three primary lists, not inferred
# from equality between the corrected canonical records.
COKER_STOCKS = {
    "OAS925",
    "OAS809",
    "OAE908",
    "OAE515",
    "OAS795",
    "OAE497",
    "OAE506",
    "OAE829",
    "OAE881",
    "OAP107",
    "OAE513",
    "OAE865",
    "OAE612",
    "OAS944",
    "OAP136",
    "OAE614",
}
RING_STOCKS = COKER_STOCKS | {"OAE603"}
DING_STOCKS = RING_STOCKS - {"OAE829"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def load(path):
    return yaml.safe_load(path.read_text())


def relative(path):
    return str(path.resolve().relative_to(ROOT))


def expected_command(record, gate, name):
    target = TARGETS[record]
    if gate in GATE_RECIPES and gate != "terms":
        argument = str(Path("history/records") / Path(target).stem) if gate == "history" else target
        result = ["just", "--no-dotenv", GATE_RECIPES[gate], argument]
        if gate == "strict":
            result.extend(["--out", relative(STATE / (name + ".tsv"))])
        return result
    if gate == "terms":
        return [
            "uv",
            "run",
            "--no-sync",
            "linkml-term-validator",
            "validate-data",
            target,
            "-s",
            "src/communitymech/schema/communitymech.yaml",
            "--labels",
            "--config",
            relative(STATE / (name + "-oak.yaml")),
            "--cache-dir",
            relative(STATE / (name + "-labels")),
        ]
    if gate == "references":
        return [
            "uv",
            "run",
            "--no-sync",
            "linkml-reference-validator",
            "validate",
            "data",
            target,
            "-s",
            "src/communitymech/schema/communitymech.yaml",
            "--config",
            "conf/reference_validator.yaml",
            "--cache-dir",
            relative(STATE / (name + "-cache")),
            "--no-full-text",
        ]
    if gate == "network":
        return [
            "uv",
            "run",
            "--no-sync",
            "communitymech",
            "audit-network",
            "--communities-dir",
            relative(STATE / (name + "-records")),
            "--json",
        ]
    raise ValueError("unknown gate")


def verify_receipt(record, gate):
    name = f"linked-{record}-{gate}-{GENERATION}"
    path = STATE / (name + ".json")
    receipt = json.loads(path.read_text())
    code = int((STATE / (name + ".exit")).read_text().strip())
    log = ROOT / receipt["log"]
    if (
        receipt["name"] != name
        or receipt["head"] != BASE
        or receipt["record"] != TARGETS[record]
        or receipt["gate"] != gate
        or receipt["command"] != expected_command(record, gate, name)
        or receipt["exit_code"] != code
        or receipt["status"] != ("PASSED" if code == 0 else "FAILED")
        or receipt["runner_sha256"]
        != sha(ROOT / "scripts/adhoc/check_phase2_linked_records_20261115.py")
        or not receipt["inputs_unchanged"]
        or receipt["record_worktree_sha256"] != sha(ROOT / TARGETS[record])
        or receipt["inputs"] != current_gate_inputs()
        or not log.stat().st_size
        or sha(log) != receipt["log_sha256"]
    ):
        raise ValueError("unbound or incomplete native receipt: " + name)
    if gate == "terms" and (
        not receipt.get("ontology_inputs_unchanged")
        or set(receipt.get("ontology_inputs", {})) != REQUIRED_ONTOLOGIES
        or sha(STATE / (name + "-oak.yaml")) != receipt["ontology_config_sha256"]
    ):
        raise ValueError("ontology input binding missing")
    if gate == "references" and not receipt.get("private_cache_unchanged"):
        raise ValueError("reference cache changed")
    if gate == "network" and (
        receipt["private_record_sha256"] != sha(ROOT / TARGETS[record])
        or json.loads(log.read_text()) != {}
    ):
        raise ValueError("network input or result differs from assessed target")
    # A known supplementary-source mismatch is a retained failed check, never a
    # waived pass. Other failures require a new assessment before construction.
    if code and gate != "references":
        raise ValueError("unresolved non-reference gate failure: " + name)
    if code:
        failures = re.findall(
            r"\[ERROR\] Text part not found as substring: '([^']+)'\s+Location: ([^\n]+)\s+Reference: ([^\n]+)",
            log.read_text(),
        )
        expected = [
            ("OAE516", "discussions[4].evidence[2].snippet", "PMID:36472419"),
            ("OAE603", "discussions[4].evidence[4].snippet", "PMID:36472419"),
        ]
        if (
            record != "lbnl"
            or code != 1
            or failures != expected
            or log.read_text().count("[ERROR]") != 2
        ):
            raise ValueError(
                "reference result differs from independently inspected supplement boundary"
            )
    return path, receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify-record", choices=TARGETS)
    args = parser.parse_args()
    if args.verify_record:
        result = {
            gate: verify_receipt(args.verify_record, gate)[1]["exit_code"]
            for gate in (*GATE_RECIPES, "references", "network")
        }
        print(json.dumps({"record": args.verify_record, "verified_current_receipts": result}))
        if any(result.values()):
            raise SystemExit(1)
        return
    if args.output is None:
        raise ValueError("--output required when authoring a review")
    output = args.output.resolve()
    if output.exists() or not output.is_relative_to(STATE):
        raise ValueError("new exclusive private output required")
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() != BASE:
        raise ValueError("review base changed")
    for key, path in PRIMARY.items():
        if sha(path) != EXPECTED_PRIMARY[key]:
            raise ValueError("inspected primary bytes changed: " + key)
    documents = {key: load(ROOT / path) for key, path in TARGETS.items()}
    source_sets = {"ecofab": RING_STOCKS, "dopamine": DING_STOCKS, "lbnl": COKER_STOCKS}
    for key, doc in documents.items():
        stocks = [row["strain_designation"]["strain_name"] for row in doc["taxonomy"]]
        if len(stocks) != len(source_sets[key]) or set(stocks) != source_sets[key]:
            raise ValueError("canonical roster differs from inspected primary stock set")
        applied = json.loads((PLAN / key / "apply/receipt.json").read_text())
        if (
            not applied["applied_at"]
            or applied["target"] != TARGETS[key]
            or applied["after_sha256"] != sha(ROOT / TARGETS[key])
            or applied["before_sha256"] != sha(PLAN / key / "before.yaml")
        ):
            raise ValueError("applied correction no longer matches current bytes")
        if (PLAN / key / "candidate.yaml").read_bytes() != (ROOT / TARGETS[key]).read_bytes():
            raise ValueError("corrected canonical bytes differ from reviewed candidate")
    receipts = {
        (record, gate): verify_receipt(record, gate)
        for record in TARGETS
        for gate in (*GATE_RECIPES, "references", "network")
    }
    old_delta = ROOT / f"reviews/structured/{DELTA_ID}/review.yaml"
    old_canary = ROOT / f"reviews/structured/{CANARY_ID}/review.yaml"
    inputs = {
        *TARGETS.values(),
        *CACHES.values(),
        relative(old_delta),
        relative(old_canary),
        "docs/record-review-profile.md",
        "docs/record-reviews.md",
        "conf/record_review.yaml",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "src/communitymech/validators/related_communities.py",
        "scripts/validate_strict.py",
        "docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
        "uv.lock",
        "justfile",
        ".claude/skills/curate-yaml-record/SKILL.md",
        relative(Path(__file__)),
        "scripts/adhoc/check_phase2_linked_records_20261115.py",
        "scripts/adhoc/curate_phase2_linked_stocks_20261115.py",
        "scripts/adhoc/run_phase2_linked_gates_20261115.sh",
        relative(PLAN / "receipt.json"),
    }
    inputs.update(relative(path) for path in PRIMARY.values())
    for key in TARGETS:
        for name in ("before.yaml", "candidate.yaml", "apply/receipt.json"):
            inputs.add(relative(PLAN / key / name))
        inputs.update(
            relative(path)
            for path in (ROOT / "history/records" / Path(TARGETS[key]).stem).glob("*.yaml")
        )
    for key in ("ecofab", "dopamine"):
        inputs.add(relative(STATE / f"linked-{key}-grounding-001.json"))
    for path, receipt in receipts.values():
        inputs.update((relative(path), receipt["log"], relative(path.with_suffix(".exit"))))
    inputs.update(relative(path) for path in STATE.glob("linked-*-terms-002-oak.yaml"))
    inputs.update(
        relative(STATE / name)
        for name in (
            "linked-ecofab-terms-001.json",
            "linked-ecofab-terms-001.log",
            "linked-ecofab-terms-001.exit",
            "linked-host-anatomy-authority-001.json",
            "linked-adapter-regressions-001.log",
            "linked-staged-policy-001.json",
            "linked-checkpoint-gen-html-001.log",
            "lbnl-supplement-tables.json",
        )
    )
    output.mkdir()
    target_document = load(STATE / "linked-review-targets.yaml")
    for target in target_document["targets"]:
        target["kind"] = "maintained"
        target["ownership_note"] = (
            "Maintained canonical record; only the source-grounding and reciprocal-relation scope declared in this review is reassessed."
        )
    target_file = output / "targets.yaml"
    target_file.write_text(yaml.safe_dump(target_document, sort_keys=False))
    inputs.add(relative(target_file))
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        relative(target_file),
    ]
    for name in sorted(inputs):
        command.extend(["--input", name])
    raw = subprocess.check_output(command, cwd=ROOT, text=True)
    (output / "inspection.json").write_text(raw)
    inspected = json.loads(raw)
    finished = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    evidence, assessments, checks = [], [], []

    def ev(key, kind, reference, locator, summary, path, quote=None):
        item = {
            "evidence_id": key,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "summary": summary,
            "support": "supports",
            "accessed_at": finished,
            "snapshot_sha256": sha(path),
        }
        if quote:
            item["quote"] = quote
        evidence.append(item)

    def assessment(key, targets, area, topic, summary, evidence_ids, details=None):
        item = {
            "assessment_id": key,
            "target_ids": targets,
            "area": area,
            "topic": topic,
            "outcome": "supported",
            "summary": summary,
            "evidence_ids": evidence_ids,
        }
        if details:
            item["details"] = details
        assessments.append(item)
        return item

    ev(
        "coker",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC9765266/",
        "Methods/Isolate selection, s4-1; final16 stock/DSM list",
        "Final16 includes OAS925 with individual DSM113627 and OAP107 with DSM113524. These are source-reported individual stocks; source earlier18/17 panels and TableS1 discrepancy remain distinct.",
        PRIMARY["coker"],
        "DSM 113627",
    )
    ev(
        "ring",
        "primary_source",
        "https://doi.org/10.1371/journal.pbio.3003358",
        "Methods4.1 source collection;4.8 stock/genome list; separately S2Table rows2–18",
        "Ring17 equals the Methods-defined Coker16 plus OAE603. DSM200000SY denotes the collection; it is not the individual OAS925 deposit. The source connects the former Burkholderia and Bacillus stock names to Paraburkholderia and Gottfriedia.",
        PRIMARY["ring"],
        "or as a collection (DSM 200000SY",
    )
    ev(
        "ring-table",
        "primary_source",
        "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.3003358.s013&type=supplementary",
        "S2Table Sheet1 rows2–18, taxon/stock identifiers",
        "All17 study stock codes are directly enumerated, including OAE829, OAE603 and OAP107; their genomic identifiers are separate columns, not inferred by genus mapping.",
        PRIMARY["ring-table"],
    )
    ev(
        "ding",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/",
        "Methods/Bacterial strains and synthetic community inoculation, Sec9 paragraph0; Sec8 host design",
        "The16-stock inoculum includes OAE603 and excludes OAE829. It overlaps15 stocks with Coker final16 and is a subset of ring17; this stock correspondence does not equate their experiments or measured endpoints.",
        PRIMARY["ding"],
        "Bacillus OAE603",
    )
    ev(
        "ding-table",
        "primary_source",
        "https://doi.org/10.1038/s41467-026-76211-1",
        "Supplementary Data1 stock/media table, rows2–17",
        "Stock list corroborates the16 inoculum members; Data1 cellA16 OAE51 conflicts with Methods/Fig3a OAE515 and is retained as a source reporting discrepancy, not invented as a strain alias.",
        PRIMARY["ding-table"],
    )
    ev(
        "coker-supplement",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC9765266/#supplementary-material",
        "Separate TableS1 DOCX, table1 row12 Strain cell OAE516 and row18 Strain cell OAE603; genus cells Methylobacterium and Bacillus respectively",
        "The two exact stock-cell quotations are present in the separate supplemental table. Their absence from the main-article cache is not a false quotation. TableS1/Methods roster disagreement remains explicit under1548; no alias or final16 membership is inferred from these earlier-assay cells.",
        PRIMARY["coker-supplement"],
        "OAE516",
    )
    for key in TARGETS:
        ev(
            key + "-record",
            "record_content",
            TARGETS[key],
            "current stock metadata and six paired related_communities claims",
            "Exact applied candidate bytes checked against the current record and append-only correction receipt; no canonical content is generated by this review.",
            ROOT / TARGETS[key],
        )
        ev(
            key + "-curation",
            "record_content",
            relative(PLAN / key / "apply/receipt.json"),
            "guarded apply before/after hashes",
            "One reviewed native validated write, bounded reconstruction, peer/source byte guards and native append-only history; previous history remains intact.",
            PLAN / key / "apply/receipt.json",
        )
    for key, cores in (("ecofab", 15), ("dopamine", 14)):
        path = STATE / f"linked-{key}-grounding-001.json"
        ev(
            key + "-grounding",
            "database",
            relative(path),
            "readonly NCBI labels/ranks/synonyms and native crosswalk reproduction for every stock",
            f"All {cores} existing GTDB numerical cores reproduce and are preserved. Crosswalk SHA761d5537… is pinned; no latest/build date is asserted. OAP107 maps to genus Arthrobacter1663 with11 candidates; Paenibacillus retains33 candidates. Allobosea uses explicit bacterial Bosea synonym lookup and preserves curated34/34 mapping.",
            path,
        )
        assessment(
            key + "-rank",
            [IDS[key]],
            "grounding",
            "Source genus and reproducible mapping provenance",
            f"OAP107 now uses Arthrobacter NCBITaxon1663, with species unresolved and11 genus-mapping candidates. All {cores} preexisting numeric mapping cores remain unchanged; curated Allobosea flags and Paenibacillus ambiguity remain explicit. The full primary stock list and readonly NCBI authority support the bounded correction; mapping votes are not stock genome identity.",
            [key + "-record", key + "-grounding", "ring-table", "coker", "ding"],
            "Selectors taxonomy[*].taxon_term, mapping_source, and every OAP107 participating_taxa term. No functional roles, stock phenotypes or genome accession inference is approved here.",
        )
        assessment(
            key + "-deposit",
            [IDS[key]],
            "identity",
            "Individual stock versus consortium deposit",
            "OAS925 now carries source-reported individual DSM113627. The collection DSM200000SY remains in community engineering notes/evidence, where the source identifies it. No individual stock is grounded by a consortium accession. Other reported individual deposits and source strain designations are preserved.",
            [key + "-record", "coker", "ring"],
            "Selectors OAS925 culture_collections and engineering_design.notes/evidence. Current collection-catalog status and individual whole-genome placement are not established by this source assertion.",
        )
    assessment(
        "three-source-sets",
        list(IDS.values()),
        "identity",
        "Three distinct source-defined stock rosters",
        "Coker Methods16 plus OAE603 equals ring17; ring17 minus OAE829 equals Ding16; Coker16 and Ding16 share15 stocks. Every canonical stock assertion was compared with its explicit primary list. The ring-trial OAS925-dropout16 is a fourth, different experimental roster and is not conflated with either source16.",
        [
            "coker",
            "ring",
            "ring-table",
            "ding",
            "ding-table",
            "ecofab-record",
            "dopamine-record",
            "lbnl-record",
        ],
    )
    for key in TARGETS:
        assessment(
            key + "-relations",
            [IDS[key]],
            "consistency",
            "Both reciprocal cohort relations use complete stock designations",
            "Both links to the other assessed cohort members now use SHARED_STRAIN_DESIGNATIONS and correct subset/superset/overlap directions. Descriptions preserve final Methods16 versus earlier assay18/17 and TableS1 differences. Strong integrated relation validation compares actual stock metadata; scientific interpretation rests on the three inspected source lists.",
            ["coker", "ring-table", "ding", key + "-record", key + "-curation"],
            "Selectors related_communities entries whose community_id is000025,000516 or000087. Other links, including the separate natural-soil study, are outside this delta.000087 taxonomy, earlier-assay discussions and zero-node graph are unchanged by this correction.",
        )
    failed_references = []
    for (key, gate), (path, receipt) in receipts.items():
        ev_id = f"check-{key}-{gate}"
        ev(
            ev_id,
            "validation",
            receipt["log"],
            "complete native focused gate log and bound receipt",
            f"Actual revision {BASE}; exit{receipt['exit_code']}; all current scientific/config/history input hashes unchanged. This check is not scientific claim approval.",
            ROOT / receipt["log"],
        )
        checks.append(
            {
                "check_id": ev_id,
                "name": key + " " + gate,
                "status": "passed" if receipt["exit_code"] == 0 else "failed",
                "required": True,
                "summary": "Fresh focused native gate; literal result retained.",
                "target_ids": [IDS[key]],
                "command": shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [ev_id],
            }
        )
        if receipt["exit_code"]:
            failed_references.append(key)
    prior_delta, prior_canary = load(old_delta), load(old_canary)
    ev(
        "prior-delta",
        "prior_review",
        relative(old_delta),
        "exact stable grounding finding heads and retained scientific findings",
        "Retains the previous scientific observation unchanged. Its causal-role/study-stage/genome findings remain open outside this metadata correction; current evidence is reassessed independently below.",
        old_delta,
    )
    ev(
        "prior-canary",
        "prior_review",
        relative(old_canary),
        "linked-stock-metadata finding and full000087 assessment",
        "Preserves the accepted16-stock/assay-scope canary. This successor resolves paired metadata only, not the Methods/TableS1 discrepancy or all discussion reference coverage.",
        old_canary,
    )
    findings = []
    dispositions = {
        "cm-000025-grounding-provenance": (prior_delta, DELTA_ID, "ecofab", "ecofab-rank"),
        "cm-000516-grounding-provenance": (prior_delta, DELTA_ID, "dopamine", "dopamine-rank"),
        "cm-000087-linked-stock-metadata": (prior_canary, CANARY_ID, "lbnl", "lbnl-relations"),
    }
    for issue_key, (prior, prior_id, key, assessment_id) in dispositions.items():
        predecessor = next(item for item in prior["findings"] if item["issue_key"] == issue_key)
        finding = copy.deepcopy(predecessor)
        finding.update(
            finding_id=issue_key,
            status="resolved",
            title="Source-backed linked stock metadata corrected",
            description="The narrow source-supported stock/rank/provenance/reciprocal metadata correction is present in the inspected current bytes. No source-conflict, causal-role, experimental-stage or exact-genome claim is cleared by this disposition.",
            disposition_reason=next(
                item["summary"] for item in assessments if item["assessment_id"] == assessment_id
            ),
            evidence_ids=[
                "coker",
                "ring",
                "ring-table",
                "ding",
                key + "-record",
                key + "-curation",
                "check-" + key + "-strict",
            ]
            + (
                [key + "-grounding"]
                if key != "lbnl"
                else ["ecofab-grounding", "dopamine-grounding"]
            ),
            previous_occurrences=[
                {
                    "repository": REPOSITORY,
                    "review_id": prior_id,
                    "finding_id": predecessor["finding_id"],
                }
            ],
        )
        findings.append(finding)
    if failed_references != ["lbnl"]:
        raise ValueError(
            "actual reference outcomes differ from the inspected26pass/1failure checkpoint"
        )
    assessment(
        "lbnl-supplement-boundary",
        [IDS["lbnl"]],
        "evidence",
        "SupportingReference traversal now reaches two separately sourced TableS1 cells",
        "The new shared annotation exposes two actual article-cache substring failures: OAE516 at discussions[4].evidence[2] and OAE603 at evidence[4]. Direct inspection verifies both in TableS1 rows12/18. Preserve the exact quotes and the failed native result; source-specific supplement routing remains under1996. This observation does not establish complete corpus assertion coverage or resolve1548 source roster disagreement.",
        ["coker-supplement", "check-lbnl-references", "prior-canary"],
    )["outcome"] = "concern"
    findings.append(
        {
            "finding_id": "lbnl-supplement-routing",
            "issue_key": "cm-000087-supplement-reference-routing",
            "category": "evidence",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "Direct primary supplement inspection verifies both cell quotations; the remaining failure is source routing rather than an established scientific falsehood.",
            "rule_id": "review-checklist.claim-specific-support-and-context",
            "status": "open",
            "certainty": "confirmed",
            "title": "Route two exact TableS1 stock cells to their retained supplement",
            "description": "Adopted SupportingReference traversal now reaches discussion4 and reports exactly two article-cache misses. OAE516 is TableS1 row12 and OAE603 row18. Main-article PMID36472419 cache cannot certify separate supplement text; preserve source boundary and correct quotations. Existing issue1996 owns supplement routing, with1548 retaining the substantive roster discrepancy.",
            "target_ids": [IDS["lbnl"]],
            "field_paths": [
                "discussions[4].evidence[2].snippet",
                "discussions[4].evidence[4].snippet",
            ],
            "owner_paths": [
                {"repository": REPOSITORY, "path": TARGETS["lbnl"], "role": "canonical_record"}
            ],
            "evidence_ids": ["coker-supplement", "check-lbnl-references"],
            "external_issues": [f"https://github.com/{REPOSITORY}/issues/1996"],
        }
    )
    review = {
        "schema_version": "1.0.0",
        "review_id": stamp + "-phase2-linked-stock-delta",
        "kind": "batch",
        "repository": REPOSITORY,
        "title": "Source-backed stock grounding and reciprocal relation correction",
        "started_at": "2026-11-15T02:25:59Z",
        "finished_at": finished,
        "reviewer": {
            "identity": "codex-community-m5",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored guarded correction after direct primary-source/ontology inspection; independent parent reviewed staged source delta and guards before apply.",
        },
        "skill": "curate-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Three linked stock/provenance findings resolve within this bounded metadata scope. Of27 current focused gates,26passed and the LBNL reference gate failed on two verified supplement-only quotations; this required failure remains open under1996. Full-record source assertions and retained EcoFAB1427/2675, LBNL1548 and wider Phase2/QC remain separate obligations.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "000025/000516 stock rank, mapping provenance and individual-versus-consortium deposits; all six reciprocal cohort relations including000087. No entire-record or corpus approval.",
            "selection": "Dependent source-backed paired correction required by accepted000087 canary; exact fixed cohort, not a sample.",
            "coverage": "partial",
            "population_size": 3,
            "reviewed_target_ids": list(IDS.values()),
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": [
            {
                "action_id": "retain-supplement-routing",
                "description": "Add source-aware supplement routing through the maintained shared reference contract while preserving exact primary text and article/supplement boundaries.",
                "finding_ids": ["lbnl-supplement-routing"],
                "target_ids": [IDS["lbnl"]],
                "owner_paths": [
                    {
                        "repository": REPOSITORY,
                        "path": "conf/reference_validator.yaml",
                        "role": "reference_validation_configuration",
                    }
                ],
                "acceptance_checks": [
                    "Verify exact TableS1 artifact identity and stock-cell locators; run native validation against the correctly selected source without rewriting quotations or mixing supplement text into article caches.",
                    "Retain the failed original run and independently measure covered assertions; a low issue counter is not coverage proof.",
                ],
            }
        ],
        "limitations": [
            "This intermediate successor covers corrected fields only. Full current record reviews follow the separate EcoFAB causal/study-stage and genome correction; no whole-record freshness is conferred by this delta.",
            "Retained EcoFAB1427 comprises causal-role and pooled-study-stage findings, and2675 concerns exact17 genome IDs. Primary sources are available; these are actionable next corrections, not inaccessible evidence.",
            "000087 Methods/TableS1 conflicts remain under1548. Current source-reported individual collection numbers are not independent current catalog verification; NCBI genus mapping is not exact study-stock genome identity.",
            "The earlier EcoFAB term canary failed one of nine gates because its explicit ontology map omitted PO. Issue2817 and the immutable failed receipt/readonly authority proof are retained; the repaired same-launcher canary binds all six required local adapter hashes before and after.",
            "Reference matching uses private exact cache copies with native cache-hit preflight and no full-text enrichment. Native results do not substitute for direct source assessment or establish all-record assertion coverage.",
            "Previously corrected2708–2710 and2772/2773/2778 retain their earlier dispositions; this delta does not reclassify them or drop000515 from shared-cache lineage.",
            "Literal whole-record completeness/validation-quality metrics are not recalculated for this partial metadata review. Low-level network integrity is independent of causal science.",
            "No canonical record, cache, prior review, prior history, issue state or native review status is changed by this builder. Parent owns final full-QC, generated-document integration and publication/merge decisions.",
        ],
        "related_reviews": [
            {
                "repository": REPOSITORY,
                "review_id": ident,
                "relationship": "Preserves immutable predecessor; supersedes only explicitly named stock metadata findings",
            }
            for ident in (DELTA_ID, CANARY_ID)
        ],
        "links": [
            f"https://github.com/{REPOSITORY}/issues/{number}"
            for number in (2674, 2774, 2806, 2817, 1427, 2675, 1548, 476)
        ],
    }
    # Native target labels are reused, but their ownership notes must not imply
    # that this deliberately partial successor reviewed every unchanged field.
    for target in review["targets"]:
        target["ownership_note"] = (
            "Maintained canonical record; only the source-grounding and reciprocal-relation scope declared in this review is reassessed."
        )
    (output / "review.yaml").write_text(
        yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=105)
    )
    print(
        json.dumps(
            {
                "review_id": review["review_id"],
                "checks": len(checks),
                "assessments": len(assessments),
                "resolved_findings": sum(item["status"] == "resolved" for item in findings),
                "open_findings": sum(item["status"] == "open" for item in findings),
                "output": relative(output / "review.yaml"),
            }
        )
    )


if __name__ == "__main__":
    main()
