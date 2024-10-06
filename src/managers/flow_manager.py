import os
import time

import pytesseract

from src.logger import config, logger
from src.managers.browser_manager import BrowserManager
from src.managers.redis_manager import RedisManager

pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_FILE

class FlowManager:
    @classmethod
    def run_flow(cls, browser_manager: BrowserManager, redis_manager: RedisManager) -> None:
        logger.info("\nRUN FLOW")
        url = os.environ["TARGET_URL"]

        browser_manager.visit_page(url)
        time.sleep(1)
        browser_manager.zoom_in()
        browser_manager.open_console()
        time.sleep(0.5)
        browser_manager.disable_auto_switching()
        browser_manager.allow_pasting()
        browser_manager.clean_console()

        attempt = 0
        while True:
            if attempt > 5:
                logger.warn("EXCEEDED COUNT ATTEMPTS")
                return

            status = browser_manager.waiting_status()
            if status is None:
                logger.warn("EXCEEDED WAITING STATUS TIME")
                return
            elif status == "success":
                browser_manager.clean_console()
                token = browser_manager.copy_cf_token()
                redis_manager.add(url, token)
                logger.info("TOKEN IS GOTTEN")
                time.sleep(config.CF_GEN_INTERVAL)
                browser_manager.gen_new_token()

            elif status in ["failure", "human"]:
                browser_manager.gen_new_token()
                attempt += 1
