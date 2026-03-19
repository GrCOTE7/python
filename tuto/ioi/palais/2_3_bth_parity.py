from typing import List, Tuple, Optional
from pymox_kit import cls, end, SB, R, bip_time
import time

START = (0, 0)

Pos = Tuple[int, int]

ROWS = 6
COLS = ROWS

# --- 1. Voisins orthogonaux ---


def neighbors(pos: Pos) -> List[Pos]:
    r, c = pos
    result = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result


# --- 2. Pré-calcul du graphe de la grille ---


def build_graph() -> Tuple[List[Pos], List[List[int]], int]:
    positions: List[Pos] = [(r, c) for r in range(ROWS) for c in range(COLS)]
    index = {p: i for i, p in enumerate(positions)}
    neigh: List[List[int]] = [[] for _ in positions]

    for i, pos in enumerate(positions):
        neigh[i] = [index[v] for v in neighbors(pos)]

    return positions, neigh, index[START]


# --- 3. Backtracking optimisé pour trouver 1 cycle ---


def find_one_cycle_parity(start: Pos = START) -> Optional[Tuple[Pos, ...]]:
    if (ROWS * COLS) % 2 != 0:
        return None

    positions, neigh, start_i = build_graph()
    if start != START:
        # Garde le comportement explicite: ce script est spécialisé pour START.
        raise ValueError("Ce script parity optimisé utilise START comme point fixe")

    total = len(positions)
    start_parity = (start[0] + start[1]) & 1

    visited = [False] * total
    path_idx = [start_i]
    visited[start_i] = True

    def onward_degree(node: int) -> int:
        return sum(1 for n in neigh[node] if not visited[n])

    def dfs(current: int, depth: int) -> bool:
        if depth == total:
            return start_i in neigh[current]

        expected_parity = (start_parity + depth) & 1
        moves = [
            n
            for n in neigh[current]
            if (not visited[n])
            and (((positions[n][0] + positions[n][1]) & 1) == expected_parity)
        ]

        # Warnsdorff: explorer d'abord les cases les plus contraintes.
        moves.sort(key=onward_degree)

        for nxt in moves:
            visited[nxt] = True
            path_idx.append(nxt)

            # Prune léger: sauf au dernier coup, la case choisie doit avoir une sortie.
            if depth + 1 == total or onward_degree(nxt) > 0:
                if dfs(nxt, depth + 1):
                    return True

            path_idx.pop()
            visited[nxt] = False

        return False

    if not dfs(start_i, 1):
        return None

    return tuple(positions[i] for i in path_idx)


# --- 4. Conversion mouvement → flèche & Affichage d’une solution ---


def direction(a: Pos, b: Pos) -> str:
    ar, ac = a
    br, bc = b
    # if (ar + ac) == 0:
    #     return 'X'
    if br == ar + 1 and bc == ac:
        return "↑"
    if br == ar - 1 and bc == ac:
        return "↓"
    if br == ar and bc == ac + 1:
        return "→"
    if br == ar and bc == ac - 1:
        return "←"

    return "?"


def print_cycle(cycle: Tuple[Pos, ...]) -> None:
    arrows = {}
    for i in range(len(cycle)):
        a = cycle[i]
        b = cycle[(i + 1) % len(cycle)]
        arrows[a] = direction(a, b)

    for r in range(ROWS - 1, -1, -1):
        print(" ".join(arrows[(r, c)] for c in range(COLS)))


# --- 5. Lancement ---


def main(aff: int = 1):
    """_summary_

    Args:
        aff (int, optional): affiche. Defaults to 1.
    """
    method = "parity"
    cycle = find_one_cycle_parity(START)

    print(f"Méthode: {SB}{method}{R}")
    if cycle is None:
        print(f"Aucun cycle trouvé sur une grille {ROWS} x {COLS}\n")
        return

    print(f"Cycle hamiltonien trouvé sur une grille {ROWS} x {COLS}\n")
    if aff:
        print_cycle(cycle)


if __name__ == "__main__":
    ROWS = 4
    COLS = ROWS

    def top():
        bip_time()
        return time.time()

    def fin(top):
        fin = time.time()
        print(f"\nTemps écoulé : {fin - top:.2f} secondes")

    cls()

    t1 = top()
    main(1)
    fin(t1)

    end()

    print(direction((0, 0), (0, 1)), direction((0, 0), (-1, 0)))  # ←
    print(direction((0, 0), (1, 0)), direction((0, 0), (0, -1)))  # ↑→
