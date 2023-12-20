from math import prod
import re


with open("data") as f:
    raw_workflows, ratings = f.read().split("\n\n", 1)


def parse_workflow(workflow):
    name, rules = re.match(r"(\w+)\{(.+)\}", workflow).groups()
    return name, rules


def compute_accepted(name, ranges, workflows):
    if name == "A":
        return [ranges]
    if name == "R":
        return []

    accepted = []
    *rules, fallback = workflows[name].split(",")
    while rules:
        char, op, sep, next_name = re.match(
            r"([xmas])([<>])(\d+):([ARa-z]+)", rules.pop(0)
        ).groups()
        a, b = ranges[char]
        match op:
            case "<":
                accepted += compute_accepted(
                    next_name, ranges | {char: (a, int(sep) - 1)}, workflows
                )
                ranges |= {char: (int(sep), b)}
            case ">":
                accepted += compute_accepted(
                    next_name, ranges | {char: (int(sep) + 1, b)}, workflows
                )
                ranges |= {char: (a, int(sep))}

    accepted += compute_accepted(fallback, ranges, workflows)
    return accepted


workflows = dict(parse_workflow(x) for x in raw_workflows.splitlines())
ranges = dict(zip("xmas", [(1, 4000)] * 4))
accepted = compute_accepted("in", ranges, workflows)

# ==== PART 1 ====
accepted_xmas = 0
for rating in ratings.splitlines():
    xmas = dict((c, int(v)) for c, v in re.findall(r"([xmas])=(\d+)", rating))
    for r in accepted:
        if all(a <= xmas[c] <= b for c, (a, b) in r.items()):
            accepted_xmas += sum(xmas.values())
            break
print(accepted_xmas)

# ==== PART 2 ====
print(sum(prod(b - a + 1 for a, b in r.values()) for r in accepted))
