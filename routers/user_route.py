# routers/users.py

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from db import get_db
from schema.schema import User
from controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users(
    db: Session = Depends(get_db),
    limit: int = Query(5, ge=1),
    offset: int = Query(0, ge=0)
):
    return user_controller.get_users(limit, offset, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(item: User, db: Session = Depends(get_db)):
    return user_controller.create_user(item, db)


@router.get("/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    return user_controller.get_user(user_id=user_id, db=db)


@router.put("/{user_id}")
def update_user(user_id: str, item: User, db: Session = Depends(get_db)):
    return user_controller.update_user(user_id, item, db)


@router.delete("/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    return user_controller.delete_user(user_id, db)
