import re

SUBS = dict(zip("0123", "RDLU"))


def parse(instructions):
    parsed = list()
    for instruction in instructions:
        direction, size = re.match(r"([DLRU])\s(\d+)", instruction).groups()
        parsed.append((direction, int(size)))
    return parsed


def fix(instructions):
    fixed = list()
    for instruction in instructions:
        size, direction = re.search(r"\(#(\w{5})(\d)\)", instruction).groups()
        fixed.append((SUBS[direction], int(size, 16)))
    return fixed


def lagoon(instructions):
    sx, sy = (0, 0)
    border = 0
    area = 0
    for direction, size in instructions:
        border += size
        match direction:
            case "D":
                cx, cy = (sx, sy + size)
            case "L":
                cx, cy = (sx - size, sy)
            case "R":
                cx, cy = (sx + size, sy)
            case "U":
                cx, cy = (sx, sy - size)
            case _:
                break
        area += (sx * cy - cx * sy) / 2
        sx, sy = cx, cy
    return int(area + border // 2 + 1)


with open("data") as f:
    digplan = f.read().splitlines()


# ==== PART 1 ====
print(lagoon(parse(digplan)))

# ==== PART 2 ====
print(lagoon(fix(digplan)))
