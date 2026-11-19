"""Named-arm rendering preserves repeated observations and zero values (#2796)."""

from communitymech.render import CommunityRenderer


def test_named_arm_observations_keep_source_scope_and_legacy_values():
    record = {
        "id": "CommunityMech:999998",
        "name": "Synthetic rendering control",
        "taxonomy": [
            {
                "member_id": "member",
                "taxon_term": {
                    "preferred_term": "Test organism",
                    "term": {"id": "NCBITaxon:2", "label": "Bacteria"},
                },
                "relative_abundance": 0.7,
                "relative_abundance_unit": "fraction",
                "abundance_observations": [
                    {
                        "treatment_arm_id": "amended",
                        "timepoint_id": "day-one",
                        "replicate": "replicate 1",
                        "measurement_basis": "plate count",
                        "description": "Below detection <limit>",
                        "absolute_abundance": 0,
                        "absolute_abundance_unit": "CFU/mL",
                        "evidence": [{"reference": "PMID:1", "snippet": "Source <qualification>"}],
                    },
                    {
                        "treatment_arm_id": "amended",
                        "timepoint_id": "day-one",
                        "replicate": "replicate 2",
                        "measurement_basis": "amplicon reads",
                        "relative_abundance": 0,
                        "relative_abundance_unit": "FRACTION",
                    },
                ],
            }
        ],
        "treatment_arms": [
            {
                "id": "vehicle",
                "name": "Vehicle control",
                "context": "broth assay",
                "membership_status": "NOT_SPECIFIED",
            },
            {
                "id": "amended",
                "name": "Amended <arm>",
                "context": "broth assay",
                "membership_status": "DEFINED_MEMBERS",
                "participant_member_ids": ["member"],
                "comparator_arm_ids": ["vehicle"],
                "timepoints": [
                    {
                        "id": "day-one",
                        "name": "Day one",
                        "elapsed": {"value": 24, "unit": {"label": "hour"}},
                        "reference_event": "medium <exchange>",
                    }
                ],
                "conditions": [
                    {
                        "name": "dopamine",
                        "description": "Pulse exposure <not continuous>",
                        "value": "100",
                        "unit": "micromolar",
                        "term": {"id": "CHEBI:18243", "label": "dopamine"},
                    }
                ],
            },
            {
                "id": "sterile",
                "name": "Sterile control",
                "context": "broth assay",
                "membership_status": "NO_MICROBES",
            },
        ],
        "ecological_interactions": [
            {
                "name": "Scoped response",
                "scope": "COMMUNITY_LEVEL",
                "treatment_arm_ids": ["amended"],
            }
        ],
        "environmental_factors": [
            {
                "name": "Temperature",
                "value": "25",
                "unit": "Celsius",
                "term": {"id": "PATO:0000146", "label": "temperature"},
            }
        ],
    }
    html = (
        CommunityRenderer()
        .env.get_template("community.html")
        .render(community=record, source_file="fixture.yaml", related_pages={})
    )
    for value in [
        "0 CFU/mL",
        "0 FRACTION",
        "0.7 fraction",
        "replicate 1",
        "replicate 2",
        "plate count",
        "amplicon reads",
        "Legacy value; arm not assigned",
        "Day one",
        "24 hour",
        "Test organism (member)",
        "No microbes in this arm.",
        "Arm membership not specified.",
        "CHEBI:18243",
        "PATO:0000146",
        "Below detection &lt;limit&gt;",
        "after medium &lt;exchange&gt;",
        "Pulse exposure &lt;not continuous&gt;",
    ]:
        assert value in html
    assert html.count('href="#arm-amended"') == 3
    assert 'href="#arm-vehicle"' in html
    assert 'aria-label="Abundance observations"' in html
    assert "Source &lt;qualification&gt;" in html
    assert "Amended &lt;arm&gt;" in html
    assert "Amended <arm>" not in html


def test_absent_new_fields_render_no_empty_arm_or_observation_sections():
    html = (
        CommunityRenderer()
        .env.get_template("community.html")
        .render(
            community={"id": "CommunityMech:999998", "name": "Legacy record"},
            source_file="fixture.yaml",
            related_pages={},
        )
    )
    assert 'id="treatment-arms"' not in html
    assert 'id="abundance-observations"' not in html


def test_optional_qualifier_absence_does_not_invent_an_anchor_or_placeholder():
    html = (
        CommunityRenderer()
        .env.get_template("community.html")
        .render(
            community={
                "id": "CommunityMech:999998",
                "name": "Minimal arm control",
                "treatment_arms": [
                    {
                        "id": "control",
                        "name": "Control",
                        "context": "assay",
                        "membership_status": "NOT_SPECIFIED",
                        "conditions": [{"name": "Temperature", "value": "25", "unit": "Celsius"}],
                        "timepoints": [{"id": "endpoint", "name": "Endpoint"}],
                    }
                ],
            },
            source_file="fixture.yaml",
            related_pages={},
        )
    )
    section = html.split('<section id="treatment-arms">', 1)[1].split("</section>", 1)[0]
    assert "Endpoint (endpoint)" in section
    assert "after " not in section
    assert "None" not in section
    assert '<p class="prewrap"></p>' not in section
