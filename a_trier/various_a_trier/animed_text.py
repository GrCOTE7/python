from turtle import st
from tabulate import tabulate
import sys
from time import sleep

sys.path.append("c:/laragon/www/PYTHON/python/tools/")
from globals import *
from main_tools import *


def K2000Animation(t="Lionel"):

    sleepDuration = 0.03
    l = len(t)
    print()
    tlo = list(t)
    tl = tlo[:]

    for j in range(0, l):
        for i in range(0, l):
            tl = tlo[:]
            tl.insert(i, "\033[31m")
            tl.insert(i + 2, eb)
            ts = "".join(map(str, tl))
            print(ts, f"{i+1: >3}", " / ", f"{j+1: >2}", end=("\r"))
            sleep(sleepDuration)

        for i in range(l - 1, -1, -1):
            tl = tlo[:]
            tl.insert(i, "\033[31m")
            tl.insert(i + 2, eb)
            ts = "".join(map(str, tl))
            print(ts, f"{i+1: >3}", " / ", f"{j+1: >2}", end=("\r"))
            sleep(sleepDuration)
    print(t)


if __name__ == "__main__":

    cls("Anime Text")
    import string

    # K2000Animation(list(string.ascii_uppercase))

    # ls()
    exit()
