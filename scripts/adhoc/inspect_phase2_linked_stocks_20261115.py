"""Read-only source/grounding proof for #2674/#2774/#2806, 2026-11-15.

Inputs: one exact linked record, retained primary XML, readonly NCBI database,
and an explicit GTDB crosswalk. Output: exclusive repository-private JSON.
No record, cache, ontology, environment or provider writes. Run one record
as a canary before the second. Genus votes do not identify stock genomes.
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from curate_phase2_lbnl_canary_20261115 import load_document, norm
from defusedxml import ElementTree
from ground_phase2_lbnl_roster_20261115 import digest_file, query_terms

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/phase2-science-20261115"
sys.path.insert(0, str(ROOT / "scripts"))
import gtdb_ground as native  # noqa: E402

RECORDS = {
    "ecofab": "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml",
    "dopamine": "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml",
}
SOURCES = {
    "PMID:36472419": (
        "lbnl-retained/ecofab-relations/PMC9765266.xml",
        "ad9774e85b789eaa1718f1f06984f59845f20e3108993418c0444f715e869922",
    ),
    "PMID:40920748": (
        "lbnl-retained/ecofab-independent/ring-main-plos.xml",
        "8ab7d3de83f7b92e7dc6443db61d9ed31471d7ccdbdd1c8cf6c3d3b2efc6e947",
    ),
}
CORES = ("gtdb_id", "gtdb_lineage", "support_genomes", "total_genomes", "majority_fraction")


def primary_proof():
    result = {}
    for reference, (relative, expected) in SOURCES.items():
        path = STATE / relative
        if digest_file(path) != expected:
            raise ValueError(f"changed primary source: {relative}")
        tree = ElementTree.parse(path)
        paragraphs = []
        for index, element in enumerate(tree.iter("p")):
            text = norm("".join(element.itertext()))
            if not any(
                token in text
                for token in ("DSM 200000SY", "DSM 113627", "formerly known as Burkholderia")
            ):
                continue
            # The collection availability paragraph contains contact text. Keep
            # a short exact quotation, without republishing contact information.
            selected = "or as a collection (DSM 200000SY" if "DSM 200000SY" in text else text
            if selected not in text or re.search(r"[\w.+-]+@[\w.-]+", selected):
                raise ValueError("unsafe or inexact primary excerpt")
            paragraphs.append(
                {
                    "locator": f"JATS p index {index}; element id {element.get('id')}",
                    "quote": selected,
                }
            )
        if not paragraphs:
            raise ValueError(f"no requested primary evidence: {reference}")
        result[reference] = {
            "path": str(path.relative_to(ROOT)),
            "sha256": expected,
            "excerpts": paragraphs,
        }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", choices=RECORDS, required=True)
    parser.add_argument("--ncbi", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(STATE) or output.exists():
        parser.error("output must be a new exclusive file beneath the private state directory")
    path = ROOT / RECORDS[args.record]
    before_hash = digest_file(path)
    record = load_document(path.read_text())
    identifiers = {row["taxon_term"]["term"]["id"] for row in record["taxonomy"]}
    identifiers.discard("NCBITaxon:1667")
    identifiers.add("NCBITaxon:1663")
    ncbi = query_terms(args.ncbi, sorted(identifiers))
    labels = {
        identifier: next(row["value"] for row in rows if row["predicate"] == "rdfs:label")
        for identifier, rows in ncbi["rows"].items()
    }
    for identifier, rows in ncbi["rows"].items():
        if not any(row["object"] == "NCBITaxon:genus" for row in rows):
            raise ValueError(f"expected genus rank: {identifier}")
    if not any(row["value"] == "Bosea Das et al. 1996" for row in ncbi["rows"]["NCBITaxon:85413"]):
        raise ValueError("legacy bacterial Bosea synonym is not verified")
    crosswalk_hash = digest_file(args.mapping)
    if crosswalk_hash != "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd":
        raise ValueError("unreviewed crosswalk")
    higher = {key for label in [*labels.values(), "Bosea"] for key in native.lookup_keys(label)}
    indexed = native.collect_rows(args.mapping, set(), set(), higher)
    rows = []
    for index, item in enumerate(record["taxonomy"]):
        term = item["taxon_term"]
        identifier = term["term"]["id"]
        if item["strain_designation"]["strain_name"] == "OAP107":
            identifier = "NCBITaxon:1663"
        label = labels[identifier]
        grounding = native.resolve_target(
            identifier.split(":")[1], label, *indexed, denominator="aggregate", exclude_unnamed=True
        )
        legacy = None
        if identifier == "NCBITaxon:85413":
            legacy = native.resolve_target(
                "85413", "Bosea", *indexed, denominator="aggregate", exclude_unnamed=True
            )
        stored = term.get("gtdb_classification")
        comparison = legacy or grounding
        rows.append(
            {
                "selector": f"taxonomy[{index}]",
                "strain": item["strain_designation"]["strain_name"],
                "stored_term": term["term"],
                "verified_genus_term": {"id": identifier, "label": label},
                "stored_grounding": stored,
                "native_current_label_grounding": grounding,
                "explicit_legacy_bacterial_Bosea_grounding": legacy,
                "stored_numeric_core_reproduced": bool(
                    stored
                    and comparison
                    and all(stored.get(key) == comparison.get(key) for key in CORES)
                ),
                "stored_candidates_reproduced": bool(
                    grounding
                    and grounding.get("ambiguous")
                    and term.get("gtdb_candidates") == grounding.get("gtdb_options")
                ),
            }
        )
    if digest_file(path) != before_hash:
        raise ValueError("record changed during inspection")
    result = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "git_revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "record": {"path": RECORDS[args.record], "id": record["id"], "sha256": before_hash},
        "helper_sha256": digest_file(Path(__file__)),
        "ncbi": ncbi,
        "crosswalk": {"filename": args.mapping.name, "sha256": crosswalk_hash},
        "native_mapper_sha256": digest_file(ROOT / "scripts/gtdb_ground.py"),
        "method": "Native aggregate genus mapping, unnamed species excluded. Explicit legacy bacterial Bosea lookup only after NCBI synonym verification; preserves curated current Allobosea identity.",
        "primary_sources": primary_proof(),
        "rows": rows,
        "limitations": [
            "No GTDB release/build date certified.",
            "Genus correspondences do not assign an exact stock genome.",
            "DSM accession is a primary-source statement; current DSMZ individual catalog not inspected.",
            "No ecological or causal conclusion follows from mapping votes.",
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "path": str(output.relative_to(ROOT)),
                "sha256": digest_file(output),
                "members": len(rows),
                "reproduced_numeric_cores": sum(
                    row["stored_numeric_core_reproduced"] for row in rows
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
