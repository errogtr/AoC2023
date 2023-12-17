from tqdm import tqdm


UP, DOWN, LEFT, RIGHT = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def update(x, y, vx, vy, current):
    match current:
        case "|":
            return [(x, y, *UP), (x, y, *DOWN)] if vy == 0 else [(x, y, vx, vy)]
        case "-":
            return [(x, y, *LEFT), (x, y, *RIGHT)] if vx == 0 else [(x, y, vx, vy)]
        case "/":
            if vy == 0:
                return [(x, y, *UP)] if vx > 0 else [(x, y, *DOWN)]
            else:
                return [(x, y, *LEFT)] if vy > 0 else [(x, y, *RIGHT)]
        case "\\":
            if vy == 0:
                return [(x, y, *DOWN)] if vx > 0 else [(x, y, *UP)]
            else:
                return [(x, y, *RIGHT)] if vy > 0 else [(x, y, *LEFT)]
        case ".":
            return [(x, y, vx, vy)]


def energize(mirror_map, Lx, Ly, init_point, visited_edges=None):
    energized = set()
    init_points = [init_point]  # initial position and direction x, y, vx, vy
    while init_points:
        x, y, vx, vy = init_points.pop()
        x, y = (x + vx, y + vy)
        if x < 0 or x > Lx or y < 0 or y > Ly:
            # optimization trick: if an edge is visited outwards coming from the grid, then starting
            # a beam evolution from that edge is redundant
            if visited_edges is not None and vy == 0:
                visited_edges.add((x, y, -vx, vy))
            if visited_edges is not None and vx == 0:
                visited_edges.add((x, y, vx, -vy))
            continue
        if (x, y, vx, vy) in energized:
            continue
        energized.add((x, y, vx, vy))
        init_points += update(x, y, vx, vy, current=mirror_map[(x, y)])
    return len(set((x, y) for x, y, *_ in energized))


with open("data") as f:
    mirror_map = {(x, y): v for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}

Lx = max(x for x, _ in mirror_map)
Ly = max(y for _, y in mirror_map)

# ==== PART 1 ====
print(energize(mirror_map, Lx, Ly, (-1, 0, *RIGHT)))

# ==== PART 2 ====
init_points = list()
for x in range(Lx+1):
    init_points += [(x, -1, *DOWN), (x, Lx+1, *UP)]
for y in range(Ly+1):
    init_points += [(-1, y, *RIGHT), (Ly+1, y, *LEFT)]
visited_edges = set()
print(max(energize(mirror_map, Lx, Ly, pt, visited_edges) for pt in tqdm(init_points) if pt not in visited_edges))
