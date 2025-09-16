from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import models
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


async def init_db():
    try:
        print("Mencoba menghubungkan ke MongoDB...")
        client = AsyncIOMotorClient(MONGO_URI)
        # Menambahkan perintah 'ping' untuk menguji koneksi
        await client.admin.command('ping')
        print("Koneksi ke MongoDB berhasil!")
        db = client["ml_diabetes_predict"]
        await init_beanie(database=db, document_models=[models.User, models.Diabetes])
        print("Beanie berhasil diinisialisasi.")
    except Exception as e:
        print(f"Error saat inisialisasi DB: {e}")
        raise
