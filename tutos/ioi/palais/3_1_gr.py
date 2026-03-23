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

    def ordered_candidates(current: Pos, seen: Set[Pos]) -> List[Pos]:
        candidates = [v for v in neighbors(current) if v not in seen]
        # Tri décroissant: meilleur score d'abord.
        return sorted(candidates, key=lambda cell: evaluate_local_score(cell, seen), reverse=True)

    def search(current: Pos) -> bool:
        if len(path) == ROWS * COLS:
            return start in neighbors(current)

        for nxt in ordered_candidates(current, visited):
            visited.add(nxt)
            path.append(nxt)

            if search(nxt):
                return True

            path.pop()
            visited.remove(nxt)
        return False

    if not search(start):
        return None

    path.append(start)
    return tuple(path)


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
    # Si le cycle est "fermé" (START répété en fin), on n'affiche qu'une seule fois cette case.
    nodes = cycle[:-1] if len(cycle) > 1 and cycle[0] == cycle[-1] else cycle
    display = {}
    for i in range(len(nodes)):
        prev_pos = nodes[(i - 1) % len(nodes)]
        cur_pos = nodes[i]
        next_pos = nodes[(i + 1) % len(nodes)]

        in_dir = direction(cur_pos, prev_pos)
        out_dir = direction(cur_pos, next_pos)

        if cur_pos == START:
            display[cur_pos] = "x"
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
    
    ROWS = 8
    COLS = ROWS
    
    main()
    
    end()
