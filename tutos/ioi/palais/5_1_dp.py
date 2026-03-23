from functools import lru_cache
from typing import Dict, List, Tuple
from pymox_kit import cls, end, SB, R, bip_time, nf

START = (0, 0)
Pos = Tuple[int, int]
MAX_DP_CELLS = 36

# --- 1. Voisins orthogonaux ---


def neighbors(pos: Pos) -> List[Pos]:
    r, c = pos
    result = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result


# --- 2. DP : cycle hamiltonien avec bitmask ---


def _idx(pos: Pos) -> int:
    return pos[0] * COLS + pos[1]


def _pos(i: int) -> Pos:
    return (i // COLS, i % COLS)


def dp_cycle(start: Pos = START) -> Tuple[Pos, ...] | None:
    if start != START:
        return None

    n = ROWS * COLS
    if ROWS < 2 or COLS < 2 or n > MAX_DP_CELLS:
        return None

    all_visited = (1 << n) - 1
    start_i = _idx(start)
    parent: Dict[Tuple[int, int], int] = {}

    @lru_cache(maxsize=None)
    def solve(pos_i: int, mask: int) -> bool:
        if mask == all_visited:
            return start in neighbors(_pos(pos_i))

        for nxt in neighbors(_pos(pos_i)):
            nxt_i = _idx(nxt)
            bit = 1 << nxt_i
            if mask & bit:
                continue

            new_mask = mask | bit
            if solve(nxt_i, new_mask):
                parent[(pos_i, mask)] = nxt_i
                return True
        return False

    start_mask = 1 << start_i
    if not solve(start_i, start_mask):
        return None

    path: List[Pos] = [start]
    pos_i, mask = start_i, start_mask
    while mask != all_visited:
        nxt_i = parent[(pos_i, mask)]
        path.append(_pos(nxt_i))
        mask |= 1 << nxt_i
        pos_i = nxt_i

    path.append(start)
    return tuple(path)


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
    n = ROWS * COLS

    if ROWS < 2 or COLS < 2:
        print("Dimensions incompatibles: il faut au moins 2x2.")
        return

    if n % 2:
        print("Dimensions incompatibles: un cycle hamiltonien est impossible sur un nombre impair de cases.")
        return

    if n > MAX_DP_CELLS:
        print(
            f"DP bitmask désactivé au-delà de {MAX_DP_CELLS} cases (ici {n}). "
            "Ce n'est pas incompatible mathématiquement, c'est une limite pratique de complexité."
        )
        return

    cyc = dp_cycle(START)

    if cyc is None:
        print("DP n'a pas trouvé de cycle malgré des dimensions compatibles.")
        return

    print("Cycle trouvé par DP :\n")
    print_cycle(cyc)


if __name__ == "__main__":
    cls()

    ROWS = 4
    COLS = ROWS

    main()

    end()
