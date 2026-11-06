"""Build a JSON successor candidate and use native immutable review persistence."""

from __future__ import annotations

import argparse
import copy
import json
from datetime import datetime, timezone

import yaml
from pr2053_175_audit import COMMON, ID, OLD, ROOT, SCRATCH, TARGET, now, run, sha, write

REPOSITORY = "CultureBotAI/CommunityMech"
CHECKS = ["validate", "validate-strict", "validate-terms", "validate-gtdb",
          "validate-gtdb-domain", "validate-history", "normalize-cache-names-check",
          "validate-references-explained", "audit-network", "check-network-quality"]
PRIMARY_2007 = "https://www.academia.edu/11977828/Electricity_production_from_cellulose_in_a_microbial_fuel_cell_using_a_defined_binary_culture"
PRIMARY_2008 = "https://www.academia.edu/11977824/Electricity_production_and_microbial_biofilm_characterization_in_cellulose_fed_microbial_fuel_cells"


def load(name):
    return json.loads((SCRATCH / name).read_text())


def evidence(eid, kind, path, locator, summary, reference=None):
    return {"evidence_id": eid, "kind": kind, "reference": reference or path,
            "locator": locator, "summary": summary, "support": "supports",
            "accessed_at": now(), "snapshot_sha256": sha((ROOT / path).read_bytes())}


def build(label):
    old = yaml.safe_load((ROOT / OLD).read_text())
    initial = load("initial-inspection.json")
    for item in initial["source"]["inputs"]:
        assert sha((ROOT / item["path"]).read_bytes()) == item["sha256"], item["path"]
    paths = {x["path"] for x in initial["source"]["inputs"] if x["role"] != "target"}
    paths.update(str(p.relative_to(ROOT)) for p in (ROOT / "scripts/adhoc").glob("pr2053_175_*.py"))
    names = ["initial-inspection.json", "initial-inspect.json", "initial-targets.json",
             "initial-lineage.json", "initial-target-diff.stdout.txt",
             "initial-frozen-target.stdout.txt", "initial-local-search.stdout.txt",
             "support-final.json", "web-primary-main.json", "strict.tsv"]
    for name in CHECKS:
        names.extend([name + ".json", name + ".stdout.txt", name + ".stderr.txt"])
    for name in ["pubmed-175.xml", "epmc-175.json", "academia-2007.html",
                 "academia-2008.html", "taxonomy-175.xml", "CHEBI18246.json",
                 "CHEBI85146.json", "CHEBI234035.json", "imodulon-catalog.json"]:
        names.extend([name, name + ".receipt.json"])
    paths.update(str((SCRATCH / name).relative_to(ROOT)) for name in names)
    paths.update(f".temp/pr2053/issue{n}.json" for n in [1324, 1327, 1744, 2073])
    paths.update([".temp/pr2053/independent-secondary/gtdb-exact-rows.json",
                  ".temp/pr2053/independent-secondary/gtdb-community-mode.json",
                  ".temp/pr2053/independent-secondary/175-gtdb-authority.txt"])
    paths.update(".temp/pr2053/adversarial/" + name for name in [
        "175-missing-source-ranges.json", "175-final-source-ranges.json",
        "175-extraction-coverage.json"])
    args = ["uv", "run", "python", "scripts/record_review.py", "inspect", "--targets",
            str(SCRATCH / "initial-targets.json")]
    for path in sorted(paths):
        args += ["--input", path]
    inspected = run("final-inspect-" + label, args)
    assert inspected.returncode == 0, inspected.stderr.decode()
    final = json.loads(inspected.stdout)
    write("final-inspection-" + label, final)
    review = copy.deepcopy(old)
    review.update({
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-pr2053-cellulose-mfc-current-input-refresh",
        "title": "Cellulose MFC coculture: current taxon-link and source-scope refresh",
        "started_at": load("initial-inspect.json")["started_at"], "finished_at": now(),
        "reviewer": {"identity": "codex", "kind": "agent", "independence": "self_review",
                     "independence_basis": "Author refresh of PR 2053's stale record 175 observation. A separate read-only adversarial pass evaluates the committed result; this bundle does not claim independent approval."},
        "completion": "partial", "verdict": "needs_curation", "scientific_review": False,
        "summary": "The new reusable Geobacter link resolves to the correct species and preserves focal-system scope. Four existing curation findings remain open: metabolite/recipient-role evidence, CMC identity, study-specific cultivation, and strain/mapping provenance. Both primary full-text extractions are now read; unverified figure pixels and typography keep scientific completion partial. All eight focused native checks pass.",
        "source": final["source"], "targets": final["targets"],
        "scope": {"description": "Entire current maintained record, three interaction nodes and one arrow; new common-taxon identity link, both fresh primary abstracts and publicly accessible complete article text/captions. Figure pixels, raw data and the reusable taxon's unrelated experimental claims are not certified.",
                  "selection": "The sole stale record identified in PR 2053 after merging current main.",
                  "coverage": "partial", "population_size": 1, "reviewed_target_ids": [ID]},
    })
    prefix = ".temp/pr2053/175/"
    ev = [
        evidence("record", "record_content", TARGET, "Entire current maintained YAML", "The only record delta since the original review is taxonomy[1].common_taxon and its append-only history. All four original concern areas remain unchanged."),
        evidence("delta", "validation", prefix + "initial-target-diff.stdout.txt", "Historical input versus current main", "Exact diff contains the reusable taxon link and corresponding history entry; it does not alter graph, media, evidence, or species assignments."),
        evidence("common", "record_content", COMMON, "Identifier, taxon_term, PCA context, genes and curation history", "CommunityMech:taxon:000002 has the same Geobacter sulfurreducens NCBITaxon:35554 identity. Its other-community gene, DIET and assembly examples do not establish those mechanisms in the cellulose MFC."),
        evidence("abstracts", "database", prefix + "pubmed-175.xml", "Two exact PMID/DOI/title records and complete primary abstracts", "The two records identify the exact binary MFC studies, distinguish the activated-sludge comparison, and support the source-specific current/degradation and spatial endpoints.", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17695929,18725730&retmode=xml"),
        evidence("main-2007", "primary_source", prefix + "web-primary-main.json", "Complete public text extraction: Materials and Methods, Results, Discussion, Table 1, four captions and references; snapshot is the web-reader response, not original PDF bytes", "Both study stocks are named. The text reports complete medium/catholyte replacement, separate preparation and experimental stages, acetate controls and endpoint metabolite comparisons. Product-inhibition relief is the authors' interpretation; metabolite-specific partner flux and a Geobacter-derived resource consumed by Clostridium are not isolated. Figure pixels remain unverified.", PRIMARY_2007),
        evidence("main-2008", "primary_source", prefix + "web-primary-main.json", "Complete public text extraction: Methods, Results/Discussion, five captions and references; snapshot is the web-reader response, not original PDF bytes", "The source separates CMC and MN301 reactors, anode and catholyte, source-specific medium and electrode geometry, FISH localization and qPCR gene-copy comparisons. The proposed settling/decanting improvement was not a tested causal perturbation. Extraction corrupts some degree, ohm and micro-unit glyphs; those values require independently readable rendering.", PRIMARY_2008),
        evidence("access", "validation", prefix + "web-primary-main.json", "Public web-reader article extractions; separate direct-curl receipts retained", "Both complete article text extractions were inspected. Direct curl returned 403 challenge pages, not PDF or visual evidence. No original PDF equivalence or figure-pixel inspection is claimed. Earlier unavailable-2007 statements remain historical, not the current access assessment."),
        evidence("support", "validation", prefix + "support-final.json", "Fresh abstract replay, native term labels, target graph and linked identity", "All 28 reference-specific abstract snippet occurrences match after NFKC/whitespace normalization; all 25 encoded ID-label occurrences match. Target graph is structurally COMPLETE. These checks do not establish biological entailment or correct CMC semantic identity."),
        evidence("cmc", "authority", prefix + "CHEBI85146.json", "Current ChEBI derivative definition", "CHEBI:85146 is carboxymethylcellulose, a substituted cellulose derivative; CHEBI:18246 represents the unmodified backbone. Preserve generic cellulose and MN301 contexts.", "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:85146"),
        evidence("cmc-salt", "authority", prefix + "CHEBI234035.json", "Current label and available definition fields", "CHEBI:234035 is carboxymethylcellulose sodium salt. This response has no definition; source-specific reagent wording remains necessary.", "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:234035"),
        evidence("taxa", "authority", prefix + "taxonomy-175.xml", "Species, strain parents and type-material aliases", "Species 1521/35554 and strains 394503/243231 resolve consistently. Type-material aliases connect ATCC 35319, DSM 5812 and H10, and ATCC 51573, DSM 12127 and PCA. Catalogue maintenance is not the study protocol.", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1521,35554,394503,243231&retmode=xml"),
        evidence("gtdb", "authority", ".temp/pr2053/independent-secondary/gtdb-exact-rows.json", "Independent current exact-ID crosswalk replay, with community-mode control", "Snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd supports species counts 1 and 19 at majority 1.0. Optional strain rows each have two genomes. File mtime does not establish a release or build date."),
        evidence("schema", "authority", "src/communitymech/schema/communitymech.yaml", "FunctionalRoleEnum, InteractionTypeEnum, AbundanceEnum, CultivationModeEnum and common_taxon", "Recipient CROSS_FEEDER requires utilization; SYNTROPHY does not require obligacy. Ordinal ABUNDANT has no fixed percentage threshold. FED_BATCH excludes broth removal; the literal operation must determine mode."),
        evidence("history", "prior_review", prefix + "initial-lineage.json", "Original four single-target findings and Cycle 2 multi-target link findings/remediation", "The prior single-target findings are reassessed explicitly. The later common-taxon remediation and closed issue 2073 are preserved; this narrower review does not supersede multi-target dispositions."),
        evidence("issues", "prior_review", ".temp/pr2053/issue1327.json", "Current issue body and all returned comments; other issue states separately pinned", "Issue 1327 remains open for non-graph curation. Closed 1324 preserves the graph repair; open 1744 explicitly retains this record's classification. No closure of these curation issues follows from this review."),
        evidence("inspection", "validation", prefix + "initial-inspection.json", "Native current-input inspection using the current AGENTS rubric", "Initial target/context hashes were rechecked before adding current source, authority, check and helper pins. The final working-tree snapshot remains a reviewer byte attestation, not a claim that ignored research artifacts were committed."),
        evidence("adapter", "database", prefix + "imodulon-catalog.json", "Complete returned public organism catalogue", "No focal Geobacter or cellulolyticum organism match occurs in this catalogue. No expression-module evidence is used to infer focal phenotype or transfer.", "https://imodulondb.org/api/datasets"),
    ]
    checks = []
    for name in ["175-missing-source-ranges.json", "175-final-source-ranges.json",
                 "175-extraction-coverage.json"]:
        ev.append(evidence("source-" + name.removesuffix(".json"), "validation",
                           ".temp/pr2053/adversarial/" + name,
                           "Supplemental public-reader ranges, independently retrieved and author-read before final input freezing",
                           "Together with web-primary-main.json these receipts cover all 79 lines of the 2007 extraction and all 60 lines of the 2008 extraction. They are parsed web responses, not original PDF bytes or figure pixels."))
    for item in ev:
        if item["evidence_id"] in {"main-2007", "main-2008"}:
            item["locator"] = item["locator"].replace(
                "Complete public text extraction:",
                "Public text extraction; full coverage is distributed across this snapshot and the separately pinned source-range receipts:")
        if item["evidence_id"] == "access":
            item["locator"] += "; complete coverage requires both separately pinned source-range supplements"
    for name in CHECKS:
        receipt = load(name + ".json")
        corpus = name in {"audit-network", "check-network-quality"}
        ev.append(evidence("check-" + name, "validation", prefix + name + ".json", "Actual command, times, exit and output digests", "Corpus diagnostic: 48 warnings, zero errors across 17/510 records; target-specific graph has no issue." if corpus else "Focused native command and immutable output receipts."))
        checks.append({"check_id": name, "name": name, "status": "passed" if receipt["exit_code"] == 0 else "failed",
                       "required": not corpus, "command": receipt["command"], "exit_code": receipt["exit_code"],
                       "expected_exit_code": 0, "target_ids": [ID], "evidence_ids": ["check-" + name],
                       "summary": "Actual corpus warning-only diagnostic retained; no validator weakened." if corpus else "Focused native command exit 0.",
                       "scope_note": "Current record-only gate." if not corpus else "Corpus diagnostic, not a new all-record scientific assessment."})
    checks.extend([
        {"check_id": "scientific-source", "name": "Claim-critical visual/source verification", "status": "unavailable", "required": True, "summary": "Both main text extractions read; original figure pixels and ambiguous typography not verified. Partial scientific status retained.", "target_ids": [ID], "evidence_ids": ["main-2007", "main-2008", "access"]},
        {"check_id": "direct-excerpts", "name": "Fresh reference-specific excerpts", "status": "passed", "required": True, "summary": "All 28 abstract excerpt occurrences match; no current cache enrichment performed.", "target_ids": [ID], "evidence_ids": ["support"]},
        {"check_id": "authority-review", "name": "Identifier, schema and taxon-link scope", "status": "passed", "required": True, "summary": "Encoded labels, species/type-material identity, exact crosswalk rows and new reusable link independently checked; semantic concerns retained.", "target_ids": [ID], "evidence_ids": ["support", "taxa", "gtdb", "cmc", "cmc-salt", "schema", "common"]},
        {"check_id": "adapter", "name": "Focal structured expression adapter", "status": "not_applicable", "required": False, "summary": "No focal organism in the current public catalogue; this is not negative biological evidence.", "target_ids": [ID], "evidence_ids": ["adapter"]},
        {"check_id": "reanalysis", "name": "Raw-data and experimental reproduction", "status": "skipped", "required": False, "summary": "No raw-image, qPCR, current-trace, sequence or culture reanalysis.", "target_ids": [ID], "evidence_ids": ["access"]},
    ])
    review["evidence"], review["checks"] = ev, checks
    for assessment in review["assessments"]:
        assessment["evidence_ids"] = ["record", "abstracts", "main-2007", "main-2008", "support", "schema"]
    by_id = {a["assessment_id"]: a for a in review["assessments"]}
    by_id["taxonomy"]["evidence_ids"] = ["taxa", "gtdb", "common", "main-2007", "main-2008"]
    by_id["taxonomy"]["details"] = "Both primary texts identify the same collection stocks; current species terms and the new reusable Geobacter identity link are consistent. Optional strain refinement must retain the species-versus-strain mapping denominators. The link does not import unrelated DIET/gene experiments into this community."
    by_id["chemical-identity"]["evidence_ids"] = ["cmc", "cmc-salt", "main-2008"]
    by_id["cultivation"]["summary"] = "Recoverable study-specific Methods should replace stale workflow prose while preserving distinct protocols."
    by_id["cultivation"]["details"] = "Separate precursor cultures, final substrate arms, anode/catholyte compartments, capacity/working volume and study-specific power results. Both sources describe medium replacement. Author terminology does not override the native operation definition. The 2008 extraction's ambiguous glyphs require visual verification."
    by_id["evidence"]["details"] = "Both maintained caches remain correctly abstract-only; newly read complete public text extractions can support separately authorized evidence enrichment with precise provenance. Figure pixels and original PDF equivalence remain unverified; completion remains partial."
    by_id["provenance"]["summary"] = "The current common-taxon change and prior review lineage are reconciled without retiring unrelated findings."
    by_id["provenance"]["details"] = "Only the four original single-target findings receive previous_occurrences. The multi-target Cycle 2 link-gap dispositions and closed 2073 remain context; other affected communities are not reassessed. Open 1327 remains the curation owner."
    by_id["provenance"]["evidence_ids"] = ["history", "issues", "inspection", "delta", "common"]
    by_id["validation"]["evidence_ids"] = ["support", "access"] + ["check-" + n for n in CHECKS]
    by_id["validation"]["details"] = "Eight focused native gates pass. Corpus diagnostics retain 48 warnings/zero errors; target connectivity is complete. Full-source text access improved, but no figure-pixel certification or canonical change occurred."
    by_id["metrics"]["evidence_ids"] = ["support"]
    by_id["identity"]["dimensions"] = [
        {"name": "community_scope", "value": "Defined two-member laboratory MFC", "definition": "Excludes activated-sludge comparators and analytical cloning hosts.", "evidence_ids": ["record", "abstracts"]},
        {"name": "study_stocks", "value": "ATCC 35319 and ATCC 51573", "definition": "Explicit focal stock designations, linked to H10 and PCA type-material authority without transferring catalogue maintenance conditions.", "evidence_ids": ["main-2007", "main-2008", "taxa"]},
    ]
    for finding in review["findings"]:
        finding["previous_occurrences"] = [{"repository": REPOSITORY, "review_id": old["review_id"], "finding_id": finding["finding_id"]}]
        finding["evidence_ids"] = ["record", "main-2007", "main-2008", "support", "schema"]
        finding["ownership_note"] = "Canonical/source curation remains outside PR 2053. Preserve open 1327, closed graph repair 1324 and the completed common-taxon linkage tracked by 2073."
    findings = {f["finding_id"]: f for f in review["findings"]}
    findings["qualify-metabolite-use"]["description"] = "The donor's optional CROSS_FEEDER role still lacks evidence of utilization of a Geobacter product. Ingredient assertions attach only a residual-metabolite snippet; strengthen their local source attribution or qualify the inferred molecule-specific transfer. Newly accessible main-text controls and author interpretations inform this repair without establishing partner-resolved flux or a reciprocal recipient role. Preserve the qualified graph."
    findings["ground-cmc-derivative"]["evidence_ids"] = ["record", "cmc", "cmc-salt", "main-2008"]
    findings["recover-study-protocol"]["description"] = "Current cultivation notes retain unrelated workflow history and unavailable-Methods statements. Both primary text extractions are now accessible. Recover study-specific preparation, substrate arms and apparatus without merging recipes, power values or compartments; distinguish author fed-batch terminology from medium replacement and native mode semantics."
    findings["document-strain-mapping"]["description"] = "Both primary texts name exact culture stocks, while mapping_source still asserts a latest release/build date without sufficient provenance. Add source-specific strain context and the examined snapshot/method; preserve current species mappings and ordinal abundance. The newly added common_taxon link is valid and should remain."
    findings["document-strain-mapping"]["evidence_ids"] = ["record", "taxa", "gtdb", "common", "main-2007", "main-2008"]
    actions = {a["action_id"]: a for a in review["actions"]}
    actions["ground-cmc"]["acceptance_checks"][1] = "Keep CHEBI:18246 for MN301 and generic cellulose contexts. Both study texts name sodium CMC; do not infer a shared formulation, substitution degree or grade from another study or ambiguous extraction. Verify any proposed numerical reagent specification against the exact original."
    actions["recover-protocol"]["description"] = "Represent the two recovered protocols without merging study stages or compartments."
    actions["recover-protocol"]["acceptance_checks"][3] = "Preserve the authors' fed-batch wording alongside actual medium/catholyte replacement. The 2007 text specifies complete replacement below 40 mV. Select a native mode from the literal operation; do not force FED_BATCH with broth removal, partial-harvest SEMI_CONTINUOUS or an unperformed settle/draw cycle. Keep the 2008 operation and proposed optimization distinct."
    actions["recover-protocol"]["acceptance_checks"][4] = "Verify ambiguous 2008 degree/ohm/micro-unit glyphs against readable page images before numerical curation. The newly accessible 2007 text provides separate stage-specific Methods; do not copy the 2008 recipe into it. Preserve exact author-copy/source version and actual access limits if enriching caches. Update current access rationale without altering historical review receipts."
    actions["document-taxonomy"]["acceptance_checks"][0] = "Attach the independently inspected Methods from both studies and current NCBI type-material aliases for ATCC 35319/H10/DSM 5812 and ATCC 51573/PCA/DSM 12127. Preserve valid species terms and the resolved common_taxon link; optional strain refinement is not mandatory. Do not import unrelated reusable-gene mechanisms into the focal pair."
    actions["verify-future-curation"]["acceptance_checks"][0] = "Both primary text extractions are now read. Before declaring complete scientific verification, inspect critical original figures and ambiguous typography, retain version/locator provenance and reassess any resulting interpretation changes. Do not treat a current abstract cache or a web response hash as original-PDF equivalence."
    actions["verify-future-curation"]["acceptance_checks"][2] = "Canonical YAML, caches, histories, schema and products remain unchanged in PR 2053. Save only the new immutable linked review and its reproducible helpers; obtain a separate read-only review of the committed head before merge."
    review["limitations"] = [
        "Complete public author-copy text extractions, captions and references for both focal papers were read. Direct curl requests returned 403 challenge HTML. No original PDF byte equivalence, figure pixels or raw data were verified; scientific completion remains partial.",
        "The two-column extraction has ambiguous scientific glyphs and interleaved layout, particularly in the 2008 article. Do not silently normalize uncertain units or import measurements across studies, stages or compartments.",
        "Bulk residual pools, current/degradation comparisons and the authors' product-removal interpretation do not quantify molecule-specific partner flux or establish a metabolite utilized by the cellulolytic donor. No obligacy test is required to use the repository's syntrophy semantics.",
        "The new common_taxon link is assessed for identity and scope. Generic gene, assembly and other-community DIET claims in the reusable record are not independently certified as focal cellulose-MFC evidence.",
        "Both original caches remain abstract-only and all 28 current snippets match fresh reference-specific abstracts. Neither the caches nor the canonical history was enriched or rewritten.",
        "Corpus network diagnostics return exit 1 for 48 warnings/zero errors across 17/510 records; this target has no structural network issue. Native presence/validation scores do not certify the science.",
        "Only the original four single-target findings are superseded as continuing open observations. Multi-target Cycle 2 dispositions and other communities remain outside this review's adjudication scope.",
    ]
    review["notes"] = [
        "Two major and two minor findings remain open; completeness 85 and validation quality 100 (raw 111) retain their documented native formulas.",
        "The new record hash includes the valid common-taxon link/history. Source access has improved relative to the original review; no unavailable historical scratch file was recovered or invented.",
        "All helper scripts feeding this result are versioned under scripts/adhoc. Ignored source receipts are frozen working-tree attestations, not committed source bodies.",
    ]
    review["related_reviews"] = [{"repository": REPOSITORY, "review_id": row["review_id"],
        "relationship": "Immutable current-input successor; four original findings remain open." if row["review_id"] == old["review_id"] else "Common-taxon lineage context only; multi-target disposition not superseded."}
        for row in load("initial-lineage.json")]
    review["tags"] = list(dict.fromkeys(review.get("tags", []) + ["pr2053-current-input-refresh"]))
    review["finished_at"] = now()
    candidate = write("candidate-" + label + ".json", review)
    result = run("candidate-validate-" + label, ["uv", "run", "python", "scripts/record_review.py", "validate", str(candidate)])
    assert result.returncode == 0, result.stderr.decode()
    print(json.dumps({"candidate": str(candidate), "review_id": review["review_id"]}))


def save(label):
    result = run("native-save-" + label, ["uv", "run", "python", "scripts/record_review.py", "save", "--content", str(SCRATCH / ("candidate-" + label + ".json"))])
    assert result.returncode == 0, result.stderr.decode()
    print(result.stdout.decode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["build", "save"])
    parser.add_argument("--label", default="v1")
    args = parser.parse_args()
    {"build": build, "save": save}[args.mode](args.label)
