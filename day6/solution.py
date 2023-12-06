from math import sqrt, prod
import re


def num_kerning(text):
    return int(re.sub(r"[^0-9]", "", text))


def nums(text):
    return map(int, re.findall(r"\d+", text))


def x_span(t, d):
    return int(2 * (t // 2 - (t - sqrt(t**2 - 4 * d)) // 2) - (1 - t % 2))


with open("data") as f:
    time, distance = f.read().split("\n")

# ========= PART 1 =========
print(prod(x_span(t, d) for t, d in zip(nums(time), nums(distance))))

# ========= PART 2 =========
print(x_span(num_kerning(time), num_kerning(distance)))
