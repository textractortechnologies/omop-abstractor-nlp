import requests
import datetime
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import List, Dict, Optional


########################################################################################################################
# GET https://moomin.com/abstractor_abstraction_schemas/:abstractor_abstraction_schema_id(.:format)
########################################################################################################################


class Variant(BaseModel):
    """ """
    value: str
    case_sensitive: bool


class Entry(BaseModel):
    """ """
    value: str
    properties: str = None
    vocabulary_code: str
    vocabulary: str
    vocabulary_version: str
    case_sensitive: bool
    object_value_variants: List[Variant]


class AbstractionSchema(BaseModel):
    """ """
    predicate: str
    display_name: str
    abstractor_object_type: str
    preferred_name: str
    predicate_variants: List[str]
    object_values: List[Entry]


class AbstractionSchemaMetaData(BaseModel):
    """ """
    abstractor_abstraction_schema_id: int
    abstractor_abstraction_schema_uri: str
    abstractor_abstraction_abstractor_suggestions_uri: str
    abstractor_abstraction_id: int
    abstractor_abstraction_source_id: int
    abstractor_subject_id: int
    namespace_type: str
    namespace_id: int
    abstractor_rule_type: str  # TODO: options are value and name-value
    abstractor_object_type: str  # TODO: type of value
    updated_at: datetime.datetime


########################################################################################################################
# POST http://custom-nlp-provider.test/multiple_suggest
########################################################################################################################


class AbstractorSectionNameVariants(BaseModel):
    """ """
    name: str


class AbstractorSection(BaseModel):
    """ """
    name: str
    section_mention_type: str
    section_name_variants: List[AbstractorSectionNameVariants]


class SuggestRequest(BaseModel):
    """ """
    source_id: int
    source_type: str
    source_method: str
    abstractor_rules_uri: str
    text: str
    namespace_type: str
    namespace_id: int
    abstractor_abstraction_schemas: List[AbstractionSchemaMetaData] = []
    abstractor_sections: List[AbstractorSection]


########################################################################################################################
# POST https://moomin.com/abstractor_abstractions/:abstractor_abstraction_id/abstractor_suggestions(.:format)
########################################################################################################################


class SuggestionSource(BaseModel):
    """ """
    negated: Optional[bool] = None
    match_value: str
    sentence_match_value: str
    section_name: str  # canonical name of section (not the variant name)
    section_name_begin: int  # start offset of matched header
    section_name_end: int  # end of entire section


class Suggestion(BaseModel):
    """ """
    abstractor_abstraction_source_id: int  # from schema metadata in request (named identically)
    source_id: int  # request source id
    source_type: str  # request source type
    source_method: str  # request source method
    value: str  # object value value from the schema (or number or date, depending on type)
    unknown: Optional[bool] = None  # no suggestions
    not_applicable: Optional[bool] = None  # leave as None
    negated: bool = False  # nlp says mention is negated
    suggestion_sources: List[SuggestionSource]
