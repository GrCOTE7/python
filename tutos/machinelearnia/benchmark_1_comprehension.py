import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))


from tools import *
import time as top

# uv run flet run .\tutos\machinelearnia\benchmark_1_comprehension.py

if __name__ == "__main__":

    def prevent(n, genre):
        print(f"Je compte jusqu'à {nf(n,0)}... De façon {genre} :")

    w = 45
    cls()

    n = int(1e6)  # → 1e8
    
    prevent(n, genre := "classique")
    s = top.time()
    for i in range(n):  # Ce i est global... <=> Recherche dans un dictionnaire
        if i < 8:
            print(f"{i} ", sep=" ", end="")
    print(f"... {i}\nBoucle {genre} : {(top.time() - s):.2f}")

    sl(color="french")

    prevent(n, genre := "compréhension")
    s = top.time()
    print(*(i for i in range(n) if i < 9), end="\b")  # Ici, les var sont générées
    print(f"... {i}\nBoucle {genre} : {(top.time() - s):.2f}")

    top.sleep(3)
    sl(color=GREEN)

    print("Fini.")
