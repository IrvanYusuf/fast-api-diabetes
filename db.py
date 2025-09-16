from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import models
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["ml_diabetes_predict"]  # jangan pakai get_default_database
    await init_beanie(database=db, document_models=[models.User, models.Diabetes])
