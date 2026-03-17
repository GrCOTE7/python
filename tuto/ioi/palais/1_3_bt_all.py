from typing import List, Tuple, Dict, Set
from pymox_kit import *

ROWS = 4
COLS = 4
START = (0, 0)

Pos = Tuple[int, int]

# --- 1. Voisins orthogonaux ---


def neighbors(pos: Pos) -> List[Pos]:
    r, c = pos
    result = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result


# --- 2. Normalisation d’un cycle pour éviter les doublons ---


def normalize_cycle(cycle: List[Pos]) -> Tuple[Pos, ...]:
    n = len(cycle)
    forward = [tuple(cycle[i:] + cycle[:i]) for i in range(n)]
    backward = [
        tuple(list(reversed(cycle))[i:] + list(reversed(cycle))[:i]) for i in range(n)
    ]
    return min(forward + backward)


# --- 3. Backtracking pour énumérer tous les cycles ---


def backtrack(
    current: Pos,
    visited: Dict[Pos, bool],
    path: List[Pos],
    start: Pos,
    total: int,
    solutions: Set[Tuple[Pos, ...]],
) -> None:

    if len(path) == total:
        if start in neighbors(current):
            norm = normalize_cycle(path.copy())
            solutions.add(norm)
        return

    for v in neighbors(current):
        if not visited[v]:
            visited[v] = True
            path.append(v)
            backtrack(v, visited, path, start, total, solutions)
            visited[v] = False
            path.pop()


def find_all_cycles(start: Pos = START) -> List[Tuple[Pos, ...]]:
    visited = {(r, c): False for r in range(ROWS) for c in range(COLS)}
    visited[start] = True
    path = [start]
    total = ROWS * COLS
    solutions: Set[Tuple[Pos, ...]] = set()
    backtrack(start, visited, path, start, total, solutions)
    return sorted(solutions)


# --- 4. Conversion mouvement → flèche ---


def direction(a: Pos, b: Pos) -> str:
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


# --- 5. Affichage d’une solution ---


def print_cycle(cycle: Tuple[Pos, ...]) -> None:
    order = {pos: i + 1 for i, pos in enumerate(cycle)}

    # print("Matrice des numéros :")
    # for r in range(ROWS - 1, -1, -1):
    #     print(" ".join(f"{order[(r,c)]:2d}" for c in range(COLS)))
    # print()

    # print("Matrice des flèches :")
    arrows = {}
    for i in range(len(cycle)):
        a = cycle[i]
        b = cycle[(i + 1) % len(cycle)]
        arrows[a] = direction(a, b)

    for r in range(ROWS - 1, -1, -1):
        print(" ".join(arrows[(r, c)] for c in range(COLS)))
    # print("\n" + "-" * 40 + "\n")
    # print()


# --- 6. Lancement ---

all_cycles = find_all_cycles()

cls()

print(f"Nombre de cycles hamiltoniens distincts sur 4x4 : {len(all_cycles)}\n")

for i, cyc in enumerate(all_cycles, 1):
    print("─" * 8, i)
    print_cycle(cyc)

end()
