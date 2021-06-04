from typing import List

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer


def lsi_analysis(reviews_texts: List[str]) -> TruncatedSVD:
    vectorizer = TfidfVectorizer(lowercase=False, ngram_range=(1, 2), stop_words=['a', 'the', 'that', 'is'])
    word_bag = vectorizer.fit_transform(reviews_texts)
    lsi = TruncatedSVD(n_components=100)
    return lsi.fit_transform(word_bag)
