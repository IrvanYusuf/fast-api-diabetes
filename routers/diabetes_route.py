from fastapi import APIRouter, Depends, status
from schema.schema import Diabetes
import joblib
import pandas as pd
import requests
from ..lib.endpoints import ENDPOINTS


router = APIRouter(prefix="/predict/diabetes", tags=['Diabetes'])

API_MODEL_URL = "https://irvan222-diabetes-prediction.hf.space/predict"


@router.post(ENDPOINTS['predict_diabetes']['root'])
def predict(data: Diabetes):
    input_df = pd.DataFrame([
        {
            "gender": data.gender,
            "age": data.age,
            "hypertension": data.hypertension,
            "heart_disease": data.heart_disease,
            "smoking_history": data.smoking_history,
            "bmi": data.bmi,
            "HbA1c_level": data.HbA1c_level,
            "blood_glucose_level": data.blood_glucose_level
        }
    ])

    response = requests.post(API_MODEL_URL, json=input_df)
    response.raise_for_status()

    print("on processs")

    result = response.json()

    print(result)
    return {
        "message": "success",
        "data": data,
        "prediction": result['prediction_result'],
        "probability_diabetes": f"{round(result['prediction_probabilities'][1]*100, 2)}%"
    }
