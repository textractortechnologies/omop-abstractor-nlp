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
        abstractor_abstraction_source_id=11,
        source_id=13,
        source_type="mock",
        source_method="mock",
        value="foo",
        suggestion_sources=[],
    )
    ic(s)
    return [s]
