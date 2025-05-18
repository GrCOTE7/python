import sys

# sys.path.append("c:/laragon/www/PYTHON/python/tools/")
# from tools import *
# from tools import cls
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *

# Réf.: https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/

if __name__ == "__main__":

    cls(" zestedesavoir.com")

    s = "  Lionel    CÔTE"
    x = 7
    x = 2.3
    print(x.numerator, x.denominator)

    # print(input().strip())
    exit()
