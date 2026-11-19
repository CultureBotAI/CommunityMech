"""Author full current EcoFAB/Dopamine/LBNL scientific review, 2026-11-15.

Inputs: three exact current records, inspected primary sources, all applied-write
receipts/sidecars, immutable reviews and actual final native gates. Output: new
private candidate plus native inspection; native validate/save is separate.
Serves Phase2 #1427/#2675/#1548/#476/#1996 and provenance #2816/#2818.
Authored scientific judgments below are independent of native validator scores.
"""

import argparse
import copy
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
import build_phase2_linked_review_20261115 as proof  # noqa: E402

STATE = ROOT / ".temp/phase2-science-20261115"
BASE = "17616c9cad16a1b62cd6e9b39d82af4276e5188a"
proof.BASE = BASE
proof.GENERATION = "003"
TARGETS, IDS, REPOSITORY = proof.TARGETS, proof.IDS, proof.REPOSITORY
EXPECTED = {
    "ecofab": "7f5b0122647382d048e0b750d1c5f324b32f74868685d111db39d588c735b339",
    "dopamine": "304702c684faedb244d678e628ec174851dbdcafe46128eab86d824798e0482a",
    "lbnl": "bb31b1df4a9be2241453528101fc5d55657c23eccf1d58ce1cc9639e5912b368",
}
PRIOR_IDS = {
    "ecofab": "20261114T212137Z-m5-ecofab-completion-canary",
    "dopamine": "20261114T213444Z-m5-dopamine-syncom-primary-review",
    "lbnl": "20261115T021628Z-phase2-lbnl-canary",
    "delta": "20261114T221158Z-m5-postcuration-scientific-delta",
    "linked": "20261115T025004Z-phase2-linked-stock-delta",
}
APPLIES = [
    "curation-applied-001/receipt.json",
    "mapping-note-applied-001/receipt.json",
    "linked-stock-plan-003/ecofab/apply/receipt.json",
    "linked-stock-plan-003/dopamine/apply/receipt.json",
    "linked-stock-plan-003/lbnl/apply/receipt.json",
    "ecofab-scope-plan-002/apply/receipt.json",
]
PRIMARY = dict(proof.PRIMARY)
PRIMARY.update(
    {
        "ring-s1": STATE / "linked-retained/ecofab-independent/ring-s1.xlsx",
        "ring-s9": STATE / "linked-retained/ecofab-independent/ring-s9.xlsx",
        "ring-s8": STATE / "linked-retained/ecofab-independent/ring-s8.tif",
        "ring-s10": STATE / "linked-retained/ecofab-independent/ring-s10.tif",
        "ring-s11": STATE / "linked-retained/ecofab-independent/ring-s11.tif",
        "ding-fig2": STATE / "linked-retained/dopamine-syncom-sources/fig2.png",
        "ding-fig3": STATE / "linked-retained/dopamine-syncom-sources/fig3.png",
        "ding-supplement": STATE / "linked-retained/dopamine-syncom-sources/supplement.pdf",
        "coker-fig2": STATE / "lbnl-retained/lbnl-sources/fig2.png",
        "coker-fig3": STATE / "lbnl-retained/lbnl-sources/fig3.png",
        "coker-fig5": STATE / "lbnl-retained/lbnl-sources/fig5.png",
    }
)
URLS = {
    "ecofab": "https://doi.org/10.1371/journal.pbio.3003358",
    "dopamine": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/",
    "lbnl": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9765266/",
}


def sha(path):
    return proof.sha(path)


def relative(path):
    return str(path.resolve().relative_to(ROOT))


def load(path):
    return yaml.safe_load(path.read_text())


def verify(record):
    if sha(ROOT / TARGETS[record]) != EXPECTED[record]:
        raise ValueError("assessed current canonical bytes changed")
    return {
        gate: proof.verify_receipt(record, gate)
        for gate in (*proof.GATE_RECIPES, "references", "network")
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-record", choices=TARGETS)
    parser.add_argument("--expected-revision")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.verify_record:
        receipts = verify(args.verify_record)
        results = {gate: item[1]["exit_code"] for gate, item in receipts.items()}
        print(json.dumps({"record": args.verify_record, "verified_current_receipts": results}))
        raise SystemExit(int(any(results.values())))
    if args.output is None:
        raise ValueError("new private --output directory required")
    if not args.expected_revision:
        raise ValueError("actual committed review revision required")
    author(args.output.resolve(), args.expected_revision)


def author(output, review_revision):
    if output.exists() or not output.is_relative_to(STATE):
        raise ValueError("new exclusive private output required")
    if (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        != review_revision
    ):
        raise ValueError("actual review base changed")
    docs = {key: load(ROOT / path) for key, path in TARGETS.items()}
    receipts = {key: verify(key) for key in TARGETS}
    prior = {
        key: load(ROOT / f"reviews/structured/{ident}/review.yaml")
        for key, ident in PRIOR_IDS.items()
    }
    for key, expected in proof.EXPECTED_PRIMARY.items():
        if sha(PRIMARY[key]) != expected:
            raise ValueError("reviewed primary bytes changed")
    plan = json.loads((STATE / "ecofab-scope-plan-002/receipt.json").read_text())
    applied = json.loads((STATE / APPLIES[-1]).read_text())
    if applied["after_sha256"] != EXPECTED["ecofab"] or plan["after_sha256"] != EXPECTED["ecofab"]:
        raise ValueError("EcoFAB source/curation checkpoint differs")
    source_sets = {
        "ecofab": proof.RING_STOCKS,
        "dopamine": proof.DING_STOCKS,
        "lbnl": proof.COKER_STOCKS,
    }
    for key, doc in docs.items():
        stocks = [row["strain_designation"]["strain_name"] for row in doc["taxonomy"]]
        if len(stocks) != len(source_sets[key]) or set(stocks) != source_sets[key]:
            raise ValueError("primary-defined stock set changed")
    measurement_dir = STATE / "imported-root-lbnl-measurement-001"
    measurement = json.loads((measurement_dir / "measurement.json").read_text())
    parent = json.loads((measurement_dir / "receipt.json").read_text())
    if (
        sha(measurement_dir / "receipt.json")
        != "0e15273cb752653d0dda84289b0385e147d188ae254d856fa8263d885f6a61f0"
        or sha(measurement_dir / "measurement.json")
        != "64c9a1c9b53f372efdca908d389a0d6f27855ce90e6f9438edf0b9a24c5128c4"
        or parent["revision"] != "f52ff4ef36c59bace4271d4dc256e33d621ddabd"
        or not parent["inputs_unchanged"]
        or not measurement["measurement_valid"]
        or not measurement["assertion_coverage_complete"]
        or measurement["counts"]["snippet_surfaces"] != 37
        or measurement["counts"]["snippet_occurrences_compared"] != 37
        or measurement["assertion_status_counts"] != {"matched": 35, "mismatched": 2}
    ):
        raise ValueError("imported current LBNL coverage evidence differs")
    coverage_dir = STATE / "final-three-coverage-002"
    coverage = json.loads((coverage_dir / "measurement.json").read_text())
    coverage_receipt = json.loads((coverage_dir / "receipt.json").read_text())
    if (
        coverage_receipt["revision"] != review_revision
        or set(coverage_receipt["selected_records"]) != set(TARGETS.values())
        or not coverage_receipt["inputs_unchanged"]
        or not coverage["measurement_valid"]
        or not coverage["assertion_coverage_complete"]
        or coverage["counts"]["records_completed"] != 3
        or coverage["counts"]["snippet_surfaces"]
        != coverage["counts"]["snippet_occurrences_compared"]
        or coverage["assertion_status_counts"].get("mismatched") != 2
        or coverage["native_exit_code"] != 1
    ):
        raise ValueError("current three-record assertion measurement is incomplete or unbound")
    for path, expected in coverage_receipt["input_sha256"].items():
        if sha(ROOT / path) != expected:
            raise ValueError("measured assertion input changed: " + path)
    for key, path in TARGETS.items():
        if coverage_receipt["input_sha256"][path] != EXPECTED[key]:
            raise ValueError("measured record is not final assessed input")
    coverage_rows = {row["record"]: row for row in coverage["records"]}
    if set(coverage_rows) != set(TARGETS.values()):
        raise ValueError("unexpected measured record set")
    for key, path in TARGETS.items():
        assertions = coverage_rows[path]["assertions"]
        if not assertions or not all(row["actually_compared"] for row in assertions):
            raise ValueError("uncompared current assertion")
        mismatches = [row["path"] for row in assertions if row["status"] != "matched"]
        expected = (
            ["discussions[4].evidence[2].snippet", "discussions[4].evidence[4].snippet"]
            if key == "lbnl"
            else []
        )
        if sorted(mismatches) != expected:
            raise ValueError("unexpected measured source mismatch")
    inputs = {
        *TARGETS.values(),
        *proof.CACHES.values(),
        relative(Path(__file__)),
        "scripts/adhoc/build_phase2_linked_review_20261115.py",
        "scripts/adhoc/curate_phase2_ecofab_scope_20261115.py",
        "scripts/adhoc/check_phase2_linked_records_20261115.py",
        "scripts/adhoc/run_phase2_linked_gates_20261115.sh",
        "scripts/reference_assertion_coverage.py",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "src/communitymech/schema/history.yaml",
        "src/communitymech/validators/related_communities.py",
        "src/communitymech/validators/treatment_arms.py",
        "scripts/validate_strict.py",
        "conf/record_review.yaml",
        "conf/reference_validator.yaml",
        "uv.lock",
        "justfile",
        "docs/record-reviews.md",
        "docs/record-review-profile.md",
        ".claude/skills/curate-yaml-record/SKILL.md",
        ".claude/skills/review-communities/reference/metrics-and-reports.md",
    }
    inputs.update(relative(path) for path in PRIMARY.values())
    inputs.update(f"reviews/structured/{ident}/review.yaml" for ident in PRIOR_IDS.values())
    inputs.update(relative(STATE / name) for name in APPLIES)
    for name in (
        "lbnl-grounding-final16.json",
        "lbnl-supplement-tables.json",
        "linked-ecofab-grounding-001.json",
        "linked-dopamine-grounding-001.json",
        "ecofab-scope-plan-002/receipt.json",
        "ecofab-scope-plan-002/before.yaml",
        "ecofab-scope-plan-002/candidate.yaml",
        "curation-applied-001/before.yaml",
        "curation-applied-001/candidate.yaml",
        "mapping-note-applied-001/before.yaml",
        "mapping-note-applied-001/candidate.yaml",
    ):
        inputs.add(relative(STATE / name))
    inputs.update(relative(path) for path in measurement_dir.iterdir() if path.is_file())
    inputs.update(relative(path) for path in coverage_dir.iterdir() if path.is_file())
    for key in TARGETS:
        inputs.update(
            relative(path)
            for path in (ROOT / "history/records" / Path(TARGETS[key]).stem).glob("*.yaml")
        )
        inputs.update(
            relative(STATE / "linked-stock-plan-003" / key / name)
            for name in ("before.yaml", "candidate.yaml")
        )
        for path, receipt in receipts[key].values():
            inputs.update((relative(path), receipt["log"], relative(path.with_suffix(".exit"))))
        inputs.add(relative(STATE / f"linked-{key}-terms-003-oak.yaml"))
    output.mkdir()
    targets = [
        {
            "target_id": IDS[key],
            "path": path,
            "label": docs[key]["name"],
            "kind": "maintained",
            "ownership_note": "Full current canonical MicrobialCommunity record, all populated scientific fields and explicit retained source boundaries assessed.",
        }
        for key, path in TARGETS.items()
    ]
    target_file = output / "targets.yaml"
    target_file.write_text(yaml.safe_dump({"targets": targets}, sort_keys=False))
    inputs.add(relative(target_file))
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        relative(target_file),
    ]
    for path in sorted(inputs):
        command.extend(["--input", path])
    raw = subprocess.check_output(command, cwd=ROOT, text=True)
    (output / "inspection.json").write_text(raw)
    inspected = json.loads(raw)
    finished = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    evidence, assessments, checks = [], [], []

    def ev(key, kind, reference, locator, summary, path, quote=None):
        row = {
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
            row["quote"] = quote
        evidence.append(row)

    def assess(key, record, area, topic, summary, evidence_ids, details=None, outcome="supported"):
        row = {
            "assessment_id": key,
            "target_ids": [IDS[record]],
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "evidence_ids": evidence_ids,
        }
        if details:
            row["details"] = details
        assessments.append(row)
        return row

    primary_key = {"ecofab": "ring", "dopamine": "ding", "lbnl": "coker"}
    for key in TARGETS:
        ev(
            key + "-record",
            "record_content",
            TARGETS[key],
            "Every populated scientific field, exact current input SHA256, graph/roster and append-only provenance",
            "Full current record read against primary evidence; optional missing properties are not fabricated.",
            ROOT / TARGETS[key],
        )
        ev(
            key + "-primary",
            "primary_source",
            URLS[key],
            {
                "ecofab": "Results2.1–2.7; Methods4.1–4.10; DataAvailability",
                "dopamine": "Results dopamine panels/Figs2–3; Methods Sec8–9/Sec19; SupplementaryFigs1/9/11 and Data1",
                "lbnl": "Results nutrient/ratio/preservation/plant panels/Figs2–3/5; Methods s4-1 throughs4-7",
            }[key],
            {
                "ecofab": "Four treatment arms, seventeen stock/IMG/GOLD pairs, relative16S outcomes and separate culture/reporter/genomic contexts inspected. Treatment-level effects do not identify a necessary strain or molecular mechanism.",
                "dopamine": "Ten-host-line inoculum experiment, signed relative-abundance correlations, separate six-isolate dopamine doses and lower pooled spent-medium dopamine are different evidence contexts.",
                "lbnl": "Methods-defined final sixteen stocks differ from earlier18/17 assay rosters and TableS1. Earlier measured observations remain separately scoped; no final16 graph attribution or inferred stock alias.",
            }[key],
            PRIMARY[primary_key[key]],
        )
        ev(
            key + "-prior",
            "prior_review",
            f"reviews/structured/{PRIOR_IDS[key]}/review.yaml",
            "Earlier full primary assessment, preserved unchanged",
            "Earlier inspected facts are rechecked against current fields; current assessments below replace stale state descriptions, not prior evidence bytes.",
            ROOT / f"reviews/structured/{PRIOR_IDS[key]}/review.yaml",
        )
    for key, locator, summary in (
        (
            "ring-table",
            "S2Table rows2–18 columnsA–L",
            "All17 stocks, exact IMG/GOLD pairs, medium assignment and16-arm omission of OAS925 independently checked.",
        ),
        (
            "ring-s1",
            "S1Table rows2–6",
            "Laboratory-specific chamber/light/humidity/logger differences; prescribed values are not uniform measured exposures.",
        ),
        (
            "ring-s9",
            "S9Table T3SS signaturesM00660/M00542",
            "Computational module comparison does not establish expression, selective necessity or virulence.",
        ),
        (
            "ring-s8",
            "S8 figure genome/acid-resistance panels",
            "Surveyed gene profile supports hypothesis context, not unique causal necessity of each individual gene.",
        ),
        (
            "ring-s10",
            "S10 biofilm/growth plots and caption",
            "OAS925 is sixth for biofilm; growth groups and conditions are separate from ring-trial relative16S composition.",
        ),
        (
            "ring-s11",
            "S11 motility/pH/time plots and caption",
            "OAS925 motility advantage depends on assay pH/time/comparator, with no selective perturbation in SynCom17.",
        ),
        (
            "ding-table",
            "Supplementary Data1 stock/media table; A16",
            "Methods andFig3a identifyOAE515 while Data1A16 saysOAE51; preserve internal source discrepancy rather than create an alias.",
        ),
        (
            "ding-fig2",
            "Fig2 standard/plant chromatograms and pooled endpoint",
            "Authentic standard supports dopamine identity; pooled extracellular ion intensity is not secretion rate or absolute concentration.",
        ),
        (
            "ding-fig3",
            "Fig3a six Spearman associations and3b isolate growth",
            "n28 unadjusted correlations differ from n4 separate-isolate0/50/100µg/mL intervention; finalOD does not establish catabolic flux.",
        ),
        (
            "ding-supplement",
            "SupplementaryFigs1/9/11",
            "Experimental arms/timeline, dopamineMSMS/EIC identity and axenic genotype follow-up checked as separate contexts.",
        ),
        (
            "coker-supplement",
            "TableS1 DOCX table1 rows2–19; row12 OAE516 and row18 OAE603",
            "Earlier18 list conflicts with Methods final16:OAE516/OAE515 and Bacillus/Marmoricola are not reconciled by guessing.",
        ),
        (
            "coker-fig2",
            "Fig2 nutrient dilution panel",
            "Earlier18-member community R2A dilution changes diversity; it is not an experiment on the Methods final16 roster.",
        ),
        (
            "coker-fig3",
            "Fig3 initial-ratio and time panels",
            "Earlier-panel starting composition and2/6day outcomes do not create universal final16 abundance.",
        ),
        (
            "coker-fig5",
            "Fig5 in-planta and preservation-linked contexts",
            "Earlier18 and17-minus-Burkholderia host assays are kept separate from deposited final16 collection identity.",
        ),
    ):
        ref = URLS[
            "ecofab" if key.startswith("ring") else "dopamine" if key.startswith("ding") else "lbnl"
        ]
        ev(key, "primary_source", ref, locator, summary, PRIMARY[key])
    for key in TARGETS:
        path = STATE / (
            "lbnl-grounding-final16.json" if key == "lbnl" else f"linked-{key}-grounding-001.json"
        )
        ev(
            key + "-grounding",
            "database",
            relative(path),
            "Readonly NCBI genus labels/ranks/synonyms and native hash-pinned NCBI2GTDB reproduction",
            "Genus-level identity and recorded mapping votes inspected; crosswalk SHA761d5537… and original database hashes retained. Curated bacterial Bosea/Allobosea correspondence is explicit; ambiguous candidates remain unselected. This is not exact genome placement or current catalog verification.",
            path,
        )
    for index, name in enumerate(APPLIES):
        ev(
            f"apply-{index}",
            "record_content",
            relative(STATE / name),
            "Actual guarded write before/after hashes, original receipt bytes",
            "Applied history is evidence, not a planned completion assertion. Every predecessor and corrected current record is linked through actual receipts; all new native sidecars are separately hash-bound.",
            STATE / name,
        )
    ev(
        "lbnl-coverage",
        "validation",
        relative(measurement_dir / "measurement.json"),
        "Maintained native assertion measurement on parent f52ff4ef36c59bace4271d4dc256e33d621ddabd, same current000087 hash",
        "37 snippet surfaces were actually compared:35matched,2mismatched; SupportingReference is traversed. Measurement valid/coverage complete, native exit1 retained. This proves focal traversal, not scientific truth or corpus coverage.",
        measurement_dir / "measurement.json",
    )
    ev(
        "current-three-coverage",
        "validation",
        relative(coverage_dir / "measurement.json"),
        f"Maintained native occurrence measurement on exact committed source {review_revision}",
        f"All {coverage['counts']['snippet_surfaces']} current snippet surfaces were actually compared; "
        f"{coverage['assertion_status_counts']['matched']} matched and two LBNL supplemental cells mismatched. "
        "Inputs stayed unchanged. Complete lexical comparison coverage does not establish scientific truth.",
        coverage_dir / "measurement.json",
    )
    # Full section-level scientific assessments, followed by every member and graph assertion.
    assess(
        "ecofab-identity",
        "ecofab",
        "identity",
        "Source-defined ring trial and four distinct arms",
        "Engineered17-stock Bd21-3 laboratory root model is distinct from source soil, Coker final16 and Ding16. Four native arms represent source SynCom17, OAS925-omission16, axenic mock and plant-free mock; NO_MICROBES denotes intended control design, not a claim every sterility test was negative.",
        ["ecofab-primary", "ring-table", "ecofab-record"],
    )
    assess(
        "ecofab-conditions",
        "ecofab",
        "scope",
        "Plant ring trial, inoculum stocks and reporter assay separated",
        "Ring inoculation at source10-day seedlings and harvest22DAI is separate from reporter3-day plants and microscopy1/3DAI. Nine mLhalfMS plus1mLinoculum/mock,14hlight26°C/10hdark20°C withlabC16hlight exception,PPFD110–140 and humidity70%if tunable are prescribed conditions, not uniform measured exposure. Stock27°C2–8day/media/glycerol preparation differs from reporter27°C200rpmKan20mg/L and genomic/trait assays. Unrelated nitrogen-form experiment is no longer a ring intervention.",
        ["ecofab-primary", "ring-s1", "ring-table", "ecofab-record"],
    )
    assess(
        "ecofab-means",
        "ecofab",
        "scope",
        "Four observations retain arm, time and measurement scale",
        "OAS925 at 98 ± 0.03% belongs to SynCom17; OAS809 at 68 ± 33%, OAE908 at 14 ± 27%, and OAE515 at 15 ± 20% belong to the OAS925 omission treatment. All are root relative 16S means ± SD across laboratories, 22 days after inoculation. Absolute cell counts, growth rates and competitive extinction are not established. The unsupported OAP107 abundance statement at 21 days was removed.",
        ["ecofab-primary", "ecofab-record"],
        "Selectors taxonomy[*].abundance_observations; timepoint harvest-22dai; relative_abundance_unit PERCENT.",
    )
    assess(
        "ecofab-mechanism",
        "ecofab",
        "evidence",
        "Non-graph claims now respect measured endpoint scope",
        "Generic degrader/cross-feeder roles are absent. Description, OAS925 notes, engineering endpoints and amino-acid relevance distinguish whole-treatment outcomes from strain-specific uptake/harm. Genomic annotations and separate culture/reporter data remain candidate mechanisms; graph hypotheses are not presented as selectively established causes.",
        ["ecofab-primary", "ring-s8", "ring-s9", "ring-s10", "ring-s11", "ecofab-record"],
    )
    assess(
        "ecofab-resources",
        "ecofab",
        "provenance",
        "Source-reported study resources and exact genome identifiers",
        "The five preexisting study resources remain distinct amplicon, metabolomics, integrated study and phenotype datasets. The invalid GOLD pseudo-range is replaced by17 source stock/IMG/GOLD tuples including MycobacteriumGp0440934, with per-entry mainMethods evidence. Current server availability, raw reanalysis, assembly quality and exact strain genome-to-GTDB placement are not claimed.",
        ["ecofab-primary", "ring-table", "ecofab-record"],
    )
    assess(
        "dopamine-identity",
        "dopamine",
        "identity",
        "Engineered hydroponic inoculum and ten host lines",
        "Sixteen declared stocks, ten B.distachyon genotypes, sterile start and root-bathing liquid are correctly distinguished from the separate native-soil000515 experiment. EqualOD inoculation is not equal realized abundance. Mucilaginibacter16S nondetection does not remove it from the intended inoculum.",
        ["dopamine-primary", "ding-table", "ding-supplement", "dopamine-record"],
    )
    assess(
        "dopamine-conditions",
        "dopamine",
        "scope",
        "Plant and isolate contexts remain separate",
        "Two seedlings in40mLhalfMS/PTL100,22°C16/8h150µmol/m2/s50%humidity, week1inoculation/week4harvest match Methods. Separate stocks useR2A/.1R2A/LB at30°C200rpm. NoPlants uses plant-spent medium and differs from fresh medium TeCtrl; no treatment arm or monoculture result is silently equated with the assembled community.",
        ["dopamine-primary", "ding-table", "ding-supplement", "dopamine-record"],
    )
    assess(
        "dopamine-discussion",
        "dopamine",
        "evidence",
        "Dopamine identity and open substrate-versus-signal question",
        "CHEBI18243 is supported by standard retention and MSMS/EIC. Relative spent-medium intensity is not absolute concentration or secretion rate; root2.71mg/gFW is not exudate dose. The open substrate/signalling question remains bounded because isolate finalOD effects do not identify consumption, catabolic flux or host biosynthesis mechanisms. Optional missing resources are not invented.",
        ["dopamine-primary", "ding-fig2", "ding-fig3", "ding-supplement", "dopamine-record"],
    )
    assess(
        "lbnl-identity",
        "lbnl",
        "identity",
        "Methods-defined final16 collection with unresolved source correspondence",
        "The current record explicitly denotes sixteen Methods stock/DSM assertions. Earlier18/17 assays remain discussions, not final16 graph nodes. Methods/TableS1 OAE515/OAE516 and Marmoricola/Bacillus differences remain explicit; no alias or stock-equivalence inference is made.",
        ["lbnl-primary", "coker-supplement", "lbnl-record"],
        outcome="concern",
    )
    assess(
        "lbnl-conditions",
        "lbnl",
        "scope",
        "Laboratory setting, source soil and assay-dependent cultivation",
        "ENVO01001405 laboratory setting and modeled/sourceENVO00001998soil are distinct. Isolate preculture3–5mL1xR2A30°C5–7days differs from200µLcommunity panels with dilution/time-dependent harvests and host24°C regime. No universal72h protocol, shaking condition or final16 treatment arm is invented.",
        ["lbnl-primary", "lbnl-grounding", "lbnl-record"],
    )
    for key, topic, summary, source in (
        (
            "nutrient",
            "Earlier18-member nutrient observation",
            "Discussion1 preserves the earlier18-member nutrient-dilution result and its3dayR2A context, without attributing the outcome to all16 current stock assertions.",
            "coker-fig2",
        ),
        (
            "ratios",
            "Earlier inoculum-ratio/time observation",
            "Discussion2 retains initial-ratio and2/6day temporal-composition evidence with its original panel context; neither a universal abundance nor final16 causal graph is inferred.",
            "coker-fig3",
        ),
        (
            "plant",
            "Earlier18/17 host observations",
            "Discussion3 preserves the earlier18 and17-minus-Burkholderia plant experiment and its host-culture conditions without equating either roster with the final16 collection.",
            "coker-fig5",
        ),
        (
            "gaps",
            "Ecological mediation and TableS1 uncertainty",
            "Discussions0/4 distinguish unresolved mechanism from measured compositional observations and retain the exact source stock disagreement. The two supplemental cell quotes remain true source quotes despite article-only matcher failures.",
            "coker-supplement",
        ),
    ):
        assess(
            "lbnl-" + key,
            "lbnl",
            "scope",
            topic,
            summary,
            ["lbnl-primary", source, "lbnl-record"],
            outcome="concern" if key == "gaps" else "supported",
        )
    for key, doc in docs.items():
        for index, item in enumerate(doc["taxonomy"]):
            stock = item["strain_designation"]["strain_name"]
            term = item["taxon_term"]["term"]
            state = item["taxon_term"].get("gtdb_grounding_status", "not supplied")
            extra = {
                "OAP107": "Arthrobacter1663 is genus-level, with11 unselected GTDB candidates.",
                "OAE506": "Curated Allobosea85413/bacterial Bosea34/34 mapping and original flags are retained.",
                "OAE614": "Paenibacillus split-genus mapping remains ambiguous; no candidate is selected.",
                "OAS925": "Individual DSM113627 is distinct from complete ring consortium DSM200000SY.",
                "OAE603": "Source Bacillus stock is preserved under curated Gottfriedia genus; no unrelated stock phenotype transferred.",
                "OAE515": "Ding Data1OAE51 and Coker TableS1OAE516 discrepancies remain distinct from this Methods stock assertion.",
            }.get(
                stock,
                "No species identity, functional role or precise study-stock genome mapping is inferred from genus membership.",
            )
            assess(
                f"{key}-stock-{stock.lower()}",
                key,
                "grounding",
                f"{stock}: {term['label']}",
                f"Primary study list supports stock {stock}; canonical {term['id']} ({term['label']}) is genus-level grounding with native status {state}. {extra}",
                [
                    key + "-primary",
                    key + "-grounding",
                    key + "-record",
                    (
                        "ring-table"
                        if key == "ecofab"
                        else "ding-table" if key == "dopamine" else "coker-supplement"
                    ),
                ],
                f"Selector taxonomy[{index}]; primary stock/deposit claim is not independent current collection catalog verification. Current mapping inputs and retained numerical cores are hash-bound.",
            )
        assess(
            key + "-relations",
            key,
            "consistency",
            "All populated related-community claims reviewed",
            "Ring17=Coker final16+OAE603 and ring17=Ding16+OAE829; the two16-stock collections overlap15. Reciprocal SHARED_STRAIN_DESIGNATIONS compares complete source stocks and coherent deposits; earlier Coker assay rosters remain distinct. The dopamine link to000515 denotes a shared study, not matching community membership or whole-record scientific certification.",
            ["ecofab-primary", "ring-table", "dopamine-primary", "lbnl-primary", key + "-record"],
        )
        assess(
            key + "-provenance",
            key,
            "provenance",
            "Actual corrections, immutable predecessors and native sidecars",
            "All applied receipts affecting this three-record campaign and every new native sidecar are explicit inputs. Linked stock correction and EcoFAB experimental-scope correction preserve old history and review bytes. No planned or failed run is substituted for an applied receipt.",
            [key + "-record", key + "-prior", *[f"apply-{i}" for i in range(len(APPLIES))]],
        )
    graph_summary = {
        "ecofab": [
            (
                "Whole SynCom17 treatment",
                "IN_VIVO full17 inoculum versus source controls in Bd21-3 EcoFABs; three downstream arrows are treatment effects. Participants identify the inoculum, not equal final abundance or member-specific necessity.",
                "Results2.1/2.3–2.5; Methods4.2",
            ),
            (
                "OAS925 candidate traits",
                "COMPUTATIONAL genomic profile, separate IN_VIVO RFP-root1/3DAI and IN_VITRO culture/motility data are distinct. OAS925 ranks sixth for biofilm. No selective perturbation identifies trait necessity; the arrow remains explicitly HYPOTHESIZED.",
                "Results2.7; Methods4.7–4.10; S8–S11",
            ),
            (
                "Relative root assembly",
                "IN_VIVO OAS925 relative16S dominance at22DAI, with a distinct omission16 comparator. Relative reads do not prove absolute suppression, extinction or a molecular competition mechanism.",
                "Results2.4; Fig3; Methods4.6",
            ),
            (
                "Net extracellular amino-acid cluster",
                "IN_VIVO bulk spent medium under whole treatment. CHEBI33709 amino-acid context is supported; plant/microbe production, uptake and extracellular enzymes remain alternatives. No OAS925-specific flux or donor-recipient exchange established.",
                "Results2.5; Fig4; Methods4.4–4.5",
            ),
            (
                "Plant biomass/development",
                "IN_VIVO SynCom17 versus axenic pooled-lab biomass and reduced root development after14DAI, with laboratory variation. GO0040007growth is an endpoint; no single-stock toxicity or reciprocity claim.",
                "Results2.3; Fig2b–c",
            ),
        ],
        "dopamine": [
            (
                "Positive Spearman association",
                "IN_VIVO dopamine intensity versus relative16S abundance for OAS809/OAE513/OAE497/OAE881/OAE506 across genotypes, n28. Positive association does not establish a host-to-microbe effect; current causal source/direction tags are absent.",
                "Fig3a; ResultsSec4",
            ),
            (
                "Negative OAS925 association",
                "IN_VIVO OAS925 relative abundance negatively correlates with dopamine, n28; this does not establish depletion caused by dopamine. Current HOST_IS_SOURCE and signed-effect tags are absent.",
                "Fig3a; ResultsSec4",
            ),
            (
                "Separate-isolate growth increase",
                "IN_VITRO100µg/mL dopamine increases finalOD of five separately cultured isolates, n4 at30°C. These are not assembled-SynCom results or catabolic-flux measurements;50µg/mL does not uniformly stimulate all five.",
                "Fig3b; MethodsSec19",
            ),
            (
                "Separate-isolate growth decrease",
                "IN_VITRO OAS925 finalOD decreases at50/100µg/mL dopamine in monoculture, n4 at30°C. Mechanism remains unresolved; no host participation is implied.",
                "Fig3b; MethodsSec19",
            ),
            (
                "Lower spent-medium dopamine",
                "IN_VIVO wholeSynCom versus axenic pooledn29/n28 spent-medium dopamine is lower. Endpoint direction is SynCom treatment to extracellular dopamine; host-output versus microbial-use mechanism remains unresolved. Current HOST_IS_TARGET/effect_direction absent.",
                "Fig2c; ResultsSec4",
            ),
        ],
    }
    for key, rows in graph_summary.items():
        nodes = docs[key]["ecological_interactions"]
        if len(nodes) != len(rows):
            raise ValueError("unassessed graph node")
        for index, (topic, summary, locator) in enumerate(rows):
            node = nodes[index]
            ev_ids = [key + "-primary", key + "-record"]
            for position, item in enumerate(node.get("evidence", [])):
                identifier = f"{key}-node-{index}-source-{position}"
                ev(
                    identifier,
                    "primary_source",
                    URLS[key],
                    locator,
                    summary,
                    PRIMARY[primary_key[key]],
                    item["snippet"],
                )
                ev_ids.append(identifier)
            participants = [
                x.get("preferred_term", x.get("term", {}).get("id", "unspecified"))
                for x in node.get("participating_taxa", [])
            ]
            if node.get("source_taxon"):
                participants.append(node["source_taxon"].get("preferred_term", "source stock"))
            assess(
                f"{key}-node-{index}",
                key,
                "graph",
                topic,
                summary,
                ev_ids,
                f"Exact selector ecological_interactions[{index}]. Participants: {', '.join(participants)}. Current source/target and mechanism are constrained to the authored summary; host is not microbial taxonomy. Every source quote and locator above is separate from validator success.",
            )
    for index, (topic, summary, locator, quote) in enumerate(
        [
            (
                "Treatment → root composition",
                "Full17 inoculation to22DAI root relative profile; omission16 supports composition effect, not molecular mechanism or absolute loss.",
                "Results2.4/Fig3",
                "98 ± 0.03%",
            ),
            (
                "Treatment → spent-medium profile",
                "Whole inoculation changes net extracellular abundance; plant versus microbial origin and flux remain unresolved.",
                "Results2.5/Fig4",
                "lower relative concentrations",
            ),
            (
                "Treatment → plant growth",
                "SynCom17 versus axenic treatment reduces biomass/root development; no necessary stock, nutrient competition or direct OAS925 toxicity inferred.",
                "Results2.3/Fig2",
                "consistent decrease",
            ),
            (
                "Trait hypothesis → root dominance",
                "Explicitly HYPOTHESIZED OAS925 traits may contribute; separate gene/culture/reporter data do not selectively establish mechanism in the17-member community.",
                "Discussion/Results2.7",
                "might facilitate",
            ),
        ]
    ):
        identifier = f"ecofab-arrow-{index}-source"
        ev(identifier, "primary_source", URLS["ecofab"], locator, summary, PRIMARY["ring"], quote)
        selector = (
            f"ecological_interactions[0].downstream[{index}]"
            if index < 3
            else "ecological_interactions[1].downstream[0]"
        )
        assess(
            f"ecofab-arrow-{index}",
            "ecofab",
            "graph",
            topic,
            summary,
            [identifier, "ecofab-record"],
            selector
            + "; arrow direction and experimental context inspected separately from node wording.",
        )
    assess(
        "dopamine-edges",
        "dopamine",
        "graph",
        "Five nodes and zero downstream arrows",
        "Every node was assessed above; downstream arrows are absent. Missing optional causal edges are not invented or treated as a defect.",
        ["dopamine-record", "dopamine-primary"],
    )
    assess(
        "lbnl-edges",
        "lbnl",
        "graph",
        "Zero graph nodes and zero arrows",
        "All three earlier measured observations remain individually evidenced discussions with18/17 scope. No empty-participant graph node is allowed to imply an effect of all16 final stock assertions.",
        ["lbnl-record", "lbnl-primary", "coker-fig2", "coker-fig3", "coker-fig5"],
    )
    for index, row in enumerate(plan["source_genome_rows"].values()):
        assess(
            f"ecofab-genome-{index}",
            "ecofab",
            "provenance",
            row["source_name"],
            f"MainMethods4.8 and S2 row{row['row']} report IMG{row['img']} paired with GOLD{row['gold']}. Current JGI_IMG dataset uses the IMG identifier and direct source link; GOLD pair is explicitly retained. No numerical range or independent assembly/genome-to-GTDB inference remains.",
            ["ecofab-primary", "ring-table", "ecofab-record"],
        )
    for key in TARGETS:
        for gate, (path, receipt) in receipts[key].items():
            identifier = f"check-{key}-{gate}"
            ev(
                identifier,
                "validation",
                receipt["log"],
                "Actual native focused command, exact current input hashes, full log",
                f"Base {BASE}, actual working record hash{EXPECTED[key]}, exit{receipt['exit_code']}; inputs unchanged. Reference failures remain literal.",
                ROOT / receipt["log"],
            )
            checks.append(
                {
                    "check_id": identifier,
                    "name": key + " " + gate,
                    "status": "passed" if receipt["exit_code"] == 0 else "failed",
                    "required": True,
                    "summary": "Executed current native gate; not scientific truth certification.",
                    "target_ids": [IDS[key]],
                    "command": shlex.join(receipt["command"]),
                    "exit_code": receipt["exit_code"],
                    "expected_exit_code": 0,
                    "evidence_ids": [identifier],
                }
            )
    findings = []

    def successor(prior_key, issue_key, status, description, evidence_ids):
        old = next(item for item in prior[prior_key]["findings"] if item["issue_key"] == issue_key)
        item = copy.deepcopy(old)
        item.update(
            finding_id=issue_key,
            status=status,
            description=description,
            disposition_reason=description,
            evidence_ids=evidence_ids,
            previous_occurrences=[
                {
                    "repository": REPOSITORY,
                    "review_id": PRIOR_IDS[prior_key],
                    "finding_id": old["finding_id"],
                }
            ],
        )
        findings.append(item)
        return item

    successor(
        "delta",
        "cm-000025-causal-role-evidence",
        "resolved",
        "Unsupported member roles, competitive-exclusion and OAS925-specific uptake/harm claims were removed or bounded to measured whole-treatment endpoints. All5 nodes/4qualified arrows remain; evidence tiers now separate computational genome, living-plant and isolate contexts. No selective mechanism is invented.",
        [
            "ecofab-primary",
            "ring-s8",
            "ring-s9",
            "ring-s10",
            "ring-s11",
            "ecofab-record",
            "apply-5",
        ],
    )
    successor(
        "delta",
        "cm-000025-study-stage-scope",
        "resolved",
        "Ring trial, stock preparation and reporter protocols are separated; unrelated nitrogen intervention removed. Four source-defined arms and four22DAIrelative-read observations are explicitly scoped. Unverified OAP10721DPIabundance is removed while stock/grounding remain intact.",
        ["ecofab-primary", "ring-table", "ring-s1", "ecofab-record", "apply-5"],
    )
    successor(
        "delta",
        "cm-000025-genome-identifiers",
        "resolved",
        "The invalid pseudo-range is replaced by17 exact stock-to-IMG/GOLD pairs from mainMethods4.8 and S2, including MycobacteriumGp0440934. Source identifiers are distinguished from current server availability or genome placement.",
        ["ecofab-primary", "ring-table", "ecofab-record", "apply-5"],
    )
    item = successor(
        "lbnl",
        "cm-000087-member-roster",
        "open",
        "All16 Methods stock/DSM claims remain represented; the actual Methods/TableS1 OAE515/OAE516 and Marmoricola/Bacillus correspondence remains unresolved. No stock alias, earlier-assay membership or exact genome identity is invented. This is a retained source-boundary issue, not continued absence of a roster.",
        ["lbnl-primary", "coker-supplement", "lbnl-record", "lbnl-grounding"],
    )
    item["normalization_reason"] = (
        "Unresolved source stock correspondence affects experimental identity across panels; current final16 representation is explicit, while cross-panel equivalence remains materially uncertain."
    )
    successor(
        "lbnl",
        "cm-000087-discussion-reference-coverage",
        "resolved",
        "The canonical shared SupportingReference annotation is adopted. Both the retained parent measurement and the current committed three-record measurement compare all 37 LBNL snippet surfaces: 35 match and two supplemental cells mismatch. The narrow unannotated-surface defect resolves; native validation still fails under issue 1996. This finding makes no whole-corpus coverage claim.",
        ["lbnl-coverage", "current-three-coverage", "lbnl-record", "check-lbnl-references"],
    )
    successor(
        "linked",
        "cm-000087-supplement-reference-routing",
        "open",
        "The exact TableS1 OAE516/OAE603 cells remain separately sourced and absent from the main-article cache. Current native check still fails at discussions[4].evidence[2/4]. Preserve correct quotations and primary source boundaries; issue1996 remains open.",
        ["coker-supplement", "lbnl-coverage", "current-three-coverage", "check-lbnl-references"],
    )
    for key, completeness in (("ecofab", 45), ("dopamine", 30), ("lbnl", 15)):
        nodes = docs[key].get("ecological_interactions", [])
        count = len(nodes)
        evidence_count = sum(len(node.get("evidence", [])) for node in nodes)
        issue_counts = {
            level: sum(
                item["status"] == "open"
                and IDS[key] in item["target_ids"]
                and item.get("native_severity") == level
                for item in findings
            )
            for level in ("P1", "P2", "P3")
        }
        # Native formula defaults a missing mean to zero. The zero-node ratio
        # remains undefined; zero is only the formula's coverage-bonus input.
        formula_mean = evidence_count / count if count else 0
        coverage_bonus = 20 * min(formula_mean / 2, 1)
        network_bonus = 15  # Verified current native network receipt is {}.
        quality = max(
            0,
            min(
                100,
                100
                - 50 * issue_counts["P1"]
                - 10 * issue_counts["P2"]
                - 2 * issue_counts["P3"]
                + coverage_bonus
                + network_bonus,
            ),
        )
        metrics = [
            {
                "name": "completeness",
                "value": completeness,
                "unit": "points",
                "minimum": 0,
                "maximum": 100,
                "definition": "Literal native rubric: optional-role required block0; environment5; three factors10 if present; three nodes10 if present; external resources5 if present; media10; datasets5 if present; node metabolites5 if present. No fields invented for score.",
            },
            {
                "name": "graph_nodes",
                "value": count,
                "unit": "nodes",
                "definition": "Exact current ecological_interactions list length; all nodes assessed.",
            },
        ]
        if count:
            metrics.extend(
                [
                    {
                        "name": "evidence_per_interaction",
                        "value": evidence_count / count,
                        "unit": "items per node",
                        "denominator": count,
                        "definition": f"{evidence_count} attached evidence items divided by{count}nodes; quantity does not prove quality.",
                    },
                ]
            )
        else:
            metrics.append(
                {
                    "name": "evidence_coverage_bonus",
                    "value": 0,
                    "unit": "points",
                    "definition": "The evidence-per-interaction ratio is undefined for zero nodes. The native quality formula defaults missing average evidence to zero, giving zero coverage bonus; no ratio is fabricated (#2825).",
                }
            )
        metrics.extend(
            {
                "name": "open_" + level,
                "value": value,
                "unit": "findings",
                "definition": "Actual open native-severity findings affecting this target; resolved predecessors are excluded.",
            }
            for level, value in issue_counts.items()
        )
        metrics.append(
            {
                "name": "validation_quality",
                "value": quality,
                "unit": "points",
                "minimum": 0,
                "maximum": 100,
                "definition": (
                    "Native clamp[100−50P1−10P2−2P3+20min(meanEvidence/2,1)+15networkComplete]. "
                    f"P1={issue_counts['P1']}, P2={issue_counts['P2']}, P3={issue_counts['P3']}; "
                    f"coverage bonus={coverage_bonus}, verified complete-network bonus={network_bonus}. "
                    "The capped score does not override source findings, failed checks or release status."
                ),
            }
        )
        assess(
            key + "-metrics",
            key,
            "completeness",
            "Separate native completeness and validation-quality rubrics",
            "Metrics describe the literal current rubric and denominators. Scientific outcomes and failed source-routing checks remain explicit and cannot be overridden by scores.",
            [key + "-record"],
        )["metrics"] = metrics
    review = {
        "schema_version": "1.0.0",
        "review_id": stamp + "-phase2-three-record-final-science",
        "kind": "batch",
        "repository": REPOSITORY,
        "title": "Full current EcoFAB, dopamine and Methods-defined LBNL scientific reassessment",
        "started_at": "2026-11-15T02:25:59Z",
        "finished_at": finished,
        "reviewer": {
            "identity": "codex-community-m5",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored scientific corrections after direct primary/ontology inspection; parent independently reviewed sources, candidate diffs and mutation guards before apply, and reviews final bundle separately.",
        },
        "skill": "curate-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Full current scientific assessment covers 49 stock assertions, 10 nodes, four arrows, four EcoFAB treatment arms and relative-read observations, and 17 exact genome pairs. EcoFAB causal, study-stage and genome findings and narrow LBNL annotation coverage resolve. LBNL source roster correspondence and two supplement-routing failures remain open. All 27 native focused gates executed: 26 passed and one failed. Actual snippet comparison coverage is measured separately; this is not a full-corpus or merge claim.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Every populated scientific field in current records 000025, 000516 and 000087: stocks, host, environment, cultivation, interactions, arrows, evidence, relations, resources, discussions and provenance. Full coverage applies only to these three records.",
            "selection": "Explicit Phase 2 cohort, following the accepted 000087 canary and linked correction; no all-record campaign sample inference.",
            "coverage": "full",
            "population_size": 3,
            "reviewed_target_ids": list(IDS.values()),
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": [
            {
                "action_id": "retain-source-boundaries",
                "description": "Resolve primary stock correspondence only with evidence, and route separately retained supplement text through the maintained source-aware validator.",
                "finding_ids": [
                    "cm-000087-member-roster",
                    "cm-000087-supplement-reference-routing",
                ],
                "target_ids": [IDS["lbnl"]],
                "owner_paths": [
                    {"repository": REPOSITORY, "path": TARGETS["lbnl"], "role": "canonical_record"}
                ],
                "acceptance_checks": [
                    "Independently establish Methods/TableS1 stock correspondence without aliases inferred from similar names.",
                    "Validate exact supplemental cells against their original artifact while keeping article caches separate; retain failed predecessor logs and measure actual assertion traversal.",
                ],
            }
        ],
        "limitations": [
            "Scientific review completion means every current record claim was assessed and every required focused check ran. It does not mean all checks passed: the 000087 reference check remains exit 1 with two Table S1 mismatches.",
            "Collection and genome IDs are primary-source assertions; no current catalog/server availability, genome sequence quality or independent study-stock GTDB genome placement is certified.",
            "MainMethods/TableS1 and DingData1 stock spelling conflicts remain explicit; correct source quotes are not rewritten to make article-only matching pass.",
            "The retained parent f52 measurement and new three-record measurement each retain their actual revision. Native gates ran on 17616 with the exact corrected working inputs; source inspection and current occurrence measurement use the subsequent committed source. None is relabeled as an execution on another revision.",
            "No raw statistical reanalysis, unrequested experiments, paid provider calls or wider-corpus scientific approval occurs. Taxonomic ambiguity, source limitations and unknown molecular mechanisms are preserved.",
            "Earlier structured reviews and history remain immutable. All six actual applied receipts and all native sidecars are current source inputs; prior failed/planned runs remain retained and do not enter the applied chain.",
            "Wider combined QC, generated-document integration and publication/merge status are independently reported by the integration owner; this scientific bundle is not a substitute.",
        ],
        "related_reviews": [
            {
                "repository": REPOSITORY,
                "review_id": ident,
                "relationship": "Preserves immutable earlier source assessment; explicit stable finding successors only",
            }
            for ident in PRIOR_IDS.values()
        ],
        "links": [
            f"https://github.com/{REPOSITORY}/issues/{number}"
            for number in (
                1427,
                2675,
                1548,
                476,
                1996,
                2674,
                2774,
                2806,
                2816,
                2818,
                2821,
                2823,
                2825,
            )
        ],
    }
    (output / "review.yaml").write_text(
        yaml.dump(
            review, Dumper=proof.NoAliasDumper, sort_keys=False, allow_unicode=True, width=105
        )
    )
    print(
        json.dumps(
            {
                "review_id": review["review_id"],
                "assessments": len(assessments),
                "checks": len(checks),
                "open_findings": sum(item["status"] == "open" for item in findings),
                "resolved_findings": sum(item["status"] == "resolved" for item in findings),
                "output": relative(output / "review.yaml"),
            }
        )
    )


if __name__ == "__main__":
    main()
