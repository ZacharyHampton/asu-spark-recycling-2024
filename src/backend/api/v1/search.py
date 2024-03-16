from fastapi import APIRouter, Depends
from ..db import get_database
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from .models import Product

router = APIRouter()


class SearchResults(BaseModel):
    products: list[Product]


@router.get("/search")
async def search(query: str, db: AsyncIOMotorClient = Depends(get_database)) -> SearchResults:
    collection = db['web']["products"]

    search_query = {
        '$search': {
            'index': 'default',  # the name of your search index
            'text': {
                'query': query,
                'path': {
                    'wildcard': '*'  # search all fields
                }
            }
        }
    }

    results = await collection.aggregate([search_query]).to_list(5)

    return SearchResults(
        products=[
            Product(
                id=str(result['_id']),
                title=result['walmart_title'],
                image_url=result['bestbuy_image_url']
            ) for result in results]
    )
