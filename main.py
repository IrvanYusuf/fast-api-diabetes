from fastapi import FastAPI
import models
from db import engine
from routers import user_route, diabetes_route


models.Base.metadata.create_all(engine)


app = FastAPI()


@app.get("/")
async def index():
    return {
        "data": "hello",
        "success": True
    }

app.include_router(user_route.router)
app.include_router(diabetes_route.router)
