import sys, time, math
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *
from tools import cls, nf, SB, EB, exit, sl, pf, BLUE

if __name__ == "__main__":

    cls("Exercice EULER # 006")

    def squaresSum(n):
        return n * (n + 1) * (2 * n + 1) // 6

    def sumSquare(n):
        return (n * (n + 1) // 2) ** 2

    N = 10
    s1 = squaresSum(N)
    s2 = sumSquare(N)
    pf("s2, s1, s2 - s1", 1)
    N = 100
    s1 = squaresSum(N)
    s2 = sumSquare(N)
    pf("s2, s1, s2 - s1", 1)

    exit()
