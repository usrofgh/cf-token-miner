import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.managers.flow_manager import FlowManager


def main():
    FlowManager.run_flow()

if __name__ == "__main__":
    main()
