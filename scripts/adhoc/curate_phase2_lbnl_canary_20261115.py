"""Stage/apply the source-scoped 000087 Phase2 canary, 2026-11-15.

Inputs: exact reviewed baseline, retained primary XML/S1 and genus-grounding
receipts. Outputs: exclusive staged candidate and proof; --apply replaces only
000087 after native closed-schema validation and original-byte recheck.
Serves #1548/#2776; earlier assay observations survive as discussions. No cache,
provider, old review, or old history edits. Native sidecar scaffold is separate.
"""

import argparse
import copy
import hashlib
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import yaml
from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from communitymech.curate.curation_event import (  # noqa: E402
    append_curation_event_text,
    record_curation_event,
)
from communitymech.validation.write_validated import write_validated_community  # noqa: E402

STATE = ROOT / ".temp/phase2-science-20261115"
TARGET = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"
BEFORE = "58bb996c6056821c2e5bf3d3494108826b3f836c79fc95f0c07db967e65b04e4"
INPUTS = {
    "lbnl-retained/ecofab-relations/PMC9765266.xml": "ad9774e85b789eaa1718f1f06984f59845f20e3108993418c0444f715e869922",
    "lbnl-source-roster.json": "93be03884f9fdcbb2bc7a109da6fcc9b80ce93096190def8126d6a6cb97749e3",
    "lbnl-supplements/msystems.00951-22-s0006.docx": "5bfa02fdb94538e9405fb0ec7d7b0dad338791a5ca0b4b651589f33148c8e0e7",
    "lbnl-grounding-final16.json": "a5c8dec571bba0c42a52125a71ea2b6b97ea991137ceff8bde2874abc17d489a",
    "lbnl-retained/ecofab-independent/ring-main-plos.xml": "8ab7d3de83f7b92e7dc6443db61d9ed31471d7ccdbdd1c8cf6c3d3b2efc6e947",
}
SUMMARY = "Scoped the record to the Methods-defined final 16-stock collection, restored its 16 source DSM/strain claims with genus-level NCBI grounding and explicit GTDB ambiguity, and separated laboratory growth from source soil. Preserved the three measured earlier 18/17-assay observations as individually evidenced discussions instead of final 16 graph assertions; separated isolate, community, host and preservation protocols. Main Methods/Table S1 conflicts (OAE515/OAE516 and Marmoricola/Bacillus) remain explicit under #1548; no alias, genome identity or ecological role inferred. Addresses the 000087 portion of #1548 and physical-versus-modeled environment #2776; does not close the multi-record issue."


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def norm(text):
    return " ".join(unicodedata.normalize("NFKC", text).split())


class CanonicalLoader(yaml.SafeLoader):
    """Allow the legacy record's aliases but reject duplicate mapping keys."""

    def construct_mapping(self, node, deep=False):
        keys = [self.construct_object(key, deep=deep) for key, _ in node.value]
        if len(keys) != len(set(keys)):
            raise ValueError("duplicate canonical YAML key")
        return super().construct_mapping(node, deep=deep)


def load_document(raw):
    return yaml.load(raw, Loader=CanonicalLoader)  # noqa: S506 -- subclass of SafeLoader


def evidence(quote, explanation, reference="PMID:36472419", source="IN_VITRO"):
    return {
        "reference": reference,
        "supports": "SUPPORT",
        "evidence_source": source,
        "snippet": quote,
        "explanation": explanation,
    }


def replace_section(text, key, value):
    pattern = rf"(?ms)^{re.escape(key)}:.*?(?=^[A-Za-z_][A-Za-z_0-9]*:|\Z)"
    replacement = yaml.safe_dump({key: value}, sort_keys=False, allow_unicode=True, width=108)
    result, count = re.subn(pattern, lambda _: replacement, text)
    if count != 1:
        raise ValueError(f"expected one original section: {key}")
    return result


def build(original, grounding, source_text):
    before = load_document(original)
    after = copy.deepcopy(before)
    after["description"] = (
        "Methods-defined final 16-stock synthetic collection from soil and rhizosphere surrounding a single switchgrass plant. "
        "This record follows the deposited-stock roster in Coker et al. Methods; the study's earlier 18/17-member nutrient, ratio and EcoFAB assays have different or incompletely reconciled membership and are retained as source-scoped discussions. "
        "Table S1 differs from the final Methods roster; those stock identities are not silently reconciled."
    )
    roster_quote = (
        "The final 16-member community isolates and details on their isolation are available"
    )
    after["engineering_design"] = {
        "objective": "Provide a reproducible synthetic model of soil and rhizosphere communities for laboratory microbiome research.",
        "assembly_strategy": "Bottom-up collection of the 16 deposited stocks listed in Methods/Isolate selection. Species identities are not resolved by this source; source genus and exact stock/deposit designations are preserved.",
        "perturbation_design": "The paper develops this model through distinct nutrient, starting-ratio, dropout, cryopreservation and plant-colonization assays. Earlier 18/17-member assay results are not asserted as effects in this Methods-defined final 16 roster.",
        "evidence": [
            evidence(
                roster_quote,
                "Defines which 16 deposited stocks this record represents; does not unify the paper's different experimental panels.",
            )
        ],
    }
    after["environment_term"] = {
        "preferred_term": "laboratory environment",
        "term": {"id": "ENVO:01001405", "label": "laboratory environment"},
        "notes": "Physical setting of the liquid-medium cultivation and fabricated plant assays. Soil/rhizosphere denotes the origin and modeled context, not soil as the assay substrate.",
    }
    after["modeled_environment"] = [
        {
            "preferred_term": "soil",
            "term": {"id": "ENVO:00001998", "label": "soil"},
            "notes": "The isolates originate from rhizosphere and soil surrounding one switchgrass plant; this is the ecological context modeled in laboratory cultures.",
        }
    ]
    taxonomy = []
    mapping_hash = grounding["mapping"]["sha256"]
    for row in grounding["rows"]:
        descriptor = {
            "preferred_term": f"{row['source_genus']} {row['strain']} (source name)",
            "term": row["verified_genus_term"],
            "notes": "Genus-level NCBI grounding; the primary paper identifies novel strains of unknown species. This term is not an independently verified genome identity for the stock.",
        }
        mapping = row["native_genus_grounding"]
        if mapping is None:
            descriptor["gtdb_grounding_status"] = "UNRESOLVED"
            descriptor[
                "notes"
            ] += " Current Allobosea label corresponds to the NCBI synonym Bosea Das et al. 1996; the native crosswalk does not resolve this renamed genus."
        elif mapping.get("ambiguous"):
            descriptor["gtdb_grounding_status"] = "AMBIGUOUS"
            descriptor["gtdb_candidates"] = mapping["gtdb_options"]
        else:
            descriptor["gtdb_grounding_status"] = "GROUNDED"
            descriptor["gtdb_classification"] = {
                key: value for key, value in mapping.items() if key not in {"via", "n_alt"}
            }
            descriptor["gtdb_classification"][
                "mapping_source"
            ] = f"kg-microbe NCBI2GTDB.tsv.gz sha256:{mapping_hash}; native genus-rank mapping; aggregate denominator, named species only"
            descriptor["gtdb_classification"][
                "curation_note"
            ] = "Aggregate genus correspondence, not a sequenced-study-stock placement. Minority mappings and species identity remain uncertain."
        item = {
            "taxon_term": descriptor,
            "strain_designation": {
                "strain_name": row["strain"],
                "culture_collections": [
                    {
                        "collection": "DSM",
                        "accession": row["deposit"].split()[1],
                        "notes": "Individual-stock deposit reported in Coker Methods; current collection catalog not independently inspected.",
                    }
                ],
                "isolation_source": "Rhizosphere and soil surrounding a single switchgrass plant, as reported for the source collection.",
                "notes": "Methods-defined final 16 roster; do not equate this stock with a differently named supplementary-table stock without evidence.",
            },
            "evidence": [
                evidence(
                    row["source_quote"],
                    "Exact source genus, strain designation and DSM accession in the final Methods roster.",
                )
            ],
        }
        if row["strain"] == "OAS925":
            descriptor[
                "notes"
            ] += " Ring-trial Methods explicitly identifies Paraburkholderia sp. OAS925 as formerly Burkholderia sp. OAS925."
            item["evidence"].append(
                evidence(
                    "formerly known as Burkholderia sp. OAS925",
                    "Independent later primary Methods supplies the same-stock genus rename; no other ring-trial phenotype is transferred.",
                    reference="PMID:40920748",
                )
            )
        if row["strain"] in {"OAE513", "OAE515"}:
            item["strain_designation"][
                "notes"
            ] += " Table S1 omits Marmoricola OAE513 and names Methylobacterium OAE516 rather than OAE515; the discrepancy remains open."
        taxonomy.append(item)
    if (
        len(taxonomy) != 16
        or len({row["strain_designation"]["strain_name"] for row in taxonomy}) != 16
    ):
        raise ValueError("final16 roster invariant failed")
    after["taxonomy"] = taxonomy
    nodes = after.pop("ecological_interactions")
    if len(nodes) != 3 or any(node.get("downstream") for node in nodes):
        raise ValueError("unexpected predecessor graph")
    after["environmental_factors"] = [
        {
            "name": "represented collection",
            "value": "Methods-defined final 16 deposited stocks",
            "description": "Canonical membership follows Methods, not a merged list of every isolate used in earlier assay panels. Assay outcomes and disputed stock correspondence are documented separately.",
            "evidence": [
                evidence(
                    roster_quote,
                    "Binds this record's collection scope to the final Methods roster.",
                )
            ],
        }
    ]
    after["growth_media"] = [
        {
            "name": "R2A (Teknova R0005, 1x; isolate precultures)",
            "temperature": "30",
            "temperature_unit": "°C",
            "atmosphere": "AEROBIC",
            "vessel_type": "14 mL culture tube",
            "preparation_notes": "Methods/Isolate growth: 3–5 mL liquid 1x R2A, no shaking, 5–7 days before dilution for community generation. Individual growth curves instead started at OD600 0.05 in 200 μL 0.1x R2A in 96-well plates. The plant 24°C regime is not a member growth temperature.",
            "evidence": [
                evidence(
                    "Individual isolates were grown in 3 to 5 mL liquid cultures of 1× R2A medium (Teknova, cat number R0005) in 14 mL culture tubes in aerobic conditions at 30°C without shaking.",
                    "Source isolate preculture conditions, separate from community and plant assays.",
                ),
                evidence(
                    "The isolates were allowed to grow for 5 to 7 days before dilution for community generation.",
                    "Isolate preculture duration; no universal 72 h duration is assigned.",
                ),
            ],
        },
        {
            "name": "R2A (community cultures; assay-specific dilution)",
            "temperature": "30",
            "temperature_unit": "°C",
            "atmosphere": "AEROBIC",
            "vessel_type": "96-well plate",
            "preparation_notes": "Methods/Community growth: 200 μL liquid R2A, no shaking. Dilution and harvest time vary by panel: the earlier 18-member nutrient assay compares 1x/0.2x/0.1x R2A after 3 days; ratio panels use 2/6 day harvests. These conditions are not one final 16 treatment arm. Cryopreservation uses separate 20% glycerol/DMSO or lyophilized stocks and assay-specific regrowth media; 24°C and MS apply to the host experiment.",
            "evidence": [
                evidence(
                    "Communities were grown in 200 μL of liquid R2A medium in 96-well plates in aerobic conditions at 30°C without shaking.",
                    "General community cultivation platform; does not supply a common duration or roster for every experiment.",
                )
            ],
        },
    ]
    old = after["discussions"][0]
    old["attaches_to"] = ["taxonomy#Methods-defined-final16"]
    old["rationale"] = (
        "Automated assembly and preservation are methodological results, not ecological causal arrows. "
        "Earlier nutrient, ratio and plant observations survive in the three discussions below; their 18/17-member panels cannot be mapped to this final 16 collection by deleting a domain placeholder. "
        "The final Methods list and Table S1 disagree, so stock correspondence across panels remains uncertain. "
        "Taxon dropout results and proposed Lysobacter facilitation/fast-grower competition are separate observations or interpretations, not newly inferred partner-specific arrows. "
        "Relative sequencing, PMA and DNA spike-ins do not establish absolute viable counts for every stock. "
        "Main text, original figures 2/3/5 and separate Table S1 were inspected in this follow-up; previous immutable reviews remain preserved."
    )
    old["evidence"] = [
        evidence(
            "These isolates are novel strains from unknown species",
            "Species identities and panel-specific mechanism remain unresolved.",
        )
    ]
    discussions = [old]
    names = [
        "earlier18_nutrient_response",
        "earlier17_18_ratio_response",
        "earlier17_18_ecofab_colonization",
    ]
    for local_id, node in zip(names, nodes, strict=True):
        discussions.append(
            {
                "discussion_id": local_id,
                "prompt": node["name"] + ": source-scoped observation in earlier assay panels.",
                "kind": "INTERPRETATION",
                "status": "OPEN",
                "attaches_to": ["engineering_design#study-development"],
                "rationale": node["description"]
                + " Main Methods/Table S1 stock discrepancies prevent assigning this observation to the complete Methods-defined final 16 roster. The observation is retained; its graph interpretation for all final 16 members is withheld.",
                "evidence": node["evidence"],
                "posed_by": "codex",
                "posed_date": "2026-11-15",
            }
        )
    discussions.append(
        {
            "discussion_id": "methods_final16_vs_supplement_table_s1",
            "prompt": "How do the Methods-defined final 16 stocks map to the earlier 18-stock Table S1 roster?",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "attaches_to": ["taxonomy#Methods-defined-final16"],
            "rationale": "Main Methods includes Marmoricola OAE513 and Methylobacterium OAE515, while separate Table S1 includes Bacillus OAE603 and Methylobacterium OAE516, omits Marmoricola, and also includes Sphingomonas OAE905 and Pseudomonas simiae WCS417. No supplied evidence proves OAE515 and OAE516 are aliases or makes earlier 18/17 panels equal to final 16 plus exclusions. Table S1's plant associations are genus-level literature context, not stock-specific ecological role measurements. Issue 1548 retains the unresolved panel correspondence.",
            "evidence": [
                evidence("DSM 114042 (Marmoricola OAE513)", "Present in the final Methods roster."),
                evidence(
                    "DSM 113602 (Methylobacterium OAE515)", "Exact final Methods stock designation."
                ),
                evidence(
                    "OAE516",
                    "Separate Table S1, table 1, row 12, Strain column: the adjacent Genus cell is Methylobacterium. This differs from Methods OAE515; no alias is inferred. The original DOCX and exact table extraction are retained separately from the article cache.",
                    source="supplement_table_S1",
                ),
                evidence(
                    "Bacillus",
                    "Separate Table S1, table 1, row 18, Genus column; the adjacent Strain cell is OAE603. The complete table contains no Marmoricola row, unlike the final Methods roster.",
                    source="supplement_table_S1",
                ),
                evidence(
                    "OAE603",
                    "Separate Table S1, table 1, row 18, Strain column; paired with Bacillus in the adjacent Genus cell. This is not one of the final Methods-defined 16 stocks.",
                    source="supplement_table_S1",
                ),
            ],
            "posed_by": "codex",
            "posed_date": "2026-11-15",
        }
    )
    after["discussions"] = discussions
    for item in taxonomy:
        for ev in item["evidence"]:
            if norm(ev["snippet"]) not in norm(source_text[ev["reference"]]):
                raise ValueError("new stock quotation absent from primary text")
    if after["curation_history"] != before["curation_history"]:
        raise ValueError("old history changed")
    return before, after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, required=True, help="new directory under repository .temp"
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT / ".temp") or output.exists():
        raise ValueError("output must be a new repository .temp directory")
    canonical = ROOT / TARGET
    original = canonical.read_bytes()
    if digest(original) != BEFORE:
        raise ValueError("record changed since scientific assessment")
    for relative, sha in INPUTS.items():
        if digest((STATE / relative).read_bytes()) != sha:
            raise ValueError(f"assessed source changed: {relative}")
    grounding_raw = (STATE / "lbnl-grounding-final16.json").read_bytes()
    grounding = json.loads(grounding_raw)
    if grounding["roster_sha256"] != INPUTS["lbnl-source-roster.json"]:
        raise ValueError("grounding does not bind the assessed roster")
    sources = {
        "PMID:36472419": STATE / "lbnl-retained/ecofab-relations/PMC9765266.xml",
        "PMID:40920748": STATE / "lbnl-retained/ecofab-independent/ring-main-plos.xml",
    }
    source_text = {
        key: "".join(ElementTree.fromstring(path.read_bytes()).itertext())
        for key, path in sources.items()
    }
    before, candidate = build(original, grounding, source_text)
    text = original.decode()
    for key in (
        "description",
        "engineering_design",
        "environment_term",
        "taxonomy",
        "environmental_factors",
        "growth_media",
        "discussions",
    ):
        text = replace_section(text, key, candidate[key])
    text = re.sub(
        r"(?ms)^ecological_interactions:.*?(?=^environmental_factors:)", "", text, count=1
    )
    environment = yaml.safe_dump(
        {"modeled_environment": candidate["modeled_environment"]},
        sort_keys=False,
        allow_unicode=True,
        width=108,
    )
    text = text.replace("related_communities:\n", environment + "related_communities:\n", 1)
    if load_document(text) != candidate:
        raise ValueError("bounded section replacement changed semantics")
    event = record_curation_event(
        candidate, curator="codex", action="EDIT", changes=SUMMARY, llm_assisted=True
    )
    text = append_curation_event_text(
        text,
        curator="codex",
        action="EDIT",
        changes=SUMMARY,
        timestamp=event["timestamp"],
        width=108,
    )
    unmarked = {key: value for key, value in event.items() if key != "llm_assisted"}
    old_event = yaml.safe_dump([unmarked], sort_keys=False, allow_unicode=True, width=108).rstrip()
    if text.count(old_event) != 1:
        raise ValueError("native append event anchor changed")
    text = text.replace(
        old_event,
        yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=108).rstrip(),
        1,
    )
    if load_document(text) != candidate:
        raise ValueError("native history append changed semantics")
    output.mkdir()
    staged = output / "validated.yaml"
    write_validated_community(candidate, staged)
    if load_document(staged.read_bytes()) != candidate:
        raise ValueError("native validated form differs")
    (output / "candidate.yaml").write_text(text)
    (output / "before.yaml").write_bytes(original)
    proof = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "target": TARGET,
        "before_sha256": BEFORE,
        "after_sha256": digest(text.encode()),
        "applied": args.apply,
        "source_inputs": INPUTS,
        "grounding_sha256": digest(grounding_raw),
        "additional_primary_inputs": {
            str(path.relative_to(ROOT)): digest(path.read_bytes()) for path in sources.values()
        },
        "helper_sha256": digest(Path(__file__).read_bytes()),
        "event": event,
        "scope": "Methods-defined final16; no inferred roles, genomes, ambiguous stock aliases or earlier-panel arm membership",
    }
    if args.apply:
        if canonical.read_bytes() != original:
            raise ValueError("concurrent canonical change")
        (output / "replacement.yaml").write_text(text)
        (output / "replacement.yaml").replace(canonical)
        if (
            canonical.read_bytes() != text.encode()
            or load_document(canonical.read_bytes()) != candidate
        ):
            raise ValueError("persisted candidate mismatch")
    (output / "receipt.json").write_text(json.dumps(proof, indent=2) + "\n")
    print(json.dumps(proof, indent=2))


if __name__ == "__main__":
    main()
