import json

from typing import List


def load_business(categories: List[str]):
    with open('./dataset/business.json') as file_reader:
        for json_line in file_reader:
            business = json.loads(json_line)
            cats_str = business['categories']
            cats = [cat.lower().strip() for cat in cats_str.split(',')] if cats_str else []
            if any(cat in cats for cat in categories):
                yield business


def load_reviews(business_ids: List[str]):
    with open('./dataset/review.json') as file_reader:
        for json_line in file_reader:
            review = json.loads(json_line)
            if review['business_id'] in business_ids:
                yield review
