import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "tools"))
from tools.tools import *

# from pymox_kit import *


if __name__ == "__main__":

    title = "ReaDy."

    cls(f"{title.capitalize()}")

    ls(CYAN)

    print("Ready.".center(CLIW))

    sl(FRENCH)

    exit()
