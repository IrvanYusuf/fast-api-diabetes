from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from logger import logger

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/db_fast_api"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
        logger.info("Database successfully connecting")
    finally:
        db.close()
