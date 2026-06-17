import time as top
import locale

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from tools import *


def simple_comptage(n=1e8):  # 1e8
    n = int(n)

    print(f"Je compte jusqu'à {nf(n,0)}...")

    s = top.time()
    # global i
    for i in range(n):
        if i < 8:
            print(f"{i} ", sep=" ", end="")
    print(f"... {nf(i)}.")
    print(f'Boucle classique : {(top.time() - s):.2f}"')
    # Mise dans une fonction, les var sont locales... + rapides !

    sl(color="french")

    t = top.time()
    print(*(i2 for i2 in range(n) if i2 < 9), end="\b")
    print(f"... {nf(i)}.")
    print(f'Boucle compréhension : {(top.time() - t):.2f}"')


# uv run flet run .\tutos\machinelearnia\benchmark_2_comprehension.py

if __name__ == "__main__":

    w = 55
    cls()

    simple_comptage()

    top.sleep(3)
    sl(color=GREEN)

    print("Fini.")
