from typing import List, Tuple
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


# --- 2. CO : construction directe d’un cycle hamiltonien ---


def _build_cycle_even_rows(rows: int, cols: int) -> List[Pos]:
    # Construit un cycle en O(rows*cols) si rows est pair.
    path: List[Pos] = []

    # Ligne 0 complete.
    for c in range(cols):
        path.append((0, c))

    # Lignes 1..rows-1 sans la colonne 0 (reservee pour la fermeture).
    for r in range(1, rows):
        if r % 2 == 1:
            for c in range(cols - 1, 0, -1):
                path.append((r, c))
        else:
            for c in range(1, cols):
                path.append((r, c))

    # Colonne 0 pour remonter et fermer le cycle.
    for r in range(rows - 1, 0, -1):
        path.append((r, 0))

    return path


def _is_valid_cycle(nodes: List[Pos], rows: int, cols: int, start: Pos) -> bool:
    if not nodes or nodes[0] != start:
        return False
    if len(nodes) != rows * cols:
        return False
    if len(set(nodes)) != rows * cols:
        return False

    for i in range(len(nodes)):
        a = nodes[i]
        b = nodes[(i + 1) % len(nodes)]
        if b not in [
            (a[0] + 1, a[1]),
            (a[0] - 1, a[1]),
            (a[0], a[1] + 1),
            (a[0], a[1] - 1),
        ]:
            return False
        if not (0 <= b[0] < rows and 0 <= b[1] < cols):
            return False

    return True


def direct_cycle(start: Pos = START) -> Tuple[Pos, ...] | None:
    if start != START:
        return None

    if ROWS < 2 or COLS < 2 or (ROWS * COLS) % 2 == 1:
        return None

    if ROWS % 2 == 0:
        nodes = _build_cycle_even_rows(ROWS, COLS)
    elif COLS % 2 == 0:
        # Construction sur la grille transposee, puis re-projection.
        transposed = _build_cycle_even_rows(COLS, ROWS)
        nodes = [(c, r) for (r, c) in transposed]
    else:
        return None

    if not _is_valid_cycle(nodes, ROWS, COLS, START):
        return None

    return tuple(nodes + [START])


# --- 3. Affichage ---


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


# --- 4. Lancement ---


def main():
    cyc = direct_cycle(START)

    if cyc is None:
        print("CO n'a pas pu construire de cycle (dimensions incompatibles).")
        return

    print("Cycle trouvé par CO :\n")
    print_cycle(cyc)


if __name__ == "__main__":
    cls()
    
    ROWS = 10
    COLS = ROWS
    
    main()
    
    end()
