import itertools

from analysis import lsi_analysis
from dataset_parser import load_business, load_reviews, format_review_text
import matplotlib.pyplot as plt


if __name__ == '__main__':
    business_categories = ['hotels']
    business_ids = [b.business_id for b in load_business(categories=business_categories)]

    text = [format_review_text(r.text) for r in itertools.islice(load_reviews(business_ids=business_ids), 1)][0]
    print(text)
    # texts = [format_review_text(r.text) for r in itertools.islice(load_reviews(business_ids=business_ids), 1)]
    # lsi_matrix = lsi_analysis(texts)
    #
    # plt.imshow(lsi_matrix)
    # plt.colorbar()
    # plt.show()
