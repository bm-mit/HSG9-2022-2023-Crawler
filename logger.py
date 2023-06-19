"""
Provides a logger for applition.
"""

from colorama import Fore, Style


class Logger:
    """
    Provides a logger to log text, message into stdout
    """

    @staticmethod
    def log_text(category: str, text: str, fore_color: Fore):
        """
        Log a text with category and color into stdout.
        """
        print(f"{fore_color}|{category.center(13)}|{Style.RESET_ALL}"
              f" -> "
              f"{fore_color}{text}{Style.RESET_ALL}")

    @staticmethod
    def log_message(text: str):
        """
        Log a message into stdout (category = "MESSAGE", fore_color = CYAN).
        """
        Logger.log_text("MESSAGE", text, Fore.CYAN)

    @staticmethod
    def log_error(text: str):
        """
        Log a error message into stdout (category = "ERROR", fore_color = RED).
        """
        Logger.log_text("ERROR", text, Fore.RED)

    @staticmethod
    def log_warning(text: str):
        """
        Log a warning message into stdout (category = "WARNING", fore_color = YELLOW).
        """
        Logger.log_text("WARNING", text, Fore.YELLOW)