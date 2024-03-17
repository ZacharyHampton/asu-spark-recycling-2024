from pydantic import BaseModel
from enum import Enum


class ProductStatus(Enum):
    working = "working"
    broken = "broken"
    damaged = "damaged"


class OfferRequest(BaseModel):
    status: str


class Offer(BaseModel):
    amount: float
    url: str
    site_name: str
