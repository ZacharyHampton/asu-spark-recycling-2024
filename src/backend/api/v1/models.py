from pydantic import BaseModel

class Product(BaseModel):
    id: str
    title: str
    image_url: str