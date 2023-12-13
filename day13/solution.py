MEMORY = dict()
SUBS = {"#": ".", ".": "#"}


def symmetry(p, skip=None):
    N = len(p)
    for i in range(1, N):
        if skip is not None and i == skip:
            continue
        if all(p[i - j - 1] == p[i + j] for j in range(min(i, N - i))):
            return i
    return 0


def summarize(pattern, skip=None):
    rows = pattern.split()
    cols = ["".join(line) for line in zip(*rows)]
    if skip:
        idx, direction = skip
        if direction == "h":
            h_symmetry = symmetry(rows, idx)
            v_symmetry = symmetry(cols)
        else:
            h_symmetry = symmetry(rows)
            v_symmetry = symmetry(cols, idx)
    else:
        if h_symmetry := symmetry(rows):
            MEMORY[pattern] = h_symmetry, "h"
        if v_symmetry := symmetry(cols):
            MEMORY[pattern] = v_symmetry, "v"
    return 100 * h_symmetry + v_symmetry


def smudge(pattern):
    skip = MEMORY[pattern]
    for i, c in enumerate(pattern):
        if c not in SUBS:  # skip newline char
            continue
        smudged = pattern[:i] + SUBS[c] + pattern[i + 1:]
        if s := summarize(smudged, skip):
            return s


with open("data") as f:
    patterns = f.read().split("\n\n")


# ========= PART 1 =========
print(sum(summarize(pattern) for pattern in patterns))


# ========= PART 2 =========
print(sum(smudge(pattern) for pattern in patterns))
