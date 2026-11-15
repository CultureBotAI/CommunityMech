"""Validate affirmative fungal-domain observations, #2904, 2026-11-15.

Inputs: captured source occurrences and observations from the unchanged native
classifier/local NCBI adapter. Outputs: validated metadata only; no writes,
acquisition, executor patching, or inference of absence from a null lookup.
"""

import sqlite3
from pathlib import Path

CONTRACT = "gtdb-mixed-fungal-domain-v1"
HELPER = "scripts/adhoc/gtdb_fungal_domain_contract_20261115.py"
ENGINE = "scripts/adhoc/gtdb_fungal_batch_curation_20261115.py"
DOMAIN = "src/communitymech/validators/ncbi_domain.py"
ADAPTER = "src/communitymech/ontology_adapters.py"
NATIVE = "scripts/gtdb_ground.py"
EUKARYOTA = "NCBITaxon:2759"
FUNGI = "NCBITaxon:4751"
STATUS = {"status": "NO_GTDB_EQUIVALENT", "candidates": []}
# Deliberately bounded to these recognized principal ranks; other ranks need review.
IDENTITY_RANKS = {
    "NCBITaxon:superkingdom",
    "NCBITaxon:kingdom",
    "NCBITaxon:phylum",
    "NCBITaxon:class",
    "NCBITaxon:order",
    "NCBITaxon:family",
    "NCBITaxon:genus",
    "NCBITaxon:species",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def require_fungal_source(occurrence):
    descriptor = occurrence["existing_descriptor"]
    require(
        occurrence["native_result"] is None
        and occurrence.get("classify_status") == STATUS
        and occurrence["term"]["id"].startswith("NCBITaxon:")
        and "gtdb_classification" not in descriptor
        and descriptor.get("gtdb_grounding_status") not in {"WITHHELD", "NO_GTDB_EQUIVALENT"}
        and "manual_curated_reason" in occurrence
        and "manual_withheld_reason" in occurrence
        and occurrence["manual_curated_reason"] is None
        and occurrence["manual_withheld_reason"] is None,
        "explicit unheld fungal-null NO_GTDB_EQUIVALENT source required",
    )


def verify_mixed(row, flags):
    require(flags == ["--apply", "--apply-status"], "explicit mixed native operations required")
    fungal = grounded = 0
    for item in row["occurrences"]:
        result = item["native_result"]
        descriptor = item["existing_descriptor"]
        require(
            "gtdb_classification" not in descriptor
            and descriptor.get("gtdb_grounding_status") not in {"WITHHELD", "NO_GTDB_EQUIVALENT"}
            and "manual_curated_reason" in item
            and "manual_withheld_reason" in item
            and item["manual_curated_reason"] is None
            and item["manual_withheld_reason"] is None,
            "mixed unit cannot override existing blocks or manual holds",
        )
        if result is None:
            require_fungal_source(item)
            fungal += 1
        else:
            require(isinstance(result, dict), "unsupported mixed native result")
            if result.get("gtdb_id"):
                grounded += 1
            else:
                require(result.get("ambiguous") is True, "unsupported mixed native result")
    require(fungal > 0 and grounded > 0, "mixed unit requires fungal null and a grounded route")


def database_stat(database):
    stat = database.stat()
    return {
        "filename": database.name,
        "device": stat.st_dev,
        "inode": stat.st_ino,
        "bytes": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "content_hash": None,
        "limitation": "File identity/stat only; no whole-database hash or release assertion.",
    }


def identity(database, occurrence):
    """Read the exact identity rows bound by the reviewed source adapter."""
    with sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True) as connection:
        connection.row_factory = sqlite3.Row
        result = [
            dict(row)
            for row in connection.execute(
                "SELECT subject,predicate,value,object FROM statements WHERE subject=? "
                "AND (predicate='rdfs:label' OR predicate LIKE '%Synonym%' "
                "OR predicate LIKE '%rank%' OR predicate='rdfs:subClassOf') "
                "ORDER BY predicate,value,object",
                (occurrence["term"]["id"],),
            )
        ]
    verify_identity(occurrence, result)
    return result


def verify_identity(occurrence, rows):
    require(
        isinstance(rows, list)
        and rows
        and rows == occurrence.get("ncbi_identity_rows")
        and all(row["subject"] == occurrence["term"]["id"] for row in rows)
        and {row["value"] for row in rows if row["predicate"] == "rdfs:label"}
        == {occurrence["term"]["label"]}
        and len({row["object"] for row in rows if row["predicate"].endswith("rank")}) == 1,
        "exact bound native NCBI label/rank identity required",
    )
    require(
        {row["object"] for row in rows if row["predicate"].endswith("rank")} <= IDENTITY_RANKS,
        "one recognized NCBI rank required for affirmative fungal identity",
    )


def observe(native, domain, adapter, row, occurrence, rows, identity_rows):
    require_fungal_source(occurrence)
    term = occurrence["term"]
    record_name = Path(row["record"]).name
    descriptor = occurrence["existing_descriptor"]
    require(
        (record_name, term["id"]) not in native.CURATED_GROUNDINGS
        and (record_name, descriptor.get("preferred_term")) not in native.WITHHELD_GROUNDINGS,
        "native manual hold forbids fungal admission",
    )
    require(domain._adapter() is adapter, "native domain classifier must use the same adapter")
    domain.domain_of.cache_clear()
    ancestors = sorted(set(adapter.ancestors([term["id"]], predicates=["rdfs:subClassOf"])))
    actual_domain = domain.domain_of(term["id"])
    status, candidates = native.classify_status(
        record_name,
        term["id"],
        term["label"],
        False,
        *rows,
        preferred=descriptor.get("preferred_term"),
    )
    result = {
        "taxonomy_index": occurrence["taxonomy_index"],
        "term": term,
        "strain_name": occurrence["strain_name"],
        "native_result": native.resolve_target(term["id"].split(":", 1)[1], term["label"], *rows),
        "classify_status": {"status": status, "candidates": candidates},
        "domain": actual_domain,
        "outside_gtdb_scope": domain.outside_gtdb_scope(term["id"]),
        "ancestor_ids": ancestors,
        "ncbi_identity_rows": identity_rows,
        "manual_curated_reason": None,
        "manual_withheld_reason": None,
        "scope": "Reference taxonomy/domain observation only; no stock assembly or biological claim.",
    }
    verify_observation(occurrence, result)
    return result


def verify_observation(occurrence, observation):
    require_fungal_source(occurrence)
    verify_identity(occurrence, observation.get("ncbi_identity_rows"))
    ancestors = observation.get("ancestor_ids")
    require(
        observation.get("taxonomy_index") == occurrence["taxonomy_index"]
        and observation.get("term") == occurrence["term"]
        and observation.get("strain_name") == occurrence["strain_name"]
        and "native_result" in observation
        and observation["native_result"] is None
        and observation.get("classify_status") == STATUS
        and observation.get("domain") == EUKARYOTA
        and observation.get("outside_gtdb_scope") is True
        and isinstance(ancestors, list)
        and all(isinstance(value, str) and value.startswith("NCBITaxon:") for value in ancestors)
        and ancestors == sorted(set(ancestors))
        and {FUNGI, EUKARYOTA}.issubset(ancestors)
        and not {"NCBITaxon:2", "NCBITaxon:2157", "NCBITaxon:10239"}.intersection(ancestors)
        and "manual_curated_reason" in observation
        and "manual_withheld_reason" in observation
        and observation["manual_curated_reason"] is None
        and observation["manual_withheld_reason"] is None,
        "affirmative matched Fungi/Eukaryota native observation required",
    )


def verify_document(row, document, source_proof, inputs):
    verify_mixed(row, ["--apply", "--apply-status"])
    require(
        document.get("contract") == CONTRACT
        and document.get("target") == row["record"]
        and document.get("target_id") == row["record_id"]
        and document.get("before_sha256") == row["before_sha256"]
        and document.get("source_proof") == source_proof
        and document.get("inputs") == inputs
        and document.get("scientific_review") is False,
        "fungal domain observation provenance differs",
    )
    selected = [item for item in row["occurrences"] if item["native_result"] is None]
    observations = document.get("observations", [])
    require(
        len(observations) == len(selected)
        and [item["taxonomy_index"] for item in observations]
        == [item["taxonomy_index"] for item in selected],
        "exact fungal observation coverage required",
    )
    for item, observation in zip(selected, observations, strict=True):
        verify_observation(item, observation)
    for name in (HELPER, ENGINE, DOMAIN, ADAPTER, NATIVE):
        require(name in inputs and len(inputs[name]) == 64, "domain implementation input absent")
    stat = document.get("database_observation", {})
    require(
        stat.get("filename") == "ncbitaxon.db"
        and all(
            type(stat.get(key)) is int and stat[key] >= 0
            for key in ("device", "inode", "bytes", "mtime_ns")
        )
        and stat["bytes"] > 0
        and stat.get("content_hash") is None,
        "explicit local database stat observation required",
    )
