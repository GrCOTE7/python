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
    s = ""
    for _ in range(3):
        s += "* "
    print(s.center(25), *(range(1, 10)), s.center(25), end="\b")

    sl(french)
    print(f"{'Écrit /': <{cliWR-27}}", end="")
    print("Lionel alias ", *"GrCOTE7", end="")
    print("\n", end="\r")
    exit()
