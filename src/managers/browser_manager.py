import time
import webbrowser
from datetime import datetime, timedelta

import pyautogui
import pyperclip
import pytesseract

from src.config import config
from src.logger import logger


class BrowserManager:

    @staticmethod
    def waiting_status(wait_seconds: int = 60) -> str | None:
        wait_up_to = datetime.now() + timedelta(seconds=wait_seconds)
        while datetime.now() < wait_up_to:
            time.sleep(0.2)
            screen = pyautogui.screenshot()
            text = pytesseract.image_to_string(screen, config='--psm 6').lower()

            if "verifying" in text:
                pass
            elif "success!" in text:
                return "success"
            elif "human" in text:
                return "need_click"
            elif "failure" in text:
                return "failure"

    @staticmethod
    def visit_page(url: str) -> None:
        logger.info(f"VISIT {url}")
        webbrowser.open(url)

    @staticmethod
    def open_console() -> None:
        logger.info(f"OPEN CONSOLE")
        pyautogui.hotkey(config.OPEN_CONSOLE_HOTKEY)

    @staticmethod
    def close_terminal() -> None:
        logger.info(f"CLOSE TERMINAL")
        pyautogui.hotkey(config.CLOSE_CONSOLE_HOTKEY)

    @staticmethod
    def focus_console() -> None:
        logger.info("FOCUS CONSOLE")
        pyautogui.hotkey(config.FOCUS_CONSOLE)

    @staticmethod
    def clean_console() -> None:
        logger.info(f"CLEAN CONSOLE")
        pyautogui.hotkey(config.CLEAN_CONSOLE)

    @staticmethod
    def copy_cf_token() -> str:
        logger.info(f"PASTER COMMAND")
        pyperclip.copy("copy(turnstile.getResponse())")
        pyautogui.hotkey(config.INSERT_HOTKEY)
        pyautogui.press("Enter")
        time.sleep(0.5)
        logger.info("COPY TOKEN")
        token = pyperclip.paste()
        return token

    @staticmethod
    def reset_token() -> None:
        logger.info("RESET TOKEN")
        pyperclip.copy("turnstile.reset()")
        pyautogui.hotkey(config.INSERT_HOTKEY)
        time.sleep(0.5)
        pyautogui.press("Enter")
