from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import update
import models
from schema.schema import User


def get_users(limit: int, offset: int, db: Session):
    users = db.query(models.User).offset(offset).limit(limit).all()
    total = db.query(models.User).count()
    return {"message": "success", "pagination": {"total": total, "limit": limit}, "data": users}


def create_user(item: User, db: Session):
    user = models.User(name=item.name, age=item.age)
    db.add(user)
    db.commit()
    return {"message": "success", "data": item}


def get_user(user_id: str, db: Session):
    user = db.get(models.User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"message": "success", "data": user}


def update_user(user_id: str, item: User, db: Session):
    query = (
        update(models.User)
        .where(models.User.id == user_id)
        .values(name=item.name, age=item.age)
    )
    result = db.execute(query)
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "success update user", "data": item}


def delete_user(user_id: str, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "success delete user", "data": []}
