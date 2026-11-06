"""Author the immutable PR2036/146 successor from inspected current inputs.

Writes JSON scratch only. Use the native review saver separately; no canonical
record, cache, history or historical review is edited.
"""

from __future__ import annotations

import copy
import json
import re

import yaml
from pr2036_146_audit import OLD, ROOT, SCRATCH, TARGET, now, run, sha, write

ID = "CommunityMech:000146"
HISTORY = "history/records/Anammox_Granule_Metabolic_Interaction_Community/2026-11-05T165000Z-antigravity-2120a1.yaml"


def main():
    initial = json.loads((SCRATCH / "inspection.json").read_text())
    for item in initial["source"]["inputs"]:
        assert sha((ROOT / item["path"]).read_bytes()) == item["sha256"], item["path"]
    search = run(
        "local-search-v2",
        [
            "rg",
            "--no-ignore",
            "--hidden",
            "-l",
            "ncomms15416|Anammox_Granule_Metabolic_Interaction_Community",
            "references_cache",
            "history",
            "reports/causal_graph_review/decisions",
            "kb/taxa",
        ],
    )
    assert search.returncode == 0
    paths = {i["path"] for i in initial["source"]["inputs"] if i["role"] != "target"}
    paths.update(
        str(p.relative_to(ROOT))
        for p in SCRATCH.iterdir()
        if p.is_file()
        and not p.name.startswith(
            ("candidate", "native-validate", "inspect-final", "inspection-final")
        )
    )
    paths.add("scripts/adhoc/pr2036_146_review.py")
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
        args.extend(["--input", path])
    result = run("inspect-final-v2", args)
    assert result.returncode == 0, result.stderr.decode()
    inspected = json.loads(result.stdout)
    write("inspection-final-v2.json", inspected)
    old = yaml.safe_load((ROOT / OLD).read_text())
    doc = copy.deepcopy(old)
    timestamp = now()
    rid = timestamp[:19].replace("-", "").replace(":", "") + "Z-pr2036-anammox-granule-successor"
    doc.update(
        review_id=rid,
        title="Anammox granule community: current-main review successor",
        started_at=json.loads((SCRATCH / "inspect.json").read_text())["started_at"],
        finished_at=timestamp,
        source=inspected["source"],
        targets=inspected["targets"],
    )
    doc["reviewer"] = {
        "identity": "codex",
        "kind": "agent",
        "independence": "unknown",
        "independence_basis": "Author refresh of the stale PR 2036 review, with historical Codex graph curation. Independent adversarial approval is a separate pass and is not claimed here.",
    }
    doc["summary"] = (
        "Current main adds three ordinal abundance levels and two source-matching evidence items. These additions resolve the narrow missing-field observation already assessed by the later abundance review, without correcting taxonomy. All eight original findings remain open after fresh source review: four major findings concern AMX1 species precision, the CHB clade, exchange certainty and publication-as-dataset representation; four minor findings concern setting, cultivation evidence, background scope and media linkage. Eight focused checks pass; corpus warning exits remain explicit."
    )
    doc["scope"].update(
        description="Whole current record: three grouped taxonomic entries, four interaction nodes, three downstream arrows, 17 evidence occurrences, environmental and cultivation claims, dataset representation and three history sidecars. Primary abstract, introduction, Results, Discussion, Methods and Tables 1 and 2 were read; public publication, project and sample metadata were checked.",
        selection="PR 2036 stale-target refresh against current main. The parsed diff contains three abundance levels, two evidence items and one embedded history entry; other target data are semantically unchanged. Every original finding was reassessed.",
    )
    sources = {
        row["path"].split("/")[-1]: row
        for row in json.loads((SCRATCH / "sources.json").read_text())
    }
    evidence = [
        copy.deepcopy(e) for e in old["evidence"] if not e["evidence_id"].startswith("check-")
    ]
    by_id = {e["evidence_id"]: e for e in evidence}
    primary_ids = {
        "primary",
        "amx-identity",
        "chb-identity",
        "anammox",
        "nitrite",
        "peptides",
        "donors",
        "operation",
        "abundance",
    }
    for e in evidence:
        e["accessed_at"] = timestamp
        e.pop("snapshot_sha256", None)
        if e["evidence_id"] in primary_ids:
            e["snapshot_sha256"] = sources["primary.xml"]["sha256"]
            e["accessed_at"] = sources["primary.xml"]["accessed_at"]
    by_id["record"].update(
        locator="Whole current target: three grouped taxa, four nodes, three arrows and all 17 evidence occurrences",
        snapshot_sha256=sha((ROOT / TARGET).read_bytes()),
    )
    by_id["primary"].update(
        locator="Fresh Europe PMC PMC5460018 XML; abstract, introduction, all Results, Discussion, Methods, Table 1 and Table 2 text. Snapshot and retrieval receipt frozen under .temp/pr2036/146.",
        summary="The full main article and table text were inspected. The study reconstructs metabolic potential from community DNA/RNA mapping and does not directly trace partner-resolved exchange. Supplementary files and rendered figure geometry were not inspected.",
    )
    by_id["abundance"].update(
        summary="AMX1 is approximately 62% of the source abundance proxy and 54% of its expression proxy; CHB1 is approximately 21% and 26%, respectively. DOMINANT and ABUNDANT are defensible ordinal summaries under AbundanceEnum. The source describes other flanking genomes as moderately abundant, supporting COMMON as a qualitative aggregate descriptor, not a measured percentage for every taxon. These are genome-length-normalized DNA/RNA mapping proxies; DNA covers two collection events while RNA comes from the second. No absolute cell count or combined guild percentage is established."
    )
    for eid, filename in [
        ("pubmed", "publication.xml"),
        ("crossref", "crossref.json"),
        ("bioproject", "bioproject.json"),
        ("biosample_metagenome", "biosamples.xml"),
        ("biosample_transcriptome", "biosamples.xml"),
        ("biosample_miseq", "biosamples.xml"),
    ]:
        by_id[eid]["snapshot_sha256"] = sources[filename]["sha256"]
        by_id[eid]["accessed_at"] = sources[filename]["accessed_at"]
    by_id["bioproject"].update(
        reference=sources["bioproject.json"]["url"],
        locator="NCBI BioProject esummary result 343219: accession, title, project description and data type",
        summary="PRJNA343219 describes a 5 L laboratory anammox sequencing-batch reactor fed with anaerobic digester filtrate after nitritation. It matches the article's study context; the metadata does not itself audit raw sequence content.",
    )
    for eid, accession, description in [
        (
            "biosample_metagenome",
            "SAMN05785375",
            "Illumina HiSeq 2000 metagenome, 2 x 125 bp; collected September 9, 2015; SRA sample SRS1713242",
        ),
        (
            "biosample_transcriptome",
            "SAMN05785376",
            "Illumina HiSeq 2000 metatranscriptome, 2 x 125 bp; collected September 9, 2015; SRA sample SRS1713243",
        ),
        (
            "biosample_miseq",
            "SAMN05785373",
            "Illumina MiSeq metagenome S1, 2 x 300 bp; collected September 4, 2013; SRA sample SRS1713240",
        ),
    ]:
        by_id[eid].update(
            reference=sources["biosamples.xml"]["url"],
            locator=f"BioSample XML row {accession}: accession, title, sample identifiers and collection date",
            summary=f"{accession} identifies the source-described {description}. Metadata validates accession and sample type, not every deposited read or inferred MAG.",
        )
    by_id["ontology"].update(
        locator="Ten curated ID-label pairs; alternative ENVO setting identifiers checked separately",
        summary="All ten curated labels match current local OAK authority labels. ENVO:00002123 resolves to bioreactor and ENVO:01001405 to laboratory environment. These provide appropriate setting alternatives; syntax and matching labels cannot establish that the target organism belongs to a mapped taxon.",
        snapshot_sha256=sha((SCRATCH / "ontology-authorities.json").read_bytes()),
    )
    by_id["lineage"].update(
        locator="Fresh rdfs:subClassOf ancestry for NCBITaxon:1334117, NCBITaxon:795749 and NCBITaxon:1090",
        summary="Melioribacteraceae and Ignavibacteriaceae descend through Ignavibacteria and Ignavibacteriota (NCBITaxon:1134404), not Chlorobiota (NCBITaxon:1090), in the local NCBI authority. These are the families assigned to CHB1 and CHB2 in Table 1. This confirms the clade conflict despite valid labels; the existing GTDB block follows the incorrect anchor and has not been independently re-grounded.",
        snapshot_sha256=sha((SCRATCH / "source-family-ancestry.json").read_bytes()),
    )
    by_id["snippets"].update(
        locator="All 17 current evidence placements, including duplicated cultivation text and two newly added abundance quotations",
        summary="All 17 snippets match the freshly retrieved primary XML after NFKC and whitespace normalization with inline tags joined. The two new abundance quotations preserve the source wording. Exact text matching does not establish that a genome-recovery fragment supports atmosphere or influent identity.",
        snapshot_sha256=sha((SCRATCH / "snippet-replay.json").read_bytes()),
    )
    by_id["history"].update(
        locator="Target graph decision, all three history sidecars and current embedded history",
        summary="The prior graph decision explicitly qualified exchange and excluded non-graph metadata from certification, including unresolved species identity. The November 5 sidecar accurately describes the three abundance annotations and two added evidence items. Its scope is abundance annotation; it does not certify taxonomic identity or the eight outstanding findings.",
    )
    by_id["local-search"].update(
        search_scope="rg --no-ignore --hidden -l 'ncomms15416|Anammox_Granule_Metabolic_Interaction_Community' references_cache history reports/causal_graph_review/decisions kb/taxa",
        summary="An ignored-inclusive bounded search located the cache, history and prior decision. No file matching this DOI or exact slug was returned from kb/taxa; this is not an exhaustive search for every taxonomic synonym. Missing linkage observations concern the entire current target, not absence of matches in external registries.",
        snapshot_sha256=sha((SCRATCH / "local-search-v2.stdout.txt").read_bytes()),
    )

    def ev(eid, kind, reference, locator, summary, path):
        evidence.append(
            {
                "evidence_id": eid,
                "kind": kind,
                "reference": reference,
                "locator": locator,
                "summary": summary,
                "support": "supports",
                "accessed_at": timestamp,
                "snapshot_sha256": sha((ROOT / path).read_bytes()),
            }
        )

    ev(
        "predecessor",
        "prior_review",
        OLD,
        "All eight findings and their action plans",
        "All eight original findings were reassessed and remain open. Stable issue keys and exact predecessor finding references are retained.",
        OLD,
    )
    ev(
        "target-change",
        "record_content",
        ".temp/pr2036/146/target-semantic-diff.json",
        "Parsed comparison against the predecessor's frozen Git target; textual diff separately retained",
        "Only three abundance levels, two evidence objects and one embedded history entry were added. The remaining text diff is serialization, not a biological or claim-level change.",
        ".temp/pr2036/146/target-semantic-diff.json",
    )
    ev(
        "abundance-history",
        "record_content",
        HISTORY,
        "events[0] and current curation_history[1]",
        "The history description matches the source-backed additions. The narrow missing-abundance-field issue is resolved in the inspected later review; this observation does not retire unrelated taxonomic findings or rewrite prior history.",
        HISTORY,
    )
    ev(
        "abundance-review-context",
        "prior_review",
        "reviews/structured/20261105T171000Z-c7s5-remediation-verification/review.yaml",
        "Single-target finding c7s4-000146-anammox-granule-abundance-levels and its referenced Stage 4 occurrences",
        "The later review records a resolved missing-field observation. Current field presence and fresh source inspection substantiate only that narrow repair. This successor does not create another terminal disposition for that key and does not imply corrected AMX1 or CHB taxonomy.",
        "reviews/structured/20261105T171000Z-c7s5-remediation-verification/review.yaml",
    )
    ev(
        "abundance-schema",
        "authority",
        "src/communitymech/schema/communitymech.yaml",
        "AbundanceEnum and Taxon.abundance_level",
        "The abundance enum expresses ordinal prominence, explicitly not percentages. It supports a dominant AMX1, major CHB1-associated entry and moderately represented flanking group while retaining the exact proxy and group scope in evidence.",
        "src/communitymech/schema/communitymech.yaml",
    )
    ev(
        "alternative-settings",
        "authority",
        ".temp/pr2036/146/alternative-settings.json",
        "Direct OAK lookup of two candidate ENVO settings",
        "Both bioreactor and laboratory environment labels resolve. The appropriate choice is a later curation decision grounded in the laboratory experimental setting.",
        ".temp/pr2036/146/alternative-settings.json",
    )
    ev(
        "target-network",
        "validation",
        ".temp/pr2036/146/target-network.json",
        "Fresh NetworkIntegrityAuditor.audit_community result",
        "The entire target has no structural network warnings. This does not establish the scientific correctness of participant identifiers or hypothetical transfer edges.",
        ".temp/pr2036/146/target-network.json",
    )
    ev(
        "adapter-discovery",
        "search",
        ".temp/pr2036/146/adapter-discovery.json",
        "Executable lookup and two exact expected sibling CLAW paths, including ignored paths",
        "No installed kg-microbe-sources runner was found, and both inspected sibling checkout paths are absent. This is a bounded lookup, not a claim about every filesystem location.",
        ".temp/pr2036/146/adapter-discovery.json",
    )
    ev(
        "expression-catalog",
        "database",
        sources["imodulon-catalog.json"]["url"],
        "Complete returned public catalog: 20 organism entries and their dataset keys",
        "No returned catalog organism corresponds to the source Brocadia or Ignavibacteria populations, and no exact AMX1/CHB study dataset is listed. A broad Bacteria placeholder does not establish a strain match to another organism's expression modules. The actual study's metatranscriptomic source and metadata provide the applicable evidence.",
        sources["imodulon-catalog.json"]["path"],
    )
    doc["checks"] = []
    for prior in old["checks"]:
        cid = prior["check_id"]
        if cid == "structured-expression-adapter":
            doc["checks"].append(
                {
                    "check_id": cid,
                    "name": "Structured expression-source applicability",
                    "status": "not_applicable",
                    "required": False,
                    "summary": "Native runner unavailable in bounded lookup; public catalog fallback inspected. No exact source-population dataset match was found in the returned catalog. This is not negative evidence for the study's expression claims.",
                    "target_ids": [ID],
                    "evidence_ids": [
                        "adapter-discovery",
                        "expression-catalog",
                        "biosample_transcriptome",
                    ],
                }
            )
            continue
        receipt = json.loads((SCRATCH / f"{cid}.json").read_text())
        output = (SCRATCH / f"{cid}.stdout.txt").read_text() + (
            SCRATCH / f"{cid}.stderr.txt"
        ).read_text()
        summary = (
            "Actual fresh corpus run: 503 records, 44 warnings in 16 records, zero errors; exit 1 retained. The current target has no network issues. No canonical corpus remediation was performed."
            if cid in {"audit-network", "check-network-quality"}
            else output.strip() or "Command completed without reported issues."
        )
        command = (
            " ".join(f"{k}={v}" for k, v in sorted(receipt["environment"].items()))
            + " "
            + receipt["command"]
        )
        doc["checks"].append(
            {
                "check_id": cid,
                "name": cid,
                "status": "passed" if receipt["exit_code"] == 0 else "failed",
                "required": True,
                "summary": summary,
                "target_ids": [ID],
                "command": command,
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + cid],
                "scope_note": "Focused target/history checks passed; cache-name preflight was clean. All inspected canonical inputs retain their initial hashes. Both corpus warning exits remain visible.",
            }
        )
        ev(
            "check-" + cid,
            "validation",
            command,
            f"Actual execution {receipt['started_at']} to {receipt['finished_at']}; receipt .temp/pr2036/146/{cid}.json",
            summary,
            f".temp/pr2036/146/{cid}.json",
        )
    for f in doc["findings"]:
        f["previous_occurrences"] = [
            {
                "repository": doc["repository"],
                "review_id": old["review_id"],
                "finding_id": f["finding_id"],
            }
        ]
    findings = {f["finding_id"]: f for f in doc["findings"]}
    findings["chb-clade"][
        "description"
    ] = "Table 1 assigns CHB1 and CHB2 to families now descending through Ignavibacteriota in the inspected NCBI ancestry, not Chlorobiota (NCBITaxon:1090). The current GTDB Chlorobiia block follows that incorrect anchor. Newly added abundance evidence does not correct taxonomic identity."
    findings["cultivation-evidence"][
        "description"
    ] = "The current cultivation evidence duplicates a genome-recovery quotation from engineering_design. It supports genome reconstruction rather than influent identity or anaerobic atmosphere. The source Methods provide directly relevant evidence; resolving the earlier source-verifiability backlog alone would not fix this semantic mismatch."
    assessments = {a["assessment_id"]: a for a in doc["assessments"]}
    assessments["identity"][
        "summary"
    ] = "Publication and record concern the same laboratory anammox granule enrichment. Three grouped entries are not three isolated organisms or an exhaustive census of the 17 recovered genomes."
    assessments["abundance"].update(
        summary="The new DOMINANT, ABUNDANT and COMMON levels are consistent qualitative summaries of the source's AMX1, CHB1-associated and moderately represented flanking populations. AMX1 and CHB1 values are DNA/RNA mapping proxies for recovered MAGs; CHB1 percentages must not be assigned to every CHB genome or a modern named clade, and COMMON does not encode a combined guild percentage. The two new snippets match the source exactly after documented normalization.",
        evidence_ids=["record", "abundance", "abundance-schema", "snippets", "target-change"],
    )
    assessments["history"][
        "summary"
    ] = "Three sidecars preserve the earlier snippet and graph repairs plus the November 5 abundance additions. The new event matches the actual parsed diff. The open discussion correctly keeps exchange unresolved; an abundance-field repair does not certify taxonomy, datasets or causal claims."
    assessments["history"]["evidence_ids"].extend(["abundance-history", "target-change"])
    assessments["validation"][
        "summary"
    ] = "Eight focused/history/preflight commands pass. All 10 curated ID-label pairs resolve and all 17 evidence placements match the fresh primary XML. Additional family-ancestry inspection confirms identity errors beyond label/syntax gates. The target network audit is empty, while both corpus commands retain their real warning exits."
    assessments["validation"]["evidence_ids"].append("target-network")
    assessments["node-0"][
        "details"
    ] = "AMX1 is encoded as NCBITaxon:795830, but Table 1 supports Brocadia affiliation rather than confirmed sinica identity. Ammonium/nitrite use and expressed anammox potential are supported at the study-MAG level. The linked primary evidence gives exact source locators and brief quotations. No stronger exchange claim is justified."
    assessments["metrics"][
        "summary"
    ] = "Completeness 95 counts populated fields, including the misrepresented dataset; validation quality 79.5 reflects four open major and four open minor findings. Neither score is scientific approval."
    metrics = {m["name"]: m for m in assessments["metrics"]["metrics"]}
    metrics["completeness"][
        "definition"
    ] = "min(100, 50 required metadata including roles + 5 environment + 10 for at least 3 factors + 10 for at least 3 nodes + 5 external resources + 10 media + 5 datasets + 5 node metabolites). 50 + 5 + 10 + 10 + 0 + 10 + 5 + 5 = 95. The populated dataset counts mechanically despite its representation defect."
    metrics["validation_quality"][
        "definition"
    ] = "clamp(100 - 50*P1 - 10*P2 - 2*P3 + 20*min(mean node evidence/2, 1) + 15 if native COMPLETE, 0, 100). Open P1=0, P2=4, P3=4, P4=0; 5 evidence items / 4 nodes = 1.25; all 3 declared entries participate structurally. 100 - 40 - 8 + 12.5 + 15 = 79.5."
    doc["assessments"].append(
        {
            "assessment_id": "bounded-abundance-repair",
            "area": "provenance",
            "topic": "Scope of the later abundance-field remediation",
            "outcome": "supported",
            "summary": "Current field presence, exact source evidence and the November 5 sidecar support the narrow resolution recorded for c7s4-000146-anammox-granule-abundance-levels. This assessment creates no additional terminal disposition and supersedes no unrelated or grouped review. The eight original findings remain open, especially AMX1 species precision and CHB modern-clade identity.",
            "target_ids": [ID],
            "evidence_ids": [
                "abundance-review-context",
                "abundance-history",
                "target-change",
                "abundance",
                "abundance-schema",
            ],
        }
    )
    doc["evidence"] = evidence
    next(e for e in evidence if e["evidence_id"] == "adapter-discovery")[
        "search_scope"
    ] = "PATH lookup via shutil.which plus exact filesystem existence checks of /Users/marcin/Documents/VIMSS/ontology/Mechs/culturebotai-claw and /Users/marcin/Documents/VIMSS/ontology/culturebotai-claw, including gitignored paths. No machine-wide absence claim."
    doc["limitations"] = [
        "Supplementary files, raw reads, accessioned MAG assemblies and rendered figure geometry were not inspected; no independent sequence reconstruction or flux measurement is claimed.",
        "Fresh local NCBI ancestry confirms the CHB clade conflict. Replacement GTDB grounding and exact accessioned MAG identity require separate curation; coherence gates do not certify the existing biological assignments.",
        "Abundance and expression values are genome-mapping proxies, not absolute cell counts. Qualitative group annotations must not be interpreted as per-organism measurements or percentages of a modern named clade.",
        "Required corpus checks retain nonzero warning exits; clean target participation does not verify participant identity or mechanism.",
        "The native structured-expression runner was unavailable in a bounded lookup. The public catalog fallback had no exact source-population match; primary study text and deposited sample metadata were used, without treating catalog absence as biological evidence.",
        "Media matching was not searched across external registries. The missing-link finding concerns this target's absent identifiers and does not assert that no exact applicable registry resource exists.",
    ]
    doc["notes"] = [
        "Original immutable review bytes are preserved. This successor records fresh input hashes, source snapshots and actual check receipts.",
        "Canonical records, caches, history and generated products were not changed by this author refresh.",
        "All eight original findings are retained with exact predecessor references; no new scientific curation finding was identified in this refresh.",
        "Five verified short quotations inherited from the primary paper total 22 words; other source content is paraphrased with locators.",
        "Independent adversarial review is performed separately from this author pass.",
    ]
    doc["tags"] += ["pr-2036", "staleness-refresh", "successor"]
    # Improve punctuation in inherited prose while preserving IDs, paths and quotes.
    prose_fields = {
        "summary",
        "description",
        "details",
        "definition",
        "normalization_reason",
        "scope_note",
        "value",
    }

    def readable(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key in prose_fields and isinstance(item, str):
                    value[key] = re.sub(r"([,;])(?=\S)", r"\1 ", item)
                else:
                    readable(item)
        elif isinstance(value, list):
            for item in value:
                readable(item)

    readable(doc)
    candidate = write("candidate-v2.json", doc)
    result = run(
        "native-validate-v2",
        ["uv", "run", "python", "scripts/record_review.py", "validate", str(candidate)],
    )
    assert result.returncode == 0, result.stderr.decode() + result.stdout.decode()
    print(
        json.dumps(
            {
                "candidate": str(candidate),
                "review_id": rid,
                "target_sha256": sha((ROOT / TARGET).read_bytes()),
            }
        )
    )


if __name__ == "__main__":
    main()
