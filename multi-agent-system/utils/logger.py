from loguru import logger
import os
import sys

if not os.path.exists("logs"):
    os.makedirs("logs")

logger.remove()
logger.add(sys.stdout, level="INFO", format="<green>{time}</green> <level>{message}</level>")
logger.add("logs/multi_agent_system.log", level="DEBUG", rotation="1 MB", format="<green>{time}</green> {level} <level>{message}</level>")

