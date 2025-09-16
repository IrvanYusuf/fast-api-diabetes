from fastapi import FastAPI
from db import init_db
from routers import user_route, diabetes_route


app = FastAPI()


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/")
async def index():
    return {
        "data": "hello",
        "success": True
    }

app.include_router(user_route.router)
app.include_router(diabetes_route.router)
