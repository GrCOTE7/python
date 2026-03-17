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

# --- 1. Définition de la grille et des cases ---

# Grille logique (bas en premier, comme ta convention)
# Indices (row, col) : row = 0 (bas) -> 3 (haut), col = 0 (gauche) -> 3 (droite)
grid_letters = [
    ["A", "B", "C", "D"],  # row 0 (bas)
    ["E", "F", "G", "H"],  # row 1
    ["I", "J", "K", "L"],  # row 2
    ["M", "N", "O", "P"],  # row 3 (haut)
]

# Mapping lettre -> (row, col) et (row, col) -> lettre
letter_to_pos: Dict[str, Tuple[int, int]] = {}
pos_to_letter: Dict[Tuple[int, int], str] = {}
for r in range(4):
    for c in range(4):
        letter = grid_letters[r][c]
        letter_to_pos[letter] = (r, c)
        pos_to_letter[(r, c)] = letter

# --- 2. Fonction pour obtenir les voisins orthogonaux d'une case ---
def neighbors(letter: str) -> List[str]:
    r, c = letter_to_pos[letter]
    result = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # haut, bas, droite, gauche
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            result.append(pos_to_letter[(nr, nc)])
    return result


# --- 3. Backtracking pour trouver un cycle hamiltonien ---
def backtrack(
    current: str, visited: Dict[str, bool], path: List[str], start: str, total: int
) -> bool:
    # Si on a visité toutes les cases
    if len(path) == total:
        # On vérifie si on peut revenir au départ (cycle)
        return start in neighbors(current)

    # Sinon, on essaie tous les voisins non visités
    for v in neighbors(current):
        if not visited[v]:
            visited[v] = True
            path.append(v)

            if backtrack(v, visited, path, start, total):
                return True

            # Backtrack
            visited[v] = False
            path.pop()

    return False


# --- 4. Lancement de la recherche ---


def find_hamiltonian_cycle(start: str = "A") -> Optional[List[str]]:
    visited = {letter: False for letter in letter_to_pos.keys()}
    visited[start] = True
    path = [start]
    total = len(letter_to_pos)

    if backtrack(start, visited, path, start, total):
        return path
    else:
        return None


# --- 5. Affichage du résultat ---

if __name__ == "__main__":
    cycle = find_hamiltonian_cycle("A")

    if cycle is None:
        print("Aucun cycle hamiltonien trouvé.")
    else:
        print("Cycle hamiltonien trouvé (ordre des lettres) :")
        print(" -> ".join(cycle) + " -> " + cycle[0])

        # Construire une matrice 4x4 avec les numéros de visite
        order: Dict[str, int] = {letter: i + 1 for i, letter in enumerate(cycle)}
        print("\nMatrice des numéros de visite (haut en haut, bas en bas) :\n")

        # On affiche de haut (row 3) en bas (row 0)
        for r in range(3, -1, -1):
            row_nums = []
            for c in range(4):
                letter = grid_letters[r][c]
                row_nums.append(f"{order[letter]:2d}")
            print(" ".join(row_nums))
