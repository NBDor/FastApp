from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.pool import QueuePool
from config.settings import app_settings

def get_url() -> str:
    user = app_settings.db_user
    password = app_settings.db_password
    server = app_settings.db_server
    db = app_settings.db_name
    port = app_settings.db_port
    return f"postgresql://{user}:{password}@{server}:{port}/{db}"

def get_celery_url() -> str:
    return f"db+{get_url()}"

SQLALCHEMY_DATABASE_URL = get_url()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
)

engine.pool_recycle = 300

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = DeclarativeBase

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:    
        db.close()