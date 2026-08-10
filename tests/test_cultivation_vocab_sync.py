"""Keep the cultivation enums (schema) and vocab/cultivation_terms.yaml in sync,
and smoke-test the new optional cultivation_setup slot.

The inline enums in the LinkML schema are canonical for validation; the vocab
file is canonical for term metadata (definition/synonyms/mapping/status) staged
for a METPO proposal. These tests guarantee the two never drift.
"""

import subprocess
from pathlib import Path

import yaml

SCHEMA = "src/communitymech/schema/communitymech.yaml"
VOCAB = Path("vocab/cultivation_terms.yaml")
ENUMS = ("CultivationModeEnum", "CultivationSystemEnum")
VALID_STATUS = {"proposed", "mapped", "minted"}

# Every other enum in the schema, with why it is not staged for METPO. The point
# is not the exemption but that one has to be written: `ENUMS` above is a
# hardcoded tuple, so before #518 a new enum simply fell outside the invariant
# `vocab/cultivation_terms.yaml` claims in its own header, and nothing went red.
# Same shape as #471 — a constant whose value was pinned but whose completeness
# was not.
_NOT_STAGED_FOR_METPO = {
    "CommunityOriginEnum": "structural metadata about the record, not a lab term",
    "CommunityCategoryEnum": "structural metadata about the record, not a lab term",
    # Units (#514). If these map anywhere it is UO or UCUM, not METPO.
    "TimeUnitEnum": "a unit",
    "VolumeUnitEnum": "a unit",
    "RateUnitEnum": "a unit",
    "TemperatureUnitEnum": "a unit",
    "PotentialUnitEnum": "a unit",
    "RetentionTimeTypeEnum": "which retention time is reported; a modelling kind, not a term",
    # Already grounded in an ontology, so there is nothing to propose: every
    # permissible value carries a `meaning:` CURIE (17 and 16 respectively).
    "MetalElementEnum": "fully mapped in-schema via meaning: CURIEs",
    "RareEarthElementEnum": "fully mapped in-schema via meaning: CURIEs",
    # Curation bookkeeping — how this repo records a claim, not what was
    # observed at a bench. METPO would have nothing to say about them.
    "EvidenceItemSupportEnum": "how a reference relates to a claim; curation bookkeeping",
    "EvidenceSourceEnum": "where a claim came from; curation bookkeeping",
    "ExternalResourceRepositoryEnum": "which repository a link points at; bookkeeping",
    "GtdbGroundingStatusEnum": "state of this repo's grounding workflow; bookkeeping",
    "ComputationalPredictionTypeEnum": "how a model produced a value; provenance, not a lab term",
    "CultureCollectionEnum": "strain-repository names (DSM, ATCC, ...); registry identifiers",
    "MetalRelevanceEnum": "whether metals matter to a record; a curation judgement",
    "AbundanceEnum": "qualitative abundance banding; a modelling convention here",
    "InteractionScopeEnum": "pairwise vs community-level; a graph-modelling distinction",
    # Genuine ontology candidates that are simply not staged yet. Named here
    # rather than silently omitted: the exemption is "not done", not "not
    # applicable", and #518 exists so that difference stays visible.
    "FunctionalRoleEnum": "candidate, not yet staged; see #301 for values it is missing",
    "InteractionTypeEnum": "candidate, not yet staged; overlaps the #270/#307 modelling questions",
    "AtmosphereEnum": "candidate, not yet staged; plausibly ENVO/METPO",
    "MediaRelationshipEnum": "candidate, not yet staged; adjacent to the growth-media work in #183",
    "EcologicalStateEnum": "candidate, not yet staged; plausibly ENVO",
}


def _schema():
    return yaml.safe_load(Path(SCHEMA).read_text())


def _vocab():
    return yaml.safe_load(VOCAB.read_text())


def test_enum_keys_equal_vocab_keys():
    schema, vocab = _schema(), _vocab()
    for enum in ENUMS:
        enum_keys = set(schema["enums"][enum]["permissible_values"].keys())
        vocab_keys = set(vocab[enum].keys())
        missing = enum_keys - vocab_keys
        extra = vocab_keys - enum_keys
        assert not missing, f"{enum}: vocab missing {sorted(missing)}"
        assert not extra, f"{enum}: vocab has stale keys {sorted(extra)}"


def test_vocab_terms_well_formed():
    vocab = _vocab()
    for enum in ENUMS:
        for key, term in vocab[enum].items():
            for field in ("label", "definition", "mapping", "status"):
                assert term.get(field), f"{enum}.{key} missing/empty {field}"
            assert term["status"] in VALID_STATUS, f"{enum}.{key} bad status {term['status']}"
            assert isinstance(term.get("synonyms", []), list), f"{enum}.{key} synonyms not a list"
            # status mapped <=> a real ontology CURIE; proposed <=> metpo-candidate
            if term["status"] == "mapped":
                assert term["mapping"] != "metpo-candidate", f"{enum}.{key} mapped but no CURIE"
            if term["mapping"] == "metpo-candidate":
                assert term["status"] == "proposed", f"{enum}.{key} candidate must be proposed"


def test_schema_meaning_matches_vocab_mapping():
    """Every enum value with a schema `meaning:` must match the vocab mapping + be status mapped."""
    schema, vocab = _schema(), _vocab()
    for enum in ENUMS:
        for key, pv in schema["enums"][enum]["permissible_values"].items():
            meaning = (pv or {}).get("meaning")
            if meaning:
                assert vocab[enum][key]["mapping"] == meaning, (
                    f"{enum}.{key}: schema meaning {meaning} != vocab mapping "
                    f"{vocab[enum][key]['mapping']}"
                )
                assert vocab[enum][key]["status"] == "mapped"


def test_cultivation_setup_validates(tmp_path):
    community = {
        "id": "CommunityMech:000999",
        "name": "cultivation_setup smoke test",
        "cultivation_setup": [
            {
                "cultivation_mode": "CHEMOSTAT",
                "system_type": "STIRRED_TANK_BIOREACTOR",
                "working_volume": 1.5,
                "working_volume_unit": "L",
                "feed_or_dilution_rate": 0.1,
                "feed_or_dilution_rate_unit": "1/h",
                "ph_controlled": True,
                "do_controlled": True,
            },
            {
                "cultivation_mode": "BATCH",
                "system_type": "MICROBIAL_FUEL_CELL",
                "applied_potential": 200.0,
                "applied_potential_unit": "mV",
                # The reference electrode is not part of the unit: it moved into
                # `electrode_detail` when these slots became enums (#514).
                "electrode_detail": "carbon-cloth anode, potential quoted vs SHE",
            },
        ],
    }
    f = tmp_path / "c.yaml"
    f.write_text(yaml.safe_dump(community))
    res = subprocess.run(
        [
            "uv",
            "run",
            "linkml-validate",
            "-s",
            SCHEMA,
            "--target-class",
            "MicrobialCommunity",
            str(f),
        ],
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0, f"cultivation_setup smoke test failed:\n{res.stdout}\n{res.stderr}"


def test_every_enum_is_either_staged_or_explicitly_exempt():
    """A new enum must be classified when it is added, not in a later audit (#518).

    `ENUMS` is a hardcoded tuple, so the invariant the vocab file states in its
    header only ever applied to the two names typed into it. #517 added six
    enums at once and none of them went red — correctly, since they are units,
    but the repo could not tell "deliberately exempt" from "nobody noticed".

    Listing every schema enum here forces the author of the next one to say
    which it is. The exemption reasons are required to be non-empty so the
    dictionary cannot become a silent allow-list.
    """
    schema_enums = set(_schema()["enums"])
    classified = set(ENUMS) | set(_NOT_STAGED_FOR_METPO)

    unclassified = sorted(schema_enums - classified)
    assert unclassified == [], (
        "these enums are neither staged in vocab/cultivation_terms.yaml (add "
        "them to ENUMS) nor exempted (add them to _NOT_STAGED_FOR_METPO with a "
        "reason):\n" + "\n".join(f"  {name}" for name in unclassified)
    )

    stale = sorted(classified - schema_enums)
    assert (
        stale == []
    ), "these are classified here but no longer exist in the schema:\n" + "\n".join(
        f"  {name}" for name in stale
    )

    assert not (set(ENUMS) & set(_NOT_STAGED_FOR_METPO)), "an enum cannot be both"
    blank = sorted(name for name, why in _NOT_STAGED_FOR_METPO.items() if not (why or "").strip())
    assert blank == [], f"exemptions need a reason: {blank}"
