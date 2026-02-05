from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os

logger = logging.getLogger(__name__)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "bank.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"


engine = create_engine(
    DATABASE_URL,
    echo=False,         
    future=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_session():
    try:
        return SessionLocal()
    except Exception as e:
        logger.error("Failed to create database session", exc_info=True)
        raise
