import sys
from pathlib import Path

tools_path = Path(__file__).parent.parent / "tools"
sys.path.append(str(tools_path))

from tools import *


if __name__ == "__main__":

    cls("Script tuto/")

    pass

    # print("\n" + "-" * cliWR)

    # 2do Ranger ces tips
    w = (CLIWR - 18) // 2
    s = ""
    for _ in range(3):
        s += "* "
    print(s.center(w), *(range(1, 10)), s.center(w), end="\b\n")

    sl(FRENCH)
    print(f"{'Écrit /': <{CLIWR-27}}", end="")
    print("Lionel alias ", *"GrCOTE7", end="")
    print("\n", end="\r")
    exit()
