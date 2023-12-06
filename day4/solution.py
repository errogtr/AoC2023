import re

with open("example") as f:
    lines = f.readlines()


# ========== PART 1 & 2 ==========
points = 0
cards_num = [1] * len(lines)
for i, numbers in enumerate(lines):
    winning_nums, my_nums = map(str.split, numbers.split("|"))
    my_winning_nums = len(set(winning_nums[2:]) & set(my_nums))
    points += 2**my_winning_nums // 2
    for j in range(my_winning_nums):
        cards_num[i + j + 1] += cards_num[i]

print(points, sum(cards_num), sep="\n")
