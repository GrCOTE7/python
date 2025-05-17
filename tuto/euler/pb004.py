import sys, time
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import cls, nf, SB, EB, exit, sl

if __name__ == "__main__":

    cls("Exercice EULER # 004")

    exit()
    # print(f"{nf(a, 0): >10}")
