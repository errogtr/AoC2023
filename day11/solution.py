from itertools import combinations


def voids(voids_list, a, b):
    return sum(min(a, b) < x < max(a, b) for x in voids_list)


with open("data") as f:
    image = f.read().splitlines()

empty_rows = [y for y, row in enumerate(image) if not row.count("#")]
empty_cols = [x for x, col in enumerate(zip(*image)) if not "".join(col).count("#")]
galaxies = [
    (x, y) for y, row in enumerate(image) for x, v in enumerate(row) if v == "#"
]

# ========= PART 1 =========
distances = 0
exp_counts = 0
for (g1_x, g1_y), (g2_x, g2_y) in combinations(galaxies, 2):
    expansion = voids(empty_cols, g1_x, g2_x) + voids(empty_rows, g1_y, g2_y)
    exp_counts += expansion  # needed for Part 2
    distances += abs(g1_x - g2_x) + abs(g1_y - g2_y) + expansion
print(distances)

# ========= PART 2 =========
print(distances + exp_counts * 999998)
