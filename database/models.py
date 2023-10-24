from beanie import Document
from typing import Optional


class Products(Document):
    name: str
    img: str
    desc: str
    price: str
    rating: int
    category: str

    class Settings:
        name = "products"

    class Config:
        schema_extra = {
            "example": {
                "name": "Titan Smart Watch",
                "img": "https://staticimg.titan.co.in/Titan/Catalog/90165AP01_1.jpg?impolicy=pqmed&imwidth=640",
                "desc": "Titan Talk S Black Dial Smart Silicone Strap watch for Unisex",
                "rating": 4,
                "category": "watch",
            }
        }
