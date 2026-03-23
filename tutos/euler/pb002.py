import sys, time
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import cls, nf, SB, EB, exit

if __name__ == "__main__":

    cls("Exercice EULER # 002")

    def fibo(limit=4 * 10**6):
        s = 0
        a = b = 1
        while b < limit:
            (a, b) = (b, a + b)
            s += 0 if a % 2 else a
        return s

    print("Somme des items pairs et inférieurs à 4 000 000 dans fibo = ", fibo())

    exit()
    # print(f"{nf(a, 0): >10}")
