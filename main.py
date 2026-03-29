import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "tools"))
from tools.tools import *


def template():
    title = "ReaDy.".capitalize()
    # cls(f"{title}")
    ls(CYAN)
    print(f"{title}".center(CLIW))
    sl(FRENCH)


if __name__ == "__main__":

    template()
    print("ok")
    exit()
