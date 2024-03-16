from pydantic import BaseModel


class OfferRequest(BaseModel):
    working: bool
    damaged: bool
    broken: bool


class Offer(BaseModel):
    amount: float
    url: str
    site_name: str
