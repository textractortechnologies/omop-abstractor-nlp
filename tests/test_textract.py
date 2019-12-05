import pytest
import spacy


def test_morph_matcher(morph_matcher):
    nlp = spacy.load("en_core_web_sm", disable=['ner'])
    doc = nlp("FINDINGS: Neoplasm, NOS")
    matches = morph_matcher(doc)
    assert len(matches) == 1
