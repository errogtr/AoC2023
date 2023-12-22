from copy import copy


def _print(plots):
    print("\n".join(plots))
    print("")


def nn(x, y):
    return [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]


def in_grid(x, y, Lx, Ly):
    return 0 <= x <= Lx and 0 <= y <= Ly


with open("data") as f:
    garden = f.read().splitlines()
Lx = len(garden[0])
Ly = len(garden)

start = next((x, y) for y, row in enumerate(garden) for x, v in enumerate(row) if v == 'S')
plots = {(0, 65)}
for r in range(65):
    snapshot = copy(garden)
    next_plots = set()
    for pt in plots:
        for (x, y) in nn(*pt):
            if in_grid(x, y, Lx, Ly) and garden[y][x] in "S.":
                next_plots.add((x, y))
    for (x, y) in next_plots:
        snapshot[y] = snapshot[y][:x] + "O" + snapshot[y][x + 1:]
    csv_snapshot = "\n".join(",".join(list(line)) for line in snapshot)
    with open(f"snapshot_{r+1}.csv", "w") as f:
        f.write(csv_snapshot)
    plots = next_plots
