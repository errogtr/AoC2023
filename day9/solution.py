from itertools import pairwise


def get_next(sequence):
    last = sequence[-1]
    while any(sequence):
        sequence = [y - x for x, y in pairwise(sequence)]
        last += sequence[-1]
    return last


with open("data") as f:
    sequences = [[int(x) for x in l.split()] for l in f.readlines()]

# ========= PART 1 =========
print(sum(get_next(s) for s in sequences))

# ========= PART 2 =========
print(sum(get_next(s[::-1]) for s in sequences))
