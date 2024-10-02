import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.managers.flow_manager import FlowManager
from src.managers.browser_manager import BrowserManager

def main():
    browser_manager = BrowserManager()
    FlowManager.run_flow(browser_manager)

if __name__ == "__main__":
    main()
