from typing import Dict, List, Optional, Tuple
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


# --- 2. Solveur CP-SAT (SAT) ---


def _solve_with_cp_sat(
    start_i: int, n: int, arcs: List[Tuple[int, int]]
) -> Optional[Tuple[Pos, ...]]:
    if not HAS_CP_SAT:
        return None

    model = cp_model.CpModel()

    x: Dict[Tuple[int, int], cp_model.IntVar] = {}
    for i, j in arcs:
        x[(i, j)] = model.NewBoolVar(f"x_{i}_{j}")

    out_arcs: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
    in_arcs: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
    for i, j in arcs:
        out_arcs[i].append((i, j))
        in_arcs[j].append((i, j))

    # Chaque sommet a exactement une sortie et une entrée.
    for i in range(n):
        model.Add(sum(x[a] for a in out_arcs[i]) == 1)
        model.Add(sum(x[a] for a in in_arcs[i]) == 1)

    # MTZ pour éliminer les sous-tours (ancre sur START).
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

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = float(TIME_LIMIT_SECONDS)
    solver.parameters.num_search_workers = 16

    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    successor: Dict[int, int] = {}
    for i, j in arcs:
        if solver.Value(x[(i, j)]) == 1:
            successor[i] = j

    if len(successor) != n:
        return None

    return _decode_cycle_from_successor(successor, start_i, n)


# --- 3. Solveur ILP (PuLP) ---


def _solve_with_ilp(
    start_i: int, n: int, arcs: List[Tuple[int, int]]
) -> Optional[Tuple[Pos, ...]]:
    if not HAS_PULP:
        return None

    model = pulp.LpProblem("hamiltonian_cycle_grid", pulp.LpMinimize)
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

    # CBC est généralement dispo avec PuLP; timeLimit en secondes.
    solver = pulp.PULP_CBC_CMD(msg=False, timeLimit=TIME_LIMIT_SECONDS)
    status = model.solve(solver)
    if (
        status != pulp.LpStatusOptimal
        and status != pulp.LpStatusNotSolved
        and status != pulp.LpStatusInfeasible
    ):
        return None

    if pulp.LpStatus[model.status] not in ("Optimal", "Not Solved"):
        return None

    successor: Dict[int, int] = {}
    for i, j in arcs:
        val = pulp.value(x[(i, j)])
        if val is not None and val > 0.5:
            successor[i] = j

    if len(successor) != n:
        return None

    return _decode_cycle_from_successor(successor, start_i, n)


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


# --- 4. API unifiée SAT/ILP ---


def solve_cycle_sat_ilp(
    start: Pos = START, mode: str = SOLVER_MODE
) -> Tuple[Pos, ...] | None:
    if start != START:
        return None

    n = ROWS * COLS
    if ROWS < 2 or COLS < 2 or n % 2 == 1:
        return None

    start_i = _idx(start)
    arcs = _build_directed_arcs()

    mode = mode.lower()
    if mode == "cp_sat":
        return _solve_with_cp_sat(start_i, n, arcs)

    if mode == "ilp":
        return _solve_with_ilp(start_i, n, arcs)

    # auto: priorité CP-SAT, puis ILP.
    cyc = _solve_with_cp_sat(start_i, n, arcs)
    if cyc is not None:
        return cyc
    return _solve_with_ilp(start_i, n, arcs)


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

cumul = 0


# @Timer(text="⏱️: {seconds:.2f} s")
def main(noAff=False) -> None:
    global cumul

    t = Timer(text="⏱️ {seconds:.2f} s")
    t.start()

    n = ROWS * COLS

    print(f"Grille de{SB}", ROWS, "x", COLS, f"{R}({n} cases)", end=" - ")

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

    cyc = solve_cycle_sat_ilp(START, SOLVER_MODE)

    if cyc is None:
        print(
            "Aucune solution trouvee avec le solveur courant (timeout, solver manquant, ou instance trop difficile)."
        )
        return

    # backend = "CP-SAT" if HAS_CP_SAT and SOLVER_MODE in ("auto", "cp_sat") else "ILP"
    # print(f"Cycle trouve par SAT/ILP ({backend}) :\n")

    t.stop()
    # elapsed = t.last
    # u = f"⏱️ {elapsed:.2f} s"
    # cumul = 0
    cumul += t.last
    # print (cumul, end=' ')

    if not noAff:
        print_cycle(cyc)


if __name__ == "__main__":
    cls()

    ROWS = 24

    nb =100

    for i in range(nb-1):
        COLS = ROWS
        print(f"{i+1: 3}", end=" ")
        main(True)
    print(f"{i+2: 3}", end=" ")
    main(False)
    print(f"CUMUL ⏱️ {cumul:.2f} s, soit moy. = {(cumul/(i+2)):.3f} s")

    end()
