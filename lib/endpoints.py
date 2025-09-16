from typing import TypedDict

# Definisikan tipe untuk detail setiap endpoint


class EndpointDetails(TypedDict):
    root: str


class AppEndpoints(TypedDict):
    predict_diabetes: EndpointDetails


# Terapkan tipe data pada dictionary ENDPOINTS
ENDPOINTS: AppEndpoints = {
    "predict_diabetes": {
        "root": "/"
    },
}
