from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class Diabetes(BaseModel):
    gender: int
    age: float
    hypertension: int
    heart_disease: int
    smoking_history: int
    bmi: float
    HbA1c_level: float
    blood_glucose_level: int
