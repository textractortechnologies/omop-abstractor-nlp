import pluggy
import textabstractor
from typing import Dict, List
from textabstractor.app.dataclasses import (
    AbstractionSchema,
    SuggestRequest,
    SuggestionSource
)

hookspec = pluggy.HookspecMarker(textabstractor.__project_name__)


@hookspec
def extract_suggestions(
    request: SuggestRequest, schema: AbstractionSchema, schema_idx: int
) -> Dict[str, List[SuggestionSource]]:
    """Extract suggestions

    Parameters
    ----------
    request :
        param schema:
    schema_idx :
        return: A dictionary, mapping from schema values to a list of suggestion sources supporting that value
    request: SuggestRequest :

    schema: AbstractionSchema :

    schema_idx: int :


    Returns
    -------
    type
        A dictionary, mapping from schema values to a list of suggestion sources supporting that value

    """
