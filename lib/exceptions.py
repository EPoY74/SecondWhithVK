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

    """

    def __init__ (self,search_directory = None) -> None:
        self.search_directory = search_directory or os.getcwd()
        message = f".env file not found in: {self.search_directory}"
        super().__init__(message)


class EnvVariablesNotFound(TelegramBotException):
    """
    Variables not found in .env file
    
    Exception raised when required environment variables are not found.
    Args:
        TelegramBotExeption (_type_): _description_
    """