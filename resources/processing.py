import re
from typing import List

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
from nltk.tokenize import word_tokenize

from database.query import readStopWords

nltk.data.path.append("NLTK_DATA")


def rem_stop(txt: str) -> List:
    """Remove stop words"""
    # return list(readStopWords())
    return [t for t in txt if t not in list(readStopWords())]


def normalisasi(txt: str) -> List[str]:
    """Text normalization or Pre-processing"""
    # * stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    txt = stemmer.stem(txt)
    # * remove urls
    txt = re.sub(r"http\S+", "", txt)
    # * remove punctuations
    txt = re.sub(r"[^\w\s]", "", txt)
    # * remove numbers
    txt = re.sub(r"\d+", "", txt)
    # * tokenize string
    txt = word_tokenize(txt)  # type: ignore
    # * remove stop words, return normalized strings in a list
    return rem_stop(txt)


def freqs(txt: str) -> List[tuple]:
    """Determine unique word's frequencies
    Output: tuple
    """
    return nltk.FreqDist(txt).most_common()

