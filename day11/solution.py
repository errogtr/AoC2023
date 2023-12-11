from itertools import combinations

with open("data") as f:
    image = f.read().splitlines()

empty_rows = [y for y, row in enumerate(image) if all(x == "." for x in row)]
empty_cols = [x for x, col in enumerate(zip(*image)) if all(y == "." for y in "".join(col))]
galaxies = [(x, y) for y, row in enumerate(image) for x, v in enumerate(row) if v == "#"]

# ========= PART 1 =========
distances = 0
exp_counts = 0
for (g1_x, g1_y), (g2_x, g2_y) in combinations(galaxies, 2):
    expansion = 0
    expansion += sum(x in empty_cols for x in range(min(g1_x, g2_x), max(g1_x, g2_x)))
    expansion += sum(y in empty_rows for y in range(min(g1_y, g2_y), max(g1_y, g2_y)))
    exp_counts += expansion  # needed for Part 2
    distances += abs(g1_x - g2_x) + abs(g1_y - g2_y) + expansion
print(distances)

# ========= PART 2 =========
print(distances + exp_counts * 999998)
