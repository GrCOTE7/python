from pymox_kit import cls, end

from typing import List, Tuple, Optional, Set

ROWS = 4
COLS = 4
START = (0, 0)

MOVE_DEFINITIONS = [
    ((1, 0), "↑"),
    ((-1, 0), "↓"),
    ((0, 1), "→"),
    ((0, -1), "←"),
]
OFFSETS = [delta for delta, _ in MOVE_DEFINITIONS]

Pos = Tuple[int, int]
ARROW_BY_DELTA = dict(MOVE_DEFINITIONS)


# --- 1. Voisins orthogonaux ---


def neighbors(pos: Pos) -> List[Pos]:
    r, c = pos
    result = []
    for dr, dc in OFFSETS:  # d pour décalage
        nr, nc = r + dr, c + dc  # n pour nouvelle
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result


# --- 2. Backtracking pur ---


def backtrack(
    current: Pos,
    visited: Set[Pos],
    path: List[Pos],
    start: Pos,
    total: int,
) -> bool:

    if len(path) == total:
        return start in neighbors(current)

    for v in neighbors(current):
        if v not in visited:
            visited.add(v)
            path.append(v)

            if backtrack(v, visited, path, start, total):
                return True

            visited.remove(v)
            path.pop()
    return False


# --- 3. Lancement de la recherche ---


def find_hamiltonian_cycle(
    start: Pos = START,
) -> Optional[List[Pos]]:
    visited = {start}
    path = [start]
    total = ROWS * COLS

    return path if backtrack(start, visited, path, start, total) else None


# --- 4. Génération de la matrice des flèches ---


def direction(a: Pos, b: Pos) -> str:
    ar, ac = a
    br, bc = b
    return ARROW_BY_DELTA.get((br - ar, bc - ac), "?")


# --- 5. Affichage final ---


def main():
    cycle = find_hamiltonian_cycle()

    if cycle is None:
        print("Aucun cycle hamiltonien trouvé.")
    else:
        print("Cycle trouvé (positions) :")
        print(" -> ".join(str(p) for p in cycle) + " -> " + str(cycle[0]))

        # Matrice des numéros.
        order = {pos: i + 1 for i, pos in enumerate(cycle)}

        print("\nMatrice des numéros de visite :\n")
        for r in range(ROWS - 1, -1, -1):
            print(" ".join(f"{order[(r,c)]:2d}" for c in range(COLS)))

        # Matrice des flèches
        print("\nMatrice des directions (flèches) :\n")

        pairs = zip(cycle, cycle[1:] + cycle[:1])
        arrows = {a: direction(a, b) for a, b in pairs}

        for r in range(ROWS - 1, -1, -1):
            print(" ".join(arrows[(r, c)] for c in range(COLS)))


if __name__ == "__main__":
    cls()
    main()
    end()
