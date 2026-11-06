"""Author the PR2043 sponge successor as JSON for native validation/save only."""

import hashlib
import json
import shlex
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2043/013"
OLD_ID = "20261021T124426Z-sponge-holobiont-model-record"
OLD = ROOT / "reviews/structured" / OLD_ID / "review.yaml"
TARGET_ID = "CommunityMech:000013"
TARGET = "kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml"
HISTORY = (
    "history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network/"
    "2026-10-25T151200Z-antigravity-2072.yaml"
)
REPO = "CultureBotAI/CommunityMech"
ARTICLE = "doi:10.1038/s41467-024-55222-w"
CONTEXT_IDS = [
    "20261025T113500Z-c2s4-record-deep-audit",
    "20261025T113600Z-c2s4-frozen-cohort-review",
    "20261025T161500Z-c2s5-remediation-verification",
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    review = deepcopy(yaml.safe_load(OLD.read_text()))
    inspection = json.loads((OUT / "inspect-final.stdout").read_text())
    audit = json.loads((OUT / "target-audit.json").read_text())
    assert all(item["matched"] for item in audit["snippets"])
    assert all(item["label"] == item["authority_label"] for item in audit["ontology_authorities"])
    review.update(
        review_id=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-pr2043-sponge-holobiont-successor",
        title="Current-main sponge holobiont review and bounded source-context correction",
        started_at=json.loads((OUT / "started.json").read_text())["started_at"].replace(
            "+00:00", "Z"
        ),
        finished_at=now,
        reviewer={
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author refresh; separate adversarial approval is not claimed here.",
        },
        source=inspection["source"],
        targets=inspection["targets"],
        completion="completed",
        verdict="needs_curation",
        scientific_review=True,
        summary=(
            "The added animal-associated environment is supported; its repaired omission is removed "
            "from the residual context finding. All four original finding keys remain open: two P2 "
            "membership/state findings and two P3 computational/resource findings. A new P3 finding "
            "records an unrelated PMID in the appended history. Six qualified computational nodes "
            "and two conditional arrows remain supported. Bounded corrections identify the actual "
            "sponge DOI, Great Barrier Reef sampling and unsupported quotation in three prior "
            "cohort-review contexts without superseding their multi-target findings."
        ),
        scope={
            "description": (
                "Entire current record and source delta; complete primary scientific main, six main "
                "figures, scientific SI text, selected supplementary tables, public model/archive "
                "metadata and bounded prior-review source context."
            ),
            "selection": "PR2043 stale record CommunityMech:000013; no other cohort target reassessed.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TARGET_ID],
        },
    )
    evidence = []

    def ev(eid, kind, reference, locator, summary, local=None, support="supports", accessed=now):
        item = {
            "evidence_id": eid,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "summary": summary,
            "support": support,
            "accessed_at": accessed.replace("+00:00", "Z"),
        }
        if local:
            item["snapshot_sha256"] = sha(local)
        evidence.append(item)

    source_receipts = json.loads((OUT / "fetch-receipts.json").read_text())
    article_access = next(x["finished_at"] for x in source_receipts if x["name"] == "article.xml")
    science = {
        "roster": (
            "Sec3/15-17; Figure1 pixels; SD2 rows4-11",
            "Eight named merged/representative MAG reconstructions (seven bacteria, one archaeon) "
            "represent 98.3 percent of MAG-mapped reads. Three broad current entries omit five members.",
        ),
        "nitrification": (
            "Sec5-6; Figure3 pixels; SI CenSfMM8/NitSfMM6 curation and TableS1",
            "Predicted archaeal nitrite supports bacterial nitrifier growth after an NO-forming "
            "reaction is disabled; neither measured partner transfer nor thermodynamic obligacy follows.",
        ),
        "stability": (
            "Sec6-7/21; Figures3-4 pixels",
            "Normalized final/initial AOA:NOB ratio of 0.5-2 is a conditional model criterion. "
            "Eight-member composition depends on imposed inputs, removal, death and grid dynamics; "
            "these endpoints do not establish unqualified natural ecological equilibrium.",
        ),
        "host-input": (
            "Sec4/8/13/19-21; Figure2 pixels",
            "Two samples per metabolomics group inform candidate tissue-enriched host inputs. "
            "Origin/delivery remain assumptions, and host metabolism/respiration are excluded.",
        ),
        "network": (
            "Sec7-12; Figures4-6 pixels; focal SD7/11 exchange rows",
            "Alternative hypotaurine/laurate regimes change predicted exchange; a whole-network "
            "summary is not an independent cause of component routes or proof of active coordination.",
        ),
        "deltaporibacter": (
            "Sec10-11; Figures5-6 pixels; SD7 nitrate/NO and SD11 laurate/acetate rows",
            "Conditional predictions support nitrate reduction and NO release under hypotaurine, "
            "and laurate use with acetate donation under mixed inputs; no measured flux claimed.",
        ),
        "carbon": (
            "Sec8/11-13; Figures5-6 pixels",
            "Input-dependent microbial carbon balance excludes host respiration. Pathway carbon "
            "fixation does not establish every regime or the whole living holobiont as autotrophic.",
        ),
        "model-methods": (
            "Sec15-21; SI scientific methods/notes; SD5 selected media and SD9/13",
            "Merged MAGs, gapseq 1.1 b568a4e/manual curation/gap-filling and BacArena 1.8.2 pFBA "
            "define simulations. Eight-member runs use 100 hourly cycles, 10 mM ammonia,10 percent "
            "removal and 5 percent death; distinguish single/two/three-member settings from these.",
        ),
        "source-resources": (
            "Data and Code Availability",
            "Focal model MODEL2407300002, broad prior project PRJNA602572 and STY8 v1.0.0 are "
            "source-reported. The linked MassIVE task and MSV000083743 currently describe EMP "
            "soil/fecal samples, leaving the focal metabolomics pointer unresolved.",
        ),
    }
    for eid, (locator, summary) in science.items():
        ev(
            eid,
            "primary_source",
            ARTICLE,
            locator,
            summary,
            OUT / "article.xml",
            accessed=article_access,
        )
    ev(
        "record",
        "record_content",
        TARGET,
        "Entire current file",
        "Three taxa, six nodes, two arrows; "
        "ENVO:01001002 and appended2026-10-25 history are the only changes since the frozen input.",
        ROOT / TARGET,
    )
    ev(
        "pubmed",
        "database",
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=39738126,39604529&retmode=xml",
        "Both PubmedArticle identities",
        "39738126 is the sponge paper;39604529 is an unrelated "
        "NLRP3 author correction, contradicting the new history sidecar citation.",
        OUT / "pubmed.xml",
    )
    ev(
        "supplement",
        "primary_source",
        ARTICLE,
        "MOESM1 scientific methods/notes/TablesS1-S3; MOESM5 SD2,9,12,13 and selected SD5/7/11 rows",
        "Model/MAG identities, reconstruction/curation assumptions and conditional exchanges corroborate "
        "the qualified graph. SD7/11 NO/nitrite identifier reversal and SD7 header-layout ambiguity remain "
        "source discrepancies rather than imported chemical IDs.",
        OUT / "supplement.pdf",
    )
    ev(
        "supplement-tables",
        "primary_source",
        ARTICLE,
        "MOESM5; focal-tables.json retains selected sheets",
        "Eight listed members; scenario media and model parameter provenance. Focal nitrogen/acetate "
        "directions agree with narrative and figures; no raw matrix/statistics reanalysis.",
        OUT / "supplement-tables.xlsx",
    )
    ev(
        "schema",
        "authority",
        "src/communitymech/schema/communitymech.yaml",
        "MicrobialCommunity; EcologicalStateEnum; ComputationalProvenance",
        "STABLE means equilibrium; ecological_state is optional. Structured computational provenance "
        "is available for these fourteen computational claims. Environment presence is now repaired.",
        ROOT / "src/communitymech/schema/communitymech.yaml",
    )
    ev(
        "ontology",
        "authority",
        TARGET,
        "target-audit.json ontology_authorities; native validate-terms",
        "All 11 distinct pairs across 20 occurrences resolve with exact labels, including newly added "
        "ENVO:01001002 animal-associated environment. Canonical label validity is distinct from "
        "specificity and scientific support.",
        OUT / "target-audit.json",
    )
    ev(
        "roster-authority",
        "authority",
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2973585,1671877,2973566,2881427&retmode=xml",
        "Four requested Taxon records",
        "Three Candidatus-prefixed species candidates and "
        "Parasynechococcus genus resolve. Other proposed names retain source-name uncertainty; "
        "this refresh makes no global negative identity claim.",
        OUT / "ncbi-taxonomy.xml",
    )
    for eid, file, url, summary in [
        (
            "resources",
            "biomodels-files.json",
            "https://www.ebi.ac.uk/biomodels/model/files/MODEL2407300002?format=json",
            "Exact combined-input RDS filename and eight model files verified as archive listings; payloads not parsed or executed.",
        ),
        (
            "model-identity",
            "biomodels.json",
            "https://www.ebi.ac.uk/biomodels/MODEL2407300002?format=json",
            "Archive title/description identify the focal eight-species Stylissa model.",
        ),
        (
            "bioproject",
            "project.xml",
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=602572&retmode=xml",
            "Returned accession PRJNA602572 is a broad marine-sponge metagenome project, not solely four focal specimens or a metabolomics archive.",
        ),
        (
            "massive",
            "massive.html",
            "https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?accession=MSV000083743",
            "Returned accession/task identifies public EMP soil and fecal GC-MS data. No replacement focal accession inferred.",
        ),
        (
            "code-tag",
            "sty8-tag-correct.json",
            "https://api.github.com/repos/zhssakura/STY8/git/ref/tags/v1.0.0",
            "Tag resolves to 17fd9c4eb5bd1f4cdf2c6402a2cdf3958e380546; immutable tree inventory inspected, code not executed.",
        ),
        (
            "zenodo",
            "zenodo.json",
            "https://zenodo.org/api/records/14030749",
            "DOI10.5281/zenodo.14030749 is STY8 v1.0.0 software metadata linked to the source repository.",
        ),
    ]:
        ev(eid, "database", url, "Fresh metadata/listing", summary, OUT / file)
    ev(
        "snippets",
        "validation",
        TARGET,
        "target-audit.json exact whitespace-normalized match",
        "All 14 current snippets match fresh primary XML; lexical matching does not certify each "
        "claim's scientific scope.",
        OUT / "target-audit.json",
    )
    ev(
        "history",
        "record_content",
        HISTORY,
        "Full sidecar and inline curation history",
        "New environment block/append are preserved, but sidecar details cite unrelated 39604529. "
        "Correct with a new append-only record; do not rewrite the old entry.",
        ROOT / HISTORY,
    )
    ev(
        "native-target",
        "validation",
        TARGET,
        "target-audit.json and native metrics rubric",
        "No target network issues;6 nodes, 2 arrows, 9 node evidence items. Completeness 80; quality 100 capped "
        "from 104 with 2 P2 + 3 P3. Neither score is scientific approval.",
        OUT / "target-audit.json",
    )
    ev(
        "source-scope",
        "validation",
        ARTICLE,
        "Current author reading scope and source receipts",
        "Complete scientific main, all six main figures, scientific SI text and selected tables read. "
        "No model execution, raw sequence/spectra/statistical reanalysis or external code execution.",
        OUT / "article.xml",
    )
    for rid in CONTEXT_IDS:
        ev(
            "context-" + rid,
            "record_content",
            "reviews/structured/" + rid + "/review.yaml",
            "Only ev-sponge-pmid39738126 or assess-c2s5-biomodels-environment-term and associated grouped lineage",
            "Bounded source correction: focal DOI 10.1038/s41467-024-55222-w, four Great Barrier Reef "
            "samples December 2015; not Red Sea or DOI s43705-024-00531-6. Prior purported source "
            "quotation is not present in focal primary text. Other cohort targets/dispositions not reassessed.",
            ROOT / "reviews/structured" / rid / "review.yaml",
        )
    checks = []
    for item in json.loads((OUT / "checks-receipts.json").read_text()) + json.loads(
        (OUT / "network-receipts.json").read_text()
    ):
        name = item["name"]
        network = name in {"audit-network", "check-network-quality"}
        summary = (
            "Full corpus: 44 warnings across 16 of 508 records,0 errors; known baseline, target has0 issues."
            if network
            else "Documented focused/native check passed with exit 0."
        )
        eid = "check-" + name
        command = shlex.join(item["command"])
        ev(
            eid,
            "validation",
            command,
            "Actual run " + item["started_at"] + " to " + item["finished_at"],
            summary,
            OUT / (name + (".stderr" if name == "check-network-quality" else ".stdout")),
            accessed=item["finished_at"],
        )
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "failed" if item["exit_code"] else "passed",
                "required": True,
                "summary": summary,
                "target_ids": [TARGET_ID],
                "command": command,
                "exit_code": item["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [eid],
                "scope_note": "Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src JUST_NO_DOTENV=true. Corpus failures are not target passes.",
            }
        )
    checks += [
        {
            "check_id": "scientific-source",
            "name": "Fresh scientific source reassessment",
            "status": "passed",
            "required": True,
            "summary": "Four original findings reassessed; five current open findings. Author pass, not independent approval.",
            "target_ids": [TARGET_ID],
            "evidence_ids": ["source-scope", "pubmed", "resources"],
        },
        {
            "check_id": "structured-adapter",
            "name": "iModulonDB applicability",
            "status": "not_applicable",
            "required": False,
            "summary": "No focal gene/locus/accession or covered strain-specific transcriptomic dataset is asserted; this is a MAG-derived model community.",
            "target_ids": [TARGET_ID],
            "evidence_ids": ["record", "model-methods"],
        },
        {
            "check_id": "cross-mech",
            "name": "Culture/ingredient identifiers",
            "status": "not_applicable",
            "required": False,
            "summary": "No CultureMech/MediaIngredientMech link encoded; in-silico media are not wetlab cultivation.",
            "target_ids": [TARGET_ID],
            "evidence_ids": ["record", "model-methods"],
        },
    ]
    review["checks"] = checks
    review["evidence"] = evidence
    for finding in review["findings"]:
        finding["previous_occurrences"] = [
            {"repository": REPO, "review_id": OLD_ID, "finding_id": finding["finding_id"]}
        ]
        if finding["finding_id"] == "computational-context":
            finding["title"] = "Complete computational provenance after the environment repair"
            finding["description"] = (
                "The added ENVO:01001002 environment is supported. Fourteen computational evidence items still lack queryable model/tool/scenario provenance; recoverable model context remains incompletely represented. This residual finding does not demand every optional field."
            )
            finding["field_paths"].remove("environment_term")
            finding["field_paths"].remove("modeled_environment")
        if finding["finding_id"] == "resource-scope":
            finding["evidence_ids"] += ["bioproject", "massive", "code-tag", "zenodo"]
    review["findings"].append(
        {
            "finding_id": "history-source-identity",
            "issue_key": "cm-000013-history-source-identity",
            "category": "provenance",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "P3: bounded audit-trail source mismatch; the current environment claim itself is supported.",
            "rule_id": "review-checklist.audit",
            "status": "open",
            "certainty": "confirmed",
            "title": "Correct the environment-history source identity append-only",
            "description": "The new 2026-10-25 history sidecar details cite PMID:39604529, an unrelated NLRP3 author correction. The sponge source is PMID:39738126/doi:10.1038/s41467-024-55222-w. Inline record notes retain the correct PMID.",
            "target_ids": [TARGET_ID],
            "field_paths": ["events[0].details in " + HISTORY],
            "evidence_ids": ["history", "pubmed"],
            "owner_paths": [{"repository": REPO, "path": HISTORY, "role": "append_only_history"}],
        }
    )
    for action in review["actions"]:
        if action["action_id"] == "repair-computational-context":
            action["acceptance_checks"][
                -1
            ] = "Retain the now-supported ENVO:01001002 animal-associated environment. Distinguish Great Barrier Reef natural sampling and modeled mesohyl in source-grounded notes where useful; do not require every optional modeled_environment field. Put simulated media in computational provenance, never invented wetlab vessels/temperature/salinity; preserve host-input and host-respiration limitations."
        if action["action_id"] == "repair-eight-member-roster":
            action["acceptance_checks"][
                1
            ] = "Fresh NCBI metadata verifies Candidatus Spongiicolonus versatilis 2973585, Candidatus Spongiihabitans thiooxidans 1671877 and Candidatus Oxydemutator thiolithooxidans 2973566; Parasynechococcus 2881427 is genus-level. Preserve source-name notes and unresolved identities rather than inventing species CURIEs/GTDB mappings; reverify candidates during curation."
    review["actions"].append(
        {
            "action_id": "append-history-source-correction",
            "description": "Append a history correction without rewriting old provenance.",
            "finding_ids": ["history-source-identity"],
            "target_ids": [TARGET_ID],
            "owner_paths": [
                {
                    "repository": REPO,
                    "path": "history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network",
                    "role": "append_only_history",
                }
            ],
            "acceptance_checks": [
                "Append a new native history event referencing the 2026-10-25 sidecar, correcting 39604529 to 39738126 and focal DOI 10.1038/s41467-024-55222-w; preserve original history bytes.",
                "State that the animal-associated environment itself is supported, and validate the new history entry. Do not invent a fresh canonical-record change merely to correct provenance.",
            ],
        }
    )
    for assess in review["assessments"]:
        aid = assess["assessment_id"]
        if aid == "provenance":
            assess.update(
                summary="The new host-associated environment is supported; fourteen computational claims still lack structured provenance.",
                details="Retain ENVO:01001002 and its source-backed sponge context. Recover software/model/MAG/scenario provenance with no invented cultivation. Natural sampling is Great Barrier Reef, December 2015; simulated mesohyl and medium constraints are model context. No requirement to populate all optional fields.",
            )
        elif aid == "resources":
            assess["evidence_ids"] += ["bioproject", "massive", "code-tag", "zenodo"]
        elif aid == "history":
            assess.update(
                outcome="concern",
                summary="All 14 snippets match and graph repairs persist, but the appended history cites an unrelated source.",
                details="Environment addition is sound; sidecar PMID:39604529 needs append-only correction. Historic unread-source limitations are not rewritten. This current author read expanded primary/supplement scope; no canonical/cache/history content changed.",
                evidence_ids=["history", "pubmed", "snippets", "source-scope"],
            )
        elif aid == "metrics":
            assess["summary"] = (
                "Completeness rises 75 to 80 after environment repair; quality remains capped 100, distinct from five open findings."
            )
            assess["metrics"][0].update(
                value=80,
                definition="50required-fields/roles +5environment +10nodes +5resources +5datasets +5metabolites; factor/media bonuses0.",
            )
            assess["metrics"][1].update(
                value=100,
                definition="clamp(100-50P1-10P2-2P3+20min(mean node evidence/2,1)+15ifCOMPLETE,0,100); P1=0/P2=2/P3=3/P4=0,9/6mean evidence, raw 104 capped 100.",
            )
            next(x for x in assess["metrics"] if x["name"] == "P3")["value"] = 3
    review["assessments"].append(
        {
            "assessment_id": "bounded-prior-source-correction",
            "area": "provenance",
            "topic": "Sponge-specific context in c2s4/c2s5 reviews",
            "outcome": "supported",
            "target_ids": [TARGET_ID],
            "evidence_ids": ["pubmed", "roster", "model-methods"]
            + ["context-" + rid for rid in CONTEXT_IDS],
            "summary": "Correct the sponge source identity, geography and unsupported quotation in three prior-review contexts.",
            "details": "The two c2s4 ev-sponge-pmid39738126 entries incorrectly couple PMID:39738126 with DOI 10.1038/s43705-024-00531-6 and a Red Sea statement presented as a quotation. The focal source instead identifies DOI 10.1038/s41467-024-55222-w and four Great Barrier Reef specimens collected December 2015; the quoted sentence is not present. The c2s5 environment assessment repeats Red Sea and is corrected here only for 000013. ENVO:01001002 remains sound. No terminal disposition or supersession of communitymech-c2s4-biomodels-missing-environment-term is made, and 000006/000007/000008 are not assessed or dropped from that grouped lineage.",
        }
    )
    review["limitations"] = [
        "Eight merged/representative MAG reconstructions are seven bacteria and one archaeon; no host model or cultured eight-strain consortium.98.3 percent denominator is MAG-mapped reads.",
        "Complete scientific main and all six main figure pixels were read, along with scientific SI text/TablesS1-S3. Supplementary figure captions were read, but SI figure pixels and whole raw SourceData matrices were not independently analyzed. SD2/9/12/13 were read; SD5/7/11 inspection is limited to relevant model media/exchange rows and headers.",
        "Candidate host inputs rely on two samples per group; source/delivery, host respiration and reciprocal fitness are unresolved. No model execution, RDS deserialization, external code execution, raw sequence/spectra/FISH/flux/statistical reanalysis.",
        "Current corpus checks exit 1 with44 warnings across 16 of 508 records,0 errors. Target native network has0 issues; neither is a whole-corpus scientific approval.",
        "SD7/11 NO/nitrite compound identifiers disagree and SD7 header placement differs from numeric pairs; use narrative/figures for bounded direction without importing those IDs. SI model-name variants and the S.thiooxidans abundance statement are not silently imported into canonical fields.",
        "Public archive metadata verifies listings and source pointers, not model reproducibility or correct focal metabolomics deposition. MSV000083743 currently resolves to EMP soil/fecal data; no replacement accession inferred.",
        "Fresh NCBI checks verify four candidate taxon records only. Proposed names otherwise retain uncertainty; no global absence or species-level GTDB mapping asserted. Historical GTDB support counts not recomputed.",
        "The initial inspection failed on CLAUDE.md symbolic-link resolution; readable canonical AGENTS.md was inspected instead. No file/symlink was changed. Initial wrong-owner STY8 URLs and aggregate-supplement timeout were retained as failed acquisition receipts; corrected public routes succeeded.",
        "Prior cohort-review context is assessed only for 000013. Their grouped multi-target finding dispositions remain untouched; this is an author refresh awaiting independent review.",
    ]
    review["notes"] = [
        "Immutable successor; original four stable keys retain exact previous_occurrences. No original bundle or canonical/cache/history file rewritten.",
        "Scratch candidates are JSON; only the native helper writes saved YAML/Markdown. Helper scripts were formatted before final inspection and are frozen inputs.",
        "Native input count: "
        + str(len(review["source"]["inputs"]))
        + ". Source receipt timestamps denote fresh retrieval; assertions reflect the separately stated actual reading scope.",
    ]
    review["related_reviews"] = [
        {
            "repository": REPO,
            "review_id": OLD_ID,
            "relationship": "Original single-target observation; all four finding lineages retained.",
        }
    ] + [
        {
            "repository": REPO,
            "review_id": rid,
            "relationship": "Bounded sponge source-context correction only; no grouped supersession or other-target disposition.",
        }
        for rid in CONTEXT_IDS
    ]
    review["tags"] = ["record-review", "sponge", "computational", "batch-07", "staleness-refresh"]
    (OUT / "review-candidate.json").write_text(json.dumps(review, indent=2) + "\n")
    print(
        json.dumps(
            {
                "review_id": review["review_id"],
                "findings": len(review["findings"]),
                "inputs": len(review["source"]["inputs"]),
            }
        )
    )


if __name__ == "__main__":
    main()
