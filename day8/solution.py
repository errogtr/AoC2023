from itertools import cycle
from math import lcm


NODE_SELECTOR = {"L": 0, "R": 1}


def steps(current, network, stopping):
    for step, direction in enumerate(cycle(instructions), 1):
        next_element = network[current]
        current = next_element[NODE_SELECTOR[direction]]
        if stopping(current):
            return step


with open("data") as f:
    instructions, _, *network = f.read().split("\n")

# parsing '(AAA) = (BBB, CCC)'
network = {l[:3]: (l[7:10], l[12:15]) for l in network}


# ========= PART 1 =========
print(steps("AAA", network, stopping=lambda x: x == "ZZZ"))

# ========= PART 2 ==========
all_steps = [
    steps(k, network, stopping=lambda x: x.endswith("Z"))
    for k in network
    if k.endswith("A")
]
print(lcm(*all_steps))
