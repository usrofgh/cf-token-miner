import pyautogui
import webbrowser
import time
import pyperclip

from src.config import config
from src.logger import logger


class BrowserManager:
    @staticmethod
    def visit_page(url: str) -> None:
        logger.info(f"VISIT {url}")
        webbrowser.open(url)
        time.sleep(10)

    @staticmethod
    def open_console() -> None:
        logger.info(f"OPEN CONSOLE")
        pyautogui.hotkey(config.OPEN_CONSOLE_HOTKEY)
        time.sleep(0.5)

    @staticmethod
    def focus_console() -> None:
        logger.info("FOCUS CONSOLE")
        pyautogui.hotkey(config.FOCUS_CONSOLE)
        time.sleep(0.5)

    @staticmethod
    def clean_console() -> None:
        logger.info(f"CLEAN CONSOLE")
        pyautogui.hotkey(config.CLEAN_CONSOLE)

    @staticmethod
    def copy_cf_token() -> str:
        logger.info(f"PASTER COMMAND")
        pyautogui.write("copy(turnstile.getResponse())")
        pyautogui.press("Enter")
        time.sleep(0.5)
        logger.info("COPY TOKEN")
        token = pyperclip.paste()
        return token

    @staticmethod
    def reset_token() -> None:
        logger.info("RESET TOKEN")
        pyautogui.write("turnstile.reset()")
        time.sleep(0.5)
        pyautogui.press("Enter")
