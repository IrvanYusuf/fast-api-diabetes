from typing import Optional
from beanie import Document


class User(Document):
    name: str
    age: int

    class Settings:
        name = "users"


class Diabetes(Document):
    glucose: int
    blood_pressure: int
    insulin: int
    bmi: float
    prediction: Optional[str] = None

    class Settings:
        name = "diabetes"
