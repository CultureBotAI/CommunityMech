# Auto generated from communitymech.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-02-13T19:42:01
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

from linkml_runtime.linkml_model.types import String

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
    evidence_source: Optional[Union[str, "EvidenceSourceEnum"]] = None
    snippet: Optional[str] = None
    explanation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self._is_empty(self.supports):
            self.MissingRequiredField("supports")
        if not isinstance(self.supports, EvidenceItemSupportEnum):
            self.supports = EvidenceItemSupportEnum(self.supports)

        if self.evidence_source is not None and not isinstance(self.evidence_source, EvidenceSourceEnum):
            self.evidence_source = EvidenceSourceEnum(self.evidence_source)

        if self.snippet is not None and not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

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
    abundance_level: Optional[Union[str, "AbundanceEnum"]] = None
    abundance_value: Optional[str] = None
    functional_role: Optional[Union[Union[str, "FunctionalRoleEnum"], list[Union[str, "FunctionalRoleEnum"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxon_term):
            self.MissingRequiredField("taxon_term")
        if not isinstance(self.taxon_term, TaxonDescriptor):
            self.taxon_term = TaxonDescriptor(**as_dict(self.taxon_term))

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
class MicrobialCommunity(YAMLRoot):
    """
    A microbial community with composition and interactions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["MicrobialCommunity"]
    class_class_curie: ClassVar[str] = "communitymech:MicrobialCommunity"
    class_name: ClassVar[str] = "MicrobialCommunity"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.MicrobialCommunity

    name: str = None
    description: Optional[str] = None
    ecological_state: Optional[Union[str, "EcologicalStateEnum"]] = None
    environment_term: Optional[Union[dict, EnvironmentDescriptor]] = None
    taxonomy: Optional[Union[Union[dict, TaxonomicComposition], list[Union[dict, TaxonomicComposition]]]] = empty_list()
    ecological_interactions: Optional[Union[Union[dict, EcologicalInteraction], list[Union[dict, EcologicalInteraction]]]] = empty_list()
    environmental_factors: Optional[Union[Union[dict, EnvironmentalFactor], list[Union[dict, EnvironmentalFactor]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ecological_state is not None and not isinstance(self.ecological_state, EcologicalStateEnum):
            self.ecological_state = EcologicalStateEnum(self.ecological_state)

        if self.environment_term is not None and not isinstance(self.environment_term, EnvironmentDescriptor):
            self.environment_term = EnvironmentDescriptor(**as_dict(self.environment_term))

        self._normalize_inlined_as_dict(slot_name="taxonomy", slot_type=TaxonomicComposition, key_name="taxon_term", keyed=False)

        self._normalize_inlined_as_dict(slot_name="ecological_interactions", slot_type=EcologicalInteraction, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="environmental_factors", slot_type=EnvironmentalFactor, key_name="name", keyed=False)

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

# Slots
class slots:
    pass

slots.term__id = Slot(uri=COMMUNITYMECH.id, name="term__id", curie=COMMUNITYMECH.curie('id'),
                   model_uri=COMMUNITYMECH.term__id, domain=None, range=str)

slots.term__label = Slot(uri=COMMUNITYMECH.label, name="term__label", curie=COMMUNITYMECH.curie('label'),
                   model_uri=COMMUNITYMECH.term__label, domain=None, range=str)

slots.evidenceItem__reference = Slot(uri=COMMUNITYMECH.reference, name="evidenceItem__reference", curie=COMMUNITYMECH.curie('reference'),
                   model_uri=COMMUNITYMECH.evidenceItem__reference, domain=None, range=str)

slots.evidenceItem__supports = Slot(uri=COMMUNITYMECH.supports, name="evidenceItem__supports", curie=COMMUNITYMECH.curie('supports'),
                   model_uri=COMMUNITYMECH.evidenceItem__supports, domain=None, range=Union[str, "EvidenceItemSupportEnum"])

slots.evidenceItem__evidence_source = Slot(uri=COMMUNITYMECH.evidence_source, name="evidenceItem__evidence_source", curie=COMMUNITYMECH.curie('evidence_source'),
                   model_uri=COMMUNITYMECH.evidenceItem__evidence_source, domain=None, range=Optional[Union[str, "EvidenceSourceEnum"]])

slots.evidenceItem__snippet = Slot(uri=COMMUNITYMECH.snippet, name="evidenceItem__snippet", curie=COMMUNITYMECH.curie('snippet'),
                   model_uri=COMMUNITYMECH.evidenceItem__snippet, domain=None, range=Optional[str])

slots.evidenceItem__explanation = Slot(uri=COMMUNITYMECH.explanation, name="evidenceItem__explanation", curie=COMMUNITYMECH.curie('explanation'),
                   model_uri=COMMUNITYMECH.evidenceItem__explanation, domain=None, range=Optional[str])

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

slots.taxonomicComposition__taxon_term = Slot(uri=COMMUNITYMECH.taxon_term, name="taxonomicComposition__taxon_term", curie=COMMUNITYMECH.curie('taxon_term'),
                   model_uri=COMMUNITYMECH.taxonomicComposition__taxon_term, domain=None, range=Union[dict, TaxonDescriptor])

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

slots.microbialCommunity__name = Slot(uri=COMMUNITYMECH.name, name="microbialCommunity__name", curie=COMMUNITYMECH.curie('name'),
                   model_uri=COMMUNITYMECH.microbialCommunity__name, domain=None, range=str)

slots.microbialCommunity__description = Slot(uri=COMMUNITYMECH.description, name="microbialCommunity__description", curie=COMMUNITYMECH.curie('description'),
                   model_uri=COMMUNITYMECH.microbialCommunity__description, domain=None, range=Optional[str])

slots.microbialCommunity__ecological_state = Slot(uri=COMMUNITYMECH.ecological_state, name="microbialCommunity__ecological_state", curie=COMMUNITYMECH.curie('ecological_state'),
                   model_uri=COMMUNITYMECH.microbialCommunity__ecological_state, domain=None, range=Optional[Union[str, "EcologicalStateEnum"]])

slots.microbialCommunity__environment_term = Slot(uri=COMMUNITYMECH.environment_term, name="microbialCommunity__environment_term", curie=COMMUNITYMECH.curie('environment_term'),
                   model_uri=COMMUNITYMECH.microbialCommunity__environment_term, domain=None, range=Optional[Union[dict, EnvironmentDescriptor]])

slots.microbialCommunity__taxonomy = Slot(uri=COMMUNITYMECH.taxonomy, name="microbialCommunity__taxonomy", curie=COMMUNITYMECH.curie('taxonomy'),
                   model_uri=COMMUNITYMECH.microbialCommunity__taxonomy, domain=None, range=Optional[Union[Union[dict, TaxonomicComposition], list[Union[dict, TaxonomicComposition]]]])

slots.microbialCommunity__ecological_interactions = Slot(uri=COMMUNITYMECH.ecological_interactions, name="microbialCommunity__ecological_interactions", curie=COMMUNITYMECH.curie('ecological_interactions'),
                   model_uri=COMMUNITYMECH.microbialCommunity__ecological_interactions, domain=None, range=Optional[Union[Union[dict, EcologicalInteraction], list[Union[dict, EcologicalInteraction]]]])

slots.microbialCommunity__environmental_factors = Slot(uri=COMMUNITYMECH.environmental_factors, name="microbialCommunity__environmental_factors", curie=COMMUNITYMECH.curie('environmental_factors'),
                   model_uri=COMMUNITYMECH.microbialCommunity__environmental_factors, domain=None, range=Optional[Union[Union[dict, EnvironmentalFactor], list[Union[dict, EnvironmentalFactor]]]])

