import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "tools"))
from tools.tools import *

if __name__ == "__main__":

    cls("Script racine")

    print("\n" + "A".center(55), end="")
    ls()
    print(f"{'B': ^{CLIWR}}")
    # print(f"{0: ^{CLIWR}}".format("B"))

    exit()
