import random
from re import S
import sys
from pathlib import Path
from types import LambdaType

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls
from mvts import *

if __name__ == "__main__":
    cls(" old.algorea.org_chap7_enCours")

    def case():

        # print(
        #     (
        #         lambda x: (
        #             lambda: [
        #                 (
        #                     print(f"Nombre d'essais nécessaires :\n{tour}")
        #                     if (r := int(input())) == x
        #                     else (
        #                         print("c'est plus") if r < x else print("c'est moins")
        #                     )
        #                     or False
        #                 )
        #                 for tour in iter(int, 1)
        #             ]
        #         )()
        #     )(int(input()))
        # )

        ls()

    case()

    exit()

    # print(
    #     *(n := int(input())) and (n := n * i for i in range(1, int(input()) + 1)),
    #     sep="\n",
    # )
