from collections import defaultdict, OrderedDict
import re


def hash(s):
    current = 0
    for c in s:
        current = 17 * (current + ord(c)) % 256
    return current


with open("data") as f:
    sequence = f.read().split(",")

# ==== PART 1 ====
print(sum(hash(s) for s in sequence))

# ==== PART 2 ====
boxes = defaultdict(OrderedDict)
for s in sequence:
    label, op, focal_length = re.match(r"(\w+)(-|=)(\d*)", s).groups()
    box_id = hash(label)
    match op:
        case "=":
            boxes[box_id] |= {label: int(focal_length)}
        case "-":
            _ = boxes[box_id].pop(label, None)

print(
    sum(
        (box_id + 1) * slot * focal_length
        for box_id, box in boxes.items()
        for slot, focal_length in enumerate(box.values(), 1)
    )
)
