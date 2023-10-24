from beanie import init_beanie
import motor.motor_asyncio
from .models import Products


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb+srv://Aiswarya:Mellow23%23@cluster0.twvmure.mongodb.net/Products?retryWrites=true&w=majority"
    )

    await init_beanie(database=client.db_name, document_models=[Products])
