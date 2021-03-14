import pluggy
from typing import List, Optional
import abstractor
from abstractor.app.dataclasses import *


hookspec = pluggy.HookspecMarker(abstractor.PROJECT_NAME)


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
