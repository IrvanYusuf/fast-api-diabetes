from fastapi import FastAPI
from db import init_db
from routers import user_route, diabetes_route
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await init_db()
        yield
    except Exception as e:
        raise e


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def index():
    return {
        "data": "hello",
        "success": True
    }

app.include_router(user_route.router)
app.include_router(diabetes_route.router)
