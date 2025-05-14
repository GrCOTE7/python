import sys

# sys.path.append("c:/laragon/www/PYTHON/python/tools/")
# from tools import *
# from tools import cls
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *

# Réf.: https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/

if __name__ == "__main__":

    cls("Zestedesavoir.com")

    def aFunction():
        x = 0
        x -= 8
        x *= -11
        x //= 4
        x **= 3
        x %= 10
        print(x)
        exit()

    def hello(name: str = None) -> str:
        print("Hello " + ("World" if name is None else name) + "!")

    hello("Zestedesavoir")
    hello()

    aFunction()
    exit()
