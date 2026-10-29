# Hosts, soils and related communities

Schema additions for three things the model could not say before: how two
community records relate, which host a community lives on, and what soil it
lives in. They follow the DisMech/mechmaker conventions (mechmaker
`docs/design.md` §5-§7, `skills/design-mech-schema`): a descriptor per role
with `preferred_term` plus a `term` bound to a checked dynamic enum, measured
values as `Quantity` with a UO unit, evidence as `EvidenceItem` quoting the
source verbatim, and every addition optional so no existing record changes.

Worked examples, all from PMID:42660928 (Ding et al. 2026), PMID:40920748 (the
EcoFAB 2.0 ring trial) and PMID:36472419 (Coker et al. 2022):

| Record | Shows |
|---|---|
| `Brachypodium_Natural_Variation_Dopamine_SynCom16` (000496) | `host` with ten genotypes, a computed `MEMBER_SUBSET_OF`, a quoted `OVERLAPPING_MEMBERSHIP`, `host_participation`, `effect_direction`, `HYDROPONIC_VESSEL` |
| `Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm` (000497) | `soils` with texture, location, sieve size and water content; no host; `SAME_STUDY_AS`; `SOIL_MICROCOSM` |
| `EcoFAB_Ring_Trial_SynCom17` (000025) | `host` with one line; computed `MEMBER_SUPERSET_OF` |
| `LBNL_Switchgrass_Soil_SynCom16` (000087) | links from a record with no strain roster, so `SOURCE_STATEMENT` |

## `related_communities`

| | |
|---|---|
| Question | Which other records describe the same strains, a subset of them, the community this one came from, or a sibling experiment of the same study? |
| Grounding | None: the target is a `CommunityMech:` id. Field names follow mech_shared `CrossCorpusLink` (`identifier`, `relation`, `basis`), without `corpus`, which is always this one. |
| Cardinality | Many. |
| Who fills it, by what rule | A curator, whenever two records share a strain, a source names a parent community, or one paper yields two records. Add the inverse link on the target in the same change. |

Relations (`CommunityRelationEnum`):

- **Membership** (`SAME_MEMBERSHIP_AS`, `MEMBER_SUBSET_OF`, `MEMBER_SUPERSET_OF`,
  `OVERLAPPING_MEMBERSHIP`) are facts about two strain lists. When both records
  name a strain for every member, use `basis: SHARED_STRAIN_DESIGNATIONS`: the
  validator recomputes the relation and fails on a mismatch. When either roster
  is incomplete, use `basis: SOURCE_STATEMENT` and quote the rosters.
- **`DERIVED_FROM`**: a source says this community was assembled, enriched or
  isolated from the target. Always `SOURCE_STATEMENT` with a quote.
- **`SAME_STUDY_AS`**: a different community from the same paper, when nothing
  above holds.

Not for: two records that merely share a genus, an environment or an ontology
term. A shared term is a lead for a link, not a link.

Checked by `communitymech.validators.related_communities` in
`just validate-strict`: the target exists, no self-links or duplicates,
`SOURCE_STATEMENT` has evidence, `SHARED_STRAIN_DESIGNATIONS` is used only for
membership relations between two complete rosters, and a membership relation
never contradicts the rosters, whatever its basis.

Example (000496): its 16 strains are the ring trial's 17 minus
Bradyrhizobium OAE829, so `MEMBER_SUBSET_OF CommunityMech:000025` is computed.
It shares 15 strains with Coker et al.'s final 16, which has Bradyrhizobium
OAE829 where 000496 has OAE603. 000087 does not list strains, so that link is
`OVERLAPPING_MEMBERSHIP` with `SOURCE_STATEMENT` and quotes both rosters.

## `host`

| | |
|---|---|
| Question | On or in which organism does the community live, or was it inoculated, and in what state? |
| Grounding | `term` → `HostTaxonTerm` (NCBITaxon under NCBITaxon:2759 Eukaryota). `anatomical_sites[].term` → `HostAnatomyTerm` (PO:0025131 plant anatomical entity, UBERON:0001062 anatomical entity). `developmental_stage.term` → `HostDevelopmentalStageTerm` (PO:0009012 plant structure development stage, UBERON:0000105 life cycle stage). |
| Cardinality | One per record. The same community on two host species is two records joined by `SAME_MEMBERSHIP_AS`. |
| Who fills it, by what rule | A curator, for any record whose source names a host. `genotypes` takes each line name exactly as written. `microbial_status` is `AXENIC` only when the source describes sterilization or germ-free status, `CONVENTIONAL` when the host kept its own microbiota, otherwise `NOT_REPORTED`. `developmental_stage` only when a PO or UBERON stage fits; "four-week-old plants" alone goes in `description`. |

The host is not a member (#319): it never appears in `taxonomy`, and the
validator fails a record whose host id is also a member.

An interaction involving the host keeps `COMMUNITY_LEVEL` scope with
`participating_taxa` for the members, and says the host's role in
`host_participation`:

- `HOST_IS_SOURCE`: the host produces the factor (a root exudate).
- `HOST_IS_TARGET`: members act on the host.
- `RECIPROCAL`: both directions are shown.

A record with `host_participation` and no `host` fails validation.

## `soils`

| | |
|---|---|
| Question | What soil, from where, handled how, at what measured properties? |
| Grounding | `term` and `texture` → `SoilTerm` (ENVO under ENVO:00001998 soil). ENVO models texture classes (loam, silty loam, sandy loam, clay loam) as subclasses of soil, so one root admits both. `Quantity.unit` → `UnitTerm` (UO under UO:0000000 unit). |
| Cardinality | Many; one entry per distinct soil. |
| Who fills it, by what rule | A curator, from the Methods. `term` is the use or provenance class (`agricultural soil`), or `soil` when nothing narrower fits; `texture` only when the source states it. Each measured property is a `Quantity` with the number as printed and a UO unit, and is left empty when unreported. `location` is decimal degrees, converted from the source's form; say so in `description`. `sterilization` is `NONE` only when the source uses the soil as collected. |

Not for liquid or agar media, which stay in `growth_media`.

## Interaction sign: `effect_direction`

`EffectDirectionEnum` (`INCREASES`, `DECREASES`, `NO_DETECTED_CHANGE`,
`MIXED`) gives the sign of the effect on the target's measured response.
Set it only when the source reports a direction. Prefer two interactions to
one `MIXED`: 000496 splits its exudate-dopamine correlation into a positive
edge (five members) and a negative edge (OAS925).

## `CultivationSystemEnum` additions

`PLANT_POT`, `SOIL_MICROCOSM`, `HYDROPONIC_VESSEL` and
`FABRICATED_ECOSYSTEM_DEVICE` (EcoFAB), staged in
`vocab/cultivation_terms.yaml` as METPO candidates.

## Checked roots

Each root was checked against the ontology (OLS4) together with a term it
must admit:

| Enum | Root | Admits |
|---|---|---|
| HostTaxonTerm | NCBITaxon:2759 Eukaryota | NCBITaxon:15368 Brachypodium distachyon |
| HostAnatomyTerm | PO:0025131 plant anatomical entity; UBERON:0001062 anatomical entity | PO:0009005 root; UBERON:0000160 intestine |
| HostDevelopmentalStageTerm | PO:0009012 plant structure development stage; UBERON:0000105 life cycle stage | (none used yet) |
| SoilTerm | ENVO:00001998 soil | ENVO:00002259 agricultural soil; ENVO:06105275 silty loam |
| UnitTerm | UO:0000000 unit | UO:0000187 percent; UO:0000016 millimeter; UO:0000196 pH |

`just validate-terms` enforces them. With mutated copies of 000496 and
000497, it rejected a bacterial phylum as host, a GO process as host anatomy,
a bioreactor as soil and a soil as a unit, while the unmutated copies passed.

## Deferred

- **Treatment arms.** Named experimental conditions (axenic vs inoculated,
  dose levels, host lines) that abundances and interactions can refer to. It
  touches the abundance and interaction model and needs its own design (#1729
  is one instance of the need).
- **An ontology term on `EnvironmentalFactor`.**
- **KGX export of host, soil and related-community edges.** The new sections
  are rendered on community pages but not yet exported as graph edges.
- **A strain roster for 000087** (#1548), which would turn its two
  `SOURCE_STATEMENT` links into computed ones.
