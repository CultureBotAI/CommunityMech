"""Exact Akkermansia source partitions for #2833/#2948.

The default hierarchy checker remains source-agnostic. This explicit wrapper
admits two independently verified R232 assertions and compares them together;
all other blocks retain the existing shared comparison. No source prose or
curated flag can authorize a partition. No cross-release hierarchy is asserted.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

from communitymech.validators.gtdb_lineage_tree import _blocks, check_corpus

DEFAULT = "legacy-shared-population"
R232 = "gtdb-r232-e401d80c-akkermansia-ncbi-name"
NCBI = "NCBITaxon:239935"
GTDB = "GTDB:s__Akkermansia_muciniphila"
PROOFS = {
    "reports/akkermansia-source-adjudication-20261116/workbook-inspection-001.json": (
        "d5d7726fe35bd235df89d3bdd4480cf238e4ba5a3159a62ae4c578adfadbb296"
    ),
    "reports/akkermansia-source-adjudication-20261116/lineage-evidence-001.json": (
        "3436d0cbc2fa8fa8bd29351af4b3da517517c060fcf2a91e5c71f716ac879589"
    ),
    "reports/gtdb-code006-20261115/gut-pair-382-001-native-proof.json": (
        "ce0d0aedaecc45d61db8575c131145f9380670a1d171e0eff145f32199b89a0d"
    ),
}
AMSTERDAM = "kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml"
EXPECTED = {
    AMSTERDAM: ("CommunityMech:000382", 0),
    "kb/communities/MUC2_Human_Gut_Commensal_Defined_Consortium.yaml": ("CommunityMech:000351", 13),
    "kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml": ("CommunityMech:000392", 0),
}


class SourceProvenanceError(ValueError):
    """The exact source-bound assertion is absent, changed or misidentified."""


class AkkermansiaSources:
    """Read immutable public metadata once per check; never cache mutable records."""

    def __init__(self, root: Path):
        self.root = root
        proofs = []
        for path, expected in PROOFS.items():
            raw = (root / path).read_bytes()
            if hashlib.sha256(raw).hexdigest() != expected:
                raise SourceProvenanceError(f"source proof changed: {path}")
            proofs.append(json.loads(raw))
        workbook, lineage, native = proofs
        # The hashes authenticate complete proof bytes; retain the scientific
        # relationship explicitly rather than treating arbitrary hashes as truth.
        row = workbook["exact_ncbi_name_rows"]
        if (
            len(row) != 1
            or row[0]["row"] != 34
            or row[0]["values"][:3] != ["s__Akkermansia muciniphila", 1806, 110]
            or not row[0]["values"][3].startswith("s__Akkermansia muciniphila 73.09%,")
            or not workbook["inputs_unchanged"]
            or not lineage["inputs_unchanged"]
        ):
            raise SourceProvenanceError("unexpected verified R232 population")
        self.entries = {
            record["path"]: record["selected"][0]["entry"]
            for record in workbook["current_descriptors"]
        }
        if set(self.entries) != set(EXPECTED):
            raise SourceProvenanceError("source target set differs")
        native_result = native["occurrences"][0]["native_result"]
        for path, entry in self.entries.items():
            block = entry["taxon_term"]["gtdb_classification"]
            if path == AMSTERDAM:
                if any(
                    block.get(key) != value for key, value in native_result.items() if key != "via"
                ):
                    raise SourceProvenanceError("native population differs from current assertion")
            elif (
                block["total_genomes"] != 1806
                or block["majority_fraction"] != 0.731
                or lineage["lineage_counts"].get(block["gtdb_lineage"]) != 1372
            ):
                raise SourceProvenanceError("R232 assertion differs from independent sources")

    def validate_document(self, label: str, document: Any) -> None:
        """Bind full relative path, record identity, selector and selected stock."""
        if not isinstance(document, dict):
            if label in EXPECTED:
                raise SourceProvenanceError("source-bound document is not a mapping")
            return
        known_id = document.get("id") in {value[0] for value in EXPECTED.values()}
        if label not in EXPECTED:
            if known_id:
                raise SourceProvenanceError(
                    "source-bound record path differs or is only a basename"
                )
            return
        if str(PurePosixPath(label)) != label or ".." in PurePosixPath(label).parts:
            raise SourceProvenanceError("noncanonical source-bound record path")
        record_id, index = EXPECTED[label]
        taxonomy = document.get("taxonomy")
        if (
            document.get("id") != record_id
            or not isinstance(taxonomy, list)
            or len(taxonomy) <= index
            or taxonomy[index] != self.entries[label]
        ):
            raise SourceProvenanceError(
                f"source-bound assertion differs: {label} taxonomy[{index}]"
            )
        matches = [
            block
            for _, block in _blocks(document)
            if block.get("ncbi_source_id") == NCBI or block.get("gtdb_id") == GTDB
        ]
        if len(matches) != 1:
            raise SourceProvenanceError("source-bound assertion duplicated or absent")

    def population(self, label: str, block: dict, document: Any = None) -> str:
        if label not in EXPECTED:
            # A copied verified assertion or arbitrary manual-source assertion
            # is a reason to inspect, never a reason to grant admission.
            if (block.get("ncbi_source_id") == NCBI or block.get("gtdb_id") == GTDB) and (
                block.get("curated") or "R232" in str(block.get("mapping_source", ""))
            ):
                raise SourceProvenanceError("unknown Akkermansia source-bound path")
            return DEFAULT
        if document is None:
            document = yaml.safe_load((self.root / label).read_bytes())
        self.validate_document(label, document)
        if not any(block == actual for _, actual in _blocks(document)):
            raise SourceProvenanceError("supplied block is not the current record assertion")
        selected = self.entries[label]["taxon_term"]["gtdb_classification"]
        if block == selected and label != AMSTERDAM:
            return R232
        return DEFAULT


def partition_corpus(documents, *, root: Path):
    """Return complete comparison groups after validating exact source admissions."""
    sources = AkkermansiaSources(root)
    partitions: dict[str, list] = {}
    for label, document in documents:
        sources.validate_document(label, document)
        for name, block in _blocks(document):
            group = sources.population(label, block, document)
            # Shape and current biology remain on the original documents. Only
            # the cross-record parent comparison receives these block views.
            view = {
                "taxonomy": [{"taxon_term": {"preferred_term": name, "gtdb_classification": block}}]
            }
            partitions.setdefault(group, []).append((label, view))
    return partitions


def check_source_bound_corpus(documents, *, root: Path) -> list[str]:
    """Apply the unchanged hierarchy check inside every authenticated group."""
    try:
        partitions = partition_corpus(documents, root=root)
    except (SourceProvenanceError, OSError, KeyError, TypeError) as error:
        return [f"source provenance refused: {error}"]
    return [
        f"[{group}] {problem}"
        for group, rows in partitions.items()
        for problem in check_corpus(rows)
    ]
