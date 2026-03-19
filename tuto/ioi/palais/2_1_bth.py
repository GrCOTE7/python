from typing import List, Tuple, Dict, Set
from pymox_kit import cls, end, SB, R

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


# --- ★ Ajout : heuristique de degré (Warnsdorff) ---


def degree(pos: Pos, visited: Dict[Pos, bool]) -> int:
    """Nombre de voisins libres autour de pos."""
    return sum(1 for v in neighbors(pos) if not visited[v])


def dist_center(pos: Pos) -> float:
    """Distance de Manhattan au centre géométrique de la grille."""
    r, c = pos
    cr = (ROWS - 1) / 2
    cc = (COLS - 1) / 2
    return abs(r - cr) + abs(c - cc)


def dist_start(pos: Pos, start: Pos = START) -> int:
    """Distance de Manhattan à la case de départ."""
    r, c = pos
    sr, sc = start
    return abs(r - sr) + abs(c - sc)


def parity_ok(pos: Pos, path: List[Pos], start: Pos = START) -> bool:
    """Vérifie que la parité correspond à l'étape suivante du chemin."""
    expected_parity = (start[0] + start[1] + len(path)) % 2
    return (pos[0] + pos[1]) % 2 == expected_parity


def dist_border(pos: Pos) -> int:
    """Distance à la frontière la plus proche (plus petit = plus près du bord)."""
    r, c = pos
    return min(r, c, ROWS - 1 - r, COLS - 1 - c)


def select_moves(method, current, visited, path):
    moves = [v for v in neighbors(current) if not visited[v]]

    if method == "bth":
        moves.sort(key=lambda v: degree(v, visited))

    elif method == "bth++":
        moves.sort(key=lambda v: (degree(v, visited), dist_center(v)))

    elif method == "bth+++":
        moves.sort(
            key=lambda v: (
                degree(v, visited),
                (len(path) % 2),  # parité
                dist_start(v),  # distance à START
            )
        )

    elif method == "parity":
        moves = [v for v in moves if parity_ok(v, path)]

    elif method == "frontier":
        moves.sort(key=lambda v: (degree(v, visited), dist_border(v)))

    else:
        raise ValueError(f"Méthode inconnue : {method}")

    return moves


# --- 3. Backtracking + Heuristics (BTH) ---


def backtrack_core(current, visited, path, start, total, solutions, method):
    if len(path) == total:
        if start in neighbors(current):
            norm = normalize_cycle(path.copy())
            solutions.add(norm)
        return

    # Appel à la fonction heuristique
    moves = select_moves(method, current, visited, path)

    for nxt in moves:
        visited[nxt] = True
        path.append(nxt)
        backtrack_core(nxt, visited, path, start, total, solutions, method)
        visited[nxt] = False
        path.pop()


def find_all_cycles(method: str = "bth", start: Pos = START) -> List[Tuple[Pos, ...]]:
    """<p>Args:</p>

    <p><strong>method (str, optional)</strong> — Méthodes disponibles :</p>
    <ul><li><strong>"BTH"</strong> — Backtracking + Warnsdorff : tri par degré simple(défaut)</li>
    <li><strong>"BTH++"</strong> — BTH + tie‑breaking : tri par degré + critère secondaire</li>
    <li><strong>"BTH+++"</strong> — BTH + tie‑breaking dynamique : critère secondaire dépendant du step, de la parité, ou de la distance à START</li>
    <li><strong>"parity"</strong> — BTH + filtre de parité : élimine les voisins qui violent la parité du chemin</li>
    <li><strong>"frontier"</strong> — BTH + tie‑breaking frontière : favorise les cases proches de la frontière (très efficace)</li></ul>
    <p><strong>start (Pos, optional)</strong> — Position de départ. Defaults to START.</p>
    Returns:
    <p>List[Tuple[Pos, ...]]: Liste des cycles hamiltoniens distincts trouvés.</p>
    """
    method = method.lower()
    visited = {(r, c): False for r in range(ROWS) for c in range(COLS)}
    visited[start] = True
    path = [start]
    total = ROWS * COLS
    solutions: Set[Tuple[Pos, ...]] = set()

    backtrack_core(start, visited, path, start, total, solutions, method)
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
    arrows = {}
    for i in range(len(cycle)):
        a = cycle[i]
        b = cycle[(i + 1) % len(cycle)]
        arrows[a] = direction(a, b)

    for r in range(ROWS - 1, -1, -1):
        print(" ".join(arrows[(r, c)] for c in range(COLS)))


# --- 6. Lancement ---


def main(method: str = "BTH", aff: int = 1):
    """_summary_

    Args:
        method (str, optional):
        ++       : tie-breaking
        +++      : tie-breaking dynamic - Tie‑breaking dépendant du step, de la parité, ou de la distance à START.
        parity   : On élimine les voisins qui violent la parité du chemin.
        frontier : Tie‑breaking basé sur la distance à la frontière (très efficace).
        Defaults to BTH.
        aff (int, optional): affiche. Defaults to 1.
    """
    all_cycles = find_all_cycles(method)
    print(
        f"Méthode: {SB}{method}{R}\nNombre de cycles hamiltoniens distincts sur une grille de {ROWS} x {COLS} : {len(all_cycles)}\n"
    )

    if aff:
        for i, cyc in enumerate(all_cycles, 1):
            print("─" * 8, i)
            print_cycle(cyc)


import json, os, sys, shutil, time, tempfile

if __name__ == "__main__":
    ROWS = 4
    COLS = ROWS

    import time

    def top():
        return time.time()

    def fin(top):
        fin = time.time()
        print(f"Temps écoulé : {fin - top:.2f} secondes")

    cls()

    t1 = top()
    main("bth", 0)
    fin(t1)
    end()

    t1 = top()
    main("bth++", 0)
    fin(t1)
    end()

    t1 = top()
    main("bth+++", 0)
    fin(t1)
    end()

    t1 = top()
    main("parity", 0)
    fin(t1)
    end()

    t1 = top()
    main("frontier", 1)
    fin(t1)
    end()
