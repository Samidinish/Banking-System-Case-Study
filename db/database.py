"""
Database configuration module.

This module is responsible for:
- Creating the SQLAlchemy engine
- Managing database sessions
- Connecting to a SQLite database using ORM
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os

# ------------------------------------------------------------------
# Logging configuration for database operations
# ------------------------------------------------------------------
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Database location
# ------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "bank.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"

# ------------------------------------------------------------------
# SQLAlchemy Engine
# ------------------------------------------------------------------
engine = create_engine(
    DATABASE_URL,
    echo=False,          # Set to True if you want to see SQL queries
    future=True
)

# ------------------------------------------------------------------
# Session factory
# ------------------------------------------------------------------
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# ------------------------------------------------------------------
# Session provider
# ------------------------------------------------------------------
def get_session():
    """
    Creates and returns a new database session.
    Caller is responsible for closing the session.
    """
    try:
        return SessionLocal()
    except Exception as e:
        logger.error("Failed to create database session", exc_info=True)
        raise
