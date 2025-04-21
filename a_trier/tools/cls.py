# 2do https://www.youtube.com/results?search_query=tuto+python+en+fran%C3%A7ais
import os, sys


def cls(title="module cls"):
    # Réinitialiser la console
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("-" * 55)
    print("{0: ^55}".format(title.capitalize()))
    print("-" * 55)
    print()
    # print()
    # print("-" * 55)


# from modules.fibo import fib, fib2

if __name__ == "__main__":

    cls()
