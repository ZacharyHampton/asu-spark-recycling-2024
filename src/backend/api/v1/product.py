from fastapi import APIRouter, Depends
from ..db import get_database
from motor.motor_asyncio import AsyncIOMotorClient
from .models import Product
from pydantic import BaseModel
from bson.objectid import ObjectId

router = APIRouter()


class ProductResponse(BaseModel):
    success: bool

    message: str = None
    product: Product = None


@router.get("/product/{uuid}")
async def get_product(uuid: str, db: AsyncIOMotorClient = Depends(get_database)) -> ProductResponse:
    collection = db["web"]["products"]

    product = await collection.find_one({"_id": ObjectId(uuid)})

    if not product:
        return ProductResponse(success=False, message="Product not found")

    return ProductResponse(
        success=True,
        product=Product(
            id=str(product['_id']),
            title=product['walmart_title'],
            image_url=product['bestbuy_image_url']
        )
    )
