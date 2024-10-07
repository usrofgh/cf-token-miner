from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from src.config import config


class BaseModel(DeclarativeBase):
    pass

engine = create_engine(config.PSQL_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
