import sys
import os
from dotenv import load_dotenv
load_dotenv(override=True)

from frames2story_agent import frames2story_agent

def run_agent(dir_path):
    print(f"Starting the frames2story agent with images in {dir_path}")
    initial_state = {"dir_path": dir_path,"metadata": []}
    frames2story_agent.invoke(initial_state)

if __name__ == "__main__":
    print(os.getenv("DIR_PATH"))
    dir_path = sys.argv[1] if len(sys.argv) > 1 else os.getenv("DIR_PATH")
    run_agent(dir_path)