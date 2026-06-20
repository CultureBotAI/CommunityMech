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
                "feed_or_dilution_rate_unit": "h^-1",
                "ph_controlled": True,
                "do_controlled": True,
            },
            {
                "cultivation_mode": "BATCH",
                "system_type": "MICROBIAL_FUEL_CELL",
                "applied_potential": 200.0,
                "applied_potential_unit": "mV vs SHE",
                "electrode_detail": "carbon-cloth anode",
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
