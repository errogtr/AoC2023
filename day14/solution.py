def cycle(platform):
    for _ in range(4):
        platform = rotate(tilt(platform))
    return platform


def rotate(platform):
    return ["".join(line) for line in zip(*map(reversed, platform))]


def tilt(platform):
    tilted_platform = list()
    for col in platform:
        tilted = list()
        for group in col.split("#"):
            if group:
                tilted.append("".join(["O"] * group.count("O") + ["."] * group.count(".")))
            else:
                tilted.append("")
        tilted_platform.append("#".join(tilted))
    return tilted_platform


def load(platform):
    return sum(sum(i * (c == "O") for i, c in enumerate(col[::-1], 1)) for col in platform)


with open("data") as f:
    platform = ["".join(c) for c in zip(*f.read().splitlines())]


# ==== PART 1 ====
print(load(tilt(platform)))

# ==== PART 2 ====
states = [platform]
period = transient = t = 0
target = 1_000_000_000
while True:
    end_cycle = cycle(states[t])
    if end_cycle in states:
        transient = states.index(end_cycle)
        period = t + 1 - states.index(end_cycle)
        break
    states.append(end_cycle)
    t += 1
print(load(states[(target - transient) % period + transient]))
