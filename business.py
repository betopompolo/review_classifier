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
    categories: List[str]

    def __init__(self, business_dict):
        self.__dict__.update(business_dict)