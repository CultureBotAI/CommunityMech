"""Stage guarded linked-stock corrections for #2674/#2774/#2806, 2026-11-15.

Inputs: exact three-record cohort and inspected primary/grounding receipts.
Output: exclusive private candidates, native validated copies, diffs and hashes.
Planning changes no canonical input. Applying one explicitly named target reuses
the reviewed candidate, revalidates it, binds every cohort input and source, and
atomically replaces that one record. Native append-only sidecars are separate.
"""

import argparse
import copy
import difflib
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from curate_phase2_lbnl_canary_20261115 import evidence, load_document, replace_section

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from communitymech.curate.curation_event import (  # noqa: E402
    append_curation_event_text,
    record_curation_event,
)
from communitymech.validation.write_validated import write_validated_community  # noqa: E402

STATE = ROOT / ".temp/phase2-science-20261115"
TARGETS = {
    "ecofab": (
        "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml",
        "77625f064af7946f875460cb321e450b6bfcd667d0ad9ec1ebabb502a6865348",
        "CommunityMech:000025",
    ),
    "dopamine": (
        "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml",
        "41aa3b07822847b7cb0670874225419e23a672c2b27f76417c35d8792bb87a5e",
        "CommunityMech:000516",
    ),
    "lbnl": (
        "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml",
        "aa146b5e21d2480725ed8a017372fd1dd9dc8b1e89778e7ca1f83477566845c4",
        "CommunityMech:000087",
    ),
}
INPUTS = {
    "linked-ecofab-grounding-001.json": "ad27b65c8e6304d86638115d31b30c61f5f937bfaa91f4873dec8b5150170ac8",
    "linked-dopamine-grounding-001.json": "867bbaff2936ac73bc2d9824eeffcba7f9bbdab3c8d2969eb07553d1983cd05e",
    "lbnl-retained/ecofab-relations/PMC9765266.xml": "ad9774e85b789eaa1718f1f06984f59845f20e3108993418c0444f715e869922",
    "lbnl-retained/ecofab-independent/ring-main-plos.xml": "8ab7d3de83f7b92e7dc6443db61d9ed31471d7ccdbdd1c8cf6c3d3b2efc6e947",
    "lbnl-retained/ecofab-relations/PMC13522444.xml": "9a58e566488461f6bda24554f2ab3c580e53fff58f5413b74e0957220acbe274",
}
MAPPING_HASH = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
MAPPING_NOTE = f"kg-microbe NCBI2GTDB.tsv.gz sha256:{MAPPING_HASH}; native genus-rank mapping; aggregate denominator, named species only; no release/build date certified"
COLLECTION_NOTE = "Ring-trial Methods distinguishes individual source stocks from the complete SynCom17 consortium deposit DSM 200000SY. DSM 113627 is the individual OAS925 accession reported in Coker Methods; this source-reported stock identity is not an independent current DSMZ catalog verification."
SUMMARIES = {
    "ecofab": "Corrected OAP107 to the source-supported Arthrobacter genus and retained its 11-way GTDB ambiguity; updated all graph participant identifiers consistently. Replaced unsupported GTDB build-date prose with the inspected crosswalk SHA/method while preserving every numerical mapping core, the curated bacterial Bosea mapping and Paenibacillus ambiguity. Distinguished OAS925 individual DSM113627 from the complete SynCom17 DSM200000SY collection, and recomputed paired membership against the Methods-defined final16. Addresses #2674/#2806; non-graph causal/study-stage claims #1427 and exact genome accessions #2675 remain unresolved.",
    "dopamine": "Corrected OAP107 genus/participant grounding, retained 11-way GTDB ambiguity, replaced unsupported mapping date prose with inspected crosswalk SHA/method while preserving all numerical cores and curated Bosea mapping, and distinguished individual OAS925 DSM113627 from the ring-trial consortium deposit. Recomputed reciprocal membership against the Methods-defined final16 without transferring earlier assay results. Addresses #2774/#2806; no dopamine causal annotations or source caches changed.",
    "lbnl": "After source-supported neighbor stock metadata corrections, changed both reciprocal membership bases to SHARED_STRAIN_DESIGNATIONS and explicitly retained Methods-defined final16 scope. No taxonomy, earlier-assay discussions, cultivation conditions or graph assertions changed. Resolves only linked-stock metadata under #2806; Main Methods/Table S1 correspondence #1548 remains unresolved.",
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def verify_inputs():
    for name, expected in INPUTS.items():
        if digest((STATE / name).read_bytes()) != expected:
            raise ValueError(f"source input changed: {name}")


def semantic_changes(before, after, path=""):
    if isinstance(before, dict) and isinstance(after, dict):
        changes = []
        for key in sorted(before.keys() | after.keys()):
            child = f"{path}.{key}" if path else key
            if key not in before or key not in after:
                changes.append(child)
            else:
                changes.extend(semantic_changes(before[key], after[key], child))
        return changes
    if isinstance(before, list) and isinstance(after, list) and len(before) == len(after):
        return [
            change
            for index, (a, b) in enumerate(zip(before, after, strict=True))
            for change in semantic_changes(a, b, f"{path}[{index}]")
        ]
    return [] if before == after else [path]


def replace_taxon(text, index, row):
    match = re.search(r"(?ms)^taxonomy:\n(.*?)(?=^[A-Za-z_][A-Za-z_0-9]*:|\Z)", text)
    if not match:
        raise ValueError("missing unique taxonomy block")
    body = match[1]
    items = re.split(r"(?m)(?=^- taxon_term:)", body)
    if items[0] or index + 1 >= len(items):
        raise ValueError("unexpected taxonomy layout")
    items[index + 1] = yaml.safe_dump([row], sort_keys=False, allow_unicode=True, width=108)
    return text[: match.start(1)] + "".join(items) + text[match.end(1) :]


def append_history(text, candidate, key, timestamp=None):
    event = record_curation_event(
        candidate,
        curator="codex",
        action="EDIT",
        changes=SUMMARIES[key],
        llm_assisted=True,
        **({"timestamp": timestamp} if timestamp is not None else {}),
    )
    text = append_curation_event_text(
        text,
        curator="codex",
        action="EDIT",
        changes=SUMMARIES[key],
        timestamp=event["timestamp"],
        width=108,
    )
    unmarked = {name: value for name, value in event.items() if name != "llm_assisted"}
    old_event = yaml.safe_dump([unmarked], sort_keys=False, allow_unicode=True, width=108).rstrip()
    if text.count(old_event) != 1:
        raise ValueError("native append event anchor changed")
    text = text.replace(
        old_event,
        yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=108).rstrip(),
        1,
    )
    return text, event


def build(key, original, proof=None, timestamp=None):
    before = load_document(original)
    if before["id"] != TARGETS[key][2]:
        raise ValueError("record identity mismatch")
    after = copy.deepcopy(before)
    text = original.decode()
    if key != "lbnl":
        if (
            proof["record"]["sha256"] != digest(original)
            or proof["crosswalk"]["sha256"] != MAPPING_HASH
        ):
            raise ValueError("grounding proof is not bound to this record")
        for index, item in enumerate(after["taxonomy"]):
            row = proof["rows"][index]
            term = item["taxon_term"]
            if row["strain"] != item["strain_designation"]["strain_name"]:
                raise ValueError("grounding roster order changed")
            stored = term.get("gtdb_classification")
            if stored:
                if not row["stored_numeric_core_reproduced"]:
                    raise ValueError("unreproduced numerical mapping core")
                stored["mapping_source"] = MAPPING_NOTE + (
                    "; curated legacy bacterial Bosea name, verified NCBI Allobosea synonym"
                    if row["strain"] == "OAE506"
                    else ""
                )
            elif row["strain"] == "OAP107":
                term["term"] = row["verified_genus_term"]
                if not row["native_current_label_grounding"]["ambiguous"]:
                    raise ValueError("OAP107 ambiguity changed")
                term["gtdb_grounding_status"] = "AMBIGUOUS"
                term["gtdb_candidates"] = row["native_current_label_grounding"]["gtdb_options"]
                term["notes"] = (
                    (term.get("notes", "").strip() + " " if term.get("notes") else "")
                    + "Source identifies an unknown species within Arthrobacter; NCBITaxon:1663 is genus-level grounding, not an independently verified stock genome. The inspected crosswalk has 11 genus candidates; no single GTDB lineage is selected."
                )
                item["evidence"].append(
                    evidence(
                        "DSM 113524 (Arthrobacter OAP107)",
                        "Primary Methods identifies the same stock under the Arthrobacter genus, not a named species or sequenced-genome assignment.",
                    )
                )
            elif row["strain"] != "OAE614" or not row["stored_candidates_reproduced"]:
                raise ValueError("unreviewed ungrounded member")
            if row["strain"] == "OAS925":
                item["strain_designation"]["culture_collections"] = [
                    {
                        "collection": "DSM",
                        "accession": "113627",
                        "notes": "Individual-stock deposit reported in Coker Methods; current collection catalog not independently inspected. The complete SynCom17 collection DSM 200000SY is not an individual-stock accession.",
                    }
                ]
                item["evidence"].extend(
                    [
                        evidence(
                            "DSM 113627 (Burkholderia OAS925)",
                            "Source-reported individual OAS925 stock accession; this is distinct from the complete SynCom17 collection.",
                        ),
                        evidence(
                            "formerly known as Burkholderia sp. OAS925",
                            "Ring-trial Methods explicitly supplies the same-stock Paraburkholderia rename; no phenotype is transferred.",
                            reference="PMID:40920748",
                        ),
                    ]
                )
        # Preserve presentation outside the two bounded taxonomy rows and
        # mapping provenance scalars; participant changes are exact term pairs.
        mapping_iter = iter(
            item["taxon_term"]["gtdb_classification"]["mapping_source"]
            for item in after["taxonomy"]
            if "gtdb_classification" in item["taxon_term"]
        )

        def replace_mapping(match):
            value = next(mapping_iter)
            rendered = yaml.safe_dump(
                {"mapping_source": value}, sort_keys=False, allow_unicode=True, width=102
            )
            return "".join("      " + line + "\n" for line in rendered.splitlines())

        text, count = re.subn(
            r"(?m)^      mapping_source:.*\n(?: {8,}\S.*\n)*", replace_mapping, text
        )
        if count != sum("gtdb_classification" in item["taxon_term"] for item in after["taxonomy"]):
            raise ValueError("mapping scalar replacement count changed")
        for index, item in enumerate(after["taxonomy"]):
            if item["strain_designation"]["strain_name"] in {"OAS925", "OAP107"}:
                text = replace_taxon(text, index, item)
        for node in after.get("ecological_interactions", []):
            for participant in node.get("participating_taxa", []):
                if participant.get("term", {}).get("id") == "NCBITaxon:1667":
                    participant["term"] = {"id": "NCBITaxon:1663", "label": "Arthrobacter"}
        text = text.replace(
            "id: NCBITaxon:1667\n      label: Arthrobacter sp.",
            "id: NCBITaxon:1663\n      label: Arthrobacter",
        )
        design = after["engineering_design"]
        design["notes"] = (
            design.get("notes", "").strip() + " " if design.get("notes") else ""
        ) + COLLECTION_NOTE
        design["evidence"].append(
            evidence(
                "or as a collection (DSM 200000SY",
                "Ring-trial Methods describes the consortium collection separately from individual strains; this is not an OAS925 stock accession.",
                reference="PMID:40920748",
            )
        )
        text = replace_section(text, "engineering_design", design)
    cohort_ids = {value[2] for value in TARGETS.values()}
    for relation in after["related_communities"]:
        if relation["identifier"] in cohort_ids:
            relation["basis"] = "SHARED_STRAIN_DESIGNATIONS"
            if relation["identifier"] == "CommunityMech:000087":
                relation["description"] = (
                    "SynCom17 is the Methods-defined final 16 deposited stocks in CommunityMech:000087 plus Gottfriedia (formerly Bacillus) OAE603. Earlier Coker assay rosters and Table S1 discrepancies are not equated with that final16."
                    if key == "ecofab"
                    else "Shares 15 source-designated stocks with the Methods-defined final16 in CommunityMech:000087; this roster has Bacillus (Gottfriedia) OAE603 where that final16 has Bradyrhizobium OAE829. Earlier Coker assay rosters and Table S1 discrepancies remain distinct."
                )
            elif key == "lbnl":
                relation["description"] = (
                    relation["description"]
                    + " This relation uses the Methods-defined final16, not the earlier assay rosters or unresolved Table S1 correspondence."
                )
    text = replace_section(text, "related_communities", after["related_communities"])
    if load_document(text) != after:
        raise ValueError("bounded textual mutation differs from reviewed semantic candidate")
    # Every established numerical classification remains exactly unchanged,
    # except its source-string provenance. Curated flags/notes remain intact.
    for old, new in zip(before["taxonomy"], after["taxonomy"], strict=True):
        old_map = copy.deepcopy(old["taxon_term"].get("gtdb_classification"))
        new_map = copy.deepcopy(new["taxon_term"].get("gtdb_classification"))
        if old_map:
            old_map.pop("mapping_source")
            new_map.pop("mapping_source")
        if old_map != new_map:
            raise ValueError("existing classification changed beyond provenance")
    text, event = append_history(text, after, key, timestamp=timestamp)
    if load_document(text) != after:
        raise ValueError("native history append changed candidate semantics")
    return before, after, text, event


def plan(output):
    if output.exists() or not output.is_relative_to(STATE):
        raise ValueError("plan output must be a new private directory")
    verify_inputs()
    originals = {key: (ROOT / value[0]).read_bytes() for key, value in TARGETS.items()}
    if any(digest(originals[key]) != value[1] for key, value in TARGETS.items()):
        raise ValueError("cohort differs from reviewed originals")
    output.mkdir(parents=True)
    receipt = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "helper_sha256": digest(Path(__file__).read_bytes()),
        "source_inputs": INPUTS,
        "targets": {},
        "applied": False,
    }
    for key, (relative, before_hash, identifier) in TARGETS.items():
        proof = (
            json.loads((STATE / f"linked-{key}-grounding-001.json").read_text())
            if key != "lbnl"
            else None
        )
        before, candidate, text, event = build(key, originals[key], proof)
        directory = output / key
        directory.mkdir()
        (directory / "before.yaml").write_bytes(originals[key])
        write_validated_community(candidate, directory / "native-validated.yaml")
        if load_document((directory / "native-validated.yaml").read_bytes()) != candidate:
            raise ValueError("native validated candidate differs")
        (directory / "candidate.yaml").write_text(text)
        (directory / "diff.patch").write_text(
            "".join(
                difflib.unified_diff(
                    originals[key].decode().splitlines(True),
                    text.splitlines(True),
                    fromfile=relative,
                    tofile=relative,
                )
            )
        )
        receipt["targets"][key] = {
            "path": relative,
            "id": identifier,
            "before_sha256": before_hash,
            "after_sha256": digest(text.encode()),
            "semantic_changes": semantic_changes(before, candidate),
            "event": event,
        }
    if any((ROOT / TARGETS[key][0]).read_bytes() != raw for key, raw in originals.items()):
        raise ValueError("cohort changed during planning")
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {
                "plan": str(output.relative_to(ROOT)),
                "receipt_sha256": digest((output / "receipt.json").read_bytes()),
                "canonical_changed": False,
            },
            indent=2,
        )
    )


def apply(plan_path, key):
    if not plan_path.is_relative_to(STATE):
        raise ValueError("plan must remain repository-private")
    verify_inputs()
    receipt = json.loads((plan_path / "receipt.json").read_text())
    if (
        receipt["helper_sha256"] != digest(Path(__file__).read_bytes())
        or receipt["source_inputs"] != INPUTS
    ):
        raise ValueError("reviewed plan/helper binding changed")
    if set(receipt["targets"]) != set(TARGETS):
        raise ValueError("reviewed cohort changed")
    for name, (relative, before_hash, identifier) in TARGETS.items():
        entry = receipt["targets"][name]
        if (
            entry["path"] != relative
            or entry["before_sha256"] != before_hash
            or entry["id"] != identifier
        ):
            raise ValueError("target identity binding changed")
        if digest((plan_path / name / "before.yaml").read_bytes()) != before_hash:
            raise ValueError("original snapshot changed")
        if digest((plan_path / name / "candidate.yaml").read_bytes()) != entry["after_sha256"]:
            raise ValueError("reviewed candidate changed")
        proof = (
            json.loads((STATE / f"linked-{name}-grounding-001.json").read_text())
            if name != "lbnl"
            else None
        )
        _, _, rebuilt_text, rebuilt_event = build(
            name,
            (plan_path / name / "before.yaml").read_bytes(),
            proof,
            timestamp=entry["event"]["timestamp"],
        )
        if (
            rebuilt_text.encode() != (plan_path / name / "candidate.yaml").read_bytes()
            or rebuilt_event != entry["event"]
        ):
            raise ValueError("candidate differs from bounded source-backed reconstruction")
        if digest((ROOT / relative).read_bytes()) not in {before_hash, entry["after_sha256"]}:
            raise ValueError("concurrent cohort change")
    target = ROOT / TARGETS[key][0]
    original = target.read_bytes()
    if digest(original) != TARGETS[key][1]:
        raise ValueError("target already applied or changed")
    audit = plan_path / key / "apply"
    audit.mkdir()
    text = (plan_path / key / "candidate.yaml").read_bytes()
    candidate = load_document(text)
    write_validated_community(candidate, audit / "native-validated.yaml")
    if load_document((audit / "native-validated.yaml").read_bytes()) != candidate:
        raise ValueError("native revalidation changed semantics")
    verify_inputs()
    for name, (relative, before_hash, _) in TARGETS.items():
        if digest((ROOT / relative).read_bytes()) not in {
            before_hash,
            receipt["targets"][name]["after_sha256"],
        }:
            raise ValueError("cohort changed during native revalidation")
    if target.read_bytes() != original:
        raise ValueError("canonical changed before replacement")
    (audit / "replacement.yaml").write_bytes(text)
    (audit / "replacement.yaml").replace(target)
    if target.read_bytes() != text:
        raise ValueError("persisted candidate mismatch")
    result = {
        "applied_at": datetime.now(timezone.utc).isoformat(),
        "target": TARGETS[key][0],
        "before_sha256": digest(original),
        "after_sha256": digest(text),
        "plan_receipt_sha256": digest((plan_path / "receipt.json").read_bytes()),
        "history_sidecar_required": True,
    }
    (audit / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--plan",
        type=Path,
        required=True,
        help="exclusive new plan directory, or reviewed existing plan for apply",
    )
    parser.add_argument("--apply-target", choices=TARGETS)
    args = parser.parse_args()
    if args.apply_target:
        apply(args.plan.resolve(), args.apply_target)
    else:
        plan(args.plan.resolve())


if __name__ == "__main__":
    main()
