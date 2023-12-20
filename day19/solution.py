from functools import partial
from operator import lt, gt
from math import  prod
import re

OP = {">": gt, "<": lt}


def parse_single_rule(rule):
    def _check(part, category, op, value, dst):
        if op(part[category], value):
            return dst
        return None
    category, op, value, dst = re.match(r"([xmas])([<>])(\d+):([ARa-z]+)", rule).groups()
    return partial(_check, category=category, op=OP[op], value=int(value), dst=dst)


def parse_workflow(workflow):
    name, rules = re.search(r"(\w+)\{(.+)\}", workflow).groups()
    *single_rules, fallback = rules.split(",")
    return name, ([parse_single_rule(rule) for rule in single_rules], fallback)


def parse_rating(rating):
    splits = [r.split("=") for r in re.findall(r"\w=\d+", rating)]
    return {cat: int(val) for cat, val in splits}


def run(workflow, ratings):
    rules, fallback = workflow
    for rule in rules:
        if dst := rule(ratings):
            return dst
    return fallback


with open("data") as f:
    raw_workflows, ratings = f.read().split("\n\n", 1)

workflows = dict(parse_workflow(w) for w in raw_workflows.split("\n"))
accepted = 0
for rating in ratings.split("\n"):
    rating_vals = parse_rating(rating)
    name = "in"
    while name not in "AR":
        name = run(workflows[name], rating_vals)
        if name == "A":
            accepted += sum(rating_vals.values())
print(accepted)


def parse_workflow_2(line):
    name, rules = re.match(r"(\w+)\{(.+)\}", line).groups()
    *single_rules, fallback = rules.split(",")
    return name, (single_rules, fallback)


def compute_accepted(name, intervals, workflows):
    if name == "A":
        return prod(b - a + 1 for a, b in intervals.values())
    if name == "R":
        return 0

    rules, fallback = workflows[name]
    accepted = 0
    while rules:
        char, op, sep, next_name = re.match(r"([xmas])([<>])(\d+):([ARa-z]+)", rules.pop(0)).groups()
        a, b = intervals[char]
        if op == "<":
            accepted += compute_accepted(next_name, intervals | {char: (a, int(sep) - 1)}, workflows)
            intervals |= {char: (int(sep), b)}
        else:
            accepted += compute_accepted(next_name, intervals | {char: (int(sep) + 1, b)}, workflows)
            intervals |= {char: (a, int(sep))}

    accepted += compute_accepted(fallback, intervals, workflows)
    return accepted


workflows_2 = dict(parse_workflow_2(x) for x in raw_workflows.split("\n"))
intervals = dict(zip("xmas", [(1, 4000)] * 4))
print(compute_accepted("in", intervals, workflows_2))
