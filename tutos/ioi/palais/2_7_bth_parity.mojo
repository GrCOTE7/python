# parity-only Hamiltonian cycle on an orthogonal grid
# Mojo version focused on speed for even grids (e.g. 8x8)

alias ROWS = 4
alias COLS = 4

# ❌ Faire marcher ce script en Mojo

@value
struct Pos:
    var r: Int
    var c: Int

    fn __init__(inout self, r: Int, c: Int):
        self.r = r
        self.c = c


fn construct_cycle_cols_even(rows: Int, cols: Int) -> List[Pos]:
    var cycle = List[Pos]()

    # 1) top row: left to right
    for c in range(cols):
        cycle.append(Pos(0, c))

    # 2) snake through columns [cols-1 .. 1], skipping top row
    var go_down = True
    for c in range(cols - 1, 0, -1):
        if go_down:
            for r in range(1, rows):
                cycle.append(Pos(r, c))
        else:
            for r in range(rows - 1, 0, -1):
                cycle.append(Pos(r, c))
        go_down = not go_down

    # 3) close through column 0 from bottom to row 1
    for r in range(rows - 1, 0, -1):
        cycle.append(Pos(r, 0))

    return cycle


fn rotate_cycle(cycle: List[Pos], start: Pos) -> List[Pos]:
    var start_index = -1
    for i in range(len(cycle)):
        if cycle[i].r == start.r and cycle[i].c == start.c:
            start_index = i
            break

    if start_index < 0:
        return List[Pos]()

    var rotated = List[Pos]()
    for i in range(start_index, len(cycle)):
        rotated.append(cycle[i])
    for i in range(0, start_index):
        rotated.append(cycle[i])
    return rotated


fn find_one_cycle_parity(start: Pos) -> List[Pos]:
    if ROWS < 2 or COLS < 2:
        return List[Pos]()
    if (ROWS * COLS) % 2 != 0:
        return List[Pos]()

    var cycle = List[Pos]()

    if COLS % 2 == 0:
        cycle = construct_cycle_cols_even(ROWS, COLS)
    elif ROWS % 2 == 0:
        # build on transposed grid, then map back
        let t = construct_cycle_cols_even(COLS, ROWS)
        for p in t:
            cycle.append(Pos(p.c, p.r))
    else:
        return List[Pos]()

    return rotate_cycle(cycle, start)


fn direction(a: Pos, b: Pos) -> String:
    if b.r == a.r + 1 and b.c == a.c:
        return "U"
    if b.r == a.r - 1 and b.c == a.c:
        return "D"
    if b.r == a.r and b.c == a.c + 1:
        return "R"
    if b.r == a.r and b.c == a.c - 1:
        return "L"
    return "?"


fn print_cycle(cycle: List[Pos]):
    if len(cycle) == 0:
        print("No cycle")
        return

    var arrows = List[String]()
    for _ in range(ROWS * COLS):
        arrows.append("?")

    for i in range(len(cycle)):
        let a = cycle[i]
        let b = cycle[(i + 1) % len(cycle)]
        arrows[a.r * COLS + a.c] = direction(a, b)

    for r in range(ROWS - 1, -1, -1):
        var line = String("")
        for c in range(COLS):
            if c > 0:
                line += " "
            line += arrows[r * COLS + c]
        print(line)


fn main():
    let start = Pos(0, 0)
    let cycle = find_one_cycle_parity(start)

    print("Method: parity")
    if len(cycle) == 0:
        print("No Hamiltonian cycle found")
        return

    print("Hamiltonian cycle found on", ROWS, "x", COLS)
    print_cycle(cycle)
