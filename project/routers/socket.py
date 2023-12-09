from config.settings import app_settings
from logs.logger import logger
import socketio
from sqlalchemy.orm import Session
from database import get_db
from models import Item

mgr = socketio.AsyncRedisManager(app_settings.REDIS_SERVER)
sio = socketio.AsyncServer(
    client_manager=mgr,
    cors_allowed_origins=[],
    async_mode="asgi",
    logger=logger,
    engineio_logger=logger,
)
socket_app = socketio.ASGIApp(sio)
