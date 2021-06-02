from typing import List


class Business:
    business_id: str
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    latitude: float
    longitude: float
    stars: float
    review_count: int
    is_open: int
    categories: str

    def __init__(self, business_dict):
        self.__dict__.update(business_dict)


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
