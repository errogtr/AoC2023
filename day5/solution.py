import re


def locations(intervals):
    for maps_block in input_maps.split("\n\n"):
        mappings = [[int(x) for x in rules.split()] for rules in maps_block.split("\n")[1:]]
        images = list()
        while intervals:
            x, y = intervals.pop()
            for mapping in mappings:
                a, b, delta = mapping
                r_endpoint = b + delta - 1
                if b <= x <= y <= r_endpoint:
                    images.append((x - b + a, y - b + a))
                    break
                elif b <= x <= r_endpoint < y:
                    images.append((x - b + a, r_endpoint - b + a))
                    intervals.append((r_endpoint + 1, y))
                    break
                elif x < b <= y <= r_endpoint:
                    images.append((a, y - b + a))
                    intervals.append((x, b - 1))
                    break
            else:
                images.append((x, y))
        intervals = images
    return intervals


with open("data") as f:
    input_seeds, input_maps = f.read().split("\n\n", 1)

# ========= PART 1 ==========
seed_data = [int(x) for x in re.findall(r"\d+", input_seeds)]
print(min(min(locations([(x, x) for x in seed_data]))))

# ========= PART 2 ==========
seed_intervals = [(x, x + d - 1) for x, d in zip(seed_data[::2], seed_data[1::2])]
print(min(min(locations(seed_intervals))))
