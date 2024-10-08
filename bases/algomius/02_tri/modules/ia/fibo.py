import time

"""
    Fonction qui retourne l'élément n de la suite de Fibonacci de manière récursive 
"""


def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


"""
    Fonction qui retourne l'élément n de la suite de Fibonacci de manière récursive en programmation dynamique
"""


def fiboDyn(n, d):
    if n == 0 or n == 1:
        return 1
    elif n in d:
        return d[n]
    else:
        somme = fiboDyn(n - 1, d) + fiboDyn(n - 2, d)
        d[n] = somme
        return somme


"""
    Exemple de temps d’exécution des deux fonctions
"""

# debut = time.time()
# print(fibo(10))
# fin = time.time()
# print(fin - debut)

debut = time.time()
d = {}
n = 50
print(n, "→", fiboDyn(n, d))
fin = time.time()
print(fin - debut)
