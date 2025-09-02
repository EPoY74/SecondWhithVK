"""
Обработка и загрузка чувствительных данных из окружения
Processing and Loading Sensitive Data from Environment Variables
"""
import os

from dotenv import load_dotenv

import lib.project_log as proj_log

logger = proj_log.logging.getLogger("lib/secrets.py")

dotenv_path: str  = os.path.join(os.path.dirname(__file__),"..", '.env')

logger.info("---")
logger.info(dotenv_path)

if not os.path.exists(dotenv_path):
    logger.warning("File .env not found in current directory")
    # raise
elif not load_dotenv():
    logger.warning("Environment variable(s) not found in .env file")
    raise
else:
    if os.getenv('BOT_TOKEN'):
        BOT_TOKEN = os.getenv('BOT_TOKEN')
        logger.info("Bot token: %s", BOT_TOKEN)
    else:
        logger.error("Variable BOT_TOKEN not found")
        raise