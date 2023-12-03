from functools import partial
from math import prod
import re


with open("data") as f:
    games = f.readlines()

CUBES_REGEX = re.compile(r"(\d+) (blue|red|green)")

# ========== PART 1 ==========
MAX_PER_COLOR = {"red": 12, "green": 13, "blue": 14}


def is_possible(game: str) -> bool:
    for num, color in CUBES_REGEX.findall(game):
        if int(num) > MAX_PER_COLOR[color]:
            return False
    return True


print(sum(idx for idx, game in enumerate(games, 1) if is_possible(game)))


# ========== PART 2 ==========
def fewest_cubes_num(target: str, cubes: list) -> int:
    return max(int(num) for num, color in cubes if color == target)


def min_power_set(game: str) -> int:
    return prod(
        map(
            partial(fewest_cubes_num, cubes=CUBES_REGEX.findall(game)),
            ["red", "green", "blue"],
        )
    )


print(sum(min_power_set(game) for game in games))
