import pluggy
from typing import List, Optional
import abstractor
from abstractor.app.dataclasses import *


hookspec = pluggy.HookspecMarker(abstractor.PROJECT_NAME)


@hookspec
def extract_suggestions(
    text: str,
    schema: AbstractionSchema,
    sections: Optional[List[AbstractorSection]] = None,
) -> List[Suggestion]:
    """

    :param text:
    :param schema:
    :param sections:
    :return: List[Suggestion]
    """
