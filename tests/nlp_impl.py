from icecream import ic
import abstractor
from abstractor.app.dataclasses import *


@abstractor.hookimpl
def extract_suggestions(
    text: str,
    schema: AbstractionSchema,
    sections: Optional[List[AbstractorSection]] = None,
) -> bool:
    s = Suggestion(
        abstractor_abstraction_source_id=0,
        source_id=0,
        source_type="",
        source_method="",
        value="",
        suggestion_sources=[],
    )
    ic(s)
    return [s, s, s]
