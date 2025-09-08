from sqlalchemy import Column, String, Integer
from db import Base
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(255))
    age = Column(Integer)
