from fastapi import APIRouter, Depends, status
from schema.schema import Diabetes
import joblib
import pandas as pd
from ..lib.endpoints import ENDPOINTS


router = APIRouter(prefix="/predict/diabetes", tags=['Diabetes'])


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

    model = joblib.load("ml_model/diabetes_model.joblib")

    print("on processs")

    predict = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]

    return {
        "message": "success",
        "data": data,
        "prediction": "Diabetes" if int(predict) == 1 else "No Diabetes",
        "probability_diabetes": f"{round(proba*100, 2)}%"
    }
