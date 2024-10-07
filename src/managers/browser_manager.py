import subprocess
import time
from datetime import datetime, timedelta

import pyautogui
import pytesseract

from src.config import config, HotKeys
from src.logger import logger
from src.misc import paste_from_clipboard, copy_to_clipboard


class BrowserManager:

    @staticmethod
    def waiting_status(wait_seconds: int = 60) -> str:
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
                return "human"
            elif "failure" in text:
                return "failure"

    @staticmethod
    def visit_page(url: str) -> None:
        subprocess.Popen(
            [
                config.CHROME_FILE,
                "--no-first-run",
                "--no-default-browser-check",
                "--disable-cache",
                "--no-sandbox",
                # f"--user-data-dir={config.BROWSER_PROFILE}",
                f"--load-extension={config.BROWSER_EXT}",
                "--window-size=1920,1080",
                url

            ]
        )

    @classmethod
    def disable_auto_switching(cls) -> None:
        # Turned off in the prepared chrome profile
        pyautogui.press("F1")
        time.sleep(0.3)
        # Move up to flag 'Focus Sources panel when triggering a breakpoint' and turn off it
        [pyautogui.press("Tab") for _ in range(18)]
        pyautogui.press("space")
        pyautogui.press("Esc")


    @staticmethod
    def zoom_in() -> None:
        pyautogui.hotkey(HotKeys.ZOOM_IN)
        pyautogui.hotkey(HotKeys.ZOOM_IN)

    @staticmethod
    def open_console() -> None:
        logger.info(f"OPEN CONSOLE")
        pyautogui.hotkey(HotKeys.OPEN_CONSOLE_HOTKEY)

    @staticmethod
    def focus_console() -> None:
        logger.info("FOCUS CONSOLE")
        pyautogui.hotkey(HotKeys.FOCUS_CONSOLE)

    @staticmethod
    def allow_pasting() -> None:
        copy_to_clipboard("")
        pyautogui.hotkey(HotKeys.INSERT_HOTKEY)
        pyautogui.write("allow pasting")
        time.sleep(0.2)
        pyautogui.press("Enter")

    @staticmethod
    def clean_console() -> None:
        logger.info(f"CLEAN CONSOLE")
        pyautogui.hotkey(HotKeys.CLEAN_CONSOLE)

    @staticmethod
    def copy_cf_token() -> str:
        logger.info(f"PASTER COMMAND")
        copy_to_clipboard("copy(turnstile.getResponse())")
        pyautogui.hotkey(HotKeys.INSERT_HOTKEY)
        pyautogui.press("Enter")
        time.sleep(0.5)
        logger.info("COPY TOKEN")
        token = paste_from_clipboard()
        return token

    @staticmethod
    def gen_new_token() -> None:
        logger.info("GENERATE NEW TOKEN")
        copy_to_clipboard("turnstile.reset()")
        pyautogui.hotkey(HotKeys.INSERT_HOTKEY)
        time.sleep(0.5)
        pyautogui.press("Enter")

browser_manager = BrowserManager()
