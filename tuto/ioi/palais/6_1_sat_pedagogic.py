from typing import Dict, List, Optional, Set, Tuple
from pymox_kit import cls, end, SB, R, bip_time, nf

START = (0, 0)
Pos = Tuple[int, int]
MAX_DPLL_CELLS = 100

# --- 1. Voisins orthogonaux ---


def neighbors(pos: Pos) -> List[Pos]:
    r, c = pos
    result = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result


# --- 2. SAT : encodage CNF + solveur DPLL ---


def _idx(pos: Pos) -> int:
    return pos[0] * COLS + pos[1]


def _pos(i: int) -> Pos:
    return (i // COLS, i % COLS)


def _add_exactly_one(clauses: List[List[int]], vars_list: List[int]) -> None:
    # Au moins une variable vraie.
    clauses.append(vars_list[:])
    # Au plus une variable vraie (encodage pairwise).
    for i in range(len(vars_list)):
        for j in range(i + 1, len(vars_list)):
            clauses.append([-vars_list[i], -vars_list[j]])


def _build_cycle_even_rows(rows: int, cols: int) -> List[Pos]:
    path: List[Pos] = []

    for c in range(cols):
        path.append((0, c))

    for r in range(1, rows):
        if r % 2 == 1:
            for c in range(cols - 1, 0, -1):
                path.append((r, c))
        else:
            for c in range(1, cols):
                path.append((r, c))

    for r in range(rows - 1, 0, -1):
        path.append((r, 0))

    return path


def _direct_cycle_fallback(start: Pos) -> Tuple[Pos, ...] | None:
    if start != START:
        return None

    if ROWS < 2 or COLS < 2 or (ROWS * COLS) % 2 == 1:
        return None

    if ROWS % 2 == 0:
        nodes = _build_cycle_even_rows(ROWS, COLS)
    elif COLS % 2 == 0:
        transposed = _build_cycle_even_rows(COLS, ROWS)
        nodes = [(c, r) for (r, c) in transposed]
    else:
        return None

    if not nodes or nodes[0] != START:
        return None

    return tuple(nodes + [START])


def _build_sat_instance(start: Pos) -> Tuple[List[List[int]], Dict[Tuple[int, int], int], Dict[int, Tuple[int, int]]]:
    n = ROWS * COLS

    # Variable x_(v,t): la case v est visitee au pas t.
    vt_to_var: Dict[Tuple[int, int], int] = {}
    var_to_vt: Dict[int, Tuple[int, int]] = {}
    next_var = 1
    for v in range(n):
        for t in range(n):
            vt_to_var[(v, t)] = next_var
            var_to_vt[next_var] = (v, t)
            next_var += 1

    clauses: List[List[int]] = []

    # 1) Chaque pas t contient exactement une case.
    for t in range(n):
        time_vars = [vt_to_var[(v, t)] for v in range(n)]
        _add_exactly_one(clauses, time_vars)

    # 2) Chaque case v apparait exactement une fois.
    for v in range(n):
        node_vars = [vt_to_var[(v, t)] for t in range(n)]
        _add_exactly_one(clauses, node_vars)

    start_i = _idx(start)

    # 3) Symetrie: START fixe au pas 0.
    clauses.append([vt_to_var[(start_i, 0)]])

    # 4) Adjacence entre pas consecutifs (chemin hamiltonien cyclique).
    adjacency: Dict[int, Set[int]] = {}
    for v in range(n):
        adjacency[v] = {_idx(p) for p in neighbors(_pos(v))}

    # Interdire transitions non-adjacentes pour t -> t+1.
    for t in range(n - 1):
        for v in range(n):
            xv_t = vt_to_var[(v, t)]
            allowed = adjacency[v]
            for u in range(n):
                if u not in allowed:
                    xu_next = vt_to_var[(u, t + 1)]
                    clauses.append([-xv_t, -xu_next])

    # Fermeture du cycle: dernier sommet adjacent au START.
    for v in range(n):
        if start_i not in adjacency[v]:
            clauses.append([-vt_to_var[(v, n - 1)]])

    return clauses, vt_to_var, var_to_vt


def _simplify_clauses(clauses: List[List[int]], lit: int) -> Optional[List[List[int]]]:
    simplified: List[List[int]] = []
    neg = -lit

    for clause in clauses:
        if lit in clause:
            continue

        if neg in clause:
            new_clause = [x for x in clause if x != neg]
            if not new_clause:
                return None
            simplified.append(new_clause)
        else:
            simplified.append(clause)

    return simplified


def _dpll(clauses: List[List[int]], assignment: Dict[int, bool]) -> Optional[Dict[int, bool]]:
    # Propagation unitaire.
    while True:
        unit = None
        for clause in clauses:
            if len(clause) == 0:
                return None
            if len(clause) == 1:
                unit = clause[0]
                break

        if unit is None:
            break

        var = abs(unit)
        val = unit > 0
        if var in assignment and assignment[var] != val:
            return None

        assignment[var] = val
        new_clauses = _simplify_clauses(clauses, unit)
        if new_clauses is None:
            return None
        clauses = new_clauses

    if not clauses:
        return assignment

    # Heuristique simple: variable la plus frequente.
    freq: Dict[int, int] = {}
    for clause in clauses:
        for lit in clause:
            v = abs(lit)
            if v not in assignment:
                freq[v] = freq.get(v, 0) + 1

    if not freq:
        return assignment

    var = max(freq, key=lambda v: freq[v])

    for val in (True, False):
        lit = var if val else -var
        local_assignment = assignment.copy()
        local_assignment[var] = val

        new_clauses = _simplify_clauses(clauses, lit)
        if new_clauses is None:
            continue

        result = _dpll(new_clauses, local_assignment)
        if result is not None:
            return result

    return None


def sat_cycle(start: Pos = START) -> Tuple[Pos, ...] | None:
    if start != START:
        return None

    n = ROWS * COLS
    if ROWS < 2 or COLS < 2:
        return None

    # Le DPLL pédagogique devient vite impraticable; on bascule vers une construction directe.
    if n > MAX_DPLL_CELLS:
        return _direct_cycle_fallback(start)

    clauses, _, var_to_vt = _build_sat_instance(start)
    model = _dpll(clauses, {})
    if model is None:
        return None

    order: Dict[int, int] = {}
    for var, value in model.items():
        if not value:
            continue
        if var not in var_to_vt:
            continue
        v, t = var_to_vt[var]
        order[t] = v

    if len(order) != n:
        return None

    nodes = [_pos(order[t]) for t in range(n)]
    nodes.append(start)
    return tuple(nodes)


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


def main() -> None:
    n = ROWS * COLS

    if ROWS < 2 or COLS < 2:
        print("Dimensions incompatibles: il faut au moins 2x2.")
        return

    if n % 2 == 1:
        print("Dimensions incompatibles: un cycle hamiltonien est impossible sur un nombre impair de cases.")
        return

    if n > MAX_DPLL_CELLS:
        print(
            f"SAT DPLL pedagogique trop couteux au-dela de {MAX_DPLL_CELLS} cases (ici {n}). "
            "Fallback automatique vers une construction directe (CO)."
        )

    cyc = sat_cycle(START)

    if cyc is None:
        print("SAT n'a pas trouve de cycle malgre des dimensions compatibles.")
        return

    print("Cycle trouve par SAT :\n")
    print_cycle(cyc)


if __name__ == "__main__":
    cls()

    ROWS = 6
    COLS = ROWS

    main()

    end()
