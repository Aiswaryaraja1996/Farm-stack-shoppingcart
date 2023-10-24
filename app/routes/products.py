from beanie import PydanticObjectId
from fastapi import HTTPException, APIRouter
from database.models import Products


router = APIRouter()


@router.get("/", response_description="Get all products")
async def get_products():
    products = await Products.find_all().to_list()
    return products


@router.post("/add_product", response_description="Product added to database")
async def add_product(product: Products) -> dict:
    await product.create()
    return {"Product added successfully": product}


@router.get("/{category}", response_description="Product by category")
async def get_product_by_category(category: str):
    products = await Products.find({"category": category}).to_list()
    return products
