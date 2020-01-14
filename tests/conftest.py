import os
import pytest
from spacy.matcher import PhraseMatcher
from pathlib import Path
from abstractor.textractor.textract import MatcherGenerator, TermItem
import pandas as pd
from typing import Callable, List
import math

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_morph_dict_loader(path: Path, n=math.inf) -> List[TermItem]:
    """"
    Load the first N entries of the ICDO-3 file
    """
    term_item_dict = {}
    morph_df = pd.read_csv(path, sep="\t")
    counter = 0
    for index, row in morph_df.iterrows():
        counter += 1
        if counter > n:
            break
        code, struct, label = row["Code"], row["Struct"], row["Label"]
        if code in term_item_dict:
            ti = term_item_dict[code]
            ti.syns.append(label)
        else:
            term_item_dict[code] = TermItem(code, label, [label])
    return list(term_item_dict.values())


@pytest.fixture(scope="session")
def morph_file_path() -> Path:
    return Path(dir_path) / "../data/ICD-O-3_CSV-metadata/Morphenglish.txt"


@pytest.fixture(scope="session")
def topo_file_path() -> Path:
    return Path(dir_path) / "../data/ICD-O-3_CSV-metadata/Topoenglish.txt"


@pytest.fixture(scope="session")
def morph_matcher(morph_file_path) -> PhraseMatcher:
    mgen = MatcherGenerator()
    return mgen(test_morph_dict_loader(morph_file_path, 100))
