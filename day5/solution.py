import re


def locations(seed_intervals):
    for maps_block in input_maps.split("\n\n"):
        mappings = maps_block.split("\n")[1:]
        images = list()
        while seed_intervals:
            x, y = seed_intervals.pop()
            for mapping in mappings:
                a, b, delta = map(int, mapping.split())
                if b <= x <= y < b + delta:
                    images.append((x - b + a, y - b + a))
                    break
                if b <= x < b + delta < y:
                    seed_intervals.extend([(x, b + delta - 1), (b + delta, y)])
                    break
            else:
                images.append((x, y))
        seed_intervals = images
    return seed_intervals


with open("data") as f:
    input_seeds, input_maps = f.read().split("\n\n", 1)

from time import time
start = time()
# ========= PART 1 ==========
seed_data = [int(x) for x in re.findall(r"\d+", input_seeds)]
print(min(min(locations([(x, x) for x in seed_data]))))

# ========= PART 2 ==========
seed_intervals = [(x, x + d - 1) for x, d in zip(seed_data[::2], seed_data[1::2])]
print(min(min(locations(seed_intervals))))
print("Elapsed:", round(1000*(time() - start)), "ms")