import pandas as pd
import re
import spacy
import num2words
import numpy as np
from collections import Counter
from typing import Dict, List, Tuple 


def tokenize(phase: str) -> str:
    """Generate tokens using spacy"""
    nlp = spacy.load("fr_core_news_md")
    tokenizer = nlp.tokenizer
    return [token.text for token in tokenizer(phase)] 


tokenize_all = lambda phase: tokenize(phase)


def tokenize_lemmatize(sentenses: str) -> str:
    """Generate lemmatized tokens using spacy"""
    nlp = spacy.load("fr_core_news_md")
    tokenizer = nlp.tokenizer

    # tokenized_lemmatized_sentences = [
    #     [token.lemma_ for token in tokenizer(sentence)] for sentence in sentenses
    # ]
    # lemmatized_sentences = [
    #     " ".join(tokens) for tokens in tokenized_lemmatized_sentences
    # ]
    # return tokenized_lemmatized_sentences, lemmatized_sentences

    return [token.lemma_ for token in tokenizer(phase)] 


tokenize_lemmatize_all = lambda phase: tokenize_lemmatize(phase)


def clean_genesys_tokens(tokens: List) -> List:
    """Eliminate numbers at the begining of the transcription"""
    it_nums = []
    for number in range(25):
        it_nums.append(num2words.num2words(number + 1, lang="fr"))
        it_nums = [re.sub(r"-", " ", sentence) for sentence in it_nums]

    numbs_tokens = list(map(tokenize_all, it_nums))
    flat_numbs = [item for sublist in numbs_tokens for item in sublist]
    flat_numbs = list(dict.fromkeys(flat_numbs))
    flat_numbs_ = [x for x in flat_numbs if x != "et"]

    new_tokens = []
    for trans in tokens:
        if (
            (trans[0] in flat_numbs)
            and (trans[1] in flat_numbs)
            and (trans[2] in flat_numbs_)
        ):
            trans = trans[3:]
        elif (trans[0] in flat_numbs) and (trans[1] in flat_numbs):
            trans = trans[2:]
        elif trans[0] in flat_numbs or trans[0] == " ":
            trans = trans[1:]
        else:
            trans = trans
        new_tokens.append(trans)
    return new_tokens