from typing import List


class Review:
    review_id: str
    user_id: str
    business_id: str
    stars: int
    date: str
    text: str
    useful: int
    funny: int
    cool: int

    def __init__(self, review_dict):
        self.__dict__.update(review_dict)