import sys, time, math
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *
from tools import cls, nf, SB, EB, exit, sl, pf, BLUE

if __name__ == "__main__":

    cls("Exercice EULER # 007")

    # By listing the first six prime numbers: 2,3,5,7,11,13, we can see that the 6th prime is 13.
    # What is the 10 001st prime number?

    # En profiter pour voir:
    
    # 2do il existe une autre methode plus rapide: l’algorithme du crible d'Ératosthène, qui est une méthode rapide pour trouver tous les nombres premiers jusqu'à un certain n
    # Pourquoi un "sieve" (crible) ?
    # Un crible est une méthode qui élimine progressivement les nombres non premiers.
    # Il fonctionne comme un tamis : on élimine les multiples des nombres premiers pour ne garder que les vrais nombres premiers.
    
    # 2do en fin: Faire rapide comparatif entre exo # 5 et celui-ci
    
    exit()
