import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "tools"))
from tools.tools import *

# Redéfinir print pour utiliser sys.__stdout__ par défaut
_builtin_print = print


def print(*args, **kwargs):
    if "file" not in kwargs:
        kwargs["file"] = sys.__stdout__
    _builtin_print(*args, **kwargs)


if __name__ == "__main__":

    cols = CLIWR
    print(f"Largeur actuelle = {cols}")

    print("\n" + "A".center(55), end="")
    ls()
    print(f"{'B': ^{CLIWR}}")
    print(f"{0: ^{CLIWR}}".format("B"))
    print(*[i for i in range(68)], sep=" ", end="\n") #73
    exit()
