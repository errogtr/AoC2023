from functools import cache


@cache
def update(x, y, vx, vy, current):
    match current:
        case "|":
            return [(x, y, 0, -1), (x, y, 0, 1)] if vy == 0 else [(x, y, vx, vy)]
        case "-":
            return [(x, y, -1, 0), (x, y, 1, 0)] if vx == 0 else [(x, y, vx, vy)]
        case "/":
            if vy == 0:
                return [(x, y, 0, -1)] if vx > 0 else [(x, y, 0, 1)]
            else:
                return [(x, y, -1, 0)] if vy > 0 else [(x, y, 1, 0)]
        case "\\":
            if vy == 0:
                return [(x, y, 0, 1)] if vx > 0 else [(x, y, 0, -1)]
            else:
                return [(x, y, 1, 0)] if vy > 0 else [(x, y, -1, 0)]
        case ".":
            return [(x, y, vx, vy)]


def energize(mirror_map, Lx, Ly, init_point):
    energized = set()
    init_points = [init_point]  # initial position and direction x, y, vx, vy
    while init_points:
        x, y, vx, vy = init_points.pop()
        x, y = (x + vx, y + vy)
        if x < 0 or x > Lx or y < 0 or y > Ly or (x, y, vx, vy) in energized:
            continue
        energized.add((x, y, vx, vy))
        init_points += update(x, y, vx, vy, current=mirror_map[(x, y)])
    return len(set((x, y) for x, y, *_ in energized))


with open("data") as f:
    mirror_map = {(x, y): v for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}

Lx = max(x for x, _ in mirror_map)
Ly = max(y for _, y in mirror_map)

# ==== PART 1 ====
print(energize(mirror_map, Lx, Ly, (-1, 0, 1, 0)))

# ==== PART 2 ====
init_points = list()
for x in range(Lx+1):
    init_points += [(x, -1, 0, 1), (x, Lx+1, 0, -1)]
for y in range(Ly+1):
    init_points += [(-1, y, 1, 0), (Ly+1, y, -1, 0)]
print(max(energize(mirror_map, Lx, Ly, pt) for pt in init_points))
