import sys, time as wait
from pathlib import Path

tools_path = Path(__file__).parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import CLIW, cls, exit, sl, GREEN, CYAN, YELLOW

if __name__ == "__main__":

    cls("Script Template")

    sl("french")
    wait.sleep(1)
    print("Ready.".center(CLIW))
    wait.sleep(1)
    sl(YELLOW)
    wait.sleep(1)

    exit()
