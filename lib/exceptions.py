"""
Exceptions for telegrm bot
"""

import os


class TelegramBotException(Exception):
    """
    Base exeption for telegram bot

    Args:
        Exception (_type_): _description_
    """

    pass


class EnvFileNotFound(TelegramBotException):
    """
    File .env not found at current directory

    Args:
        search_directory (str): Folder, when search .env file

    Usage:
        if not os.path.exists(dotenv_path):
            logger.error("File .env not found in current directory")
            raise EnvFileNotFound()

    """

    def __init__(self, search_directory=None) -> None:
        self.search_directory = search_directory or os.getcwd()
        message = f".env file not found in: {self.search_directory}"
        super().__init__(message)


class RequiredEnvVariablesNotFound(TelegramBotException):
    """
    Variables not found in .env file

    Exception raised when required environment variables are not found.
    Args:
        missed_vars (list[str]): Missed variables at .env file

    Usage:
        required_vars: list[str]  = ["BOT_TOKEN"]
        missing_vars  =  [var for var in required_vars if var not in os.environ]
        if len(missing_vars) < 1:
            BOT_TOKEN = os.getenv('BOT_TOKEN')
            logger.info("Bot token: %s", BOT_TOKEN)
            return BOT_TOKEN
        else:
            logger.error("Variable BOT_TOKEN not found")
            raise RequiredEnvVariablesNotFound(missing_vars)
    """

    def __init__(self, missed_vars: list[str]) -> None:
        self.missed_vars = missed_vars
        message = f"Missing enveronment variables: {', '.join(missed_vars)}"
        super().__init__(message)
