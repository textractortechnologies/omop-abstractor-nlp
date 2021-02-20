import requests
import datetime
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import List, Dict


########################################################################################################################
# GET https://moomin.com/abstractor_abstraction_schemas/:abstractor_abstraction_schema_id(.:format)
########################################################################################################################


class Variant(BaseModel):
    value: str
    case_sensitive: bool


class Entry(BaseModel):
    value: str
    properties: str = None
    vocabulary_code: str
    vocabulary: str
    vocabulary_version: str
    case_sensitive: bool
    object_value_variants: List[Variant]


class AbstractionSchema(BaseModel):
    predicate: str
    display_name: str
    abstractor_object_type: str
    preferred_name: str
    predicate_variants: List[str]
    object_values: List[Entry]


class AbstractionSchemaMeta(BaseModel):
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
    name: str


class AbstractorSection(BaseModel):
    name: str
    section_mention_type: str
    section_name_variants: List[AbstractorSectionNameVariants]


class SuggestRequest(BaseModel):
    source_id: int
    source_type: str
    source_method: str
    abstractor_rules_uri: str
    text: str
    namespace_type: str
    namespace_id: int
    abstractor_abstraction_schemas: List[AbstractionSchemaMeta] = []
    abstractor_sections: List[AbstractorSection]


class SuggestionSource(BaseModel):
    match_value: str
    sentence_match_value: str
    section_name: str
    section_name_begin: int
    section_name_end: int


########################################################################################################################
# POST https://moomin.com/abstractor_abstractions/:abstractor_abstraction_id/abstractor_suggestions(.:format)
# TODO: one post call per suggestion to return
########################################################################################################################


class Suggestion(BaseModel):
    abstractor_abstraction_source_id: int
    source_id: int
    source_type: str
    source_method: str
    value: str
    unknown: bool = None
    not_applicable: bool = None
    negated: bool
    suggestion_sources: List[SuggestionSource]

