import os
import sys


from src.managers.redis_manager import RedisManager

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.managers.browser_manager import BrowserManager
from src.managers.flow_manager import FlowManager
from pyvirtualdisplay.smartdisplay import SmartDisplay


def main():
    browser_manager = BrowserManager()
    redis_manager = RedisManager()
    with SmartDisplay(visible=True, size=(1920, 1080), backend="xvfb"):
        FlowManager.run_flow(browser_manager, redis_manager)

if __name__ == "__main__":
    main()
