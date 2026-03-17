from pymox_kit import *

# Le palais est un carré de taille 4×4, et le robot se trouve au départ dans le coin en bas à gauche.
# Votre robot doit passer une et une seule fois dans chacune des pièces, puis se retrouver dans sa case de départ.

# On a donc au moins 6 façons de voir ce problème :
# 1️⃣ BT — BackTracking “pur” (le plus intuitif)
# 2️⃣ BTH — BackTracking + Heuristiques (la version intelligente)
# 3️⃣ GR — Greedy / Heuristique gloutonne (rapide, mais pas garanti)
# 4️⃣ CO — Construction directe (méthode mathématique)
# 5️⃣ DP — Dynamic Programming (programmation dynamique)
# 6️⃣ SAT/ILP — Encodage dans un solveur général

# 🧘 Pourquoi BT est fondamental
# Parce que :
# BTH = BT + intelligence
# GR = BT sans retour arrière
# DP = BT mais avec mémoire
# SAT = BT mais délégué à un solveur
# CO = solution trouvée sans BT, mais BT permet de la vérifier
# BT est la racine de toutes les autres méthodes.

from typing import List, Tuple, Dict, Optional

ROWS = 4
COLS = 4
START = (0, 0)

# --- 1. Voisins orthogonaux ---


def neighbors(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    r, c = pos
    result = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result


# --- 2. Backtracking pur ---


def backtrack(
    current: Tuple[int, int],
    visited: Dict[Tuple[int, int], bool],
    path: List[Tuple[int, int]],
    start: Tuple[int, int],
    total: int,
) -> bool:

    if len(path) == total:
        return start in neighbors(current)

    for v in neighbors(current):
        if not visited[v]:
            visited[v] = True
            path.append(v)

            if backtrack(v, visited, path, start, total):
                return True

            visited[v] = False
            path.pop()

    return False


# --- 3. Lancement de la recherche ---


def find_hamiltonian_cycle(
    start: Tuple[int, int] = START,
) -> Optional[List[Tuple[int, int]]]:
    visited = {(r, c): False for r in range(ROWS) for c in range(COLS)}
    visited[start] = True
    path = [start]
    total = ROWS * COLS

    if backtrack(start, visited, path, start, total):
        return path
    return None


# --- 4. Génération de la matrice des flèches ---


def direction(a: Tuple[int, int], b: Tuple[int, int]) -> str:
    ar, ac = a
    br, bc = b
    if br == ar + 1 and bc == ac:
        return "↑"
    if br == ar - 1 and bc == ac:
        return "↓"
    if br == ar and bc == ac + 1:
        return "→"
    if br == ar and bc == ac - 1:
        return "←"
    return "?"


# --- 5. Affichage final ---


def main():
    cycle = find_hamiltonian_cycle()

    if cycle is None:
        print("Aucun cycle hamiltonien trouvé.")
    else:
        print("Cycle trouvé (positions) :")
        print(" -> ".join(str(p) for p in cycle) + " -> " + str(cycle[0]))

        # Matrice des numéros
        order = {pos: i + 1 for i, pos in enumerate(cycle)}

        print("\nMatrice des numéros de visite :\n")
        for r in range(ROWS - 1, -1, -1):
            print(" ".join(f"{order[(r,c)]:2d}" for c in range(COLS)))

        # Matrice des flèches
        print("\nMatrice des directions (flèches) :\n")

        arrows = {}
        for i in range(len(cycle)):
            a = cycle[i]
            b = cycle[(i + 1) % len(cycle)]  # suivant, ou retour à start
            arrows[a] = direction(a, b)

        for r in range(ROWS - 1, -1, -1):
            print(" ".join(arrows[(r, c)] for c in range(COLS)))


if __name__ == "__main__":
    main()
