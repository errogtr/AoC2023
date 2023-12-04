import re

with open("data") as f:
    lines = f.read().splitlines()


# ========== PART 1 & 2 ==========
points = 0
cards_num = [1] * len(lines)
for i, line in enumerate(lines):
    winning_numbers, my_numbers = map(
        str.split, re.sub(r"Card\s+\d:", "", line).split("|")
    )
    my_winning_numbers = len(set(winning_numbers) & set(my_numbers))
    points += 2**my_winning_numbers // 2
    for j in range(i + 1, i + my_winning_numbers + 1):
        cards_num[j] += cards_num[i]

print(points, sum(cards_num), sep="\n")
