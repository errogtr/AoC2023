with open("data") as f:
    lines = [l.split() for l in f.readlines()]


# ========== PART 1 & 2 ==========
points = 0
cards_num = [1] * len(lines)
for i, numbers in enumerate(lines):
    my_winning_nums = len(set(numbers[2:12]) & set(numbers[13:]))
    points += 2**my_winning_nums // 2
    for j in range(my_winning_nums):
        cards_num[i + j + 1] += cards_num[i]

print(points, sum(cards_num), sep="\n")
