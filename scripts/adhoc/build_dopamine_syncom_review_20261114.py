"""Assemble the independently assessed dopamine SynCom16 review, 2026-11-14.

Inputs: pinned initial inspection, canonical record, anonymously read primary
paper/supplements, retained issues and fresh M5 receipts. Outputs: native review
candidate and checkpoint under .temp; serves #2710/#2708/#2773/#2774.
This authors assessments explicitly; it never edits canonical records or caches.
"""

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
STATE = ROOT / ".temp/m5-completion-20261114"
TARGET = "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml"
TARGET_ID = "CommunityMech:000516"
PAPER = "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/"
SOURCES = STATE / "dopamine-syncom-sources"
XML = STATE / "ecofab-relations/PMC13522444.xml"
CHECK_NAMES = ("schema", "strict", "terms", "references", "gtdb", "domain", "history")
PRIOR_ID = "20261107T030000Z-c9s4-record-deep-audit"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    initial_path = STATE / "dopamine-syncom-initial-inspection.json"
    initial = json.loads(initial_path.read_text())
    for item in initial["source"]["inputs"]:
        if digest(ROOT / item["path"]) != item["sha256"]:
            raise ValueError("initially assessed input changed: " + item["path"])
    inputs = {i["path"] for i in initial["source"]["inputs"]}
    inputs.update(
        [
            "conf/record_review.yaml",
            "docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
            f"reviews/structured/{PRIOR_ID}/review.yaml",
            "reports/m5-completion-20261114/scope.json",
            "scripts/adhoc/review_dopamine_syncom_20261114.py",
            "scripts/adhoc/build_dopamine_syncom_review_20261114.py",
            "scripts/adhoc/verify_completion_mapping_20261114.py",
            "scripts/gtdb_ground.py",
            ".temp/m5-completion-20261114/yolo-sources/NCBI2GTDB.tsv.gz",
            "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml",
            "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml",
        ]
    )
    for name in CHECK_NAMES:
        inputs.update(
            str((STATE / f"dopamine-syncom-{name}.{ext}").relative_to(ROOT))
            for ext in ("json", "log", "exit")
        )
    for name in ("shared-network", "shared-network-quality"):
        inputs.update(str((STATE / f"{name}.{ext}").relative_to(ROOT)) for ext in ("json", "log"))
    inputs.update(str(p.relative_to(ROOT)) for p in SOURCES.iterdir() if p.is_file())
    inputs.update(
        str((STATE / "ecofab-independent" / name).relative_to(ROOT))
        for name in (
            "dsm113524.html",
            "dsm113524.html.source.json",
            "arthrobacter-taxonomy.xml",
            "arthrobacter-taxonomy.xml.source.json",
            "ring-s2.xlsx",
            "ring-s2.txt",
            "ring-s2.xlsx.source.json",
        )
    )
    inputs.update(
        str((STATE / "ecofab-relations" / name).relative_to(ROOT))
        for name in (
            "PMC9765266.xml",
            "PMC9765266-retrieval.json",
            "PMC13522444-retrieval.json",
            "roster-comparison.json",
        )
    )
    inputs.add(str((STATE / "ecofab-relations.md").relative_to(ROOT)))
    inputs.add(str(initial_path.relative_to(ROOT)))
    inputs.update(
        str((STATE / f"dopamine-syncom-{name}-issue.md").relative_to(ROOT))
        for name in ("correlation-direction", "grounding-provenance")
    )
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(STATE / "dopamine-syncom-targets.yaml"),
    ]
    for path in sorted(inputs):
        command.extend(["--input", path])
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    inspected = json.loads(result.stdout)
    (STATE / "dopamine-syncom-final-inspection.json").write_text(result.stdout)
    record = yaml.safe_load((ROOT / TARGET).read_text())
    nodes = record["ecological_interactions"]
    if record["id"] != TARGET_ID or len(nodes) != 5 or any(n.get("downstream") for n in nodes):
        raise ValueError("Assessed target or graph changed")
    now = datetime.now(timezone.utc)
    finished = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    evidence, assessments, checks = [], [], []

    def ev(
        key,
        kind,
        reference,
        locator,
        summary,
        support="supports",
        quote=None,
        path=None,
        accessed_at=None,
    ):
        row = {
            "evidence_id": key,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "summary": summary,
            "support": support,
            "accessed_at": (accessed_at or finished).replace("+00:00", "Z"),
        }
        if quote:
            row["quote"] = quote
        if path:
            row["snapshot_sha256"] = digest(path)
        evidence.append(row)

    def assess(key, area, topic, outcome, summary, ids, details=None):
        area = {
            "environment": "grounding",
            "cultivation": "scope",
            "composition": "identity",
            "taxonomy": "grounding",
        }.get(area, area)
        row = {
            "assessment_id": key,
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "target_ids": [TARGET_ID],
            "evidence_ids": ids,
        }
        if details:
            row["details"] = details
        assessments.append(row)
        return row

    ev(
        "record",
        "record_content",
        TARGET,
        "Complete current record, lines1-967",
        "Read every populated section, sixteen members, five interactions and zero downstream arrows; initial input hash retained.",
        path=ROOT / TARGET,
    )
    ev(
        "design",
        "primary_source",
        PAPER,
        "Methods: Plant materials and plant growth (Sec8 paragraphs0-1); Bacterial strains and synthetic community inoculation (Sec9 paragraphs0-1); Results Sec3",
        "Ten natural B.distachyon lines; sterile start; two seedlings per40mL half-strength MS vessel,22C,16h light/8h dark,150micromol/m2/s,50%RH; pool equalOD1 cultures, add800microlitres at week1 to approximatelyOD.02 and harvest week4. NoPlants means plant-spent medium plus SynCom; fresh halfMS-only TeCtrl is distinct. The separate Bd21-3 dopamine treatment is not the assembled SynCom test.",
        quote="equal volumes were pooled together",
        path=XML,
    )
    ev(
        "roster",
        "primary_source",
        PAPER,
        "Methods Sec9 paragraph0; Fig3a labels; Data availability; compare SupplementaryData1 A3:A18",
        "The main Methods enumerates sixteen stocks including OAE603, excluding OAE829, and spells OAE515 consistently with Fig3a. Twelve isolates use R2A, OAS944/OAE497/OAE908 use0.1R2A, OAE603 usesLB; preculture30C/200rpm is separate from22C plant growth. Origin described collectively as switchgrass rhizosphere and bulk soil. CollectionDSM200000 denotes the collection, not the individual OAS925 accession.",
        quote="Methylobacterium OAE515",
        path=XML,
    )
    ev(
        "correlations",
        "primary_source",
        PAPER,
        "Results Sec4 paragraph1; Figure3a and legend; Methods Sec14",
        "Spent-medium dopamine ion intensity versus relative16S abundance, Spearman n28, two-sided unadjustedP. Positive OAS809 r.5044,P.00324; OAE497 .5033,.00332; OAE506 .4238,.01566; OAE881 .3930,.02609; OAE513 .3750,.03445. Negative OAS925 -.4773,.00574. These are genotype-confounded associations, not an intervention on dopamine in the assembled SynCom.",
        quote="No multiple-comparison adjustment was applied.",
        path=XML,
    )
    ev(
        "isolate-growth",
        "primary_source",
        PAPER,
        "Results Sec4 paragraph2; Figure3b and legend; Methods Effect of dopamine on bacterial growth, Sec19",
        "Each of the six isolates is assayed separately at0/50/100ug/mL dopamine, n4,30C in R2A or0.1R2A with matched0.1%methanol controls. FinalOD at100ug/mL increases for five positive-correlating isolates and decreases forOAS925;50ug/mL does not universally stimulate them (Bosea lower). Significance letters concern final measured points, not every timepoint or maximal rate. No catabolic flux or in-community causal mechanism follows.",
        quote="at 100 μg/mL",
        path=XML,
    )
    ev(
        "exudate-decrease",
        "primary_source",
        PAPER,
        "Results Sec4 paragraph0; Figure2b-c and legend; Methods Sec20",
        "Measured spent-medium dopamine is lower in SynCom versus axenic conditions pooled across lines (Fig2c n28axenic/n29SynCom,P=.0075,two-sidedt-test). Potential microbial consumption versus changed plant production/exudation remains unresolved. The experiment does not establish community action on host metabolism.",
        quote="potential microbial utilization",
        path=XML,
    )
    ev(
        "dopamine-identity",
        "primary_source",
        PAPER,
        "Figure2a; Methods Sec12; SupplementaryFigure9 panelsa-c",
        "Authentic standard retention and MS/MS support dopamine CHEBI18243, including precursor154.086 and fragment137.0597. Ion intensity in spent medium is not absolute exudate concentration; root tissue2.71mg/gFW is a different matrix and must not be transferred to medium dose.",
        path=XML,
    )
    for key, filename, locator, summary in (
        (
            "stock-table",
            "stocks.xlsx",
            "SupplementaryData1, sheet1 rows3-18, columnsA-C",
            "Sixteen named stocks and preferred growth media. CellA16 says Methylobacterium OAE51, inconsistent with main Methods and Fig3a OAE515; retain OAE515 and document the table typo. The table does not assign individual rhizosphere versus bulk-soil origins.",
        ),
        (
            "supplement",
            "supplement.pdf",
            "SupplementaryFigures1,9,11 visually inspected; captions1-14; Fig11 page11",
            "Fig1 separates SynCom, axenic and NoPlants arms, week1 inoculation and week4 harvest. Fig9 validates dopamine identity in root/spent-medium matrices. Fig11 separately verifies genotype variation in axenic spent medium with n6,WelchANOVA/DunnettT3; its genotype ordering is not proof of an in-community dopamine causal mechanism. Fig13 concerns a separate plant dopamine assay, not a rescue for node4's unresolved mechanism.",
        ),
        (
            "figure2",
            "fig2.png",
            "Actual Figure2 panelsa-c, visually inspected",
            "Standard/plant chromatograms and pooled extracellular dopamine differences are visible. Panelb's linewise groups are distinct from pooled panelc; the plotted decrease does not localize production or consumption.",
        ),
        (
            "figure3",
            "fig3.png",
            "Actual Figure3 panelsa-b, visually inspected",
            "Panel a shows six unadjusted significant correlations; panel b shows independent isolate dose responses. OAS925 response decreases; five others increase at100ug/mL. Bosea50ug/mL decreases relative to0, supporting the record's explicit100ug/mL scope.",
        ),
    ):
        meta = json.loads((SOURCES / (filename + ".source.json")).read_text())
        ev(
            key,
            "primary_source",
            meta["url"],
            locator,
            summary,
            path=SOURCES / filename,
            accessed_at=meta["retrieved_at"],
        )
    ev(
        "rank",
        "database",
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1663,1667",
        "Fresh NCBI Taxon1663 and1667 responses; DSM113524 catalogue identity/strain fields",
        "1663 is Arthrobacter genus;1667 is an unclassified species placeholder. DSM113524 is Arthrobacter sp. OAP107. Species remains unknown. Current data supports a genus refinement, not one arbitrary GTDB species/split genus.",
        path=STATE / "ecofab-independent/arthrobacter-taxonomy.xml",
    )
    ev(
        "stock-rank",
        "database",
        "https://www.dsmz.de/collection/catalogue/details/culture/DSM-113524",
        "Catalogue name, culture number and strain designation, capturedHTML lines143-163",
        "Catalogue ties the source's OAP107 to Arthrobacter sp. DSM113524; same stock as the source list.",
        path=STATE / "ecofab-independent/dsm113524.html",
    )
    ev(
        "coker-relation",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC9765266/",
        "Methods Isolate selection, XMLs4-1 paragraph0; source roster compared with DingSec9",
        "Coker final deposited sixteen shares fifteen stocks with Ding but includesOAE829 instead ofOAE603. The source final model is separate from Coker's17/18-isolate plant experiments; a quoted relation remains bounded while000087's record lacks resolved stock members.",
        path=STATE / "ecofab-relations/PMC9765266.xml",
    )
    meta = json.loads((STATE / "ecofab-independent/ring-s2.xlsx.source.json").read_text())
    ev(
        "ring-relation",
        "primary_source",
        meta["url"],
        "Ring-trial S2Table rows2-18 columnsA,K",
        "Ring17 equals Ding16 plusOAE829, with OAE603 retained. Its own OAS925-dropout SynCom16 is a third distinct set; no member equivalence is inferred beyond exact source stock identities.",
        path=STATE / "ecofab-independent/ring-s2.xlsx",
        accessed_at=meta["retrieved_at"],
    )
    ev(
        "schema",
        "record_content",
        "src/communitymech/schema/communitymech.yaml",
        "HostParticipationEnum, EffectDirectionEnum, HostMicrobialStatusEnum, evidence-source and scope enums",
        "AXENIC describes pre-inoculation status. HOST_IS_SOURCE defines a host factor acting on members; HOST_IS_TARGET defines members acting on host. EffectDirectionEnum describes what source does to measured target response. Correlation alone does not satisfy directional causal claims under the native checklist.",
        path=ROOT / "src/communitymech/schema/communitymech.yaml",
    )
    ev(
        "guidance",
        "record_content",
        "docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
        "Host participation and Interaction sign sections, lines65-96",
        "Documentation uses these positive/negative correlations as signed-edge examples; that conflicts with the stricter native scientific rule against upgrading association to direction. Correct the example alongside node tags.",
        support="refutes",
        path=ROOT / "docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
    )
    ev(
        "cache",
        "record_content",
        "references_cache/PMID_42660928.md",
        "Frontmatter content_type line30; full-text boundary line96; main article beginningline98",
        "Frontmatter says abstract_only although the file preserves appended full main text. Keep abstract/main/SI boundaries and correct metadata separately; shared issue2708 also affects000515, whose scientific review is outside this bundle.",
        support="refutes",
        path=ROOT / "references_cache/PMID_42660928.md",
    )
    ev(
        "prior",
        "record_content",
        "reports/m5-completion-20261114/scope.json",
        "Retained live issues2708/2710 and linked prior partial scientific audit receipt; later cohort review completeness assessment for000516",
        "Both prior issues remain open. The cohort90-point completeness audit is diagnostic, not a finding disposition. No earlier immutable scientific bundle is superseded by this narrower single-record assessment.",
        support="context_only",
        path=ROOT / "reports/m5-completion-20261114/scope.json",
    )
    mapping_path = SOURCES / "mapping-comparison.json"
    mapping = json.loads(mapping_path.read_text())
    if mapping["record_sha256"] != digest(ROOT / TARGET):
        raise ValueError("mapping receipt used a different target")
    matched = sum(r["numeric_core_matches_native"] for r in mapping["rows"])
    ev(
        "mapping-reproduction",
        "validation",
        str(mapping_path.relative_to(ROOT)),
        "All sixteen taxonomy selectors; native aggregate denominator, unnamed rows excluded",
        f"Fresh read-only reproduction from recovered crosswalk SHA256{mapping['mapping_sha256']} matches{matched} ordinary stored numerical cores. Curated Allobosea/Bosea is deliberately not matched by current label; Paenibacillus remains33-option ambiguous and Arthrobacter1667 unresolved. This reproduces numerical mappings but supplies no GTDB release/build metadata.",
        support="context_only",
        path=mapping_path,
    )
    for name in (*CHECK_NAMES, "shared-network", "shared-network-quality"):
        prefix = "dopamine-syncom-" if name in CHECK_NAMES else ""
        receipt = json.loads((STATE / f"{prefix}{name}.json").read_text())
        log = STATE / f"{prefix}{name}.log"
        if receipt.get("log_sha256") != digest(log) or "exit_code" not in receipt:
            raise ValueError("Incomplete or modified check: " + name)
        if datetime.fromisoformat(receipt["finished_at"]) > now:
            raise ValueError("Assessment predates check: " + name)
        key = "check-" + name
        required = name in CHECK_NAMES
        ev(
            key,
            "validation",
            str(log.relative_to(ROOT)),
            (
                "Full fresh M5 native log and JSON receipt"
                if required
                else "Shared whole-corpus network diagnostic"
            ),
            (
                f"M5 revision {receipt['head']}, exit{receipt['exit_code']}; receipt retains exact command, stages and timestamps."
                if required
                else "Wider corpus48warnings in17of549records and zero errors; exit1 is explicit and not a focal scientific verdict."
            ),
            support="context_only",
            path=log,
        )
        checks.append(
            {
                "check_id": name,
                "name": "Native " + name,
                "status": "passed" if receipt["exit_code"] == 0 else "failed",
                "required": required,
                "summary": (
                    "Focused current-input gate."
                    if required
                    else "Nonrequired wider-corpus diagnostic; unresolved warnings retained."
                ),
                "target_ids": [TARGET_ID],
                "command": shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [key],
            }
        )

    assess(
        "identity",
        "identity",
        "One engineered hydroponic SynCom, distinct from native soil",
        "supported",
        "Identity, ENGINEERED/SYNTHETIC origin and RHIZOSPHERE model agree with the16-stock ten-host-line design. CommunityMech000515 is a separate native soil experiment.",
        ["record", "design", "roster", "supplement"],
        "Selectors id/name/description/ecological_state/community_origin/community_category/engineering_design. Direct plant-associated experiment is IN_VIVO; single-isolate growth is IN_VITRO; separate native soil assay is MESOCOSM. EqualOD pool is not evidence of equal realized abundance or persistence.",
    )
    assess(
        "host-environment",
        "environment",
        "Host, anatomy, laboratory and modeled rhizosphere",
        "supported",
        "NCBITaxon15368 B.distachyon, ten named genotypes and PO0009005 root context are appropriate; sampled material is medium bathing roots. AXENIC applies before inoculation. ENVO01001405 laboratory and modeled ENVO00005801 rhizosphere preserve artificial versus modeled setting.",
        ["design", "supplement", "schema", "check-terms"],
        "Selectors host.*, environment_term, modeled_environment, environmental_factors[0]. No roots-only community or soil field sample is implied; the n6 axenic replication supports genotype-associated dopamine variation, not the same samples as Figure3.",
    )
    assess(
        "cultivation",
        "cultivation",
        "Separate plant cultivation and isolate preparation",
        "supported",
        "HalfMS40mL, PTL100, two seedlings,22C16/8h150micromol/m2/s50%RH, week1 inoculation/week4 harvest match Methods and SI1. R2A/.1R2A/LB at30C200rpm describe separate stock preparation; current notes keep that separation.",
        ["design", "roster", "stock-table", "supplement"],
        "Selectors growth_media[0], cultivation_setup[0], engineering_design. HYDROPONIC_VESSEL is the native controlled-vocabulary choice. No optional CultureMech media linkage is invented; absence does not itself fail review.",
    )
    taxa = record["taxonomy"]
    stock_names = ", ".join(t["strain_designation"]["strain_name"] for t in taxa)
    assess(
        "composition",
        "composition",
        "Sixteen declared inoculum stocks with measured-detection limits",
        "supported",
        "The sixteen main-text stocks match the record and media assignments. MucilaginibacterOAE612 was not recovered from16S profiling; current note does not infer viability loss or removal from the inoculum. Individual rhizosphere origin wording follows the Results collective origin but Methods includes bulk soil; no strain-local site refinement is justified by Data1.",
        ["record", "roster", "stock-table"],
        "Selectors taxonomy[*].strain_designation and composition language. Stocks: "
        + stock_names
        + ". Data1A16 OAE51 is an internal source typo relative to Methods/Fig3a OAE515; retain OAE515 with this conflict visible. No functional role is populated or demanded without evidence.",
    )
    for index, taxon in enumerate(taxa):
        term = taxon["taxon_term"]
        special = {
            1: "Published Burkholderia is retained as the source synonym of curated Paraburkholderia; DSM200000 is explicitly the collection.",
            4: "Canonical Allobosea85413 with curated GTDBBosea34/34 is preserved, not silently rewritten from its spelling.",
            7: "Paenibacillus is explicitly AMBIGUOUS; retain split-genus uncertainty without selecting an arbitrary candidate.",
            8: "Source Methods/Fig3a support OAE515; Data1A16 OAE51 conflict is disclosed.",
            9: "OAP107 remains1667 UNRESOLVED despite source-linked genus1663; finding2774 preserves unknown species and requires reproducible grounding.",
            10: "16S non-detection does not invalidate intended inoculum membership or establish extinction.",
            15: "Published BacillusOAE603 is retained as the source synonym of curated Gottfriedia; the stock is also present in ringS2.",
        }.get(
            index,
            "Source genus and stock identity agree; no species-level identity or ecological role is inferred.",
        )
        assess(
            f"taxon-{index}",
            "taxonomy",
            term["preferred_term"],
            "concern" if index == 9 else "supported",
            f"{term['term']['id']} ({term['term']['label']}), stock{taxon['strain_designation']['strain_name']}; status{term.get('gtdb_grounding_status')}. "
            + special,
            ["roster", "stock-table", "check-terms", "check-gtdb", "mapping-reproduction"]
            + (["rank", "stock-rank"] if index == 9 else []),
            f"Selector taxonomy[{index}]. Current term/coherence checks pass; recovered crosswalk reproduces13ordinary numerical cores. Historical mapping release/build claims remain unresolved in grounding-provenance; current-label failure for curated Allobosea is not a reason to discard its valid legacy mapping.",
        )
    contexts = [
        (
            "concern",
            "correlations",
            "IN_VIVO association: host-exuded dopamine versus five member relative abundances across ten host genotypes. Positive sign supported; host-caused increase unproved.",
            "RhodococcusOAS809, MarmoricolaOAE513, RhizobiumOAE497, LysobacterOAE881, BoseaOAE506",
            "No established causal source/target direction; current HOST_IS_SOURCE/INCREASES exceeds association evidence.",
        ),
        (
            "concern",
            "correlations",
            "IN_VIVO association: host-exuded dopamine versus OAS925 relative abundance, Spearmann28. Negative sign supported; dopamine-induced depletion in the host SynCom unproved.",
            "ParaburkholderiaOAS925 (source Burkholderia)",
            "No established causal source/target direction; current HOST_IS_SOURCE/DECREASES exceeds association evidence.",
        ),
        (
            "supported",
            "isolate-growth",
            "IN_VITRO intervention on separate isolates in R2A/.1R2A,30C,n4:100ug/mL dopamine increases finalOD600. Community-level scope here groups named members; prose explicitly says monoculture and forbids an in-SynCom mechanism.",
            "RhodococcusOAS809, MarmoricolaOAE513, RhizobiumOAE497, LysobacterOAE881, BoseaOAE506",
            "Source exogenous dopamine -> individual isolate growth increase; no host participant, catabolic flux or signalling mechanism established.",
        ),
        (
            "supported",
            "isolate-growth",
            "IN_VITRO intervention on OAS925 monoculture,30C,R2A,n4:50/100ug/mL dopamine decreases finalOD600. Inhibitory mechanism is not determined.",
            "ParaburkholderiaOAS925 (source Burkholderia)",
            "Source exogenous dopamine -> individual isolate growth decrease; no host participant and no mechanism inferred.",
        ),
        (
            "concern",
            "exudate-decrease",
            "IN_VIVO wholeSynCom versus axenic comparison of spent-medium dopamine atweek4; pooledn28/n29 and two-sidedt-test. This is a treatment-associated extracellular endpoint, not direct host metabolic-response measurement.",
            stock_names,
            "WholeSynCom inoculation -> lower measured extracellular dopamine; host-target/consumption mechanism unresolved. HOST_IS_TARGET is unsupported; keep endpoint direction in prose.",
        ),
    ]
    for i, (outcome, evidence_id, context, participants, direction) in enumerate(contexts):
        assess(
            f"node-{i}",
            "graph",
            nodes[i]["name"],
            outcome,
            context,
            [evidence_id, "figure3" if i < 4 else "figure2", "dopamine-identity", "schema"],
            f"Selector ecological_interactions[{i}]. Participants: {participants}. {direction} "
            "Metabolite CHEBI18243 dopamine; biological process "
            + (
                "GO0040007 growth."
                if i in (2, 3)
                else "GO0044419 interspecies biological process, a broad context not a specific mechanism."
            )
            + " DOI10.1038/s41467-026-76211-1, PMID42660928. Linked primary evidence supplies exact source locator and inspected quote. Host when relevant is B.distachyonNCBITaxon15368; host is not a community member.",
        )
    assess(
        "edges",
        "graph",
        "Explicit edge inventory",
        "supported",
        "Five interaction nodes; zero downstream edges. All five nodes were assessed separately. No missing optional causal edges are invented or treated as a defect.",
        ["record", "check-strict", "check-shared-network", "check-shared-network-quality"],
        "Selectors ecological_interactions[*].downstream: absent throughout. Graph-reference integrity is vacuously complete for this target; that does not certify typed node direction or causal biology.",
    )
    assess(
        "relations",
        "identity",
        "Bounded source-based relations",
        "supported",
        "000516 is a member subset of ring000025, overlaps fifteen of Cokerfinal16 in000087, and shares study with soil000515. Typed directions and quoted stock differences match primary lists. Unknown000087 member resolution is not silently filled from these comparisons.",
        ["roster", "coker-relation", "ring-relation", "check-strict"],
        "Selectors related_communities[0:3]. These claims do not confer full scientific approval on related records. The current SOURCE_STATEMENT basis for000087 preserves explicit quoted evidence while that record lacks an enumerated maintained roster.",
    )
    assess(
        "evidence-provenance",
        "evidence",
        "Claim-local evidence and cache boundary",
        "concern",
        "Current record generally separates IN_VIVO plant observations and IN_VITRO isolates, and retains PARTIAL caveats. Primary full main text, Figures2/3, SI1/9/11 and stockData1 were read directly. Cache abstract_only metadata is wrong; passing snippet matching does not resolve it.",
        ["cache", "correlations", "isolate-growth", "exudate-decrease", "check-references"],
        "Selectors evidence throughout, references_cache/PMID_42660928.md. PMID36472419 is separately read for relation provenance. Discussion is independently assessed because reference-validator success is not complete Discussion claim coverage (#476). No paid providers, user emails or authenticated downloads used.",
    )
    assess(
        "discussion-resources-history",
        "scope",
        "Open scientific question, optional resources and history",
        "supported",
        "dopamine_substrate_or_signal remains a bounded open question. Main methods and claim-relevant supplement describe isolate dosing, not assembled-SynCom dopamine addition or selective host biosynthesis perturbation. Absence of optional datasets/resources is not a scientific finding. Existing dated creation/renumbering history remains unchanged and validates.",
        ["design", "isolate-growth", "exudate-decrease", "supplement", "check-history"],
        "Selectors discussions[0], curation_history. No raw-data reanalysis or exhaustive literature-absence claim. Root tissue amount, plant dopamine follow-up and native-soil enrichment cannot be imported as proof of the community's dopamine-catabolic mechanism.",
    )
    findings = []

    def finding(key, stable, category, severity, title, description, fields, ids, issue):
        native = "P2" if severity == "major" else "P3"
        findings.append(
            {
                "finding_id": key,
                "issue_key": stable,
                "category": category,
                "severity": severity,
                "native_severity": native,
                "normalization_reason": (
                    "Unsupported directional biological claim changes interpretation."
                    if native == "P2"
                    else "Bounded provenance/grounding defect; source stock identity and main measured result remain interpretable."
                ),
                "rule_id": "review-checklist.claim-specific-support-and-context",
                "status": "open",
                "certainty": "confirmed",
                "title": title,
                "description": description,
                "target_ids": [TARGET_ID],
                "field_paths": fields,
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/CommunityMech",
                        "path": TARGET,
                        "role": "canonical_record",
                    }
                ],
                "evidence_ids": ids,
                "external_issues": [
                    f"https://github.com/CultureBotAI/CommunityMech/issues/{issue}"
                ],
            }
        )

    finding(
        "host-target-scope",
        "cm-000516-exudate-decrease-host-target-scope",
        "scope",
        "major",
        "Preserve unresolved host versus microbial mechanism",
        "Retain #2710: extracellular dopamine decrease does not identify a host-target response. Remove optional HOST_IS_TARGET unless direct evidence establishes altered host metabolism; preserve pooled endpoint and alternative explanations.",
        ["ecological_interactions[4].host_participation", "ecological_interactions[4].description"],
        ["exudate-decrease", "figure2", "schema", "prior"],
        2710,
    )
    finding(
        "cache-content-type",
        "cm-pmid42660928-cache-content-type",
        "provenance",
        "minor",
        "Correct shared Ding source cache content type",
        "Retain #2708: frontmatter abstract_only disagrees with the appended full main text. This bundle assesses its use for000516 only;000515 remains affected and is not silently superseded or cleared.",
        ["references_cache/PMID_42660928.md:content_type"],
        ["cache", "check-references", "prior"],
        2708,
    )
    findings[-1]["owner_paths"] = [
        {
            "repository": "CultureBotAI/CommunityMech",
            "path": "references_cache/PMID_42660928.md",
            "role": "shared_reference_cache",
        }
    ]
    finding(
        "correlation-direction",
        "cm-000516-correlation-direction-scope",
        "scope",
        "major",
        "Keep correlation nodes free of unsupported causal direction",
        "Explicitly correlational nodes0/1 carry causal HOST_IS_SOURCE and signed-effect fields. Isolate perturbations support nodes2/3 only. Remove causal tags or introduce an explicitly noncausal typed representation; correct the documentation example.",
        [
            "ecological_interactions[0].host_participation",
            "ecological_interactions[0].effect_direction",
            "ecological_interactions[1].host_participation",
            "ecological_interactions[1].effect_direction",
        ],
        ["correlations", "figure3", "isolate-growth", "schema", "guidance"],
        2773,
    )
    findings[-1]["owner_paths"].append(
        {
            "repository": "CultureBotAI/CommunityMech",
            "path": "docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
            "role": "curation_guidance",
        }
    )
    finding(
        "grounding-provenance",
        "cm-000516-grounding-provenance",
        "provenance",
        "minor",
        "Refine OAP107 rank and reproduce mapping provenance",
        "OAP107 remains an unclassified1667 placeholder rather than supported genus1663; fourteen mappings repeat unverified latest/build wording. Preserve species and Paenibacillus uncertainty and curated Allobosea/Bosea mapping. Current coherence checks do not identify historical map release.",
        [
            "taxonomy[9].taxon_term",
            "ecological_interactions[4].participating_taxa[9].term",
            "taxonomy[*].taxon_term.gtdb_classification.mapping_source",
        ],
        ["rank", "stock-rank", "stock-table", "check-terms", "check-gtdb", "mapping-reproduction"],
        2774,
    )
    counts = {p: sum(f["native_severity"] == p for f in findings) for p in ("P1", "P2", "P3", "P4")}
    excerpts = sum(len(n.get("evidence", [])) for n in nodes)
    required = all(
        record.get(k)
        for k in ("id", "name", "description", "taxonomy", "ecological_state", "community_category")
    ) and all(t.get("functional_role") for t in taxa)
    completeness = (
        50 * required
        + 5 * bool(record.get("environment_term"))
        + 10 * (len(record.get("environmental_factors", [])) >= 3)
        + 10 * (len(nodes) >= 3)
        + 5 * bool(record.get("external_resources"))
        + 10 * bool(record.get("growth_media"))
        + 5 * bool(record.get("associated_datasets"))
        + 5 * any(n.get("metabolites") for n in nodes)
    )
    raw_quality = (
        100
        - 50 * counts["P1"]
        - 10 * counts["P2"]
        - 2 * counts["P3"]
        + min(excerpts / len(nodes) / 2, 1) * 20
        + 15
    )
    metric = assess(
        "metrics",
        "completeness",
        "Two native scores, not scientific approval",
        "supported",
        "Literal native rubric: optional unsupported roles are not invented to improve completeness; high quality score does not clear open findings.",
        ["record", "prior"],
    )
    metric["metrics"] = [
        {
            "name": "completeness",
            "value": completeness,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "50 only if required fields including all taxon roles present (false);+5environment+10at least3factors(false)+10at least3nodes+5resources(false)+10medium+5datasets(false)+5metabolites. Literal rubric differs from earlier proportional cohort audit; missing optional roles are not a finding.",
        },
        {
            "name": "validation_quality",
            "value": max(0, min(100, raw_quality)),
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": f"100-50P1-10P2-2P3+20min(({excerpts}/{len(nodes)})/2,1)+15 structural graph completeness; raw={raw_quality}; capped0..100. Zero downstream edges makes reference integrity vacuously complete, not causal evidence.",
            "denominator": len(nodes),
        },
        {
            "name": "evidence_items",
            "value": excerpts,
            "unit": "items",
            "denominator": len(nodes),
            "definition": "Eight node-local EvidenceItems across five nodes; average1.6 per node. Count is not independent-source coverage.",
        },
    ] + [
        {
            "name": p,
            "value": n,
            "unit": "findings",
            "definition": "Native-severity count in this record review.",
        }
        for p, n in counts.items()
    ]
    actions = [
        {
            "action_id": "repair-" + f["finding_id"],
            "description": f["description"],
            "finding_ids": [f["finding_id"]],
            "target_ids": [TARGET_ID],
            "owner_paths": copy.deepcopy(f["owner_paths"]),
            "acceptance_checks": [
                "Address the exact field-level finding without broadening source support; append history for canonical changes; rerun seven focused checks and native generated-docs checks, then save a successor review with fresh input hashes."
            ],
        }
        for f in findings
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": now.strftime("%Y%m%dT%H%M%SZ") + "-m5-dopamine-syncom-primary-review",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "Dopamine SynCom16 full current-input scientific review",
        "started_at": datetime.fromtimestamp(initial_path.stat().st_mtime, timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "finished_at": finished,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Independent of canonical record author; read full current record and primary paper plus claim-relevant supplements, main figures and taxonomy authority; parent independently reviews saved bundle.",
        },
        "skill": "review-yaml-record",
        "completion": (
            "completed"
            if all(c["status"] == "passed" for c in checks if c["required"])
            else "partial"
        ),
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Full record scientific review retains2710/2708 and files2773/2774. Five nodes and sixteen members assessed; zero downstream arrows. Seven fresh M5 gates pass, while scientific/provenance findings remain open. No canonical changes made.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Entire CommunityMech000516 record; every populated dimension, five nodes and zero downstream edges; related records read only for source-linked membership context.",
            "selection": "One of four explicit recovered PR2102 records after successful saved EcoFAB canary.",
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
            "This is full scientific review of the record's existing claims, not exhaustive reanalysis of all source datasets or all supplements. Main Methods/Results and Figures2/3 read; SI1/9/11 visually inspected, claim-relevant captions and stockData1 inspected. No raw metabolomics,16S reanalysis or new numerical inference.",
            "Seven focused checks ran on fresh M5 revision76aa644cd6803ea2c9545d4c704276ede219d354. Final local inspection may have a later review-only commit; initial input hashes are checked unchanged before assembly. No canonical/cache/history writes by this helper.",
            "Shared full-corpus network diagnostics exit1 with48warnings17of549records, zero errors; neither full repository QC nor other three records are certified by this bundle.",
            "A recovered hashed GTDB crosswalk reproduces13ordinary numerical cores; curated Allobosea/Bosea needs legacy-label handling, Paenibacillus remains ambiguous and OAP107 placeholder unresolved. File recovery and numerical coherence do not establish its release/build date.",
            "Shared cache finding2708 also affects000515, outside this single-target scientific scope; no terminal disposition or supersession is asserted for it or earlier multi-record reviews.",
            "No complete search of issue comments or exhaustive external literature absence is claimed. Absent optional fields and unresolved dopamine mechanism are not filled with inferred roles or new causal arrows.",
        ],
        "related_reviews": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "review_id": PRIOR_ID,
                "relationship": "Prior diagnostic completeness assessment; current independent scientific review does not supersede unrelated targets or findings.",
            }
        ],
    }
    for item in inspected["source"]["inputs"]:
        if digest(ROOT / item["path"]) != item["sha256"]:
            raise ValueError("assessed input changed during build: " + item["path"])
    output = STATE / "dopamine-syncom-review-candidate.yaml"
    output.write_text(yaml.safe_dump(review, sort_keys=False, allow_unicode=True, width=100))
    (STATE / "dopamine-syncom-review-checkpoint.json").write_text(
        json.dumps(
            {
                "review_id": review["review_id"],
                "target": TARGET,
                "target_sha256": digest(ROOT / TARGET),
                "status": "native_candidate",
                "findings": [
                    {"issue": f["external_issues"][0], "key": f["issue_key"]} for f in findings
                ],
                "nodes": len(nodes),
                "downstream_edges": 0,
                "completeness": completeness,
                "quality_raw": raw_quality,
                "quality": max(0, min(100, raw_quality)),
                "evidence_items": excerpts,
                "required_checks_passed": sum(
                    c["status"] == "passed" for c in checks if c["required"]
                ),
            },
            indent=2,
        )
        + "\n"
    )
    print(output)


if __name__ == "__main__":
    main()
