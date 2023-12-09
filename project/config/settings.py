import os
from pydantic_settings import BaseSettings

log_dict = {
    "CRITICAL": 50,
    "FATAL": 50,
    "ERROR": 40,
    "WARNING": 30,
    "INFO": 20,
    "DEBUG": 10,
    "NOTSET": 0,
}


class Settings(BaseSettings):
    PAGE_SIZE: int = os.getenv("PAGE_SIZE", 10)
    db_user: str = os.getenv("DB_USER", "postgres")
    db_password: str = os.getenv("DB_PASSWORD", "simple_pssword")
    db_server: str = os.getenv("DB_SERVER", "localhost")
    db_name: str = os.getenv("DB_NAME", "test-projet")
    db_port: int = os.getenv("DB_PORT", 5432)
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    REDIS_SERVER: str = os.getenv("REDIS_SERVER", "redis://localhost:6379/1")


app_settings = Settings()