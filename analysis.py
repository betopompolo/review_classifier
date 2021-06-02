from typing import List

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer


def lsi_analysis(reviews_texts: List[str]) -> TruncatedSVD:
    word_bag = TfidfVectorizer(lowercase=False).fit_transform(reviews_texts)
    lsi = TruncatedSVD(n_iter=100)
    return lsi.fit_transform(word_bag)