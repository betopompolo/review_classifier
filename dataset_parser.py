import json
import re

from typing import List, Generator

from model import Business, Review


def load_business(categories: List[str]) -> Generator[Business, None, None]:
    with open('./dataset/business.json') as file_reader:
        for json_line in file_reader:
            business: Business = json.loads(json_line, object_hook=Business)
            cats = [cat.lower().strip() for cat in business.categories.split(',')] if business.categories else []
            if any(cat in cats for cat in categories):
                yield business

    print('closing business file stream')


def load_reviews(business_ids: List[str]) -> Generator[Review, None, None]:
    with open('./dataset/review.json') as file_reader:
        for json_line in file_reader:
            review: Review = json.loads(json_line, object_hook=Review)
            if review.business_id in business_ids:
                yield review

    print('closing review stream')


regex = re.compile(r'[^\w\s]')


def format_review_text(text: str) -> str:
    return regex.sub(' ', text.lower())

