import os
import time
import pytesseract

from src.logger import logger, config
from src.managers.browser_manager import BrowserManager

pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_FILE

class FlowManager:
    @classmethod
    def run_flow(cls, browser_manager: BrowserManager) -> None:
        logger.info("\nRUN FLOW")
        url = os.environ["TARGET_URL"]
        attempt = 0
        browser_manager.visit_page(url)

        while True:
            if attempt > 5:
                logger.warn("EXCEEDED COUNT ATTEMPTS")
                return

            status = browser_manager.waiting_status()
            if status is None:
                logger.warn("EXCEEDED WAITING STATUS TIME")
                return
            elif status == "success":
                browser_manager.open_console()
                time.sleep(0.5)
                browser_manager.focus_console()
                time.sleep(0.5)
                browser_manager.clean_console()
                time.sleep(0.2)
                token = browser_manager.copy_cf_token()
                logger.info(token)
                break
            elif status in ["failure", "human"]:
                browser_manager.reset_token()
                browser_manager.close_terminal()
                attempt += 1
