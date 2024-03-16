from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import MONGODB_URL


class Database:
    web: AsyncIOMotorClient = None


db = Database()


def get_database() -> AsyncIOMotorClient:
    return db.web


async def connect_to_mongo():
    db.web = AsyncIOMotorClient(str(MONGODB_URL), maxPoolSize=10, minPoolSize=10)


async def close_mongo_connection():
    db.web.close()
