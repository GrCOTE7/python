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
    title='tiTre'
    
    print(f"Largeur actuelle = {cols}")
    cls(f"{title.capitalize()}")

    print("\n" + "A".center(cols), end="")
    print(f"{'B': ^{cols}}")
    ls('')
    print(*[i for i in range(7)], sep="\n", end="\n") #73
    exit()
    