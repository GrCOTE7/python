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

from typing import List, Dict, Tuple, Optional

# --- 1. Définition de la grille ---

ROWS = 4
COLS = 4

# Départ : A = (0, 0)
START = (0, 0)


# --- 2. Voisins orthogonaux ---
def neighbors(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    r, c = pos
    result = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result


# --- 3. Backtracking pur ---


def backtrack(
    current: Tuple[int, int],
    visited: Dict[Tuple[int, int], bool],
    path: List[Tuple[int, int]],
    start: Tuple[int, int],
    total: int,
) -> bool:

    # Si toutes les cases sont visitées
    if len(path) == total:
        # On vérifie si on peut revenir au départ
        return start in neighbors(current)

    # Sinon, on explore les voisins
    for v in neighbors(current):
        if not visited[v]:
            visited[v] = True
            path.append(v)

            if backtrack(v, visited, path, start, total):
                return True

            # Retour arrière
            visited[v] = False
            path.pop()

    return False


# --- 4. Lancement de la recherche ---


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


# --- 5. Affichage du résultat ---

if __name__ == "__main__":
    cycle = find_hamiltonian_cycle()

if cycle is None:
    print("Aucun cycle hamiltonien trouvé.")
else:
    print("Cycle trouvé (positions) :")
    print(" -> ".join(str(p) for p in cycle) + " -> " + str(cycle[0]))

    # Matrice des numéros de visite
    order = {pos: i + 1 for i, pos in enumerate(cycle)}

    print("\nMatrice des numéros de visite (haut en haut) :\n")
    for r in range(ROWS - 1, -1, -1):
        row_nums = []
        for c in range(COLS):
            row_nums.append(f"{order[(r,c)]:2d}")
        print(" ".join(row_nums))
