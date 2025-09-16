# routers/users.py

from fastapi import APIRouter, Depends, Query, status
from schema.schema import User
from controllers.user_controller import UserController

router = APIRouter(prefix="/users", tags=["Users"])

user_controller = UserController()


@router.get("/")
async def get_users(
    limit: int = Query(5, ge=1),
    offset: int = Query(0, ge=0)
):
    return await user_controller.get_users(limit, offset)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(item: User):
    return await user_controller.create_user(item)


@router.get("/{user_id}")
async def get_user(user_id: str):
    return await user_controller.get_user(user_id=user_id)


@router.put("/{user_id}")
async def update_user(user_id: str, item: User):
    return await user_controller.update_user(user_id, item)


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    return await user_controller.delete_user(user_id)
