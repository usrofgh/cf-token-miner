import sys
import time

from src.logger import logger
from src.managers.browser_manager import BrowserManager


class FlowManager:
    @classmethod
    def run_flow(cls, browser_manager: BrowserManager) -> None:
        logger.info("\nRUN FLOW")
        url = sys.argv[-1]

        browser_manager.visit_page(url)
        browser_manager.open_console()
        browser_manager.focus_console()
        browser_manager.clean_console()
        token = browser_manager.copy_cf_token()
        print(token)

        browser_manager.reset_token()
        time.sleep(5)
        browser_manager.focus_console()
        browser_manager.clean_console()
        token = browser_manager.copy_cf_token()
        print(token)
