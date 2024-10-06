import os
import sys


from src.managers.redis_manager import RedisManager

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.managers.browser_manager import BrowserManager
from src.managers.flow_manager import FlowManager


def main():
    browser_manager = BrowserManager()
    redis_manager = RedisManager()
    FlowManager.run_flow(browser_manager, redis_manager)

if __name__ == "__main__":
    main()
