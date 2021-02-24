import os
import json
from icecream import ic
import abstractor
from abstractor.app.dataclasses import *
from pathlib import Path

# ---------------------------------------------------------------
# Plugin project setup.py contents:
# ---------------------------------------------------------------
# from setuptools import setup
#
# setup(
#     name="omop_nlp_plugin",
#     install_requires=["omop_abstractor_nlp"],
#     entry_points={"omop_abstractor_nlp": ["nlp = omop_nlp"]},
#     py_modules=["omop_nlp"],
# )
# ---------------------------------------------------------------


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

json_text = Path(dir_path / "data/suggestion-1.json").read_text()
json_dict = json.loads(json_text)
suggestion1 = Suggestion(**json_dict)

json_text = Path(dir_path / "data/suggestion-2.json").read_text()
json_dict = json.loads(json_text)
suggestion2 = Suggestion(**json_dict)


@abstractor.hookimpl
def extract_suggestions(
    text: str,
    schema: AbstractionSchema,
    sections: Optional[List[AbstractorSection]] = None,
) -> List[Suggestion]:
    return [suggestion1, suggestion2]