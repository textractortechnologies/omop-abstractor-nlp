import pluggy
from typing import List, Optional
import abstractor
from abstractor.app.dataclasses import *


hookspec = pluggy.HookspecMarker(abstractor.PROJECT_NAME)


@hookspec
def extract_suggestions(
    text: str,
    schema_metadata: AbstractionSchemaMetaData,
    schema: AbstractionSchema,
    sections: Optional[List[AbstractorSection]] = None,
) -> Dict[str, List[SuggestionSource]]:
    """
    Extract suggestions
    :param text:
    :param schema_metadata:
    :param schema:
    :param updated_schema:
    :param sections:
    :return: Dict[str, List[SuggestionSource]]
    """
