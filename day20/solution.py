from copy import deepcopy
from math import lcm
import re

LOW = "low"
HIGH = "high"
ON = "on"
OFF = "off"
BROADCASTER = "broadcaster"
BUTTON = "button"


def parse_input(lines):
    modules = dict()
    for line in lines:
        src, dst = re.match(r"(.+) -> (.+)", line).groups()
        first, other = src[0], src[1:]
        destinations = dst.split(", ")
        if first in "%&":
            modules[other] = first, destinations
        else:
            modules[src] = src, destinations
    return modules


def init_state(modules):
    state = dict()
    for module, (module_type, _) in modules.items():
        match module_type:
            case "%":
                state[module] = OFF
            case "&":
                state[module] = {
                    m: LOW for m, (_, dst) in modules.items() if module in dst
                }
    return state


def flip_flop(dst, pulse, state):
    if pulse == LOW:
        if state[dst] == OFF:
            state[dst] = ON
            return HIGH
        else:
            state[dst] = OFF
            return LOW
    return None


def conjunction(dst, src, pulse, state):
    state[dst][src] = pulse
    if all(x == HIGH for x in state[dst].values()):
        return LOW
    return HIGH


def press(state, modules, trigger=""):
    lows = highs = 0
    time = 1
    while True:
        pulses = [(BUTTON, BROADCASTER, LOW)]
        while pulses:
            src, dst, pulse = pulses.pop(0)
            lows += pulse == LOW
            highs += pulse == HIGH
            if dst not in modules:  # sink module
                continue
            dst_type, next_modules = modules[dst]
            match dst_type:
                case "%":
                    next_pulse = flip_flop(dst, pulse, state)
                case "&":
                    next_pulse = conjunction(dst, src, pulse, state)
                case _:
                    next_pulse = LOW  # broadcaster
            if next_pulse:
                for m in next_modules:
                    pulses.append((dst, m, next_pulse))
            if dst == trigger and next_pulse == HIGH:  # for Part 2
                return time
        if not trigger and time == 1000:
            break
        time += 1
    return lows * highs


with open("data") as f:
    modules = parse_input(f.read().splitlines())

initial_state = init_state(modules)

# ==== PART 1 ====
print(press(deepcopy(initial_state), modules))

# ==== PART 2 ====
rx_src = next(m for m, (_, dst) in modules.items() if "rx" in dst)
print(lcm(*(press(deepcopy(initial_state), modules, t) for t in initial_state[rx_src])))
