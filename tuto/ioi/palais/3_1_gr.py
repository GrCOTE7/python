from typing import List, Tuple, Set
from pathlib import Path
from pymox_kit import cls, end, SB, R, bip_time, nf

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


# --- 2. Heuristique locale GR ---


def evaluate_local_score(cell: Pos, visited: Set[Pos]) -> int:
    score = 0

    # 1. On préfère les cases avec peu de voisins libres (évite les impasses)
    free = sum(1 for v in neighbors(cell) if v not in visited)
    score -= free

    # 2. On évite les coins trop tôt
    if cell in [(0, 0), (0, COLS - 1), (ROWS - 1, 0), (ROWS - 1, COLS - 1)]:
        score -= 2

    return score


# --- 3. GR : construction gloutonne d’un cycle hamiltonien ---


def greedy_cycle(start: Pos = START) -> Tuple[Pos, ...] | None:
    visited: Set[Pos] = {start}
    path: List[Pos] = [start]
    current = start

    for _ in range(ROWS * COLS - 1):

        # voisins non visités
        candidates = [v for v in neighbors(current) if v not in visited]

        if not candidates:
            return None  # GR échoue

        # choisir le meilleur voisin selon l’heuristique
        best = max(candidates, key=lambda cell: evaluate_local_score(cell, visited))

        visited.add(best)
        path.append(best)
        current = best

    # vérifier si on peut revenir au départ
    if START in neighbors(current):
        path.append(START)
        return tuple(path)

    return None


# --- 4. Affichage (identique à ton script BTH) ---


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


CONNECTION_GLYPHS = {
    frozenset(("←", "→")): "─",
    frozenset(("↑", "↓")): "│",
    frozenset(("↓", "→")): "┌",
    frozenset(("↓", "←")): "┐",
    frozenset(("↑", "→")): "└",
    frozenset(("↑", "←")): "┘",
}


def print_cycle(cycle: Tuple[Pos, ...]) -> None:
    display = {}
    for i in range(len(cycle)):
        prev_pos = cycle[(i - 1) % len(cycle)]
        cur_pos = cycle[i]
        next_pos = cycle[(i + 1) % len(cycle)]

        in_dir = direction(cur_pos, prev_pos)
        out_dir = direction(cur_pos, next_pos)

        if cur_pos == START:
            display[cur_pos] = out_dir
        else:
            display[cur_pos] = CONNECTION_GLYPHS.get(frozenset((in_dir, out_dir)), "?")

    for r in range(ROWS - 1, -1, -1):
        print(" ".join(display[(r, c)] for c in range(COLS)))


# --- 5. Lancement ---


def main():
    cyc = greedy_cycle(START)

    if cyc is None:
        print("GR a échoué à construire un cycle.")
        return

    print("Cycle trouvé par GR :\n")
    print_cycle(cyc)


if __name__ == "__main__":
    cls()
    
    ROWS = 4
    COLS = ROWS
    
    main()
    
    end()
