from functools import lru_cache


@lru_cache
def arrange(record, groups):
    if not record:
        return groups == ()

    if not groups:
        return "#" not in record

    result = 0

    if record[0] in ".?":
        result += arrange(record[1:], groups)

    if record[0] in "#?":
        if (
            (curr := groups[0]) <= len(record)
            and "." not in record[: curr]
            and (curr == len(record) or record[curr] != "#")
        ):
            result += arrange(record[curr + 1:], groups[1:])

    return result


def unfold(r, g):
    return "?".join([r] * 5), g * 5


def parse_record(record):
    springs, groups = record.split()
    return springs, tuple(int(x) for x in groups.split(","))


with open("data") as f:
    records = [parse_record(r) for r in f.read().splitlines()]

# ========= PART 1 =========
print(sum(arrange(r, g) for r, g in records))

# ========= PART 2 =========
print(sum(arrange(*unfold(r, g)) for r, g in records))
