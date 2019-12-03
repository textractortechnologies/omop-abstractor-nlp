#
# TODO: Add header here
#
import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher
from pathlib import Path
from collections import namedtuple
from typing import List, Dict, Callable

TermItem = namedtuple(
    "TermItem", ["code", "canonical", "synonyms"], defaults=["", "", []]
)


def morph_dict_loader(path: Path) -> List[TermItem]:
    term_item_dict = {}
    morph_df = pd.read_csv(path, sep="\t")
    for index, row in morph_df.iterrows():
        code, struct, label = row["Code"], row["Struct"], row["Label"]
        if code in term_item_dict:
            ti = term_item_dict[code]
            ti.subs.append(label)
        else:
            term_item_dict[code] = TermItem(code, label, [label])
    return list(term_item_dict.values())


class MatcherGenerator(object):
    def __init__(self, dict_loader: Callable):
        # TODO: put all configuration parameters into the config.yaml file
        nlp = spacy.load("en_core_web_sm", disable=["ner"])
        matcher = PhraseMatcher(nlp.vocab, attr="LEMMA")
        term_items = dict_loader(
            Path(
                "/Users/willthompson/Code/wkt/omop-abstractor-nlp/data/ICD-O-3_CSV-metadata/Morphenglish.txt"
            )
        )
        for ti in term_items:
            patterns = [nlp(sub) for sub in ti.subs]
            matcher.add(
                ti.code,
                [nlp(sub) for sub in ti.subs],
                on_match=self.gen_match_function(ti),
            )
        return matcher

    def gen_match_function(self, term_item: TermItem) -> Callable:
        def on_match(matcher, doc, id, matches):
            print(f"Matched: {term_item.code}", matches)

        return on_match
