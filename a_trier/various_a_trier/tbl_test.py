from pyparsing import C
from tabulate import tabulate
import sys

sys.path.append("c:/laragon/www/PYTHON/python/tools/")
from globals import *
from main_tools import *

if __name__ == "__main__":

    cls("tbl() - Tests")
    from itertools import combinations, permutations, product

    ss = [("a", 111), (1, 2), (2, 3)]

    for index, (expr, s) in enumerate(ss):
        print(f"# {index: >3} - {nf(s,0): >3} : {expr}")
    # exit()

    ls()

    # res = list(enumerate(combinations("ABCD", 2)))
    headers = ["#", "Combinaison"]

    res = enumerate(list(combinations("ABCD", 2)))
    tbl(res, headers=headers)

    sl(french)
    res = list(enumerate(["".join(pair) for pair in combinations("ABCD", 2)]))
    tbl(res, headers=headers)
    sl(french)

    tbl(
        [[r] for r in ["".join(pair) for pair in (combinations("ABCD", 2))]],
        headers=headers,
        indexes=1,
    ),

    ls()

    arr = [21, 12, 31]
    print(arr)
    print(*arr)
    print(", ".join(map(str, arr)))
    print(*enumerate(arr))
    for i, v in enumerate(arr):
        print(f"Index: {i}, Valeur: {v}")

    exit()
