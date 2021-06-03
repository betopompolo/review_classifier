import re
from typing import List, Iterator

import orjson

from model import Business, Review


def load_business(categories: List[str]) -> Iterator[Business]:
    with open('./dataset/business.json') as file_reader:
        for json_line in file_reader:
            business: Business = Business(orjson.loads(json_line))
            cats = [cat.lower().strip() for cat in business.categories.split(',')] if business.categories else []
            if any(cat in cats for cat in categories):
                yield business

    print('closing business file stream')


def load_reviews(business_ids: List[str]) -> Iterator[Review]:
    with open('./dataset/review.json') as file_reader:
        for json_line in file_reader:
            review: Review = Review(orjson.loads(json_line))
            if review.business_id in business_ids:
                yield review

    print('closing review stream')


regex = re.compile('[^a-zA-Z]')


def format_review_text(text: str) -> str:
    return regex.sub(' ', text.lower())
