from loguru import logger
logger.add("logs/utamaduni.log", rotation="1 week", level="INFO")
