"""Author the immutable PR 2034 successor for record 321; never edit the record.

Run after pr2034_321_capture.py and pr2034_321_evidence.py. Saving is a separate,
serialized native operation, coordinated by the PR owner.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shlex
from pathlib import Path

import yaml
from pr2034_321_capture import OLD, ROOT, SCRATCH, TARGET, now, run, write

REPO = "CultureBotAI/CommunityMech"
ID = "CommunityMech:000321"


class NoAliases(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def main():
    initial = json.loads((SCRATCH / "inspect.json").read_text())
    paths = {i["path"] for i in initial["source"]["inputs"] if i["role"] != "target"}
    paths.update(str(p.relative_to(ROOT)) for p in (SCRATCH / "sources").iterdir())
    paths.update(str(p.relative_to(ROOT)) for p in (ROOT / "scripts/adhoc").glob("pr2034_321_*.py"))
    paths.update(
        [
            "src/communitymech/ontology_adapters.py",
            ".claude/skills/evidence-curation/SKILL.md",
            ".claude/skills/ground-taxa-gtdb/SKILL.md",
        ]
    )
    receipts = [
        "inspect-command.json",
        "inspect-command-v2.json",
        "source-retrieval.json",
        "source-retrieval-v2.json",
        "snippet-replay.json",
        "ontology-authority.json",
        "primary-artifact-projection.json",
        "target-change-proof.json",
        "network-reuse.json",
        "strict.tsv",
    ]
    receipts += [p.name for p in SCRATCH.glob("validate*.json")]
    paths.update(str((SCRATCH / name).relative_to(ROOT)) for name in receipts)
    network_names = [
        "network-corpus-inputs.json",
        "audit-network.json",
        "check-network-quality.json",
        "audit-network.stdout.txt",
        "audit-network.stderr.txt",
        "check-network-quality.stdout.txt",
        "check-network-quality.stderr.txt",
    ]
    paths.update(".temp/pr2034/273/" + n for n in network_names)
    manifest = json.loads((ROOT / ".temp/pr2034/273/network-corpus-inputs.json").read_text())
    assert len(manifest["inputs"]) == 503
    assert all(
        hashlib.sha256((ROOT / x["path"]).read_bytes()).hexdigest() == x["sha256"]
        for x in manifest["inputs"]
    )
    write("context-inputs-v3.json", sorted(paths))
    cmd = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(SCRATCH / "targets.json"),
    ]
    for p in sorted(paths):
        cmd.extend(["--input", p])
    result = run("inspect-command-v3", cmd)
    assert result["exit_code"] == 0
    inspected = json.loads(result["stdout"])
    write("inspect-v3.json", inspected)
    timestamp = now().replace("+00:00", "Z")
    rid = (
        timestamp[:19].replace("-", "").replace(":", "").replace("T", "T")
        + "Z-pr2034-kefir-rothia-successor"
    )
    old = yaml.safe_load((ROOT / OLD).read_text())
    record = yaml.safe_load((ROOT / TARGET).read_text())
    owner = copy.deepcopy(inspected["targets"][0]["owner_paths"])
    evidence = []

    def ev(eid, kind, ref, locator, summary, support="supports", path=None):
        row = {
            "evidence_id": eid,
            "kind": kind,
            "reference": ref,
            "locator": locator,
            "accessed_at": timestamp,
            "support": support,
            "summary": summary,
        }
        if path:
            row["snapshot_sha256"] = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        evidence.append(row)

    ev(
        "record",
        "record_content",
        TARGET,
        "Whole current record, including all nine EvidenceItems, one community-level node and no arrows.",
        "Current KRP model, source isolation, taxonomy, resource/dataset claims and the October 21 role/abundance additions were assessed.",
        path=TARGET,
    )
    ev(
        "predecessor",
        "prior_review",
        OLD,
        "All three findings, actions, limitations, current-source comparisons and predecessor input identity.",
        "The two major and one minor predecessor findings are independently rechecked and retained open; no terminal disposition is inferred from a newer review.",
        path=OLD,
    )
    ev(
        "change-proof",
        "record_content",
        ".temp/pr2034/321/target-change-proof.json",
        "Exact Git diff and parsed field paths from a4611c913c8da9619673df63a0c2cce3aa206a83 to current HEAD.",
        "Only CROSS_FEEDER, RARE, two associated EvidenceItems and their history event changed. The three previously flagged claim surfaces remain unchanged.",
        path=".temp/pr2034/321/target-change-proof.json",
    )
    ev(
        "genome-paper",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC5624747/",
        "PMID:28963201; DOI:10.1128/genomeA.00869-17. Retained scientific body characters 2849:6360; KRP isolation at 3787, accession at 6252.",
        "The genome report identifies KRP as ISC 156 from kefir grain, describes GAM agar isolation for two days at 30 degrees C, and reports 81 contigs, 2,522,693 bp and NDFM00000000. The low-abundance species context supports RARE without a numerical abundance claim.",
        path="references_cache/PMID_28963201.txt",
    )
    ev(
        "modeling-paper",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC7610452/",
        "PMID:33398099; DOI:10.1038/s41564-020-00816-5. Entire retained scientific main characters 3567:62478 read; Metabolic modelling paragraph begins 56565.",
        "The authors reconstruct bacterial metabolic models and combine simulated amino-acid fluxes with measured community abundance. Specific experimental cooperation results concern other named pairs. Generic FBA and whole-kefir cooperation do not establish KRP utilization of a partner-derived metabolite.",
        path="references_cache/PMID_33398099.md",
    )
    sources = json.loads((SCRATCH / "source-retrieval-v2.json").read_text())
    lookup = {Path(x["snapshot"]["path"]).name: x for x in sources}
    source_specs = [
        (
            "biomodels",
            "biomodels-metadata.json",
            "name, description, submissionId, files.main, modelLevelAnnotations, curationStatus and revision comments; author/contact fields excluded.",
            "Current BioModels names the KRP model, links the paper and authors repository, identifies the downloaded XML checksum, and records a 2024 gene-reaction-association update. NON_CURATED is the repository status, not a failed scientific identity check.",
        ),
        (
            "biomodels-sbml",
            "biomodels-model.xml",
            "SBML model id and structural counts only; no solver execution.",
            "Downloaded model m_156_03182016 has 962 species, 1,336 reactions and 542 gene products. Its bytes agree with the current metadata checksum.",
        ),
        (
            "authors-model",
            "authors-model.xml",
            "SBML model id and structural counts; compared with authors species mapping.",
            "The authors artifact m_156_03182016 has 893 species, 1,274 reactions and 451 gene products. It supports model provenance but is not byte- or structure-identical to the current BioModels revision.",
        ),
        (
            "authors-species",
            "authors-species.tsv",
            "Exact row with key 156_03182016; other Rothia dentocariosa rows remain distinct.",
            "The authors map 156_03182016 to Rothia kefirresidentii KRP, supporting the KRP model identity without identifying every genome-processing step.",
        ),
        (
            "nuccore",
            "nuccore.gb",
            "ACCESSION, VERSION, ORGANISM, WGS comment and source organism/strain qualifiers; submitter/contact fields excluded.",
            "NDFM00000000.1 is deposited as Rothia sp. Olga with NDFM01 components 1 through 401 and BioSample SAMN06718477.",
        ),
        (
            "ena",
            "ena.embl",
            "ID, AC, DE, BioSample cross-reference, WGS comment and source qualifiers.",
            "ENA independently exposes the NDFM01 Olga project and 401 sequences; this corroborates deposit metadata, not exact KRP model-input equivalence.",
        ),
        (
            "biosample",
            "biosample.xml",
            "BioSample accession, Sample name, organism and strain/isolation-source attributes only.",
            "SAMN06718477 uses sample name 156 - R.dentocariosa, organism Rothia sp. Olga and strain Olga, isolated from kefir. The shared 156 stock code is a partial bridge, not proof of a different isolate or a complete alias reconciliation.",
        ),
        (
            "assembly",
            "assembly.json",
            "result.1163481 accession/synonym, organism, biosource, WGS, assembly statistics, update date and QC flags.",
            "GCA/GCF_002238135.1 reports 401 contigs and 2,756,010 bp, with contamination/excluded-from-RefSeq/suppressed-RefSeq flags updated September 23, 2026. These differ from the paper statistics; they do not alone invalidate all model predictions.",
        ),
    ]
    for eid, name, loc, summary in source_specs:
        x = lookup[name]
        ev(
            eid,
            "database",
            x["url"],
            loc + " Retrieved " + x["finished_at"] + ".",
            summary,
            path=x["snapshot"]["path"],
        )
    ev(
        "artifact-proof",
        "database",
        ".temp/pr2034/321/primary-artifact-projection.json",
        "Scientific projection and all nine retrieved source hashes; parsed SBML counts.",
        "The helper retains source hash/version evidence and excludes personal metadata from the scientific projection.",
        path=".temp/pr2034/321/primary-artifact-projection.json",
    )
    ev(
        "ontology",
        "authority",
        ".temp/pr2034/321/ontology-authority.json",
        "All six distinct ontology terms at seven placements, current labels, definitions and taxon rank from existing OAK SQLite builds.",
        "Labels all match. NCBITaxon:32207 is genus Rothia. ENVO:00003862 denotes a building, whereas GO amino-acid metabolism/transport and CHEBI amino acid fit the expressly computational node scope.",
        path=".temp/pr2034/321/ontology-authority.json",
    )
    ev(
        "schema",
        "authority",
        "src/communitymech/schema/communitymech.yaml",
        "FunctionalRoleEnum.CROSS_FEEDER, AbundanceEnum, TaxonomicComposition, GrowthMedia and modeled_environment semantics.",
        "CROSS_FEEDER means utilization of metabolites from other taxa, not generic amino-acid transport or a modeled exchange reaction. RARE is an ordinal community annotation, not a percentage.",
        path="src/communitymech/schema/communitymech.yaml",
    )
    ev(
        "dataset-schema",
        "authority",
        "src/communitymech/schema/mech_shared.yaml",
        "Dataset definition, accession and separate publication attribute.",
        "A publication-only DOI entry is bibliographic context; the model XML and WGS accession remain positive data resources.",
        path="src/communitymech/schema/mech_shared.yaml",
    )
    ev(
        "rubric",
        "authority",
        ".claude/skills/review-communities/reference/validation-rules.md",
        "P3.1 growth-media linkage and impact-based P1-P4 interpretation.",
        "GAM lacks CultureMech/MediaIngredientMech linkage. Exact formulation verification is required before linking; the published medium name alone is not recipe equivalence.",
        path=".claude/skills/review-communities/reference/validation-rules.md",
    )
    ev(
        "replay",
        "validation",
        ".temp/pr2034/321/snippet-replay.json",
        "All nine recursive EvidenceItems; whitespace-only normalization, no spelling/punctuation repair.",
        "Nine snippets match after whitespace normalization; eight match raw. Both graph snippets are raw exact. Literal matching does not establish the role, accession or claim-local support.",
        path=".temp/pr2034/321/snippet-replay.json",
    )
    checks = []
    for name in [
        "validate",
        "validate-strict",
        "validate-terms",
        "validate-references-explained",
        "validate-gtdb",
        "validate-gtdb-domain",
        "validate-history",
    ]:
        p = SCRATCH / (name + ".json")
        d = json.loads(p.read_text())
        eid = "check-" + name
        ev(
            eid,
            "validation",
            str(p.relative_to(ROOT)),
            "Actual command, environment, start/finish, exit code and complete stdout/stderr.",
            d["stdout"].strip() or d["stderr"].strip(),
            path=str(p.relative_to(ROOT)),
        )
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "passed",
                "required": True,
                "target_ids": [ID],
                "command": shlex.join(d["command"]),
                "exit_code": d["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [eid],
                "summary": (
                    "Focused current-record check passed; the reference summary counts reported issues, not checked excerpts."
                    if name == "validate-references-explained"
                    else "Focused current-record check passed."
                ),
                "scope_note": "Single target; history checks use its exact history directory. Shared main .venv used with UV_NO_SYNC=1; full environment is recorded in the receipt.",
            }
        )
    for name in ["audit-network", "check-network-quality"]:
        path = ".temp/pr2034/273/" + name + ".json"
        d = json.loads((ROOT / path).read_text())
        eid = "check-" + name
        ev(
            eid,
            "validation",
            path,
            "Actual same-session corpus command; output hashes and files; network-corpus-inputs.json independently rehashed for all 503 inputs.",
            "Actual exit 1: 44 warnings in 16 of 503 records, zero errors. No KRP target finding. The unchanged-corpus result is reused rather than rerun.",
            path=path,
        )
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "failed",
                "required": True,
                "target_ids": [ID],
                "command": d["command"],
                "exit_code": 1,
                "expected_exit_code": 0,
                "evidence_ids": [eid],
                "summary": "Corpus warnings retain a failed required gate; they are not attributed to this target.",
                "scope_note": "All 503 direct records in both default roots, including ignored files; exact manifest hashes verified at reuse.",
            }
        )
    assessments = []

    def assess(aid, area, topic, outcome, summary, ids, dimensions=None):
        a = {
            "assessment_id": aid,
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "target_ids": [ID],
            "evidence_ids": ids,
        }
        if dimensions:
            a["dimensions"] = dimensions
        assessments.append(a)
        return a

    def dim(name, value, definition, ids):
        return {"name": name, "value": value, "definition": definition, "evidence_ids": ids}

    assess(
        "identity",
        "identity",
        "KRP computational model and source strain",
        "supported",
        "Current primary metadata and both model artifacts identify KRP. This is one isolate-derived computational model, not the whole kefir community and not proof that the isolate was genetically engineered.",
        ["record", "genome-paper", "biomodels", "authors-model", "authors-species"],
        [
            dim(
                "source-strain",
                "Rothia kefirresidentii KRP; ISC 156",
                "Publication and authors model identity; deposited Olga naming is separately unresolved.",
                ["genome-paper", "authors-species", "biosample"],
            ),
            dim(
                "taxon-rank",
                "NCBITaxon:32207 and GTDB:g__Rothia are genus-level",
                "A conservative genus identity does not authenticate an exact genome.",
                ["ontology", "record"],
            ),
            dim(
                "community-scope",
                "Single-member computational model",
                "No measured KRP coculture, partner-specific transfer or causal arrow is encoded.",
                ["record", "modeling-paper"],
            ),
            dim(
                "biomass-state",
                "Cultured isolate supplies genomic provenance; metabolism is simulated",
                "GAM cultivation is not an FBA exchange-bound specification.",
                ["genome-paper", "biomodels"],
            ),
            dim(
                "source-category",
                "Two retained primary papers and freshly downloaded primary model/genome repositories",
                "Paper claims, original author model and later BioModels revision remain distinct.",
                ["genome-paper", "modeling-paper", "artifact-proof"],
            ),
        ],
    )
    assess(
        "roles",
        "scope",
        "New role and abundance annotations",
        "concern",
        "RARE is supported in the source grain context. CROSS_FEEDER still needs KRP-specific attribution: generic expected uptake/secretion and whole-community cooperation do not identify KRP consumption of another taxon's products. Preserve computational potential without inventing a replacement ecological role.",
        ["record", "schema", "genome-paper", "modeling-paper", "change-proof"],
    )
    node = record["ecological_interactions"][0]
    dimensions = [
        dim(
            "node-0",
            "ecological_interactions[0]; community-level; one participant NCBITaxon:32207; zero arrows",
            "The computational node is not a measured pairwise ecological interaction.",
            ["record", "modeling-paper", "biomodels"],
        )
    ]
    for i, item in enumerate(node["evidence"]):
        offset = (ROOT / "references_cache/PMID_33398099.md").read_text().index(item["snippet"])
        dimensions.append(
            dim(
                f"node-0-evidence-{i}",
                f"references_cache/PMID_33398099.md characters {offset}:{offset+len(item['snippet'])}. Inspected record snippet: {item['snippet']}",
                "Raw exact source match; model-method evidence with the recorded computational provenance, not direct biological transfer.",
                ["modeling-paper", "replay"],
            )
        )
    assess(
        "graph",
        "graph",
        "Existing computational graph",
        "supported",
        "Preserve the sole qualified node, amino-acid metabolite/process context, genus participant and absent edges. The source models amino-acid uptake and secretion; neither transport terms nor exchange reactions demonstrate donor-to-KRP transfer. The current graph already keeps that boundary.",
        ["record", "modeling-paper", "authors-species", "biomodels-sbml", "ontology", "replay"],
        dimensions,
    )
    assess(
        "environment",
        "grounding",
        "Isolation setting and represented kefir environment",
        "concern",
        "Laboratory isolation is defensible. The dairy building term is not supported as the modeled kefir material/environment, even though its label validates.",
        ["record", "genome-paper", "ontology"],
    )
    assess(
        "genome",
        "provenance",
        "Genome and model versions",
        "concern",
        "The published KRP/NDFM and deposited Olga/NDFM01 relationship remains unreconciled. Model identity is positive; the shared 156 key partly bridges names. Assembly size/contig differences and current QC flags require explicit version/filtering provenance, not an automatic taxon replacement or blanket rejection of modeled predictions.",
        [
            "genome-paper",
            "authors-species",
            "nuccore",
            "ena",
            "biosample",
            "assembly",
            "biomodels",
            "artifact-proof",
        ],
    )
    assess(
        "cultivation",
        "completeness",
        "KRP isolation and exact GAM linkage",
        "concern",
        "Retain GAM agar, 30 degrees C, two days and ground-kefir serial-dilution isolation. Source does not establish an exact GAM formulation/catalogue match or an isolate-specific atmosphere; neither recipe nor model exchange constraints should be invented.",
        ["record", "genome-paper", "rubric"],
        [
            dim(
                "cultivation-stage",
                "GAM agar isolation: 30 degrees C, two days",
                "Natural-community fermentation conditions and computational medium are distinct.",
                ["genome-paper", "modeling-paper"],
            )
        ],
    )
    assess(
        "resources",
        "evidence",
        "Claim-local citation and resource representation",
        "concern",
        "The model and WGS accessions are positive resources. Design/resource title snippets do not establish their specific claims, despite independently available Methods/deposit support. The paper DOI is a publication, not a separate deposited dataset.",
        ["record", "modeling-paper", "biomodels", "dataset-schema"],
    )
    assess(
        "gtdb",
        "grounding",
        "Current taxonomic semantic checks",
        "supported",
        "Current labels and genus rank are correct; GTDB lineage and domain gates pass. These checks do not regenerate the historical 1,075-genome mapping aggregate or establish KRP/Olga strain equivalence. No automatic species-level replacement is proposed.",
        ["ontology", "record", "check-validate-gtdb", "check-validate-gtdb-domain"],
    )
    findings = []
    actions = []

    def finding(
        fid, key, cat, severity, title, description, fields, ids, rule, accept, previous=None
    ):
        f = {
            "finding_id": fid,
            "issue_key": key,
            "category": cat,
            "severity": severity,
            "status": "open",
            "certainty": "confirmed",
            "title": title,
            "description": description,
            "target_ids": [ID],
            "field_paths": fields,
            "evidence_ids": ids,
            "rule_id": rule,
            "native_severity": "P2" if severity == "major" else "P3",
            "normalization_reason": (
                "Materially unsupported ecological/identity/grounding inference."
                if severity == "major"
                else "Bounded, non-blocking evidence, representation or external-linkage correction."
            ),
            "owner_paths": owner,
        }
        if previous:
            f["previous_occurrences"] = [
                {"repository": REPO, "review_id": old["review_id"], "finding_id": previous}
            ]
            f["disposition_reason"] = (
                "Remains open after independent current-source reassessment; the relevant canonical field is unchanged."
            )
        findings.append(f)
        actions.append(
            {
                "action_id": "address-" + fid,
                "description": title + ". " + accept[0],
                "finding_ids": [fid],
                "target_ids": [ID],
                "owner_paths": owner,
                "acceptance_checks": accept
                + [
                    f"After separately authorized curation, run focused schema, strict, term and reference checks for {TARGET}; append the required record history."
                ],
            }
        )

    finding(
        "environment",
        "cm-000321-dairy-building-grounding",
        "grounding",
        "major",
        "Modeled environment still denotes a dairy building",
        "ENVO:00003862 has the correct dairy label but denotes a building for milk harvesting/processing. The record represents an isolate-derived kefir model; no building-specific modeled setting is established. This semantic finding survives a passing label check.",
        ["modeled_environment[0].term.id", "modeled_environment[0].preferred_term"],
        ["record", "ontology", "genome-paper"],
        "review-checklist.environment",
        [
            "Use an authoritative term matching the source-supported kefir/milk setting, or withhold the unsupported class.",
            "Check the proposed definition against the source; preserve laboratory isolation versus modeled natural context.",
        ],
        "environment",
    )
    finding(
        "genome-provenance",
        "cm-000321-genome-input-provenance",
        "provenance",
        "major",
        "Exact genome input remains unreconciled",
        "The paper reports KRP/NDFM with 81 contigs and 2,522,693 bp; current NDFM01/Olga and assembly metadata report 401 contigs and 2,756,010 bp with contamination and RefSeq suppression. Sample 156 partially bridges aliases, so these sources do not prove distinct isolates. The exact version/preprocessing used for the KRP model remains unsupported by an unqualified accession assertion.",
        [
            "taxonomy[0].taxon_term.notes",
            "taxonomy[0].evidence[1]",
            "taxonomy[0].evidence[3].computational_provenance.input_accession",
            "ecological_interactions[0].evidence[0].computational_provenance.input_accession",
            "ecological_interactions[0].evidence[1].computational_provenance.input_accession",
            "associated_datasets[2]",
        ],
        [
            "record",
            "genome-paper",
            "authors-species",
            "nuccore",
            "ena",
            "biosample",
            "assembly",
            "biomodels",
        ],
        "CLAUDE.claim-level-evidence",
        [
            "Document KRP/ISC 156/Olga aliases and distinguish published statistics from current deposited assembly metadata.",
            "Identify the sequence/protein input version and filtering used for reconstruction before asserting exact equivalence.",
            "Preserve current QC limitations and the difference between authors and BioModels model revisions without declaring every prediction invalid.",
        ],
        "genome-provenance",
    )
    finding(
        "citation-placement",
        "cm-000321-title-only-evidence",
        "evidence",
        "minor",
        "Design and model-resource evidence still use a title only",
        "The unchanged title-only snippets provide study context but do not substantiate KRP reconstruction/FBA endpoints or the exact BioModels artifact. Current Methods, authors mapping and retrieved model metadata supply positive evidence for those claims, so the correction is claim-local placement rather than model-identity rejection.",
        ["engineering_design.evidence[0]", "external_resources[0].evidence[0]"],
        ["record", "modeling-paper", "authors-species", "biomodels", "biomodels-sbml"],
        "CLAUDE.claim-level-evidence",
        [
            "Attach concise Methods evidence to reconstruction/FBA claims and exact deposit provenance to the model-resource identity.",
            "Keep publication workflow, authors artifact and later BioModels revision distinct; quotations must match the source.",
        ],
        "citation-placement",
    )
    finding(
        "role-attribution",
        "cm-000321-cross-feeder-attribution",
        "scope",
        "major",
        "Generic FBA does not establish a KRP cross-feeder role",
        "The new functional_role CROSS_FEEDER asserts utilization of metabolites from other taxa. Its attached evidence describes all-species simulated amino-acid uptake/secretion. The inspected paper and artifact identity do not establish the origin of a KRP-consumed metabolite or KRP-specific partner exchange. Computational evidence could support a properly specified prediction, but the present generic workflow does not support this particular role.",
        ["taxonomy[0].functional_role", "taxonomy[0].evidence[3].explanation"],
        ["record", "schema", "modeling-paper", "authors-species", "change-proof"],
        "P2.4; CLAUDE.claim-level-evidence",
        [
            "Remove or qualify the unsupported role until exact KRP-specific partner-product evidence or a defined computational cross-feeding result is attached.",
            "Retain the supported computational-potential node and RARE annotation; do not invent an alternative role or a measured exchange edge.",
        ],
    )
    finding(
        "medium-link",
        "cm-000321-gam-medium-linkage",
        "completeness",
        "minor",
        "GAM isolation medium lacks an exact external linkage",
        "The GAM agar entry has no CultureMech or MediaIngredientMech linkage. The paper supports the medium name and isolation conditions but not an exact recipe/catalogue identity; this is an enrichment gap, not evidence that cultivation values are wrong.",
        ["growth_media[0]"],
        ["record", "genome-paper", "rubric"],
        "P3.1",
        [
            "Verify the source GAM formulation or product identity and match an exact maintained medium entry before adding a link.",
            "If exact identity remains unresolved, document that limit rather than substituting a similarly named recipe or modifying source-positive temperature/time.",
        ],
    )
    finding(
        "publication-placement",
        "cm-000321-publication-as-dataset",
        "representation",
        "minor",
        "A publication is represented as a dataset",
        "associated_datasets[1] is the primary article DOI/title and landing page rather than an identified dataset. The schema separates dataset accessions from associated publications. Retain the paper as literature context and preserve the independently positive BioModels and WGS entries.",
        ["associated_datasets[1]"],
        ["record", "dataset-schema", "modeling-paper", "biomodels", "nuccore"],
        "review-checklist.resource-semantics",
        [
            "Move the publication-only entry to a supported publication/external-resource relationship or identify a genuine deposited dataset before retaining it in associated_datasets.",
            "Do not invent a data accession or remove the valid BioModels/WGS resources.",
        ],
    )
    metrics = assess(
        "metrics",
        "completeness",
        "Native metrics and executed gates",
        "concern",
        "All focused gates pass. Both required corpus gates executed and retain unrelated warning failures. Native completeness counts field presence, including the role under review; neither metric certifies scientific correctness.",
        ["record", "replay", "check-audit-network", "check-check-network-quality"],
    )
    metrics["metrics"] = [
        {
            "name": "Completeness score",
            "value": 80,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "Literal native formula: 50 required-field points (including role presence), 5 environment, 5 external resources, 10 growth_media, 5 datasets, 5 interaction metabolites; no environmental-factor or three-node bonus.",
        },
        {
            "name": "Validation quality score",
            "value": 99,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "100 - 3 P2*10 - 3 P3*2 + min((2 evidence/1 interaction)/2,1)*20 + 15 for complete target network = 99. Corpus warnings remain separate failed checks.",
        },
        {
            "name": "P2 findings",
            "value": 3,
            "unit": "findings",
            "definition": "Target-specific major scientific/grounding findings.",
        },
        {
            "name": "P3 findings",
            "value": 3,
            "unit": "findings",
            "definition": "Target-specific bounded evidence, medium-linkage and publication-placement findings.",
        },
        {
            "name": "Evidence per interaction",
            "value": 2,
            "unit": "EvidenceItems per interaction",
            "denominator": 1,
            "definition": "Two excerpts on the single computational node; both from the same paper, not independent replication.",
        },
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": rid,
        "kind": "record",
        "repository": REPO,
        "title": "PR 2034: current-source successor for the KRP BioModels isolate",
        "started_at": "2026-11-05T20:08:00Z",
        "finished_at": timestamp,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "unknown",
            "independence_basis": "This author did not curate the current target. Earlier curation/review used agent identities, so personal independence is not established. Root and a separately assigned adversary review this successor independently.",
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "The three predecessor findings remain open. Current evidence also identifies an unsupported KRP cross-feeder role, an unlinked GAM formulation and a publication-only dataset entry: 3 P2 and 3 P3. Model identity, the qualified computational node, RARE and GAM isolation conditions are supported. All focused checks passed; two executed corpus gates retain unrelated warning failures.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Whole current isolate record and all predecessor findings, with current primary model/genome retrieval, paper/source and ontology reassessment.",
            "selection": "Explicit PR 2034 canary refresh of the stale CommunityMech:000321 review only.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [ID],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "No FBA optimization or FROG rerun was performed. Structural model checks and artifact hashes do not prove numerical reproducibility or revision equivalence.",
            "The exact model-input assembly/version/filtering and complete KRP/Olga alias relationship remain unresolved and are an explicit finding. This does not prevent completing the evidence assessment.",
            "The historical 1,075-genome GTDB aggregate was not regenerated. Current local ontology rank/labels, lineage coherence and prokaryotic domain were independently checked; no strain identity is inferred from genus grounding.",
            "Current sources identify GAM agar but do not settle exact formulation, isolate-specific atmosphere or FBA medium exchange bounds. No values are inferred from whole-kefir fermentation.",
            "Both required corpus network gates returned warning failures elsewhere. These remain failed checks; the target itself has one connected computational node and no dangling edges.",
            "Public model/genome metadata initially displayed some author/contact fields during an overbroad projection. They were excluded from scientific use; the persisted scientific projection and evidence locators select only model, organism, accession and QC fields.",
            "Downloaded snapshots and command outputs are retained in current session scratch and hash-pinned through native inspection; this successor does not depend on deleted historical /tmp artifacts.",
        ],
        "notes": [
            "No canonical record, history event, ontology, schema, generated product or scientific-status field was edited. All curation actions are proposals.",
            "CLAUDE.md is a symlink to the regular AGENTS.md. Native inspection rejected the symlink before assessment; the corrected inspection pins AGENTS.md. The initial administrative failure remains in a separate receipt.",
            "The initial sandbox source-download attempt failed DNS resolution. The authorized public-source retry succeeded for all nine URLs; neither attempt is represented as a scientific validator failure.",
            "The historical #2050 role/abundance curation is context, not a resolution of the three predecessor findings. This review does not itself change any GitHub issue disposition.",
        ],
        "related_reviews": [
            {
                "repository": REPO,
                "review_id": old["review_id"],
                "relationship": "Current whole-record successor; all three original issue identities retained open with exact previous_occurrences.",
            }
        ],
        "links": [
            "https://github.com/CultureBotAI/CommunityMech/pull/2034",
            "https://github.com/CultureBotAI/CommunityMech/issues/2138",
        ],
        "tags": ["pr-2034", "record-review", "isolate", "computational-model"],
    }

    def no_trailing(x):
        if isinstance(x, str):
            assert all(line == line.rstrip(" \t") for line in x.splitlines()), repr(x)
        elif isinstance(x, dict):
            for v in x.values():
                no_trailing(v)
        elif isinstance(x, list):
            for v in x:
                no_trailing(v)

    no_trailing(review)
    path = SCRATCH / "candidate-v1.yaml"
    with path.open("x") as stream:
        yaml.dump(review, stream, Dumper=NoAliases, sort_keys=False, allow_unicode=True, width=110)
    print(
        json.dumps(
            {
                "candidate": str(path.relative_to(ROOT)),
                "review_id": rid,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )
    )
    run(
        "candidate-native-v1",
        ["uv", "run", "python", "scripts/record_review.py", "validate", str(path)],
    )


if __name__ == "__main__":
    assert Path.cwd() == ROOT
    main()
