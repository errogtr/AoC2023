import re
from tqdm import tqdm

U, D, L, R = [(0, -1), (0, 1), (-1, 0), (1, 0)]

RULES = {
    "S": {U: "|7F", D: "|JL", L: "-FL", R: "-J7"},
    "|": {U: "|7F", D: "|JL"},
    "-": {L: "-FL", R: "-J7"},
    "F": {D: "|JL", R: "-J7"},
    "7": {D: "|JL", L: "-FL"},
    "L": {U: "|7F", R: "-J7"},
    "J": {U: "|7F", L: "-FL"},
}


def can_go(x, y, v_x, v_y, area_map, visited):
    a, b = x + v_x, y + v_y
    if (a, b) in visited:
        return False
    current = area_map[(x, y)]
    candidate = area_map[(a, b)]
    if candidate in RULES[current][(v_x, v_y)]:
        return True
    return False


with open("data") as f:
    area_map = {(x, y): v for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}

x, y = next(p for p, v in area_map.items() if v == "S")
visited = [(x, y)]
u, w = next((x + v_x, y + v_y) for v_x, v_y in RULES[area_map[(x, y)]] if can_go(x, y, v_x, v_y, area_map, visited))
while (u, w) != (x, y):
    visited.append((u, w))
    x, y = (u, w)
    try:
        u, w = next((x + v_x, y + v_y) for v_x, v_y in RULES[area_map[(x, y)]] if can_go(x, y, v_x, v_y, area_map, visited))
    except StopIteration:
        pass
print(len(visited) // 2)

area_map[next(p for p, v in area_map.items() if v == "S")] = "J"
max_y = max(y for y, _ in area_map)
enclosed = 0
for y in tqdm(range(max_y + 1)):
    min_x = min([x for x, z in visited if z == y], default=0)
    max_x = max([x for x, z in visited if z == y], default=-1)
    ray = "".join(area_map[(x, y)] if (x, y) in visited else "." for x in range(min_x, max_x + 1))
    ray_ = re.sub(r"(-+|F-*7|L-*J|)", "", ray)
    ray__ = re.sub(r"(FJ|L7)", "|", ray_)
    for i, c in enumerate(ray__):
        if c == ".":
            enclosed += ray__[i:].count("|") % 2
print(enclosed)
