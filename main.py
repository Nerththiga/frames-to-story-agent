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
    dir_path = sys.argv[1] if len(sys.argv) > 1 else os.getenv("DIR_PATH")

    if not dir_path:
        raise ValueError("No directory path provided. Please pass as argument or define DIR_PATH in .env.")
    
    if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
        raise FileNotFoundError(f"The directory path '{dir_path}' does not exist or is not a directory.")
    
    try:
        run_agent(dir_path)
    except Exception as e:
        raise e