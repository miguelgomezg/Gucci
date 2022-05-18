import logging
import sys
from typing import List

from loguru import logger
from starlette.config import Config
from core.logging import InterceptHandler
from starlette.datastructures import CommaSeparatedStrings

API_PREFIX = "/api"
VERSION = "1.0.0"
config = Config(".env")
DEBUG: bool = config("DEBUG", cast=bool, default=False)

PROJECT_NAME: str = config(
    "PROJECT_NAME", default="Gucci")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default=""
)

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
