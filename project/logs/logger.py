from config.settings import log_dict, app_settings
import logging

logging.basicConfig(
    level=log_dict[app_settings.LOG_LEVEL],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("FastAPI Test Project")