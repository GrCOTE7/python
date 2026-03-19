from typing import List, Tuple, Optional
from pymox_kit import cls, end, SB, R, bip_time

START = (0, 0)
# Convention globale: on fixe le point de depart du cycle ici.

Pos = Tuple[int, int]
# Alias de lisibilite: une position est un tuple (ligne, colonne).

ROWS = 6
COLS = ROWS

# --- 1. Voisins orthogonaux ---


def neighbors(pos: Pos) -> List[Pos]:
    r, c = pos
    result = []
    # Voisinage 4-connecte (haut, bas, droite, gauche).
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # ↑, ↓, →, ←
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result


# --- 2. Pré-calcul du graphe de la grille ---


def build_graph() -> Tuple[List[Pos], List[List[int]], int]:
    # Enumeration ligne-major de toutes les cases de la grille.
    positions: List[Pos] = [(r, c) for r in range(ROWS) for c in range(COLS)]
    # Conversion position -> indice (acces O(1) pour construire les aretes).
    index = {p: i for i, p in enumerate(positions)}
    # Liste d'adjacence indexee: neigh[i] contient les voisins de i (en indices).
    neigh: List[List[int]] = [[] for _ in positions]

    for i, pos in enumerate(positions):
        neigh[i] = [index[v] for v in neighbors(pos)]

    # On renvoie aussi l'indice de START pour initialiser la recherche.
    return positions, neigh, index[START]


# --- 3. Backtracking optimisé pour trouver 1 cycle ---


def find_one_cycle_parity(start: Pos = START) -> Optional[Tuple[Pos, ...]]:
    if (ROWS * COLS) % 2:
        return None

    # Sur une grille bipartie, un cycle hamiltonien exige un nombre pair de cases.
    positions, neigh, start_i = build_graph()
    if start != START:
        # Garde le comportement explicite: ce script est spécialisé pour START.
        raise ValueError("Ce script parity optimisé utilise START comme point fixe")

    total = len(positions)
    start_parity = (start[0] + start[1]) & 1

    # Parite de la case de depart (0/1 selon (r + c) % 2).
    visited = [False] * total
    # Le chemin est stocke en indices pour eviter des conversions repetitives.
    path_idx = [start_i]
    visited[start_i] = True

    def onward_degree(node: int) -> int:
        # Heuristique de Warnsdorff: compter les sorties encore libres.
        return sum(1 for n in neigh[node] if not visited[n])

    # Depth-First Search avec backtracking et pruning.
    def dfs(current: int, depth: int) -> bool:
        if depth == total:
            # Cycle valide seulement si le dernier sommet reconnecte START.
            return start_i in neigh[current]

        # Dans un graphe biparti, la parite alterne a chaque pas.
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

    # Renvoie la direction "vue depuis a" pour aller vers b.
    if br == ar + 1 and bc == ac:
        return "↑"
    if br == ar - 1 and bc == ac:
        return "↓"
    if br == ar and bc == ac + 1:
        return "→"
    if br == ar and bc == ac - 1:
        return "←"

    return "?"


CONNECTION_GLYPHS: dict[frozenset[str], str] = {
    # Chaque case (hors START) a exactement 2 connexions: entree + sortie.
    # L'ensemble de ces deux directions determine le glyphe de liaison.
    frozenset(("←", "→")): "─",  # ALT + 196
    frozenset(("↑", "↓")): "│",  # ALT + 179
    frozenset(("↓", "→")): "┌",  # ALT + 218
    frozenset(("↓", "←")): "┐",  # ALT + 191
    frozenset(("↑", "→")): "└",  # ALT + 192
    frozenset(("↑", "←")): "┘",  # ALT + 217
}


def print_cycle(cycle: Tuple[Pos, ...]) -> None:
    display: dict[Pos, str] = {}
    for i in range(len(cycle)):
        # Indices circulaires pour relier premier et dernier sommet.
        prev_pos = cycle[(i - 1) % len(cycle)]
        cur_pos = cycle[i]
        next_pos = cycle[(i + 1) % len(cycle)]

        in_dir = direction(cur_pos, prev_pos)
        out_dir = direction(cur_pos, next_pos)

        if cur_pos == START:
            # Convention d'affichage: START montre seulement la direction de sortie.
            display[cur_pos] = out_dir
        else:
            display[cur_pos] = CONNECTION_GLYPHS.get(
                frozenset((in_dir, out_dir)),
                "?",
            )
    # Impression du haut vers le bas pour respecter la geometrie visuelle.
    for r in range(ROWS - 1, -1, -1):
        print(" ".join(display[(r, c)] for c in range(COLS)))


# --- 5. Lancement ---


def main(aff: int = 1):
    """_summary_

    Args:
        aff (int, optional): affiche. Defaults to 1.
    """
    cycle = find_one_cycle_parity(START)
    if cycle is None:
        print(f"Aucun cycle trouvé sur une grille {ROWS} x {COLS}")
        return
    print(f"Cycle trouvé sur une grille {ROWS} x {COLS}\n")
    if aff:
        print_cycle(cycle)


if __name__ == "__main__":

    cls()

    ROWS = 4
    COLS = ROWS

    main(1)

    end()
