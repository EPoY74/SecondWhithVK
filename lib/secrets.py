"""
Обработка и загрузка чувствительных данных из окружения
Processing and Loading Sensitive Data from Environment Variables
"""
import os

from dotenv import load_dotenv

import lib.project_log as proj_log
from lib.exceptions import EnvFileNotFound

logger = proj_log.logging.getLogger("lib/secrets.py")

def get_bot_api_from_dotenv() -> str | None:
    """
    Retrieve Telegram bot token from environment variables
     loaded from .env file.
    The .env file should be located in the root directory of the project
    
    Returns:
        str: Bot token if found, None if not found or error occurs.
    
    Raises:
        KeyError: If BOT_API_KEY not found in .env file
    """
        
    dotenv_path: str  = os.path.join(os.path.dirname(__file__),"..", '.env')

    logger.info("---")
    logger.info(dotenv_path)

    if not os.path.exists(dotenv_path):
        logger.error("File .env not found in current directory")
        raise EnvFileNotFound()
    elif not load_dotenv():
        logger.warning("Environment variable(s) not found in .env file")
        raise
    else:
        if os.getenv('BOT_TOKEN'):
            BOT_TOKEN = os.getenv('BOT_TOKEN')
            logger.info("Bot token: %s", BOT_TOKEN)
            return BOT_TOKEN
        else:
            logger.error("Variable BOT_TOKEN not found")
            raise

if __name__ == "__main__":
    get_bot_api_from_dotenv()