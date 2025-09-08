from typing import TypedDict

# Definisikan tipe untuk detail setiap endpoint


class EndpointDetails(TypedDict):
    root: str

# Tambahkan kunci baru di sini


class AppEndpoints(TypedDict):
    predict_diabetes: EndpointDetails
    predict_heart_disease: EndpointDetails  # <-- Tambahkan ini


# Terapkan tipe data pada dictionary ENDPOINTS
ENDPOINTS: AppEndpoints = {
    "predict_diabetes": {
        "root": "/"
    },
    "predict_heart_disease": {  # <-- Tambahkan ini
        "root": "/heart"
    }
}
