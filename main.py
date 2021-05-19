import itertools

from dataset_parser import load_business, load_reviews

if __name__ == '__main__':
    business_cats = ['restaurants', 'hotels']
    business_ids = []

    for business in load_business(categories=business_cats):
        business_ids.append(business['business_id'])

    for review in itertools.islice(load_reviews(business_ids=business_ids), 5000):
        pass
