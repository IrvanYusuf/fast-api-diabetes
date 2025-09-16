from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import models
import os

MONGO_URI = os.getenv(
    "MONGO_URI", "mongodb+srv://irvanyusufcahyadi_db_user:yUvChhrWcens63SI@cluster0.jtgihum.mongodb.net/ml_diabetes_predict?retryWrites=true&w=majority&appName=Cluster0")


async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.get_default_database()
    await init_beanie(database=db, document_models=[models.User, models.Diabetes])
