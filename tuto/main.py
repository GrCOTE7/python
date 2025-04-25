import sys
from pathlib import Path

tools_path = Path(__file__).parent.parent / "tools"
sys.path.append(str(tools_path))

from tools import dg, fg, lg, cls, exit, pf

cls("Script tuto/")

if __name__ == "__main__":
    pass

    print("{0: ^55}".format("x"))
    print("\n" + "-" * 55)

    print(*(range(1, 10)))

    exit()
