def symmetry(p, N):
    for i in range(1, N):
        if all(p[i - j - 1] == p[i + j] for j in range(min(i, N - i))):
            return i
    return 0


def smudge_symmetry(p, N):
    for i in range(1, N):
        if sum(hamming(p[i - j - 1], p[i + j]) for j in range(min(i, N - i))) == 1:
            return i
    return 0


def hamming(X, Y):
    return sum(x != y for x, y in zip(X, Y))


def summarize(pattern, smudge=False):
    rows = pattern.split()
    cols = ["".join(line) for line in zip(*rows)]
    if smudge:
        return 100 * smudge_symmetry(rows, len(rows)) or smudge_symmetry(cols, len(cols))
    return 100 * symmetry(rows, len(rows)) or symmetry(cols, len(cols))


with open("data") as f:
    patterns = f.read().split("\n\n")


# ========= PART 1 =========
print(sum(summarize(pattern) for pattern in patterns))


# ========= PART 2 =========
print(sum(summarize(pattern, smudge=True) for pattern in patterns))
