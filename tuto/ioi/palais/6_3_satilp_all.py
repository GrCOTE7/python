from typing import Dict, List, Optional, Set, Tuple
from pymox_kit import cls, end, SB, R, bip_time, nf
from codetiming import Timer


try:
    from ortools.sat.python import cp_model  # type: ignore

    HAS_CP_SAT = True
except Exception:
    HAS_CP_SAT = False

try:
    import pulp  # type: ignore

    HAS_PULP = True
except Exception:
    HAS_PULP = False

START = (0, 0)
Pos = Tuple[int, int]

# Choix solveur: "auto", "cp_sat", "ilp"
SOLVER_MODE = "auto"
TIME_LIMIT_SECONDS = 120
MAX_ENUM_CELLS = 100
MAX_SOLUTIONS = 0 # 0 = sans limite
PRINT_EACH_SOLUTION = False


# --- 1. Voisins orthogonaux ---


def neighbors(pos: Pos) -> List[Pos]:
    r, c = pos
    result = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result


def _idx(pos: Pos) -> int:
    return pos[0] * COLS + pos[1]


def _pos(i: int) -> Pos:
    return (i // COLS, i % COLS)


def _build_directed_arcs() -> List[Tuple[int, int]]:
    n = ROWS * COLS
    arcs: List[Tuple[int, int]] = []
    for i in range(n):
        for nb in neighbors(_pos(i)):
            arcs.append((i, _idx(nb)))
    return arcs


def _decode_cycle_from_successor(
    successor: Dict[int, int], start_i: int, n: int
) -> Optional[Tuple[Pos, ...]]:
    order = [start_i]
    cur = start_i

    for _ in range(n - 1):
        nxt = successor.get(cur)
        if nxt is None:
            return None
        if nxt in order:
            return None
        order.append(nxt)
        cur = nxt

    if successor.get(cur) != start_i:
        return None

    nodes = [_pos(i) for i in order]
    nodes.append(_pos(start_i))
    return tuple(nodes)


# --- 2. Normalisation / anti-doublons ---


def _cycle_to_index_sequence(cycle: Tuple[Pos, ...]) -> Tuple[int, ...]:
    # Retire la fermeture START finale.
    nodes = cycle[:-1]
    return tuple(_idx(p) for p in nodes)


def _canonical_signature(cycle: Tuple[Pos, ...]) -> Tuple[int, ...]:
    seq = _cycle_to_index_sequence(cycle)

    # On garde la plus petite représentation entre sens direct et inverse,
    # en maintenant START en première position.
    rev = (seq[0],) + tuple(reversed(seq[1:]))
    return seq if seq <= rev else rev


# --- 3. Build modèles SAT/ILP ---


def _build_cp_sat_model(start_i: int, n: int, arcs: List[Tuple[int, int]]):
    model = cp_model.CpModel()

    x: Dict[Tuple[int, int], cp_model.IntVar] = {}
    for i, j in arcs:
        x[(i, j)] = model.NewBoolVar(f"x_{i}_{j}")

    out_arcs: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
    in_arcs: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
    for i, j in arcs:
        out_arcs[i].append((i, j))
        in_arcs[j].append((i, j))

    for i in range(n):
        model.Add(sum(x[a] for a in out_arcs[i]) == 1)
        model.Add(sum(x[a] for a in in_arcs[i]) == 1)

    # MTZ pour éliminer les sous-tours.
    u: Dict[int, cp_model.IntVar] = {}
    for i in range(n):
        if i == start_i:
            u[i] = model.NewIntVar(0, 0, f"u_{i}")
        else:
            u[i] = model.NewIntVar(1, n - 1, f"u_{i}")

    for i, j in arcs:
        if i == start_i or j == start_i:
            continue
        model.Add(u[i] + 1 <= u[j] + n * (1 - x[(i, j)]))

    return model, x


def _build_ilp_model(start_i: int, n: int, arcs: List[Tuple[int, int]]):
    model = pulp.LpProblem("ham_cycle_enum", pulp.LpMinimize)
    model += 0

    x = pulp.LpVariable.dicts("x", arcs, lowBound=0, upBound=1, cat=pulp.LpBinary)

    out_arcs: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
    in_arcs: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
    for i, j in arcs:
        out_arcs[i].append((i, j))
        in_arcs[j].append((i, j))

    for i in range(n):
        model += pulp.lpSum(x[a] for a in out_arcs[i]) == 1
        model += pulp.lpSum(x[a] for a in in_arcs[i]) == 1

    u: Dict[int, pulp.LpVariable] = {}
    for i in range(n):
        if i == start_i:
            u[i] = pulp.LpVariable(f"u_{i}", lowBound=0, upBound=0, cat=pulp.LpInteger)
        else:
            u[i] = pulp.LpVariable(
                f"u_{i}", lowBound=1, upBound=n - 1, cat=pulp.LpInteger
            )

    for i, j in arcs:
        if i == start_i or j == start_i:
            continue
        model += u[i] + 1 <= u[j] + n * (1 - x[(i, j)])

    return model, x


# --- 4. Énumération ---


def _enumerate_cp_sat(
    start_i: int, n: int, arcs: List[Tuple[int, int]]
) -> List[Tuple[Pos, ...]]:
    model, x = _build_cp_sat_model(start_i, n, arcs)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = float(TIME_LIMIT_SECONDS)
    solver.parameters.num_search_workers = 8

    raw_cycles: List[Tuple[Pos, ...]] = []
    seen: Set[Tuple[int, ...]] = set()

    while True:
        status = solver.Solve(model)
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            break

        successor: Dict[int, int] = {}
        active_arcs: List[Tuple[int, int]] = []
        for i, j in arcs:
            if solver.Value(x[(i, j)]) == 1:
                successor[i] = j
                active_arcs.append((i, j))

        cyc = _decode_cycle_from_successor(successor, start_i, n)
        if cyc is None:
            break

        sig = _canonical_signature(cyc)
        if sig not in seen:
            seen.add(sig)
            raw_cycles.append(cyc)
            if PRINT_EACH_SOLUTION:
                print(f"Solution {len(raw_cycles)}")
                print_cycle(cyc)
                print()

        # Clause de blocage: on interdit exactement cet ensemble d'arcs.
        model.Add(sum(x[a] for a in active_arcs) <= n - 1)

        if MAX_SOLUTIONS > 0 and len(raw_cycles) >= MAX_SOLUTIONS:
            break

    return raw_cycles


def _enumerate_ilp(
    start_i: int, n: int, arcs: List[Tuple[int, int]]
) -> List[Tuple[Pos, ...]]:
    model, x = _build_ilp_model(start_i, n, arcs)

    raw_cycles: List[Tuple[Pos, ...]] = []
    seen: Set[Tuple[int, ...]] = set()

    while True:
        solver = pulp.PULP_CBC_CMD(msg=False, timeLimit=TIME_LIMIT_SECONDS)
        status = model.solve(solver)

        if status != pulp.LpStatusOptimal:
            break

        successor: Dict[int, int] = {}
        active_arcs: List[Tuple[int, int]] = []
        for a in arcs:
            val = pulp.value(x[a])
            if val is not None and val > 0.5:
                successor[a[0]] = a[1]
                active_arcs.append(a)

        cyc = _decode_cycle_from_successor(successor, start_i, n)
        if cyc is None:
            break

        sig = _canonical_signature(cyc)
        if sig not in seen:
            seen.add(sig)
            raw_cycles.append(cyc)
            if PRINT_EACH_SOLUTION:
                print(f"Solution {len(raw_cycles)}")
                print_cycle(cyc)
                print()

        # Coupe d'exclusion ILP.
        model += pulp.lpSum(x[a] for a in active_arcs) <= n - 1

        if MAX_SOLUTIONS > 0 and len(raw_cycles) >= MAX_SOLUTIONS:
            break

    return raw_cycles


def enumerate_all_cycles_sat_ilp(
    start: Pos = START, mode: str = SOLVER_MODE
) -> List[Tuple[Pos, ...]]:
    if start != START:
        return []

    n = ROWS * COLS
    if ROWS < 2 or COLS < 2 or n % 2 == 1:
        return []

    if n > MAX_ENUM_CELLS:
        print(
            f"Enumeration limitee a {MAX_ENUM_CELLS} cases (ici {n}) pour eviter une explosion combinatoire."
        )
        return []

    start_i = _idx(start)
    arcs = _build_directed_arcs()
    mode = mode.lower()

    if mode == "cp_sat":
        return _enumerate_cp_sat(start_i, n, arcs) if HAS_CP_SAT else []

    if mode == "ilp":
        return _enumerate_ilp(start_i, n, arcs) if HAS_PULP else []

    if HAS_CP_SAT:
        return _enumerate_cp_sat(start_i, n, arcs)

    if HAS_PULP:
        return _enumerate_ilp(start_i, n, arcs)

    return []


# --- 5. Affichage ---


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


# --- 6. Lancement ---


@Timer(text="⏱️: {seconds:.2f} s")
def main() -> None:
    n = ROWS * COLS

    if ROWS < 2 or COLS < 2:
        print("Dimensions incompatibles: il faut au moins 2x2.")
        return

    if n % 2 == 1:
        print(
            "Dimensions incompatibles: un cycle hamiltonien est impossible sur un nombre impair de cases."
        )
        return

    if not HAS_CP_SAT and not HAS_PULP:
        print("Aucun solveur disponible. Installer 'ortools' (CP-SAT) ou 'pulp' (ILP).")
        return

    cycles = enumerate_all_cycles_sat_ilp(START, SOLVER_MODE)

    if not cycles:
        print(
            "Aucune solution enumeree (limite de taille, timeout, ou solveur indisponible)."
        )
        return

    backend = "CP-SAT" if HAS_CP_SAT and SOLVER_MODE in ("auto", "cp_sat") else "ILP"
    print(
        f"{SB}{len(cycles)}{R} solution{'s' if len(cycles)>1 else ''} par SAT/ILP ({backend}) pour {SB}{ROWS * COLS}{R} cases ( {SB}{ROWS}x{COLS}{R} )."
    )

    # Affiche un exemple pour vérification visuelle.
    print("\nExemple de solution :\n")
    print_cycle(cycles[0])


if __name__ == "__main__":

    cls()

    ROWS = 8
    COLS = ROWS

    main()

    end()
