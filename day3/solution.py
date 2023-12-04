import re
from collections import defaultdict
from math import prod

with open("data") as f:
    lines = f.read().split("\n")

# building symbols grid as {xy_position: symbol}
symbols = dict()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c not in "1234567890.":
            symbols[(x, y)] = c

# checking if a number has a rectangular neighborhood containing a symbol and
# building a grid as {symbol_position: [part numbers list]}
part_numbers = defaultdict(list)
part_numbers_sum = 0
for y, line in enumerate(lines):
    for num in re.finditer(r"\d+", line):
        for s_x, s_y in symbols:
            if (num.start() - 1 <= s_x <= num.end()) and (y - 1 <= s_y <= y + 1):
                int_num = int(num.group())
                part_numbers[(s_x, s_y)].append(int_num)
                part_numbers_sum += int_num
                break

# ========= PART 1 =========
print(part_numbers_sum)

# ========= PART 2 =========
print(
    sum(
        prod(parts)
        for pos, parts in part_numbers.items()
        if len(parts) == 2 and symbols[pos] == "*"
    )
)
