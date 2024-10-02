import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.managers.browser_manager import BrowserManager
from src.managers.flow_manager import FlowManager


def main():
    browser_manager = BrowserManager()
    FlowManager.run_flow(browser_manager)

if __name__ == "__main__":
    main()
