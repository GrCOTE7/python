import sys

sys.path.append("c:/laragon/www/PYTHON/python/tools/")
from tools import cls, sl, yellow, exit

if __name__ == "__main__":

    cls()

    def aFunction() -> None:
        print("\nAppel de aFunction()... Juste pour...: exit() !\n")
        exit()

    def hello(name: str = None, toPrint=True) -> None | str:
        s = "Hello " + ("World" if name is None else name) + "!"
        return s if not toPrint else print(s)

    s = hello("PyPaPro", 0)
    print(s.replace("Pa", ""))

    sl(yellow)

    hello()

    aFunction()
    exit()
