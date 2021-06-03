from typing import List

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from analysis import lsi_analysis
from dataset_parser import load_business, load_reviews, format_review_text

if __name__ == '__main__':
    business_categories = ['hotels']
    business_ids = [b.business_id for b in load_business(categories=business_categories)]

    # 174.164 hotel reviews
    review_texts: List[str] = []
    review_stars: List[int] = []
    for review in load_reviews(business_ids=business_ids):
        review_texts.append(format_review_text(review.text))
        review_stars.append(review.stars)

    lsi_matrix = lsi_analysis(review_texts)
    classifiers = [LinearRegression()]
    X_train, X_test, y_train, y_test = train_test_split(lsi_matrix, review_stars, test_size=0.33, random_state=42)

    for classifier in classifiers:
        classifier.fit(X_train, y_train)
        score = classifier.score(X_test, y_test)
        print(f'{classifier} score {score}')

