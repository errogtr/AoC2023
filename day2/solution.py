import re

with open("data") as f:
    games = f.readlines()

CUBES_REGEX = re.compile(r"(\d+) (blue|red|green)")

# PART 1
MAX_PER_COLOR = {"red": 12, "green": 13, "blue": 14}


def is_possible(game: str) -> bool:
    for num, color in CUBES_REGEX.findall(game):
        if int(num) > MAX_PER_COLOR[color]:
            return False
    return True


print(sum(idx for idx, game in enumerate(games, 1) if is_possible(game)))


# PART 2
def get_min_cubes(target: str, cubes: list) -> int:
    return max(int(num) for num, color in cubes if color == target)


def min_power_set(game: str) -> int:
    cubes = CUBES_REGEX.findall(game)
    min_reds = get_min_cubes("red", cubes)
    min_greens = get_min_cubes("green", cubes)
    min_blues = get_min_cubes("blue", cubes)
    return min_reds * min_greens * min_blues


print(sum(min_power_set(game) for game in games))
