"""`participating_taxa` narrows the community-level connectivity credit (#312).

A `COMMUNITY_LEVEL` interaction was credited as connecting **every** member of
the record. Defensible — such an interaction asserts something holding across
the community rather than between a named pair — and unavoidably coarse, because
`EcologicalInteraction` had only `source_taxon` and `target_taxon` and no way to
say *which* members participate. In a record carrying both kinds of edge, a
taxon in no pairwise edge could be credited by an unrelated community-level one.

`participating_taxa` is the refinement #312 proposed. Optional, and absent or
empty means "every member"; when a curator names participants, the
community-level credit narrows to those taxa.

Two things here were found by running the code rather than reading it, and both
are pinned below:

* an entry naming a member by CURIE resolved to the id string, which is not a
  key of `taxonomy_by_term` — so naming participants by id credited *nobody*
  and disconnected the whole record. The name path returned the right count
  throughout, so a test of the happy path alone would have shipped it.
* once that was fixed, naming by CURIE in the worked example credits **all 28**
  members, because those 28 taxa share one NCBITaxon id. That is correct, and it
  is the trap in #524: the slot silently does nothing in exactly the strain-level
  records whose over-broad credit motivated it.
"""

from __future__ import annotations

import pathlib
import tempfile

import pytest
import yaml

from communitymech.network.auditor import IssueType, NetworkIntegrityAuditor
from communitymech.paths import record_files

REPO = pathlib.Path(__file__).parent.parent

# Both record roots, not kb/communities alone. `data/isolates` holds the same
# root class -- 4 records with 66 snippets, 3 ecological_interactions and 3
# gtdb_classification blocks -- and this module could not see any of it (#689).
COMMUNITIES = REPO / "kb/communities"
# #312's illustration: 28 taxa, every interaction COMMUNITY_LEVEL.
EXAMPLE = COMMUNITIES / "GLBRC_Populus_Variovorax_SynCom28.yaml"


def _disconnected(document: dict) -> int:
    """DISCONNECTED findings for one record, audited in isolation."""
    with tempfile.TemporaryDirectory() as directory:
        path = pathlib.Path(directory) / "record.yaml"
        path.write_text(
            yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=4096),
            encoding="utf-8",
        )
        issues = NetworkIntegrityAuditor(pathlib.Path(directory)).audit_community(path) or []
        return sum(1 for issue in issues if issue["type"] == IssueType.DISCONNECTED)


@pytest.fixture
def example() -> dict:
    return yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))


def _members(document: dict) -> list[dict]:
    return [(entry.get("taxon_term") or {}) for entry in document.get("taxonomy") or []]


def test_the_example_still_has_the_shape_the_test_needs(example):
    """Guard: if the record changes, the numbers below stop meaning anything."""
    assert len(_members(example)) == 28
    interactions = example["ecological_interactions"]
    assert len(interactions) == 3
    assert all(i.get("scope") == "COMMUNITY_LEVEL" for i in interactions)


def test_absent_participating_taxa_still_credits_everyone(example):
    """The default, and why landing this changes no finding today."""
    assert _disconnected(example) == 0


def test_an_empty_list_means_every_member_not_none(example):
    """`[]` is "unspecified", not "nobody".

    The opposite reading would turn an interaction that omits the slot by
    accident into 28 spurious DISCONNECTED findings.
    """
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = []
    assert _disconnected(example) == 0


def test_naming_participants_narrows_the_credit(example):
    """The point of #312: 2 named of 28 leaves 26 uncredited."""
    members = _members(example)
    named = [
        {"preferred_term": m.get("preferred_term"), "term": m.get("term")} for m in members[:2]
    ]
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = named
    assert _disconnected(example) == 26


def test_narrowing_one_of_three_interactions_is_not_enough(example):
    """Credit is a union across interactions, so the others still cover everyone.

    Worth pinning because it is how the first run of this check fooled me: I
    narrowed only the first interaction, saw 0, and briefly took the feature
    for broken rather than the probe.
    """
    members = _members(example)
    example["ecological_interactions"][0]["participating_taxa"] = [
        {"preferred_term": members[0].get("preferred_term"), "term": members[0].get("term")}
    ]
    assert _disconnected(example) == 0


def test_a_curie_only_entry_resolves_rather_than_crediting_nobody(example):
    """The bug the canary caught: ids are not keys of `taxonomy_by_term`.

    Before the fix this returned 28 — every member disconnected — because the
    id string matched no member key and the interaction credited nothing.
    """
    members = _members(example)
    by_id = [{"term": {"id": m["term"]["id"]}} for m in members[:2] if m.get("term", {}).get("id")]
    assert by_id, "the example lost its term ids"
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = by_id
    assert _disconnected(example) != 28, (
        "a CURIE-named participant credited nobody, which disconnects the whole "
        "record — ids resolve through `taxonomy_keys_by_id`, not `taxonomy_by_term`"
    )


def test_a_curie_is_ambiguous_where_members_share_an_id(example):
    """#524, pinned as a property rather than left as a surprise.

    All 28 taxa carry `NCBITaxon:34072`. Naming two by CURIE credits all 28,
    which is the only sound reading of an ambiguous reference — and means the
    slot appears to do nothing in exactly the strain-level records that
    motivated it. The guidance ("name by preferred_term") is on the slot.
    """
    members = _members(example)
    ids = {m.get("term", {}).get("id") for m in members}
    assert len(ids) == 1, "the example no longer shares one id across its members"

    by_id = [{"term": {"id": next(iter(ids))}}]
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = by_id
    assert _disconnected(example) == 0


# The records that deliberately use the slot. Pinned as an exact set rather than
# an allowlist: adding *or* removing a user fails, so the population cannot drift
# in either direction. The connectivity numbers in
# `tests/test_community_level_connectivity_credit.py` must be re-checked when
# this set changes.
USERS = {
    "AMD_Acidophile_Heterotroph_Network.yaml",
    "AMD_Nitrososphaerota_Archaeal.yaml",
    "ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia.yaml",
    "Aalborg_East_Full_Scale_EBPR_Community.yaml",
    "Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml",
    "Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml",
    "Aerobic_Denitrification_Disturbance_SynCom.yaml",
    "Aerobic_Denitrification_QQ_SynCom.yaml",
    "Alaska_Tundra_Permafrost_Iron_Redox_Community.yaml",
    "Altered_Schaedler_Flora_Gnotobiotic_Mouse_Community.yaml",
    "Anammox_Bioreactor_DNRA_Destabilization_Community.yaml",
    "Anammox_Granule_Metabolic_Interaction_Community.yaml",
    "Apple_Fire_Blight_ANP_SynCom.yaml",
    "Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml",
    "Arabidopsis_Coumarin_Root_SynCom.yaml",
    "Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml",
    "At_RSPHERE_SynCom.yaml",
    "Australian_Lead_Zinc_Polymetallic.yaml",
    "Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml",
    "BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml",
    "Bacillus_A1_A3_Naphthalene_Biofilm_Consortium.yaml",
    "Bacillus_Bradyrhizobium_Straw_Humification_SynCom.yaml",
    "Bacillus_Saccharomyces_Daqu_Spatial_Cooperation_SynCom.yaml",
    "Bacteroides_Eubacterium_Gnotobiotic_Gut_Model.yaml",
    "Bacteroides_Methanobrevibacter_Gnotobiotic_Mouse_Mutualism.yaml",
    "Bayan_Obo_REE_Tailings_Consortium.yaml",
    "Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml",
    "Bifidobacterium_Trichomonas_Vaginal_Coculture.yaml",
    "BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml",
    "BioModels_MODEL2204300001_Kefir_Community_Model.yaml",
    "BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml",
    "BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom.yaml",
    "BioRock_ISS_Basalt_Biomining_Consortium.yaml",
    "Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml",
    "Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml",
    "Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml",
    "Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml",
    "Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml",
    "Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml",
    "Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml",
    "Candida_Parapsilosis_Hospitalized_Infant_Microbiome.yaml",
    "Caragana_Korshinskii_CrossKingdom_Forage_SynCom.yaml",
    "Chlamydomonas_Bacterial_H2_Consortium.yaml",
    "Chlamydomonas_Methylobacterium_Mutualism.yaml",
    "Chlorella_Keystone_Taxa_Antifungal_SynCom.yaml",
    "Chlorella_Rhizobium_Bioflocculation.yaml",
    "Chromium_Sulfur_Reduction_Enrichment.yaml",
    "Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml",
    "Clostridium_Caldicellulosiruptor_Minimal_Medium_Coculture.yaml",
    "Clostridium_Phytofermentans_Ecoli_Cellobiose_Biofilm_Consortium.yaml",
    "Coniochaeta_Sphingobacterium_Citrobacter_Wheat_Straw_Consortium.yaml",
    "Copper_Biomining_Heap_Leach.yaml",
    "Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml",
    "Coscinodiscus_Synthetic_Community.yaml",
    "Crucian_Carp_Gut_Disease_Resistance_SynCom.yaml",
    "DVM_Triculture.yaml",
    "Drought_Rhizosphere_Iron_Actinobacteria_Community.yaml",
    "EcoFAB_Ring_Trial_SynCom17.yaml",
    "Ecoli_Bifidobacterium_bifidum_Infant_gut_HMO_Mutualism_Coculture.yaml",
    "Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml",
    "Ensifer_YF2_Sphingobacterium_Y2_Polyethylene_Degrading_Consortium.yaml",
    "Episymbiotic_CPR_DPANN_Groundwater_Community.yaml",
    "Euglena_Chlorella_Microalgal_Biorefinery_Coculture.yaml",
    "Ewaste_Bioleaching_Consortium.yaml",
    "Ferroplasma_Leptospirillum_Syntrophy.yaml",
    "Geobacter_Methanosarcina_DIET.yaml",
    "Ginseng_CL95_Rusty_Root_Rot_Biocontrol_SynCom.yaml",
    "Honeybee_Core20_Defined_Microbiota.yaml",
    "Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml",
    "Iberian_Pit_Lake_Stratified_Community.yaml",
    "Industrial_Bioreactor_Consortium.yaml",
    "Infant_Gut_Strain_Persistence_Maternal_Community.yaml",
    "Legume_Rhizobia_Mars_Simulant_Symbiosis.yaml",
    "Lunar_Simulant_Phosphate_Solubilizing_Bacteria_Nicotiana.yaml",
    "MSC1_Dominant_Core.yaml",
    "MSC2_Model_Soil_Consortium.yaml",
    "Maize_Root_Simplified_Community.yaml",
    "Maize_SC2_RootRot_Biocontrol_SynCom.yaml",
    "Medicago_Nodule_Biofertilizer_SynCom.yaml",
    "Mesorhizobium_Synechococcus_B12_Synthetic_Consortium.yaml",
    "Methane_MFC_Electrogenesis_Nitrogen_Fixation_Consortium.yaml",
    "Methane_Oxidation_CrVI_Reduction_SynCom.yaml",
    "Mixed_Gallium_LED_Recovery_Consortium.yaml",
    "Mushroom_Spring_Hot_Spring_Phototrophic_Mat_Community.yaml",
    "Naica_Deep_Subsurface_Thermophilic.yaml",
    "ORNL_PMI_Populus_PD10_SynCom.yaml",
    "Ostreococcus_Dinoroseobacter_BVitamin_Mutualism.yaml",
    "PET_Artificial_FourSpecies_Degradation_Consortium.yaml",
    "PSY_Transgenic_Rice_Rhizosphere_Methane_Community.yaml",
    "Phenol_Carboxylation_Consortium.yaml",
    "Propanotrophic_Chlorinated_Ethene_Cometabolism_Enrichment.yaml",
    "Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture.yaml",
    "Rhodococcus_Pseudomonas_PPOW_Consortium.yaml",
    "Rifle_Aquifer_Bioanode_EET_Community.yaml",
    "SF356_Cellulose_Degrader.yaml",
    "Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml",
    "Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml",
    "Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture.yaml",
    "Soil_Corrinoid_B12_Reservoir_Community.yaml",
    "Soybean_Chlorophyll_Selected_Biofertilizer_SynCom.yaml",
    "Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml",
    "Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml",
    "SynComBac10_Chicken_Intestinal_SynCom.yaml",
    "SynCom_Pseudomonas_Rahnella_Artemisia_Phytoremediation.yaml",
    "SynCom_Sesame_Flavor_Baijiu_Fuqu_13Genus.yaml",
    "Synechococcus_Halomonas_Light_Driven_PHB_Coculture.yaml",
    "Synechococcus_Pseudomonas_PhotoPHA_DNT_Coculture.yaml",
    "Synthetic_Lichen_Synechococcus_Rhodotorula_Coculture.yaml",
    "Syntrophobacter_Methanobacterium_Syntrophy.yaml",
    "Syntrophobacter_Methanospirillum_Syntrophy.yaml",
    "Syntrophomonas_Methanospirillum_Syntrophy.yaml",
    "Syntrophus_Benzoate_Degrader.yaml",
    "Tropidoatractus_Magnetotacticus_Tripartite_Syntrophy.yaml",
    "Urine_Nitrification_SynCom.yaml",
    "Wheat_Consortium_C1.yaml",
    "Wheat_Consortium_C6.yaml",
    "Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml",
    "Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.yaml",
    "mCAFEs_Brachypodium_RCC.yaml",
}


def test_the_corpus_is_unchanged_by_this_feature():
    """Only the records that mean to use the slot do.

    Asserted on the corpus rather than trusted from the schema: an
    `ifabsent` or a default that quietly populated the slot would change 312
    records' connectivity without anyone editing a record. That is still the
    failure this catches — a silent default would put every record in `users`,
    not just the three named below.
    """
    users = {
        path.name
        for path in record_files()
        for interaction in (yaml.safe_load(path.read_text()) or {}).get("ecological_interactions")
        or []
        if isinstance(interaction, dict) and interaction.get("participating_taxa")
    }
    assert users == USERS, (
        f"{len(users)} records use participating_taxa, expected {len(USERS)}. "
        f"Adding a user is fine — but the connectivity numbers in "
        f"tests/test_community_level_connectivity_credit.py were measured "
        f"before the slot was used, so re-check them and then update USERS. "
        f"Added: {sorted(users - USERS)}. Removed: {sorted(USERS - users)}"
    )


def test_a_name_beats_an_id_on_the_same_entry(example):
    """Precedence, not union — and the flaw that nearly shipped this useless.

    Curators copy the whole `taxon_term` block into a participant, so an entry
    normally carries `preferred_term` *and* `term.id`. Resolving both and
    unioning them meant the id credited all 28 members sharing it, so an entry
    naming one strain credited every strain and the narrowing did nothing.

    The name path alone gave the right answer at every step, and the id path
    alone gave the right answer; only an entry carrying both was wrong. That is
    why this case is pinned separately from the two above.
    """
    members = _members(example)
    both = [{"preferred_term": m.get("preferred_term"), "term": m.get("term")} for m in members[:2]]
    assert all(entry["term"].get("id") for entry in both), "the fixture lost its ids"
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = both
    assert _disconnected(example) == 26, (
        "an entry carrying both a preferred_term and a shared term.id credited "
        "every member sharing that id, defeating the narrowing (#312/#524)"
    )
