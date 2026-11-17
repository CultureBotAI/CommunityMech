#!/usr/bin/env python3
"""Assemble the independently assessed three-record curation delta, 2026-11-14.

Inputs: frozen native inspection, three immutable prior reviews, primary evidence,
bounded diff receipt, and explicit final native gate receipts. Output: staging
YAML for native validate/save; no canonical mutation or automatic issue closure.
Serves #2676/#2708/#2709/#2710/#2772/#2773, checks #2777/#2778, retains other heads.
Scientific judgments are authored below; passing validators do not create them.
"""

from __future__ import annotations

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
from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
REPOSITORY = "CultureBotAI/CommunityMech"
GATES = ("schema", "strict", "terms", "references", "gtdb", "domain", "history")
RECIPES = {
    "schema": "validate",
    "strict": "validate-strict",
    "terms": "validate-terms",
    "references": "validate-references-explained",
    "gtdb": "validate-gtdb",
    "domain": "validate-gtdb-domain",
    "history": "validate-history",
    "docs-current": "check-docs-current",
    "history-all": "validate-history",
    "gen-html": "gen-html",
    "aggregate-qc": "qc-references",
    "products": "validate-products",
}
CACHE_TESTS = (
    "tests/test_reference_cache_names_are_case_exact.py",
    "tests/test_no_case_conflicting_cache_pairs.py",
    "tests/test_cache_is_source_text_not_notes.py",
    "tests/test_cache_supplements.py",
)
OUTCOMES = {
    "cm-000025-cache-content-type": (
        "Both EcoFAB and nitrogen cache headers now say abstract_and_full_text. "
        "Independent byte comparison proves only those header values changed; existing "
        "main-article markers, source identities, quotations and supplement boundaries are preserved."
    ),
    "cm-000025-dopamine-relation-description": (
        "The corrected prose states ring17 equals dopamine16 plus Bradyrhizobium OAE829. "
        "Ring S2 and Ding Methods stock sets independently support this exact operation; "
        "typed MEMBER_SUPERSET_OF, membership and the separate Coker comparator are unchanged."
    ),
    "cm-000515-gtdb-copied-mechanism-provenance": (
        "The new note distinguishes measured 16S taxonomy from unmeasured amoA activity. "
        "All six numeric cores are unchanged and independently reproduced from the full "
        "crosswalk SHA256. The curated Nitrososphaeria552/631 remains distinct from the "
        "native Thermoproteota631/631 vote; no release/build date or function is asserted."
    ),
    "cm-pmid42660928-cache-content-type": (
        "The shared Ding cache now declares its existing abstract and main article. "
        "All other bytes are identical. Both consumers000515 and000516 are assessed and "
        "both prior finding occurrences are reconciled; no supplementary text is imported."
    ),
    "cm-000516-exudate-decrease-host-target-scope": (
        "Node4 no longer declares HOST_IS_TARGET. The measured pooled extracellular "
        "dopamine decrease, both quotations, and microbial-use versus altered-host-output "
        "alternatives remain unchanged. The separately identified residual direction2778 "
        "was also removed: the experiment measures SynCom-to-extracellular dopamine, "
        "not a dopamine-to-participating-taxa effect."
    ),
    "cm-000516-correlation-direction-scope": (
        "Nodes0/1 retain signed Spearman association prose but neither HOST_IS_SOURCE "
        "nor effect_direction. Nodes2/3 retain the source-supported isolate intervention "
        "signs. The guide now uses those measured culture effects and its worked-example "
        "table no longer claims host_participation; the issue2777 omission is corrected."
    ),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_yaml(path):
    return yaml.load(path.read_text(), Loader=yaml.CSafeLoader)


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def just_arguments(command):
    """Accept the persisted native runner's options, never a scoped extra recipe."""
    if not command or Path(command[0]).name != "just":
        return None
    index = 1
    while index < len(command) and command[index].startswith("--"):
        if command[index] in ("--verbose", "--no-dotenv", "--no-deps"):
            index += 1
        elif command[index : index + 2] == ["--color", "never"]:
            index += 2
        else:
            raise ValueError("Unsupported native launcher option")
    return command[index:]


def verify_gate_binding(key, receipt, targets, revision, validation_inputs, verified_revisions):
    """Check scope plus frozen revision/current bytes for every gate (#2781)."""
    if not revision or receipt["head"] != revision:
        raise ValueError("Gate revision differs from explicit frozen revision: " + key)
    short, category = key.split(".", 1)
    command = receipt["command"]
    native_args = just_arguments(command)
    if short != "all":
        target_path = targets["CommunityMech:" + short]["path"]
        expected_argument = (
            "history/records/" + Path(target_path).stem if category == "history" else target_path
        )
        expected = [RECIPES[category], expected_argument]
        valid = native_args == expected
        if category == "strict" and native_args is not None:
            valid = valid or (
                len(native_args) == 4 and native_args[:2] == expected and native_args[2] == "--out"
            )
        if not valid:
            raise ValueError("Native recipe/target scope differs: " + key)
    elif category == "cache-tests":
        full_native = native_args in (["test"], ["qc"], ["qc-references"])
        focused_pytest = command[:3] == ["uv", "run", "pytest"] and command[3:] == [
            *CACHE_TESTS,
            "-q",
        ]
        if not (full_native or focused_pytest):
            raise ValueError("Cache gate does not cover the required full test scope")
    elif native_args != [RECIPES[category]]:
        raise ValueError("Shared gate requires exact unscoped native recipe: " + key)
    if revision not in verified_revisions:
        for filename in validation_inputs:
            raw_at_revision = subprocess.check_output(
                ["git", "show", revision + ":" + filename], cwd=ROOT
            )
            if hashlib.sha256(raw_at_revision).hexdigest() != digest(ROOT / filename):
                raise ValueError("Gate validation input changed: " + filename)
        verified_revisions.add(revision)
    passed = receipt.get("exit_code") == 0 and not receipt.get("skip_markers")
    if category == "cache-tests" and native_args in (["qc"], ["qc-references"]):
        passed = any(
            row.get("recipe") == "test" and row.get("status") == "PASSED"
            for row in receipt.get("stages", [])
        )
    return passed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--gate",
        action="append",
        default=[],
        help="KEY=repository-relative receipt JSON. KEY is 000025.schema etc, or all.docs-current/history-all/cache-tests/gen-html",
    )
    parser.add_argument(
        "--expected-revision", help="Exact frozen M5 revision; mandatory with gates"
    )
    args = parser.parse_args()
    if args.gate and not args.expected_revision:
        parser.error("--expected-revision is required when any final gate is supplied")
    initial = json.loads((STATE / "postcuration-initial-inspection.json").read_text())
    acceptance = json.loads((STATE / "postcuration-acceptance-map.json").read_text())
    delta = json.loads((STATE / "postcuration-diff-check.json").read_text())
    reassessed = []
    for item in initial["source"]["inputs"]:
        if digest(ROOT / item["path"]) != item["sha256"]:
            raw = (ROOT / item["path"]).read_bytes()
            # Coordinator removed exactly one unintended module-docstring space.
            # Reconstruct its prior bytes in memory and prove the original hash;
            # do not silently refresh the initial inspection or source judgments.
            restored = raw.replace(b"\nbefore/after receipt.", b"\n before/after receipt.", 1)
            if (
                item["path"] == "scripts/adhoc/apply_m5_completion_corrections_20261114.py"
                and item["sha256"]
                == "4a09377ebf8ddf6dba26aba19f1b66fee19a629c811d46bc872942070ef0c5a5"
                and hashlib.sha256(restored).hexdigest() == item["sha256"]
            ):
                reassessed.append(
                    {
                        "path": item["path"],
                        "initial_sha256": item["sha256"],
                        "current_sha256": digest(ROOT / item["path"]),
                        "proof": "Reinserting exactly one leading space in the module docstring reconstructs the original inspected byte hash. Full current helper was reread: exact baseline/concurrency checks, native writer, semantic guard, append-only events and atomic replacement remain intact.",
                    }
                )
            else:
                raise ValueError(
                    "Reassess changed initial input before continuing: " + item["path"]
                )
    reassessment_path = STATE / "postcuration-input-reassessment.json"
    reassessment_path.write_text(json.dumps(reassessed, indent=2) + "\n")
    for item in delta["results"]:
        if digest(ROOT / item["path"]) != item["after_sha256"]:
            raise ValueError("Delta receipt is stale: " + item["path"])
    now = datetime.now(timezone.utc)
    finished = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    targets = {t["target_id"]: t for t in initial["targets"]}
    target_ids = list(targets)
    records = {key: read_yaml(ROOT / row["path"]) for key, row in targets.items()}
    inputs = {item["path"] for item in initial["source"]["inputs"]}
    inputs.update(
        {
            str(Path(__file__).relative_to(ROOT)),
            ".temp/m5-completion-20261114/postcuration-diff-check.json",
            ".temp/m5-completion-20261114/postcuration-initial-inspection.json",
            ".temp/m5-completion-20261114/postcuration-input-reassessment.json",
            ".claude/skills/review-communities/SKILL.md",
            ".claude/skills/review-communities/reference/execution-protocol.md",
            "conf/reference_validator.yaml",
            "pyproject.toml",
            "uv.lock",
        }
    )
    evidence = []

    def ev(key, kind, reference, locator, summary, support="supports", quote=None, path=None):
        value = {
            "evidence_id": key,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "accessed_at": finished,
            "support": support,
            "summary": summary,
        }
        if quote:
            value["quote"] = quote
            if path and path.endswith(".xml"):
                plain = " ".join(
                    "".join(ElementTree.parse(ROOT / path).getroot().itertext()).split()
                )
                if " ".join(quote.split()) not in plain:
                    raise ValueError("Authored quote is not exact source text: " + key)
        if path:
            value["snapshot_sha256"] = digest(ROOT / path)
            inputs.add(path)
        evidence.append(value)

    ev(
        "delta",
        "validation",
        ".temp/m5-completion-20261114/postcuration-diff-check.json",
        "all six record/cache paths; before76aa644c and current SHA256; explicit selectors",
        "Independent mechanical comparison permits only reviewed relation, mapping provenance and causal-tag fields plus four appended inline events. All other parsed record semantics and eighteen historical sidecar bytes are identical; all three caches differ only at content_type. This bounds assessment; it does not prove science.",
        path=".temp/m5-completion-20261114/postcuration-diff-check.json",
    )
    for key, target in targets.items():
        short = key.split(":")[1]
        ev(
            "record-" + short,
            "record_content",
            target["path"],
            "whole previously read baseline plus exact current semantic diff; explicit changed selectors",
            "Maintained identity is unchanged. All changed fields were directly inspected with primary evidence; complete prior reviews retain unchanged claim/edge coverage. This successor assesses the bounded correction and predecessor selectors only.",
            path=target["path"],
        )
    ev(
        "ring-stocks",
        "primary_source",
        "https://doi.org/10.1371/journal.pbio.3003358",
        "Ring-trial S2 Table, all17 named stock rows; independently compared with Ding Methods and Coker Methods",
        "Ring17 contains all sixteen dopamine stocks and OAE829. Coker's final16 instead includes OAE829 and lacks OAE603. The corrected ring-to-dopamine relation does not equate those distinct16-stock sets.",
        path=".temp/m5-completion-20261114/ecofab-independent/ring-s2.xlsx",
    )
    ev(
        "dopamine-stocks",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/",
        "Methods SynCom16 preparation; explicit16-member stock list; SI Table1 context",
        "The dopamine community includes OAE603 and excludes OAE829. Its strain list matches the corrected set difference. The article's main Methods/figure identities govern the minor SI stock-code typo; no new taxonomic identity is inferred.",
        quote="Sixteen bacterial strains",
        path=".temp/m5-completion-20261114/ecofab-relations/PMC13522444.xml",
    )
    ev(
        "soil-evidence",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/",
        "Fig4; main soil experiment Methods; Supplementary Fig16; Supplementary Data5 control community",
        "Soil evidence is relative16S composition and six-week catecholamine treatment response in natural agricultural soil, without a host or direct amoA assay. Four Thaumarchaeota workbook rows bear Nitrososphaera taxonomy. Removing a functional claim preserves both actual ecological nodes, all six control abundances and all source snippets.",
        path=".temp/m5-completion-20261114/yolo-sources/soil-data5.xlsx",
    )
    ev(
        "mapping",
        "database",
        ".temp/m5-completion-20261114/yolo-sources/mapping-comparison.json",
        "all six taxonomy rows; native aggregate denominator excluding unnamed species; separate curated class vote",
        "Crosswalk761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd reproduces five ordinary numeric cores plus the curated class core.65 named-species rows split into57 Nitrososphaeria rows/552genomes and8 Nitrososphaeria_A rows/79genomes;552/631 rounds0.875. Pinning this file/method does not certify a historical release or ecological function.",
        path=".temp/m5-completion-20261114/yolo-sources/mapping-comparison.json",
    )
    ev(
        "correlations",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/",
        "Fig3a; Results correlations between exudate dopamine and relative abundance across genotypes; main text paragraphs around Fig3",
        "Nodes0/1 describe five positive associations and one negative OAS925 association (Spearman,n28) across plant genotypes. These are unadjusted observational associations with possible genotype confounding; no intervention establishes host-to-member causal direction in these nodes. Sign remains explicit in prose.",
        quote="positively associated",
        path=".temp/m5-completion-20261114/ecofab-relations/PMC13522444.xml",
    )
    ev(
        "isolate-interventions",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/",
        "Fig3b-h; isolated bacterial culture Methods;0/50/100microgram-per-mL dopamine,30C,R2A/0.1R2A,n4",
        "At the node-specified100microgram-per-mL dose, five isolated stocks have greater finalOD600 and OAS925 lowerOD600. Nodes2/3 correctly retain those intervention signs. This does not establish in-SynCom mediation, catabolism or universal monotonic dose response (Bosea's50-dose differs).",
        path=".temp/m5-completion-20261114/dopamine-syncom-sources/fig3.png",
    )
    ev(
        "extracellular-endpoint",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/",
        "Fig2c and caption; Results SynCom inoculation and spent hydroponic-medium dopamine; Discussion alternatives",
        "Node4 measures lower extracellular dopamine following whole-SynCom inoculation versus axenic plants (pooledn28/n29,two-sidedt P=.0075). Microbial utilization and altered host production/exudation remain alternative explanations. Neither HOST_IS_TARGET nor a dopamine-to-taxa effect_direction follows. The record retains this endpoint, uncertainty and both quotations.",
        path=".temp/m5-completion-20261114/dopamine-syncom-sources/fig2.png",
    )
    ev(
        "schema-guidance",
        "authority",
        "src/communitymech/schema/communitymech.yaml",
        "HostParticipationEnum; EffectDirectionEnum; docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md worked-example table and signed-effect section",
        "Typed host/source/target and effect_direction encode source-to-target biological responses, not arbitrary correlation signs or a reversed metabolite endpoint. Updated guide now cites actual isolate interventions and excludes causal tags from correlations. Issue2777's table omission and2778's residual node4 direction are directly checked; no fabricated historical structured finding is introduced.",
        path="docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
    )
    for cache in ("PMID_40920748.md", "doi_10.1126_sciadv.adg7888.md", "PMID_42660928.md"):
        ev(
            "cache-" + cache.replace(".md", "").replace(".", "-"),
            "record_content",
            "references_cache/" + cache,
            "frontmatter plus main-article boundary and unchanged payload",
            "Header accurately states abstract_and_full_text; exact byte comparison against reviewed baseline preserves article identity, source text and main/supplement separation. Header correction does not repair unrelated claim-scope defects.",
            path="references_cache/" + cache,
        )
    ev(
        "history",
        "record_content",
        "history/records and history/other",
        "eight new2026-11-14 sidecars plus four appended inline EDIT events",
        "Record and cache changes have new native sidecars; all four inline events identify codex and llm_assisted. The initial EcoFAB sidecar's accidental claude-code default is preserved and explicitly corrected by a later codex AUDIT entry, not rewritten. Two SynCom edits retain distinct provenance. Prior eighteen sidecar files remain byte-identical.",
    )

    # Explicit checks are supplied by the coordinator after frozen M5 execution.
    # Missing inputs stay unavailable and prevent terminal finding dispositions.
    supplied = {}
    for text in args.gate:
        key, path = text.split("=", 1)
        if key in supplied:
            raise ValueError("Duplicate gate: " + key)
        supplied[key] = path
    required = {short + "." + gate for short in ("000025", "000515", "000516") for gate in GATES}
    required.update({"all.docs-current", "all.history-all", "all.cache-tests"})
    if not set(supplied) <= required | {"all.gen-html", "all.aggregate-qc", "all.products"}:
        raise ValueError("Unexpected gate key")
    checks = []
    verified_revisions = set()
    validation_inputs = [t["path"] for t in targets.values()] + [
        "references_cache/PMID_40920748.md",
        "references_cache/doi_10.1126_sciadv.adg7888.md",
        "references_cache/PMID_42660928.md",
        "src/communitymech/schema/communitymech.yaml",
        "docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
        "conf/reference_validator.yaml",
        "uv.lock",
        "justfile",
    ]
    validation_inputs.extend(
        item["path"] for item in initial["source"]["inputs"] if item["path"].startswith("history/")
    )
    for key in sorted(required | set(supplied)):
        short, category = key.split(".", 1)
        ids = target_ids if short == "all" else ["CommunityMech:" + short]
        check = {
            "check_id": "post-" + key.replace(".", "-"),
            "name": "Post-curation " + key,
            "required": key in required,
            "target_ids": ids,
            "status": "unavailable",
            "summary": "Final native receipt has not been supplied; not counted as passed.",
            "scope_note": "Bounded post-curation acceptance gate; separate full repository QC is not inferred.",
        }
        if key in supplied:
            path = supplied[key]
            receipt = json.loads((ROOT / path).read_text())
            log_path = receipt["log"]
            if (
                digest(ROOT / log_path) != receipt["log_sha256"]
                or not (ROOT / log_path).stat().st_size
            ):
                raise ValueError("Receipt log absent, empty or changed: " + key)
            if not receipt.get("finished_at") or receipt.get("dry_run"):
                raise ValueError("Receipt not a completed live check: " + key)
            passed = verify_gate_binding(
                key, receipt, targets, args.expected_revision, validation_inputs, verified_revisions
            )
            evidence_id = "gate-" + key.replace(".", "-")
            ev(
                evidence_id,
                "validation",
                log_path,
                "Complete persisted native log; exact command, revision and hash in receipt",
                "Receipt "
                + receipt["name"]
                + " finished "
                + receipt["finished_at"]
                + "; native exit="
                + str(receipt["exit_code"])
                + ". No deterministic result is treated as primary scientific proof.",
                path=log_path,
            )
            inputs.add(path)
            check.update(
                status="passed" if passed else "failed",
                summary="Verified actual persisted native receipt and log bytes.",
                command=shlex.join(receipt["command"]),
                exit_code=receipt["exit_code"],
                expected_exit_code=0,
                evidence_ids=[evidence_id],
            )
            if category == "cache-tests" and receipt["exit_code"] != 0 and passed:
                check["summary"] = (
                    "Native test dependency passed; enclosing QC later failed. Only the test stage is accepted here."
                )
                check.pop("exit_code")
            checks.append(check)
        else:
            checks.append(check)
    ready = all(check["status"] == "passed" for check in checks if check["required"])

    assessments = []

    def assess(key, area, topic, summary, ids, evidence_ids, outcome="supported", details=None):
        item = {
            "assessment_id": key,
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "target_ids": ids,
            "evidence_ids": evidence_ids,
        }
        if details:
            item["details"] = details
        assessments.append(item)
        return item

    assess(
        "ecofab-delta",
        "scope",
        "Ring17-to-dopamine16 relationship and retained scientific findings",
        OUTCOMES["cm-000025-dopamine-relation-description"],
        ["CommunityMech:000025"],
        ["record-000025", "ring-stocks", "dopamine-stocks", "delta"],
        details="Exact selector related_communities[0].description. Identity/stock set, hostBd21-3, sterile-start versus post-inoculation status, five nodes and four downstream arrows are unchanged; the original full scientific assessment remains authoritative. Four unrelated retained findings are reassessed below, not cleared by this correction.",
    )
    assess(
        "yolo-delta",
        "grounding",
        "Six reproduced taxonomic votes without unmeasured function",
        OUTCOMES["cm-000515-gtdb-copied-mechanism-provenance"],
        ["CommunityMech:000515"],
        ["record-000515", "soil-evidence", "mapping", "delta"],
        details="Selectors taxonomy[0:6].taxon_term.gtdb_classification.mapping_source and taxonomy[4] curation_note. Natural-soil community, nohost,20gsoil, six-weekamendments, six measured control abundances, two bounded relative16S nodes and zero arrows are unchanged. The wider GTDB taxonomic interpretation is not newly certified beyond the reproduced numerical support and explicit uncertainty.",
    )
    assess(
        "syncom-nodes-0-1",
        "graph",
        "Correlation-only nodes preserve observational direction in prose",
        OUTCOMES["cm-000516-correlation-direction-scope"],
        ["CommunityMech:000516"],
        ["record-000516", "correlations", "isolate-interventions", "schema-guidance", "delta"],
        details="Exact fields ecological_interactions[0/1].host_participation/effect_direction. Source observation: dopamine ion signal versus member relative16S across genotypes; five positive stocks and negativeOAS925. No treatment-to-member mechanism follows. All claim-local source evidence, phenotypic context and signed association descriptions remain.",
    )
    assess(
        "syncom-node-4",
        "graph",
        "Whole-SynCom-to-extracellular dopamine endpoint without reversed causal tags",
        OUTCOMES["cm-000516-exudate-decrease-host-target-scope"],
        ["CommunityMech:000516"],
        ["record-000516", "extracellular-endpoint", "schema-guidance", "delta"],
        details="Exact fields ecological_interactions[4].host_participation/effect_direction; Fig2c, pooled genotypes harvested at week4 after week1 inoculation, SynCom n29 versus axenic n28. All16participants and two quotations unchanged. This corrects2710 and independently verifies issue-only2778; does not identify which organism consumes dopamine or prove altered plant metabolism.",
    )
    assess(
        "syncom-preservation",
        "graph",
        "Measured isolate nodes, membership and all downstream edges preserved",
        "Nodes2/3 retain dopamine-to-isolate growth signs at the supported dose/assay; the16-stock roster and hostgenotype context are unchanged. All five nodes have zero downstream arrows. Source-to-target signs are retained only where the underlying intervention measures that response.",
        ["CommunityMech:000516"],
        ["record-000516", "isolate-interventions", "delta"],
    )
    cache_ids = [row["evidence_id"] for row in evidence if row["evidence_id"].startswith("cache-")]
    assess(
        "cache-metadata",
        "provenance",
        "Three article payloads and shared-consumer coverage",
        "Both cache findings are addressed by content declarations only; all payload/source-boundary bytes are unchanged. Ring/nitrogen caches cover000025; Ding cache covers both000515 and000516. Fresh reference gates are required independently for each consumer.",
        target_ids,
        ["delta", *cache_ids],
    )
    assess(
        "append-only-history",
        "provenance",
        "New record/cache events and attribution correction",
        "Inspected receipts and native sidecars agree with exact changed fields. Prior history remains unchanged; accidental actor naming was corrected with an additional audit sidecar. No review action itself appends history or promotes scientific status.",
        target_ids,
        ["history", "delta"],
    )
    assess(
        "issue-only-corrections",
        "consistency",
        "Directly verified2777 and2778 without invented predecessors",
        "The guide table no longer advertises absent host tags (#2777), and node4 no longer carries reversed effect_direction (#2778). Both corrections have been directly assessed. These issue-only observations are linked context, not new terminal structured findings or automatic GitHub closure.",
        ["CommunityMech:000516"],
        ["schema-guidance", "extracellular-endpoint", "delta"],
        details="Existing issue records: https://github.com/CultureBotAI/CommunityMech/issues/2777 and https://github.com/CultureBotAI/CommunityMech/issues/2778.",
    )

    priors = {}
    for index, source in enumerate(acceptance["prior_review_inputs"]):
        review = read_yaml(ROOT / source["path"])
        priors[source["review_id"]] = ("prior" + str(index), review)
        ev(
            "prior" + str(index),
            "prior_review",
            source["path"],
            "immutable full scientific review; current predecessor finding heads",
            "Source-backed full baseline review retained for unchanged claims. Its old validator receipts and source hashes are historical; current gates are listed separately.",
            "context_only",
            path=source["path"],
        )
    findings = []
    actions = []
    for entry in acceptance["finding_acceptance_map"]:
        key = entry["issue_key"]
        finding = copy.deepcopy(entry["prior_findings"][0])
        finding.update(
            finding_id=key,
            target_ids=entry["target_ids"],
            previous_occurrences=entry["previous_occurrences"],
        )
        finding["evidence_ids"] = ["delta"]
        merged_paths, merged_owners, merged_issues = [], [], []
        for prior_finding, reference in zip(
            entry["prior_findings"], entry["previous_occurrences"], strict=True
        ):
            prefix, prior = priors[reference["review_id"]]
            finding["evidence_ids"].append(prefix)
            prior_evidence = {row["evidence_id"]: row for row in prior["evidence"]}
            for identifier in prior_finding["evidence_ids"]:
                new_id = prefix + "-" + identifier
                if not any(row["evidence_id"] == new_id for row in evidence):
                    copied = copy.deepcopy(prior_evidence[identifier])
                    copied["evidence_id"] = new_id
                    copied["summary"] = (
                        "Retained historical evidence from "
                        + prior["review_id"]
                        + ": "
                        + copied["summary"]
                    )
                    evidence.append(copied)
                finding["evidence_ids"].append(new_id)
            for name, destination in (
                ("field_paths", merged_paths),
                ("owner_paths", merged_owners),
                ("external_issues", merged_issues),
            ):
                for value in prior_finding.get(name, []):
                    if value not in destination:
                        destination.append(value)
        finding.update(
            field_paths=merged_paths, owner_paths=merged_owners, external_issues=merged_issues
        )
        finding["evidence_ids"] = list(dict.fromkeys(finding["evidence_ids"]))
        if key in OUTCOMES:
            finding["description"] = (
                "Predecessor defect: "
                + finding["description"]
                + " Current assessment: "
                + OUTCOMES[key]
            )
            finding["status"] = "resolved" if ready else "open"
            finding["disposition_reason"] = OUTCOMES[key] + (
                " All required post-curation native gates are verified. This is scoped finding resolution, not release approval or GitHub issue closure."
                if ready
                else " Scientific correction is supported, but final required native receipts remain pending; no terminal disposition yet."
            )
            finding["evidence_ids"].extend(
                {
                    "cm-000025-cache-content-type": cache_ids,
                    "cm-000025-dopamine-relation-description": [
                        "ring-stocks",
                        "dopamine-stocks",
                        "record-000025",
                    ],
                    "cm-000515-gtdb-copied-mechanism-provenance": [
                        "soil-evidence",
                        "mapping",
                        "record-000515",
                    ],
                    "cm-pmid42660928-cache-content-type": cache_ids,
                    "cm-000516-exudate-decrease-host-target-scope": [
                        "extracellular-endpoint",
                        "record-000516",
                        "schema-guidance",
                    ],
                    "cm-000516-correlation-direction-scope": [
                        "correlations",
                        "isolate-interventions",
                        "record-000516",
                        "schema-guidance",
                    ],
                }[key]
            )
            if not ready:
                actions.append(
                    {
                        "action_id": "verify-" + key,
                        "description": "Verify final native acceptance before terminal disposition.",
                        "finding_ids": [key],
                        "target_ids": entry["target_ids"],
                        "owner_paths": merged_owners,
                        "acceptance_checks": entry["acceptance"],
                    }
                )
        else:
            finding["status"] = "open"
            finding[
                "description"
            ] += " Current delta leaves these exact scientific selectors unchanged. The primary-source assessment and unresolved action remain applicable."
            assess(
                "retained-" + key,
                finding["category"],
                finding["title"],
                "Re-inspected predecessor selectors remain semantically identical; this bounded curation does not address their documented scientific/provenance concern.",
                finding["target_ids"],
                finding["evidence_ids"],
                "concern",
            )
            for reference in entry["previous_occurrences"]:
                prefix, prior = priors[reference["review_id"]]
                for action in prior["actions"]:
                    if reference["finding_id"] in action["finding_ids"]:
                        copied = copy.deepcopy(action)
                        copied.update(
                            action_id=prefix + "-" + action["action_id"], finding_ids=[key]
                        )
                        actions.append(copied)
        findings.append(finding)

    for key, record in records.items():
        short = key.split(":")[1]
        nodes = record.get("ecological_interactions", [])
        excerpts = sum(len(node.get("evidence", [])) for node in nodes)
        counts = {
            p: sum(
                key in f["target_ids"] and f["status"] == "open" and f["native_severity"] == p
                for f in findings
            )
            for p in ("P1", "P2", "P3", "P4")
        }
        required_present = all(
            record.get(k)
            for k in (
                "id",
                "name",
                "description",
                "taxonomy",
                "ecological_state",
                "community_category",
            )
        ) and all(t.get("functional_role") for t in record["taxonomy"])
        components = [
            50 * required_present,
            5 * bool(record.get("environment_term")),
            10 * (len(record.get("environmental_factors", [])) >= 3),
            10 * (len(nodes) >= 3),
            5 * bool(record.get("external_resources")),
            10 * bool(record.get("growth_media")),
            5 * bool(record.get("associated_datasets")),
            5 * any("metabolites" in node for node in nodes),
        ]
        member_ids = {member["taxon_term"]["term"]["id"] for member in record["taxonomy"]}
        graph_complete = all(
            t["term"]["id"] in member_ids
            for node in nodes
            for t in node.get("participating_taxa", [])
        )
        raw = (
            100
            - 50 * counts["P1"]
            - 10 * counts["P2"]
            - 2 * counts["P3"]
            + min(excerpts / len(nodes) / 2, 1) * 20
            + 15 * graph_complete
        )
        row = assess(
            "metrics-" + short,
            "completeness",
            "Native diagnostic scores with retained findings visible",
            "Metrics are recomputed from current structure and all retained predecessor findings; no whole-record scientific pass follows from capped quality or completeness.",
            [key],
            ["record-" + short, "delta"],
        )
        row["metrics"] = [
            {
                "name": "completeness",
                "value": min(100, sum(components)),
                "unit": "points",
                "minimum": 0,
                "maximum": 100,
                "definition": "Native50required-with-all-member-roles+5environment+10three-factors+10three-nodes+5resources+10medium+5datasets+5node-metabolites; components="
                + str(components)
                + ". Presence is not source support.",
            },
            {
                "name": "validation_quality",
                "value": max(0, min(100, raw)),
                "unit": "points",
                "minimum": 0,
                "maximum": 100,
                "denominator": len(nodes),
                "definition": f"100-50P1-10P2-2P3+20min(({excerpts}/{len(nodes)})/2,1)+15structural-membership-completeness; counts={counts}; raw={raw}; capped0..100. Only retained current finding heads contribute; no scientific clearance.",
            },
            {
                "name": "evidence_per_interaction",
                "value": excerpts / len(nodes),
                "unit": "excerpts per node",
                "denominator": len(nodes),
                "definition": "Graph evidence-entry count divided by interaction nodes; not unique sources or claim coverage.",
            },
        ] + [
            {
                "name": p,
                "value": count,
                "unit": "open findings",
                "definition": "Current unresolved native finding count for this target in the predecessor-aware delta.",
            }
            for p, count in counts.items()
        ]

    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(STATE / "postcuration-targets.yaml"),
    ]
    for filename in sorted(inputs):
        command.extend(["--input", filename])
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
    inspected = json.loads(result.stdout)
    (STATE / "postcuration-final-inspection.json").write_text(result.stdout)
    review = {
        "schema_version": "1.0.0",
        "review_id": now.strftime("%Y%m%dT%H%M%SZ") + "-m5-postcuration-scientific-delta",
        "kind": "batch",
        "repository": REPOSITORY,
        "title": "Three-record M5 post-curation scientific delta",
        "started_at": datetime.fromtimestamp(
            (STATE / "postcuration-initial-inspection.json").stat().st_mtime, timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "finished_at": finished,
        "reviewer": {
            "identity": "codex-community-m5",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Not author of canonical corrections or the three predecessor bundles. Independently inspected primary sources, read baseline records, reviewed exact frozen deltas and verified retained claim scopes. Authored this successor; root performs its separate adversarial review.",
        },
        "skill": "review-communities",
        "completion": "completed" if ready else "partial",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": (
            "Bounded scientific delta assessed for three changed records and three article caches. "
            + (
                "Six stable finding keys are resolved with fresh native gates; five remain open. "
                if ready
                else "Six scientifically supported corrections await native acceptance receipts; all eleven keys remain open in this staging observation. "
            )
            + "Partial field coverage is explicit. Shared2708 retains both consumers. This is not full repository technical completion, nor an automatic issue closure."
        ),
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Only corrected relation, mapping rationale/provenance, causal tags, cache declarations, related guidance/history and all affected predecessor selectors. Other claims retain their full baseline reviews.",
            "selection": "All three canonical records changed after four-record primary scientific assessment; no sample or inferred enlargement.",
            "coverage": "partial",
            "population_size": 3,
            "reviewed_target_ids": target_ids,
            "exclusions": [
                {
                    "target": "CommunityMech:000087",
                    "reason": "Unchanged target; two major1548 findings and minor2776 addendum remain in their own immutable bundles, not superseded.",
                },
                {
                    "target": "Repository-wide features and full QC",
                    "reason": "Separate coordinator work; this scoped successor neither certifies completion nor hides ongoing/failed aggregate gates.",
                },
            ],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "This completed-or-partial status refers only to the explicit delta scope. Full record reviews and their primary evidence remain historical linked observations; no entire-record pass or corpus-wide scientific review is inferred.",
            "Five unresolved predecessor keys remain open: two EcoFAB major causal/study-scope findings and three minor grounding/genome-provenance findings across EcoFAB and dopamine SynCom. Unchanged000087 findings1548/2776 remain outside this review.",
            "Original source interpretations and unchanged nodes/edges are preserved. No new raw sequencing/metabolomics reanalysis, strain identification, paid provider call or functional inference was performed.",
            "Generated documentation and native checks prove bounded technical properties, not primary scientific support. Full repository QC and reference backlog are reported separately and can remain incomplete despite this review's scoped acceptance.",
            "The C1 aggregate QC failed its native test stage; required later aggregate stages were not thereby completed. The separate product diagnostic failed because generated output/kgx/nodes.tsv was missing and reported553 SKIPPED_NO_ADAPTER entries. These observed technical limitations remain explicit optional context and are not converted into passes by the24 scoped acceptance gates.",
            "Terminal dispositions reconcile exact prior structured occurrences only. Issues2777/2778 are directly verified issue-linked corrections without fabricated predecessor findings. No GitHub issue is automatically closed.",
        ],
        "related_reviews": [
            {
                "repository": REPOSITORY,
                "review_id": source["review_id"],
                "relationship": "Exact predecessor heads reassessed in bounded correction; unchanged full scientific scope retained.",
            }
            for source in acceptance["prior_review_inputs"]
        ]
        + [
            {
                "repository": REPOSITORY,
                "review_id": source["review_id"],
                "relationship": "Unchanged000087 context excluded; every open finding retained without supersession.",
            }
            for source in acceptance["excluded_context"]
        ],
    }
    if len(findings) != 11 or sum(f["status"] == "resolved" for f in findings) != (
        6 if ready else 0
    ):
        raise ValueError("Unexpected predecessor/disposition count")
    output = STATE / "postcuration-scientific-delta.yaml"
    output.write_text(
        yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=100)
    )
    print(
        json.dumps(
            {
                "path": str(output.relative_to(ROOT)),
                "completion": review["completion"],
                "resolved_keys": sum(f["status"] == "resolved" for f in findings),
                "open_keys": sum(f["status"] == "open" for f in findings),
            }
        )
    )


if __name__ == "__main__":
    main()
