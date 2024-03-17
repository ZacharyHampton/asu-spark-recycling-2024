from fastapi import APIRouter, Depends
from ..db import get_database
from motor.motor_asyncio import AsyncIOMotorClient
from .models import Product
from pydantic import BaseModel
from bson.objectid import ObjectId
from concurrent.futures import ThreadPoolExecutor, as_completed
from .offers.models import OfferRequest, Offer, ProductStatus
from .offers.walmart import get_walmart_offer
from .offers.bestbuy import get_bestbuy_offer

router = APIRouter()


class ProductResponse(BaseModel):
    success: bool

    message: str = None
    product: Product = None


class Offers(BaseModel):
    walmart: Offer = None
    bestbuy: Offer = None


class OfferResponse(BaseModel):
    success: bool

    message: str = None
    offers: Offers = None


@router.get("/product/{uuid}")
async def get_product(uuid: str, db: AsyncIOMotorClient = Depends(get_database)) -> ProductResponse:
    collection = db["web"]["products"]

    product = await collection.find_one({"_id": ObjectId(uuid)})

    if not product:
        return ProductResponse(success=False, message="Product not found.")

    return ProductResponse(
        success=True,
        product=Product(
            id=str(product['_id']),
            title=product['walmart_title'],
            image_url=product['bestbuy_image_url']
        )
    )


@router.post("/product/{uuid}/offers")
async def get_offers(uuid: str, data: OfferRequest, db: AsyncIOMotorClient = Depends(get_database)) -> OfferResponse:
    collection = db["web"]["products"]

    if data.status not in ProductStatus.__members__:
        return OfferResponse(success=False, message="Invalid request.")

    product = await collection.find_one({"_id": ObjectId(uuid)})

    if not product:
        return OfferResponse(success=False, message="Product not found.")

    offers = {}
    with ThreadPoolExecutor() as executor:
        futures = []

        if bestbuy_url := product['product_urls'].get('bestbuy'):
            futures.append(executor.submit(get_bestbuy_offer, bestbuy_url, data))

        if walmart_url := product['product_urls'].get('walmart'):
            futures.append(executor.submit(get_walmart_offer, walmart_url, data))

        for future in as_completed(futures):
            offer: Offer = future.result()

            if offer:
                offers[offer.site_name] = offer

    return OfferResponse(
        success=True,
        offers=Offers(
            walmart=offers.get('walmart'),
            bestbuy=offers.get('bestbuy')
        )
    )
