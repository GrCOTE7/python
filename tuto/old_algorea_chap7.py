from re import S
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls
from mvts import *

# Réf.: https://www.france-ioi.org/
# Code Démo Algorea: m5iycsiw
# Code ALGORÉA: yqp4gbnf

if __name__ == "__main__":
    cls(" old.algorea.org_chap7")

    def resolve(d, f, ps):
        print(sum(1 for p in ps if p[0] <= f and p[1] >= d))

    def case():

        print(
            (
                lambda d, f, n: sum(
                    1
                    for e, s in [(int(input()) for _ in range(2)) for _ in range(n)]
                    if e <= f and s >= d
                )
            )(*[int(input()) for _ in range(3)])
        )

    case()

    exit()
