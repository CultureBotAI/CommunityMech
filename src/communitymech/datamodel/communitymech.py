# Auto generated from communitymech.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-14T19:12:10
# Schema: communitymech
#
# id: https://w3id.org/culturebot-ai/communitymech
# description: Schema for modeling microbial community structure, function, and ecological interactions
# license: BSD-3-Clause

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
COMMUNITYMECH = CurieNamespace('communitymech', 'https://w3id.org/culturebot-ai/communitymech/')
DOI = CurieNamespace('doi', 'https://doi.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = COMMUNITYMECH


# Types
class PMID(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PMID"
    type_model_uri = COMMUNITYMECH.PMID


# Class references
class MicrobialCommunityId(extended_str):
    pass


@dataclass(repr=False)
class Term(YAMLRoot):
    """
    An ontology term with ID and label
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["Term"]
    class_class_curie: ClassVar[str] = "communitymech:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.Term

    id: str = None
    label: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceItem(YAMLRoot):
    """
    An evidence item linking a claim to a publication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["EvidenceItem"]
    class_class_curie: ClassVar[str] = "communitymech:EvidenceItem"
    class_name: ClassVar[str] = "EvidenceItem"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.EvidenceItem

    reference: str = None
    supports: Union[str, "EvidenceItemSupportEnum"] = None
    evidence_source: Union[str, "EvidenceSourceEnum"] = None
    snippet: str = None
    explanation: Optional[str] = None
    confidence_score: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self._is_empty(self.supports):
            self.MissingRequiredField("supports")
        if not isinstance(self.supports, EvidenceItemSupportEnum):
            self.supports = EvidenceItemSupportEnum(self.supports)

        if self._is_empty(self.evidence_source):
            self.MissingRequiredField("evidence_source")
        if not isinstance(self.evidence_source, EvidenceSourceEnum):
            self.evidence_source = EvidenceSourceEnum(self.evidence_source)

        if self._is_empty(self.snippet):
            self.MissingRequiredField("snippet")
        if not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        if self.confidence_score is not None and not isinstance(self.confidence_score, float):
            self.confidence_score = float(self.confidence_score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonDescriptor(YAMLRoot):
    """
    Describes an organism with NCBITaxon term
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["TaxonDescriptor"]
    class_class_curie: ClassVar[str] = "communitymech:TaxonDescriptor"
    class_name: ClassVar[str] = "TaxonDescriptor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.TaxonDescriptor

    preferred_term: str = None
    term: Union[dict, Term] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetaboliteDescriptor(YAMLRoot):
    """
    Describes a metabolite with CHEBI term
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["MetaboliteDescriptor"]
    class_class_curie: ClassVar[str] = "communitymech:MetaboliteDescriptor"
    class_name: ClassVar[str] = "MetaboliteDescriptor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.MetaboliteDescriptor

    preferred_term: str = None
    term: Union[dict, Term] = None
    concentration: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.concentration is not None and not isinstance(self.concentration, str):
            self.concentration = str(self.concentration)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalProcessDescriptor(YAMLRoot):
    """
    Describes a biological process with GO term
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["BiologicalProcessDescriptor"]
    class_class_curie: ClassVar[str] = "communitymech:BiologicalProcessDescriptor"
    class_name: ClassVar[str] = "BiologicalProcessDescriptor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.BiologicalProcessDescriptor

    preferred_term: str = None
    term: Union[dict, Term] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentDescriptor(YAMLRoot):
    """
    Describes an environment with ENVO term
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["EnvironmentDescriptor"]
    class_class_curie: ClassVar[str] = "communitymech:EnvironmentDescriptor"
    class_name: ClassVar[str] = "EnvironmentDescriptor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.EnvironmentDescriptor

    preferred_term: str = None
    term: Union[dict, Term] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CultureCollectionID(YAMLRoot):
    """
    A culture collection identifier with accession number
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["CultureCollectionID"]
    class_class_curie: ClassVar[str] = "communitymech:CultureCollectionID"
    class_name: ClassVar[str] = "CultureCollectionID"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.CultureCollectionID

    collection: Union[str, "CultureCollectionEnum"] = None
    accession: str = None
    url: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.collection):
            self.MissingRequiredField("collection")
        if not isinstance(self.collection, CultureCollectionEnum):
            self.collection = CultureCollectionEnum(self.collection)

        if self._is_empty(self.accession):
            self.MissingRequiredField("accession")
        if not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StrainDesignation(YAMLRoot):
    """
    Detailed strain-level information for reproducibility
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["StrainDesignation"]
    class_class_curie: ClassVar[str] = "communitymech:StrainDesignation"
    class_name: ClassVar[str] = "StrainDesignation"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.StrainDesignation

    strain_name: Optional[str] = None
    culture_collections: Optional[Union[Union[dict, CultureCollectionID], list[Union[dict, CultureCollectionID]]]] = empty_list()
    type_strain: Optional[Union[bool, Bool]] = None
    genome_accession: Optional[str] = None
    genome_url: Optional[str] = None
    genetic_modification: Optional[str] = None
    isolation_source: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.strain_name is not None and not isinstance(self.strain_name, str):
            self.strain_name = str(self.strain_name)

        self._normalize_inlined_as_dict(slot_name="culture_collections", slot_type=CultureCollectionID, key_name="collection", keyed=False)

        if self.type_strain is not None and not isinstance(self.type_strain, Bool):
            self.type_strain = Bool(self.type_strain)

        if self.genome_accession is not None and not isinstance(self.genome_accession, str):
            self.genome_accession = str(self.genome_accession)

        if self.genome_url is not None and not isinstance(self.genome_url, str):
            self.genome_url = str(self.genome_url)

        if self.genetic_modification is not None and not isinstance(self.genetic_modification, str):
            self.genetic_modification = str(self.genetic_modification)

        if self.isolation_source is not None and not isinstance(self.isolation_source, str):
            self.isolation_source = str(self.isolation_source)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonomicComposition(YAMLRoot):
    """
    A taxon present in the community with abundance and role
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["TaxonomicComposition"]
    class_class_curie: ClassVar[str] = "communitymech:TaxonomicComposition"
    class_name: ClassVar[str] = "TaxonomicComposition"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.TaxonomicComposition

    taxon_term: Union[dict, TaxonDescriptor] = None
    strain_designation: Optional[Union[dict, StrainDesignation]] = None
    abundance_level: Optional[Union[str, "AbundanceEnum"]] = None
    abundance_value: Optional[str] = None
    functional_role: Optional[Union[Union[str, "FunctionalRoleEnum"], list[Union[str, "FunctionalRoleEnum"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxon_term):
            self.MissingRequiredField("taxon_term")
        if not isinstance(self.taxon_term, TaxonDescriptor):
            self.taxon_term = TaxonDescriptor(**as_dict(self.taxon_term))

        if self.strain_designation is not None and not isinstance(self.strain_designation, StrainDesignation):
            self.strain_designation = StrainDesignation(**as_dict(self.strain_designation))

        if self.abundance_level is not None and not isinstance(self.abundance_level, AbundanceEnum):
            self.abundance_level = AbundanceEnum(self.abundance_level)

        if self.abundance_value is not None and not isinstance(self.abundance_value, str):
            self.abundance_value = str(self.abundance_value)

        if not isinstance(self.functional_role, list):
            self.functional_role = [self.functional_role] if self.functional_role is not None else []
        self.functional_role = [v if isinstance(v, FunctionalRoleEnum) else FunctionalRoleEnum(v) for v in self.functional_role]

        self._normalize_inlined_as_dict(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InteractionDownstream(YAMLRoot):
    """
    A downstream target in a causal interaction graph
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["InteractionDownstream"]
    class_class_curie: ClassVar[str] = "communitymech:InteractionDownstream"
    class_name: ClassVar[str] = "InteractionDownstream"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.InteractionDownstream

    target: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EcologicalInteraction(YAMLRoot):
    """
    An interaction between organisms or metabolic processes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["EcologicalInteraction"]
    class_class_curie: ClassVar[str] = "communitymech:EcologicalInteraction"
    class_name: ClassVar[str] = "EcologicalInteraction"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.EcologicalInteraction

    name: str = None
    description: Optional[str] = None
    interaction_type: Optional[Union[str, "InteractionTypeEnum"]] = None
    source_taxon: Optional[Union[dict, TaxonDescriptor]] = None
    target_taxon: Optional[Union[dict, TaxonDescriptor]] = None
    metabolites: Optional[Union[Union[dict, MetaboliteDescriptor], list[Union[dict, MetaboliteDescriptor]]]] = empty_list()
    biological_processes: Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]] = empty_list()
    downstream: Optional[Union[Union[dict, InteractionDownstream], list[Union[dict, InteractionDownstream]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.interaction_type is not None and not isinstance(self.interaction_type, InteractionTypeEnum):
            self.interaction_type = InteractionTypeEnum(self.interaction_type)

        if self.source_taxon is not None and not isinstance(self.source_taxon, TaxonDescriptor):
            self.source_taxon = TaxonDescriptor(**as_dict(self.source_taxon))

        if self.target_taxon is not None and not isinstance(self.target_taxon, TaxonDescriptor):
            self.target_taxon = TaxonDescriptor(**as_dict(self.target_taxon))

        self._normalize_inlined_as_dict(slot_name="metabolites", slot_type=MetaboliteDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_dict(slot_name="biological_processes", slot_type=BiologicalProcessDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_dict(slot_name="downstream", slot_type=InteractionDownstream, key_name="target", keyed=False)

        self._normalize_inlined_as_dict(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentalFactor(YAMLRoot):
    """
    An environmental condition or parameter
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["EnvironmentalFactor"]
    class_class_curie: ClassVar[str] = "communitymech:EnvironmentalFactor"
    class_name: ClassVar[str] = "EnvironmentalFactor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.EnvironmentalFactor

    name: str = None
    value: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GrowthMediaComponent(YAMLRoot):
    """
    A component of growth media (nutrient, salt, buffer, etc.)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["GrowthMediaComponent"]
    class_class_curie: ClassVar[str] = "communitymech:GrowthMediaComponent"
    class_name: ClassVar[str] = "GrowthMediaComponent"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.GrowthMediaComponent

    name: str = None
    media_ingredient_mech_id: Optional[str] = None
    media_ingredient_mech_url: Optional[str] = None
    concentration: Optional[str] = None
    unit: Optional[str] = None
    chebi_term: Optional[Union[dict, MetaboliteDescriptor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.media_ingredient_mech_id is not None and not isinstance(self.media_ingredient_mech_id, str):
            self.media_ingredient_mech_id = str(self.media_ingredient_mech_id)

        if self.media_ingredient_mech_url is not None and not isinstance(self.media_ingredient_mech_url, str):
            self.media_ingredient_mech_url = str(self.media_ingredient_mech_url)

        if self.concentration is not None and not isinstance(self.concentration, str):
            self.concentration = str(self.concentration)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.chebi_term is not None and not isinstance(self.chebi_term, MetaboliteDescriptor):
            self.chebi_term = MetaboliteDescriptor(**as_dict(self.chebi_term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GrowthMedia(YAMLRoot):
    """
    Growth media used for cultivation of the community or its members
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["GrowthMedia"]
    class_class_curie: ClassVar[str] = "communitymech:GrowthMedia"
    class_name: ClassVar[str] = "GrowthMedia"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.GrowthMedia

    name: str = None
    culturemech_id: Optional[str] = None
    culturemech_url: Optional[str] = None
    composition: Optional[Union[Union[dict, GrowthMediaComponent], list[Union[dict, GrowthMediaComponent]]]] = empty_list()
    ph: Optional[str] = None
    ph_range: Optional[str] = None
    temperature: Optional[str] = None
    temperature_unit: Optional[str] = None
    temperature_range: Optional[str] = None
    atmosphere: Optional[Union[str, "AtmosphereEnum"]] = None
    headspace_gas: Optional[str] = None
    salinity: Optional[str] = None
    salinity_unit: Optional[str] = None
    pressure: Optional[str] = None
    pressure_unit: Optional[str] = None
    light_regime: Optional[str] = None
    light_intensity: Optional[str] = None
    light_intensity_unit: Optional[str] = None
    redox_potential: Optional[str] = None
    redox_potential_unit: Optional[str] = None
    inoculum_source: Optional[str] = None
    inoculum_size: Optional[str] = None
    inoculum_unit: Optional[str] = None
    incubation_time: Optional[str] = None
    incubation_time_unit: Optional[str] = None
    shaking_speed: Optional[str] = None
    shaking_speed_unit: Optional[str] = None
    vessel_type: Optional[str] = None
    preparation_notes: Optional[str] = None
    protocol_url: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.culturemech_id is not None and not isinstance(self.culturemech_id, str):
            self.culturemech_id = str(self.culturemech_id)

        if self.culturemech_url is not None and not isinstance(self.culturemech_url, str):
            self.culturemech_url = str(self.culturemech_url)

        self._normalize_inlined_as_dict(slot_name="composition", slot_type=GrowthMediaComponent, key_name="name", keyed=False)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.ph_range is not None and not isinstance(self.ph_range, str):
            self.ph_range = str(self.ph_range)

        if self.temperature is not None and not isinstance(self.temperature, str):
            self.temperature = str(self.temperature)

        if self.temperature_unit is not None and not isinstance(self.temperature_unit, str):
            self.temperature_unit = str(self.temperature_unit)

        if self.temperature_range is not None and not isinstance(self.temperature_range, str):
            self.temperature_range = str(self.temperature_range)

        if self.atmosphere is not None and not isinstance(self.atmosphere, AtmosphereEnum):
            self.atmosphere = AtmosphereEnum(self.atmosphere)

        if self.headspace_gas is not None and not isinstance(self.headspace_gas, str):
            self.headspace_gas = str(self.headspace_gas)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_unit is not None and not isinstance(self.salinity_unit, str):
            self.salinity_unit = str(self.salinity_unit)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.pressure_unit is not None and not isinstance(self.pressure_unit, str):
            self.pressure_unit = str(self.pressure_unit)

        if self.light_regime is not None and not isinstance(self.light_regime, str):
            self.light_regime = str(self.light_regime)

        if self.light_intensity is not None and not isinstance(self.light_intensity, str):
            self.light_intensity = str(self.light_intensity)

        if self.light_intensity_unit is not None and not isinstance(self.light_intensity_unit, str):
            self.light_intensity_unit = str(self.light_intensity_unit)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.redox_potential_unit is not None and not isinstance(self.redox_potential_unit, str):
            self.redox_potential_unit = str(self.redox_potential_unit)

        if self.inoculum_source is not None and not isinstance(self.inoculum_source, str):
            self.inoculum_source = str(self.inoculum_source)

        if self.inoculum_size is not None and not isinstance(self.inoculum_size, str):
            self.inoculum_size = str(self.inoculum_size)

        if self.inoculum_unit is not None and not isinstance(self.inoculum_unit, str):
            self.inoculum_unit = str(self.inoculum_unit)

        if self.incubation_time is not None and not isinstance(self.incubation_time, str):
            self.incubation_time = str(self.incubation_time)

        if self.incubation_time_unit is not None and not isinstance(self.incubation_time_unit, str):
            self.incubation_time_unit = str(self.incubation_time_unit)

        if self.shaking_speed is not None and not isinstance(self.shaking_speed, str):
            self.shaking_speed = str(self.shaking_speed)

        if self.shaking_speed_unit is not None and not isinstance(self.shaking_speed_unit, str):
            self.shaking_speed_unit = str(self.shaking_speed_unit)

        if self.vessel_type is not None and not isinstance(self.vessel_type, str):
            self.vessel_type = str(self.vessel_type)

        if self.preparation_notes is not None and not isinstance(self.preparation_notes, str):
            self.preparation_notes = str(self.preparation_notes)

        if self.protocol_url is not None and not isinstance(self.protocol_url, str):
            self.protocol_url = str(self.protocol_url)

        self._normalize_inlined_as_dict(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociatedDataset(YAMLRoot):
    """
    An omics or other dataset associated with the community
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["AssociatedDataset"]
    class_class_curie: ClassVar[str] = "communitymech:AssociatedDataset"
    class_name: ClassVar[str] = "AssociatedDataset"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.AssociatedDataset

    name: str = None
    dataset_type: Union[str, "DatasetTypeEnum"] = None
    accession: str = None
    repository: Optional[Union[str, "DatasetRepositoryEnum"]] = None
    url: Optional[str] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.dataset_type):
            self.MissingRequiredField("dataset_type")
        if not isinstance(self.dataset_type, DatasetTypeEnum):
            self.dataset_type = DatasetTypeEnum(self.dataset_type)

        if self._is_empty(self.accession):
            self.MissingRequiredField("accession")
        if not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.repository is not None and not isinstance(self.repository, DatasetRepositoryEnum):
            self.repository = DatasetRepositoryEnum(self.repository)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalResource(YAMLRoot):
    """
    An external model or narrative resource linked to the community
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["ExternalResource"]
    class_class_curie: ClassVar[str] = "communitymech:ExternalResource"
    class_name: ClassVar[str] = "ExternalResource"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.ExternalResource

    name: str = None
    repository: Union[str, "ExternalResourceRepositoryEnum"] = None
    resource_id: str = None
    url: str = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.repository):
            self.MissingRequiredField("repository")
        if not isinstance(self.repository, ExternalResourceRepositoryEnum):
            self.repository = ExternalResourceRepositoryEnum(self.repository)

        if self._is_empty(self.resource_id):
            self.MissingRequiredField("resource_id")
        if not isinstance(self.resource_id, str):
            self.resource_id = str(self.resource_id)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, str):
            self.url = str(self.url)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommunityEngineeringDesign(YAMLRoot):
    """
    Design intent and implementation details for engineered or synthetic communities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["CommunityEngineeringDesign"]
    class_class_curie: ClassVar[str] = "communitymech:CommunityEngineeringDesign"
    class_name: ClassVar[str] = "CommunityEngineeringDesign"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.CommunityEngineeringDesign

    objective: Optional[str] = None
    assembly_strategy: Optional[str] = None
    inoculation_strategy: Optional[str] = None
    passaging_regimen: Optional[str] = None
    perturbation_design: Optional[str] = None
    measurement_endpoints: Optional[Union[str, list[str]]] = empty_list()
    protocol_url: Optional[str] = None
    notes: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.objective is not None and not isinstance(self.objective, str):
            self.objective = str(self.objective)

        if self.assembly_strategy is not None and not isinstance(self.assembly_strategy, str):
            self.assembly_strategy = str(self.assembly_strategy)

        if self.inoculation_strategy is not None and not isinstance(self.inoculation_strategy, str):
            self.inoculation_strategy = str(self.inoculation_strategy)

        if self.passaging_regimen is not None and not isinstance(self.passaging_regimen, str):
            self.passaging_regimen = str(self.passaging_regimen)

        if self.perturbation_design is not None and not isinstance(self.perturbation_design, str):
            self.perturbation_design = str(self.perturbation_design)

        if not isinstance(self.measurement_endpoints, list):
            self.measurement_endpoints = [self.measurement_endpoints] if self.measurement_endpoints is not None else []
        self.measurement_endpoints = [v if isinstance(v, str) else str(v) for v in self.measurement_endpoints]

        if self.protocol_url is not None and not isinstance(self.protocol_url, str):
            self.protocol_url = str(self.protocol_url)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_dict(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MicrobialCommunity(YAMLRoot):
    """
    A microbial community with composition and interactions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["MicrobialCommunity"]
    class_class_curie: ClassVar[str] = "communitymech:MicrobialCommunity"
    class_name: ClassVar[str] = "MicrobialCommunity"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.MicrobialCommunity

    id: Union[str, MicrobialCommunityId] = None
    name: str = None
    description: Optional[str] = None
    ecological_state: Optional[Union[str, "EcologicalStateEnum"]] = None
    community_origin: Optional[Union[str, "CommunityOriginEnum"]] = None
    community_category: Optional[Union[str, "CommunityCategoryEnum"]] = None
    engineering_design: Optional[Union[dict, CommunityEngineeringDesign]] = None
    environment_term: Optional[Union[dict, EnvironmentDescriptor]] = None
    taxonomy: Optional[Union[Union[dict, TaxonomicComposition], list[Union[dict, TaxonomicComposition]]]] = empty_list()
    ecological_interactions: Optional[Union[Union[dict, EcologicalInteraction], list[Union[dict, EcologicalInteraction]]]] = empty_list()
    environmental_factors: Optional[Union[Union[dict, EnvironmentalFactor], list[Union[dict, EnvironmentalFactor]]]] = empty_list()
    growth_media: Optional[Union[Union[dict, GrowthMedia], list[Union[dict, GrowthMedia]]]] = empty_list()
    associated_datasets: Optional[Union[Union[dict, AssociatedDataset], list[Union[dict, AssociatedDataset]]]] = empty_list()
    external_resources: Optional[Union[Union[dict, ExternalResource], list[Union[dict, ExternalResource]]]] = empty_list()
    metals_present: Optional[Union[Union[str, "MetalElementEnum"], list[Union[str, "MetalElementEnum"]]]] = empty_list()
    rare_earth_elements_present: Optional[Union[Union[str, "RareEarthElementEnum"], list[Union[str, "RareEarthElementEnum"]]]] = empty_list()
    metal_relevance: Optional[Union[str, "MetalRelevanceEnum"]] = None
    metal_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicrobialCommunityId):
            self.id = MicrobialCommunityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ecological_state is not None and not isinstance(self.ecological_state, EcologicalStateEnum):
            self.ecological_state = EcologicalStateEnum(self.ecological_state)

        if self.community_origin is not None and not isinstance(self.community_origin, CommunityOriginEnum):
            self.community_origin = CommunityOriginEnum(self.community_origin)

        if self.community_category is not None and not isinstance(self.community_category, CommunityCategoryEnum):
            self.community_category = CommunityCategoryEnum(self.community_category)

        if self.engineering_design is not None and not isinstance(self.engineering_design, CommunityEngineeringDesign):
            self.engineering_design = CommunityEngineeringDesign(**as_dict(self.engineering_design))

        if self.environment_term is not None and not isinstance(self.environment_term, EnvironmentDescriptor):
            self.environment_term = EnvironmentDescriptor(**as_dict(self.environment_term))

        self._normalize_inlined_as_dict(slot_name="taxonomy", slot_type=TaxonomicComposition, key_name="taxon_term", keyed=False)

        self._normalize_inlined_as_dict(slot_name="ecological_interactions", slot_type=EcologicalInteraction, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="environmental_factors", slot_type=EnvironmentalFactor, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="growth_media", slot_type=GrowthMedia, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="associated_datasets", slot_type=AssociatedDataset, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="external_resources", slot_type=ExternalResource, key_name="name", keyed=False)

        if not isinstance(self.metals_present, list):
            self.metals_present = [self.metals_present] if self.metals_present is not None else []
        self.metals_present = [v if isinstance(v, MetalElementEnum) else MetalElementEnum(v) for v in self.metals_present]

        if not isinstance(self.rare_earth_elements_present, list):
            self.rare_earth_elements_present = [self.rare_earth_elements_present] if self.rare_earth_elements_present is not None else []
        self.rare_earth_elements_present = [v if isinstance(v, RareEarthElementEnum) else RareEarthElementEnum(v) for v in self.rare_earth_elements_present]

        if self.metal_relevance is not None and not isinstance(self.metal_relevance, MetalRelevanceEnum):
            self.metal_relevance = MetalRelevanceEnum(self.metal_relevance)

        if self.metal_notes is not None and not isinstance(self.metal_notes, str):
            self.metal_notes = str(self.metal_notes)

        super().__post_init__(**kwargs)


# Enumerations
class EvidenceItemSupportEnum(EnumDefinitionImpl):
    """
    The level of support for an evidence item
    """
    SUPPORT = PermissibleValue(
        text="SUPPORT",
        description="Evidence supports the claim")
    REFUTE = PermissibleValue(
        text="REFUTE",
        description="Evidence refutes the claim")
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        description="Evidence partially supports the claim")
    NO_EVIDENCE = PermissibleValue(
        text="NO_EVIDENCE",
        description="No evidence found")
    WRONG_STATEMENT = PermissibleValue(
        text="WRONG_STATEMENT",
        description="Statement is incorrect")

    _defn = EnumDefinition(
        name="EvidenceItemSupportEnum",
        description="The level of support for an evidence item",
    )

class EvidenceSourceEnum(EnumDefinitionImpl):
    """
    The provenance/source of the evidence
    """
    IN_VITRO = PermissibleValue(
        text="IN_VITRO",
        description="In vitro experiments (batch culture, bioreactor, etc.)")
    IN_VIVO = PermissibleValue(
        text="IN_VIVO",
        description="In vivo experiments (field studies, host-associated, etc.)")
    COMPUTATIONAL = PermissibleValue(
        text="COMPUTATIONAL",
        description="In silico modeling, simulation, or prediction")
    REVIEW = PermissibleValue(
        text="REVIEW",
        description="Review article or meta-analysis")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other evidence type")

    _defn = EnumDefinition(
        name="EvidenceSourceEnum",
        description="The provenance/source of the evidence",
    )

class EcologicalStateEnum(EnumDefinitionImpl):
    """
    The ecological or health state of the community
    """
    STABLE = PermissibleValue(
        text="STABLE",
        description="Stable, equilibrium community")
    PERTURBED = PermissibleValue(
        text="PERTURBED",
        description="Recently perturbed (e.g., antibiotic treatment)")
    ENGINEERED = PermissibleValue(
        text="ENGINEERED",
        description="Synthetic or engineered community")
    TRANSIENT = PermissibleValue(
        text="TRANSIENT",
        description="Transient or developing community")

    _defn = EnumDefinition(
        name="EcologicalStateEnum",
        description="The ecological or health state of the community",
    )

class CommunityOriginEnum(EnumDefinitionImpl):
    """
    The origin or source of the community
    """
    NATURAL = PermissibleValue(
        text="NATURAL",
        description="Naturally occurring community from environment")
    ENGINEERED = PermissibleValue(
        text="ENGINEERED",
        description="Deliberately engineered or synthetic community")
    SYNTHETIC = PermissibleValue(
        text="SYNTHETIC",
        description="Fully synthetic community designed in laboratory")

    _defn = EnumDefinition(
        name="CommunityOriginEnum",
        description="The origin or source of the community",
    )

class CommunityCategoryEnum(EnumDefinitionImpl):
    """
    Broad functional/ecological category of the community
    """
    BIOMINING = PermissibleValue(
        text="BIOMINING",
        description="Metal extraction and bioleaching systems")
    AMD = PermissibleValue(
        text="AMD",
        description="Acid mine drainage communities")
    SYNTROPHY = PermissibleValue(
        text="SYNTROPHY",
        description="Syntrophic metabolic cooperation")
    PHYTOPLANKTON = PermissibleValue(
        text="PHYTOPLANKTON",
        description="Algae-bacteria associations")
    RHIZOSPHERE = PermissibleValue(
        text="RHIZOSPHERE",
        description="Plant root-associated communities")
    LIGNOCELLULOSE = PermissibleValue(
        text="LIGNOCELLULOSE",
        description="Lignocellulose degradation systems")
    METHANOGENESIS = PermissibleValue(
        text="METHANOGENESIS",
        description="Methane-producing communities")
    DIET = PermissibleValue(
        text="DIET",
        description="Direct interspecies electron transfer")
    METAL_REDUCTION = PermissibleValue(
        text="METAL_REDUCTION",
        description="Metal-reducing communities")
    BIOREMEDIATION = PermissibleValue(
        text="BIOREMEDIATION",
        description="Pollutant degradation and remediation")
    CARBON_SEQUESTRATION = PermissibleValue(
        text="CARBON_SEQUESTRATION",
        description="Carbon fixation and storage")
    EXTREME_ENVIRONMENT = PermissibleValue(
        text="EXTREME_ENVIRONMENT",
        description="Communities from extreme conditions")
    BIOTECHNOLOGY = PermissibleValue(
        text="BIOTECHNOLOGY",
        description="Industrial biotechnology applications")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other or uncategorized communities")

    _defn = EnumDefinition(
        name="CommunityCategoryEnum",
        description="Broad functional/ecological category of the community",
    )

class InteractionTypeEnum(EnumDefinitionImpl):
    """
    Type of ecological interaction between organisms
    """
    MUTUALISM = PermissibleValue(
        text="MUTUALISM",
        description="Both organisms benefit (+/+)")
    COMMENSALISM = PermissibleValue(
        text="COMMENSALISM",
        description="One benefits, other unaffected (+/0)")
    CROSS_FEEDING = PermissibleValue(
        text="CROSS_FEEDING",
        description="Metabolite exchange between organisms")
    COMPETITION = PermissibleValue(
        text="COMPETITION",
        description="Both negatively affected (-/-)")
    PREDATION = PermissibleValue(
        text="PREDATION",
        description="One benefits, other harmed (+/-)")
    SYNTROPHY = PermissibleValue(
        text="SYNTROPHY",
        description="Obligate metabolic cooperation")
    NICHE_PARTITIONING = PermissibleValue(
        text="NICHE_PARTITIONING",
        description="""Strains/species occupy distinct ecological niches, reducing competition through spatial or temporal separation""")
    STRAIN_COMPETITION = PermissibleValue(
        text="STRAIN_COMPETITION",
        description="Intraspecific competition between closely related strains of the same species")
    COLONIZATION_FACILITATION = PermissibleValue(
        text="COLONIZATION_FACILITATION",
        description="""One organism facilitates the colonization or establishment of another through priority effects or niche modification""")

    _defn = EnumDefinition(
        name="InteractionTypeEnum",
        description="Type of ecological interaction between organisms",
    )

class AbundanceEnum(EnumDefinitionImpl):
    """
    Relative abundance categories
    """
    DOMINANT = PermissibleValue(
        text="DOMINANT",
        description="Greater than 1% relative abundance")
    ABUNDANT = PermissibleValue(
        text="ABUNDANT",
        description="0.1-1% relative abundance")
    COMMON = PermissibleValue(
        text="COMMON",
        description="0.01-0.1% relative abundance")
    RARE = PermissibleValue(
        text="RARE",
        description="Less than 0.01% relative abundance")

    _defn = EnumDefinition(
        name="AbundanceEnum",
        description="Relative abundance categories",
    )

class FunctionalRoleEnum(EnumDefinitionImpl):
    """
    Functional role in the community
    """
    PRIMARY_PRODUCER = PermissibleValue(
        text="PRIMARY_PRODUCER",
        description="Fixes carbon (autotroph)")
    PRIMARY_DEGRADER = PermissibleValue(
        text="PRIMARY_DEGRADER",
        description="Degrades complex substrates")
    SECONDARY_FERMENTER = PermissibleValue(
        text="SECONDARY_FERMENTER",
        description="Ferments products from primary degraders")
    SYNTROPHIC_PARTNER = PermissibleValue(
        text="SYNTROPHIC_PARTNER",
        description="Engages in syntrophic metabolism")
    CROSS_FEEDER = PermissibleValue(
        text="CROSS_FEEDER",
        description="Utilizes metabolites from other taxa")

    _defn = EnumDefinition(
        name="FunctionalRoleEnum",
        description="Functional role in the community",
    )

class AtmosphereEnum(EnumDefinitionImpl):
    """
    Atmospheric/oxygen requirements for growth
    """
    AEROBIC = PermissibleValue(
        text="AEROBIC",
        description="Requires oxygen for growth")
    ANAEROBIC = PermissibleValue(
        text="ANAEROBIC",
        description="Growth only in absence of oxygen (strict anaerobe)")
    MICROAEROBIC = PermissibleValue(
        text="MICROAEROBIC",
        description="Requires low oxygen levels (typically 2-10%)")
    FACULTATIVE_ANAEROBIC = PermissibleValue(
        text="FACULTATIVE_ANAEROBIC",
        description="Can grow with or without oxygen")
    FACULTATIVE_AEROBIC = PermissibleValue(
        text="FACULTATIVE_AEROBIC",
        description="Preferentially aerobic but can grow anaerobically")
    CAPNOPHILIC = PermissibleValue(
        text="CAPNOPHILIC",
        description="Requires elevated CO2 levels")

    _defn = EnumDefinition(
        name="AtmosphereEnum",
        description="Atmospheric/oxygen requirements for growth",
    )

class DatasetTypeEnum(EnumDefinitionImpl):
    """
    Type of omics or other dataset associated with a community
    """
    METAGENOME = PermissibleValue(
        text="METAGENOME",
        description="Shotgun metagenomic sequencing")
    AMPLICON_16S = PermissibleValue(
        text="AMPLICON_16S",
        description="16S rRNA amplicon sequencing")
    AMPLICON_ITS = PermissibleValue(
        text="AMPLICON_ITS",
        description="ITS amplicon sequencing (fungal)")
    METATRANSCRIPTOME = PermissibleValue(
        text="METATRANSCRIPTOME",
        description="Metatranscriptomic sequencing")
    METAPROTEOME = PermissibleValue(
        text="METAPROTEOME",
        description="Metaproteomic analysis")
    METABOLOMICS = PermissibleValue(
        text="METABOLOMICS",
        description="Metabolomics (LC-MS, GC-MS, etc.)")
    GENOME = PermissibleValue(
        text="GENOME",
        description="Isolate whole genome sequencing")
    PHENOTYPE = PermissibleValue(
        text="PHENOTYPE",
        description="Phenotypic measurements (growth, imaging, etc.)")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other dataset type")

    _defn = EnumDefinition(
        name="DatasetTypeEnum",
        description="Type of omics or other dataset associated with a community",
    )

class DatasetRepositoryEnum(EnumDefinitionImpl):
    """
    Data repositories for omics and related datasets
    """
    NCBI_SRA = PermissibleValue(
        text="NCBI_SRA",
        description="NCBI Sequence Read Archive")
    NCBI_BIOPROJECT = PermissibleValue(
        text="NCBI_BIOPROJECT",
        description="NCBI BioProject")
    NMDC = PermissibleValue(
        text="NMDC",
        description="National Microbiome Data Collaborative")
    JGI_GOLD = PermissibleValue(
        text="JGI_GOLD",
        description="JGI Genomes OnLine Database")
    JGI_IMG = PermissibleValue(
        text="JGI_IMG",
        description="JGI Integrated Microbial Genomes")
    MGNIFY = PermissibleValue(
        text="MGNIFY",
        description="MGnify (EBI metagenomics)")
    METABOLOMICS_WORKBENCH = PermissibleValue(
        text="METABOLOMICS_WORKBENCH",
        description="Metabolomics Workbench")
    MASSIVE = PermissibleValue(
        text="MASSIVE",
        description="MassIVE mass spectrometry data")
    GNPS = PermissibleValue(
        text="GNPS",
        description="Global Natural Products Social Molecular Networking")
    FIGSHARE = PermissibleValue(
        text="FIGSHARE",
        description="Figshare data repository")
    ZENODO = PermissibleValue(
        text="ZENODO",
        description="Zenodo data repository")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other data repository")

    _defn = EnumDefinition(
        name="DatasetRepositoryEnum",
        description="Data repositories for omics and related datasets",
    )

class ExternalResourceRepositoryEnum(EnumDefinitionImpl):
    """
    External repositories and platforms that host community model resources
    """
    BIOMODELS = PermissibleValue(
        text="BIOMODELS",
        description="BioModels database")
    KBASE = PermissibleValue(
        text="KBASE",
        description="KBase Narrative platform")
    BIGG = PermissibleValue(
        text="BIGG",
        description="BiGG Models")
    VMH = PermissibleValue(
        text="VMH",
        description="Virtual Metabolic Human")
    MODELSEED = PermissibleValue(
        text="MODELSEED",
        description="ModelSEED resources")
    GITHUB = PermissibleValue(
        text="GITHUB",
        description="GitHub repository")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other resource repository")

    _defn = EnumDefinition(
        name="ExternalResourceRepositoryEnum",
        description="External repositories and platforms that host community model resources",
    )

class CultureCollectionEnum(EnumDefinitionImpl):
    """
    Major microbial culture collections worldwide
    """
    ATCC = PermissibleValue(
        text="ATCC",
        description="American Type Culture Collection (USA)")
    DSM = PermissibleValue(
        text="DSM",
        description="Deutsche Sammlung von Mikroorganismen (DSMZ, Germany)")
    JCM = PermissibleValue(
        text="JCM",
        description="Japan Collection of Microorganisms (Japan)")
    NCTC = PermissibleValue(
        text="NCTC",
        description="National Collection of Type Cultures (UK)")
    CCUG = PermissibleValue(
        text="CCUG",
        description="Culture Collection University of Gothenburg (Sweden)")
    PCC = PermissibleValue(
        text="PCC",
        description="Pasteur Culture Collection of Cyanobacteria (France)")
    NCIMB = PermissibleValue(
        text="NCIMB",
        description="National Collection of Industrial Marine Bacteria (UK)")
    LMG = PermissibleValue(
        text="LMG",
        description="BCCM/LMG Bacteria Collection (Belgium)")
    KCTC = PermissibleValue(
        text="KCTC",
        description="Korean Collection for Type Cultures (Korea)")
    CIP = PermissibleValue(
        text="CIP",
        description="Collection de l'Institut Pasteur (France)")
    NBRC = PermissibleValue(
        text="NBRC",
        description="NITE Biological Resource Center (Japan)")
    VKM = PermissibleValue(
        text="VKM",
        description="All-Russian Collection of Microorganisms (Russia)")
    CGMCC = PermissibleValue(
        text="CGMCC",
        description="China General Microbiological Culture Collection (China)")
    BCRC = PermissibleValue(
        text="BCRC",
        description="Bioresource Collection and Research Center (Taiwan)")
    CBS = PermissibleValue(
        text="CBS",
        description="Westerdijk Fungal Biodiversity Institute (Netherlands)")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other culture collection not listed")

    _defn = EnumDefinition(
        name="CultureCollectionEnum",
        description="Major microbial culture collections worldwide",
    )

class MetalElementEnum(EnumDefinitionImpl):
    """
    Metal elements relevant to microbial communities
    """
    COPPER = PermissibleValue(
        text="COPPER",
        description="Copper(2+) cation",
        meaning=CHEBI["29036"])
    IRON = PermissibleValue(
        text="IRON",
        description="Iron(2+) cation",
        meaning=CHEBI["29033"])
    ZINC = PermissibleValue(
        text="ZINC",
        description="Zinc(2+) cation",
        meaning=CHEBI["27363"])
    NICKEL = PermissibleValue(
        text="NICKEL",
        description="Nickel(2+) cation",
        meaning=CHEBI["49786"])
    COBALT = PermissibleValue(
        text="COBALT",
        description="Cobalt(2+) cation",
        meaning=CHEBI["48828"])
    VANADIUM = PermissibleValue(
        text="VANADIUM",
        description="Vanadium cation",
        meaning=CHEBI["27698"])
    URANIUM = PermissibleValue(
        text="URANIUM",
        description="Uranium atom",
        meaning=CHEBI["27214"])
    CHROMIUM = PermissibleValue(
        text="CHROMIUM",
        description="Chromium atom",
        meaning=CHEBI["28073"])
    LEAD = PermissibleValue(
        text="LEAD",
        description="Lead(2+) cation",
        meaning=CHEBI["25016"])
    LITHIUM = PermissibleValue(
        text="LITHIUM",
        description="Lithium(1+) cation",
        meaning=CHEBI["49713"])
    GOLD = PermissibleValue(
        text="GOLD",
        description="Gold atom",
        meaning=CHEBI["29287"])
    SILVER = PermissibleValue(
        text="SILVER",
        description="Silver(1+) cation",
        meaning=CHEBI["30512"])
    PALLADIUM = PermissibleValue(
        text="PALLADIUM",
        description="Palladium atom",
        meaning=CHEBI["33373"])
    GALLIUM = PermissibleValue(
        text="GALLIUM",
        description="Gallium(3+) cation",
        meaning=CHEBI["49631"])
    INDIUM = PermissibleValue(
        text="INDIUM",
        description="Indium(3+) cation",
        meaning=CHEBI["49464"])
    TITANIUM = PermissibleValue(
        text="TITANIUM",
        description="Titanium atom",
        meaning=CHEBI["33341"])

    _defn = EnumDefinition(
        name="MetalElementEnum",
        description="Metal elements relevant to microbial communities",
    )

class RareEarthElementEnum(EnumDefinitionImpl):
    """
    Rare earth elements (lanthanides + Y, Sc)
    """
    LANTHANUM = PermissibleValue(
        text="LANTHANUM",
        description="Lanthanum(3+) cation",
        meaning=CHEBI["32359"])
    CERIUM = PermissibleValue(
        text="CERIUM",
        description="Cerium(3+) cation",
        meaning=CHEBI["32998"])
    PRASEODYMIUM = PermissibleValue(
        text="PRASEODYMIUM",
        description="Praseodymium(3+) cation",
        meaning=CHEBI["49648"])
    NEODYMIUM = PermissibleValue(
        text="NEODYMIUM",
        description="Neodymium(3+) cation",
        meaning=CHEBI["33372"])
    SAMARIUM = PermissibleValue(
        text="SAMARIUM",
        description="Samarium(3+) cation",
        meaning=CHEBI["33376"])
    EUROPIUM = PermissibleValue(
        text="EUROPIUM",
        description="Europium(3+) cation",
        meaning=CHEBI["30688"])
    GADOLINIUM = PermissibleValue(
        text="GADOLINIUM",
        description="Gadolinium(3+) cation",
        meaning=CHEBI["33375"])
    TERBIUM = PermissibleValue(
        text="TERBIUM",
        description="Terbium(3+) cation",
        meaning=CHEBI["33374"])
    DYSPROSIUM = PermissibleValue(
        text="DYSPROSIUM",
        description="Dysprosium(3+) cation",
        meaning=CHEBI["49782"])
    HOLMIUM = PermissibleValue(
        text="HOLMIUM",
        description="Holmium(3+) cation",
        meaning=CHEBI["49649"])
    ERBIUM = PermissibleValue(
        text="ERBIUM",
        description="Erbium(3+) cation",
        meaning=CHEBI["49650"])
    THULIUM = PermissibleValue(
        text="THULIUM",
        description="Thulium(3+) cation",
        meaning=CHEBI["33377"])
    YTTERBIUM = PermissibleValue(
        text="YTTERBIUM",
        description="Ytterbium(3+) cation",
        meaning=CHEBI["33378"])
    LUTETIUM = PermissibleValue(
        text="LUTETIUM",
        description="Lutetium(3+) cation",
        meaning=CHEBI["33382"])
    YTTRIUM = PermissibleValue(
        text="YTTRIUM",
        description="Yttrium(3+) cation",
        meaning=CHEBI["49976"])
    SCANDIUM = PermissibleValue(
        text="SCANDIUM",
        description="Scandium(3+) cation",
        meaning=CHEBI["33330"])

    _defn = EnumDefinition(
        name="RareEarthElementEnum",
        description="Rare earth elements (lanthanides + Y, Sc)",
    )

class MetalRelevanceEnum(EnumDefinitionImpl):
    """
    Relevance of metals/REE to community function
    """
    PRIMARY = PermissibleValue(
        text="PRIMARY",
        description="Primary function involves metal/REE extraction or cycling")
    SIGNIFICANT = PermissibleValue(
        text="SIGNIFICANT",
        description="Significant metal/REE metabolism but not primary function")
    INCIDENTAL = PermissibleValue(
        text="INCIDENTAL",
        description="Incidental metal/REE interaction")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        description="No significant metal/REE relevance")

    _defn = EnumDefinition(
        name="MetalRelevanceEnum",
        description="Relevance of metals/REE to community function",
    )

# Slots
class slots:
    pass

slots.term__id = Slot(uri=COMMUNITYMECH.id, name="term__id", curie=COMMUNITYMECH.curie('id'),
                   model_uri=COMMUNITYMECH.term__id, domain=None, range=str)

slots.term__label = Slot(uri=COMMUNITYMECH.label, name="term__label", curie=COMMUNITYMECH.curie('label'),
                   model_uri=COMMUNITYMECH.term__label, domain=None, range=str)

slots.evidenceItem__reference = Slot(uri=COMMUNITYMECH.reference, name="evidenceItem__reference", curie=COMMUNITYMECH.curie('reference'),
                   model_uri=COMMUNITYMECH.evidenceItem__reference, domain=None, range=str,
                   pattern=re.compile(r'^(PMID:|doi:|bioproject:).*'))

slots.evidenceItem__supports = Slot(uri=COMMUNITYMECH.supports, name="evidenceItem__supports", curie=COMMUNITYMECH.curie('supports'),
                   model_uri=COMMUNITYMECH.evidenceItem__supports, domain=None, range=Union[str, "EvidenceItemSupportEnum"])

slots.evidenceItem__evidence_source = Slot(uri=COMMUNITYMECH.evidence_source, name="evidenceItem__evidence_source", curie=COMMUNITYMECH.curie('evidence_source'),
                   model_uri=COMMUNITYMECH.evidenceItem__evidence_source, domain=None, range=Union[str, "EvidenceSourceEnum"])

slots.evidenceItem__snippet = Slot(uri=COMMUNITYMECH.snippet, name="evidenceItem__snippet", curie=COMMUNITYMECH.curie('snippet'),
                   model_uri=COMMUNITYMECH.evidenceItem__snippet, domain=None, range=str)

slots.evidenceItem__explanation = Slot(uri=COMMUNITYMECH.explanation, name="evidenceItem__explanation", curie=COMMUNITYMECH.curie('explanation'),
                   model_uri=COMMUNITYMECH.evidenceItem__explanation, domain=None, range=Optional[str])

slots.evidenceItem__confidence_score = Slot(uri=COMMUNITYMECH.confidence_score, name="evidenceItem__confidence_score", curie=COMMUNITYMECH.curie('confidence_score'),
                   model_uri=COMMUNITYMECH.evidenceItem__confidence_score, domain=None, range=Optional[float])

slots.taxonDescriptor__preferred_term = Slot(uri=COMMUNITYMECH.preferred_term, name="taxonDescriptor__preferred_term", curie=COMMUNITYMECH.curie('preferred_term'),
                   model_uri=COMMUNITYMECH.taxonDescriptor__preferred_term, domain=None, range=str)

slots.taxonDescriptor__term = Slot(uri=COMMUNITYMECH.term, name="taxonDescriptor__term", curie=COMMUNITYMECH.curie('term'),
                   model_uri=COMMUNITYMECH.taxonDescriptor__term, domain=None, range=Union[dict, Term])

slots.taxonDescriptor__notes = Slot(uri=COMMUNITYMECH.notes, name="taxonDescriptor__notes", curie=COMMUNITYMECH.curie('notes'),
                   model_uri=COMMUNITYMECH.taxonDescriptor__notes, domain=None, range=Optional[str])

slots.metaboliteDescriptor__preferred_term = Slot(uri=COMMUNITYMECH.preferred_term, name="metaboliteDescriptor__preferred_term", curie=COMMUNITYMECH.curie('preferred_term'),
                   model_uri=COMMUNITYMECH.metaboliteDescriptor__preferred_term, domain=None, range=str)

slots.metaboliteDescriptor__term = Slot(uri=COMMUNITYMECH.term, name="metaboliteDescriptor__term", curie=COMMUNITYMECH.curie('term'),
                   model_uri=COMMUNITYMECH.metaboliteDescriptor__term, domain=None, range=Union[dict, Term])

slots.metaboliteDescriptor__concentration = Slot(uri=COMMUNITYMECH.concentration, name="metaboliteDescriptor__concentration", curie=COMMUNITYMECH.curie('concentration'),
                   model_uri=COMMUNITYMECH.metaboliteDescriptor__concentration, domain=None, range=Optional[str])

slots.metaboliteDescriptor__notes = Slot(uri=COMMUNITYMECH.notes, name="metaboliteDescriptor__notes", curie=COMMUNITYMECH.curie('notes'),
                   model_uri=COMMUNITYMECH.metaboliteDescriptor__notes, domain=None, range=Optional[str])

slots.biologicalProcessDescriptor__preferred_term = Slot(uri=COMMUNITYMECH.preferred_term, name="biologicalProcessDescriptor__preferred_term", curie=COMMUNITYMECH.curie('preferred_term'),
                   model_uri=COMMUNITYMECH.biologicalProcessDescriptor__preferred_term, domain=None, range=str)

slots.biologicalProcessDescriptor__term = Slot(uri=COMMUNITYMECH.term, name="biologicalProcessDescriptor__term", curie=COMMUNITYMECH.curie('term'),
                   model_uri=COMMUNITYMECH.biologicalProcessDescriptor__term, domain=None, range=Union[dict, Term])

slots.biologicalProcessDescriptor__notes = Slot(uri=COMMUNITYMECH.notes, name="biologicalProcessDescriptor__notes", curie=COMMUNITYMECH.curie('notes'),
                   model_uri=COMMUNITYMECH.biologicalProcessDescriptor__notes, domain=None, range=Optional[str])

slots.environmentDescriptor__preferred_term = Slot(uri=COMMUNITYMECH.preferred_term, name="environmentDescriptor__preferred_term", curie=COMMUNITYMECH.curie('preferred_term'),
                   model_uri=COMMUNITYMECH.environmentDescriptor__preferred_term, domain=None, range=str)

slots.environmentDescriptor__term = Slot(uri=COMMUNITYMECH.term, name="environmentDescriptor__term", curie=COMMUNITYMECH.curie('term'),
                   model_uri=COMMUNITYMECH.environmentDescriptor__term, domain=None, range=Union[dict, Term])

slots.environmentDescriptor__notes = Slot(uri=COMMUNITYMECH.notes, name="environmentDescriptor__notes", curie=COMMUNITYMECH.curie('notes'),
                   model_uri=COMMUNITYMECH.environmentDescriptor__notes, domain=None, range=Optional[str])

slots.cultureCollectionID__collection = Slot(uri=COMMUNITYMECH.collection, name="cultureCollectionID__collection", curie=COMMUNITYMECH.curie('collection'),
                   model_uri=COMMUNITYMECH.cultureCollectionID__collection, domain=None, range=Union[str, "CultureCollectionEnum"])

slots.cultureCollectionID__accession = Slot(uri=COMMUNITYMECH.accession, name="cultureCollectionID__accession", curie=COMMUNITYMECH.curie('accession'),
                   model_uri=COMMUNITYMECH.cultureCollectionID__accession, domain=None, range=str)

slots.cultureCollectionID__url = Slot(uri=COMMUNITYMECH.url, name="cultureCollectionID__url", curie=COMMUNITYMECH.curie('url'),
                   model_uri=COMMUNITYMECH.cultureCollectionID__url, domain=None, range=Optional[str])

slots.cultureCollectionID__notes = Slot(uri=COMMUNITYMECH.notes, name="cultureCollectionID__notes", curie=COMMUNITYMECH.curie('notes'),
                   model_uri=COMMUNITYMECH.cultureCollectionID__notes, domain=None, range=Optional[str])

slots.strainDesignation__strain_name = Slot(uri=COMMUNITYMECH.strain_name, name="strainDesignation__strain_name", curie=COMMUNITYMECH.curie('strain_name'),
                   model_uri=COMMUNITYMECH.strainDesignation__strain_name, domain=None, range=Optional[str])

slots.strainDesignation__culture_collections = Slot(uri=COMMUNITYMECH.culture_collections, name="strainDesignation__culture_collections", curie=COMMUNITYMECH.curie('culture_collections'),
                   model_uri=COMMUNITYMECH.strainDesignation__culture_collections, domain=None, range=Optional[Union[Union[dict, CultureCollectionID], list[Union[dict, CultureCollectionID]]]])

slots.strainDesignation__type_strain = Slot(uri=COMMUNITYMECH.type_strain, name="strainDesignation__type_strain", curie=COMMUNITYMECH.curie('type_strain'),
                   model_uri=COMMUNITYMECH.strainDesignation__type_strain, domain=None, range=Optional[Union[bool, Bool]])

slots.strainDesignation__genome_accession = Slot(uri=COMMUNITYMECH.genome_accession, name="strainDesignation__genome_accession", curie=COMMUNITYMECH.curie('genome_accession'),
                   model_uri=COMMUNITYMECH.strainDesignation__genome_accession, domain=None, range=Optional[str])

slots.strainDesignation__genome_url = Slot(uri=COMMUNITYMECH.genome_url, name="strainDesignation__genome_url", curie=COMMUNITYMECH.curie('genome_url'),
                   model_uri=COMMUNITYMECH.strainDesignation__genome_url, domain=None, range=Optional[str])

slots.strainDesignation__genetic_modification = Slot(uri=COMMUNITYMECH.genetic_modification, name="strainDesignation__genetic_modification", curie=COMMUNITYMECH.curie('genetic_modification'),
                   model_uri=COMMUNITYMECH.strainDesignation__genetic_modification, domain=None, range=Optional[str])

slots.strainDesignation__isolation_source = Slot(uri=COMMUNITYMECH.isolation_source, name="strainDesignation__isolation_source", curie=COMMUNITYMECH.curie('isolation_source'),
                   model_uri=COMMUNITYMECH.strainDesignation__isolation_source, domain=None, range=Optional[str])

slots.strainDesignation__notes = Slot(uri=COMMUNITYMECH.notes, name="strainDesignation__notes", curie=COMMUNITYMECH.curie('notes'),
                   model_uri=COMMUNITYMECH.strainDesignation__notes, domain=None, range=Optional[str])

slots.taxonomicComposition__taxon_term = Slot(uri=COMMUNITYMECH.taxon_term, name="taxonomicComposition__taxon_term", curie=COMMUNITYMECH.curie('taxon_term'),
                   model_uri=COMMUNITYMECH.taxonomicComposition__taxon_term, domain=None, range=Union[dict, TaxonDescriptor])

slots.taxonomicComposition__strain_designation = Slot(uri=COMMUNITYMECH.strain_designation, name="taxonomicComposition__strain_designation", curie=COMMUNITYMECH.curie('strain_designation'),
                   model_uri=COMMUNITYMECH.taxonomicComposition__strain_designation, domain=None, range=Optional[Union[dict, StrainDesignation]])

slots.taxonomicComposition__abundance_level = Slot(uri=COMMUNITYMECH.abundance_level, name="taxonomicComposition__abundance_level", curie=COMMUNITYMECH.curie('abundance_level'),
                   model_uri=COMMUNITYMECH.taxonomicComposition__abundance_level, domain=None, range=Optional[Union[str, "AbundanceEnum"]])

slots.taxonomicComposition__abundance_value = Slot(uri=COMMUNITYMECH.abundance_value, name="taxonomicComposition__abundance_value", curie=COMMUNITYMECH.curie('abundance_value'),
                   model_uri=COMMUNITYMECH.taxonomicComposition__abundance_value, domain=None, range=Optional[str])

slots.taxonomicComposition__functional_role = Slot(uri=COMMUNITYMECH.functional_role, name="taxonomicComposition__functional_role", curie=COMMUNITYMECH.curie('functional_role'),
                   model_uri=COMMUNITYMECH.taxonomicComposition__functional_role, domain=None, range=Optional[Union[Union[str, "FunctionalRoleEnum"], list[Union[str, "FunctionalRoleEnum"]]]])

slots.taxonomicComposition__evidence = Slot(uri=COMMUNITYMECH.evidence, name="taxonomicComposition__evidence", curie=COMMUNITYMECH.curie('evidence'),
                   model_uri=COMMUNITYMECH.taxonomicComposition__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.interactionDownstream__target = Slot(uri=COMMUNITYMECH.target, name="interactionDownstream__target", curie=COMMUNITYMECH.curie('target'),
                   model_uri=COMMUNITYMECH.interactionDownstream__target, domain=None, range=str)

slots.interactionDownstream__description = Slot(uri=COMMUNITYMECH.description, name="interactionDownstream__description", curie=COMMUNITYMECH.curie('description'),
                   model_uri=COMMUNITYMECH.interactionDownstream__description, domain=None, range=Optional[str])

slots.ecologicalInteraction__name = Slot(uri=COMMUNITYMECH.name, name="ecologicalInteraction__name", curie=COMMUNITYMECH.curie('name'),
                   model_uri=COMMUNITYMECH.ecologicalInteraction__name, domain=None, range=str)

slots.ecologicalInteraction__description = Slot(uri=COMMUNITYMECH.description, name="ecologicalInteraction__description", curie=COMMUNITYMECH.curie('description'),
                   model_uri=COMMUNITYMECH.ecologicalInteraction__description, domain=None, range=Optional[str])

slots.ecologicalInteraction__interaction_type = Slot(uri=COMMUNITYMECH.interaction_type, name="ecologicalInteraction__interaction_type", curie=COMMUNITYMECH.curie('interaction_type'),
                   model_uri=COMMUNITYMECH.ecologicalInteraction__interaction_type, domain=None, range=Optional[Union[str, "InteractionTypeEnum"]])

slots.ecologicalInteraction__source_taxon = Slot(uri=COMMUNITYMECH.source_taxon, name="ecologicalInteraction__source_taxon", curie=COMMUNITYMECH.curie('source_taxon'),
                   model_uri=COMMUNITYMECH.ecologicalInteraction__source_taxon, domain=None, range=Optional[Union[dict, TaxonDescriptor]])

slots.ecologicalInteraction__target_taxon = Slot(uri=COMMUNITYMECH.target_taxon, name="ecologicalInteraction__target_taxon", curie=COMMUNITYMECH.curie('target_taxon'),
                   model_uri=COMMUNITYMECH.ecologicalInteraction__target_taxon, domain=None, range=Optional[Union[dict, TaxonDescriptor]])

slots.ecologicalInteraction__metabolites = Slot(uri=COMMUNITYMECH.metabolites, name="ecologicalInteraction__metabolites", curie=COMMUNITYMECH.curie('metabolites'),
                   model_uri=COMMUNITYMECH.ecologicalInteraction__metabolites, domain=None, range=Optional[Union[Union[dict, MetaboliteDescriptor], list[Union[dict, MetaboliteDescriptor]]]])

slots.ecologicalInteraction__biological_processes = Slot(uri=COMMUNITYMECH.biological_processes, name="ecologicalInteraction__biological_processes", curie=COMMUNITYMECH.curie('biological_processes'),
                   model_uri=COMMUNITYMECH.ecologicalInteraction__biological_processes, domain=None, range=Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]])

slots.ecologicalInteraction__downstream = Slot(uri=COMMUNITYMECH.downstream, name="ecologicalInteraction__downstream", curie=COMMUNITYMECH.curie('downstream'),
                   model_uri=COMMUNITYMECH.ecologicalInteraction__downstream, domain=None, range=Optional[Union[Union[dict, InteractionDownstream], list[Union[dict, InteractionDownstream]]]])

slots.ecologicalInteraction__evidence = Slot(uri=COMMUNITYMECH.evidence, name="ecologicalInteraction__evidence", curie=COMMUNITYMECH.curie('evidence'),
                   model_uri=COMMUNITYMECH.ecologicalInteraction__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.environmentalFactor__name = Slot(uri=COMMUNITYMECH.name, name="environmentalFactor__name", curie=COMMUNITYMECH.curie('name'),
                   model_uri=COMMUNITYMECH.environmentalFactor__name, domain=None, range=str)

slots.environmentalFactor__value = Slot(uri=COMMUNITYMECH.value, name="environmentalFactor__value", curie=COMMUNITYMECH.curie('value'),
                   model_uri=COMMUNITYMECH.environmentalFactor__value, domain=None, range=Optional[str])

slots.environmentalFactor__unit = Slot(uri=COMMUNITYMECH.unit, name="environmentalFactor__unit", curie=COMMUNITYMECH.curie('unit'),
                   model_uri=COMMUNITYMECH.environmentalFactor__unit, domain=None, range=Optional[str])

slots.environmentalFactor__description = Slot(uri=COMMUNITYMECH.description, name="environmentalFactor__description", curie=COMMUNITYMECH.curie('description'),
                   model_uri=COMMUNITYMECH.environmentalFactor__description, domain=None, range=Optional[str])

slots.environmentalFactor__evidence = Slot(uri=COMMUNITYMECH.evidence, name="environmentalFactor__evidence", curie=COMMUNITYMECH.curie('evidence'),
                   model_uri=COMMUNITYMECH.environmentalFactor__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.growthMediaComponent__name = Slot(uri=COMMUNITYMECH.name, name="growthMediaComponent__name", curie=COMMUNITYMECH.curie('name'),
                   model_uri=COMMUNITYMECH.growthMediaComponent__name, domain=None, range=str)

slots.growthMediaComponent__media_ingredient_mech_id = Slot(uri=COMMUNITYMECH.media_ingredient_mech_id, name="growthMediaComponent__media_ingredient_mech_id", curie=COMMUNITYMECH.curie('media_ingredient_mech_id'),
                   model_uri=COMMUNITYMECH.growthMediaComponent__media_ingredient_mech_id, domain=None, range=Optional[str])

slots.growthMediaComponent__media_ingredient_mech_url = Slot(uri=COMMUNITYMECH.media_ingredient_mech_url, name="growthMediaComponent__media_ingredient_mech_url", curie=COMMUNITYMECH.curie('media_ingredient_mech_url'),
                   model_uri=COMMUNITYMECH.growthMediaComponent__media_ingredient_mech_url, domain=None, range=Optional[str])

slots.growthMediaComponent__concentration = Slot(uri=COMMUNITYMECH.concentration, name="growthMediaComponent__concentration", curie=COMMUNITYMECH.curie('concentration'),
                   model_uri=COMMUNITYMECH.growthMediaComponent__concentration, domain=None, range=Optional[str])

slots.growthMediaComponent__unit = Slot(uri=COMMUNITYMECH.unit, name="growthMediaComponent__unit", curie=COMMUNITYMECH.curie('unit'),
                   model_uri=COMMUNITYMECH.growthMediaComponent__unit, domain=None, range=Optional[str])

slots.growthMediaComponent__chebi_term = Slot(uri=COMMUNITYMECH.chebi_term, name="growthMediaComponent__chebi_term", curie=COMMUNITYMECH.curie('chebi_term'),
                   model_uri=COMMUNITYMECH.growthMediaComponent__chebi_term, domain=None, range=Optional[Union[dict, MetaboliteDescriptor]])

slots.growthMedia__name = Slot(uri=COMMUNITYMECH.name, name="growthMedia__name", curie=COMMUNITYMECH.curie('name'),
                   model_uri=COMMUNITYMECH.growthMedia__name, domain=None, range=str)

slots.growthMedia__culturemech_id = Slot(uri=COMMUNITYMECH.culturemech_id, name="growthMedia__culturemech_id", curie=COMMUNITYMECH.curie('culturemech_id'),
                   model_uri=COMMUNITYMECH.growthMedia__culturemech_id, domain=None, range=Optional[str])

slots.growthMedia__culturemech_url = Slot(uri=COMMUNITYMECH.culturemech_url, name="growthMedia__culturemech_url", curie=COMMUNITYMECH.curie('culturemech_url'),
                   model_uri=COMMUNITYMECH.growthMedia__culturemech_url, domain=None, range=Optional[str])

slots.growthMedia__composition = Slot(uri=COMMUNITYMECH.composition, name="growthMedia__composition", curie=COMMUNITYMECH.curie('composition'),
                   model_uri=COMMUNITYMECH.growthMedia__composition, domain=None, range=Optional[Union[Union[dict, GrowthMediaComponent], list[Union[dict, GrowthMediaComponent]]]])

slots.growthMedia__ph = Slot(uri=COMMUNITYMECH.ph, name="growthMedia__ph", curie=COMMUNITYMECH.curie('ph'),
                   model_uri=COMMUNITYMECH.growthMedia__ph, domain=None, range=Optional[str])

slots.growthMedia__ph_range = Slot(uri=COMMUNITYMECH.ph_range, name="growthMedia__ph_range", curie=COMMUNITYMECH.curie('ph_range'),
                   model_uri=COMMUNITYMECH.growthMedia__ph_range, domain=None, range=Optional[str])

slots.growthMedia__temperature = Slot(uri=COMMUNITYMECH.temperature, name="growthMedia__temperature", curie=COMMUNITYMECH.curie('temperature'),
                   model_uri=COMMUNITYMECH.growthMedia__temperature, domain=None, range=Optional[str])

slots.growthMedia__temperature_unit = Slot(uri=COMMUNITYMECH.temperature_unit, name="growthMedia__temperature_unit", curie=COMMUNITYMECH.curie('temperature_unit'),
                   model_uri=COMMUNITYMECH.growthMedia__temperature_unit, domain=None, range=Optional[str])

slots.growthMedia__temperature_range = Slot(uri=COMMUNITYMECH.temperature_range, name="growthMedia__temperature_range", curie=COMMUNITYMECH.curie('temperature_range'),
                   model_uri=COMMUNITYMECH.growthMedia__temperature_range, domain=None, range=Optional[str])

slots.growthMedia__atmosphere = Slot(uri=COMMUNITYMECH.atmosphere, name="growthMedia__atmosphere", curie=COMMUNITYMECH.curie('atmosphere'),
                   model_uri=COMMUNITYMECH.growthMedia__atmosphere, domain=None, range=Optional[Union[str, "AtmosphereEnum"]])

slots.growthMedia__headspace_gas = Slot(uri=COMMUNITYMECH.headspace_gas, name="growthMedia__headspace_gas", curie=COMMUNITYMECH.curie('headspace_gas'),
                   model_uri=COMMUNITYMECH.growthMedia__headspace_gas, domain=None, range=Optional[str])

slots.growthMedia__salinity = Slot(uri=COMMUNITYMECH.salinity, name="growthMedia__salinity", curie=COMMUNITYMECH.curie('salinity'),
                   model_uri=COMMUNITYMECH.growthMedia__salinity, domain=None, range=Optional[str])

slots.growthMedia__salinity_unit = Slot(uri=COMMUNITYMECH.salinity_unit, name="growthMedia__salinity_unit", curie=COMMUNITYMECH.curie('salinity_unit'),
                   model_uri=COMMUNITYMECH.growthMedia__salinity_unit, domain=None, range=Optional[str])

slots.growthMedia__pressure = Slot(uri=COMMUNITYMECH.pressure, name="growthMedia__pressure", curie=COMMUNITYMECH.curie('pressure'),
                   model_uri=COMMUNITYMECH.growthMedia__pressure, domain=None, range=Optional[str])

slots.growthMedia__pressure_unit = Slot(uri=COMMUNITYMECH.pressure_unit, name="growthMedia__pressure_unit", curie=COMMUNITYMECH.curie('pressure_unit'),
                   model_uri=COMMUNITYMECH.growthMedia__pressure_unit, domain=None, range=Optional[str])

slots.growthMedia__light_regime = Slot(uri=COMMUNITYMECH.light_regime, name="growthMedia__light_regime", curie=COMMUNITYMECH.curie('light_regime'),
                   model_uri=COMMUNITYMECH.growthMedia__light_regime, domain=None, range=Optional[str])

slots.growthMedia__light_intensity = Slot(uri=COMMUNITYMECH.light_intensity, name="growthMedia__light_intensity", curie=COMMUNITYMECH.curie('light_intensity'),
                   model_uri=COMMUNITYMECH.growthMedia__light_intensity, domain=None, range=Optional[str])

slots.growthMedia__light_intensity_unit = Slot(uri=COMMUNITYMECH.light_intensity_unit, name="growthMedia__light_intensity_unit", curie=COMMUNITYMECH.curie('light_intensity_unit'),
                   model_uri=COMMUNITYMECH.growthMedia__light_intensity_unit, domain=None, range=Optional[str])

slots.growthMedia__redox_potential = Slot(uri=COMMUNITYMECH.redox_potential, name="growthMedia__redox_potential", curie=COMMUNITYMECH.curie('redox_potential'),
                   model_uri=COMMUNITYMECH.growthMedia__redox_potential, domain=None, range=Optional[str])

slots.growthMedia__redox_potential_unit = Slot(uri=COMMUNITYMECH.redox_potential_unit, name="growthMedia__redox_potential_unit", curie=COMMUNITYMECH.curie('redox_potential_unit'),
                   model_uri=COMMUNITYMECH.growthMedia__redox_potential_unit, domain=None, range=Optional[str])

slots.growthMedia__inoculum_source = Slot(uri=COMMUNITYMECH.inoculum_source, name="growthMedia__inoculum_source", curie=COMMUNITYMECH.curie('inoculum_source'),
                   model_uri=COMMUNITYMECH.growthMedia__inoculum_source, domain=None, range=Optional[str])

slots.growthMedia__inoculum_size = Slot(uri=COMMUNITYMECH.inoculum_size, name="growthMedia__inoculum_size", curie=COMMUNITYMECH.curie('inoculum_size'),
                   model_uri=COMMUNITYMECH.growthMedia__inoculum_size, domain=None, range=Optional[str])

slots.growthMedia__inoculum_unit = Slot(uri=COMMUNITYMECH.inoculum_unit, name="growthMedia__inoculum_unit", curie=COMMUNITYMECH.curie('inoculum_unit'),
                   model_uri=COMMUNITYMECH.growthMedia__inoculum_unit, domain=None, range=Optional[str])

slots.growthMedia__incubation_time = Slot(uri=COMMUNITYMECH.incubation_time, name="growthMedia__incubation_time", curie=COMMUNITYMECH.curie('incubation_time'),
                   model_uri=COMMUNITYMECH.growthMedia__incubation_time, domain=None, range=Optional[str])

slots.growthMedia__incubation_time_unit = Slot(uri=COMMUNITYMECH.incubation_time_unit, name="growthMedia__incubation_time_unit", curie=COMMUNITYMECH.curie('incubation_time_unit'),
                   model_uri=COMMUNITYMECH.growthMedia__incubation_time_unit, domain=None, range=Optional[str])

slots.growthMedia__shaking_speed = Slot(uri=COMMUNITYMECH.shaking_speed, name="growthMedia__shaking_speed", curie=COMMUNITYMECH.curie('shaking_speed'),
                   model_uri=COMMUNITYMECH.growthMedia__shaking_speed, domain=None, range=Optional[str])

slots.growthMedia__shaking_speed_unit = Slot(uri=COMMUNITYMECH.shaking_speed_unit, name="growthMedia__shaking_speed_unit", curie=COMMUNITYMECH.curie('shaking_speed_unit'),
                   model_uri=COMMUNITYMECH.growthMedia__shaking_speed_unit, domain=None, range=Optional[str])

slots.growthMedia__vessel_type = Slot(uri=COMMUNITYMECH.vessel_type, name="growthMedia__vessel_type", curie=COMMUNITYMECH.curie('vessel_type'),
                   model_uri=COMMUNITYMECH.growthMedia__vessel_type, domain=None, range=Optional[str])

slots.growthMedia__preparation_notes = Slot(uri=COMMUNITYMECH.preparation_notes, name="growthMedia__preparation_notes", curie=COMMUNITYMECH.curie('preparation_notes'),
                   model_uri=COMMUNITYMECH.growthMedia__preparation_notes, domain=None, range=Optional[str])

slots.growthMedia__protocol_url = Slot(uri=COMMUNITYMECH.protocol_url, name="growthMedia__protocol_url", curie=COMMUNITYMECH.curie('protocol_url'),
                   model_uri=COMMUNITYMECH.growthMedia__protocol_url, domain=None, range=Optional[str])

slots.growthMedia__evidence = Slot(uri=COMMUNITYMECH.evidence, name="growthMedia__evidence", curie=COMMUNITYMECH.curie('evidence'),
                   model_uri=COMMUNITYMECH.growthMedia__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.associatedDataset__name = Slot(uri=COMMUNITYMECH.name, name="associatedDataset__name", curie=COMMUNITYMECH.curie('name'),
                   model_uri=COMMUNITYMECH.associatedDataset__name, domain=None, range=str)

slots.associatedDataset__dataset_type = Slot(uri=COMMUNITYMECH.dataset_type, name="associatedDataset__dataset_type", curie=COMMUNITYMECH.curie('dataset_type'),
                   model_uri=COMMUNITYMECH.associatedDataset__dataset_type, domain=None, range=Union[str, "DatasetTypeEnum"])

slots.associatedDataset__repository = Slot(uri=COMMUNITYMECH.repository, name="associatedDataset__repository", curie=COMMUNITYMECH.curie('repository'),
                   model_uri=COMMUNITYMECH.associatedDataset__repository, domain=None, range=Optional[Union[str, "DatasetRepositoryEnum"]])

slots.associatedDataset__accession = Slot(uri=COMMUNITYMECH.accession, name="associatedDataset__accession", curie=COMMUNITYMECH.curie('accession'),
                   model_uri=COMMUNITYMECH.associatedDataset__accession, domain=None, range=str)

slots.associatedDataset__url = Slot(uri=COMMUNITYMECH.url, name="associatedDataset__url", curie=COMMUNITYMECH.curie('url'),
                   model_uri=COMMUNITYMECH.associatedDataset__url, domain=None, range=Optional[str])

slots.associatedDataset__description = Slot(uri=COMMUNITYMECH.description, name="associatedDataset__description", curie=COMMUNITYMECH.curie('description'),
                   model_uri=COMMUNITYMECH.associatedDataset__description, domain=None, range=Optional[str])

slots.associatedDataset__evidence = Slot(uri=COMMUNITYMECH.evidence, name="associatedDataset__evidence", curie=COMMUNITYMECH.curie('evidence'),
                   model_uri=COMMUNITYMECH.associatedDataset__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.externalResource__name = Slot(uri=COMMUNITYMECH.name, name="externalResource__name", curie=COMMUNITYMECH.curie('name'),
                   model_uri=COMMUNITYMECH.externalResource__name, domain=None, range=str)

slots.externalResource__repository = Slot(uri=COMMUNITYMECH.repository, name="externalResource__repository", curie=COMMUNITYMECH.curie('repository'),
                   model_uri=COMMUNITYMECH.externalResource__repository, domain=None, range=Union[str, "ExternalResourceRepositoryEnum"])

slots.externalResource__resource_id = Slot(uri=COMMUNITYMECH.resource_id, name="externalResource__resource_id", curie=COMMUNITYMECH.curie('resource_id'),
                   model_uri=COMMUNITYMECH.externalResource__resource_id, domain=None, range=str)

slots.externalResource__url = Slot(uri=COMMUNITYMECH.url, name="externalResource__url", curie=COMMUNITYMECH.curie('url'),
                   model_uri=COMMUNITYMECH.externalResource__url, domain=None, range=str)

slots.externalResource__description = Slot(uri=COMMUNITYMECH.description, name="externalResource__description", curie=COMMUNITYMECH.curie('description'),
                   model_uri=COMMUNITYMECH.externalResource__description, domain=None, range=Optional[str])

slots.externalResource__evidence = Slot(uri=COMMUNITYMECH.evidence, name="externalResource__evidence", curie=COMMUNITYMECH.curie('evidence'),
                   model_uri=COMMUNITYMECH.externalResource__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.communityEngineeringDesign__objective = Slot(uri=COMMUNITYMECH.objective, name="communityEngineeringDesign__objective", curie=COMMUNITYMECH.curie('objective'),
                   model_uri=COMMUNITYMECH.communityEngineeringDesign__objective, domain=None, range=Optional[str])

slots.communityEngineeringDesign__assembly_strategy = Slot(uri=COMMUNITYMECH.assembly_strategy, name="communityEngineeringDesign__assembly_strategy", curie=COMMUNITYMECH.curie('assembly_strategy'),
                   model_uri=COMMUNITYMECH.communityEngineeringDesign__assembly_strategy, domain=None, range=Optional[str])

slots.communityEngineeringDesign__inoculation_strategy = Slot(uri=COMMUNITYMECH.inoculation_strategy, name="communityEngineeringDesign__inoculation_strategy", curie=COMMUNITYMECH.curie('inoculation_strategy'),
                   model_uri=COMMUNITYMECH.communityEngineeringDesign__inoculation_strategy, domain=None, range=Optional[str])

slots.communityEngineeringDesign__passaging_regimen = Slot(uri=COMMUNITYMECH.passaging_regimen, name="communityEngineeringDesign__passaging_regimen", curie=COMMUNITYMECH.curie('passaging_regimen'),
                   model_uri=COMMUNITYMECH.communityEngineeringDesign__passaging_regimen, domain=None, range=Optional[str])

slots.communityEngineeringDesign__perturbation_design = Slot(uri=COMMUNITYMECH.perturbation_design, name="communityEngineeringDesign__perturbation_design", curie=COMMUNITYMECH.curie('perturbation_design'),
                   model_uri=COMMUNITYMECH.communityEngineeringDesign__perturbation_design, domain=None, range=Optional[str])

slots.communityEngineeringDesign__measurement_endpoints = Slot(uri=COMMUNITYMECH.measurement_endpoints, name="communityEngineeringDesign__measurement_endpoints", curie=COMMUNITYMECH.curie('measurement_endpoints'),
                   model_uri=COMMUNITYMECH.communityEngineeringDesign__measurement_endpoints, domain=None, range=Optional[Union[str, list[str]]])

slots.communityEngineeringDesign__protocol_url = Slot(uri=COMMUNITYMECH.protocol_url, name="communityEngineeringDesign__protocol_url", curie=COMMUNITYMECH.curie('protocol_url'),
                   model_uri=COMMUNITYMECH.communityEngineeringDesign__protocol_url, domain=None, range=Optional[str])

slots.communityEngineeringDesign__notes = Slot(uri=COMMUNITYMECH.notes, name="communityEngineeringDesign__notes", curie=COMMUNITYMECH.curie('notes'),
                   model_uri=COMMUNITYMECH.communityEngineeringDesign__notes, domain=None, range=Optional[str])

slots.communityEngineeringDesign__evidence = Slot(uri=COMMUNITYMECH.evidence, name="communityEngineeringDesign__evidence", curie=COMMUNITYMECH.curie('evidence'),
                   model_uri=COMMUNITYMECH.communityEngineeringDesign__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.microbialCommunity__id = Slot(uri=COMMUNITYMECH.id, name="microbialCommunity__id", curie=COMMUNITYMECH.curie('id'),
                   model_uri=COMMUNITYMECH.microbialCommunity__id, domain=None, range=URIRef,
                   pattern=re.compile(r'^CommunityMech:\d{6}$'))

slots.microbialCommunity__name = Slot(uri=COMMUNITYMECH.name, name="microbialCommunity__name", curie=COMMUNITYMECH.curie('name'),
                   model_uri=COMMUNITYMECH.microbialCommunity__name, domain=None, range=str)

slots.microbialCommunity__description = Slot(uri=COMMUNITYMECH.description, name="microbialCommunity__description", curie=COMMUNITYMECH.curie('description'),
                   model_uri=COMMUNITYMECH.microbialCommunity__description, domain=None, range=Optional[str])

slots.microbialCommunity__ecological_state = Slot(uri=COMMUNITYMECH.ecological_state, name="microbialCommunity__ecological_state", curie=COMMUNITYMECH.curie('ecological_state'),
                   model_uri=COMMUNITYMECH.microbialCommunity__ecological_state, domain=None, range=Optional[Union[str, "EcologicalStateEnum"]])

slots.microbialCommunity__community_origin = Slot(uri=COMMUNITYMECH.community_origin, name="microbialCommunity__community_origin", curie=COMMUNITYMECH.curie('community_origin'),
                   model_uri=COMMUNITYMECH.microbialCommunity__community_origin, domain=None, range=Optional[Union[str, "CommunityOriginEnum"]])

slots.microbialCommunity__community_category = Slot(uri=COMMUNITYMECH.community_category, name="microbialCommunity__community_category", curie=COMMUNITYMECH.curie('community_category'),
                   model_uri=COMMUNITYMECH.microbialCommunity__community_category, domain=None, range=Optional[Union[str, "CommunityCategoryEnum"]])

slots.microbialCommunity__engineering_design = Slot(uri=COMMUNITYMECH.engineering_design, name="microbialCommunity__engineering_design", curie=COMMUNITYMECH.curie('engineering_design'),
                   model_uri=COMMUNITYMECH.microbialCommunity__engineering_design, domain=None, range=Optional[Union[dict, CommunityEngineeringDesign]])

slots.microbialCommunity__environment_term = Slot(uri=COMMUNITYMECH.environment_term, name="microbialCommunity__environment_term", curie=COMMUNITYMECH.curie('environment_term'),
                   model_uri=COMMUNITYMECH.microbialCommunity__environment_term, domain=None, range=Optional[Union[dict, EnvironmentDescriptor]])

slots.microbialCommunity__taxonomy = Slot(uri=COMMUNITYMECH.taxonomy, name="microbialCommunity__taxonomy", curie=COMMUNITYMECH.curie('taxonomy'),
                   model_uri=COMMUNITYMECH.microbialCommunity__taxonomy, domain=None, range=Optional[Union[Union[dict, TaxonomicComposition], list[Union[dict, TaxonomicComposition]]]])

slots.microbialCommunity__ecological_interactions = Slot(uri=COMMUNITYMECH.ecological_interactions, name="microbialCommunity__ecological_interactions", curie=COMMUNITYMECH.curie('ecological_interactions'),
                   model_uri=COMMUNITYMECH.microbialCommunity__ecological_interactions, domain=None, range=Optional[Union[Union[dict, EcologicalInteraction], list[Union[dict, EcologicalInteraction]]]])

slots.microbialCommunity__environmental_factors = Slot(uri=COMMUNITYMECH.environmental_factors, name="microbialCommunity__environmental_factors", curie=COMMUNITYMECH.curie('environmental_factors'),
                   model_uri=COMMUNITYMECH.microbialCommunity__environmental_factors, domain=None, range=Optional[Union[Union[dict, EnvironmentalFactor], list[Union[dict, EnvironmentalFactor]]]])

slots.microbialCommunity__growth_media = Slot(uri=COMMUNITYMECH.growth_media, name="microbialCommunity__growth_media", curie=COMMUNITYMECH.curie('growth_media'),
                   model_uri=COMMUNITYMECH.microbialCommunity__growth_media, domain=None, range=Optional[Union[Union[dict, GrowthMedia], list[Union[dict, GrowthMedia]]]])

slots.microbialCommunity__associated_datasets = Slot(uri=COMMUNITYMECH.associated_datasets, name="microbialCommunity__associated_datasets", curie=COMMUNITYMECH.curie('associated_datasets'),
                   model_uri=COMMUNITYMECH.microbialCommunity__associated_datasets, domain=None, range=Optional[Union[Union[dict, AssociatedDataset], list[Union[dict, AssociatedDataset]]]])

slots.microbialCommunity__external_resources = Slot(uri=COMMUNITYMECH.external_resources, name="microbialCommunity__external_resources", curie=COMMUNITYMECH.curie('external_resources'),
                   model_uri=COMMUNITYMECH.microbialCommunity__external_resources, domain=None, range=Optional[Union[Union[dict, ExternalResource], list[Union[dict, ExternalResource]]]])

slots.microbialCommunity__metals_present = Slot(uri=COMMUNITYMECH.metals_present, name="microbialCommunity__metals_present", curie=COMMUNITYMECH.curie('metals_present'),
                   model_uri=COMMUNITYMECH.microbialCommunity__metals_present, domain=None, range=Optional[Union[Union[str, "MetalElementEnum"], list[Union[str, "MetalElementEnum"]]]])

slots.microbialCommunity__rare_earth_elements_present = Slot(uri=COMMUNITYMECH.rare_earth_elements_present, name="microbialCommunity__rare_earth_elements_present", curie=COMMUNITYMECH.curie('rare_earth_elements_present'),
                   model_uri=COMMUNITYMECH.microbialCommunity__rare_earth_elements_present, domain=None, range=Optional[Union[Union[str, "RareEarthElementEnum"], list[Union[str, "RareEarthElementEnum"]]]])

slots.microbialCommunity__metal_relevance = Slot(uri=COMMUNITYMECH.metal_relevance, name="microbialCommunity__metal_relevance", curie=COMMUNITYMECH.curie('metal_relevance'),
                   model_uri=COMMUNITYMECH.microbialCommunity__metal_relevance, domain=None, range=Optional[Union[str, "MetalRelevanceEnum"]])

slots.microbialCommunity__metal_notes = Slot(uri=COMMUNITYMECH.metal_notes, name="microbialCommunity__metal_notes", curie=COMMUNITYMECH.curie('metal_notes'),
                   model_uri=COMMUNITYMECH.microbialCommunity__metal_notes, domain=None, range=Optional[str])

