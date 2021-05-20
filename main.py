import itertools
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer

from dataset_parser import load_business, load_reviews
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt


def lsi_analysis(reviews_texts: List[str]) -> TruncatedSVD:
    word_bag = TfidfVectorizer(lowercase=True).fit_transform(reviews_texts)
    lsi = TruncatedSVD(n_components=100, n_iter=100)
    return lsi.fit_transform(word_bag)


if __name__ == '__main__':
    business_cats = ['restaurants', 'hotels']
    business_ids = [b.business_id for b in load_business(categories=business_cats)]

    texts = [r.text for r in itertools.islice(load_reviews(business_ids=business_ids), 10)]
    lsi_matrix = lsi_analysis(texts)
    plt.imshow(lsi_matrix)
    plt.colorbar()
    plt.show()
