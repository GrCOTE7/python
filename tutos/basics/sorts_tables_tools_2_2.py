import sys
from pathlib import Path
from turtle import st
from tabulate import tabulate
from operator import itemgetter, attrgetter

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import dg, fg, lg, cls, exit, pf

cls("Sorts 2/2 ()")

if __name__ == "__main__":

    print(
        "https://docs.python.org/3.13/howto/sorting.html#sortinghowto\n→ Decorate-Sort-Undecorate"
    )

    exit()  #################################
