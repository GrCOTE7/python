import flet as ft

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from tools import *
import time as top

if __name__ == "__main__":

    def prevent(n, genre):
        print(f"Je compte jusqu'à {nf(n,0)}... De façon {genre} :")

    w = 45
    cls()

    n = int(1e3) # 1e8
    prevent(n, 'classique')
    s = top.time()
    for i in range(n):  # Ce i est global... <=> Recherche dans un dictionnaire
        if i < 8:
            print(f"{i} ", sep=" ", end="")

    print(f"... {i}")
    print(f'Boucle classique : {(top.time() - s):.2f}"')

    sl()
    
    prevent(n, 'compréhension')
    s = top.time()
    print(*(i for i in range(n) if i < 9), end="\b")  # Ici, les var sont générées
    print(f"... {i}")
    print(f'Boucle compréhension : {(top.time() - s):.2f}"')

    top.sleep(3)
    sl(w)

    print('Fini.')
