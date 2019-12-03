#
# TODO: Add header here
#

import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher
from pathlib import Path
from collections import namedtuple

TermItem = namedtuple("TermItem", ["code", "title", "subs"], defaults=["", "", []])


class DictLoader(object):
    def __init__(self):
        pass


