import re

with open("data") as f:
    lines = f.read().splitlines()


# ========== PART 1 & 2 ==========
points = 0
cards_num = [1] * len(lines)
for i, line in enumerate(lines):
    winning_nums, my_nums = map(str.split, re.sub(r"Card\s+\d:", "", line).split("|"))
    my_winning_nums = len(set(winning_nums) & set(my_nums))
    points += 2**my_winning_nums // 2
    for j in range(i + 1, i + my_winning_nums + 1):
        cards_num[j] += cards_num[i]

print(points, sum(cards_num), sep="\n")