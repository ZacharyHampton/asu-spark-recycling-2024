from fastapi import APIRouter
from .search import router as search_router
from .product import router as product_router

router = APIRouter(prefix="/api/v1", tags=["v1"])
router.include_router(search_router)
router.include_router(product_router)
